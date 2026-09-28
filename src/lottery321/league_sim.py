"""league-world simulator: remaining season -> seeding/play-in -> old & 3-2-1 lotteries -> full
native draft order -> rights routing -> expected slot holdings for every team.

Design notes
* Team index order follows teams.TEAMS (15 East then 15 West) so standings.conference_orders can be
  reused unchanged (sporting tiebreak criteria, point-differential residual = random priority).
* Common random numbers: every world draws one uniform per remaining game plus separate streams for
  the sporting-tie priority, play-in games, draft-tie priority and lottery draws. The forced branches of
  every focal game reuse the same uniforms, so branch differences come only from the forced result.
* Lotteries are SAMPLED (not marginal kernels) because pooled/swap rights depend on the joint draft
  order. Exact kernels in lottery_rules.py are used in tests to validate the samplers.
* Output Q[g, b, r, team, slot] = expected number of draft slots `slot` (1..30, index 0..29) held by
  `team` when focal game g ends with branch b (0 = home wins, 1 = away wins) under rule r (0 = old
  flattened-2019, 1 = 3-2-1). Holdings are after routing through `router`.
"""
import numpy as np

try:
    from teams import TEAMS
    from standings import conference_orders
    from lottery_rules import _count_rule_applies, FLAT_2019_COMBOS, GROUP_BALLS, RELEGATED_FLOOR, feasible, flattened_2019_fast as flattened_2019, sequential_feasible, draw_then_adjust_mc, repair_positions
except ImportError:  # package-style import
    from .teams import TEAMS
    from .standings import conference_orders
    from .lottery_rules import _count_rule_applies, FLAT_2019_COMBOS, GROUP_BALLS, RELEGATED_FLOOR, feasible, flattened_2019_fast as flattened_2019, sequential_feasible, draw_then_adjust_mc, repair_positions

T = {t: i for i, t in enumerate(TEAMS)}
from functools import lru_cache


class OwnRouter:
    """Every native pick stays with its native team."""
    simple_natives = tuple(TEAMS)
    pools = ()

    @staticmethod
    def simple(native, slot):
        return native

    @staticmethod
    def pooled(pos):
        return {}


# ------------------------------------------------------------------ play-in and lottery membership
def playin(orders, u, q):
    """orders: [east, west] best-first. u: 6 uniforms. q[i,j] = P(i beats j) with i at home.
    Returns dict with playoff set and 3-2-1 membership groups."""
    playoffs, non, seeds910, losers78 = set(), [], [], []
    for ci, order in enumerate(orders):
        playoffs.update(order[:6]); non.extend(order[10:]); seeds910.extend(order[8:10])
        a, b, c, d = order[6:10]
        w78, l78 = (a, b) if u[ci * 3] < q[a, b] else (b, a)
        w910 = c if u[ci * 3 + 1] < q[c, d] else d
        eighth = l78 if u[ci * 3 + 2] < q[l78, w910] else w910
        playoffs.update([w78, eighth]); losers78.append(l78)
    return {'playoffs': playoffs, 'nonplayin': non, 'seeds910': seeds910, 'losers78': losers78}


def _ascending(teams, wins, prio):
    """Worst record first; ties by draft-tie priority (lower = earlier)."""
    return sorted(teams, key=lambda t: (wins[t], prio[t]))


# ------------------------------------------------------------------ old (2019-2026) lottery sampler
def old_draft(wins, pl, prio, u):
    """Return list of 30 team indices in draft order (slot 1 first). u: >=5 uniforms."""
    lottery = _ascending([t for t in range(30) if t not in pl['playoffs']], wins, prio)
    if len(lottery) != 14:
        raise ValueError('old lottery needs 14 teams')
    # tied records split their combined combinations; odd remainder to earliest by priority
    combos = [0] * 14; i = 0
    while i < 14:
        j = i
        while j + 1 < 14 and wins[lottery[j + 1]] == wins[lottery[i]]:
            j += 1
        tot = sum(FLAT_2019_COMBOS[i:j + 1]); m = j - i + 1; base, extra = divmod(tot, m)
        for k in range(i, j + 1):
            combos[k] = base + (1 if k - i < extra else 0)
        i = j + 1
    drawn = []
    for d in range(4):
        rem = [k for k in range(14) if k not in drawn]
        w = np.array([combos[k] for k in rem], float); c = np.cumsum(w) / w.sum()
        drawn.append(rem[min(int(np.searchsorted(c, u[d], side='right')), len(rem) - 1)])
    order = [lottery[k] for k in drawn] + [lottery[k] for k in range(14) if k not in drawn]
    rest = _ascending(sorted(pl['playoffs']), wins, prio)
    return order + rest


# ------------------------------------------------------------------ 3-2-1 lottery sampler
def new_draft(wins, pl, prio, u, min_pick=None):
    """3-2-1 draft order (list of 30 team indices). min_pick: {team_index: earliest allowed slot}."""
    min_pick = min_pick or {}
    members = pl['nonplayin'] + pl['seeds910'] + pl['losers78']
    if len(set(members)) != 16:
        raise ValueError('3-2-1 lottery needs 16 distinct teams')
    relegated = set(_ascending(pl['nonplayin'], wins, prio)[:3])  # boundary ties: draft priority (the official text does not say)
    balls = {}
    for t in pl['nonplayin']:
        balls[t] = GROUP_BALLS['bottom3'] if t in relegated else GROUP_BALLS['non_playin']
    for t in pl['seeds910']:
        balls[t] = GROUP_BALLS['playin_9_10']
    for t in pl['losers78']:
        balls[t] = GROUP_BALLS['playin_7_8_losers']
    mx = {t: (RELEGATED_FLOOR if t in relegated else 16) for t in members}
    mn = {t: min_pick.get(t, 1) for t in members}
    restricted = {t for t in members if mn[t] > 1}
    if _count_rule_applies(members, mx, mn, 16):
        restricted = set()   # count rule: must_rel below is then exactly the feasibility condition
    order, rem = [], list(members)
    for pick in range(1, 17):
        n_rel = sum(1 for x in rem if x in relegated)
        must_rel = n_rel > 0 and n_rel >= RELEGATED_FLOOR - pick + 1  # remaining relegated need every slot <= 12
        ok = []
        for t in rem:
            if not (mn[t] <= pick <= mx[t]):
                continue
            if must_rel and t not in relegated:
                continue
            if restricted & (set(rem) - {t}):                     # rare: exact interval check
                if not feasible([x for x in rem if x != t], pick + 1, mx, mn):
                    continue
            ok.append(t)
        w = np.array([balls[t] for t in ok], float); c = np.cumsum(w) / w.sum()
        if not ok:
            raise ValueError(f'3-2-1 draw infeasible at pick {pick}')
        t = ok[min(int(np.searchsorted(c, u[pick - 1], side='right')), len(ok) - 1)]
        order.append(t); rem.remove(t)
    rest = _ascending([t for t in range(30) if t not in members], wins, prio)
    return order + rest


NEW_PROCEDURES = ('sequential_feasible', 'draw_then_adjust')
DTA_KERNEL_DRAWS = 1_000_000
DTA_KERNEL_SEED = 20260922


def _new_field(wins, pl, prio, min_pick):
    """Members, relegated set, balls, floors and minimum slots of the 3-2-1 field."""
    members = pl['nonplayin'] + pl['seeds910'] + pl['losers78']
    relegated = set(_ascending(pl['nonplayin'], wins, prio)[:3])
    balls = {}
    for t in pl['nonplayin']:
        balls[t] = GROUP_BALLS['bottom3'] if t in relegated else GROUP_BALLS['non_playin']
    for t in pl['seeds910']:
        balls[t] = GROUP_BALLS['playin_9_10']
    for t in pl['losers78']:
        balls[t] = GROUP_BALLS['playin_7_8_losers']
    mx = {t: (RELEGATED_FLOOR if t in relegated else 16) for t in members}
    mn = {t: (min_pick or {}).get(t, 1) for t in members}
    return members, relegated, balls, mx, mn


def new_draft_dta(wins, pl, prio, u, min_pick=None):
    """3-2-1 draft order under the draw-then-adjust reading (sensitivity only): an unconstrained
    ball-weighted order of the 16 members (Plackett-Luce via an exponential race with E = -log u),
    then lottery_rules.repair_positions (floors first, then minimum slots); unconstrained teams fill the
    free slots in drawn order. Same repair as lottery_rules.draw_then_adjust_mc."""
    members, relegated, balls, mx, mn = _new_field(wins, pl, prio, min_pick)
    if len(set(members)) != 16:
        raise ValueError('3-2-1 lottery needs 16 distinct teams')
    u = np.clip(np.asarray(u[:16], float), 1e-300, 1.0)
    keys = -np.log(u) / np.array([balls[t] for t in members], float)
    seq = [members[i] for i in np.argsort(keys, kind='stable')]
    cons = [t for t in members if mx[t] < 16 or mn[t] > 1]
    cpos = {t: r + 1 for r, t in enumerate(seq) if t in cons}
    if any(cpos[t] > mx[t] or cpos[t] < mn[t] for t in cpos):
        fixed = repair_positions(cpos, None, None, mx, mn, 16)
        others = [t for t in seq if t not in fixed]
        free = sorted(set(range(1, 17)) - set(fixed.values()))
        slot = dict(fixed); slot.update({t: free[k] for k, t in enumerate(others)})
        seq = sorted(members, key=lambda t: slot[t])
    rest = _ascending([t for t in range(30) if t not in members], wins, prio)
    return seq + rest


# ------------------------------------------------------------------ exact lottery marginals (cached)
@lru_cache(maxsize=4096)
def _old_kernel(combos):
    return np.array(flattened_2019(combos))


def _old_combos(lottery, wins):
    combos = [0] * 14; i = 0
    while i < 14:
        j = i
        while j + 1 < 14 and wins[lottery[j + 1]] == wins[lottery[i]]:
            j += 1
        tot = sum(FLAT_2019_COMBOS[i:j + 1]); m = j - i + 1; base, extra = divmod(tot, m)
        for k in range(i, j + 1):
            combos[k] = base + (1 if k - i < extra else 0)
        i = j + 1
    return tuple(combos)


def old_marginal(wins, pl, prio):
    """Exact M[native, slot] for the old rule given standings (draft-tie priority fixes tie order)."""
    lottery = _ascending([t for t in range(30) if t not in pl['playoffs']], wins, prio)
    K = _old_kernel(_old_combos(lottery, wins)); M = np.zeros((30, 30))
    M[lottery, :14] = K
    for s, t in enumerate(_ascending(sorted(pl['playoffs']), wins, prio)):
        M[t, 14 + s] = 1.0
    return M


@lru_cache(maxsize=512)
def _new_kernel(field):
    """field: tuple of (balls, is_relegated, min_pick) for 16 members (canonical order).
    Returns array (16, 16) of exact pick distributions (sequential_feasible)."""
    names = [f'm{i}' for i in range(len(field))]
    balls = {n: f[0] for n, f in zip(names, field)}
    mx = {n: (RELEGATED_FLOOR if f[1] else 16) for n, f in zip(names, field)}
    mn = {n: f[2] for n, f in zip(names, field)}
    d = sequential_feasible(names, balls, mx, mn)
    return np.array([d[n] for n in names])


@lru_cache(maxsize=512)
def _new_kernel_dta(field):
    """Draw-then-adjust pick distributions for a canonical field, by Monte Carlo with a fixed seed and
    DTA_KERNEL_DRAWS draws (lottery_rules.draw_then_adjust_mc). Deterministic, so both forced branches and
    every world with the same field share one kernel (its MC error is common to both branches)."""
    names = [f'm{i}' for i in range(len(field))]
    balls = {n: f[0] for n, f in zip(names, field)}
    mx = {n: (RELEGATED_FLOOR if f[1] else 16) for n, f in zip(names, field)}
    mn = {n: f[2] for n, f in zip(names, field)}
    d = draw_then_adjust_mc(names, balls, mx, mn, draws=DTA_KERNEL_DRAWS, seed=DTA_KERNEL_SEED)
    K = np.array([d[n] for n in names])
    # exchangeable members (identical labels) get their pooled row, so the kernel stays doubly stochastic
    # when new_marginal assigns one row per label
    for f in set(field):
        idx = [i for i, g in enumerate(field) if g == f]
        K[idx] = K[idx].mean(axis=0)
    return K


def new_marginal(wins, pl, prio, min_pick=None, procedure='sequential_feasible'):
    """Exact M[native, slot] for 3-2-1 given standings, relegation (ties by draft priority) and restrictions."""
    min_pick = min_pick or {}
    members = pl['nonplayin'] + pl['seeds910'] + pl['losers78']
    relegated = set(_ascending(pl['nonplayin'], wins, prio)[:3])
    def label(t):
        b = (GROUP_BALLS['bottom3'] if t in relegated else GROUP_BALLS['non_playin']) if t in pl['nonplayin'] \
            else GROUP_BALLS['playin_9_10'] if t in pl['seeds910'] else GROUP_BALLS['playin_7_8_losers']
        return (b, t in relegated, min_pick.get(t, 1))
    labels = {t: label(t) for t in members}
    field = tuple(sorted(labels.values()))
    K = _new_kernel(field) if procedure == 'sequential_feasible' else _new_kernel_dta(field)
    first = {}
    for i, f in enumerate(field):
        first.setdefault(f, i)
    M = np.zeros((30, 30))
    for t in members:
        M[t, :16] = K[first[labels[t]]]
    for s, t in enumerate(_ascending([t for t in range(30) if t not in members], wins, prio)):
        M[t, 16 + s] = 1.0
    return M


# ------------------------------------------------------------------ remaining-season simulation
N_STATUS = 9
STATUS_OF_RANK = [0, 1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 8, 8, 8, 8]  # conference rank 1..15 -> status class
def simulate(state, focal, n, seed, router=None, min_pick_new=None, sport_mode='criteria',
             lottery_draws=4, batches=50, probs_override=None, use_cache=True,
             new_procedure='sequential_feasible'):
    """state: dict with wins (30), h2h_wins (30x30), h2h_games_final (30x30), remaining [(h,a,p_home)],
    q (30x30 pairwise home-win matrix for play-in). focal: indices into remaining.
    A remaining entry (a, -1, p) is a TBD game of team a against an unknown opponent (p = P(a wins));
    it can never be a focal game.
    router: object with simple_natives, simple(native, slot)->holder, pools, pooled(pos)->{slot: holder};
            None = OwnRouter. Single-pick natives use EXACT lottery marginals; pooled natives are
            routed on `lottery_draws` sampled joint draft orders per world and branch.
    Returns dict with Q (G,2,2,30,30) mean holdings and DB (batches,G,2,30,30) batch means of
    D = holdings(away wins) - holdings(home wins), DB_own the same for own-pick-only portfolios (every
    native holds its own pick: exact lottery marginals, no traded rights), and ST (G,2,30,9): per focal game and branch, the share
    of worlds in which each team ends in status class 0-5 (seed 1-6), 6 (seed 7-8), 7 (seed 9-10),
    8 (seed 11-15). Status does not depend on the lottery rule.
    new_procedure: 3-2-1 joint procedure, 'sequential_feasible' (primary) or 'draw_then_adjust' (sensitivity:
    exact-seed MC kernel for simple natives, draw-then-adjust sampler for pooled natives)."""
    if new_procedure not in NEW_PROCEDURES:
        raise ValueError(f'unknown 3-2-1 procedure {new_procedure}')
    router = router or OwnRouter
    new_sampler = new_draft if new_procedure == 'sequential_feasible' else new_draft_dta
    if n % batches:
        raise ValueError('n must be a multiple of batches')
    rem = state['remaining']; G = len(rem)
    if any(rem[j][1] < 0 for j in focal):
        raise ValueError('a TBD (unknown-opponent) game cannot be focal')
    probs = np.array([p for _, _, p in rem]) if probs_override is None else np.asarray(probs_override, float)
    q = np.asarray(state['q'])
    rng = np.random.default_rng(seed)
    simple_idx = np.array([T[x] for x in router.simple_natives], int)
    HM = np.array([[T[router.simple(TEAMS[nat], s + 1)] for s in range(30)] for nat in simple_idx], int)
    slots = np.broadcast_to(np.arange(30), HM.shape)
    has_pools = bool(router.pools); inv = 1.0 / lottery_draws
    Q = np.zeros((len(focal), 2, 2, 30, 30)); DB = np.zeros((batches, len(focal), 2, 30, 30))
    ST = np.zeros((len(focal), 2, 30, N_STATUS))
    DBo = np.zeros((batches, len(focal), 2, 30, 30))    # own-pick-only portfolios (every native holds its own)
    per = n // batches
    base_w = np.asarray(state['wins'], int); base_h = np.asarray(state['h2h_wins'], int)
    hg = np.asarray(state['h2h_games_final'], int)
    for k in range(n):
        ug = rng.random(G); us = rng.random(30); up = rng.random(6); ud = rng.random(30)
        ul = rng.random((lottery_draws, 16))
        cache = {}
        home_wins = ug < probs
        w = base_w.copy(); h = base_h.copy()
        for j, (a, b, _) in enumerate(rem):
            if b < 0:                      # TBD game vs an unknown opponent: only team a's record is modelled
                w[a] += int(home_wins[j]); continue
            if home_wins[j]:
                w[a] += 1; h[a, b] += 1
            else:
                w[b] += 1; h[b, a] += 1
        H = np.zeros((len(focal), 2, 2, 30, 30)); Ho = np.zeros((len(focal), 2, 2, 30, 30))
        for gi, j in enumerate(focal):
            a, b, _ = rem[j]
            ww = w.copy(); hh = h.copy()
            if home_wins[j]:
                ww[a] -= 1; hh[a, b] -= 1
            else:
                ww[b] -= 1; hh[b, a] -= 1
            for br, (win, lose) in enumerate(((a, b), (b, a))):
                w2 = ww.copy(); h2 = hh.copy(); w2[win] += 1; h2[win, lose] += 1
                orders = conference_orders(w2, h2, hg, us, sport_mode)
                for conf in orders:
                    for rank, t in enumerate(conf):
                        ST[gi, br, t, STATUS_OF_RANK[rank]] += 1.0
                pl = playin(orders, up, q)
                for r in (0, 1):
                    # Within a world every lottery input except (w2, pl) is fixed (prio ud, draws ul, rules), so
                    # branches with the same lottery-relevant state give identical marginals and draft orders.
                    # key: old rule -> exact wins and playoff set (ties split combinations); 3-2-1 -> member
                    # lists in order and the strict (wins, prio) order (new_draft uses nothing else).
                    if r == 0:
                        key = (0, tuple(int(x) for x in w2), tuple(sorted(pl['playoffs'])))
                    else:
                        key = (1, tuple(pl['nonplayin']), tuple(pl['seeds910']), tuple(pl['losers78']),
                               tuple(_ascending(range(30), w2, ud)))
                    hit = cache.get(key) if use_cache else None
                    if hit is None:
                        M = old_marginal(w2, pl, ud) if r == 0 else new_marginal(w2, pl, ud, min_pick_new, new_procedure)
                        pooled = []
                        if has_pools:
                            for kk in range(lottery_draws):
                                order = old_draft(w2, pl, ud, ul[kk]) if r == 0 else new_sampler(w2, pl, ud, ul[kk], min_pick_new)
                                pos = {TEAMS[t]: s + 1 for s, t in enumerate(order)}
                                pooled.extend((T[holder], s - 1) for s, holder in router.pooled(pos).items())
                        hit = (M[simple_idx], pooled, M)
                        if use_cache:
                            cache[key] = hit
                    np.add.at(H[gi, br, r], (HM, slots), hit[0])
                    Ho[gi, br, r] = hit[2]
                    for hi, si in hit[1]:
                        H[gi, br, r, hi, si] += inv
        Q += H
        DB[k // per] += H[:, 1] - H[:, 0]
        DBo[k // per] += Ho[:, 1] - Ho[:, 0]
    return {'Q': Q / n, 'DB': DB / per, 'DB_own': DBo / per, 'ST': ST / n, 'n': n, 'batches': batches, 'lottery_draws': lottery_draws}


def seeding_stake(res, focal_teams):
    """Total-variation distance between a team's end-of-season status distribution after a forced loss and
    after a forced win. focal_teams: [(home, away)] aligned with the focal games. Returns [(home_stake,
    away_stake)]. Branch 0 = home wins, branch 1 = away wins."""
    ST = res['ST']; out = []
    for gi, (h, a) in enumerate(focal_teams):
        tv = lambda t, lose, win: 0.5 * float(np.abs(ST[gi, lose, t] - ST[gi, win, t]).sum())
        out.append((tv(h, 1, 0), tv(a, 0, 1)))
    return out

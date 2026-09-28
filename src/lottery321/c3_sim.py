"""C3 simulator: one set of worlds, every component configuration (C3 registration, sections 1 and 4).

Components: F (3-2-1 field and balls), L (floor at 12), R (repeat restrictions), P (protection ban,
variant 'A' = top-11 or 'B' = top-16). A configuration is a lottery setting (F, L, R) plus a rights setting
(base ledger, ban A, ban B), so the 16 subsets of {F, L, R, P} are covered by 8 x 3 = 24 runs, with the
P-off runs shared by the two ban variants.

The world loop draws exactly the same uniforms, in the same order, as league_sim.simulate, so a C3 run with
the same seed puts every configuration on the primary run's worlds (validated in the tests: the old-rule and
3-2-1 configurations reproduce league_sim.simulate's Q bit for bit).

Stored per state (C3 registration section 4 needs no more than this):
    DOWN[batch, game, config, side, slot]  own-team loss-minus-win slot difference (drives Y1 and Y2)
    ST_[batch, game, config, curve, team]  each team's stake in a home win (drives Y3)
"""
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
for p in (HERE, HERE / 'ledgers'):
    sys.path.insert(0, str(p))

from teams import TEAMS  # noqa: E402
from standings import conference_orders  # noqa: E402
from lottery_rules import GROUP_BALLS, RELEGATED_FLOOR, feasible  # noqa: E402
from league_sim import OwnRouter, T, _ascending, _old_combos, playin  # noqa: E402
from c3_rules import new_kernel_components, old_kernel_components, place_undrawn  # noqa: E402
from value import CURVES  # noqa: E402

CURVE_NAMES = tuple(CURVES)
CURVE_MATRIX = np.array([CURVES[c] for c in CURVE_NAMES])          # (curves, 30)
LOTTERY_SETS = tuple((f, l, r) for f in (0, 1) for l in (0, 1) for r in (0, 1))
RIGHTS = ('base', 'A', 'B')


def config_list():
    """The 24 (lottery, rights) pairs, each with the subset of {F,L,R,P} it represents."""
    out = []
    for f, l, r in LOTTERY_SETS:
        for g in RIGHTS:
            subset = ''.join(k for k, on in (('F', f), ('L', l), ('R', r), ('P', g != 'base')) if on) or '0'
            out.append({'name': f'F{f}L{l}R{r}_{g}', 'field': 'new' if f else 'old', 'floor': bool(l),
                        'restr': bool(r), 'rights': g, 'subset': subset})
    return out


# ------------------------------------------------------------------ exact marginals per configuration
def old_marginal_cfg(wins, pl, prio, min_pick):
    """M[native, slot] for the old lottery, with minimum slots when R is on."""
    lottery = _ascending([t for t in range(30) if t not in pl['playoffs']], wins, prio)
    if len(lottery) != 14:
        raise ValueError('old lottery needs 14 teams')
    mp = {i: min_pick[t] for i, t in enumerate(lottery) if t in min_pick}
    K = np.array(old_kernel_components(_old_combos(lottery, wins), tuple(sorted(mp.items()))))
    M = np.zeros((30, 30))
    M[lottery, :14] = K
    for s, t in enumerate(_ascending(sorted(pl['playoffs']), wins, prio)):
        M[t, 14 + s] = 1.0
    return M


def _new_field(wins, pl, prio, min_pick):
    members = pl['nonplayin'] + pl['seeds910'] + pl['losers78']
    relegated = set(_ascending(pl['nonplayin'], wins, prio)[:3])
    balls = {}
    for t in pl['nonplayin']:
        balls[t] = GROUP_BALLS['bottom3'] if t in relegated else GROUP_BALLS['non_playin']
    for t in pl['seeds910']:
        balls[t] = GROUP_BALLS['playin_9_10']
    for t in pl['losers78']:
        balls[t] = GROUP_BALLS['playin_7_8_losers']
    return members, relegated, balls


def new_marginal_cfg(wins, pl, prio, min_pick, floor):
    """M[native, slot] for the 3-2-1 field, with or without the pick-12 floor."""
    members, relegated, balls = _new_field(wins, pl, prio, min_pick)
    labels = {t: (balls[t], t in relegated, min_pick.get(t, 1)) for t in members}
    field = tuple(sorted(labels.values()))
    K = np.array(new_kernel_components(field, floor))
    first = {}
    for i, f in enumerate(field):
        first.setdefault(f, i)
    M = np.zeros((30, 30))
    for t in members:
        M[t, :16] = K[first[labels[t]]]
    for s, t in enumerate(_ascending([t for t in range(30) if t not in members], wins, prio)):
        M[t, 16 + s] = 1.0
    return M


# ------------------------------------------------------------------ samplers (pooled rights only)
def old_draft_cfg(wins, pl, prio, u, min_pick):
    lottery = _ascending([t for t in range(30) if t not in pl['playoffs']], wins, prio)
    combos = list(_old_combos(lottery, wins))
    mp = {i: min_pick[t] for i, t in enumerate(lottery) if t in min_pick}
    drawn = []
    for d in range(4):
        elig = [k for k in range(14) if k not in drawn and mp.get(k, 1) <= d + 1]
        w = np.array([combos[k] for k in elig], float); c = np.cumsum(w) / w.sum()
        drawn.append(elig[min(int(np.searchsorted(c, u[d], side='right')), len(elig) - 1)])
    order = [None] * 14
    for s, k in enumerate(drawn):
        order[s] = lottery[k]
    for k, s in place_undrawn([k for k in range(14) if k not in drawn], mp).items():
        order[s - 1] = lottery[k]
    return order + _ascending(sorted(pl['playoffs']), wins, prio)


def new_draft_cfg(wins, pl, prio, u, min_pick, floor):
    members, relegated, balls = _new_field(wins, pl, prio, min_pick)
    if len(set(members)) != 16:
        raise ValueError('3-2-1 lottery needs 16 distinct teams')
    mx = {t: (RELEGATED_FLOOR if (floor and t in relegated) else 16) for t in members}
    mn = {t: min_pick.get(t, 1) for t in members}
    order, rem = [], list(members)
    for pick in range(1, 17):
        ok = [t for t in rem if mn[t] <= pick <= mx[t] and feasible([x for x in rem if x != t], pick + 1, mx, mn)]
        if not ok:
            raise ValueError(f'draw infeasible at pick {pick}')
        w = np.array([balls[t] for t in ok], float); c = np.cumsum(w) / w.sum()
        t = ok[min(int(np.searchsorted(c, u[pick - 1], side='right')), len(ok) - 1)]
        order.append(t); rem.remove(t)
    return order + _ascending([t for t in range(30) if t not in members], wins, prio)


# ------------------------------------------------------------------ world loop
def _lottery_key(cf):
    """Distinct lottery settings: under the old field the floor can never bind, so F0L0 and F0L1 share one."""
    return (cf['field'], cf['floor'] if cf['field'] == 'new' else False, cf['restr'])


def holder_tensor(router):
    """A[slot, holder, native] = 1 when `holder` receives `native`'s pick at that slot (simple rights)."""
    A = np.zeros((30, 30, 30))
    for nat in router.simple_natives:
        n = T[nat]
        for s in range(30):
            A[s, T[router.simple(nat, s + 1)], n] = 1.0
    return A


def simulate_c3(state, focal, n, seed, routers, configs=None, min_pick_new=None, batches=50,
                lottery_draws=4, sport_mode='criteria', probs_override=None):
    """routers: {'base': Router, 'A': RouterBanA, 'B': RouterBanB}. Returns DOWN, STK and metadata.
    DOWN: (batches, G, C, 2 sides, 30); STK: (batches, G, C, curves, 30 teams), the value to each team of
    the HOME team winning. Uniform draws follow league_sim.simulate exactly (common random numbers)."""
    configs = configs or config_list()
    min_pick_new = min_pick_new or {}
    rem = state['remaining']; G = len(rem)
    probs = np.array([p for _, _, p in rem]) if probs_override is None else np.asarray(probs_override, float)
    q = np.asarray(state['q']); rng = np.random.default_rng(seed)
    if n % batches:
        raise ValueError('n must be a multiple of batches')
    per = n // batches
    A = {g: holder_tensor(routers[g]) for g in routers}
    pooled_nat = {g: [T[t] for p in routers[g].pools for t in p] for g in routers}
    has_pools = {g: bool(routers[g].pools) for g in routers}
    keys = [_lottery_key(cf) for cf in configs]
    uniq = sorted(set(keys))
    C = len(configs); NF = len(focal)
    DOWN = np.zeros((batches, NF, C, 2, 30)); STK = np.zeros((batches, NF, C, len(CURVE_NAMES), 30))
    base_w = np.asarray(state['wins'], int); base_h = np.asarray(state['h2h_wins'], int)
    hg = np.asarray(state['h2h_games_final'], int)
    for k in range(n):
        ug = rng.random(G); us = rng.random(30); up = rng.random(6); ud = rng.random(30)
        ul = rng.random((lottery_draws, 16))
        home_wins = ug < probs
        w = base_w.copy(); h = base_h.copy()
        for j, (a, b, _) in enumerate(rem):
            if b < 0:
                w[a] += int(home_wins[j]); continue
            if home_wins[j]:
                w[a] += 1; h[a, b] += 1
            else:
                w[b] += 1; h[b, a] += 1
        cache = {}                                   # (lottery setting, world key) -> (M, {rights: pooled})
        H = np.zeros((NF, 2, C, 30, 30))
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
                pl = playin(orders, up, q)
                per_key = {}
                for key in uniq:
                    field, floor, restr = key
                    wkey = ((0, tuple(int(x) for x in w2), tuple(sorted(pl['playoffs']))) if field == 'old'
                            else (1, tuple(pl['nonplayin']), tuple(pl['seeds910']), tuple(pl['losers78']),
                                  tuple(_ascending(range(30), w2, ud))))
                    ck = (key, wkey)
                    hit = cache.get(ck)
                    if hit is None:
                        mp = min_pick_new if restr else {}
                        M = (old_marginal_cfg(w2, pl, ud, mp) if field == 'old'
                             else new_marginal_cfg(w2, pl, ud, mp, floor))
                        pooled = {}
                        if any(has_pools.values()):
                            positions = []
                            for kk in range(lottery_draws):
                                order = (old_draft_cfg(w2, pl, ud, ul[kk], mp) if field == 'old'
                                         else new_draft_cfg(w2, pl, ud, ul[kk], mp, floor))
                                positions.append({TEAMS[t]: s + 1 for s, t in enumerate(order)})
                            for g_ in routers:
                                if not has_pools[g_]:
                                    continue
                                hits = []
                                for pos in positions:
                                    hits += [(T[hol], s - 1) for s, hol in routers[g_].pooled(pos).items()]
                                pooled[g_] = hits
                        hit = (M, pooled)
                        cache[ck] = hit
                    per_key[key] = hit
                for ci, cf in enumerate(configs):
                    M, pooled = per_key[keys[ci]]
                    g_ = cf['rights']
                    Hc = np.einsum('shn,ns->hs', A[g_], M)
                    if has_pools[g_]:
                        Hc[:, :] -= np.einsum('shn,ns->hs', A[g_][:, :, pooled_nat[g_]], M[pooled_nat[g_]])
                        for hi, si in pooled[g_]:
                            Hc[hi, si] += 1.0 / lottery_draws
                    H[gi, br, ci] = Hc
        D = H[:, 1] - H[:, 0]
        bi = k // per
        for gi, j in enumerate(focal):
            hteam, ateam, _ = rem[j]
            DOWN[bi, gi, :, 0] += D[gi, :, hteam]
            DOWN[bi, gi, :, 1] += -D[gi, :, ateam]
        STK[bi] += -np.einsum('gcts,vs->gcvt', D, CURVE_MATRIX)
    DOWN /= per; STK /= per
    return {'DOWN': DOWN, 'STK': STK, 'n': n, 'batches': batches,
            'configs': [c['name'] for c in configs], 'subsets': [c['subset'] for c in configs],
            'curves': list(CURVE_NAMES), 'focal_teams': [(rem[j][0], rem[j][1]) for j in focal]}

"""Exact theory checks: cumulative-difference (Abel) representation of draft incentives.

Objects (all exact, no Monte Carlo)
-----------------------------------
For a team c and a focal game, q_loss(k) / q_win(k) = expected number of first-round slots k (1..30) HELD
by c (after routing native picks through protections / conveyances) when c's focal game is lost / won.

    d(k) = q_loss(k) - q_win(k),     C(j) = sum_{k<=j} d(k)  (j = 1..30),     M = C(30),
    tau(v) = sum_k v(k) d(k)  =  sum_{j=1}^{29} (v(j) - v(j+1)) C(j) + v(30) C(30)      (Abel identity).

Value classes (v indexed by slot, slot 1 most valuable):
    A: v nonincreasing (any sign);  B: nonincreasing and v >= 0;  C: nonincreasing, v >= 0 and v(30) = 0.
With v(1) = 1, tau over class B is a convex combination of C(1..30) (weights v(j)-v(j+1) >= 0 and v(30));
over class C of C(1..29). Hence the sharp bounds are min/max of C over those index sets, attained by the
step functions 1{k <= j}. Dominance (tau >= 0 for every v in the class):
    B  <=>  C(1..30) >= 0;     C  <=>  C(1..29) >= 0;     A  <=>  C(1..29) >= 0 and C(30) == 0.

Lottery rules are NOT re-implemented here: exact marginals come from league_sim.old_marginal / new_marginal
and position kernels from lottery_rules.flattened_2019_fast / sequential_feasible(standard_field()).

Arrays use 0-based indices: C[j-1] is C(j); slot s (1..30) is column s-1; teams are 0..29.
"""
import functools
import itertools

import numpy as np

try:
    from lottery_rules import flattened_2019_fast, sequential_feasible, standard_field
    from league_sim import new_marginal, old_marginal, _ascending
except ImportError:  # package-style import
    from .lottery_rules import flattened_2019_fast, sequential_feasible, standard_field
    from .league_sim import new_marginal, old_marginal, _ascending

N_TEAMS = 30
N_SLOTS = 30
RULES = ('old', 'new')
# 'old_strict' (diagnostic only): the old rule evaluated on strictly ranked records (wins replaced by the
# rank in the (wins, prio) order), i.e. without the official splitting of combinations between tied
# records. The draft ORDER is unchanged; only tied teams' combinations differ. See property_scan.
LOSS, WIN = 0, 1            # branch indices used for d-vectors from a player's own viewpoint


# ====================================================================== 1. Abel algebra
def cumulative(d):
    """C(j) = sum_{k<=j} d(k), returned as an array of the same length as d (C[j-1] = C(j))."""
    return np.cumsum(np.asarray(d, float))


def tau(d, v):
    """tau(v) = sum_k v(k) d(k)."""
    return float(np.dot(np.asarray(v, float), np.asarray(d, float)))


def abel(d, v):
    """Abel (summation-by-parts) form: sum_{j<n} (v(j)-v(j+1)) C(j) + v(n) C(n). Equals tau(d, v)."""
    v = np.asarray(v, float); C = cumulative(d)
    return float(np.dot(v[:-1] - v[1:], C[:-1]) + v[-1] * C[-1])


def _class_index(C, cls):
    n = len(C)
    if cls == 'B':
        return np.arange(n)
    if cls == 'C':
        return np.arange(n - 1)
    raise ValueError("cls must be 'B' or 'C'")


def value_class_bounds(C, cls):
    """Sharp bounds of tau over class `cls` in {'B','C'} with normalization v(1) = 1.
    Returns dict(min, max, argmin_j, argmax_j); j is 1-based and the bound is attained by v = 1{k <= j}."""
    C = np.asarray(C, float); idx = _class_index(C, cls); sub = C[idx]
    lo, hi = int(np.argmin(sub)), int(np.argmax(sub))
    return {'min': float(sub[lo]), 'max': float(sub[hi]), 'argmin_j': int(idx[lo]) + 1, 'argmax_j': int(idx[hi]) + 1}


def dominates(C, cls, tol=1e-12):
    """True iff tau(v) >= 0 for every v in class `cls` in {'A','B','C'} (see module docstring)."""
    C = np.asarray(C, float)
    if cls == 'B':
        return bool(np.all(C >= -tol))
    if cls == 'C':
        return bool(np.all(C[:-1] >= -tol))
    if cls == 'A':
        return bool(np.all(C[:-1] >= -tol) and abs(C[-1]) <= tol)
    raise ValueError("cls must be 'A', 'B' or 'C'")


def step_value(j, n=N_SLOTS):
    """Step value function v(k) = 1{k <= j} (j 1-based), the extreme point of class B / C."""
    return (np.arange(1, n + 1) <= j).astype(float)


# ====================================================================== 2. position kernels
def position_kernels():
    """Exact P(pick = s | draft position r) in a standard tie-free field, for both rules.

    'old': 14 x 14 array from flattened_2019_fast() (row r-1 = lottery position r, worst record = 1;
           columns = picks 1..14).
    'new': 16 x 16 array from sequential_feasible(*standard_field()). standard_field() orders its members
           bottom3 x3 (2 balls, floor 12), non_playin x7 (3 balls), playin_9_10 x4 (2 balls),
           playin_7_8_losers x2 (1 ball), so positions 1-3 are relegated, 4-10 the other non-play-in teams,
           11-14 the 9/10 seeds, 15-16 the 7/8 losers. NOTE: this is a position in the 3-2-1 FIELD, not a
           league-wide record rank (a 9/10 seed can have a worse record than a non-play-in team)."""
    old = np.array(flattened_2019_fast())
    teams, balls, mx, mn = standard_field()
    dist = sequential_feasible(teams, balls, mx, mn)
    new = np.array([dist[t] for t in teams])
    return {'old': old, 'new': new}


def rank_monotone(K, tol=1e-12):
    """FOSD check between adjacent positions: returns the list of violating (r, j) pairs (1-based) where
    P(pick <= j | r) < P(pick <= j | r+1) - tol. An empty list means the rule is rank-monotone."""
    F = np.cumsum(np.asarray(K, float), axis=1)
    return [(r + 1, j + 1) for r in range(F.shape[0] - 1) for j in range(F.shape[1])
            if F[r, j] < F[r + 1, j] - tol]


# ====================================================================== 3. rights (simple routers)
def make_router(rights=None):
    """Build slot_holder(native, slot) -> holder from a dict native -> right (natives not listed keep
    their own pick). Rights (slot is 1-based, P a protection threshold, X the counterparty):
        ('own',)              native keeps
        ('conveyed', X)       X always gets it
        ('protected', P, X)   native keeps if slot <= P, else X gets it
        ('reverse', P, X)     X gets it if slot <= P, else native keeps
    Only simple rights (holder depends on the pick's own slot) are supported; pooled/swap rights need the
    joint draft order and are outside the exact enumerator."""
    rights = dict(rights or {})

    def slot_holder(native, slot):
        r = rights.get(native, ('own',))
        kind = r[0]
        if kind == 'own':
            return native
        if kind == 'conveyed':
            return r[1]
        if kind == 'protected':
            return native if slot <= r[1] else r[2]
        if kind == 'reverse':
            return r[2] if slot <= r[1] else native
        raise ValueError(f'unknown right {r!r}')
    return slot_holder


def holder_matrix(router):
    """R[native, slot-1] = holder index."""
    return np.array([[router(n, s + 1) for s in range(N_SLOTS)] for n in range(N_TEAMS)], int)


# ====================================================================== 3. instances and exact enumerator
NONPLAYIN = tuple(range(10))
SEEDS910 = tuple(range(10, 14))
LOSERS78 = (14, 15)
NEW_OUTSIDE = tuple(range(16, 30))        # the 14 teams outside the 3-2-1 lottery
OLD_PLAYOFFS = tuple(range(14, 30))       # 16 playoff teams under the old rule (7/8 losers qualify)


def standard_layout():
    """Fixed lottery membership used by all instances in this module (documented simplification):
    teams 0-9 = 10 non-play-in teams, 10-13 = play-in 9/10 seeds, 14-15 = 7/8 losers, 16-29 = playoff teams.
    Old rule: playoffs = 14..29 (14-team lottery 0..13). New rule: nonplayin/seeds910/losers78 as above,
    playoffs = 16..29. Membership is given explicitly and does NOT respond to results; instances therefore
    only schedule remaining games for teams 0-9 and 16-29 and keep their records inside their tier (see
    make_instance), so fixed membership is consistent with final standings."""
    pl_old = {'playoffs': set(OLD_PLAYOFFS)}
    pl_new = {'nonplayin': list(NONPLAYIN), 'seeds910': list(SEEDS910), 'losers78': list(LOSERS78),
              'playoffs': set(NEW_OUTSIDE)}
    return pl_old, pl_new


def make_instance(nonplayin_wins, games, rights=None, prio=None, min_pick_new=None, playoff_wins=None):
    """Build a 30-team instance on the standard layout.

    nonplayin_wins: 10 base win totals (before the remaining games) for teams 0-9.
    games: list of (home, away, p_home_win); every team involved must be in 0-9 or 16-29.
    rights: dict for make_router (default: every team owns its pick). prio: draft-tie priority (lower =
    earlier among equal records); default = team index. min_pick_new: 3-2-1 repeat restrictions.
    Seeds 9/10 get 36-39 wins, 7/8 losers 41-42, playoff teams 44-57 (or `playoff_wins`, 14 values).
    Raises if a game could move a non-play-in team out of its tier."""
    w = np.zeros(N_TEAMS, int)
    w[list(NONPLAYIN)] = nonplayin_wins
    w[list(SEEDS910)] = [36, 37, 38, 39]
    w[list(LOSERS78)] = [41, 42]
    w[list(NEW_OUTSIDE)] = playoff_wins if playoff_wins is not None else np.arange(44, 58)
    ng = np.zeros(N_TEAMS, int)
    for h, a, p in games:
        if h == a or not (0 <= p <= 1):
            raise ValueError('bad game')
        for t in (h, a):
            if 10 <= t <= 15:
                raise ValueError('play-in teams cannot have remaining games (membership is fixed)')
            ng[t] += 1
    if max(w[t] + ng[t] for t in NONPLAYIN) >= min(w[t] for t in SEEDS910):
        raise ValueError('a non-play-in team could overtake a play-in team; membership would change')
    pl_old, pl_new = standard_layout()
    return {'wins': w, 'games': list(games), 'pl_old': pl_old, 'pl_new': pl_new,
            'prio': np.arange(N_TEAMS) if prio is None else np.asarray(prio),
            'router': make_router(rights), 'min_pick_new': dict(min_pick_new or {})}


def exact_holdings(inst, rules=RULES):
    """Exact expected holdings for every focal game.

    Enumerates all 2^G joint outcomes of the remaining games once. For focal game f and branch b
    (0 = home LOSES, 1 = home WINS) the outcome weight is the product of the probabilities of the OTHER
    games, so each branch is the exact conditional expectation given the forced focal result.

    Returns {rule: dict(Qn, Q, rel)} with
      Qn[f, b, native, holder, slot] expected holding of slot by holder coming from `native`'s pick,
      Q [f, b, holder, slot]         = Qn summed over natives,
      rel[f, b, team]                probability that team is in the relegated bottom three (3-2-1 only;
                                     zeros for the old rule)."""
    games = inst['games']; G = len(games)
    if G == 0 or G > 10:
        raise ValueError('need 1 <= G <= 10 remaining games')
    R = holder_matrix(inst['router'])
    nat = np.repeat(np.arange(N_TEAMS)[:, None], N_SLOTS, axis=1)
    slot = np.repeat(np.arange(N_SLOTS)[None, :], N_TEAMS, axis=0)
    p = np.array([g[2] for g in games], float)
    out = {r: {'Qn': np.zeros((G, 2, N_TEAMS, N_TEAMS, N_SLOTS)), 'rel': np.zeros((G, 2, N_TEAMS))}
           for r in rules}
    for bits in itertools.product((0, 1), repeat=G):          # bit 1 = home wins
        w = inst['wins'].copy()
        for (h, a, _), b in zip(games, bits):
            w[h if b else a] += 1
        gp = np.where(np.array(bits) == 1, p, 1.0 - p)
        mats = {}
        for r in rules:
            if r == 'old':
                mats[r] = (old_marginal(w, inst['pl_old'], inst['prio']), None)
            elif r == 'old_strict':
                mats[r] = (old_marginal(strict_ranks(w, inst['prio']), inst['pl_old'], inst['prio']), None)
            else:
                M = new_marginal(w, inst['pl_new'], inst['prio'], inst['min_pick_new'])
                rel = list(_ascending(inst['pl_new']['nonplayin'], w, inst['prio'])[:3])
                mats[r] = (M, rel)
        for f in range(G):
            weight = float(np.prod(np.delete(gp, f)))
            if weight == 0.0:
                continue
            b = bits[f]
            for r in rules:
                M, rel = mats[r]
                out[r]['Qn'][f, b][nat, R, slot] += weight * M
                if rel is not None:
                    out[r]['rel'][f, b, rel] += weight
    for r in rules:
        out[r]['Q'] = out[r]['Qn'].sum(axis=2)
    return out


def strict_ranks(wins, prio):
    """Tie-free surrogate records: team t gets its rank (0 = worst) in the (wins, prio) order used by
    league_sim._ascending, so every ordering is preserved but no two records are equal."""
    r = np.empty(N_TEAMS, int)
    r[_ascending(list(range(N_TEAMS)), wins, prio)] = np.arange(N_TEAMS)
    return r


def own_view_d(Q, team, home, away):
    """d(k) for `team` from its own viewpoint in a focal game (home, away): its loss minus its win.
    Q: array [branch(0 = home loses, 1 = home wins), holder, slot] (or per-native [b, native, holder, slot],
    in which case the per-native contributions [native, slot] are returned)."""
    if team == home:
        lose, win = 0, 1
    elif team == away:
        lose, win = 1, 0
    else:
        raise ValueError('team does not play the focal game; choose a branch explicitly')
    Q = np.asarray(Q)
    if Q.ndim == 3:
        return Q[lose, team] - Q[win, team]
    return Q[lose, :, team] - Q[win, :, team]


# ====================================================================== 4. checks
def zero_sum(Q_loss, Q_win, tol=1e-12):
    """Q_loss, Q_win: [team, slot] holdings in two branches. Checks that every slot is held exactly once in
    each branch (column sums = 1) and hence sum_c d_c(k) = 0 for every k. Returns the max abs deviation
    and a bool."""
    Q_loss = np.asarray(Q_loss); Q_win = np.asarray(Q_win)
    dev = max(np.abs(Q_loss.sum(0) - 1).max(), np.abs(Q_win.sum(0) - 1).max(),
              np.abs((Q_loss - Q_win).sum(0)).max())
    return float(dev), bool(dev <= tol)


def asset_decomposition(Qn_loss, Qn_win, team, tol=1e-12):
    """Per-native decomposition d_c = sum_n d_c^(n). Qn_*: [native, holder, slot] in the loss/win branch
    of `team`. Returns (dn [native, slot], d [slot], additive: bool)."""
    dn = np.asarray(Qn_loss)[:, team] - np.asarray(Qn_win)[:, team]
    d = np.asarray(Qn_loss).sum(0)[team] - np.asarray(Qn_win).sum(0)[team]
    return dn, d, bool(np.abs(dn.sum(0) - d).max() <= tol)


# ====================================================================== 5. minimal examples
# Boundary field: non-play-in base wins; teams 2 and 3 are tied at 16 and play each other (game 0), so the
# focal game decides which of them is 3rd/4th worst (old positions 3/4, 3-2-1 relegated / not) without ties.
BOUNDARY_WINS = [10, 12, 16, 16, 20, 22, 24, 26, 28, 30]
A, Y = 2, 3                      # focal player A (home) and its opponent Y (away)
BOUNDARY_GAMES = [(A, Y, 0.5)]
BEST = 29                        # best playoff team (slot 30 in every branch)


def _example(inst, rule, player, focal=0, name='', note=''):
    res = exact_holdings(inst, rules=(rule,))[rule]
    h, a, _ = inst['games'][focal]
    d = own_view_d(res['Q'][focal], player, h, a)
    dn = own_view_d(res['Qn'][focal], player, h, a)
    return {'name': name, 'note': note, 'instance': inst, 'rule': rule, 'player': player, 'focal': focal,
            'd': d, 'dn': dn, 'C': cumulative(d), 'res': res}


def example_e1():
    """E1 (old rule): own unprotected pick. A's loss puts it 3rd worst (140 combos) instead of 4th (125):
    expect all C(j) >= 0 (class-B dominance)."""
    return _example(make_instance(BOUNDARY_WINS, BOUNDARY_GAMES), 'old', A, name='E1',
                    note="A's own pick, old rule, A loses")


def example_e2():
    """E2 (3-2-1): own unprotected pick. A's loss drops it into the relegated bottom three (2 balls, floor
    12) instead of 4th-worst non-play-in (3 balls): expect C(1) < 0 and C(12) > 0 (no class-B dominance)."""
    return _example(make_instance(BOUNDARY_WINS, BOUNDARY_GAMES), 'new', A, name='E2',
                    note="A's own pick, 3-2-1, A loses")


def example_e3(rule='new', P=4):
    """E3: A holds Y's pick protected top-P (Y keeps if slot <= P, A gets it otherwise) and plays Y.
    A's own loss is forced; it makes Y win. Under 3-2-1 Y's win lifts Y OUT of the relegated bottom three,
    which RAISES P(Y slot <= P) for small P, so A is less likely to receive the pick: M = C(30) < 0.
    A's own pick contributes zero to M (A holds it in both branches). A holds no slot beyond 16, so
    C(29) = C(30) = M < 0 and class C fails as well. Under the old rule the same portfolio gives M > 0."""
    inst = make_instance(BOUNDARY_WINS, BOUNDARY_GAMES, rights={Y: ('protected', P, A)})
    return _example(inst, rule, A, name='E3', note=f"A holds Y's top-{P}-protected pick; A loses to Y")


def example_e4(rule='old'):
    """E4 (old rule): the best team (29) holds its opponent's (team 3) unprotected pick and plays it. Its
    own pick is slot 30 in both branches. Its loss makes team 3 win (17 wins, 4th worst alone) instead of
    tying team 2 at 16 (split 140+125 combinations; team 2 earlier by priority). Expect all C(j) <= 0.
    The tie in the win branch is unavoidable with one game and integer records; old_marginal splits the
    combinations exactly."""
    inst = make_instance(BOUNDARY_WINS[:3] + [16] + BOUNDARY_WINS[4:], [(BEST, Y, 0.6)],
                         rights={Y: ('conveyed', BEST)}, playoff_wins=np.arange(44, 58).tolist()[:-1] + [60])
    return _example(inst, rule, BEST, name='E4', note="best team holds opponent 3's pick; best team loses")


def example_e5(P_min=6):
    """E5 (3-2-1): E2 with a repeat restriction min_pick = P_min for A: own-pick C(j) = 0 for j < P_min."""
    inst = make_instance(BOUNDARY_WINS, BOUNDARY_GAMES, min_pick_new={A: P_min})
    return _example(inst, 'new', A, name='E5', note=f"A's own pick, 3-2-1, min_pick={P_min}, A loses")


def example_e6(P=4, X=20):
    """E6 (old rule): A's own pick protected top-P (A keeps if slot <= P, else conveyed to X). A's loss
    raises P(slot <= P): C(j) >= 0 for all j (class B holds) and M = C(P) > 0, so class A fails."""
    inst = make_instance(BOUNDARY_WINS, BOUNDARY_GAMES, rights={A: ('protected', P, X)})
    return _example(inst, 'old', A, name='E6', note=f"A's own pick top-{P} protected to {X}; A loses")


def all_examples():
    return [example_e1(), example_e2(), example_e3(), example_e4(), example_e5(), example_e6()]


# ====================================================================== 6. randomized property test
def random_instance(rng, g_max=6):
    """Random own-pick-only instance: tight non-play-in records (ties frequent), 2..g_max remaining games
    among teams 0-9 and four playoff teams (26-29), random probabilities and random draft-tie priority."""
    wins = rng.integers(18, 25, size=10).tolist()
    pool = list(NONPLAYIN) + [26, 27, 28, 29]
    G = int(rng.integers(2, g_max + 1)); games = []
    for _ in range(G):
        h, a = rng.choice(pool, size=2, replace=False)
        games.append((int(h), int(a), float(rng.uniform(0.2, 0.8))))
    return make_instance(wins, games, prio=rng.permutation(N_TEAMS))


def property_scan(n_instances=200, seed=20260921, g_max=6, tol=1e-12):
    """For random own-pick-only instances, compute every focal player's C under the old rule, its tie-free
    diagnostic 'old_strict' and 3-2-1. Returns dict with counts and lists of cases:
      old_violations: cases with some C(j) < -tol under the OFFICIAL old rule. FINDING: these exist
                      (seed 20260921: 42 of 1622 player cases, min C = -0.0014). Mechanism (verified on
                      instance 1, focal game 2, team 5): the player's own rank and combinations do not change,
                      but its opponent's win moves the opponent into a tie group whose combinations are
                      then split evenly; a more equal spread of the rivals' combinations lowers the player's
                      chance of a top-4 draw (e.g. rivals 140/99/99/99/98 -> 107 x 5). So the old rule is
                      rank-monotone only for strict records; tie splitting breaks own-pick dominance;
      old_strict_violations: same on strict records (expected and observed: none);
      new_violations: same under 3-2-1, each with a flag whether the team's relegation probability differs
                      between its loss and win branch (the relegation-boundary mechanism);
      max_zero_sum_dev: largest zero-sum deviation over all instances/focal games/rules."""
    rng = np.random.default_rng(seed)
    rules = ('old', 'old_strict', 'new')
    out = {'n_instances': n_instances, 'n_player_cases': 0, 'old_violations': [], 'old_strict_violations': [],
           'new_violations': [], 'max_zero_sum_dev': 0.0}
    for i in range(n_instances):
        inst = random_instance(rng, g_max)
        res = exact_holdings(inst, rules)
        for f, (h, a, _) in enumerate(inst['games']):
            for r in rules:
                dev, _ = zero_sum(res[r]['Q'][f, 0], res[r]['Q'][f, 1])
                out['max_zero_sum_dev'] = max(out['max_zero_sum_dev'], dev)
            for c in (h, a):
                out['n_player_cases'] += 1
                lose = 0 if c == h else 1
                for r in rules:
                    C = cumulative(own_view_d(res[r]['Q'][f], c, h, a))
                    if C.min() < -tol:
                        rec = {'instance': i, 'focal': f, 'team': c, 'minC': float(C.min()),
                               'argmin_j': int(C.argmin()) + 1}
                        if r == 'new':
                            rel = res[r]['rel'][f]
                            rec['rel_loss'] = float(rel[lose, c]); rec['rel_win'] = float(rel[1 - lose, c])
                            rec['relegation_boundary'] = bool(rel[lose, c] > rel[1 - lose, c] + tol)
                        out[r + '_violations'].append(rec)
    return out


# ====================================================================== 7. position-boundary decomposition
# Theorem (paper Section 3.3). Under (i) fixed lottery membership, (ii) strict records
# (draft order and lottery weights depend only on the strict (wins, prio) order), (iii) a position-only
# kernel (a native's slot distribution depends only on its own position, not on who else is where) and
# (iv) simple rights h_{n->c}(k), the player's cumulative difference satisfies exactly
#     C_c(j) = sum_n sum_{r=1}^{29} dPi_n(r) * G_{n->c,r}(j),
#     dPi_n(r) = P(pos_n <= r | player loses) - P(pos_n <= r | player wins),
#     G_{n->c,r}(j) = sum_{k<=j} h_{n->c}(k) [K_r(k) - K_{r+1}(k)],
# where K_r(k) = P(slot = k | position r). Coupling lemma: dPi_player >= 0 and dPi_opponent <= 0; a third party's sign is not determined.

@functools.lru_cache(maxsize=4)
def _full_kernel_cached(rule):
    return _full_kernel(rule)


def full_kernel(rule):
    """Cached copy of _full_kernel (see there)."""
    return _full_kernel_cached(rule).copy()


def _full_kernel(rule):
    """30 x 30 kernel K[r-1, k-1] = P(slot k | global position r) on the standard layout (positions by
    ascending (wins, prio) over all 30 teams). 'old'/'old_strict': 14-team lottery for positions 1-14,
    positions 15-30 get slot = position. 'new': 16-member 3-2-1 field for positions 1-16 (1-3 relegated),
    positions 17-30 get slot = position. Valid only when the layout's tiers are ordered by record, which
    make_instance guarantees."""
    ker = position_kernels()
    K = np.zeros((N_SLOTS, N_SLOTS))
    base = ker['new'] if rule == 'new' else ker['old']
    m = base.shape[0]
    K[:m, :m] = base
    for r in range(m, N_SLOTS):
        K[r, r] = 1.0
    return K


def exact_positions(inst):
    """pi[f, b, team, r-1] = P(global position of team = r | focal f forced to branch b) with b = 0 home
    loses, 1 home wins (same enumeration as exact_holdings). Positions use the strict (wins, prio) order."""
    games = inst['games']; G = len(games)
    p = np.array([g[2] for g in games], float)
    pi = np.zeros((G, 2, N_TEAMS, N_SLOTS))
    for bits in itertools.product((0, 1), repeat=G):
        w = inst['wins'].copy()
        for (h, a, _), b in zip(games, bits):
            w[h if b else a] += 1
        gp = np.where(np.array(bits) == 1, p, 1.0 - p)
        order = _ascending(list(range(N_TEAMS)), w, inst['prio'])
        for f in range(G):
            weight = float(np.prod(np.delete(gp, f)))
            if weight:
                pi[f, bits[f], order, np.arange(N_TEAMS)] += weight
    return pi


def boundary_decomposition(inst, rule, focal, player):
    """Predicted C_c(j) from the theorem, plus its per-(native, boundary) terms.
    Returns dict(C_pred [30], dPi [native, r], terms [native, r, j] (cumulative contributions),
    negative_terms: list of (native, r, min over j of term) with a negative minimum)."""
    h, a, _ = inst['games'][focal]
    lose = 0 if player == h else 1
    if player not in (h, a):
        raise ValueError('player must play the focal game')
    pi = exact_positions(inst)[focal]
    dPi = np.cumsum(pi[lose] - pi[1 - lose], axis=1)            # [native, r]
    K = full_kernel(rule)
    R = holder_matrix(inst['router'])
    gap = K[:-1] - K[1:]                                          # [r (1..29), k]
    terms = np.zeros((N_TEAMS, N_SLOTS - 1, N_SLOTS))
    for n in range(N_TEAMS):
        held = (R[n] == player).astype(float)                    # h_{n->player}(k)
        if not held.any():
            continue
        terms[n] = dPi[n, :-1, None] * np.cumsum(gap * held[None, :], axis=1)
    C_pred = terms.sum(axis=(0, 1))
    neg = [(n, r + 1, float(terms[n, r].min())) for n in range(N_TEAMS) for r in range(N_SLOTS - 1)
           if terms[n, r].min() < -1e-12]
    return {'C_pred': C_pred, 'dPi': dPi, 'terms': terms, 'negative_terms': neg}

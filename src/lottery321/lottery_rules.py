"""rule engine v2: exact 3-2-1 lottery distributions (no Monte Carlo).

Teams are drawn one at a time without replacement, weighted by lottery balls, for picks 1..16.
Constraints per team: `max_pick` (pick floor, e.g. relegated teams <= 12) and `min_pick`
(repeat restrictions: can't be #1 -> min_pick 2; can't be top-5 -> min_pick 6).

Two candidate joint procedures (the official release does not fully specify the joint operation):
  * 'sequential_feasible': at each pick, draw only among teams whose selection keeps a feasible
    completion (all floors/mins satisfiable), weighted by balls.
  * 'draw_then_adjust': draw an unconstrained weighted order, then repair: teams violating min_pick
    are pushed down to the earliest allowed slot and teams violating floors moved up to the latest
    allowed slot, preserving relative draw order among the rest (a common reading of floors).
Exact computation via dynamic programming over subsets (2^16 states).
"""
from functools import lru_cache
from itertools import permutations

GROUP_BALLS = {'bottom3': 2, 'non_playin': 3, 'playin_9_10': 2, 'playin_7_8_losers': 1}
RELEGATED_FLOOR = 12
N_LOTTERY = 16


def _count_rule_applies(remaining, max_pick, min_pick, n):
    """True when every constraint is one of: max_pick in {floor, n} with one common floor, and min_pick
    <= 6 for at most 2 teams (the 3-2-1 relegation floor plus native repeat restrictions). Then Hall's
    condition reduces to counting the floored teams (proof in the paper's online appendix; checked against the
    exact test in tests/lottery321/test_lottery_rules.py)."""
    floors = {max_pick[t] for t in remaining if max_pick[t] < n}
    restricted = [t for t in remaining if min_pick[t] > 1]
    return len(floors) <= 1 and len(restricted) <= 2 and all(min_pick[t] <= 6 for t in restricted) and \
        (not floors or min(floors) >= 12)


def feasible(remaining, next_pick, max_pick, min_pick, n=N_LOTTERY):
    """Fast path for the 3-2-1 constraint family (see _count_rule_applies), else the exact Hall check."""
    if len(remaining) != n - next_pick + 1:
        return False
    if _count_rule_applies(remaining, max_pick, min_pick, n):
        for t in remaining:
            if max(min_pick[t], next_pick) > min(max_pick[t], n):
                return False
        floored = [t for t in remaining if max_pick[t] < n]
        return not floored or len(floored) <= max_pick[floored[0]] - next_pick + 1
    return feasible_hall(remaining, next_pick, max_pick, min_pick, n)


def feasible_hall(remaining, next_pick, max_pick, min_pick, n=N_LOTTERY):
    """Can `remaining` teams fill picks next_pick..n (one team per pick) respecting max/min?
    Exact via Hall's theorem for interval (convex) bipartite graphs: a perfect matching exists iff the counts
    match and, for every slot interval [a, b] with a a team lower end and b a team upper end, at most b-a+1
    teams have their whole allowed interval inside [a, b]. (Cross-checked against a greedy
    scan in tests/lottery321/test_lottery_rules.py.)"""
    k = len(remaining)
    if k != n - next_pick + 1:
        return False
    iv = []
    for t in remaining:
        lo = max(min_pick[t], next_pick); hi = min(max_pick[t], n)
        if lo > hi:
            return False
        iv.append((lo, hi))
    los = set(x for x, _ in iv); his = set(y for _, y in iv)
    for a in los:
        for b in his:
            if a <= b and sum(1 for lo, hi in iv if lo >= a and hi <= b) > b - a + 1:
                return False
    return True


def feasible_greedy(remaining, next_pick, max_pick, min_pick, n=N_LOTTERY):
    """Reference implementation (earliest-deadline greedy), kept for cross-checking only."""
    teams = sorted(remaining, key=lambda t: (max_pick[t], min_pick[t]))
    slots = list(range(next_pick, n + 1))
    used = set()
    # earliest-deadline-first: for each slot in order, assign the available team with smallest max_pick
    avail = list(remaining)
    for s in slots:
        cands = [t for t in avail if min_pick[t] <= s]
        if not cands:
            return False
        t = min(cands, key=lambda u: (max_pick[u], min_pick[u], u))
        if max_pick[t] < s:
            return False
        avail.remove(t)
    return not avail


def sequential_feasible(teams, balls, max_pick, min_pick, n=N_LOTTERY, force_exact=False):
    """Return {team: [P(pick=1..n)]} exactly. force_exact=True disables the count-rule shortcut (tests)."""
    idx = {t: i for i, t in enumerate(teams)}
    full = (1 << len(teams)) - 1
    prob = {0: 1.0}
    out = {t: [0.0] * n for t in teams}
    # iterate by number drawn
    layer = {0: 1.0}
    # 3-2-1 constraint family: choosing t keeps a feasible completion iff the floored teams left after t
    # fit into the slots up to the floor (see feasible / _count_rule_applies); decided per state, no search.
    fast = _count_rule_applies(teams, max_pick, min_pick, n) and not force_exact
    floor = min([max_pick[t] for t in teams if max_pick[t] < n], default=n)
    for pick in range(1, n + 1):
        nxt = {}
        for mask, p in layer.items():
            rem = [t for t in teams if not mask >> idx[t] & 1]
            ok = []
            if fast:
                n_fl = sum(1 for t in rem if max_pick[t] < n)
                for t in rem:
                    if min_pick[t] <= pick <= max_pick[t] and n_fl - (max_pick[t] < n) <= max(0, floor - pick):
                        ok.append(t)
            else:
                for t in rem:
                    if min_pick[t] > pick or max_pick[t] < pick:
                        continue
                    rest = [u for u in rem if u != t]
                    if feasible(rest, pick + 1, max_pick, min_pick, n):
                        ok.append(t)
            if not ok:
                raise ValueError(f'infeasible state at pick {pick}')
            tot = sum(balls[t] for t in ok)
            for t in ok:
                q = p * balls[t] / tot
                out[t][pick - 1] += q
                m2 = mask | 1 << idx[t]
                nxt[m2] = nxt.get(m2, 0.0) + q
        layer = nxt
    return out


def draw_then_adjust_mc(teams, balls, max_pick, min_pick, n=N_LOTTERY, draws=2_000_000, seed=20260921):
    """Comparison-only Monte Carlo for the draw-then-repair reading (exact DP is impractical because the
    repair depends on the full order). Returns {team: [P(pick)]} and is NOT used for production values."""
    import numpy as np
    rng = np.random.default_rng(seed)
    w = np.array([balls[t] for t in teams], float)
    # Plackett-Luce sampling via exponential race: key = E / w, sort ascending
    keys = rng.exponential(size=(draws, len(teams))) / w
    order = np.argsort(keys, axis=1)            # order[:, r] = team index drawn at pick r+1
    pos = np.empty_like(order); rows = np.arange(draws)[:, None]
    pos[rows, order] = np.arange(1, len(teams) + 1)
    out = {t: np.zeros(n) for t in teams}
    cons = [i for i, t in enumerate(teams) if max_pick[t] < n or min_pick[t] > 1]
    # vectorised repair is complex; do it per draw only where a violation exists
    viol = np.zeros(draws, bool)
    for i in cons:
        viol |= (pos[:, i] > max_pick[teams[i]]) | (pos[:, i] < min_pick[teams[i]])
    for d in np.nonzero(viol)[0]:
        seq = [teams[i] for i in order[d]]
        cpos = {t: r + 1 for r, t in enumerate(seq) if teams.index(t) in cons}
        fixed = repair_positions(cpos, None, None, max_pick, min_pick, n)
        others = [t for t in seq if t not in fixed]
        free = sorted(set(range(1, n + 1)) - set(fixed.values()))
        new = dict(fixed); new.update({t: free[k] for k, t in enumerate(others)})
        for i, t in enumerate(teams):
            pos[d, i] = new[t]
    for i, t in enumerate(teams):
        out[t] = np.bincount(pos[:, i], minlength=n + 1)[1:] / draws
    return {t: list(v) for t, v in out.items()}


def repair_positions(pos, constrained, others, max_pick, min_pick, n):
    """Given drawn positions of constrained teams (in a full unconstrained order), apply floors then mins.
    Floors: violators move up to the latest slots <= floor not already taken by earlier-drawn relegated,
    in their drawn order. Mins: violators move down to the earliest allowed slot."""
    pos = dict(pos)
    # floors (process in drawn order)
    for t in sorted(pos, key=lambda u: pos[u]):
        if pos[t] > max_pick[t]:
            taken = {pos[u] for u in pos if u != t}
            s = max(s for s in range(1, max_pick[t] + 1) if s not in taken)
            pos[t] = s
    for t in sorted(pos, key=lambda u: pos[u]):
        if pos[t] < min_pick[t]:
            taken = {pos[u] for u in pos if u != t}
            s = min(s for s in range(min_pick[t], n + 1) if s not in taken)
            pos[t] = s
    return pos


def weighted_rank_dist(teams, balls):
    """Exact distribution of rank among `teams` under weighted draw without replacement."""
    idx = {t: i for i, t in enumerate(teams)}
    out = {t: [0.0] * len(teams) for t in teams}
    layer = {0: 1.0}
    for r in range(len(teams)):
        nxt = {}
        for mask, p in layer.items():
            rem = [t for t in teams if not mask >> idx[t] & 1]
            tot = sum(balls[t] for t in rem)
            for t in rem:
                q = p * balls[t] / tot
                out[t][r] += q
                m2 = mask | 1 << idx[t]
                nxt[m2] = nxt.get(m2, 0.0) + q
        layer = nxt
    return out


def standard_field(restrict=None):
    """16-team field: 3 bottom3, 7 non_playin, 4 playin_9_10, 2 losers. Returns teams, balls, max, min."""
    groups = ['bottom3'] * 3 + ['non_playin'] * 7 + ['playin_9_10'] * 4 + ['playin_7_8_losers'] * 2
    teams = [f'{g}_{i}' for i, g in enumerate(groups)]
    balls = {t: GROUP_BALLS[t.rsplit('_', 1)[0]] for t in teams}
    mx = {t: (RELEGATED_FLOOR if t.startswith('bottom3') else N_LOTTERY) for t in teams}
    mn = {t: 1 for t in teams}
    for t, m in (restrict or {}).items():
        mn[t] = m
    return teams, balls, mx, mn


# ---------------------------------------------------------------------------------------------
# Flattened-odds lottery used for the 2019-2026 drafts (the old rule in the paper).
FLAT_2019_COMBOS = (140, 140, 140, 125, 105, 90, 75, 60, 45, 30, 20, 15, 10, 5)  # per 1000, worst first
FLAT_2019_DRAWS = 4


def flattened_2019(combos=FLAT_2019_COMBOS, draws=FLAT_2019_DRAWS):
    """Exact pick distribution for the 14 lottery teams (index 0 = worst record).
    Top `draws` picks drawn by combination weight without replacement; the rest in reverse record order.
    Returns list of 14 lists P(pick 1..14). Tie-splitting of combinations is applied upstream by
    passing already-split combination counts."""
    n = len(combos)
    out = [[0.0] * n for _ in range(n)]

    def rec(drawn, p):
        k = len(drawn)
        if k == draws:
            rest = [i for i in range(n) if i not in drawn]
            for r, i in enumerate(rest):
                out[i][draws + r] += p
            return
        rem = [i for i in range(n) if i not in drawn]
        tot = sum(combos[i] for i in rem)
        for i in rem:
            q = p * combos[i] / tot
            out[i][k] += q
            rec(drawn + (i,), q)

    rec((), 1.0)
    return out


def flattened_2019_fast(combos=FLAT_2019_COMBOS, draws=FLAT_2019_DRAWS):
    """Same result as flattened_2019, via dynamic programming over drawn SETS (<=1471 states for 14 teams,
    4 draws) instead of enumerating ordered draws (24,024 paths). Tested for equality."""
    n = len(combos); W = float(sum(combos))
    out = [[0.0] * n for _ in range(n)]
    level = {0: 1.0}                     # bitmask of drawn teams -> probability
    for d in range(draws):
        nxt = {}
        for mask, p in level.items():
            wm = sum(combos[i] for i in range(n) if mask >> i & 1)
            rest = W - wm
            for i in range(n):
                if mask >> i & 1:
                    continue
                q = p * combos[i] / rest
                out[i][d] += q
                m2 = mask | 1 << i
                nxt[m2] = nxt.get(m2, 0.0) + q
        level = nxt
    for mask, p in level.items():         # undrawn teams keep record order after the drawn picks
        r = draws
        for i in range(n):
            if not mask >> i & 1:
                out[i][r] += p; r += 1
    return out

"""C3 component engine: lottery kernels for every subset of the 3-2-1 components (C3 registration, section 1).

Components: F (3-2-1 field and ball counts), L (floor at pick 12 for the three worst), R (repeat
restrictions). P (protection ban) is a rights change and lives in protection_ban.py, not here.

  F off -> the 2019-2026 flattened lottery: 14 teams, combinations 140..5, top 4 drawn, the rest by record.
  F on  -> the 3-2-1 field: 16 teams, 2/3/2/1 balls, all 16 picks drawn (lottery_rules.sequential_feasible).
  L     -> max_pick 12 for the three worst records (with F off it can never bind: the worst team cannot
           fall below 5th, so the kernel is unchanged; this is computed, not assumed).
  R     -> minimum slots from the repeat restrictions.

With F off and R on, the old lottery needs a definition, fixed in the C3 registration:
  * in each of the four draws a restricted team is not eligible for a pick earlier than its minimum slot,
    and the draw is made among the eligible teams weighted by combinations;
  * slots 5..14 are then filled in record order, skipping a team whose minimum exceeds the current slot;
    a skipped team takes the first later slot it is allowed.
"""
import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lottery_rules import (FLAT_2019_COMBOS, FLAT_2019_DRAWS, GROUP_BALLS, N_LOTTERY,  # noqa: E402
                       RELEGATED_FLOOR, flattened_2019_fast, sequential_feasible)

COMPONENTS = ('F', 'L', 'R', 'P')


def place_undrawn(undrawn, min_pick, draws=FLAT_2019_DRAWS, n=14):
    """Fill slots draws+1..n with the undrawn teams in record order, respecting minimum slots.
    `undrawn` is a list of team indices in record order (worst first). Returns {team: slot}."""
    free = list(range(draws + 1, n + 1))
    rest = list(undrawn)
    out = {}
    for s in free:
        pick = None
        for k, t in enumerate(rest):
            if min_pick.get(t, 1) <= s:
                pick = k
                break
        if pick is None:
            raise ValueError('no eligible team for slot %d' % s)
        out[rest.pop(pick)] = s
    return out


def flattened_2019_restricted(combos=FLAT_2019_COMBOS, min_pick=None, draws=FLAT_2019_DRAWS):
    """Exact slot distribution (14 x 14) for the old lottery with minimum slots. min_pick maps the
    lottery index (0 = worst record) to the earliest allowed slot. Equals flattened_2019_fast when empty."""
    min_pick = dict(min_pick or {})
    if not min_pick:
        return flattened_2019_fast(combos, draws)
    n = len(combos)
    out = [[0.0] * n for _ in range(n)]
    level = {0: 1.0}
    for d in range(draws):
        pick = d + 1
        nxt = {}
        for mask, p in level.items():
            elig = [i for i in range(n) if not mask >> i & 1 and min_pick.get(i, 1) <= pick]
            w = float(sum(combos[i] for i in elig))
            if w <= 0:
                raise ValueError('no eligible team for draw %d' % pick)
            for i in elig:
                q = p * combos[i] / w
                out[i][d] += q
                m2 = mask | 1 << i
                nxt[m2] = nxt.get(m2, 0.0) + q
        level = nxt
    for mask, p in level.items():
        undrawn = [i for i in range(n) if not mask >> i & 1]
        for t, s in place_undrawn(undrawn, min_pick, draws, n).items():
            out[t][s - 1] += p
    return out


@lru_cache(maxsize=2048)
def new_kernel_components(field, floor=True):
    """3-2-1 kernel for a canonical field with or without the floor.
    field: tuple of (balls, is_relegated, min_pick) for the 16 members, sorted."""
    names = [f'm{i}' for i in range(len(field))]
    balls = {n_: f[0] for n_, f in zip(names, field)}
    mx = {n_: (RELEGATED_FLOOR if (floor and f[1]) else N_LOTTERY) for n_, f in zip(names, field)}
    mn = {n_: f[2] for n_, f in zip(names, field)}
    d = sequential_feasible(names, balls, mx, mn)
    return tuple(tuple(d[n_]) for n_ in names)


@lru_cache(maxsize=4096)
def old_kernel_components(combos, min_pick_items):
    """Old-rule kernel with optional minimum slots. min_pick_items is a sorted tuple of (index, slot)."""
    return tuple(tuple(r) for r in flattened_2019_restricted(combos, dict(min_pick_items)))

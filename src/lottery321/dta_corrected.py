"""Corrected repair for the draw-then-adjust reading of the 3-2-1 draw (run tag `dta2`).

The reading (lottery_rules module header; Online Appendix E.3): draw an unconstrained ball-weighted order of the
16 lottery teams, then repair it. A team drawn before its earliest allowed slot (repeat restriction) goes
down to the earliest allowed slot; a relegated team drawn after the floor (12) goes up to the latest allowed
slot; every other team keeps its drawn order.

The repair used by the first draw-then-adjust run (lottery_rules.repair_positions) held every constrained team
at its drawn slot while another constrained team was being moved. A team with a repeat restriction was
therefore never pushed back when a relegated team moved ahead of it, and a relegated team never moved up when
a restricted team moved down past it. Example: U, X, B drawn 11th, 12th, 13th, where X may not pick first
and B is relegated; the first run gave B, X, U, the reading gives U, B, X. With the floor alone (no repeat
restriction in the field) the two repairs give the same distribution. Online Appendix I.6 (amendment 18) reports the size of the difference.

This module does not change lottery_rules.py or league_sim.py (both are kept as used in the registered runs). `install()`
replaces the two draw-then-adjust entry points of league_sim in the running process, so that
league_sim.simulate(..., new_procedure='draw_then_adjust') uses the corrected repair. run_simulation.py calls
it for the `dta2` variant only.
"""
from functools import lru_cache

import numpy as np

try:
    import league_sim as S
    from lottery_rules import RELEGATED_FLOOR
except ImportError:                                   # package import
    from . import league_sim as S
    from .lottery_rules import RELEGATED_FLOOR

REPAIR_LABEL = 'order-preserving repair (dta_corrected.repair_order)'


def repair_order(seq, max_pick, min_pick, n=None):
    """Final order of a drawn order `seq` (list of teams, first drawn first).

    Fill slots 1..n in turn. When the floored teams not yet placed need every remaining slot up to their
    floor, take the earliest-drawn of them; otherwise take the earliest-drawn remaining team allowed at this
    slot. Hence a team below its minimum lands on its earliest allowed slot, a floored team drawn too late
    on the latest allowed slot, and all other teams keep their drawn order. Assumes one common floor and
    minimum slots below it (the 3-2-1 scenario: floor 12, minimum slots 2 or 6)."""
    n = len(seq) if n is None else n
    rem = list(seq)
    out = []
    for s in range(1, n + 1):
        fl = [t for t in rem if max_pick[t] < n]
        if fl and len(fl) >= min(max_pick[t] for t in fl) - s + 1:
            cand = [u for u in fl if min_pick[u] <= s]
        else:
            cand = [u for u in rem if min_pick[u] <= s <= max_pick[u]]
        if not cand:
            raise ValueError(f'no team can take slot {s}')
        t = cand[0]
        out.append(t)
        rem.remove(t)
    return out


def _needs_repair(seq, max_pick, min_pick):
    return any(not (min_pick[t] <= r + 1 <= max_pick[t]) for r, t in enumerate(seq))


def draw_then_adjust_mc(teams, balls, max_pick, min_pick, n=16, draws=2_000_000, seed=20260921):
    """Slot distributions {team: [P(slot 1..n)]} under the reading, by Monte Carlo (Plackett-Luce draws
    via an exponential race, the same random numbers as lottery_rules.draw_then_adjust_mc for a given seed)."""
    rng = np.random.default_rng(seed)
    w = np.array([balls[t] for t in teams], float)
    keys = rng.exponential(size=(draws, len(teams))) / w
    order = np.argsort(keys, axis=1)
    pos = np.empty_like(order)
    rows = np.arange(draws)[:, None]
    pos[rows, order] = np.arange(1, len(teams) + 1)
    lo = np.array([min_pick[t] for t in teams]); hi = np.array([max_pick[t] for t in teams])
    viol = ((pos < lo) | (pos > hi)).any(axis=1)
    idx = {t: i for i, t in enumerate(teams)}
    for d in np.nonzero(viol)[0]:
        seq = [teams[i] for i in order[d]]
        for s, t in enumerate(repair_order(seq, max_pick, min_pick, n)):
            pos[d, idx[t]] = s + 1
    return {t: list(np.bincount(pos[:, i], minlength=n + 1)[1:] / draws) for i, t in enumerate(teams)}


def new_draft_dta(wins, pl, prio, u, min_pick=None):
    """Drop-in replacement for league_sim.new_draft_dta with the corrected repair (same random numbers)."""
    members, relegated, balls, mx, mn = S._new_field(wins, pl, prio, min_pick)
    if len(set(members)) != 16:
        raise ValueError('3-2-1 lottery needs 16 distinct teams')
    u = np.clip(np.asarray(u[:16], float), 1e-300, 1.0)
    keys = -np.log(u) / np.array([balls[t] for t in members], float)
    seq = [members[i] for i in np.argsort(keys, kind='stable')]
    if _needs_repair(seq, mx, mn):
        seq = repair_order(seq, mx, mn, 16)
    rest = S._ascending([t for t in range(30) if t not in members], wins, prio)
    return seq + rest


@lru_cache(maxsize=512)
def _new_kernel_dta(field):
    """Drop-in replacement for league_sim._new_kernel_dta (same draws and seed, corrected repair; rows pooled
    over exchangeable members)."""
    names = [f'm{i}' for i in range(len(field))]
    balls = {k: f[0] for k, f in zip(names, field)}
    mx = {k: (RELEGATED_FLOOR if f[1] else 16) for k, f in zip(names, field)}
    mn = {k: f[2] for k, f in zip(names, field)}
    d = draw_then_adjust_mc(names, balls, mx, mn, draws=S.DTA_KERNEL_DRAWS, seed=S.DTA_KERNEL_SEED)
    K = np.array([d[k] for k in names])
    for f in set(field):
        ix = [i for i, g in enumerate(field) if g == f]
        K[ix] = K[ix].mean(axis=0)
    return K


def install():
    """Point league_sim's draw-then-adjust sampler and kernel at the corrected repair (this process only)."""
    S.new_draft_dta = new_draft_dta
    S._new_kernel_dta = _new_kernel_dta
    S.DTA_REPAIR = REPAIR_LABEL
    return S

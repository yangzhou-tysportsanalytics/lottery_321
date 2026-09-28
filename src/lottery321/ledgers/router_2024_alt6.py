"""2024 draft: alternative reading of the WAS 13-30 branch (registration addendum A1, sections 5(d) and 6).

Assumption item 6 (ledger_assumption_check.py): when the Washington pick conveys to New York (slot 13-30), the sources do not state whether
Memphis' swap right still reaches that pick. The primary router (`router_2024`) reads the Hoops
Rumors sentence as "Memphis may then swap only against the Phoenix pick". This module encodes the literal
ProSportsTransactions wording instead, "less favorable of Suns, Wizards picks": Memphis swaps its own pick
for the less favourable of the Phoenix and Washington picks whenever that pick is more favourable than its
own, and the team holding it (Phoenix, or New York for the Washington pick) receives Memphis' pick.

Everything else - the WAS 1-12 branch, the OKC pool, MIL/NOP and every simple right - is imported unchanged
from the primary module. Registered use: the 25 window days of 2023-24 listed in
`results/ledger_assumption_check.json`.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from teams import TEAMS  # noqa: E402
import router_2024 as BASE  # noqa: E402

POOLS = BASE.POOLS
POOLED = BASE.POOLED
ASSUMPTIONS = [BASE.ASSUMPTIONS[0],
               "WAS/PHX/MEM, alternative reading of the 13-30 branch (assumption item 6): the WAS pick conveys to "
               "NYK and MEM may swap its own pick for the less favorable of the PHX and WAS picks; the holder "
               "of that pick (PHX, or NYK) receives MEM's pick."] + list(BASE.ASSUMPTIONS[2:])
POST_DEADLINE_CHANGES = BASE.POST_DEADLINE_CHANGES


def _pool_wpm_alt(pos):
    h = {}
    if pos['WAS'] <= 12:
        return BASE._pool_wpm(pos)                      # unchanged branch
    h['WAS'] = 'NYK'
    worse = 'PHX' if pos['PHX'] > pos['WAS'] else 'WAS'  # less favorable of the two
    holder = 'PHX' if worse == 'PHX' else 'NYK'
    other = 'WAS' if worse == 'PHX' else 'PHX'
    h[other] = 'NYK' if other == 'WAS' else 'PHX'
    if pos[worse] < pos['MEM']:                          # MEM swaps into the less favorable pick
        h[worse], h['MEM'] = 'MEM', holder
    else:
        h[worse], h['MEM'] = holder, 'MEM'
    return h


def route(pos):
    if sorted(pos) != sorted(TEAMS) or sorted(pos.values()) != list(range(1, 31)):
        raise ValueError('pos must map all 30 native teams to a permutation of 1..30')
    h = {t: BASE._simple_holder(t, pos[t]) for t in TEAMS if t not in POOLED}
    h.update(_pool_wpm_alt(pos))
    h.update(BASE._pool_okc(pos))
    h.update(BASE._pool_milnop(pos))
    return {pos[t]: h[t] for t in TEAMS}


class Router2024Alt6:
    simple_natives = tuple(t for t in TEAMS if t not in POOLED)
    pools = POOLS

    @staticmethod
    def simple(native, slot):
        return BASE._simple_holder(native, slot)

    @staticmethod
    def pooled(pos):
        full = {t: pos[t] for t in POOLED}
        others = [s for s in range(1, 31) if s not in full.values()]
        filler = [t for t in TEAMS if t not in POOLED]
        full.update(dict(zip(filler, others)))
        out = route(full)
        return {full[t]: out[full[t]] for t in POOLED}

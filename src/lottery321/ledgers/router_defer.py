"""Deferral-option reading of two deadline ledgers (exploratory sensitivity, run tag `defer`).

At the 2022 deadline Brooklyn held Philadelphia's 2022 first, and at the 2024 deadline New Orleans held the
Los Angeles Lakers' 2024 first, each with an option to take the pick in that draft or defer it one year.
Both deferred in June. The primary routers code the deadline state as the holder taking the pick at every
slot. This module encodes the other side of the option: the holder takes the pick when it lands in the top
fourteen (a lottery pick under the old rule) and defers otherwise, so that from slot 15 on the native keeps
its pick in the current draft. Both realized picks (slots 23 and 17) fall in the deferred range.

Everything else in the two ledgers is imported unchanged. Registered nowhere; reported as exploratory
(Online Appendix H.33).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import router_2022 as B22  # noqa: E402
import router_2024 as B24  # noqa: E402

DEFER_FROM_SLOT = 15
OPTIONS = {2022: ('PHI', 'BKN'), 2024: ('LAL', 'NOP')}   # year: (native, holder)


def _wrap(base, native, holder):
    def simple_holder(nat, slot):
        if nat == native:
            return holder if slot < DEFER_FROM_SLOT else native
        return base._simple_holder(nat, slot)

    def route(pos):
        out = base.route(pos)
        s = pos[native]
        out[s] = simple_holder(native, s)
        return out

    class Router:
        simple_natives = base.Router2022.simple_natives if base is B22 else base.Router2024.simple_natives
        pools = base.POOLS

        @staticmethod
        def simple(nat, slot):
            return simple_holder(nat, slot)

        @staticmethod
        def pooled(pos):
            return (base.Router2022 if base is B22 else base.Router2024).pooled(pos)
    return Router, route


Router2022Defer, route_2022 = _wrap(B22, *OPTIONS[2022])
Router2024Defer, route_2024 = _wrap(B24, *OPTIONS[2024])
ROUTERS = {2022: Router2022Defer, 2024: Router2024Defer}

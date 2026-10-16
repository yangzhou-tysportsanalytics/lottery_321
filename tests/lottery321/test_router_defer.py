"""Tests for the deferral-option routers (router_defer)."""
import sys, unittest
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src/lottery321/ledgers'))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src/lottery321'))
import router_defer as D
import router_2022 as B22
import router_2024 as B24


class DeferRouters(unittest.TestCase):
    def _orders(self, teams, k=5000, seed=1):
        rng = np.random.default_rng(seed)
        for _ in range(k):
            perm = rng.permutation(30) + 1
            yield dict(zip(teams, perm.tolist()))

    def test_only_the_option_native_changes_and_slots_are_conserved(self):
        for base, route, (nat, holder) in ((B22, D.route_2022, D.OPTIONS[2022]), (B24, D.route_2024, D.OPTIONS[2024])):
            for pos in self._orders(base.TEAMS):
                a, b = base.route(pos), route(pos)
                self.assertEqual(sorted(b), list(range(1, 31)))
                for s in range(1, 31):
                    if s != pos[nat]:
                        self.assertEqual(a[s], b[s])
                exp = holder if pos[nat] < D.DEFER_FROM_SLOT else nat
                self.assertEqual(b[pos[nat]], exp)

    def test_router_classes_agree_with_route(self):
        for year, base, route in ((2022, B22, D.route_2022), (2024, B24, D.route_2024)):
            R = D.ROUTERS[year]
            for pos in self._orders(base.TEAMS, 2000, 2):
                full = route(pos)
                for nat in R.simple_natives:
                    self.assertEqual(R.simple(nat, pos[nat]), full[pos[nat]])
                for s, h in R.pooled(pos).items():
                    self.assertEqual(full[s], h)

    def test_realized_slots_fall_in_the_deferred_range(self):
        self.assertEqual(D.Router2022Defer.simple('PHI', 23), 'PHI')
        self.assertEqual(D.Router2024Defer.simple('LAL', 17), 'LAL')
        self.assertEqual(D.Router2022Defer.simple('PHI', 14), 'BKN')


if __name__ == '__main__':
    unittest.main()

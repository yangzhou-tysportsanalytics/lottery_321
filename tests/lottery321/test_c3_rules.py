"""Tests for the C3 component engine (old lottery with minimum slots, 3-2-1 without the floor)."""
import sys, unittest
from pathlib import Path
import numpy as np
R = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(R / 'src/lottery321'))
import c3_rules as C
from lottery_rules import FLAT_2019_COMBOS, flattened_2019_fast, GROUP_BALLS, RELEGATED_FLOOR


class OldWithRestrictions(unittest.TestCase):
    def test_equals_primary_kernel_without_restrictions(self):
        a = np.array(C.flattened_2019_restricted(FLAT_2019_COMBOS, {}))
        b = np.array(flattened_2019_fast())
        np.testing.assert_allclose(a, b, atol=1e-12)

    def test_doubly_stochastic(self):
        K = np.array(C.flattened_2019_restricted(FLAT_2019_COMBOS, {0: 2, 5: 6}))
        np.testing.assert_allclose(K.sum(1), 1.0, atol=1e-12)
        np.testing.assert_allclose(K.sum(0), 1.0, atol=1e-12)

    def test_minimum_slots_are_respected(self):
        K = np.array(C.flattened_2019_restricted(FLAT_2019_COMBOS, {0: 2, 3: 6}))
        self.assertEqual(K[0, 0], 0.0)                 # worst team cannot be #1
        self.assertEqual(K[3, :5].sum(), 0.0)          # 4th-worst cannot be top 5
        self.assertGreater(K[0, 1], 0.0)

    def test_matches_brute_force_enumeration(self):
        """Small analogue: 5 teams, 2 draws, enumerate every ordered draw."""
        combos = (40, 30, 20, 7, 3); mp = {0: 2, 1: 3}
        K = np.array(C.flattened_2019_restricted(combos, mp, draws=2))
        n = len(combos); brute = np.zeros((n, n))
        def rec(drawn, p):
            d = len(drawn)
            if d == 2:
                for t, s in C.place_undrawn([i for i in range(n) if i not in drawn], mp, 2, n).items():
                    brute[t, s - 1] += p
                for k, t in enumerate(drawn):
                    brute[t, k] += p
                return
            elig = [i for i in range(n) if i not in drawn and mp.get(i, 1) <= d + 1]
            w = sum(combos[i] for i in elig)
            for i in elig:
                rec(drawn + [i], p * combos[i] / w)
        rec([], 1.0)
        np.testing.assert_allclose(K, brute, atol=1e-12)

    def test_undrawn_placement_pushes_restricted_team_down(self):
        # teams 0,1,2 undrawn after 4 draws; team 0 cannot pick before slot 6
        got = C.place_undrawn([0, 1, 2], {0: 6}, draws=4, n=7)
        self.assertEqual(got, {1: 5, 0: 6, 2: 7})


class NewWithoutFloor(unittest.TestCase):
    FIELD = tuple(sorted([(2, True, 1)] * 3 + [(3, False, 1)] * 7 + [(2, False, 1)] * 4 + [(1, False, 1)] * 2))

    def test_floor_binds_only_when_on(self):
        with_floor = np.array(C.new_kernel_components(self.FIELD, True))
        without = np.array(C.new_kernel_components(self.FIELD, False))
        rel = [i for i, f in enumerate(self.FIELD) if f[1]]
        self.assertEqual(with_floor[rel, RELEGATED_FLOOR:].sum(), 0.0)
        self.assertGreater(without[rel, RELEGATED_FLOOR:].sum(), 0.0)
        for K in (with_floor, without):
            np.testing.assert_allclose(K.sum(1), 1.0, atol=1e-9)
            np.testing.assert_allclose(K.sum(0), 1.0, atol=1e-9)

    def test_without_floor_is_a_plain_weighted_draw(self):
        """With no floor and no restrictions the draw is Plackett-Luce on the ball counts."""
        from lottery_rules import weighted_rank_dist
        names = [f'm{i}' for i in range(16)]
        balls = {n: f[0] for n, f in zip(names, self.FIELD)}
        ref = weighted_rank_dist(names, balls)
        K = np.array(C.new_kernel_components(self.FIELD, False))
        np.testing.assert_allclose(K, np.array([ref[n] for n in names]), atol=1e-9)

    def test_restrictions_without_floor(self):
        field = tuple(sorted([(2, True, 6)] + [(2, True, 1)] * 2 + [(3, False, 2)]
                             + [(3, False, 1)] * 6 + [(2, False, 1)] * 4 + [(1, False, 1)] * 2))
        K = np.array(C.new_kernel_components(field, False))
        for i, (b, rel, mn) in enumerate(field):
            self.assertEqual(K[i, :mn - 1].sum(), 0.0)
        np.testing.assert_allclose(K.sum(0), 1.0, atol=1e-9)


if __name__ == '__main__':
    unittest.main()

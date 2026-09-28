"""Tests for theory (exact theory checks). Run:
    python3 -m unittest tests.lottery321.test_theory
"""
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src/lottery321'))
import theory as T  # noqa: E402

TOL = 1e-12


class AbelAlgebra(unittest.TestCase):
    """Abel identity, sharp bounds, dominance criteria."""

    def test_abel_identity_random(self):
        rng = np.random.default_rng(1)
        for _ in range(500):
            d = rng.normal(size=30)
            v = rng.normal(size=30)
            self.assertAlmostEqual(T.tau(d, v), T.abel(d, v), places=10)
            self.assertTrue(np.allclose(T.cumulative(d), np.cumsum(d)))

    @staticmethod
    def _random_values(rng, n, cls):
        """Random nonincreasing v >= 0 with v(1) = 1 (and v(30) = 0 for class C) via random increments."""
        m = 29 if cls == 'C' else 30
        a = rng.dirichlet(np.full(m, rng.choice([0.05, 0.3, 1.0, 5.0])), size=n)
        a = np.hstack([a, np.zeros((n, 30 - m))])      # a[j-1] = v(j) - v(j+1), a[29] = v(30)
        return np.cumsum(a[:, ::-1], axis=1)[:, ::-1]   # v(k) = sum_{j>=k} a_j

    def test_bounds_sharp_and_contain_random_values(self):
        rng = np.random.default_rng(2)
        for trial in range(10):
            d = rng.normal(size=30)
            d[-1] = rng.normal() * (trial % 2)
            C = T.cumulative(d)
            for cls in ('B', 'C'):
                b = T.value_class_bounds(C, cls)
                V = self._random_values(rng, 2000, cls)
                self.assertTrue(np.allclose(V[:, 0], 1.0))
                self.assertTrue(np.all(np.diff(V, axis=1) <= 1e-15) and np.all(V >= 0))
                if cls == 'C':
                    self.assertTrue(np.all(V[:, -1] == 0))
                taus = V @ d
                self.assertTrue(np.all(taus >= b['min'] - 1e-12) and np.all(taus <= b['max'] + 1e-12))
                self.assertAlmostEqual(T.tau(d, T.step_value(b['argmin_j'])), b['min'], places=12)
                self.assertAlmostEqual(T.tau(d, T.step_value(b['argmax_j'])), b['max'], places=12)
                if cls == 'C':
                    self.assertLessEqual(b['argmax_j'], 29)
                    self.assertLessEqual(b['argmin_j'], 29)

    def test_dominance_criteria(self):
        C = np.r_[np.linspace(0.1, 0.0, 29), 0.0]
        self.assertTrue(T.dominates(C, 'A') and T.dominates(C, 'B') and T.dominates(C, 'C'))
        C2 = C.copy(); C2[-1] = 0.05
        self.assertTrue(T.dominates(C2, 'B') and T.dominates(C2, 'C'))
        self.assertFalse(T.dominates(C2, 'A'))
        C3 = C.copy(); C3[-1] = -0.05
        self.assertTrue(T.dominates(C3, 'C'))
        self.assertFalse(T.dominates(C3, 'B') or T.dominates(C3, 'A'))
        C4 = C.copy(); C4[0] = -0.01
        self.assertFalse(T.dominates(C4, 'A') or T.dominates(C4, 'B') or T.dominates(C4, 'C'))
        # class-A counterexample when C(30) != 0: constant negative v
        self.assertLess(T.tau(np.diff(np.r_[0, C2]), -np.ones(30)), 0)


class PositionKernels(unittest.TestCase):
    """Rank monotonicity of the position kernels."""

    @classmethod
    def setUpClass(cls):
        cls.K = T.position_kernels()

    def test_shapes_and_stochastic(self):
        self.assertEqual(self.K['old'].shape, (14, 14))
        self.assertEqual(self.K['new'].shape, (16, 16))
        for K in self.K.values():
            self.assertTrue(np.allclose(K.sum(0), 1) and np.allclose(K.sum(1), 1))

    def test_old_rule_monotone(self):
        self.assertEqual(T.rank_monotone(self.K['old']), [])

    def test_new_rule_violates_at_relegation_boundary(self):
        v = T.rank_monotone(self.K['new'])
        self.assertEqual(v, [(3, j) for j in range(1, 12)])
        F = np.cumsum(self.K['new'], axis=1)
        self.assertAlmostEqual(F[2, 11], 1.0, places=12)      # floor: P(pick <= 12 | position 3) = 1
        self.assertGreater(F[2, 11], F[3, 11])


class Enumerator(unittest.TestCase):
    """Exact enumerator, zero-sum identity, asset decomposition."""

    @classmethod
    def setUpClass(cls):
        games = [(2, 3, 0.5), (4, 27, 0.4), (1, 5, 0.7), (3, 28, 0.55)]
        cls.inst = T.make_instance([10, 12, 16, 16, 17, 18, 22, 24, 26, 28], games,
                                   rights={3: ('protected', 4, 2), 5: ('reverse', 10, 27), 7: ('conveyed', 29)})
        cls.res = T.exact_holdings(cls.inst)

    def test_rows_are_probabilities(self):
        for r in T.RULES:
            Q = self.res[r]['Q']
            self.assertTrue(np.allclose(Q.sum(axis=2), 1.0))   # every slot held exactly once in expectation

    def test_zero_sum(self):
        for r in T.RULES:
            for f in range(len(self.inst['games'])):
                dev, ok = T.zero_sum(self.res[r]['Q'][f, 0], self.res[r]['Q'][f, 1])
                self.assertTrue(ok, (r, f, dev))

    def test_asset_decomposition(self):
        for r in T.RULES:
            for f, (h, a, _) in enumerate(self.inst['games']):
                for c in (h, a):
                    lose = 0 if c == h else 1
                    Qn = self.res[r]['Qn'][f]
                    dn, d, ok = T.asset_decomposition(Qn[lose], Qn[1 - lose], c)
                    self.assertTrue(ok)
                    self.assertTrue(np.allclose(d, T.own_view_d(self.res[r]['Q'][f], c, h, a)))

    def test_router_kinds(self):
        R = T.make_router({1: ('protected', 4, 9), 2: ('reverse', 4, 9), 3: ('conveyed', 9)})
        self.assertEqual([R(1, 4), R(1, 5), R(2, 4), R(2, 5), R(3, 1), R(0, 1)], [1, 9, 9, 2, 9, 0])

    def test_membership_guard(self):
        with self.assertRaises(ValueError):
            T.make_instance([10] * 9 + [35], [(9, 20, 0.5)])
        with self.assertRaises(ValueError):
            T.make_instance([10] * 10, [(11, 20, 0.5)])

    def test_single_game_matches_direct_marginals(self):
        inst = T.make_instance(T.BOUNDARY_WINS, T.BOUNDARY_GAMES)
        res = T.exact_holdings(inst)
        w = inst['wins'].copy(); w[T.Y] += 1                   # branch 0: home (A) loses
        M = T.old_marginal(w, inst['pl_old'], inst['prio'])
        self.assertTrue(np.allclose(res['old']['Q'][0, 0], M))


class MinimalExamples(unittest.TestCase):
    """Sign patterns of E1-E6."""

    def test_e1_old_own_pick_class_b(self):
        C = T.example_e1()['C']
        self.assertTrue(T.dominates(C, 'B'))
        self.assertGreater(C.max(), 0.01)
        self.assertAlmostEqual(C[-1], 0.0, places=12)

    def test_e2_new_own_pick_reversal(self):
        e = T.example_e2(); C = e['C']; d = e['d']
        self.assertLess(C[0], 0)
        self.assertGreater(C[11], 0)
        self.assertFalse(T.dominates(C, 'B'))
        self.assertLess(T.tau(d, T.step_value(1)), 0)
        self.assertGreater(T.tau(d, T.step_value(12)), 0)

    def test_e3_protected_pick_of_other_team(self):
        e = T.example_e3(); C = e['C']
        self.assertLess(C[-1], 0)                              # M < 0 under 3-2-1
        self.assertFalse(T.dominates(C, 'B'))
        self.assertFalse(T.dominates(C, 'C'))                  # A holds nothing beyond slot 16: C(29) = M
        self.assertAlmostEqual(C[28], C[29], places=12)
        own = e['dn'][T.A]
        self.assertAlmostEqual(own.sum(), 0.0, places=12)      # own pick contributes nothing to M
        self.assertAlmostEqual(e['dn'][T.Y].sum(), C[-1], places=12)
        self.assertGreater(T.example_e3('old')['C'][-1], 0)    # same portfolio, old rule: M > 0

    def test_e4_opponents_pick(self):
        C = T.example_e4()['C']
        self.assertTrue(np.all(C <= TOL))
        self.assertLess(C.min(), -0.005)

    def test_e5_repeat_restriction(self):
        C = T.example_e5()['C']
        self.assertTrue(np.all(np.abs(C[:5]) <= TOL))
        self.assertFalse(T.dominates(C, 'B'))

    def test_e6_own_protected_pick(self):
        C = T.example_e6()['C']
        self.assertTrue(T.dominates(C, 'B') and T.dominates(C, 'C'))
        self.assertGreater(C[-1], 0)
        self.assertFalse(T.dominates(C, 'A'))
        self.assertTrue(np.allclose(C[3:], C[3]))              # nothing held beyond slot P = 4


class RandomizedProperty(unittest.TestCase):
    """Monotone benchmark on random own-pick-only instances."""

    @classmethod
    def setUpClass(cls):
        cls.scan = T.property_scan(n_instances=200, seed=20260921, g_max=6)

    def test_zero_sum_everywhere(self):
        self.assertLess(self.scan['max_zero_sum_dev'], 1e-12)

    def test_old_rule_strict_records_monotone(self):
        self.assertEqual(self.scan['old_strict_violations'], [])

    def test_old_rule_official_tie_splitting_counterexamples(self):
        # Documented finding (see property_scan docstring): official tie splitting can create tiny
        # class-B reversals for own-pick-only players. Asserted only to be small, not absent.
        for v in self.scan['old_violations']:
            self.assertGreater(v['minC'], -0.01)

    def test_new_rule_violations_at_relegation_boundary(self):
        for v in self.scan['new_violations']:
            self.assertTrue(v['relegation_boundary'], v)



class BoundaryDecomposition(unittest.TestCase):
    """Position-boundary theorem (paper Section 3.3): C_c(j) = sum_n sum_r dPi_n(r) G_{n->c,r}(j) under fixed membership, strict records,
    a position-only kernel and simple rights; plus the coupling lemma."""

    def test_theorem_exact_on_examples(self):
        for ex in (T.example_e1(), T.example_e2(), T.example_e3(), T.example_e6(), T.example_e3(rule='old')):
            bd = T.boundary_decomposition(ex['instance'], ex['rule'], ex['focal'], ex['player'])
            np.testing.assert_allclose(bd['C_pred'], ex['C'], atol=1e-12, err_msg=ex['name'])

    def test_e2_only_negative_term_is_relegation_boundary(self):
        ex = T.example_e2()
        bd = T.boundary_decomposition(ex['instance'], 'new', 0, ex['player'])
        self.assertEqual({(n, r) for n, r, _ in bd['negative_terms']}, {(ex['player'], 3)})
        self.assertAlmostEqual(ex['C'][0], -1.0 / 37.0, places=12)       # 2 balls vs 3 balls out of 37

    def test_theorem_random_new_and_strict_old_but_not_tied_old(self):
        rng = np.random.default_rng(7); n_old_fail = 0; n = 0
        for _ in range(12):
            inst = T.random_instance(rng, 4)
            res = T.exact_holdings(inst, ('new', 'old_strict', 'old'))
            for f, (h, a, _) in enumerate(inst['games']):
                for c in (h, a):
                    bn = T.boundary_decomposition(inst, 'new', f, c)
                    bo = T.boundary_decomposition(inst, 'old', f, c)
                    Cn = T.cumulative(T.own_view_d(res['new']['Q'][f], c, h, a))
                    Cs = T.cumulative(T.own_view_d(res['old_strict']['Q'][f], c, h, a))
                    Co = T.cumulative(T.own_view_d(res['old']['Q'][f], c, h, a))
                    np.testing.assert_allclose(bn['C_pred'], Cn, atol=1e-10)
                    np.testing.assert_allclose(bo['C_pred'], Cs, atol=1e-10)
                    n += 1; n_old_fail += int(np.abs(bo['C_pred'] - Co).max() > 1e-10)
        # the official old rule splits tied teams' combinations, violating assumption (ii)
        self.assertGreater(n_old_fail, 0); self.assertLess(n_old_fail, n)

    def test_coupling_lemma_player_and_opponent(self):
        rng = np.random.default_rng(11)
        for _ in range(20):
            inst = T.random_instance(rng, 5)
            pi = T.exact_positions(inst)
            for f, (h, a, _) in enumerate(inst['games']):
                for c, o in ((h, a), (a, h)):
                    lose = 0 if c == h else 1
                    d = np.cumsum(pi[f, lose] - pi[f, 1 - lose], axis=1)
                    self.assertTrue(np.all(d[c] >= -1e-12))       # the loser's position only gets worse
                    self.assertTrue(np.all(d[o] <= 1e-12))        # the winner's position only gets better


if __name__ == '__main__':
    unittest.main()

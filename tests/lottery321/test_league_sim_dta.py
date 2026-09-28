"""Tests for the draw-then-adjust sensitivity option of league_sim (registration addendum A1, section 5(a))."""
import sys, unittest
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src/lottery321'))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src/lottery321/ledgers'))
import league_sim as S
from lottery_rules import draw_then_adjust_mc, GROUP_BALLS, RELEGATED_FLOOR
import elo as E
from cutoff_state import build_state

ROOT = Path(__file__).resolve().parents[2]
GAMES = ROOT / 'data/games.csv'
WINS = np.arange(30) * 2
PL = {'playoffs': set(range(16, 30)), 'nonplayin': list(range(10)), 'seeds910': [10, 11, 12, 13], 'losers78': [14, 15]}
PRIO = np.linspace(0, 1, 30)


class DrawThenAdjustSampler(unittest.TestCase):
    def test_orders_are_valid_and_respect_floor_and_minimums(self):
        rng = np.random.default_rng(7)
        mp = {0: 6, 4: 2}                       # a relegated team restricted to >= 6, a 3-ball team to >= 2
        for _ in range(2000):
            order = S.new_draft_dta(WINS, PL, PRIO, rng.random(16), mp)
            self.assertEqual(sorted(order), list(range(30)))
            self.assertEqual(set(order[:16]), set(range(16)))
            for t in (0, 1, 2):
                self.assertLessEqual(order.index(t) + 1, RELEGATED_FLOOR)
            self.assertGreaterEqual(order.index(0) + 1, 6)
            self.assertGreaterEqual(order.index(4) + 1, 2)
            self.assertEqual(order[16:], list(range(16, 30)))

    def test_unconstrained_draw_needs_no_repair(self):
        # uniforms that put every relegated team inside the top 12 and no restriction: order = ball race
        u = np.full(16, 0.5); u[[0, 1, 2]] = 0.999
        order = S.new_draft_dta(WINS, PL, PRIO, u, {})
        self.assertEqual(set(order[:3]), {0, 1, 2})

    def test_sampler_marginals_match_reference_mc(self):
        """Sampler frequencies agree with lottery_rules.draw_then_adjust_mc (independent implementation of the
        same repair) within Monte Carlo error."""
        mp = {0: 6}
        rng = np.random.default_rng(11); n = 60000
        F = np.zeros((16, 16))
        for _ in range(n):
            order = S.new_draft_dta(WINS, PL, PRIO, rng.random(16), mp)
            for s, t in enumerate(order[:16]):
                F[t, s] += 1
        F /= n
        members, rel, balls, mx, mn = S._new_field(WINS, PL, PRIO, mp)
        ref = draw_then_adjust_mc(members, balls, mx, mn, draws=400000, seed=5)
        R = np.array([ref[t] for t in range(16)])
        self.assertLess(np.abs(F - R).max(), 0.01)

    def test_kernel_is_doubly_stochastic_and_respects_constraints(self):
        field = tuple(sorted([(2, True, 6)] + [(2, True, 1)] * 2 + [(3, False, 2)] + [(3, False, 1)] * 6
                             + [(2, False, 1)] * 4 + [(1, False, 1)] * 2))
        K = S._new_kernel_dta(field)
        np.testing.assert_allclose(K.sum(1), 1.0, atol=1e-12)
        np.testing.assert_allclose(K.sum(0), 1.0, atol=1e-12)
        for i, (b, rel, mn) in enumerate(field):
            if rel:
                self.assertEqual(K[i, RELEGATED_FLOOR:].sum(), 0.0)
            self.assertEqual(K[i, :mn - 1].sum(), 0.0)

    def test_kernel_close_to_sequential_without_restrictions(self):
        # the two readings coincide up to MC error when only the floor binds (recorded, not assumed)
        field = tuple(sorted([(2, True, 1)] * 3 + [(3, False, 1)] * 7 + [(2, False, 1)] * 4 + [(1, False, 1)] * 2))
        self.assertLess(np.abs(S._new_kernel_dta(field) - S._new_kernel(field)).max(), 0.003)

    def test_new_marginal_procedure_switch(self):
        a = S.new_marginal(WINS, PL, PRIO, {0: 6}, 'sequential_feasible')
        b = S.new_marginal(WINS, PL, PRIO, {0: 6}, 'draw_then_adjust')
        for M in (a, b):
            np.testing.assert_allclose(M.sum(1), 1.0, atol=1e-12); np.testing.assert_allclose(M.sum(0), 1.0, atol=1e-12)
        self.assertEqual(b[0, :5].sum(), 0.0)


class OfficialPrintedOdds(unittest.TestCase):
    """draw_then_adjust, like sequential_feasible,
    reproduces the 64 marginal probabilities printed in the official 3-2-1 attachment (standard field, no
    restrictions). It needs Monte Carlo draws and several printed values lie close to a rounding boundary, so the
    check is |MC - printed| <= 0.5 percentage points (rounding) + 4 Monte Carlo standard errors; with 20 million
    draws every value rounds to the printed one."""
    OFFICIAL = {  # NBA 3-2-1 attachment page 2 (2026-05), picks 1..16, percent (as in test_lottery_rules)
        'bottom3': [5.4, 5, 6, 6, 6, 6, 6, 6, 6, 8, 14, 25, 0, 0, 0, 0],
        'non_playin': [8.1, 8, 8, 8, 8, 7, 7, 7, 7, 6, 4, 2, 7, 6, 5, 3],
        'playin_9_10': [5.4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 5, 2, 9, 9, 9, 7],
        'playin_7_8_losers': [2.7, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 2, 8, 10, 15, 27]}
    REP = {'bottom3': 'bottom3_0', 'non_playin': 'non_playin_3', 'playin_9_10': 'playin_9_10_10',
           'playin_7_8_losers': 'playin_7_8_losers_14'}
    DRAWS = 1_000_000

    def test_reproduces_the_64_printed_marginals_within_rounding_and_mc_error(self):
        from lottery_rules import standard_field
        teams, balls, mx, mn = standard_field()
        d = draw_then_adjust_mc(teams, balls, mx, mn, draws=self.DRAWS, seed=20260921)
        n = 0
        for g, t in self.REP.items():
            for k, printed in enumerate(self.OFFICIAL[g]):
                p = d[t][k]
                se = 100 * np.sqrt(p * (1 - p) / self.DRAWS)
                bound = (0.05 if k == 0 else 0.5) + 4 * se
                self.assertLessEqual(abs(100 * p - printed), bound, f'{g} pick {k + 1}: {100 * p:.4f} vs {printed}')
                n += 1
        self.assertEqual(n, 64)


class SimulateWithDTA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        games = E.load_games(GAMES)
        cls.state = build_state(games, '2023-24', datetime(2024, 3, 15, 16, 0, tzinfo=timezone.utc))

    def test_unknown_procedure_rejected(self):
        with self.assertRaises(ValueError):
            S.simulate(self.state, [0], n=10, seed=1, batches=5, new_procedure='other')

    def test_conservation_with_pooled_router(self):
        from router_2024 import Router2024
        r = S.simulate(self.state, [0, 1], n=20, seed=2, batches=5, router=Router2024, min_pick_new={3: 6},
                       new_procedure='draw_then_adjust')
        # hybrid exact/sampled routing: each world holds exactly 30 slots in total (as in test_sim)
        np.testing.assert_allclose(r['Q'].sum(axis=(3, 4)), 30.0)
        np.testing.assert_allclose(r['DB'].sum(axis=(3, 4)), 0.0, atol=1e-9)
        # own-pick-only portfolios are exact marginals: every slot has exactly one holder
        np.testing.assert_allclose(r['DB_own'].sum(axis=3), 0.0, atol=1e-9)

    def test_old_rule_unaffected_by_procedure(self):
        a = S.simulate(self.state, [0], n=20, seed=3, batches=5)
        b = S.simulate(self.state, [0], n=20, seed=3, batches=5, new_procedure='draw_then_adjust')
        np.testing.assert_array_equal(a['Q'][:, :, 0], b['Q'][:, :, 0])
        np.testing.assert_array_equal(a['ST'], b['ST'])


if __name__ == '__main__':
    unittest.main()

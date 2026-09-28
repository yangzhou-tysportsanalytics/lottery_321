"""Tests for the C3 analysis: Shapley algebra, chain increments and the table build, on synthetic files."""
import json, sys, tempfile, unittest
from pathlib import Path
import numpy as np
R = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(R / 'src/lottery321'))
sys.path.insert(0, str(R / 'src/lottery321/ledgers'))
import c3_analysis as C
import c3_runs as RUN
import c3_sim as SIM
import analysis as A


class ShapleyAlgebra(unittest.TestCase):
    def test_values_sum_to_the_grand_difference(self):
        rng = np.random.default_rng(0)
        vals = {C.subset_key(''.join(s)): float(rng.normal())
                for k in range(5) for s in __import__('itertools').combinations(C.COMPONENTS, k)}
        phi = C.shapley(vals)
        self.assertAlmostEqual(sum(phi.values()), vals['FLRP'] - vals[''], places=12)

    def test_additive_value_gives_each_component_its_own_effect(self):
        eff = {'F': 1.0, 'L': -0.5, 'R': 0.25, 'P': 2.0}
        vals = {C.subset_key(''.join(s)): sum(eff[c] for c in s)
                for k in range(5) for s in __import__('itertools').combinations(C.COMPONENTS, k)}
        phi = C.shapley(vals)
        for k, v in eff.items():
            self.assertAlmostEqual(phi[k], v, places=12)

    def test_constrained_value_is_efficient_and_additive(self):
        """A1 amendment 9: F before R, still summing to the grand difference."""
        rng = np.random.default_rng(5)
        vals = {C.subset_key(''.join(s)): float(rng.normal())
                for k in range(5) for s in __import__('itertools').combinations(C.COMPONENTS, k)}
        psi = C.shapley_constrained(vals)
        self.assertAlmostEqual(sum(psi.values()), vals['FLRP'] - vals[''], places=12)
        eff = {'F': 1.0, 'L': -0.5, 'R': 0.25, 'P': 2.0}
        add = {C.subset_key(''.join(s)): sum(eff[c] for c in s)
               for k in range(5) for s in __import__('itertools').combinations(C.COMPONENTS, k)}
        for k, v in eff.items():
            self.assertAlmostEqual(C.shapley_constrained(add)[k], v, places=12)

    def test_constrained_value_ignores_orderings_with_R_before_F(self):
        """A value that only appears when R is taken without F must not reach the constrained result."""
        base = {C.subset_key(''.join(s)): 0.0
                for k in range(5) for s in __import__('itertools').combinations(C.COMPONENTS, k)}
        base['R'] = 5.0                                  # the invented "R with F off" coalition
        self.assertNotAlmostEqual(C.shapley(base)['R'], C.shapley_constrained(base)['R'])
        self.assertAlmostEqual(sum(C.shapley_constrained(base).values()), 0.0, places=12)

    def test_works_on_bootstrap_vectors(self):
        rng = np.random.default_rng(1)
        vals = {C.subset_key(''.join(s)): rng.normal(size=7)
                for k in range(5) for s in __import__('itertools').combinations(C.COMPONENTS, k)}
        phi = C.shapley(vals)
        np.testing.assert_allclose(sum(phi.values()), vals['FLRP'] - vals[''], atol=1e-12)


def fake_c3_day(path, season, day, reversal_subsets=('FLR', 'FLRP'), n_games=3, seed=0):
    """A day file in the real format: configurations listed by c3_sim.config_list()."""
    rng = np.random.default_rng(seed)
    cfgs = SIM.config_list(); C_ = len(cfgs); B = 50
    DOWN = np.zeros((B, n_games, C_, 2, 30)); STK = np.zeros((B, n_games, C_, 4, 30))
    pos = np.zeros(30); pos[:4] = 0.02
    neg = np.zeros(30); neg[:9] = -0.01; neg[11] = 0.12
    for ci, cf in enumerate(cfgs):
        sub = C.subset_key(cf['subset'].replace('0', ''))
        d = neg if sub in reversal_subsets else pos
        DOWN[:, :, ci] = d + rng.normal(0, 2e-4, (B, n_games, 2, 30))
        STK[:, :, ci, :, :] = rng.normal(0, 1e-3, (B, n_games, 4, 30))
        STK[:, :, ci, :, 5] += 0.02            # one third party with a real stake
        STK[:, :, ci, :, 0] += 0.05            # a participant
    meta = {'season': season, 'day': day, 'seed': 20240301, 'cutoff_utc': '2024-03-01T16:00:00+00:00',
            'focal_teams': [[i, i + 15] for i in range(n_games)],
            'focal_game_ids': [f'{day}-{i}' for i in range(n_games)],
            'min_pick_new': {'DET': 6}, 'precision_met': True, 'n_worlds': 2000, 'secs': 100.0,
            'configs': [c['name'] for c in cfgs], 'subsets': [c['subset'] for c in cfgs],
            'curves': list(SIM.CURVE_NAMES), 'run_tag': 'c3', 'remaining_games': 200}
    path.parent.mkdir(parents=True, exist_ok=True)
    RUN.save(path, {'DOWN': DOWN, 'STK': STK, 'configs': meta['configs'], 'subsets': meta['subsets']}, meta)


class EndToEnd(unittest.TestCase):
    def test_tables(self):
        ranks = np.arange(1, 31)
        with tempfile.TemporaryDirectory() as t:
            root = Path(t) / 'c3'
            for i in range(6):
                fake_c3_day(root / '2023-24' / f'exposures_2024-03-0{i + 1}.npz', '2023-24',
                            f'2024-03-0{i + 1}', seed=i)
            T = C.main(out=Path(t) / "out", root=root, ranks_fn=lambda m: ranks)
        # every subset present, both variants
        subs = {r['subset'] for r in T['C3_1_outcomes']}
        self.assertEqual(len(subs), 16)
        self.assertEqual({r['variant'] for r in T['C3_1_outcomes']}, {'A', 'B'})
        # Y1: reversal share is 1 for the two configurations we built as reversals, 0 elsewhere
        y1 = {(r['variant'], r['subset']): r['value'] for r in T['C3_1_outcomes']
              if r['outcome'] == 'Y1_reversal_share' and r['band'] == 'all'}
        self.assertAlmostEqual(y1[('A', 'FLR')], 1.0)
        self.assertAlmostEqual(y1[('A', 'FLRP')], 1.0)
        self.assertAlmostEqual(y1[('A', 'F')], 0.0)
        # Shapley sums to the grand difference, per outcome and variant
        for r in T['C3_3_shapley']:
            if r['component'] == 'sum':
                self.assertAlmostEqual(r['shapley_unconstrained'], r['total_FLRP_minus_old'], places=10)
                self.assertAlmostEqual(r['value_FbeforeR'], r['total_FLRP_minus_old'], places=10)
        # chain increments sum to the same total
        for variant in ('A', 'B'):
            for out in C.OUTCOMES:
                steps = [r['delta'] for r in T['C3_2_chain']
                         if r['variant'] == variant and r['outcome'] == out and r['band'] == 'all']
                tot = [r['total_FLRP_minus_old'] for r in T['C3_3_shapley']
                       if r['variant'] == variant and r['outcome'] == out and r['band'] == 'all'
                       and r['component'] == 'sum'][0]
                self.assertAlmostEqual(sum(steps), tot, places=10)
        self.assertEqual(len(T['C3_4_H3']), 2)
        self.assertEqual(T['C3_0_diagnostics'][0]['subsets'], 16)


if __name__ == '__main__':
    unittest.main()

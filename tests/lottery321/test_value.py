import sys, unittest
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src/lottery321'))
from value import tau_table, stakes, cumulative_bounds, precision_met, CURVES
from lottery_rules import flattened_2019, flattened_2019_fast


def synthetic(B=20):
    """One focal game: home team 0, away team 1, third team 2. Under 'away wins' (home loses) the home team
    moves from slot 10 to slot 8 (better pick) and team 2 moves from slot 8 to slot 10."""
    DB = np.zeros((B, 1, 2, 30, 30))
    for r in (0, 1):
        DB[:, 0, r, 0, 7] += 1; DB[:, 0, r, 0, 9] -= 1
        DB[:, 0, r, 2, 9] += 1; DB[:, 0, r, 2, 7] -= 1
    DB[:, 0, 1] *= 0.5  # new rule: half the effect
    return {'DB': DB}


class ValueLayer(unittest.TestCase):
    def test_tau_sign_home_loss_improves_pick(self):
        rows = tau_table(synthetic(), [(0, 1)])
        r = [x for x in rows if x['side'] == 'home' and x['metric'] == 'tau_old' and x['curve'] == 'linear'][0]
        self.assertAlmostEqual(r['mean'], CURVES['linear'][7] - CURVES['linear'][9])
        self.assertGreater(r['mean'], 0); self.assertEqual(r['sign'], 'positive')
        d = [x for x in rows if x['side'] == 'home' and x['metric'] == 'delta_tau' and x['curve'] == 'linear'][0]
        self.assertAlmostEqual(d['mean'], -0.5 * r['mean'])

    def test_away_team_unaffected_zero(self):
        rows = tau_table(synthetic(), [(0, 1)])
        r = [x for x in rows if x['side'] == 'away' and x['metric'] == 'tau_old' and x['curve'] == 'linear'][0]
        self.assertEqual(r['mean'], 0.0); self.assertEqual(r['sign'], 'unresolved')

    def test_third_party_stake_sign(self):
        st = stakes(synthetic())['linear'][0]          # (G, rule, team)
        self.assertGreater(st[0, 0, 2], 0)               # team 2 gains when home wins
        self.assertLess(st[0, 0, 0], 0)                  # home team's own pick worse when it wins

    def test_cumulative_bounds_step_extremes(self):
        rows, m, _ = cumulative_bounds(synthetic(), [(0, 1)])
        r = [x for x in rows if x['rule'] == 'old' and x['side'] == 'home' and x['class'] == 'B'][0]
        self.assertAlmostEqual(r['bound_max'], 1.0); self.assertAlmostEqual(r['bound_min'], 0.0)
        self.assertEqual(r['argmax_j'], 8)

    def test_precision_rule(self):
        ok, worst = precision_met([{'curve': 'linear', 'halfwidth': 0.002}, {'curve': 'linear', 'halfwidth': 0.004}])
        self.assertFalse(ok); self.assertEqual(worst, 0.004)

    def test_fast_old_kernel_equals_reference(self):
        np.testing.assert_allclose(np.array(flattened_2019_fast()), np.array(flattened_2019()), atol=1e-13)
        c = (140, 140, 140, 125, 105, 90, 75, 60, 45, 30, 20, 15, 10, 5)
        tie = (140, 140, 140, 125, 105, 90, 68, 67, 45, 30, 20, 15, 10, 5)
        np.testing.assert_allclose(np.array(flattened_2019_fast(tie)), np.array(flattened_2019(tie)), atol=1e-13)


if __name__ == '__main__':
    unittest.main()

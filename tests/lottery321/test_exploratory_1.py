"""Exploratory analyses (first set): the re-implementations must reproduce the registered numbers they extend."""
import csv, sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src/lottery321'))
import exploratory_1 as P
import robustness_headlines as R

PRIMARY = P.AN / 'primary'


@unittest.skipUnless((PRIMARY / 'team_games.csv.gz').exists(), 'primary tables not present')
class ReproduceRegistered(unittest.TestCase):
    def test_headline_matches_registered_table(self):
        tg = P.load_tg(); tg = tg[tg.rule.isin(['old', 'new'])]
        got = {r['portfolio']: r for r in P.headline(tg)}
        with open(PRIMARY / 'T5_headline_reversal_diff.csv', newline='') as f:
            reg = {r['portfolio']: r for r in csv.DictReader(f) if r['contrast'] == 'new_minus_old' and r['verdict'] == 'verdict_B'}
        for pf in ('actual', 'own'):
            self.assertAlmostEqual(got[pf]['diff'], float(reg[pf]['diff']), places=12)
            self.assertAlmostEqual(got[pf]['lo99'], float(reg[pf]['lo99']), places=12)
            self.assertAlmostEqual(got[pf]['hi99'], float(reg[pf]['hi99']), places=12)

    def test_h1_matches_registered_table(self):
        tg = P.load_tg(); tg = tg[tg.rule.isin(['old', 'new'])]
        got = R.h1(tg)
        with open(PRIMARY / 'H1.csv', newline='') as f:
            reg = next(csv.DictReader(f))
        self.assertEqual(got['h1_n'], int(reg['n_team_games']))
        self.assertAlmostEqual(got['h1_diff'], float(reg['diff_new_minus_old']), places=12)
        self.assertAlmostEqual(got['h1_lo99'], float(reg['diff_lo99']), places=12)
        self.assertEqual(got['h1_reversals'], int(reg['n_new_reversals']))


if __name__ == '__main__':
    unittest.main()

"""Figure code runs on synthetic analysis tables and produces non-empty files."""
import csv, sys, tempfile, unittest
from pathlib import Path
import numpy as np
R = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(R / 'src/lottery321'))
import figures as F


def write(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)


def fake_tables(d):
    rng = np.random.default_rng(0)
    prof = []
    for band in F.BANDS:
        for rule in ('old', 'new'):
            for pf in ('actual', 'own'):
                base = np.cumsum(rng.normal(0.002, 0.004, 30))
                for j in range(1, 31):
                    m = base[j - 1]
                    prof.append({'band': band, 'rule': rule, 'portfolio': pf, 'j': j, 'mean': m,
                                 'q10': m - 0.01, 'q90': m + 0.01, 'n': 100})
    write(d / 'F5_1_profiles.csv', prof)
    ver = []
    for band in F.BANDS:
        for rule in ('old', 'new'):
            for pf in ('actual', 'own'):
                for cls in ('B', 'C'):
                    shares = rng.dirichlet(np.ones(4))
                    for v, s in zip(('dominance_positive', 'reversal', 'negligible', 'unresolved'), shares):
                        ver.append({'rule': rule, 'portfolio': pf, 'band': band, 'value_class': cls,
                                    'verdict': v, 'share': s, 'lo99': max(0, s - .05), 'hi99': min(1, s + .05),
                                    'n': 200})
    write(d / 'T5_2_verdicts_by_band.csv', ver)
    teams = [f'T{i:02d}' for i in range(30)]
    edges = [{'season': '2025-26', 'rule': rule, 'game_team': a, 'holder': b,
              'weight': float(abs(rng.normal()))}
             for rule in ('old', 'new') for a in teams[:14] for b in teams if a != b]
    write(d / 'F5_2_network_edges.csv', edges)


class Figures(unittest.TestCase):
    def test_all_figures_render(self):
        with tempfile.TemporaryDirectory() as t:
            d = Path(t); fake_tables(d)
            F.main(str(d))
            out = d / 'figures'
            names = sorted(p.name for p in out.glob('*'))
            self.assertIn('figure_5_1_profiles.pdf', names)
            self.assertIn('figure_verdict_shares_classB_actual.png', names)
            self.assertTrue(any(n.startswith('figure_5_2_network_') for n in names))
            for p in out.glob('*'):
                self.assertGreater(p.stat().st_size, 3000, p.name)

    def test_network_needs_matching_rows(self):
        with tempfile.TemporaryDirectory() as t:
            d = Path(t); fake_tables(d)
            with self.assertRaises(ValueError):
                F.figure_5_2(F.read(d / 'F5_2_network_edges.csv'), d / 'figures', season='1999-00')


if __name__ == '__main__':
    unittest.main()

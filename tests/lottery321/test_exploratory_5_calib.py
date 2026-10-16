"""Tests for the simulations of the fifth exploratory set (exploratory_5_calib.py): part 5 (pooled rights at 16 joint draws) and
part 6 (calibration of the decision rule). The runs themselves are not exercised here."""
import sys
import unittest
from pathlib import Path
from unittest import mock

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src/lottery321'))
import exploratory_5_calib as R  # noqa: E402
import day_run  # noqa: E402
import analysis as S  # noqa: E402


@unittest.skipUnless(len(R.primary_files()) == 312, 'simulation day files not present')
class Days(unittest.TestCase):
    def test_pool_days_are_every_12th_primary_day_from_the_first(self):
        files = R.primary_files()
        self.assertEqual(len(files), 312)
        d = R.pool_days()
        self.assertEqual(len(d), 26)
        self.assertEqual(d[0], (files[0].parent.name, files[0].stem[len('exposures_'):]))
        self.assertEqual(d[1], (files[12].parent.name, files[12].stem[len('exposures_'):]))

    def test_pool32_days_are_the_twelve_fixed_before_that_run(self):
        import pool_convergence as PC
        root, days, draws, prefix = R.POOL_RUNS['pool32']()
        self.assertEqual(days, [(s, d) for s, d, _, _ in PC.SELECTED_DAYS])
        self.assertEqual((draws, prefix), (32, 'E5_5_pool32'))
        self.assertEqual(root, R.H.OUT / 'pool32')
        root16, days16, draws16, prefix16 = R.POOL_RUNS['pool16']()
        self.assertEqual((days16, draws16, prefix16), (R.pool_days(), 16, 'E5_5_pool'))

    def test_calibration_days_are_every_26th_primary_day(self):
        d = R.calib_days()
        self.assertEqual(len(d), 12)
        self.assertEqual(d[0], R.pool_days()[0])

    def test_calibration_seed_streams_are_distinct_and_apart_from_the_primary(self):
        seen = set()
        for season, day in R.calib_days():
            prim = int(day.replace('-', ''))
            for r in range(R.CALIB_RUNS_MAX):
                s = R.calib_seed(day, r)
                looks = {s + li for li in range(3)}
                self.assertFalse(looks & seen)
                self.assertNotIn(prim, looks)
                self.assertFalse(looks & {prim + li for li in range(3)})
                seen |= looks


class Stopping(unittest.TestCase):
    def test_a_run_without_stopping_contains_the_stopped_run_as_its_prefix(self):
        calls = []

        def fake(state, focal, n, seed, batches, **kw):
            calls.append((seed, n))
            rng = np.random.default_rng(seed)
            return {'DB': rng.normal(size=(batches, 1, 2, 30, 30)), 'DB_own': rng.normal(size=(batches, 1, 2, 30, 30)),
                    'Q': np.zeros(1), 'ST': np.zeros(1)}
        state = {'remaining': [(0, 1)]}
        with mock.patch.object(day_run, 'simulate', fake):
            full = day_run.run_day(state, [0], seed=7, looks=(80, 160, 320), batch=40, target=-1.0)
            stop = day_run.run_day(state, [0], seed=7, looks=(80, 160, 320), batch=40, target=float('inf'))
        self.assertEqual(full['n'], 320); self.assertEqual(stop['n'], 80)
        np.testing.assert_array_equal(full['DB'][:2], stop['DB'])
        self.assertEqual(calls[:1], calls[3:4])

    def test_stop_look_follows_the_precision_rule(self):
        # halfwidth shrinks as batches accumulate: noise with sd s per batch -> se = s / sqrt(B)
        rng = np.random.default_rng(3)
        DB = np.zeros((800, 1, 2, 30, 30))
        DB[:, 0, :, 0, :] = rng.normal(scale=0.2, size=(800, 2, 30))
        look, worst = R.stop_look(DB, [(0, 1)], target=0.003, looks_batches=(50, 200, 800))
        self.assertIn(look, (1, 2, 3))
        look_inf, _ = R.stop_look(DB, [(0, 1)], target=np.inf, looks_batches=(50, 200, 800))
        self.assertEqual(look_inf, 1)
        look_neg, _ = R.stop_look(DB, [(0, 1)], target=-1.0, looks_batches=(50, 200, 800))
        self.assertEqual(look_neg, 3)


class Reference(unittest.TestCase):
    def test_reference_classes(self):
        d = S.DELTA
        z = np.zeros(30)
        self.assertEqual(R.ref_class(z + 0.5 * d)['cls'], 'negligible')
        c = np.linspace(0.01, 0.05, 30)
        self.assertEqual(R.ref_class(c)['cls'], 'dominance')
        c2 = c.copy(); c2[3] = -0.5 * d
        self.assertEqual(R.ref_class(c2)['cls'], 'approximate_dominance')
        c3 = c.copy(); c3[20] = -2 * d
        r3 = R.ref_class(c3)
        self.assertEqual(r3['cls'], 'material_reversal'); self.assertTrue(r3['crossing'])
        c4 = -np.linspace(0.01, 0.05, 30)
        r4 = R.ref_class(c4)
        self.assertEqual(r4['cls'], 'material_reversal'); self.assertFalse(r4['crossing'])
        # only C(30) positive: not a crossing (j <= 29)
        c5 = c4.copy(); c5[29] = 0.01
        self.assertFalse(R.ref_class(c5)['crossing'])

    def test_h1_crossing_reference(self):
        c = np.zeros(30); c[5] = -0.01; c[12] = 0.01
        self.assertTrue(R.ref_class(c)['h1_crossing'])
        c[12] = 0.0; c[20] = 0.01
        self.assertFalse(R.ref_class(c)['h1_crossing'])

    def test_leave_one_out_reference_excludes_the_run(self):
        means = np.arange(4 * 3, dtype=float).reshape(4, 3)
        loo = R.leave_one_out(means)
        for r in range(4):
            np.testing.assert_allclose(loo[r], np.delete(means, r, axis=0).mean(0))


class Analyse(unittest.TestCase):
    def test_analysis_uses_runs_below_n_runs_on_every_day(self):
        # regression case: the loaded-run list overwrote the run limit after the first day
        import json
        import shutil
        import tempfile
        tmp = Path(tempfile.mkdtemp())
        days = [('2020-21', '2021-03-21'), ('2021-22', '2022-03-13')]
        rng = np.random.default_rng(0)
        try:
            for (season, day), nr in zip(days, (4, 3)):
                (tmp / 'calib' / season).mkdir(parents=True)
                for r in range(nr):
                    meta = dict(run=r, stop_look=3)
                    np.savez(tmp / 'calib' / season / f'calib_{day}_r{r:02d}.npz',
                             db=rng.normal(size=(3, 1, 2, 2, 2, 50, 30)).astype(np.float32),
                             mean32=rng.normal(size=(1, 2, 2, 2, 30)),
                             meta=np.frombuffer(json.dumps(meta).encode(), np.uint8))
            with mock.patch.object(R, 'OUT', tmp), mock.patch.object(R, 'calib_days', lambda: days):
                R.calib_analyse(n_runs=3)
            import csv
            with open(tmp / 'E5_6_calib_team_games.csv', encoding='utf-8') as f:
                rows = list(csv.DictReader(f))
            self.assertEqual(len(rows), 2 * 3 * 8)
            self.assertEqual({r['runs_on_day'] for r in rows}, {'3'})
            self.assertTrue((tmp / 'E5_6_calib_rates.csv').exists())
            self.assertTrue((tmp / 'tables' / 'tab_e5_6_calibration.tex').exists())
        finally:
            shutil.rmtree(tmp)


class PoolTable(unittest.TestCase):
    def test_pool_table_body(self):
        import shutil
        import tempfile
        tmp = Path(tempfile.mkdtemp())
        summ = [dict(kind='team-games', portfolio='actual', rule='old', scope='pooled holders', n=89,
                     mean_abs_dtau=0.00017, max_abs_dtau=0.0011, share_abs_dtau_ge_delta=0.0, verdicts_changed=4,
                     reversals_d4=6, reversals_d32=6),
                dict(kind='games', rule='new', scope='pooled games', n=72, mean_abs_third_d4=0.0022937,
                     mean_abs_third_d32=0.0022985, tp_median_d4=0.5998, tp_median_d32=0.6016),
                dict(kind='H2', scope='H2 games of the selected days', n=106, h2_d4=-4.0047e-05, h2_d32=-4.0592e-05)]
        try:
            with mock.patch.object(R, 'OUT', tmp):
                R.pool_tex('E5_5_pool32', summ, 32)
            a = (tmp / 'tables' / 'tab_e5_5_pool32_team_games.tex').read_text(encoding='utf-8')
            b = (tmp / 'tables' / 'tab_e5_5_pool32_games.tex').read_text(encoding='utf-8')
            self.assertIn('old rule & actual & pooled holders & 89 & 0.17 & 1.10 & 4 & 6 / 6 \\\\', a)
            self.assertIn('3-2-1 & pooled games & 72 & 2.29 & 2.30 & 0.600 & 0.602 \\\\', b)
            self.assertIn('H2 & H2 games of the selected days & 106 & −0.400 & −0.406', b)
        finally:
            shutil.rmtree(tmp)


class Band(unittest.TestCase):
    def test_critical_value_matches_the_registered_band_at_99(self):
        rng = np.random.default_rng(5)
        Cb = np.cumsum(rng.normal(size=(50, 30)), axis=1)
        _, _, crit = S.band_stats(Cb)
        self.assertAlmostEqual(R.crit_B(Cb, 0.99), crit['B'], places=12)
        self.assertGreater(R.crit_B(Cb, 1 - 0.01 / 3), crit['B'])

    def test_zero_variance_columns_give_zero(self):
        self.assertEqual(R.crit_B(np.zeros((50, 30)), 0.99), 0.0)


if __name__ == '__main__':
    unittest.main()

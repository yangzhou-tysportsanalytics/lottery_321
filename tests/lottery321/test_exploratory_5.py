"""Tests for the helpers of the fifth exploratory set (exploratory_5.py). The run itself also reproduces the
registered values it shares with the primary tables before writing anything (exploratory_5.checks)."""
import math
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src/lottery321'))
import exploratory_5 as R  # noqa: E402
import analysis as S  # noqa: E402


class FakeBoot:
    def __init__(self, days, W):
        self.days = days; self.idx = {k: i for i, k in enumerate(days)}; self.W = np.asarray(W, float)


class Helpers(unittest.TestCase):
    def test_weighted_median_over_resampled_days(self):
        days = [('s', 'd1'), ('s', 'd2')]
        rows = [dict(season='s', day='d1', x=1.0), dict(season='s', day='d1', x=2.0), dict(season='s', day='d2', x=10.0)]
        # replicate 1: only day 1 (median of 1, 2 -> the lower middle by the cumulative rule), replicate 2: only day 2
        b = FakeBoot(days, [[1, 0], [0, 1], [1, 1]])
        med, lo, hi, n = R.median_ci(rows, b, lambda r: r['x'], lambda r: True)
        self.assertEqual((med, n), (2.0, 3))
        # replicate medians 1 (day 1: cumulative weight reaches half at 1), 10 (day 2), 2 (both); quantiles interpolate
        self.assertTrue(1.0 <= lo < 1.1); self.assertTrue(9.9 < hi <= 10.0)

    def test_tau_a_is_the_value_under_v_a(self):
        rng = np.random.default_rng(1)
        db = rng.normal(size=(50, 30)); v = S.CURVES['linear']
        for a in R.A_VALUES:
            va = a + (1 - a) * v
            np.testing.assert_allclose(db @ va, (1 - a) * (db @ v) + a * db.sum(1))

    def test_c_rho_is_the_rollover_criterion(self):
        rng = np.random.default_rng(2)
        db = rng.normal(size=(50, 30)); v = S.CURVES['convex']
        C = np.cumsum(db, axis=1); M = C[:, 29:30]
        for rho in S.RHOS:
            Cr = C - rho * (np.arange(1, 31) / 30.0)[None, :] * M
            a_j = np.append(v[:-1] - v[1:], v[-1])                     # a_j = v(j) - v(j+1), v(31) = 0
            tau_rho = db @ v - rho * float(np.mean(v)) * M[:, 0]
            np.testing.assert_allclose(Cr @ a_j, tau_rho, atol=1e-10)
            np.testing.assert_allclose(Cr[:, 29], (1 - rho) * M[:, 0])

    def test_numbers_use_the_unicode_minus(self):
        self.assertEqual(R.num(-0.01234, 3), '−0.012'); self.assertEqual(R.num(0.5, 1, sign=True), '+0.5')
        self.assertEqual(R.ci(-1, -2, 0.5, d=1, sign=True), '−1.0 [−2.0, +0.5]')
        self.assertEqual(R.num(float('nan')), '—')

    def test_tex_body_matches_the_paper_format(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            with mock.patch.object(R, 'TAB', tmp):
                R.write_tex('t', ['a', 'b'], [['1', '−2']], 'lr')
            t = (tmp / 't.tex').read_text(encoding='utf-8')
            self.assertTrue(t.startswith('% generated from the data; do not edit by hand\n\\begin{adjustbox}{max width=\\textwidth}'))
            for part in ('\\toprule', '\\midrule', '\\bottomrule', '1 & −2 \\\\'):
                self.assertIn(part, t)
            self.assertNotIn('\r', t)
        finally:
            shutil.rmtree(tmp)

    def test_percent_signs_are_escaped_outside_the_comment_line(self):
        # regression case: headers such as "TP-dominated (%)" commented out the rest of the row
        tmp = Path(tempfile.mkdtemp())
        try:
            with mock.patch.object(R, 'TAB', tmp):
                R.write_tex('t', ['share (%)', 'already \\%'], [['50%', '1']], 'lr')
            lines = (tmp / 't.tex').read_text(encoding='utf-8').splitlines()
            self.assertTrue(lines[0].startswith('% generated'))
            body = '\n'.join(lines[1:])
            self.assertIn('share (\\%) & already \\% \\\\', body)
            self.assertIn('50\\% & 1 \\\\', body)
            self.assertNotRegex(body, r'(?<!\\)%')
        finally:
            shutil.rmtree(tmp)


if __name__ == '__main__':
    unittest.main()

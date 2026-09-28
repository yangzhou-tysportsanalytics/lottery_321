"""The rollover-adjusted dominance profile and the tail-value identity."""
import sys, unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parents[2] / 'src' / 'lottery321'
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / 'ledgers'))

import analysis as S  # noqa: E402
import exploratory_4 as R7  # noqa: E402
from value import CURVES  # noqa: E402


class RolloverDominance(unittest.TestCase):
    def test_tau_rho_is_the_abel_sum_of_c_rho(self):
        rng = np.random.default_rng(7)
        db = rng.normal(size=(50, 30)) * 0.01
        for rho in S.RHOS:
            Cr = R7.c_rho_batches(db, rho)
            for name, v in CURVES.items():
                a = np.append(v[:-1] - v[1:], v[-1])          # a_j = v(j) - v(j+1), a_30 = v(30)
                lhs = S.tau_rho(db, rho)[name][0]
                rhs = float((Cr @ a).mean())
                self.assertAlmostEqual(lhs, rhs, places=12)

    def test_own_pick_profile_is_unchanged_when_m_is_zero(self):
        rng = np.random.default_rng(8)
        db = rng.normal(size=(50, 30)); db -= db.mean(1, keepdims=True)   # each batch sums to zero: M = 0
        Cr = R7.c_rho_batches(db, 0.8)
        np.testing.assert_allclose(Cr, np.cumsum(db, axis=1), atol=1e-12)

    def test_tail_value_identity(self):
        rng = np.random.default_rng(9)
        db = rng.normal(size=(50, 30)) * 0.01
        v = CURVES['linear']; a = 0.1
        va = a + (1 - a) * v
        np.testing.assert_allclose(db @ va, (1 - a) * (db @ v) + a * db.sum(1), atol=1e-12)


if __name__ == '__main__':
    unittest.main()

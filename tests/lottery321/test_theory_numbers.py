"""Appendix B must agree with Section 3: every recomputed number matches the quoted one."""
import sys, tempfile, unittest
from pathlib import Path
R = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(R / 'src/lottery321'))
import theory_numbers as N


class AppendixB(unittest.TestCase):
    def test_every_quoted_number_is_reproduced(self):
        self.assertEqual(N.check(), [])

    def test_tolerance_is_half_a_unit_in_the_last_quoted_decimal(self):
        """The tolerance is half a unit in the last quoted decimal: the convex-curve value -0.041475 printed
        as -0.042 (error 0.000525) must fail."""
        self.assertAlmostEqual(N._tol(3.66), 0.005, places=9)
        self.assertAlmostEqual(N._tol(-0.041), 0.0005, places=9)
        self.assertAlmostEqual(N._tol(12.0), 0.05, places=9)
        self.assertGreater(abs(-0.041475 - (-0.042)), N._tol(-0.042))   # a mis-rounded value is caught
        self.assertLess(abs(-0.041475 - (-0.041)), N._tol(-0.041))      # the correctly rounded value passes

    def test_a_wrong_quote_is_caught(self):
        rs = list(N.rows())
        name, quoted, got, want, fn, test = rs[4]          # expected slot, positions 1-3
        rs[4] = (name, quoted, got, want + 0.5, fn, test)
        self.assertTrue(N.check(rs))

    def test_table_is_written_with_every_row(self):
        with tempfile.TemporaryDirectory() as t:
            p, n = N.write(Path(t) / 'appB.md')
            text = Path(p).read_text()
            self.assertEqual(n, len(N.rows()))
            self.assertEqual(text.count('\n|'), n + 2)      # header, separator, and one line per number
            self.assertIn('-1/37', text)
            self.assertIn('Corollary 2 tau, linear curve', text)
            self.assertNotIn('Corollary 3', text)


if __name__ == '__main__':
    unittest.main()

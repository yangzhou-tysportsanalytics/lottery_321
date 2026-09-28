"""Tests for the reachable-slot support of the state-conditional router features (A1 amendment 9 item 9). Uses the real 2023-24 window state but only a few hundred worlds; reads no simulation output."""
import json, sys, tempfile, unittest
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src/lottery321'))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src/lottery321/ledgers'))
import reachable_slots as R
from teams import TEAMS


class Counts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = R.counts_for_season('2023-24', n=400, seed=1)
        cls.old = np.asarray(cls.r['old']); cls.new = np.asarray(cls.r['new'])

    def test_every_world_is_a_permutation(self):
        for M in (self.old, self.new):
            self.assertTrue(np.all(M.sum(0) == 400))     # one team per slot
            self.assertTrue(np.all(M.sum(1) == 400))     # one slot per team

    def test_starts_from_the_first_window_day(self):
        import elo as E, simulate as H
        self.assertEqual(self.r['day'], next(iter(H.window_days(E.load_games(H.GAMES), '2023-24'))))

    def test_contenders_cannot_reach_the_lottery_and_no_team_reaches_everything(self):
        reach = self.old > 0
        self.assertTrue(np.all(reach.sum(1) >= 1))
        self.assertTrue(np.any(reach.sum(1) < 30))       # the window is late enough to exclude slots
        # a team that can reach slot 1 under the old rule must be a lottery team, so it cannot also
        # reach the last slot, which belongs to the best record in the league
        for t in np.nonzero(reach[:, 0])[0]:
            self.assertFalse(reach[t, 29])

    def test_the_relegation_floor_widens_the_new_rules_reach_for_the_worst_teams(self):
        """Under 3-2-1 the three worst cannot fall past 12, but 16 teams are drawn, so the field is wider:
        the union over teams of reachable slots is at least as large under the new rule."""
        self.assertGreaterEqual((self.new > 0).sum(), (self.old > 0).sum())

    def test_load_roundtrip(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'reach.json'
            p.write_text(json.dumps({'worlds': 400, 'teams': list(TEAMS), 'seasons': [self.r]}), encoding='utf-8')
            m = R.load(p)
            self.assertEqual(sorted(m), [('2023-24', 'new'), ('2023-24', 'old')])
            self.assertEqual(m[('2023-24', 'old')].dtype, np.dtype(bool))
            np.testing.assert_array_equal(m[('2023-24', 'old')], self.old > 0)


if __name__ == '__main__':
    unittest.main()

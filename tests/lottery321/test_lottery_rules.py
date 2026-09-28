import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src/lottery321'))
from lottery_rules import sequential_feasible, standard_field, feasible, N_LOTTERY, flattened_2019

OFFICIAL = {  # NBA 3-2-1 attachment page 2 (2026-05), picks 1..16, percent, assumes no restrictions
    'bottom3': [5.4, 5, 6, 6, 6, 6, 6, 6, 6, 8, 14, 25, 0, 0, 0, 0],
    'non_playin': [8.1, 8, 8, 8, 8, 7, 7, 7, 7, 6, 4, 2, 7, 6, 5, 3],
    'playin_9_10': [5.4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 5, 2, 9, 9, 9, 7],
    'playin_7_8_losers': [2.7, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 2, 8, 10, 15, 27]}
REP = {'bottom3': 'bottom3_0', 'non_playin': 'non_playin_3', 'playin_9_10': 'playin_9_10_10',
       'playin_7_8_losers': 'playin_7_8_losers_14'}


class ThreeTwoOne(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.field = standard_field()
        cls.base = sequential_feasible(*cls.field)

    def test_rows_and_columns_sum_to_one(self):
        for t, d in self.base.items():
            self.assertAlmostEqual(sum(d), 1.0, places=12)
        for k in range(N_LOTTERY):
            self.assertAlmostEqual(sum(d[k] for d in self.base.values()), 1.0, places=12)

    def test_relegated_floor_twelve(self):
        for t, d in self.base.items():
            if t.startswith('bottom3'):
                self.assertEqual(sum(d[12:]), 0.0)

    def test_matches_official_printed_odds_after_rounding(self):
        for g, t in REP.items():
            for k, v in enumerate(self.base[t]):
                ours = round(100 * v, 1 if k == 0 else 0)
                self.assertEqual(ours, OFFICIAL[g][k], f'{g} pick {k+1}')

    def test_no_top5_restriction_and_no_first_pick_restriction(self):
        teams, balls, mx, mn = standard_field({'non_playin_3': 6, 'bottom3_0': 2})
        d = sequential_feasible(teams, balls, mx, mn)
        self.assertEqual(sum(d['non_playin_3'][:5]), 0.0)
        self.assertEqual(d['bottom3_0'][0], 0.0)
        for t in teams:
            self.assertAlmostEqual(sum(d[t]), 1.0, places=12)
        # a restricted relegated team still respects its floor
        self.assertEqual(sum(d['bottom3_0'][12:]), 0.0)

    def test_feasibility_detects_impossible_floor(self):
        mx = {'a': 1, 'b': 1}; mn = {'a': 1, 'b': 1}
        self.assertFalse(feasible(['a', 'b'], 1, mx, mn, n=2))



class Flattened2019(unittest.TestCase):
    OFFICIAL = {0: [14.0, 13.4, 12.7, 12.0, 47.9], 4: [10.5, 10.5, 10.6, 10.5, 2.2, 19.6, 26.7, 8.7, 0.6],
                13: [0.5, 0.6, 0.6, 0.7] + [0.0] * 9 + [97.6]}

    def test_matches_official_2019_table(self):
        d = flattened_2019()
        for i, row in self.OFFICIAL.items():
            self.assertEqual([round(100 * x, 1) for x in d[i][:len(row)]], row)

    def test_doubly_stochastic(self):
        d = flattened_2019()
        for i in range(14):
            self.assertAlmostEqual(sum(d[i]), 1.0, places=12)
            self.assertAlmostEqual(sum(d[j][i] for j in range(14)), 1.0, places=12)

    def test_no_team_drops_more_than_four(self):
        d = flattened_2019()
        for i in range(14):
            self.assertAlmostEqual(sum(d[i][min(i + 5, 14):]), 0.0, places=15)


class FeasibleCrossCheck(unittest.TestCase):
    def test_hall_check_equals_greedy_reference(self):
        import random
        from lottery_rules import feasible, feasible_greedy
        rng = random.Random(7); n_true = 0
        for _ in range(30000):
            p = rng.randint(1, 16); k = 16 - p + 1 + rng.choice([0, 0, 0, 0, -1, 1]); ts = list(range(max(k, 0)))
            mx = {t: rng.choice([12, 16, 16, 16, rng.randint(1, 16)]) for t in ts}
            mn = {t: rng.choice([1, 1, 1, 2, 6, rng.randint(1, 16)]) for t in ts}
            a = feasible(ts, p, mx, mn); self.assertEqual(a, feasible_greedy(ts, p, mx, mn)); n_true += a
        self.assertGreater(n_true, 1000)


class FastFeasibility(unittest.TestCase):
    def test_count_rule_equals_hall_in_the_321_family(self):
        import random
        from lottery_rules import feasible, feasible_hall, _count_rule_applies
        rng = random.Random(3); n_fast = 0
        for _ in range(40000):
            p = rng.randint(1, 16); ts = list(range(16 - p + 1))
            rel = rng.sample(ts, min(len(ts), rng.randint(0, 4)))
            mx = {t: (12 if t in rel else 16) for t in ts}; mn = {t: 1 for t in ts}
            for t in rng.sample(ts, min(len(ts), rng.randint(0, 2))):
                mn[t] = rng.choice([2, 6])
            self.assertEqual(feasible(ts, p, mx, mn), feasible_hall(ts, p, mx, mn))
            n_fast += _count_rule_applies(ts, mx, mn, 16)
        self.assertEqual(n_fast, 40000)


class FastKernel(unittest.TestCase):
    def test_sequential_feasible_shortcut_equals_exact(self):
        from lottery_rules import sequential_feasible, standard_field
        names = standard_field()[0]
        for idx in ({}, {3: 6}, {0: 6, 6: 2}, {2: 2, 15: 6}, {1: 6, 4: 6}):
            teams, balls, mx, mn = standard_field({names[k]: v for k, v in idx.items()})
            a = sequential_feasible(teams, balls, mx, mn)
            b = sequential_feasible(teams, balls, mx, mn, force_exact=True)
            for t in teams:
                for x, y in zip(a[t], b[t]):
                    self.assertAlmostEqual(x, y, places=13)


if __name__ == '__main__':
    unittest.main()

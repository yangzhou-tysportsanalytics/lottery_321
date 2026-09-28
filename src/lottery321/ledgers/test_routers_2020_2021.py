import json, random, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import router_2020 as L20
import router_2021 as L21

MODS = {2020: (L20, L20.Router2020), 2021: (L21, L21.Router2021)}


def perm(teams, seed):
    rng = random.Random(seed); p = list(range(1, 31)); rng.shuffle(p)
    return dict(zip(teams, p))


def place(teams, order):
    rest = [x for x in range(1, 31) if x not in order.values()]
    p = dict(order); p.update(dict(zip([t for t in teams if t not in order], rest)))
    return p


class Common:
    YEAR = None

    @property
    def M(self): return MODS[self.YEAR][0]

    @property
    def R(self): return MODS[self.YEAR][1]

    def test_realized(self):
        led = json.loads((HERE / f'ledger_{self.YEAR}_draft.json').read_text())
        pos = {v['native']: int(k) for k, v in led['realized'].items()}
        out = self.M.route(pos)
        for k, v in led['realized'].items():
            s = int(k)
            if s in self.M.POST_DEADLINE_CHANGES:
                dl, dr, _ = self.M.POST_DEADLINE_CHANGES[s]
                self.assertEqual(dr, v['holder'], s)
                self.assertEqual(out[s], dl, s)
            else:
                self.assertEqual(out[s], v['holder'], s)

    def test_conservation(self):
        teams = set(self.M.TEAMS)
        for s in range(20000):
            out = self.M.route(perm(self.M.TEAMS, s))
            self.assertEqual(sorted(out), list(range(1, 31)))
            self.assertTrue(set(out.values()) <= teams)

    def test_decomposition(self):
        for s in range(2000):
            p = perm(self.M.TEAMS, 50_000 + s); full = self.M.route(p)
            got = {p[t]: self.R.simple(t, p[t]) for t in self.R.simple_natives}
            got.update(self.R.pooled(p))
            self.assertEqual(got, full)

    def test_rejects_non_permutation(self):
        with self.assertRaises(ValueError):
            self.M.route({t: 1 for t in self.M.TEAMS})

    def check(self, order, expect):
        out = self.M.route(place(self.M.TEAMS, order))
        for slot, holder in expect.items():
            self.assertEqual(out[slot], holder, (order, slot))


class Hist2020(Common, unittest.TestCase):
    YEAR = 2020

    def test_boundaries(self):
        cases = [('BKN', 14, 'BKN'), ('BKN', 15, 'MIN'), ('PHI', 14, 'PHI'), ('PHI', 15, 'BKN'),
                 ('CLE', 10, 'CLE'), ('CLE', 11, 'NOP'), ('IND', 14, 'IND'), ('IND', 15, 'MIL'),
                 ('MIL', 7, 'MIL'), ('MIL', 8, 'BOS'), ('DEN', 10, 'DEN'), ('DEN', 11, 'OKC'),
                 ('OKC', 20, 'OKC'), ('OKC', 21, 'PHI'), ('GSW', 20, 'GSW'), ('GSW', 21, 'BKN'),
                 ('MEM', 6, 'MEM'), ('MEM', 7, 'BOS'),
                 ('UTA', 7, 'UTA'), ('UTA', 8, 'MEM'), ('UTA', 14, 'MEM'), ('UTA', 15, 'UTA'),
                 ('LAC', 1, 'NYK'), ('LAC', 30, 'NYK'), ('HOU', 1, 'DEN'), ('HOU', 30, 'DEN'),
                 ('ATL', 1, 'ATL'), ('ATL', 30, 'ATL')]
        for t, s, h in cases:
            self.check({t: s}, {s: h})

    def test_no_pools(self):
        self.assertEqual(self.R.pools, ()); self.assertEqual(len(self.R.simple_natives), 30)


class Hist2021(Common, unittest.TestCase):
    YEAR = 2021

    def test_simple_boundaries(self):
        cases = [('MIL', 9, 'MIL'), ('MIL', 10, 'HOU'), ('LAL', 7, 'NOP'), ('LAL', 8, 'LAL'),
                 ('MIN', 3, 'MIN'), ('MIN', 4, 'GSW'), ('CHI', 4, 'CHI'), ('CHI', 5, 'ORL'),
                 ('GSW', 20, 'GSW'), ('GSW', 21, 'OKC'),
                 ('UTA', 7, 'UTA'), ('UTA', 8, 'MEM'), ('UTA', 14, 'MEM'), ('UTA', 15, 'UTA'),
                 ('DAL', 1, 'NYK'), ('DAL', 30, 'NYK'), ('BOS', 16, 'BOS')]
        for t, s, h in cases:
            self.check({t: s}, {s: h})

    def test_por_det_protection_boundaries(self):
        # BKN at 30 so the BKN swap never triggers
        self.check({'POR': 14, 'BKN': 30, 'HOU': 2}, {14: 'POR'})
        self.check({'POR': 15, 'BKN': 30, 'HOU': 2}, {15: 'HOU'})
        self.check({'DET': 16, 'BKN': 30, 'HOU': 2}, {16: 'DET'})
        self.check({'DET': 17, 'BKN': 30, 'HOU': 2}, {17: 'HOU'})

    def test_hou_top4_protected(self):
        self.check({'HOU': 4, 'OKC': 6, 'MIA': 18, 'BKN': 27, 'POR': 23},
                   {4: 'HOU', 6: 'OKC', 18: 'OKC', 27: 'BKN', 23: 'HOU'})

    def test_hou_outside_top4_okc_takes_best_two(self):
        self.check({'HOU': 5, 'OKC': 12, 'MIA': 20, 'BKN': 28, 'POR': 10, 'DET': 1},
                   {5: 'OKC', 12: 'OKC', 20: 'HOU', 28: 'BKN', 10: 'POR', 1: 'DET'})
        self.check({'HOU': 25, 'OKC': 3, 'MIA': 9, 'BKN': 29, 'POR': 11, 'DET': 2},
                   {3: 'OKC', 9: 'OKC', 25: 'HOU', 29: 'BKN'})

    def test_bkn_swap_takes_step1_pick(self):
        # HOU outside top 4, HOU ends with MIA's 20; BKN at 8 better -> HOU takes 8, BKN gets 20
        self.check({'HOU': 5, 'OKC': 12, 'MIA': 20, 'BKN': 8, 'POR': 10, 'DET': 1},
                   {5: 'OKC', 12: 'OKC', 8: 'HOU', 20: 'BKN', 10: 'POR'})

    def test_bkn_swap_gives_worst_of_eligible_incl_por(self):
        # HOU keeps own #3; POR conveys at 24; BKN at 18 -> HOU swaps POR's 24 for 18
        self.check({'HOU': 3, 'OKC': 6, 'MIA': 12, 'BKN': 18, 'POR': 24, 'DET': 1},
                   {3: 'HOU', 6: 'OKC', 12: 'OKC', 18: 'HOU', 24: 'BKN'})
        # DET conveys at 26 and is the worst eligible pick
        self.check({'HOU': 3, 'OKC': 6, 'MIA': 12, 'BKN': 18, 'POR': 10, 'DET': 26},
                   {3: 'HOU', 18: 'HOU', 26: 'BKN', 10: 'POR'})

    def test_bkn_swap_not_exercised_when_worse(self):
        self.check({'HOU': 2, 'POR': 23, 'BKN': 27, 'DET': 1},
                   {2: 'HOU', 23: 'HOU', 27: 'BKN', 1: 'DET'})

    def test_mil_pick_not_swappable_with_bkn(self):
        self.check({'HOU': 2, 'MIL': 25, 'BKN': 20, 'POR': 5, 'DET': 1},
                   {2: 'HOU', 25: 'HOU', 20: 'BKN'})

    def test_nyk_lac_swap(self):
        self.check({'NYK': 19, 'LAC': 25}, {19: 'NYK', 25: 'LAC'})
        self.check({'NYK': 15, 'LAC': 5}, {5: 'NYK', 15: 'LAC'})
        self.check({'NYK': 15, 'LAC': 4}, {4: 'LAC', 15: 'NYK'})   # ASSUMPTION branch

    def test_post_deadline_changes(self):
        self.assertEqual(set(self.M.POST_DEADLINE_CHANGES), {16})


if __name__ == '__main__':
    unittest.main()

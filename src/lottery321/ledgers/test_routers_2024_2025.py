import json, random, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import router_2024 as L24
import router_2025 as L25

TEAMS = L24.TEAMS


def perm(seed):
    rng = random.Random(seed); p = list(range(1, 31)); rng.shuffle(p)
    return dict(zip(TEAMS, p))


def fix(order):
    """Permutation with the given natives pinned; others fill remaining slots in TEAMS order."""
    rest = [x for x in range(1, 31) if x not in order.values()]
    p = dict(order); p.update(dict(zip([t for t in TEAMS if t not in order], rest)))
    return p


def realized(year):
    with open(HERE / f'ledger_{year}_draft.json') as fh:
        d = json.load(fh)['realized']
    pos = {v['native']: int(k) for k, v in d.items()}
    return pos, {int(k): v['holder'] for k, v in d.items()}


class Common:
    M = None; R = None; YEAR = None

    def test_modules_share_teams(self):
        self.assertEqual(self.M.TEAMS, TEAMS)

    def test_realized(self):
        pos, holder = realized(self.YEAR)
        out = self.M.route(pos)
        for s in range(1, 31):
            if s in self.M.POST_DEADLINE_CHANGES:
                dl, dr, _ = self.M.POST_DEADLINE_CHANGES[s]
                self.assertEqual(out[s], dl, s); self.assertEqual(holder[s], dr, s)
            else:
                self.assertEqual(out[s], holder[s], s)

    def test_conservation(self):
        for s in range(20000):
            out = self.M.route(perm(s))
            self.assertEqual(sorted(out), list(range(1, 31)))
            self.assertTrue(set(out.values()) <= set(TEAMS))

    def test_decomposition(self):
        for s in range(2000):
            p = perm(50_000 + s); full = self.M.route(p)
            got = {p[t]: self.R.simple(t, p[t]) for t in self.R.simple_natives}
            got.update(self.R.pooled(p))
            self.assertEqual(got, full)

    def test_rejects_non_permutation(self):
        with self.assertRaises(ValueError):
            self.M.route({t: 1 for t in TEAMS})

    def boundaries(self, cases):
        for native, keep_hi, dest in cases:
            for slot, h in [(keep_hi, native), (keep_hi + 1, dest)]:
                self.assertEqual(self.M.route(fix({native: slot}))[slot], h, (native, slot))
                self.assertEqual(self.R.simple(native, slot), h)


class Hist2024(Common, unittest.TestCase):
    M = L24; R = L24.Router2024; YEAR = 2024

    def test_boundaries(self):
        self.boundaries([('TOR', 6, 'SAS'), ('DET', 18, 'NYK'), ('IND', 3, 'TOR'), ('CHA', 14, 'SAS'),
                         ('POR', 14, 'CHI'), ('GSW', 4, 'POR'), ('SAC', 14, 'ATL'), ('DAL', 10, 'NYK')])

    def test_unconditional(self):
        for s in (1, 30):
            out = L24.route(fix({'BKN': s, 'LAL': 31 - s}))
            self.assertEqual(out[s], 'HOU'); self.assertEqual(out[31 - s], 'NOP')

    # WAS / PHX / MEM
    def test_was_boundary_and_swap(self):
        o = L24.route(fix({'WAS': 12, 'PHX': 5, 'MEM': 20}))
        self.assertEqual((o[5], o[12], o[20]), ('WAS', 'MEM', 'PHX'))
        o = L24.route(fix({'WAS': 13, 'PHX': 5, 'MEM': 20}))
        self.assertEqual((o[13], o[5], o[20]), ('NYK', 'MEM', 'PHX'))

    def test_was_realized_like_no_swaps(self):
        o = L24.route(fix({'WAS': 2, 'MEM': 9, 'PHX': 22}))
        self.assertEqual((o[2], o[9], o[22]), ('WAS', 'MEM', 'PHX'))

    def test_mem_best_keeps(self):
        o = L24.route(fix({'MEM': 1, 'WAS': 5, 'PHX': 8}))
        self.assertEqual((o[1], o[5], o[8]), ('MEM', 'WAS', 'PHX'))

    def test_was_to_nyk_mem_vs_phx_only(self):
        o = L24.route(fix({'WAS': 20, 'MEM': 25, 'PHX': 22}))
        self.assertEqual((o[20], o[22], o[25]), ('NYK', 'MEM', 'PHX'))
        o = L24.route(fix({'WAS': 20, 'MEM': 21, 'PHX': 22}))
        self.assertEqual((o[20], o[21], o[22]), ('NYK', 'MEM', 'PHX'))

    # OKC pool
    def test_okc_pool_four(self):
        o = L24.route(fix({'HOU': 12, 'UTA': 11, 'LAC': 26, 'OKC': 29}))
        self.assertEqual((o[11], o[12], o[26], o[29]), ('OKC', 'OKC', 'WAS', 'UTA'))

    def test_okc_pool_boundaries(self):
        o = L24.route(fix({'HOU': 4, 'UTA': 10, 'LAC': 26, 'OKC': 29}))
        self.assertEqual((o[4], o[10], o[26], o[29]), ('HOU', 'UTA', 'WAS', 'UTA'))
        o = L24.route(fix({'HOU': 5, 'UTA': 10, 'LAC': 26, 'OKC': 29}))
        self.assertEqual((o[5], o[10], o[26], o[29]), ('OKC', 'UTA', 'WAS', 'UTA'))
        o = L24.route(fix({'HOU': 4, 'UTA': 11, 'LAC': 26, 'OKC': 29}))
        self.assertEqual((o[4], o[11], o[26], o[29]), ('HOU', 'OKC', 'WAS', 'UTA'))

    def test_okc_pool_conveyed_pick_worst(self):
        o = L24.route(fix({'HOU': 28, 'UTA': 11, 'LAC': 20, 'OKC': 25}))
        self.assertEqual((o[11], o[20], o[25], o[28]), ('OKC', 'OKC', 'WAS', 'UTA'))

    def test_mil_nop_swap(self):
        o = L24.route(fix({'MIL': 21, 'NOP': 23}))
        self.assertEqual((o[21], o[23]), ('NOP', 'MIL'))
        o = L24.route(fix({'MIL': 23, 'NOP': 21}))
        self.assertEqual((o[21], o[23]), ('NOP', 'MIL'))


class Hist2025(Common, unittest.TestCase):
    M = L25; R = L25.Router2025; YEAR = 2025

    def test_boundaries(self):
        self.boundaries([('PHI', 6, 'OKC'), ('DET', 13, 'MIN'), ('CHA', 14, 'SAC'), ('MIA', 14, 'OKC'),
                         ('WAS', 10, 'NYK'), ('DEN', 5, 'ORL'), ('UTA', 10, 'OKC'), ('POR', 14, 'CHI'),
                         ('GSW', 10, 'MIA'), ('SAC', 12, 'ATL'), ('MEM', 14, 'WAS')])

    def test_mil_boundary(self):
        self.assertEqual(L25.route(fix({'MIL': 4}))[4], 'NOP')
        self.assertEqual(L25.route(fix({'MIL': 5}))[5], 'BKN')

    def test_unconditional(self):
        o = L25.route(fix({'NYK': 1, 'ATL': 2, 'LAL': 3}))
        self.assertEqual((o[1], o[2], o[3]), ('BKN', 'SAS', 'ATL'))

    def test_cle_min(self):
        o = L25.route(fix({'CLE': 29, 'MIN': 21}))
        self.assertEqual((o[21], o[29]), ('UTA', 'PHX'))
        o = L25.route(fix({'CLE': 3, 'MIN': 21}))
        self.assertEqual((o[3], o[21]), ('UTA', 'PHX'))

    # OKC / LAC / HOU / PHX / BKN network
    def test_network_lac_branch(self):
        o = L25.route(fix({'OKC': 30, 'LAC': 24, 'HOU': 27, 'PHX': 10}))
        self.assertEqual((o[10], o[24], o[27], o[30]), ('HOU', 'OKC', 'BKN', 'LAC'))

    def test_network_hou_branch(self):
        o = L25.route(fix({'OKC': 30, 'LAC': 24, 'HOU': 20, 'PHX': 10}))
        self.assertEqual((o[10], o[20], o[24], o[30]), ('HOU', 'OKC', 'LAC', 'BKN'))
        o = L25.route(fix({'OKC': 30, 'LAC': 24, 'HOU': 20, 'PHX': 29}))
        self.assertEqual((o[20], o[24], o[29], o[30]), ('OKC', 'LAC', 'HOU', 'BKN'))

    def test_network_hou_protection_boundary(self):
        o = L25.route(fix({'OKC': 30, 'LAC': 24, 'HOU': 10, 'PHX': 15}))
        self.assertEqual((o[10], o[15], o[24], o[30]), ('HOU', 'BKN', 'OKC', 'LAC'))
        o = L25.route(fix({'OKC': 30, 'LAC': 24, 'HOU': 11, 'PHX': 15}))
        self.assertEqual((o[11], o[15], o[24], o[30]), ('OKC', 'HOU', 'LAC', 'BKN'))

    def test_network_no_okc_swap(self):
        o = L25.route(fix({'OKC': 3, 'LAC': 24, 'HOU': 20, 'PHX': 29}))
        self.assertEqual((o[3], o[20], o[24], o[29]), ('OKC', 'HOU', 'LAC', 'BKN'))


if __name__ == '__main__':
    unittest.main()

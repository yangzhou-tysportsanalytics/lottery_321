import json, random, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import router_2022 as L22
import router_2023 as L23

MODS = {2022: (L22, L22.Router2022), 2023: (L23, L23.Router2023)}


def perm(teams, seed):
    rng = random.Random(seed); p = list(range(1, 31)); rng.shuffle(p)
    return dict(zip(teams, p))


def place(teams, order):
    rest = [x for x in range(1, 31) if x not in order.values()]
    p = dict(order); p.update(dict(zip([t for t in teams if t not in order], rest)))
    return p


class Common(unittest.TestCase):
    def test_realized(self):
        for y, (M, _) in MODS.items():
            led = json.loads((HERE / f'ledger_{y}_draft.json').read_text())
            pos = {v['native']: int(k) for k, v in led['realized'].items()}
            out = M.route(pos)
            for k, v in led['realized'].items():
                s = int(k)
                if s in M.POST_DEADLINE_CHANGES:
                    dl, dr, _note = M.POST_DEADLINE_CHANGES[s]
                    self.assertEqual(out[s], dl, (y, s)); self.assertEqual(v['holder'], dr, (y, s))
                else:
                    self.assertEqual(out[s], v['holder'], (y, s))

    def test_conservation(self):
        for y, (M, _) in MODS.items():
            for s in range(20000):
                out = M.route(perm(M.TEAMS, y * 100000 + s))
                self.assertEqual(sorted(out), list(range(1, 31)))
                self.assertTrue(set(out.values()) <= set(M.TEAMS))

    def test_decomposition(self):
        for y, (M, R) in MODS.items():
            self.assertEqual(set(R.simple_natives) | {t for p in R.pools for t in p}, set(M.TEAMS))
            for s in range(2000):
                p = perm(M.TEAMS, 7 * y + 1_000_000 + s); full = M.route(p)
                got = {p[t]: R.simple(t, p[t]) for t in R.simple_natives}
                got.update(R.pooled(p))
                self.assertEqual(got, full)

    def test_rejects_non_permutation(self):
        for M, _ in MODS.values():
            with self.assertRaises(ValueError):
                M.route({t: 1 for t in M.TEAMS})

    def test_metadata(self):
        for M, _ in MODS.values():
            self.assertTrue(all(isinstance(a, str) for a in M.ASSUMPTIONS))
            for s, (a, b, n) in M.POST_DEADLINE_CHANGES.items():
                self.assertIn(a, M.TEAMS); self.assertIn(b, M.TEAMS); self.assertTrue(1 <= s <= 30)


class Boundaries2022(unittest.TestCase):
    T = L22.TEAMS

    def chk(self, native, slot, holder):
        self.assertEqual(L22.route(place(self.T, {native: slot}))[slot], holder, (native, slot))

    def test_simple_protections(self):
        for n, k, x in [('DET', 16, 'OKC'), ('OKC', 14, 'ATL'), ('POR', 14, 'CHI'), ('CHA', 18, 'ATL'),
                        ('TOR', 14, 'SAS'), ('CLE', 14, 'IND'), ('BOS', 4, 'SAS'), ('UTA', 6, 'MEM'),
                        ('PHX', 12, 'OKC')]:
            self.chk(n, k, n); self.chk(n, k + 1, x)

    def test_unconditional(self):
        for s in (1, 30):
            self.chk('LAC', s, 'OKC'); self.chk('PHI', s, 'BKN')

    def test_nop_three_way(self):
        for s, h in [(1, 'NOP'), (4, 'NOP'), (5, 'POR'), (14, 'POR'), (15, 'CHA'), (30, 'CHA')]:
            self.chk('NOP', s, h)

    def test_lal_split(self):
        for s, h in [(1, 'NOP'), (10, 'NOP'), (11, 'MEM'), (30, 'MEM')]:
            self.chk('LAL', s, h)

    def test_bkn_hou_mia_pool(self):
        o = L22.route(place(self.T, {'HOU': 3, 'BKN': 17, 'MIA': 27}))
        self.assertEqual((o[3], o[17], o[27]), ('HOU', 'HOU', 'MIA'))
        o = L22.route(place(self.T, {'HOU': 3, 'BKN': 20, 'MIA': 15}))  # MIA 15 unprotected: HOU swaps
        self.assertEqual((o[3], o[15], o[20]), ('HOU', 'HOU', 'MIA'))
        o = L22.route(place(self.T, {'HOU': 3, 'BKN': 20, 'MIA': 14}))  # MIA 14 protected
        self.assertEqual((o[3], o[14], o[20]), ('HOU', 'MIA', 'HOU'))
        o = L22.route(place(self.T, {'HOU': 25, 'BKN': 20, 'MIA': 16}))  # HOU own worst -> MIA gets it
        self.assertEqual((o[16], o[20], o[25]), ('HOU', 'HOU', 'MIA'))


class Boundaries2023(unittest.TestCase):
    T = L23.TEAMS

    def chk(self, native, slot, holder):
        self.assertEqual(L23.route(place(self.T, {native: slot}))[slot], holder, (native, slot))

    def test_simple_protections(self):
        for n, k, x in [('DET', 18, 'NYK'), ('CHA', 16, 'SAS'), ('DAL', 10, 'NYK'), ('NYK', 14, 'POR'),
                        ('CLE', 14, 'IND'), ('BOS', 12, 'IND'), ('DEN', 14, 'CHA'), ('CHI', 4, 'ORL'),
                        ('WAS', 14, 'NYK'), ('POR', 14, 'CHI')]:
            self.chk(n, k, n); self.chk(n, k + 1, x)

    def test_unconditional(self):
        for s in (1, 30):
            self.chk('MIN', s, 'UTA'); self.chk('PHX', s, 'BKN')

    def test_bkn_hou_phi(self):
        o = L23.route(place(self.T, {'HOU': 4, 'BKN': 22, 'PHI': 28}))
        self.assertEqual((o[4], o[22], o[28]), ('HOU', 'BKN', 'UTA'))
        o = L23.route(place(self.T, {'HOU': 20, 'BKN': 5, 'PHI': 28}))  # HOU swaps into BKN's
        self.assertEqual((o[5], o[20], o[28]), ('HOU', 'BKN', 'UTA'))
        o = L23.route(place(self.T, {'HOU': 20, 'BKN': 25, 'PHI': 2}))  # PHI best -> BKN
        self.assertEqual((o[2], o[20], o[25]), ('BKN', 'HOU', 'UTA'))

    def test_lac_mil_okc(self):
        o = L23.route(place(self.T, {'OKC': 12, 'LAC': 20, 'MIL': 30}))  # realized
        self.assertEqual((o[12], o[20], o[30]), ('OKC', 'HOU', 'LAC'))
        o = L23.route(place(self.T, {'OKC': 20, 'LAC': 12, 'MIL': 30}))  # OKC swaps with LAC
        self.assertEqual((o[12], o[20], o[30]), ('OKC', 'HOU', 'LAC'))
        o = L23.route(place(self.T, {'OKC': 3, 'LAC': 6, 'MIL': 30}))  # LAC-held pick at 6: protected
        self.assertEqual((o[3], o[6], o[30]), ('OKC', 'LAC', 'HOU'))
        o = L23.route(place(self.T, {'OKC': 3, 'LAC': 7, 'MIL': 30}))  # at 7: HOU swaps
        self.assertEqual((o[3], o[7], o[30]), ('OKC', 'HOU', 'LAC'))
        o = L23.route(place(self.T, {'OKC': 20, 'LAC': 25, 'MIL': 8}))  # MIL best: HOU keeps MIL
        self.assertEqual((o[8], o[20], o[25]), ('HOU', 'OKC', 'LAC'))

    def test_lal_nop(self):
        o = L23.route(place(self.T, {'LAL': 5, 'NOP': 20}))
        self.assertEqual((o[5], o[20]), ('NOP', 'LAL'))
        o = L23.route(place(self.T, {'LAL': 17, 'NOP': 14}))
        self.assertEqual((o[14], o[17]), ('NOP', 'LAL'))


if __name__ == '__main__':
    unittest.main()

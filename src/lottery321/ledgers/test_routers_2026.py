import json, random, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import router_2026 as L
from router_2026 import route, TEAMS, Router2026 as R


def perm(seed):
    rng = random.Random(seed); p = list(range(1, 31)); rng.shuffle(p)
    return dict(zip(TEAMS, p))


def fix(order):
    """Permutation with the given natives pinned; others fill remaining slots in TEAMS order."""
    assert len(set(order.values())) == len(order)
    rest = [x for x in range(1, 31) if x not in order.values()]
    p = dict(order); p.update(dict(zip([t for t in TEAMS if t not in order], rest)))
    return p


class Hist2026(unittest.TestCase):
    def check(self, order, expect):
        out = route(fix(order))
        for native, holder in expect.items():
            self.assertEqual(out[order[native]], holder, (native, order, out[order[native]]))

    # (1) realized
    def test_realized(self):
        with open(HERE / 'ledger_2026_draft.json') as fh:
            d = json.load(fh)['realized']
        pos = {v['native']: int(k) for k, v in d.items()}
        holder = {int(k): v['holder'] for k, v in d.items()}
        out = route(pos)
        for s in range(1, 31):
            if s in L.POST_DEADLINE_CHANGES:
                dl, dr, _ = L.POST_DEADLINE_CHANGES[s]
                self.assertEqual(out[s], dl, s); self.assertEqual(holder[s], dr, s)
            else:
                self.assertEqual(out[s], holder[s], s)

    # (2) conservation
    def test_conservation(self):
        for s in range(20000):
            out = route(perm(s))
            self.assertEqual(sorted(out), list(range(1, 31)))
            self.assertTrue(set(out.values()) <= set(TEAMS))

    # (3) decomposition
    def test_decomposition(self):
        for s in range(2000):
            p = perm(50_000 + s); full = route(p)
            got = {p[t]: R.simple(t, p[t]) for t in R.simple_natives}
            got.update(R.pooled(p))
            self.assertEqual(got, full)

    def test_rejects_non_permutation(self):
        with self.assertRaises(ValueError):
            route({t: 1 for t in TEAMS})

    def test_all_assumptions_documented(self):
        src = (HERE / 'router_2026.py').read_text()
        self.assertGreaterEqual(len(L.ASSUMPTIONS), src.count('# ASSUMPTION'))

    # (4) boundaries: simple natives
    def test_simple_boundaries(self):
        for native, slot, holder in [('IND', 4, 'IND'), ('IND', 5, 'LAC'), ('IND', 9, 'LAC'), ('IND', 10, 'IND'),
                                     ('PHI', 4, 'PHI'), ('PHI', 5, 'OKC'), ('POR', 14, 'POR'), ('POR', 15, 'CHI')]:
            self.assertEqual(route(fix({native: slot}))[slot], holder, (native, slot))
            self.assertEqual(R.simple(native, slot), holder)

    # WAS / PHX / MEM / ORL / CHA
    def test_was_boundary(self):
        self.check({'WAS': 8, 'PHX': 20, 'MEM': 15, 'ORL': 25},
                   {'WAS': 'WAS', 'PHX': 'MEM', 'MEM': 'MEM', 'ORL': 'CHA'})
        self.check({'WAS': 9, 'PHX': 20, 'MEM': 15, 'ORL': 25},
                   {'WAS': 'NYK', 'PHX': 'MEM', 'MEM': 'MEM', 'ORL': 'CHA'})

    def test_was_takes_phx_when_better(self):
        # WAS protected at 8, PHX at 3: WAS takes #3; WAS's #8 enters the MEM/CHA group
        self.check({'WAS': 8, 'PHX': 3, 'MEM': 20, 'ORL': 12},
                   {'PHX': 'WAS', 'WAS': 'MEM', 'ORL': 'MEM', 'MEM': 'CHA'})
        # WAS unprotected at 9: goes to NYK even though PHX is better; PHX enters the group
        self.check({'WAS': 9, 'PHX': 3, 'MEM': 20, 'ORL': 12},
                   {'WAS': 'NYK', 'PHX': 'MEM', 'ORL': 'MEM', 'MEM': 'CHA'})

    # OKC / HOU / LAC
    def test_hou_boundary(self):
        self.check({'HOU': 5, 'OKC': 30, 'LAC': 12}, {'HOU': 'OKC', 'LAC': 'PHI', 'OKC': 'DAL'})
        self.check({'HOU': 4, 'OKC': 30, 'LAC': 12}, {'HOU': 'HOU', 'LAC': 'PHI', 'OKC': 'DAL'})
        self.check({'HOU': 22, 'OKC': 30, 'LAC': 12}, {'LAC': 'OKC', 'HOU': 'PHI', 'OKC': 'DAL'})

    def test_mil_nop(self):
        self.check({'MIL': 3, 'NOP': 20}, {'MIL': 'ATL', 'NOP': 'MIL'})
        self.check({'MIL': 20, 'NOP': 3}, {'NOP': 'ATL', 'MIL': 'MIL'})

    # six-team chain
    def test_uta_boundary_main(self):
        base = {'ATL': 20, 'MIN': 21, 'CLE': 23, 'DET': 28, 'SAS': 29}
        self.check({**base, 'UTA': 8}, {'UTA': 'UTA', 'ATL': 'SAS', 'MIN': 'DET', 'CLE': 'ATL', 'DET': 'MIN',
                                        'SAS': 'CLE'})
        self.check({**base, 'UTA': 9}, {'UTA': 'OKC', 'ATL': 'SAS', 'MIN': 'DET', 'CLE': 'ATL', 'DET': 'MIN',
                                        'SAS': 'CLE'})

    def test_min_top19_protection(self):
        base = {'UTA': 2, 'ATL': 25, 'CLE': 26, 'DET': 28, 'SAS': 29}
        self.check({**base, 'MIN': 19}, {'MIN': 'MIN', 'DET': 'DET'})
        self.check({**base, 'MIN': 20}, {'MIN': 'DET', 'DET': 'MIN'})
        # DET better than MIN: no swap
        self.check({**base, 'MIN': 27, 'DET': 21}, {'MIN': 'MIN', 'DET': 'DET'})

    def test_sas_atl_cle(self):
        # CLE best of the three -> ATL gets CLE's, SAS the better of SAS/ATL, CLE the worst
        self.check({'UTA': 1, 'MIN': 30, 'DET': 29, 'CLE': 10, 'ATL': 15, 'SAS': 20},
                   {'CLE': 'ATL', 'ATL': 'SAS', 'SAS': 'CLE'})
        # SAS best: SAS keeps; ATL takes CLE's if better than its own
        self.check({'UTA': 1, 'MIN': 30, 'DET': 29, 'SAS': 10, 'CLE': 15, 'ATL': 20},
                   {'SAS': 'SAS', 'CLE': 'ATL', 'ATL': 'CLE'})

    def test_uta_takes_min_then_det_swap(self):
        # UTA 8, MIN 5: UTA takes #5, MIN holds #8; DET (#25) swaps for #8 (UTA's pick, not top-19 protected)
        self.check({'UTA': 8, 'MIN': 5, 'CLE': 22, 'DET': 25, 'ATL': 27, 'SAS': 28},
                   {'MIN': 'UTA', 'UTA': 'DET', 'DET': 'MIN', 'CLE': 'ATL', 'ATL': 'SAS', 'SAS': 'CLE'})

    def test_uta_takes_cle(self):
        # UTA 8, CLE 3, MIN 6: UTA swaps MIN (gets #6, MIN holds #8), then CLE (gets #3, CLE holds #6)
        # SAS takes ATL's #20, ATL holds SAS's #24 and takes CLE's held #6; CLE ends with #24
        self.check({'UTA': 8, 'CLE': 3, 'MIN': 6, 'DET': 28, 'ATL': 20, 'SAS': 24},
                   {'CLE': 'UTA', 'MIN': 'ATL', 'UTA': 'DET', 'DET': 'MIN', 'ATL': 'SAS', 'SAS': 'CLE'})

    def test_uta_unprotected_no_swaps(self):
        # UTA 9 (to OKC): MIN/CLE picks untouched by UTA even if better
        self.check({'UTA': 9, 'CLE': 3, 'MIN': 6, 'DET': 28, 'ATL': 20, 'SAS': 24},
                   {'UTA': 'OKC', 'CLE': 'ATL', 'MIN': 'MIN', 'DET': 'DET', 'ATL': 'SAS', 'SAS': 'CLE'})


if __name__ == '__main__':
    unittest.main()

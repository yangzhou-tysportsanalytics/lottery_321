"""Tests for the alternative 2024 router (assumption item 6, WAS 13-30 branch)."""
import sys, unittest
from pathlib import Path
import numpy as np
R = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(R / 'src/lottery321'))
sys.path.insert(0, str(R / 'src/lottery321/ledgers'))
from teams import TEAMS
import router_2024 as BASE
import router_2024_alt6 as ALT


def perm(rng):
    p = rng.permutation(30) + 1
    return {t: int(s) for t, s in zip(TEAMS, p)}


class Alt6(unittest.TestCase):
    def test_conserves_slots(self):
        rng = np.random.default_rng(0)
        for _ in range(5000):
            pos = perm(rng)
            out = ALT.route(pos)
            self.assertEqual(sorted(out), list(range(1, 31)))     # every slot has exactly one holder
            self.assertTrue(set(out.values()) <= set(TEAMS))       # a team may hold several picks or none

    def test_identical_when_was_is_top_12(self):
        rng = np.random.default_rng(1); n = 0
        for _ in range(4000):
            pos = perm(rng)
            if pos['WAS'] <= 12:
                n += 1
                self.assertEqual(ALT.route(pos), BASE.route(pos))
        self.assertGreater(n, 500)

    def test_differs_only_in_the_registered_branch(self):
        rng = np.random.default_rng(2); diff = 0
        for _ in range(4000):
            pos = perm(rng)
            a, b = ALT.route(pos), BASE.route(pos)
            if a != b:
                diff += 1
                self.assertGreaterEqual(pos['WAS'], 13)
                # the difference only ever concerns MEM, PHX, WAS and NYK
                changed = {a[s] for s in a if a[s] != b[s]} | {b[s] for s in a if a[s] != b[s]}
                self.assertTrue(changed <= {'MEM', 'PHX', 'WAS', 'NYK'})
        self.assertGreater(diff, 0)

    @staticmethod
    def place(**slots):
        """A full permutation with the named teams at the named slots."""
        rest = [t for t in TEAMS if t not in slots]
        free = [s for s in range(1, 31) if s not in slots.values()]
        pos = dict(slots); pos.update(dict(zip(rest, free)))
        assert sorted(pos.values()) == list(range(1, 31))
        return pos

    def test_memphis_takes_the_less_favourable_of_phx_and_was(self):
        # less favourable of PHX (25) and WAS (20) is PHX, and it beats MEM's own (28): MEM swaps with PHX
        out = ALT.route(self.place(WAS=20, PHX=25, MEM=28))
        self.assertEqual((out[20], out[25], out[28]), ('NYK', 'MEM', 'PHX'))
        # less favourable is WAS (28), worse than MEM's own (20): no swap, NYK keeps the WAS pick
        out = ALT.route(self.place(WAS=28, PHX=25, MEM=20))
        self.assertEqual((out[20], out[25], out[28]), ('MEM', 'PHX', 'NYK'))
        # less favourable is WAS (26) and it beats MEM's own (29): MEM takes it from NYK, NYK gets MEM's
        out = ALT.route(self.place(WAS=26, PHX=22, MEM=29))
        self.assertEqual((out[22], out[26], out[29]), ('PHX', 'MEM', 'NYK'))
        # the primary router cannot reach the WAS pick there: it swaps MEM against the PHX pick instead
        base = BASE.route(self.place(WAS=26, PHX=22, MEM=29))
        self.assertEqual((base[22], base[26], base[29]), ('MEM', 'NYK', 'PHX'))

    def test_decomposed_matches_route(self):
        rng = np.random.default_rng(3)
        for _ in range(2000):
            pos = perm(rng)
            out = ALT.route(pos)
            got = {pos[t]: ALT.Router2024Alt6.simple(t, pos[t]) for t in ALT.Router2024Alt6.simple_natives}
            got.update(ALT.Router2024Alt6.pooled(pos))
            self.assertEqual(got, out)


if __name__ == '__main__':
    unittest.main()

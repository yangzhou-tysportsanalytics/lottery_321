"""Tests for the C3 protection-ban routers (C3 registration, section 2)."""
import sys, unittest
from pathlib import Path
import numpy as np
R = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(R / 'src/lottery321'))
sys.path.insert(0, str(R / 'src/lottery321/ledgers'))
from teams import TEAMS
import protection_ban as B

YEARS = tuple(B.AFFECTED)


def perms(n, seed):
    rng = np.random.default_rng(seed)
    for _ in range(n):
        yield {t: int(s) for t, s in zip(TEAMS, rng.permutation(30) + 1)}


class BanRouters(unittest.TestCase):
    def test_registered_set_of_protections(self):
        self.assertEqual(B.affected_count(), 24)
        for year, d in B.AFFECTED.items():
            for nat, (p, kind) in d.items():
                self.assertIn(p, (12, 13, 14, 15))
                self.assertIn(kind, ('simple', 'pool'))

    def test_conserves_slots_and_decomposition_matches(self):
        for year in YEARS:
            for v in B.VARIANTS:
                r = B.make_router(year, v)
                for pos in perms(600, seed=year):
                    out = r.route(pos)
                    self.assertEqual(sorted(out), list(range(1, 31)))
                    got = {pos[t]: r.simple(t, pos[t]) for t in r.simple_natives}
                    got.update(r.pooled(pos))
                    self.assertEqual(got, out)

    def test_native_keeps_the_pick_exactly_on_the_new_range(self):
        for year in YEARS:
            for v, lim in B.VARIANTS.items():
                r = B.make_router(year, v)
                for nat, (p, kind) in B.AFFECTED[year].items():
                    if kind != 'simple':
                        continue
                    for slot in (1, lim, lim + 1, 30):
                        keeps = r.simple(nat, slot) == nat
                        self.assertEqual(keeps, slot <= lim, (year, v, nat, slot))

    def test_differs_from_the_primary_router_only_inside_the_changed_range(self):
        for year in YEARS:
            for v, lim in B.VARIANTS.items():
                r = B.make_router(year, v); base = B.base(year)
                diff = 0
                for pos in perms(1500, seed=100 + year):
                    a, b = r.route(pos), base.route(pos)
                    if a == b:
                        continue
                    diff += 1
                    # some affected native must sit in the range where the two readings disagree
                    lo, hi = sorted((lim, max(p for p, _ in B.AFFECTED[year].values())))
                    self.assertTrue(any(min(lo, p) + 1 <= pos[nat] <= max(hi, p)
                                        for nat, (p, _) in B.AFFECTED[year].items()), (year, v))
                self.assertGreater(diff, 0, (year, v))

    def test_variant_b_never_conveys_before_slot_17(self):
        r = B.make_router(2025, 'B')
        for nat, (p, kind) in B.AFFECTED[2025].items():
            if kind == 'simple':
                self.assertEqual(r.simple(nat, 16), nat)
                self.assertNotEqual(r.simple(nat, 17), nat)

    def test_pool_level_bans_change_the_pool_branch(self):
        # 2022: MIA protection; 2024: WAS protection; 2021: POR inside the HOU/BKN swap
        for year, nat in ((2022, 'MIA'), (2024, 'WAS'), (2021, 'POR')):
            for v, lim in B.VARIANTS.items():
                r = B.make_router(year, v); base = B.base(year)
                found = False
                for pos in perms(3000, seed=year * 7):
                    p = B.AFFECTED[year][nat][0]
                    if min(lim, p) < pos[nat] <= max(lim, p) and r.route(pos) != base.route(pos):
                        found = True
                        break
                self.assertTrue(found, (year, nat, v))


if __name__ == '__main__':
    unittest.main()

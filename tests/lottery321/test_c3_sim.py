"""C3 simulator: common random numbers with the primary run, and per-configuration sanity."""
import sys, unittest
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
R = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(R / 'src/lottery321'))
sys.path.insert(0, str(R / 'src/lottery321/ledgers'))
import c3_sim as C3
import protection_ban as BAN
import elo as E
import simulate as H
from league_sim import simulate
from cutoff_state import build_state
from value import CURVES


def state_2023_12_01():
    games = E.load_games(H.GAMES)
    day = '2023-12-01'
    todays = [g for g in games if g['season'] == '2023-24'
              and g['start'].astimezone(H.ET).date().isoformat() == day]
    cutoff = min(g['start'] for g in todays) - __import__('datetime').timedelta(hours=6)
    st = build_state(games, '2023-24', cutoff)
    ids = {g['game_id'] for g in todays}
    focal = [j for j, gid in enumerate(st['remaining_ids']) if gid in ids][:2]
    return st, focal


class CommonRandomNumbers(unittest.TestCase):
    """The old-rule and full 3-2-1 configurations must land on the primary run's own worlds."""

    @classmethod
    def setUpClass(cls):
        cls.state, cls.focal = state_2023_12_01()
        cls.routers = {'base': H.router_for(2024), 'A': BAN.make_router(2024, 'A'), 'B': BAN.make_router(2024, 'B')}
        cls.mp = H.restrictions(2024)
        cls.seed = 20231201
        cls.n, cls.b = 40, 10
        cls.prim = simulate(cls.state, cls.focal, n=cls.n, seed=cls.seed, router=cls.routers['base'],
                            batches=cls.b, min_pick_new=cls.mp)
        cls.c3 = C3.simulate_c3(cls.state, cls.focal, n=cls.n, seed=cls.seed, routers=cls.routers,
                                min_pick_new=cls.mp, batches=cls.b)

    def own(self, res_db):
        out = np.zeros((self.b, len(self.focal), 2, 2, 30))       # batch, game, rule, side, slot
        for gi, j in enumerate(self.focal):
            h, a, _ = self.state['remaining'][j]
            out[:, gi, :, 0] = res_db[:, gi, :, h]
            out[:, gi, :, 1] = -res_db[:, gi, :, a]
        return out

    def idx(self, name):
        return self.c3['configs'].index(name)

    def test_old_rule_configuration_matches_the_primary_run(self):
        prim = self.own(self.prim['DB'])[:, :, 0]
        got = self.c3['DOWN'][:, :, self.idx('F0L0R0_base')]
        np.testing.assert_allclose(got, prim, atol=1e-12)

    def test_full_321_configuration_matches_the_primary_run(self):
        prim = self.own(self.prim['DB'])[:, :, 1]
        got = self.c3['DOWN'][:, :, self.idx('F1L1R1_base')]
        np.testing.assert_allclose(got, prim, atol=1e-12)

    def test_stakes_match_the_primary_run_on_every_curve(self):
        for ci, curve in enumerate(self.c3['curves']):
            v = CURVES[curve]
            prim = -(self.prim['DB'] @ v)                        # (B, G, rule, team)
            for name, r in (('F0L0R0_base', 0), ('F1L1R1_base', 1)):
                got = self.c3['STK'][:, :, self.idx(name), ci]
                np.testing.assert_allclose(got, prim[:, :, r], atol=1e-12)


class Configurations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state, cls.focal = state_2023_12_01()
        cls.routers = {'base': H.router_for(2024), 'A': BAN.make_router(2024, 'A'), 'B': BAN.make_router(2024, 'B')}
        cls.res = C3.simulate_c3(cls.state, cls.focal, n=20, seed=7, routers=cls.routers,
                                 min_pick_new=H.restrictions(2024), batches=10)

    def test_all_sixteen_subsets_present(self):
        self.assertEqual(len(self.res['configs']), 24)
        self.assertEqual(len(set(self.res['subsets'])), 16)

    def test_floor_and_restrictions_change_the_result(self):
        i, j = self.res['configs'].index('F1L0R0_base'), self.res['configs'].index('F1L1R0_base')
        self.assertGreater(np.abs(self.res['DOWN'][:, :, i] - self.res['DOWN'][:, :, j]).max(), 0)
        k = self.res['configs'].index('F1L1R1_base')
        self.assertGreater(np.abs(self.res['DOWN'][:, :, j] - self.res['DOWN'][:, :, k]).max(), 0)

    def test_floor_does_not_bind_under_the_old_rule(self):
        i, j = self.res['configs'].index('F0L0R0_base'), self.res['configs'].index('F0L1R0_base')
        np.testing.assert_allclose(self.res['DOWN'][:, :, i], self.res['DOWN'][:, :, j], atol=1e-12)

    def test_ban_variants_differ_from_the_base_ledger(self):
        b = self.res['configs'].index('F1L1R1_base')
        for v in ('A', 'B'):
            i = self.res['configs'].index(f'F1L1R1_{v}')
            self.assertGreater(np.abs(self.res['STK'][:, :, i] - self.res['STK'][:, :, b]).max(), 0)

    def test_stakes_sum_to_zero_across_teams_without_pooled_rights(self):
        """With exact marginals (no pooled sampling) every slot has exactly one holder in every world, so
        Proposition 2(b) holds world by world. With pooled rights it holds only in expectation."""
        from league_sim import OwnRouter
        res = C3.simulate_c3(self.state, self.focal, n=10, seed=3,
                             routers={g: OwnRouter for g in ('base', 'A', 'B')},
                             min_pick_new=H.restrictions(2024), batches=5)
        self.assertLess(np.abs(res['STK'].sum(axis=-1)).max(), 1e-9)
        self.assertLess(np.abs(res['DOWN']).max(), 10.0)


if __name__ == '__main__':
    unittest.main()

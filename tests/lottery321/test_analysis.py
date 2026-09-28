"""Tests for the registered analysis (analysis). Uses only synthetic batch arrays and one
off-window state (2023-12-01, not part of the simulation sample); never reads simulation outputs."""
import json, math, sys, tempfile, unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src/lottery321'))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src/lottery321/ledgers'))
import analysis as A
from teams import TEAMS

B = 50


def cum_from(d):
    return np.cumsum(d, axis=1)


class Verdicts(unittest.TestCase):
    def setUp(self):
        self.rng = np.random.default_rng(0)

    def noisy(self, profile, sd=0.001):
        return np.asarray(profile, float)[None, :] + self.rng.normal(0, sd, (B, 30))

    def test_positive_dominance(self):
        d = np.zeros(30); d[:5] = 0.02; d[20:25] = -0.02          # C >= 0 everywhere, > 0 early
        m, se, c = A.band_stats(cum_from(self.noisy(d, 0.0003)))
        self.assertEqual(A.verdict(m, se, c['B'], 30)[0], 'dominance_positive')

    def test_a_dip_smaller_than_delta_is_not_a_reversal(self):
        """A1 amendment 9: reversal now needs the upper band below -delta, as dominance needs -delta."""
        d = np.zeros(30); d[0] = -0.0008                     # a quarter of delta, resolved precisely
        m, se, c = A.band_stats(cum_from(self.noisy(d, 0.00002)))
        self.assertNotEqual(A.verdict(m, se, c['B'], 30)[0], 'reversal')
        d2 = np.zeros(30); d2[0] = -0.02
        m, se, c = A.band_stats(cum_from(self.noisy(d2, 0.00002)))
        self.assertEqual(A.verdict(m, se, c['B'], 30)[0], 'reversal')

    def test_reversal_and_jstar(self):
        d = np.zeros(30); d[:9] = -0.01; d[11] = 0.12            # crossing: negative to j=9..11, positive at 12
        m, se, c = A.band_stats(cum_from(self.noisy(d)))
        v, j = A.verdict(m, se, c['B'], 30)
        self.assertEqual(v, 'reversal'); self.assertIn(j, (9, 10, 11))   # C is flat at its minimum on 9..11
        self.assertTrue(A.crossing(m, se, c['B']))

    def test_negligible(self):
        m, se, c = A.band_stats(cum_from(self.noisy(np.zeros(30), sd=0.00005)))
        self.assertEqual(A.verdict(m, se, c['B'], 30)[0], 'negligible')

    def test_unresolved(self):
        m, se, c = A.band_stats(cum_from(self.noisy(np.zeros(30), sd=0.01)))
        self.assertEqual(A.verdict(m, se, c['B'], 30)[0], 'unresolved')

    def test_class_c_ignores_mass_term(self):
        d = np.zeros(30); d[:3] = 0.03; d[29] = -0.15             # M = C(30) < 0 only
        m, se, c = A.band_stats(cum_from(self.noisy(d, 0.0005)))
        self.assertEqual(A.verdict(m, se, c['B'], 30)[0], 'reversal')
        self.assertEqual(A.verdict(m, se, c['C'], 29)[0], 'dominance_positive')

    def test_supt_critical_between_pointwise_and_bonferroni(self):
        m, se, c = A.band_stats(self.rng.normal(0, 1, (B, 30)))   # independent coordinates
        self.assertGreater(c['B'], 2.576); self.assertLess(c['B'], 5.0)
        self.assertGreater(c['B_boott'], c['B'])                  # bootstrap-t (diagnostic) is wider than the multiplier
        m, se, c2 = A.band_stats(np.repeat(self.rng.normal(0, 1, (B, 1)), 30, axis=1))  # perfectly correlated
        self.assertGreater(c2['B'], 2.576)                        # a t-type quantile at 49 df, not 2.576
        self.assertLess(c2['B'], 3.4)

    def test_bootstrap_t_covers_better_than_the_multiplier_band(self):
        """A1 amendment 9: on well-behaved Gaussian coordinates the multiplier band under-covers slightly and the
        bootstrap-t is closer; the multiplier band is nevertheless primary because the bootstrap-t degenerates
        on rare-event coordinates (RareEventDegeneracy)."""
        rng = np.random.default_rng(3); J, R = 30, 300
        L = np.linalg.cholesky(np.array([[0.9 ** abs(i - j) for j in range(J)] for i in range(J)])
                               + 1e-9 * np.eye(J))
        cb = cm = 0
        for _ in range(R):
            X = rng.standard_normal((B, J)) @ L.T
            m, se, c = A.band_stats(X)
            cb += bool(np.all(np.abs(m) <= c['B_boott'] * se))    # diagnostic bootstrap-t
            cm += bool(np.all(np.abs(m) <= c['B'] * se))          # primary multiplier band
        self.assertGreaterEqual(cb, cm)
        self.assertGreater(cb / R, 0.96); self.assertGreater(cm / R, 0.95)

    def test_zero_variance_coordinates_fixed(self):
        x = self.rng.normal(0, 1, (B, 30)); x[:, :10] = 0.0
        m, se, c = A.band_stats(x)
        self.assertTrue(np.all(se[:10] == 0)); self.assertTrue(math.isfinite(c['B']))

    def test_curve_sign_and_typology(self):
        self.assertEqual(A.curve_sign(0.05, 0.001), 'lose')
        self.assertEqual(A.curve_sign(-0.05, 0.001), 'win')
        self.assertEqual(A.curve_sign(0.0015, 0.0002), 'neutral')    # significant but inside +-delta
        self.assertEqual(A.typology('lose', 'lose'), 'both_lose')
        self.assertEqual(A.typology('neutral', 'lose'), 'normal')
        self.assertEqual(A.typology('win', 'lose'), 'opposed')
        self.assertEqual(A.typology('neutral', 'win'), 'one_sided_win')
        self.assertEqual(A.typology('neutral', 'neutral'), 'no_own_stake')


class Bootstrap(unittest.TestCase):
    DAYS = [('s1', f'd{i}') for i in range(20)] + [('s2', f'e{i}') for i in range(20)]

    def test_weights_keep_the_sample_size(self):
        for two in (True, False):
            b = A.Boot(self.DAYS, [s for s, _ in self.DAYS], two_level=two)
            self.assertTrue(np.all(b.W.sum(1) == 40))

    def test_two_level_carries_the_season_component(self):
        """A1 amendment 9: a difference that lives entirely between seasons must widen the interval."""
        num = np.r_[np.ones(20), np.zeros(20)]; den = np.ones(40)      # season s1 is all ones
        within = A.Boot(self.DAYS, [s for s, _ in self.DAYS], two_level=False)
        two = A.Boot(self.DAYS, [s for s, _ in self.DAYS], two_level=True)
        p1, lo1, hi1 = within.ratio(num[:, None], den[:, None])
        p2, lo2, hi2 = two.ratio(num[:, None], den[:, None])
        self.assertAlmostEqual(p1[0], 0.5); self.assertAlmostEqual(p2[0], 0.5)
        self.assertAlmostEqual(hi1[0] - lo1[0], 0.0)                   # the within-season bootstrap misses the season component
        self.assertGreater(hi2[0] - lo2[0], 0.5)

    def test_within_day_variation_is_still_captured(self):
        rng = np.random.default_rng(0)
        num = rng.binomial(1, 0.5, 40).astype(float); den = np.ones(40)
        b = A.Boot(self.DAYS, [s for s, _ in self.DAYS])
        pt, lo, hi = b.ratio(num[:, None], den[:, None])
        self.assertLess(lo[0], pt[0]); self.assertGreater(hi[0], pt[0])


def fake_day(season, day, pattern_home, pattern_away, stakes_third=0.0):
    """One focal game (home index 0 = ATL, away index 1 = BKN) with designed own differences."""
    rng = np.random.default_rng(1)
    DB = rng.normal(0, 1e-4, (B, 1, 2, 30, 30))
    for r in range(2):
        DB[:, 0, r, 0, :] += pattern_home[r]            # home: loss-minus-win = +DB
        DB[:, 0, r, 1, :] -= pattern_away[r]            # away: loss-minus-win = -DB
        DB[:, 0, r, 5, 0] += stakes_third                # a third party
    meta = {'season': season, 'day': day, 'cutoff_utc': '2024-03-15T16:00:00+00:00', 'seed': 20240315,
            'focal_teams': [[0, 1]], 'focal_game_ids': ['g1'], 'min_pick_new': {'DET': 6},
            'looks': [{'look': 1, 'worlds': 2000}], 'precision_met': True, 'n_worlds': 2000, 'remaining_games': 99}
    Q = np.zeros((1, 2, 2, 30, 30)); Q[..., np.arange(30), np.arange(30)] = 1.0
    ST = np.zeros((1, 2, 30, 9)); ST[..., 8] = 1.0
    return {'DB': DB, 'DB_own': DB.copy(), 'Q': Q, 'ST': ST, 'meta': meta}


class EndToEndSynthetic(unittest.TestCase):
    def test_rows_verdicts_and_tables(self):
        pos = np.zeros(30); pos[:4] = 0.02; pos[26:30] = -0.02
        neg = np.zeros(30); neg[:9] = -0.01; neg[11] = 0.12
        days = []
        for i in range(6):
            days.append(fake_day('2023-24', f'2024-03-{10 + i}', (pos, neg), (pos, pos), stakes_third=0.01))
        ranks = np.arange(1, 31)[::-1].copy(); ranks[0] = 3; ranks[1] = 20
        tg, games, profs, diags = [], [], [], []
        for d in days:
            a, b, c, dg = A.analyse_day(d, ranks)
            tg += a; games += b; profs += c; diags.append(dg)
        home_new = [x for x in tg if x['team'] == 'ATL' and x['rule'] == 'new' and x['portfolio'] == 'actual']
        home_old = [x for x in tg if x['team'] == 'ATL' and x['rule'] == 'old' and x['portfolio'] == 'actual']
        self.assertTrue(all(x['verdict_B'] == 'reversal' and x['jstar_B'] in (9, 10, 11) and x['crossing'] for x in home_new))
        self.assertTrue(all(x['verdict_B'] == 'dominance_positive' for x in home_old))
        self.assertTrue(all(x['band'] == '1-3' for x in home_new))
        dl = [x for x in tg if x['team'] == 'ATL' and x['rule'] == 'delta' and x['portfolio'] == 'actual']
        self.assertTrue(all(x['verdict_B'] == 'reversal' for x in dl))
        g = [x for x in games if x['rule'] == 'old'][0]
        self.assertTrue(0 < g['tp_share'] < 1)
        self.assertEqual(len(g['stakes']), 30)
        dk = sorted({(x['season'], x['day']) for x in diags})
        T = A.build_tables(tg, games, profs, diags, A.Boot(dk, [s for s, _ in dk]))
        t51 = [r for r in T['T5_1_verdicts'] if r['rule'] == 'new' and r['portfolio'] == 'actual' and r['value_class'] == 'B']
        share = {r['verdict']: r['share'] for r in t51}
        self.assertAlmostEqual(share['reversal'], 0.5); self.assertAlmostEqual(share['dominance_positive'], 0.5)
        self.assertAlmostEqual(sum(share.values()), 1.0)
        tr = {(r['portfolio'], r['old'], r['new']): r['count'] for r in T['T5_6_transitions']}
        self.assertEqual(tr[('actual', 'dominance_positive', 'reversal')], 6)
        with tempfile.TemporaryDirectory() as t:
            A.write_tables(T, Path(t))
            self.assertTrue((Path(t) / 'report.md').exists())
            self.assertTrue((Path(t) / 'T5_1_verdicts.csv').exists())


class EndToEndSimulated(unittest.TestCase):
    """Real simulator output on an off-window state (2023-12-01): file format, ranks and conservation."""

    def test_file_roundtrip(self):
        import elo as E, simulate as H
        from cutoff_state import build_state
        from league_sim import simulate
        games = E.load_games(H.GAMES)
        day = '2023-12-01'
        todays = [g for g in games if g['season'] == '2023-24' and g['start'].astimezone(H.ET).date().isoformat() == day]
        cutoff = min(g['start'] for g in todays) - timedelta(hours=6)
        st = build_state(games, '2023-24', cutoff)
        ids = {g['game_id'] for g in todays}
        focal = [j for j, gid in enumerate(st['remaining_ids']) if gid in ids][:2]
        seed = 20231201
        res = simulate(st, focal, n=100, seed=seed, router=H.router_for(2024), batches=50,
                       min_pick_new=H.restrictions(2024))
        meta = {'season': '2023-24', 'day': day, 'cutoff_utc': cutoff.isoformat(), 'seed': seed,
                'focal_teams': [[st['remaining'][j][0], st['remaining'][j][1]] for j in focal],
                'focal_game_ids': [st['remaining_ids'][j] for j in focal],
                'min_pick_new': {TEAMS[k]: v for k, v in H.restrictions(2024).items()},
                'looks': [], 'precision_met': False, 'n_worlds': 100, 'remaining_games': len(st['remaining'])}
        with tempfile.TemporaryDirectory() as t:
            p = Path(t) / 'x' / '2023-24'; p.mkdir(parents=True)
            H.save(p / f'exposures_{day}.npz', res, meta)
            tg, gm, pr, dg = A.collect('x', root=Path(t))
        self.assertEqual(len(tg), 2 * 2 * 2 * 3)        # games x sides x portfolios x (old, new, delta)
        self.assertEqual(len(gm), 2 * 2 * len(A.CURVES))   # A1 amendment 9 item 7: all four curves
        self.assertEqual({x['curve'] for x in gm}, set(A.CURVES))
        self.assertLess(dg[0]['q_total_dev'], 1e-9)
        self.assertLess(dg[0]['own_slot_dev'], 1e-5)    # float32 storage
        # the registered check is per slot and holds only in expectation under the hybrid estimator
        self.assertIn('per_slot_dev', dg[0])
        self.assertLess(dg[0]['per_slot_dev'], 20 * dg[0]['per_slot_expected'])
        # the delta half-width is in the diagnostic and is the binding one here
        self.assertGreaterEqual(dg[0]['max_hw_linear'], dg[0]['max_hw_linear_rules_only'])
        self.assertEqual(dg[0]['max_hw_linear'], max(dg[0]['max_hw_delta_linear'], dg[0]['max_hw_linear_rules_only']))
        self.assertTrue(all(x['n_worlds_match'] == 100 for x in tg))
        ranks = sorted({x['rank'] for x in tg})
        self.assertTrue(all(1 <= r <= 30 for r in ranks))


class RolloverValuation(unittest.TestCase):
    """A1 amendment 10: tau_rho = tau - rho * vbar * M, reported beside the registered tau."""

    def setUp(self):
        self.rng = np.random.default_rng(5)

    def test_matches_the_registered_formula(self):
        db = self.rng.normal(0, 0.01, (B, 30))
        M = db.sum(axis=1).mean()
        base = A.tau_stats(db)
        for rho in A.RHOS:
            adj = A.tau_rho(db, rho)
            for cv in A.CURVES:
                self.assertAlmostEqual(adj[cv][0], base[cv][0] - rho * A.VBAR[cv] * M, places=12)

    def test_rho_zero_is_the_registered_tau(self):
        db = self.rng.normal(0, 0.01, (B, 30))
        base, adj = A.tau_stats(db), A.tau_rho(db, 0.0)
        for cv in A.CURVES:
            self.assertAlmostEqual(adj[cv][0], base[cv][0], places=12)

    def test_no_mass_change_means_no_adjustment(self):
        """When the loss and win branches hold the same total mass the channel is empty for every rho."""
        db = self.rng.normal(0, 0.01, (B, 30))
        db -= db.sum(axis=1, keepdims=True) / 30.0          # force M = 0 in every batch
        self.assertAlmostEqual(float(db.sum(axis=1).max()), 0.0, places=12)
        base = A.tau_stats(db)
        for rho in A.RHOS:
            for cv, (m, _) in A.tau_rho(db, rho).items():
                self.assertAlmostEqual(m, base[cv][0], places=12)

    def test_vbar_is_the_average_pick_value(self):
        self.assertAlmostEqual(A.VBAR['linear'], 0.5, places=9)
        for cv, v in A.CURVES.items():
            self.assertAlmostEqual(A.VBAR[cv], float(np.mean(v)), places=12)
            self.assertEqual(v[29], 0.0)     # all four curves zero the last slot, so rho=0 drops M entirely

    def test_rows_and_table_carry_the_sensitivity(self):
        pos = np.zeros(30); pos[:4] = 0.02
        ranks = np.arange(1, 31)
        tg, games, profs, diags = [], [], [], []
        for i in range(4):
            a_, b_, c_, dg = A.analyse_day(fake_day('2023-24', f'2024-03-1{i}', (pos, pos), (pos, pos)), ranks)
            tg += a_; games += b_; profs += c_; diags.append(dg)
        A.add_precision_matched(tg)
        x = tg[0]
        self.assertIn('M', x)
        for rho in A.RHOS:
            tag = f'rho{int(rho * 100)}'
            for cv in A.CURVES:
                self.assertAlmostEqual(x[f'tau_{cv}_{tag}'], x[f'tau_{cv}'] - rho * A.VBAR[cv] * x['M'], places=9)
        dk = sorted({(d['season'], d['day']) for d in diags})
        T = A.build_tables(tg, games, profs, diags, A.Boot(dk, [s for s, _ in dk]))
        self.assertTrue(T['T5_7_rollover'])
        self.assertEqual({r['rho'] for r in T['T5_7_rollover']}, {0.0} | set(A.RHOS))
        self.assertTrue(any(r['measure'] == 'M' for r in T['T5_7_rollover']))


class PrecisionMatched(unittest.TestCase):
    """A1 amendment 9 item 6 and item 9: verdicts restated at a common band width."""

    def rows(self, worlds, sd):
        rng = np.random.default_rng(4)
        d = np.zeros(30); d[0] = -0.004                      # a reversal just past the delta margin
        m, se, c = A.band_stats(cum_from(np.asarray(d)[None, :] + rng.normal(0, sd, (B, 30))))
        return {'n_worlds': worlds, '_m': m, '_se': se, 'crit_B': c['B'], 'crit_C': c['C'],
                'verdict_B': A.verdict(m, se, c['B'], 30)[0]}

    def test_precise_day_is_restated_at_the_widest_band(self):
        precise = self.rows(32000, 0.0012)                   # resolved: a reversal
        vague = self.rows(2000, 0.0012 * 4)                  # same profile, 16x the worlds -> 4x the se
        self.assertEqual(precise['verdict_B'], 'reversal')
        n = A.add_precision_matched([precise, vague])
        self.assertEqual(n, 2000)
        self.assertEqual(vague['verdict_B_pm'], vague['verdict_B'])          # the widest day is unchanged
        self.assertEqual(precise['n_worlds_match'], 2000)
        self.assertGreater(precise['band_ratio_pm'], 3.9 * precise['crit_B'] * float(np.max(precise['_se'])) / A.DELTA)
        self.assertEqual(precise['verdict_B_pm'], 'unresolved')              # resolved only by its extra worlds

    def test_matching_is_a_no_op_when_every_day_ran_the_same_worlds(self):
        a, b = self.rows(8000, 0.0012), self.rows(8000, 0.0012)
        A.add_precision_matched([a, b])
        for r in (a, b):
            self.assertEqual(r['verdict_B_pm'], r['verdict_B'])

    def test_verdict_by_look_table_is_produced(self):
        pos = np.zeros(30); pos[:4] = 0.02
        neg = np.zeros(30); neg[:9] = -0.01; neg[11] = 0.12
        ranks = np.arange(1, 31)
        tg, games, profs, diags = [], [], [], []
        for i in range(4):
            d = fake_day('2023-24', f'2024-03-1{i}', (pos, neg), (pos, pos))
            if i % 2:
                d['meta'] = dict(d['meta'], n_worlds=8000)
            a_, b_, c_, dg = A.analyse_day(d, ranks)
            tg += a_; games += b_; profs += c_; diags.append(dg)
        A.add_precision_matched(tg)
        dk = sorted({(x['season'], x['day']) for x in diags})
        T = A.build_tables(tg, games, profs, diags, A.Boot(dk, [s for s, _ in dk]))
        self.assertTrue(T['T5_0c_verdict_by_look'])
        self.assertEqual({r['stopped_at'] for r in T['T5_0c_verdict_by_look']}, {'2000', '8000'})
        self.assertTrue(any(r['value_class'] == 'B_pm' for r in T['T5_1_verdicts']))
        self.assertTrue(T['T5_0d_band_width'])
        # the stake tables carry a curve column with all four curves
        self.assertEqual({r['curve'] for r in T['T5_5_stakes_distribution']}, set(A.CURVES))
        self.assertEqual({r['curve'] for r in T['H2']}, set(A.CURVES))
        # both j* definitions are counted
        self.assertTrue(any(r['count_argmin_C_hat'] for r in T['T5_3_reversal_slot']))


class LedgerClaims(unittest.TestCase):
    def test_claims_reproduce_known_rights(self):
        cl, pooled = A.claims(2026)
        self.assertEqual(cl['PHI'].get('OKC'), 'some')      # PHI top-4 protected to OKC
        self.assertIn('UTA', pooled)
        f = A.features(2026, TEAMS.index('OKC'), TEAMS.index('PHI'), set())
        self.assertTrue(f['holds_opponent_pick']); self.assertTrue(f['holds_conditional_other'])

    def test_state_conditional_claims_drop_unreachable_slots(self):
        """A1 amendment 9 item 9: a protection that can only bite at slots the native cannot reach
        is no longer scored as conditionally held."""
        cl, _ = A.claims(2026)
        self.assertEqual(cl['PHI'].get('OKC'), 'some')       # top-4 protected: conveyed at 5..30 only
        reach = np.ones((30, 30), bool)
        reach[TEAMS.index('PHI'), :4] = False                # PHI can no longer reach slots 1..4
        cl2, _ = A.claims(2026, reach, reach_key='test_no_top4')
        self.assertEqual(cl2['PHI'].get('OKC'), 'all')       # the condition never binds -> unconditional
        reach2 = np.zeros((30, 30), bool)
        reach2[TEAMS.index('PHI'), :4] = True                # PHI only inside the protected range
        cl3, _ = A.claims(2026, reach2, reach_key='test_only_top4')
        self.assertIsNone(cl3['PHI'].get('OKC'))             # OKC never receives it

    def test_state_conditional_pass_fills_the_split(self):
        ranks = np.arange(1, 31)
        pos = np.zeros(30); pos[:4] = 0.02
        tg, games = A.analyse_day(fake_day('2023-24', '2024-03-10', (pos, pos), (pos, pos)), ranks)[:2]
        reach = {('2023-24', r): np.ones((30, 30), bool) for r in ('old', 'new')}
        self.assertTrue(A.state_conditional(tg, games, reach))
        for x in tg:                                          # full reach reproduces the registered feature
            self.assertEqual(x['holds_conditional_other_state'], x['holds_conditional_other'])
            self.assertEqual(x['holds_opponent_pick_state'], x['holds_opponent_pick'])
        for g in games:
            self.assertEqual(g['h2_sample_state'], g['h2_sample'])
        self.assertFalse(A.state_conditional(tg, games, {}))
        self.assertIsNone(tg[0]['holds_conditional_other_state'])


class CompareRuns(unittest.TestCase):
    """Generic run comparison: matched team-games only, and the paired differences it reports."""

    def rows(self, shift, days=4):
        pos = np.zeros(30); pos[:4] = 0.02
        neg = np.zeros(30); neg[:9] = -0.01; neg[11] = 0.12
        ranks = np.arange(1, 31)
        out = []
        for i in range(days):
            d = fake_day('2023-24', f'2024-03-0{i + 1}', (pos, neg if shift else pos), (pos, pos))
            if shift:
                d['DB'] += 0.0
            out += A.analyse_day(d, ranks)[0]
        return out

    def test_matches_only_common_team_games(self):
        a = self.rows(False, days=4)
        b = self.rows(True, days=3)                      # one day fewer
        rows, trans = A.compare_tags(a, b, 'primary', 'other')
        self.assertTrue(rows)
        for r in rows:
            self.assertEqual(r['n_days'], 3)
            self.assertEqual(r['n_team_games'], 3 * 2)   # 3 days x 2 sides of the single game

    def test_identical_runs_report_zero_difference(self):
        a = self.rows(False)
        rows, trans = A.compare_tags(a, list(a), 'x', 'y')
        self.assertEqual(trans, [])
        for r in rows:
            self.assertEqual(r['verdict_changed'], 0)
            self.assertAlmostEqual(r['mean_diff_linear'], 0.0)
            self.assertAlmostEqual(r['reversal_share_diff'], 0.0)

    def test_different_runs_report_the_change(self):
        a = self.rows(True); b = self.rows(False)
        rows, trans = A.compare_tags(a, b, 'new_reading', 'primary')
        new_rows = [r for r in rows if r['rule'] == 'new' and r['portfolio'] == 'actual']
        self.assertTrue(new_rows)
        r = new_rows[0]
        self.assertGreater(abs(r['mean_diff_linear']), A.DELTA)
        self.assertEqual(r['reversal_share_a'], 0.5)   # the home side of each game is the reversal
        self.assertEqual(r['reversal_share_b'], 0.0)
        self.assertTrue(any(t['verdict_a'] == 'reversal' for t in trans))


class HeadlineReversal(unittest.TestCase):
    """A1 amendment 11: the headline reversal-share differences."""
    def test_shares_and_difference(self):
        days = [('2020-21', f'd{i}') for i in range(6)] + [('2021-22', f'd{i}') for i in range(6)]
        tg = []
        for s, d in days:
            for k in range(10):
                for r in A.RULES:
                    for pf in A.PORTFOLIOS:
                        rev = (r == 'new' and k < 3) or (r == 'old' and pf == 'actual' and k < 1)
                        v = 'reversal' if rev else 'negligible'
                        tg.append(dict(season=s, day=d, rule=r, portfolio=pf, verdict_B=v, verdict_B_pm=v))
        boot = A.Boot(days, [s for s, _ in days])
        rows = {(x['contrast'], x['portfolio'], x['verdict']): x for x in A.headline_reversal(tg, boot)}
        a = rows[('new_minus_old', 'actual', 'verdict_B')]
        self.assertAlmostEqual(a['share_a'], 0.3); self.assertAlmostEqual(a['share_b'], 0.1)
        self.assertAlmostEqual(a['diff'], 0.2); self.assertLessEqual(a['lo99'], 0.2 + 1e-12); self.assertGreaterEqual(a['hi99'], 0.2 - 1e-12)
        o = rows[('new_minus_old', 'own', 'verdict_B')]
        self.assertAlmostEqual(o['diff'], 0.3)
        g = rows[('actual_minus_own', 'old', 'verdict_B')]
        self.assertAlmostEqual(g['diff'], 0.1)
        self.assertAlmostEqual(rows[('actual_minus_own', 'new', 'verdict_B')]['diff'], 0.0)


if __name__ == '__main__':
    unittest.main()


class RareEventDegeneracy(unittest.TestCase):
    """A coordinate that is float noise in 48 batches and a rare event in 2 made the bootstrap-t
    critical value explode; the primary (multiplier) band must stay finite and ordinary."""
    def test_multiplier_band_is_not_degenerate(self):
        rng = np.random.default_rng(3)
        Cb = np.cumsum(rng.normal(0, 1e-3, (B, 30)), 1)
        Cb[:, 17] = 1e-9 * rng.standard_normal(B); Cb[[4, 31], 17] = 1.56e-3
        Cb[:, 19:] = 1e-9 * rng.standard_normal((B, 11))
        m, se, c = A.band_stats(Cb)
        self.assertGreater(c['B_boott'], 1e3)          # bootstrap-t degenerates here (reported as a diagnostic)
        self.assertLess(c['B'], 5.0)
        self.assertLess(c['C'], 5.0)

"""Exploratory analyses, third set. Not registered; computed from the
stored primary, `norestr` and C3 team-game tables, the stored primary exposures (game-level stakes only) and
the game table, without new simulation (addendum A1, amendment 16). Nothing here changes a registered table
or headline quantity.

  R7   season-level inference for H1 and H2 (t with 5 d.f., 95% and 99%; sign test), beside H-a and H-b
  R8   the four headline quantities (H-a, H-b, H1 with crossing share, H2) for every robustness item that the
       body reports: precision-matched verdicts, no repeat restrictions, days meeting the target in the run,
       days meeting it at the three-look constant, flagged days, 2025-26 excluded, and the primary run on the
       days of the robustness runs (81 and 25 days)
  R9   the H1 band by season: magnitudes and the record gap between the third- and fourth-worst teams at the cutoff
  R10  set identities: old-rule reversals with j* in 16-30 against reversals kept under 3-2-1; old-rule
       reversal slots at the 14|15 boundary; the one own-pick reversal at league ranks 11-16
  R11  the protection ban's treatment group: rewritten protections, team-games whose tau changes, verdict changes
       by rule, and the per-day reversal counts among conditional holders under both readings
  R12  a horizon-matched version of the win-model favourite gap (ratings frozen at the first window day)
  R13  per-game third-party stakes on the linear curve (the input to R7 and R8), kept for reuse
  R14  99% two-level bootstrap bands on the mean C(j) profiles by band (Figure 5.1)
  R15  class-B verdicts changed by the as-run band and by precision matching (actual portfolio, by rule)
Usage: python exploratory_3.py
"""
import csv
import json
import math
import sys
from datetime import datetime
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / 'ledgers'))
import analysis as S  # noqa: E402
import exploratory_1 as P  # noqa: E402
import robustness_headlines as R  # noqa: E402
import elo as E  # noqa: E402
import simulate as H  # noqa: E402
from cutoff_state import build_state  # noqa: E402
from value import CURVES  # noqa: E402
from teams import TEAMS  # noqa: E402

OUT = S.OUT / 'exploratory_3'
P3 = S.OUT / 'exploratory_2'
Z2, Z3, DELTA, Z = 2.807034, 2.935199, 0.003, S.Z
SEASONS = ('2020-21', '2021-22', '2022-23', '2023-24', '2024-25', '2025-26')


def write(name, rows):
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / f'{name}.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)


def read(p):
    with open(p, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


# ---------------------------------------------------------------- R13: game-level stakes (linear curve)
def game_stakes(tag='primary'):
    """mean |third-party stake| on the linear curve and the H2 sample flag, per focal game and rule, from the
    stored exposures. The same arithmetic as analysis.analyse_day, restricted to what H2 needs."""
    rows = []
    v = CURVES['linear']
    for f in sorted((S.SIMULATIONS / tag).glob('*/exposures_*.npz')):
        d = S.load_day(f); meta = d['meta']; season, day = meta['season'], meta['day']
        year = int(season[:4]) + 1
        cl, _ = S.claims(year)
        for g, (h, a) in enumerate(meta['focal_teams']):
            third = [x for x in range(30) if x not in (h, a)]
            for ri, r in enumerate(S.RULES):
                s = (-(d['DB'][:, g, ri] @ v)).mean(0)
                mat = np.abs(s) >= DELTA
                third_m = [x for x in third if mat[x]]
                rows.append(dict(season=season, day=day, game_id=meta['focal_game_ids'][g], rule=r,
                                 mean_abs_third=float(np.abs(s[third_m]).sum() / len(third)),
                                 h2_sample=bool(S.third_party_claim(year, h, a, cl)),
                                 precision_met=bool(meta['precision_met']), n_worlds=int(meta['n_worlds'])))
    return rows


def h2_on(games, days, label):
    """H2 (registered sample, linear curve) on a set of days with the two-level bootstrap."""
    days = sorted(days)
    boot = S.Boot(days, [s for s, _ in days])
    by = {(x['season'], x['day'], x['game_id'], x['rule']): x for x in games if (x['season'], x['day']) in boot.idx}
    num = np.zeros(len(days)); den = np.zeros(len(days))
    for (s, dd, g, r), x in by.items():
        if r == 'old' and x['h2_sample']:
            i = boot.idx[(s, dd)]
            num[i] += by[(s, dd, g, 'new')]['mean_abs_third'] - x['mean_abs_third']; den[i] += 1
    pt, lo, hi = boot.ratio(num[:, None], den[:, None])
    return dict(analysis=label, h2_n=int(den.sum()), h2_diff=float(pt[0]), h2_lo=float(lo[0]), h2_hi=float(hi[0]),
                h2_supported=bool(pt[0] > 0 and lo[0] > 0))


# ---------------------------------------------------------------- R7: season-level inference
def t5(diffs):
    from scipy import stats
    d = np.asarray(diffs, float); m = d.mean(); se = d.std(ddof=1) / math.sqrt(len(d))
    out = dict(seasons=len(d), mean_diff=float(m), positive=int((d > 0).sum()),
               sign_test_one_sided_p=0.5 ** len(d) if (d > 0).all() else float('nan'))
    for lev in (0.95, 0.99):
        q = stats.t.ppf(1 - (1 - lev) / 2, len(d) - 1)
        out[f't5_{int(lev * 100)}_lo'] = float(m - q * se); out[f't5_{int(lev * 100)}_hi'] = float(m + q * se)
    return out


def season_inference(tg, games):
    rows = []
    for r in read(P3 / 'R5_season_inference.csv'):
        rows.append(dict(quantity={'actual': 'H-a', 'own': 'H-b'}[r['portfolio']], **{k: r[k] for k in r if k != 'portfolio'}))
    h1 = []
    for s in SEASONS:
        b = tg[(tg.season == s) & (tg.portfolio == 'own') & tg['rank'].between(2, 5)]
        h1.append((b[b.rule == 'new'].sign_linear == 'win').mean() - (b[b.rule == 'old'].sign_linear == 'win').mean())
    rows.append(dict(quantity='H1', **t5(h1)))
    h2 = []
    for s in SEASONS:
        by = {(x['day'], x['game_id'], x['rule']): x for x in games if x['season'] == s}
        d = [by[(dd, g, 'new')]['mean_abs_third'] - x['mean_abs_third'] for (dd, g, r), x in by.items()
             if r == 'old' and x['h2_sample']]
        h2.append(float(np.mean(d)))
    rows.append(dict(quantity='H2', **t5(h2)))
    return rows


def h2_by_season(games):
    """The six season values behind the H2 row of R7 (printed in Online Appendix H.12)."""
    rows = []
    for s in SEASONS:
        by = {(x['day'], x['game_id'], x['rule']): x for x in games if x['season'] == s}
        d = [by[(dd, g, 'new')]['mean_abs_third'] - x['mean_abs_third'] for (dd, g, r), x in by.items()
             if r == 'old' and x['h2_sample']]
        rows.append(dict(season=s, games=len(d), mean_diff=float(np.mean(d))))
    return rows


# ---------------------------------------------------------------- R8: the four quantities per robustness item
def h1_pm(tg):
    """H1 with every day's standard errors scaled to the least precise day (precision matching applied to
    the pointwise sign rule and to the crossing flag)."""
    n_match = int(tg.n_worlds.min())
    sub = tg[(tg.portfolio == 'own') & tg['rank'].between(2, 5)].copy()
    sc = np.sqrt(sub.n_worlds / n_match)
    lo = sub.tau_linear - Z * sub.se_linear * sc; hi = sub.tau_linear + Z * sub.se_linear * sc
    # the registered sign rule (analysis.curve_sign): neutral when the interval lies inside +-delta,
    # 'win' (significantly negative) when the upper bound is below zero
    sub['neg_pm'] = (hi < 0) & ~((lo > -DELTA) & (hi < DELTA))
    boot = P.boot_for(tg)
    rows = sub.to_dict('records')
    n1, d1 = S.per_day(rows, boot, lambda x: x['neg_pm'], lambda x: x['rule'] == 'new')
    n2, d2 = S.per_day(rows, boot, lambda x: x['neg_pm'], lambda x: x['rule'] == 'old')
    pt, lo, hi_ = boot.diff_of_ratios(n1, d1, n2, d2)
    rev = [x for x in rows if x['rule'] == 'new' and x['verdict_B_pm'] == 'reversal']
    cross = sum(bool(x['crossing_pm']) for x in rev) / max(len(rev), 1)
    return dict(h1_n=int(d1.sum()), h1_diff=pt, h1_lo99=lo, h1_hi99=hi_, h1_reversals=len(rev),
                h1_crossing_share=cross, h1_supported=bool(lo > 0 and cross > 0.5), n_match=n_match)


def four_quantities(tg, games, pr):
    rows = []
    # precision-matched
    hd = read(S.OUT / 'primary' / 'T5_headline_reversal_diff.csv')
    pm = {r['portfolio']: r for r in hd if r['contrast'] == 'new_minus_old' and r['verdict'] == 'verdict_B_pm'}
    row = dict(analysis='precision-matched verdicts (all 312 days)', n_days=312, n_team_games=4896,
               ha=float(pm['actual']['diff']), ha_lo=float(pm['actual']['lo99']), ha_hi=float(pm['actual']['hi99']),
               hb=float(pm['own']['diff']), hb_lo=float(pm['own']['lo99']), hb_hi=float(pm['own']['hi99']))
    row.update(h1_pm(tg))
    h2r = next(r for r in read(S.OUT / 'primary' / 'H2.csv') if r['curve'] == 'linear' and r['sample'] == 'registered')
    row.update(h2_n=int(h2r['n_games']), h2_diff=float(h2r['mean_diff_new_minus_old']), h2_lo=float(h2r['lo99']),
               h2_hi=float(h2r['hi99']), h2_supported=h2r['supported'] == 'True', h2_note='unchanged: H2 uses no band')
    rows.append(row)
    # no repeat restrictions
    nr = P.load_tg('norestr'); nr = nr[nr.rule.isin(['old', 'new'])]
    hdn = {r['portfolio']: r for r in P.headline(nr, label='norestr')}
    row = dict(analysis='no repeat restrictions (all 312 days)', n_days=312, n_team_games=int(hdn['actual']['n_team_games']),
               ha=hdn['actual']['diff'], ha_lo=hdn['actual']['lo99'], ha_hi=hdn['actual']['hi99'],
               hb=hdn['own']['diff'], hb_lo=hdn['own']['lo99'], hb_hi=hdn['own']['hi99'])
    row.update(R.h1(nr))
    h2n = next(r for r in read(S.OUT / 'norestr' / 'H2.csv') if r['curve'] == 'linear' and r['sample'] == 'registered')
    row.update(h2_n=int(h2n['n_games']), h2_diff=float(h2n['mean_diff_new_minus_old']), h2_lo=float(h2n['lo99']),
               h2_hi=float(h2n['hi99']), h2_supported=h2n['supported'] == 'True', h2_note='')
    rows.append(row)
    # day subsets: from R3 (H-a, H-b, H1) plus H2 computed here
    r3 = {r['analysis']: r for r in read(P3 / 'R3_headlines.csv')}
    sets = {'days meeting the target in the run (z = 2.807034)': {(r['season'], r['day']) for r in pr if r['run_met'] == 'True'},
            'days flagged in the run': {(r['season'], r['day']) for r in pr if r['run_met'] == 'False'},
            'days meeting the target at z = 2.935199 (stored batches)': {(r['season'], r['day']) for r in pr if r['stored_met_z3'] == 'True'},
            '2025-26 excluded': {(r['season'], r['day']) for r in pr if r['season'] != '2025-26'}}
    for label, days in sets.items():
        x = r3[label]
        row = dict(analysis=label, n_days=int(x['n_days']), n_team_games=int(x['n_team_games']))
        for k in ('ha', 'ha_lo', 'ha_hi', 'hb', 'hb_lo', 'hb_hi', 'h1_diff', 'h1_lo99', 'h1_hi99', 'h1_crossing_share'):
            row[k] = float(x[k])
        row.update(h1_n=int(x['h1_n']), h1_reversals=int(x['h1_reversals']), h1_supported=x['h1_supported'] == 'True', n_match='')
        h2 = h2_on(games, days, label); h2.pop('analysis')
        row.update(h2); row['h2_note'] = ''
        rows.append(row)
    # the primary run on the days of the robustness runs (H-a, H-b, H1 from robustness_headlines.csv; H2 here)
    rh = read(S.OUT / 'robustness_headlines.csv')
    for run, label in (('dta', 'primary run on the 81 robustness days'), ('alt6', 'primary run on the 25 alt6 days')):
        x = next(r for r in rh if r['run'] == run and r['version'] == 'primary, same days')
        days = set()
        for f in sorted((S.SIMULATIONS / run).glob('*/exposures_*.npz')):
            days.add((f.parent.name, f.name[len('exposures_'):-len('.npz')]))
        assert len(days) == int(x['n_days']), (run, len(days), x['n_days'])
        row = dict(analysis=label, n_days=int(x['n_days']), n_team_games=int(x['n_team_games']))
        for k in ('ha', 'ha_lo', 'ha_hi', 'hb', 'hb_lo', 'hb_hi', 'h1_diff', 'h1_lo99', 'h1_hi99', 'h1_crossing_share'):
            row[k] = float(x[k])
        row.update(h1_n=int(x['h1_n']), h1_reversals=int(x['h1_reversals']), h1_supported=x['h1_supported'] == 'True', n_match='')
        h2 = h2_on(games, days, label); h2.pop('analysis')
        row.update(h2); row['h2_note'] = ''
        rows.append(row)
    return rows


# ---------------------------------------------------------------- R15: verdicts changed by the band and by precision matching
def verdict_changes(tg):
    """Class-B verdicts (actual portfolio) that differ from the primary table under the as-run bootstrap-t band and
    under precision matching, by rule; the counterpart of the 'verdicts changed' column of the robustness runs."""
    key = ['season', 'day', 'game_id', 'team', 'rule']
    act = tg[tg.portfolio == 'actual'].set_index(key)
    asrun = P.load_tg('primary_asrun_boott'); asrun = asrun[(asrun.portfolio == 'actual') & asrun.rule.isin(['old', 'new'])].set_index(key)
    asrun = asrun.reindex(act.index)
    rows = []
    for r in ('new', 'old'):
        a = act[act.index.get_level_values('rule') == r]; b = asrun[asrun.index.get_level_values('rule') == r]
        rows.append(dict(comparison='as-run bootstrap-t band', rule=r, n=len(a),
                         verdicts_changed=int((a.verdict_B.values != b.verdict_B.values).sum()),
                         reversals_primary=int((a.verdict_B == 'reversal').sum()), reversals_other=int((b.verdict_B == 'reversal').sum())))
        rows.append(dict(comparison='precision-matched verdicts', rule=r, n=len(a),
                         verdicts_changed=int((a.verdict_B != a.verdict_B_pm).sum()),
                         reversals_primary=int((a.verdict_B == 'reversal').sum()), reversals_other=int((a.verdict_B_pm == 'reversal').sum())))
    return rows


# ---------------------------------------------------------------- R9: the H1 band by season
def h1_band_by_season(tg):
    games = E.load_games(H.GAMES)
    rows = []
    for s in SEASONS:
        b = tg[(tg.season == s) & (tg.portfolio == 'own') & (tg.rule == 'new') & tg['rank'].between(2, 5)]
        up = b.tau_linear + Z * b.se_linear
        gaps, gb = [], []
        for f in sorted((S.SIMULATIONS / 'primary' / s).glob('exposures_*.npz')):
            meta = json.loads(bytes(np.load(f)['meta']).decode())
            st = build_state(games, s, datetime.fromisoformat(meta['cutoff_utc']))
            w = st['wins'].astype(float); l = st['h2h_wins'].sum(0).astype(float)
            pct = np.where(w + l > 0, w / np.maximum(w + l, 1), 0.5)
            order = np.argsort(pct)                 # worst first
            t3, t4 = order[2], order[3]
            gaps.append(float(pct[t4] - pct[t3])); gb.append(float(((w[t4] - w[t3]) + (l[t3] - l[t4])) / 2))
        rows.append(dict(season=s, n=len(b), mean_tau=float(b.tau_linear.mean()), median_tau=float(b.tau_linear.median()),
                         share_sig_negative=float((b.sign_linear == 'win').mean()),
                         share_upper_below_minus_delta=float((up < -DELTA).mean()),
                         mean_pct_gap_3_4=float(np.mean(gaps)), mean_games_back_3_4=float(np.mean(gb)), days=len(gaps)))
    return rows


# ---------------------------------------------------------------- R10: set identities
def sets(tg):
    key = ['season', 'day', 'game_id', 'team']
    act = tg[tg.portfolio == 'actual']
    old = act[(act.rule == 'old') & (act.verdict_B == 'reversal')]
    new = act[(act.rule == 'new') & (act.verdict_B == 'reversal')]
    deep = set(map(tuple, old[old.jstar_B >= 16][key].values))
    shallow = set(map(tuple, old[old.jstar_B <= 15][key].values))
    kept = set(map(tuple, old[key].values)) & set(map(tuple, new[key].values))
    removed = set(map(tuple, old[key].values)) - kept
    own506 = tg[(tg.rule == 'new') & (tg.portfolio == 'own') & (tg.verdict_B == 'reversal') & (tg.band == '11-16')].iloc[0]
    nr = P.load_tg('norestr')
    same = nr[(nr.season == own506.season) & (nr.day == own506.day) & (nr.team == own506.team) & (nr.rule == 'new') & (nr.portfolio == 'own')].iloc[0]
    return [
        dict(item='old-rule actual reversals', value=len(old)),
        dict(item='  with j* in 16-30', value=len(deep)),
        dict(item='  with j* = 15', value=int((old.jstar_B == 15).sum())),
        dict(item='  with j* in 1-14', value=int((old.jstar_B <= 14).sum())),
        dict(item='  with j* in 15-30', value=int((old.jstar_B >= 15).sum())),
        dict(item='  ... holding a pick under a conditional clause', value=int(old[old.jstar_B >= 15].holds_conditional_other.sum())),
        dict(item='  ... holding a pick routed through a pool', value=int(old[old.jstar_B >= 15].holds_pooled_pick.sum())),
        dict(item="  ... holding the opponent's pick", value=int(old[old.jstar_B >= 15].holds_opponent_pick.sum())),
        dict(item='  with argmin C_hat in 15-30', value=int((old.jstar_hat_B >= 15).sum())),
        dict(item='  with argmin C_hat in 16-30', value=int((old.jstar_hat_B >= 16).sum())),
        dict(item='  with argmin C_hat in 1-14', value=int((old.jstar_hat_B <= 14).sum())),
        dict(item='  kept as reversals under 3-2-1 (transition table)', value=len(kept)),
        dict(item='  kept AND j* in 16-30', value=len(kept & deep)),
        dict(item='  kept AND j* in 1-15', value=len(kept & shallow)),
        dict(item='  removed under 3-2-1 AND j* in 16-30', value=len(removed & deep)),
        dict(item='  removed under 3-2-1 AND j* in 1-15', value=len(removed & shallow)),
        dict(item='own-pick 3-2-1 reversal at ranks 11-16: team, opponent, day', value=f'{own506.team} v {own506.opp}, {own506.day}'),
        dict(item='  league rank at the cutoff', value=int(own506['rank'])),
        dict(item='  j*', value=int(own506.jstar_B)),
        dict(item='  seeding stake (total variation)', value=float(own506.seeding_tv)),
        dict(item='  opponent carries a repeat restriction', value=bool(own506.opp_restricted)),
        dict(item='  linear tau', value=float(own506.tau_linear)),
        dict(item='  verdict without repeat restrictions', value=same.verdict_B),
        dict(item='  linear tau without repeat restrictions', value=float(same.tau_linear)),
    ]


# ---------------------------------------------------------------- R11: the ban's treatment group
def ban_treatment():
    import pandas as pd
    from protection_ban import AFFECTED, affected_count
    c = pd.read_csv(S.OUT / 'c3' / 'c3_team_games.csv')
    key = ['season', 'day', 'game', 'side']
    tau = c.pivot_table(index=key, columns='config', values='tau_linear', aggfunc='first')
    ver = c.pivot_table(index=key, columns='config', values='verdict_B', aggfunc='first')
    cond = c[c.config == 'F1L1R1_base'].set_index(key).holds_conditional_other
    ci = cond[cond].index
    rows = [dict(item='protections with P in 12..15 rewritten by the ban (six ledgers)', value=affected_count()),
            dict(item='  of which inside a pool', value=3),
            dict(item='team-games in the C3 sample', value=len(tau)),
            dict(item='  holding another team\'s pick conditionally (H3 sample)', value=len(ci))]
    for v, lab in (('F1L1R1_A', 'top-11'), ('F1L1R1_B', 'top-16')):
        dt = (tau[v] - tau['F1L1R1_base']).abs()
        dv = ver[v] != ver['F1L1R1_base']
        rows += [dict(item=f'{lab}: team-games whose linear tau changes at all', value=int((dt > 1e-12).sum())),
                 dict(item=f'{lab}:   of which in the H3 sample', value=int((dt[ci] > 1e-12).sum())),
                 dict(item=f'{lab}: team-games whose tau changes by at least delta', value=int((dt >= DELTA).sum())),
                 dict(item=f'{lab}:   of which in the H3 sample', value=int((dt[ci] >= DELTA).sum())),
                 dict(item=f'{lab}: class-B verdict changes, all', value=int(dv.sum())),
                 dict(item=f'{lab}:   in the H3 sample', value=int(dv[ci].sum())),
                 dict(item=f'{lab}:   reversals in the H3 sample, base / with ban',
                      value=f"{int((ver.loc[ci, 'F1L1R1_base'] == 'reversal').sum())} / {int((ver.loc[ci, v] == 'reversal').sum())}")]
        for (s, d, g, side), row in ver.loc[ci][ver.loc[ci, v] != ver.loc[ci, 'F1L1R1_base']].iterrows():
            team = c[(c.season == s) & (c.day == d) & (c.game == g) & (c.side == side)].team.iloc[0]
            rows.append(dict(item=f'{lab}:     {team} {d}: {row["F1L1R1_base"]} -> {row[v]}', value=''))
    # per-day reversal counts among conditional holders under the two readings (why Panel C's rows coincide)
    sub = c[c.holds_conditional_other & c.config.isin(['F1L1R1_base', 'F1L1R1_A', 'F1L1R1_B'])]
    pd_counts = sub.assign(rev=sub.verdict_B == 'reversal').groupby(['season', 'day', 'config']).rev.sum().unstack('config')
    rows.append(dict(item='days on which the per-day reversal count among conditional holders differs, top-11 vs base',
                     value=int((pd_counts['F1L1R1_A'] != pd_counts['F1L1R1_base']).sum())))
    rows.append(dict(item='days on which it differs, top-16 vs base', value=int((pd_counts['F1L1R1_B'] != pd_counts['F1L1R1_base']).sum())))
    rows.append(dict(item='days on which it differs, top-11 vs top-16', value=int((pd_counts['F1L1R1_A'] != pd_counts['F1L1R1_B']).sum())))
    return rows


# ---------------------------------------------------------------- R12: horizon-matched favourite gap
def horizon_gap():
    games = E.load_games(H.GAMES)
    _, recs = E.run_elo(games)
    rows = []
    for s in SEASONS:
        first = sorted((S.SIMULATIONS / 'primary' / s).glob('exposures_*.npz'))[0]
        meta = json.loads(bytes(np.load(first)['meta']).decode())
        cut = datetime.fromisoformat(meta['cutoff_utc'])
        st = build_state(games, s, cut)
        b = np.asarray(st['link']); r = st['ratings']
        from cutoff_state import A2P
        rem = [g for g in games if g['season'] == s and not g['end'] < cut]
        p = np.array([E.link_prob(b, r[A2P[g['h']]] - r[A2P[g['a']]]) for g in rem]); y = np.array([g['home_win'] for g in rem])
        fav = np.where(p >= 0.5, p, 1 - p); won = np.where(p >= 0.5, y, 1 - y)
        rows.append(dict(season=s, frozen_at=meta['day'], games=len(rem), predicted=float(fav.mean()), observed=float(won.mean()),
                         gap_pts=float(100 * (won.mean() - fav.mean()))))
    return rows


# ---------------------------------------------------------------- R14: 99% bands on the mean C(j) profiles (Figure 5.1)
def profiles_band(tag='primary'):
    """Mean C(j) by league-rank band, rule and portfolio, with the two-level bootstrap 99% interval on the mean.
    The registered F5_1_profiles table carries the 10th and 90th percentiles across team-games; the figure
    shades the uncertainty of the mean instead."""
    from collections import defaultdict
    sums, cnts, days = defaultdict(dict), defaultdict(dict), []
    for f in sorted((S.SIMULATIONS / tag).glob('*/exposures_*.npz')):
        d = S.load_day(f); meta = d['meta']; key = (meta['season'], meta['day']); days.append(key)
        ranks, _ = S.cutoff_ranks(meta)
        for g, (h, a) in enumerate(meta['focal_teams']):
            for side, c in ((0, h), (1, a)):
                sgn = 1.0 if side == 0 else -1.0
                band = S.band_of(int(ranks[c]))
                for pf, src in (('actual', d['DB']), ('own', d['DB_own'])):
                    for ri, r in enumerate(S.RULES):
                        m = np.cumsum(sgn * src[:, g, ri, c, :].mean(0))
                        k = (band, r, pf)
                        sums[k][key] = sums[k].get(key, 0.0) + m; cnts[k][key] = cnts[k].get(key, 0) + 1
    days = sorted(days); boot = S.Boot(days, [s for s, _ in days])
    rows = []
    for k in sorted(sums):
        num = np.zeros((len(days), 30)); den = np.zeros((len(days), 1))
        for key, v in sums[k].items():
            num[boot.idx[key]] = v; den[boot.idx[key], 0] = cnts[k][key]
        pt, lo, hi = boot.ratio(num, np.repeat(den, 30, axis=1))
        for j in range(30):
            rows.append(dict(band=k[0], rule=k[1], portfolio=k[2], j=j + 1, mean=float(pt[j]), lo99=float(lo[j]),
                             hi99=float(hi[j]), n=int(den.sum())))
    return rows


def main():
    tg = P.load_tg(); tg = tg[tg.rule.isin(['old', 'new'])].copy()
    if (OUT / 'R13_games_h2.csv').exists():
        games = read(OUT / 'R13_games_h2.csv')
        for x in games:
            x['mean_abs_third'] = float(x['mean_abs_third']); x['h2_sample'] = x['h2_sample'] == 'True'
    else:
        games = game_stakes('primary')
        write('R13_games_h2', games)
    write('R7_season_inference', season_inference(tg, games))
    write('R7b_h2_by_season', h2_by_season(games))
    pr = read(P3 / 'R2_precision_days.csv')
    write('R8_four_quantities', four_quantities(tg, games, pr))
    write('R9_h1_band_by_season', h1_band_by_season(tg))
    write('R10_sets', sets(tg))
    write('R11_ban_treatment', ban_treatment())
    write('R12_e4_horizon', horizon_gap())
    if not (OUT / 'R14_profiles_band.csv').exists():
        write('R14_profiles_band', profiles_band())
    write('R15_verdict_changes', verdict_changes(tg))
    print('wrote', OUT)


if __name__ == '__main__':
    main()

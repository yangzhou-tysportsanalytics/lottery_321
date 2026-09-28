"""Exploratory analyses, second set. Not registered; computed from the
stored primary and `norestr` team-game tables and run metadata without new simulation (addendum A1,
amendment 14). Nothing here changes a registered table or headline quantity.

  R1  mean tau by league-rank band on all four registered curves, old rule and 3-2-1, own pick and actual
      portfolio, with two-level bootstrap 99% intervals; the 3-2-1 / old ratio and its interval
  R2  precision flags: run flag vs the flag recomputed from stored batches at both constants (2 x 2 tables)
  R3  headline quantities on the days that meet the precision target at the three-look constant, on flagged / met days, and
      without 2025-26
  R4  flag rate by window tercile and by number of games on the day
  R5  season-level inference for H-a and H-b (t with 5 d.f., 95% and 99%; sign test) and H1 by season
  R6  old-rule reversals with j* in 16-30 by ledger feature; own-pick 3-2-1 reversals with the H1 crossing
      pattern; days on which the primary and `norestr` runs stopped at different looks
Usage: python exploratory_2.py
"""
import csv
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / 'ledgers'))
import analysis as S  # noqa: E402
import exploratory_1 as P  # noqa: E402
import robustness_headlines as R  # noqa: E402

OUT = S.OUT / 'exploratory_2'
CURVES = ('linear', 'concave', 'convex', 'top3_stress')
Z2, Z3, DELTA = 2.807034, 2.935199, 0.003
BANDS = ('1-3', '4-10', '11-16', '17-30')


def tau_by_band(tg):
    rows = []
    boot = P.boot_for(tg)
    for pf in ('own', 'actual'):
        for band in BANDS:
            sub = tg[(tg.portfolio == pf) & (tg.band == band)]
            for cv in CURVES:
                sums, cnt = {}, None
                for r in ('old', 'new'):
                    s = sub[sub.rule == r]
                    num = np.zeros(len(boot.days)); den = np.zeros(len(boot.days))
                    for (se, d), g in s.groupby(['season', 'day']):
                        i = boot.idx[(se, d)]; num[i] = g[f'tau_{cv}'].sum(); den[i] = len(g)
                    sums[r] = num; cnt = den
                bo = boot.W @ sums['old']; bn = boot.W @ sums['new']; bd = boot.W @ cnt
                a = 0.005
                with np.errstate(invalid='ignore', divide='ignore'):
                    mo, mn, ratio = bo / bd, bn / bd, bn / bo
                row = dict(portfolio=pf, band=band, curve=cv, n=int(cnt.sum()),
                           mean_old=sums['old'].sum() / cnt.sum(), mean_new=sums['new'].sum() / cnt.sum())
                row['ratio_new_old'] = row['mean_new'] / row['mean_old'] if row['mean_old'] else float('nan')
                for k, b in (('old', mo), ('new', mn), ('ratio', ratio)):
                    row[f'{k}_lo99'] = float(np.nanquantile(b, a)); row[f'{k}_hi99'] = float(np.nanquantile(b, 1 - a))
                rows.append(row)
    return rows


def precision(tg):
    full = P.load_tg()
    act = full[full.portfolio == 'actual']
    hw = act.groupby(['season', 'day']).se_linear.max()
    run = act.groupby(['season', 'day']).precision_met.first()
    games = full.groupby(['season', 'day']).game_id.nunique()
    days = sorted(hw.index)
    nd = {s: sorted(d for ss, d in days if ss == s) for s in {s for s, _ in days}}
    rows = []
    for (s, d) in days:
        k = nd[s].index(d)
        rows.append(dict(season=s, day=d, games=int(games[(s, d)]), tercile=1 + (3 * k) // len(nd[s]),
                         run_met=bool(run[(s, d)]), stored_met_z2=bool(Z2 * hw[(s, d)] <= DELTA),
                         stored_met_z3=bool(Z3 * hw[(s, d)] <= DELTA)))
    return rows


def crosstab(rows, a, b):
    out = []
    for va in (True, False):
        for vb in (True, False):
            out.append(dict(row=a, row_value=va, col=b, col_value=vb, days=sum(1 for r in rows if r[a] == va and r[b] == vb)))
    return out


def headline_row(t, label):
    t2 = t[t.rule.isin(['old', 'new'])]
    hd = {r['portfolio']: r for r in P.headline(t2, label=label)}
    row = dict(analysis=label, n_days=int(hd['actual']['n_days']), n_team_games=int(hd['actual']['n_team_games']),
               ha=hd['actual']['diff'], ha_lo=hd['actual']['lo99'], ha_hi=hd['actual']['hi99'],
               hb=hd['own']['diff'], hb_lo=hd['own']['lo99'], hb_hi=hd['own']['hi99'])
    row.update(R.h1(t2))
    return row


def season_inference(tg):
    from scipy import stats
    out = []
    for pf in ('actual', 'own'):
        d = []
        for s, g in tg.groupby('season'):
            n = g[(g.rule == 'new') & (g.portfolio == pf)]; o = g[(g.rule == 'old') & (g.portfolio == pf)]
            d.append((n.verdict_B == 'reversal').mean() - (o.verdict_B == 'reversal').mean())
        d = np.array(d); m, sd = d.mean(), d.std(ddof=1); se = sd / math.sqrt(len(d))
        row = dict(portfolio=pf, seasons=len(d), mean_diff=m, positive=int((d > 0).sum()),
                   sign_test_one_sided_p=0.5 ** len(d) if (d > 0).all() else float('nan'))
        for lev in (0.95, 0.99):
            q = stats.t.ppf(1 - (1 - lev) / 2, len(d) - 1)
            row[f't5_{int(lev * 100)}_lo'] = m - q * se; row[f't5_{int(lev * 100)}_hi'] = m + q * se
        out.append(row)
    return out


def h1_by_season(tg):
    out = []
    for s, g in tg.groupby('season'):
        b = g[(g.portfolio == 'own') & g['rank'].between(2, 5)]
        n, o = b[b.rule == 'new'], b[b.rule == 'old']
        rev = n[n.verdict_B == 'reversal']
        out.append(dict(season=s, n=len(n), share_neg_new=(n.sign_linear == 'win').mean(),
                        share_neg_old=(o.sign_linear == 'win').mean(), reversals_new=len(rev),
                        crossings=int(rev.crossing.sum())))
    return out


def misc(tg):
    out = []
    old = tg[(tg.rule == 'old') & (tg.portfolio == 'actual') & (tg.verdict_B == 'reversal')]
    deep = old[old.jstar_B >= 16]
    out += [dict(item='old-rule actual reversals', value=len(old)),
            dict(item='  with j* in 16-30', value=len(deep)),
            dict(item='  ... holding a pick under a conditional clause', value=int(deep.holds_conditional_other.sum())),
            dict(item='  ... holding a pick routed through a pool', value=int(deep.holds_pooled_pick.sum())),
            dict(item="  ... holding the opponent's pick", value=int(deep.holds_opponent_pick.sum())),
            dict(item='  with j* in 1-15', value=int((old.jstar_B <= 15).sum()))]
    own = tg[(tg.rule == 'new') & (tg.portfolio == 'own') & (tg.verdict_B == 'reversal')]
    out += [dict(item='own-pick 3-2-1 reversals', value=len(own)),
            dict(item='  with the H1 crossing pattern (band < 0 at some j <= 11 and > 0 at some j in 12-15)',
                 value=int(own.crossing.sum()))]
    others = tg[(tg.rule == 'old') & (tg.portfolio == 'actual') & (~tg.holds_conditional_other)]
    out += [dict(item='old-rule actual team-games without a conditional holding', value=len(others)),
            dict(item='  of which reversals', value=int((others.verdict_B == 'reversal').sum()))]
    nr = P.load_tg('norestr')
    a = tg[['season', 'day', 'n_worlds']].drop_duplicates(); b = nr[['season', 'day', 'n_worlds']].drop_duplicates()
    m = a.merge(b, on=['season', 'day'], suffixes=('', '_nr'))
    out += [dict(item='days on which primary and norestr stopped at different looks', value=int((m.n_worlds != m.n_worlds_nr).sum()))]
    return out


def write(name, rows):
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / f'{name}.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)


def main():
    tg = P.load_tg(); tg = tg[tg.rule.isin(['old', 'new'])].copy()
    write('R1_tau_by_band_curves', tau_by_band(tg))
    pr = precision(tg)
    write('R2_precision_days', pr)
    write('R2_crosstabs', crosstab(pr, 'run_met', 'stored_met_z2') + crosstab(pr, 'run_met', 'stored_met_z3') +
          crosstab(pr, 'stored_met_z2', 'stored_met_z3'))
    met3 = {(r['season'], r['day']) for r in pr if r['stored_met_z3']}
    runmet = {(r['season'], r['day']) for r in pr if r['run_met']}
    key = list(zip(tg.season, tg.day))
    sel = lambda s: tg[[k in s for k in key]]
    notsel = lambda s: tg[[k not in s for k in key]]
    write('R3_headlines', [headline_row(tg, 'all days'),
                           headline_row(sel(met3), 'days meeting the target at z = 2.935199 (stored batches)'),
                           headline_row(sel(runmet), 'days meeting the target in the run (z = 2.807034)'),
                           headline_row(notsel(runmet), 'days flagged in the run'),
                           headline_row(tg[tg.season != '2025-26'], '2025-26 excluded')])
    ter = []
    for t in (1, 2, 3):
        x = [r for r in pr if r['tercile'] == t]
        ter.append(dict(group=f'tercile {t}', days=len(x), flagged_run=sum(not r['run_met'] for r in x),
                        mean_games=np.mean([r['games'] for r in x])))
    for lo, hi in ((1, 5), (6, 8), (9, 11), (12, 15)):
        x = [r for r in pr if lo <= r['games'] <= hi]
        if x:
            ter.append(dict(group=f'{lo}-{hi} games', days=len(x), flagged_run=sum(not r['run_met'] for r in x),
                            mean_games=np.mean([r['games'] for r in x])))
    write('R4_flag_rates', ter)
    write('R5_season_inference', season_inference(tg))
    write('R5_h1_by_season', h1_by_season(tg))
    write('R6_misc', misc(tg))
    print('wrote', OUT)


if __name__ == '__main__':
    main()

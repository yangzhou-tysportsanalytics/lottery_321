"""Post-hoc (exploratory) analyses, first set.

None of these is registered. They are computed after the primary tables were opened, on the stored primary
exposure files and team-game table, without any new simulation, and are reported as exploratory
(addendum A1, amendment 13). Nothing here changes a registered table or headline quantity.

Part A (team-game table only):
  A1  reversal shares by season (rule x portfolio), and H-a by season (point estimates)
  A2  H-a / H-b excluding the 2020-21 window days that precede the 2021 trade deadline (2021-03-25)
  A3  H-a / H-b split by reversal slot j* in 1-15 and 16-30
  A4  own-pick 3-2-1 reversals by seeding-stake group (counts)
  A5  share of team-games with a linear-curve tau whose pointwise 99% upper bound is below -delta / whose
      point estimate is negative, by rule x portfolio x band; mean tau by band
  A6  rollover sign changes restricted to |tau| > delta
  A7  precision flag recomputed with the three-look constant 2.935199 (from the stored super-batch s.e.);
      flagged days by window tercile; H-a by tercile
  A8  verdict transitions old -> new for the same actual-portfolio team-game (counts)
Part B (raw exposure files, multiplier band recomputed exactly as in analysis.band_stats):
  B1  reversal subtypes: 'dominance-negative' (upper band below -delta somewhere, lower band never above 0)
      versus 'crossing' (also significantly positive somewhere), by rule x portfolio x band
  B2  mass channel: team-games whose band on M = C(30) lies below -delta / above +delta
Usage: python exploratory_1.py [--part A|B|all] [--out DIR]
Outputs CSVs and a markdown report; prints counts only.
"""
import argparse
import csv
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / 'ledgers'))
import analysis as S  # noqa: E402

ROOT = HERE.parents[1]
AN = ROOT / 'results'
OUT = AN / 'exploratory_1'
Z3, Z2, DELTA = 2.935199, 2.807034, 0.003
DEADLINE_2021 = '2021-03-25'


def load_tg(folder='primary'):
    import pandas as pd
    return pd.read_csv(AN / folder / 'team_games.csv.gz')


def boot_for(tg):
    days = sorted({(s, d) for s, d in zip(tg.season, tg.day)})
    return S.Boot(days, [s for s, _ in days])


def rows_of(tg):
    return tg.to_dict('records')


def headline(tg, pred_extra=None, label=''):
    """H-a (actual) and H-b (own): reversal share new minus old, two-level bootstrap 99% CI."""
    rows = rows_of(tg); boot = boot_for(tg); out = []
    for pf in ('actual', 'own'):
        rev = (lambda x: x['verdict_B'] == 'reversal' and (pred_extra(x) if pred_extra else True))
        n1, d1 = S.per_day(rows, boot, rev, lambda x: x['rule'] == 'new' and x['portfolio'] == pf)
        n2, d2 = S.per_day(rows, boot, rev, lambda x: x['rule'] == 'old' and x['portfolio'] == pf)
        pt, lo, hi = boot.diff_of_ratios(n1, d1, n2, d2)
        out.append(dict(analysis=label, portfolio=pf, share_new=n1.sum() / d1.sum(), share_old=n2.sum() / d2.sum(),
                        diff=pt, lo99=lo, hi99=hi, n_team_games=int(d1.sum()), n_days=len(boot.days)))
    return out


def part_a(out):
    tg = load_tg()
    tg = tg[tg.rule.isin(['old', 'new'])].copy()
    res = {}
    # A1 by season
    rows = []
    for (s, r, pf), g in tg.groupby(['season', 'rule', 'portfolio']):
        rows.append(dict(season=s, rule=r, portfolio=pf, n=len(g), n_days=g.day.nunique(),
                         reversal=(g.verdict_B == 'reversal').mean(),
                         dominance_positive=(g.verdict_B == 'dominance_positive').mean(),
                         negligible=(g.verdict_B == 'negligible').mean(),
                         unresolved=(g.verdict_B == 'unresolved').mean()))
    res['A1_by_season'] = rows
    # A2 deadline
    pre = (tg.season == '2020-21') & (tg.day <= DEADLINE_2021)
    res['A2_deadline'] = (headline(tg, label='all days') +
                          headline(tg[~pre], label=f'2020-21 days on or before {DEADLINE_2021} excluded'))
    res['A2_deadline_days'] = [dict(days_excluded=int(tg[pre].day.nunique()),
                                    first=str(tg[pre].day.min()), last=str(tg[pre].day.max()),
                                    team_games_excluded=int(len(tg[pre]) // 4))]
    # A3 j* split
    res['A3_jstar'] = (headline(tg, lambda x: 1 <= x['jstar_B'] <= 15, 'reversals with j* in 1-15') +
                       headline(tg, lambda x: x['jstar_B'] >= 16, 'reversals with j* in 16-30'))
    # A4 seeding
    own_new = tg[(tg.rule == 'new') & (tg.portfolio == 'own')]
    rev = own_new[own_new.verdict_B == 'reversal']
    res['A4_seeding'] = [dict(seed_group=k, own_new_reversals=int(v), team_games=int((own_new.seed_group == k).sum()))
                         for k, v in rev.seed_group.value_counts().items()]
    # A5 linear tau
    rows = []
    for (r, pf, b), g in tg.groupby(['rule', 'portfolio', 'band']):
        up = g.tau_linear + Z3 * g.se_linear
        rows.append(dict(rule=r, portfolio=pf, band=b, n=len(g), mean_tau_linear=g.tau_linear.mean(),
                         share_upper_below_minus_delta=(up < -DELTA).mean(),
                         share_upper_below_zero=(up < 0).mean(),
                         share_point_negative=(g.tau_linear < 0).mean()))
    for (r, pf), g in tg.groupby(['rule', 'portfolio']):
        up = g.tau_linear + Z3 * g.se_linear
        rows.append(dict(rule=r, portfolio=pf, band='all', n=len(g), mean_tau_linear=g.tau_linear.mean(),
                         share_upper_below_minus_delta=(up < -DELTA).mean(),
                         share_upper_below_zero=(up < 0).mean(),
                         share_point_negative=(g.tau_linear < 0).mean()))
    res['A5_linear_tau'] = rows
    # A6 rollover sign changes, material only
    rows = []
    for (r, pf), g in tg.groupby(['rule', 'portfolio']):
        for rho in ('rho50', 'rho80'):
            t0, t1 = g.tau_linear, g[f'tau_linear_{rho}']
            flip = np.sign(t0) != np.sign(t1)
            rows.append(dict(rule=r, portfolio=pf, rho=rho, n=len(g), flips_all=int(flip.sum()),
                             flips_material=int((flip & (t0.abs() > DELTA)).sum()),
                             flips_both_material=int((flip & (t0.abs() > DELTA) & (t1.abs() > DELTA)).sum())))
    res['A6_rollover_flips'] = rows
    # A7 precision flags (actual portfolio, linear curve, old/new/delta), stored super-batch s.e.
    full = load_tg(); full = full[full.portfolio == 'actual']
    hw = full.groupby(['season', 'day']).se_linear.max()
    run_flag = full.groupby(['season', 'day']).precision_met.first()
    days = sorted(hw.index)
    nd = {s: sorted(d for ss, d in days if ss == s) for s in {s for s, _ in days}}
    rows = []
    for (s, d) in days:
        k = nd[s].index(d); third = 1 + (3 * k) // len(nd[s])
        rows.append(dict(season=s, day=d, tercile=third, run_precision_met=bool(run_flag[(s, d)]),
                         met_z2_storedse=bool(Z2 * hw[(s, d)] <= DELTA), met_z3_storedse=bool(Z3 * hw[(s, d)] <= DELTA)))
    res['A7_precision_days'] = rows
    agree = sum(r['run_precision_met'] == r['met_z2_storedse'] for r in rows)
    ter = defaultdict(lambda: [0, 0, 0])
    for r in rows:
        ter[r['tercile']][0] += 1; ter[r['tercile']][1] += (not r['run_precision_met']); ter[r['tercile']][2] += (not r['met_z3_storedse'])
    res['A7_summary'] = ([dict(item='days', value=len(rows)),
                          dict(item='run flag reproduced from stored s.e. at z=2.807034', value=agree),
                          dict(item='met at z=2.807034 (run)', value=sum(r['run_precision_met'] for r in rows)),
                          dict(item='met at z=2.935199 (stored s.e.)', value=sum(r['met_z3_storedse'] for r in rows))] +
                         [dict(item=f'tercile {t}: days / flagged (run) / flagged (z3)', value=f'{a} / {b} / {c}')
                          for t, (a, b, c) in sorted(ter.items())])
    terc = {(r['season'], r['day']): r['tercile'] for r in rows}
    tg['tercile'] = [terc[(s, d)] for s, d in zip(tg.season, tg.day)]
    res['A7_headline_by_tercile'] = sum((headline(tg[tg.tercile == t], label=f'window tercile {t}') for t in (1, 2, 3)), [])
    # A8 transitions
    a = tg[tg.portfolio == 'actual']
    key = ['season', 'day', 'game_id', 'side']
    m = a[a.rule == 'old'][key + ['verdict_B']].merge(a[a.rule == 'new'][key + ['verdict_B']], on=key, suffixes=('_old', '_new'))
    res['A8_transitions'] = [dict(old=o, new=n, count=int(c)) for (o, n), c in
                             Counter(zip(m.verdict_B_old, m.verdict_B_new)).items()]
    # A9 repeat restrictions: share of team-games whose linear-curve tau_new moves by at least delta, by group
    nr = load_tg('norestr'); nr = nr[nr.rule == 'new']
    pr = load_tg(); pr = pr[pr.rule == 'new']
    key = ['season', 'day', 'game_id', 'side', 'portfolio']
    m = pr[key + ['tau_linear', 'self_restricted', 'holds_conditional_other', 'verdict_B', 'n_worlds']].merge(
        nr[key + ['tau_linear', 'verdict_B', 'n_worlds']], on=key, suffixes=('', '_nr'))
    rows = []
    restricted_holder = set()
    for (pf, grp), g in m.assign(group=np.where(m.self_restricted, 'restricted_native', 'other')).groupby(['portfolio', 'group']):
        d = g.tau_linear - g.tau_linear_nr          # with restrictions minus without
        rows.append(dict(portfolio=pf, group=grp, n=len(g), mean_change=d.mean(), moved_ge_delta=(d.abs() >= DELTA).mean(),
                         moved_down=(d <= -DELTA).mean(), moved_up=(d >= DELTA).mean(),
                         reversal_with=(g.verdict_B == 'reversal').mean(), reversal_without=(g.verdict_B_nr == 'reversal').mean(),
                         same_worlds=(g.n_worlds == g.n_worlds_nr).mean()))
    res['A9_restrictions'] = rows
    # A10 H1 band magnitudes (ranks 2-5) and rank 1-3, own and actual portfolio
    rows = []
    for (r, pf), g in tg.groupby(['rule', 'portfolio']):
        for lab, sel in (('ranks 2-5', g['rank'].between(2, 5)), ('ranks 1-3', g['rank'].between(1, 3))):
            h = g[sel]; up = h.tau_linear + Z3 * h.se_linear
            rows.append(dict(rule=r, portfolio=pf, group=lab, n=len(h), mean_tau=h.tau_linear.mean(),
                             q10=h.tau_linear.quantile(.1), median=h.tau_linear.median(), q90=h.tau_linear.quantile(.9),
                             share_sig_negative=(h.sign_linear == 'win').mean(), share_upper_below_minus_delta=(up < -DELTA).mean()))
    res['A10_h1_magnitudes'] = rows
    # A11 class B vs class C verdict agreement
    res['A11_class_agreement'] = [dict(rule=r, portfolio=pf, n=len(g), differ=int((g.verdict_B != g.verdict_C).sum()))
                                  for (r, pf), g in tg.groupby(['rule', 'portfolio'])]
    return res


def part_b(out):
    files = sorted((S.SIMULATIONS / 'primary').glob('*/exposures_*.npz'))
    rows = []
    for i, p in enumerate(files):
        d = S.load_day(p); meta = d['meta']
        ranks, _ = S.cutoff_ranks(meta)
        for g, (h, a) in enumerate(meta['focal_teams']):
            for side, c in ((0, h), (1, a)):
                sgn = 1.0 if side == 0 else -1.0
                for pf, src in (('actual', d['DB']), ('own', d['DB_own'])):
                    for ri, r in enumerate(S.RULES):
                        Cb = np.cumsum(sgn * src[:, g, ri, c, :], axis=1)
                        B = Cb.shape[0]
                        m = Cb.mean(0); sd = Cb.std(0, ddof=1); se = sd / math.sqrt(B)
                        ok = sd > 1e-12
                        cB = 0.0
                        if ok.any():
                            resid = (Cb[:, ok] - m[ok]) / (sd[ok] * math.sqrt(B - 1))
                            cB = float(np.quantile(np.abs(S._xi(B) @ resid).max(1), 0.99))
                        v, j = S.verdict(m, se, cB, 30)
                        up, lo = m + cB * se, m - cB * se
                        rows.append(dict(season=meta['season'], day=meta['day'], game=g, side=side, rule=r, portfolio=pf,
                                         band=S.band_of(int(ranks[c])), verdict=v, jstar=j,
                                         pos0=bool(np.any(lo > 0)), posd=bool(np.any(lo > DELTA)),
                                         M_neg=bool(up[29] < -DELTA), M_pos=bool(lo[29] > DELTA)))
        if (i + 1) % 50 == 0:
            print(f'{i + 1}/{len(files)} days', flush=True)
    import pandas as pd
    t = pd.DataFrame(rows)
    res = {}
    rr = []
    for keys, g in list(t.groupby(['rule', 'portfolio', 'band'])) + [((r, pf, 'all'), g) for (r, pf), g in t.groupby(['rule', 'portfolio'])]:
        rev = g[g.verdict == 'reversal']
        rr.append(dict(rule=keys[0], portfolio=keys[1], band=keys[2], n=len(g), reversals=len(rev),
                       dominance_negative=int((~rev.pos0).sum()), crossing_pos0=int(rev.pos0.sum()),
                       crossing_posdelta=int(rev.posd.sum())))
    res['B1_reversal_subtypes'] = rr
    res['B2_mass'] = [dict(rule=r, portfolio=pf, n=len(g), M_band_below_minus_delta=int(g.M_neg.sum()),
                           M_band_above_delta=int(g.M_pos.sum()))
                      for (r, pf), g in t.groupby(['rule', 'portfolio'])]
    stored = load_tg(); stored = stored[stored.rule.isin(['old', 'new'])]
    res['B0_check'] = [dict(item='team-game rows', value=len(t)),
                       dict(item='reversals recomputed / stored',
                            value=f"{int((t.verdict == 'reversal').sum())} / {int((stored.verdict_B == 'reversal').sum())}")]
    return res


def part_c(out):
    """C1: seeding stake with conference seeds 1-6 merged into one class (they do not affect lottery
    membership), recomputed from the stored ST arrays; own-pick 3-2-1 reversals and all team-games by group."""
    import pandas as pd
    rows = []
    for p in sorted((S.SIMULATIONS / 'primary').glob('*/exposures_*.npz')):
        d = np.load(p); ST = d['ST']; meta = json.loads(bytes(d['meta']).decode())
        merged = np.concatenate([ST[..., :6].sum(-1, keepdims=True), ST[..., 6:]], axis=-1)
        for g, (h, a) in enumerate(meta['focal_teams']):
            for side, c in ((0, h), (1, a)):
                lose, win = (1, 0) if side == 0 else (0, 1)
                tv = 0.5 * float(np.abs(merged[g, lose, c] - merged[g, win, c]).sum())
                tv0 = 0.5 * float(np.abs(ST[g, lose, c] - ST[g, win, c]).sum())
                rows.append(dict(season=meta['season'], day=meta['day'], game_id=int(meta['focal_game_ids'][g]),
                                 side='home' if side == 0 else 'away', tv_merged=tv, tv_registered=tv0))
    t = pd.DataFrame(rows)
    tg = load_tg(); tg = tg[(tg.rule == 'new')]
    m = tg.merge(t, on=['season', 'day', 'game_id', 'side'])
    grp = lambda x: np.where(x < 0.01, '<0.01', np.where(x < 0.05, '0.01-0.05', '>=0.05'))
    m['g_merged'] = grp(m.tv_merged); m['g_reg'] = grp(m.tv_registered)
    res = []
    for pf in ('actual', 'own'):
        h = m[m.portfolio == pf]
        for col, lab in (('g_reg', 'registered (seeds 1-6 separate)'), ('g_merged', 'seeds 1-6 merged')):
            for k, g in h.groupby(col):
                res.append(dict(portfolio=pf, measure=lab, group=k, team_games=len(g),
                                reversals=int((g.verdict_B == 'reversal').sum()),
                                reversal_share=(g.verdict_B == 'reversal').mean()))
    return {'C1_seeding_merged': res}


def write(res, out):
    out.mkdir(parents=True, exist_ok=True)
    for name, rows in res.items():
        if not rows:
            continue
        with open(out / f'{name}.csv', 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print('wrote', ', '.join(sorted(res)))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--part', default='all', choices=('A', 'B', 'C', 'all'))
    ap.add_argument('--out', default=str(OUT))
    a = ap.parse_args()
    out = Path(a.out)
    if a.part in ('A', 'all'):
        write(part_a(out), out)
    if a.part in ('B', 'all'):
        write(part_b(out), out)
    if a.part in ('C', 'all'):
        write(part_c(out), out)

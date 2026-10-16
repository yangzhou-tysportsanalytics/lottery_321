"""Exploratory analyses, fifth set, parts 1 to 4,
from the stored outputs of the primary run and of the C3 run (no new simulation).

Everything here is exploratory, added after the results were opened: no registered quantity, verdict or table changes.
Intervals are 99% two-level bootstrap intervals (seasons, then days within season; 9,999 replicates, seed
2026092201: analysis.Boot) unless a row says otherwise.

  1  last-slot value v_a(k) = a + (1 - a) v(k), a in {0.1, 0.25, 0.5}: tau_a = (1 - a) tau + a M, batch by batch.
  2  rollover criterion C_rho(j) = C(j) - rho (j/30) M, rho in {0.5, 0.8}: batch-level C_rho, its own multiplier
     sup-t band (10,000 draws, seed 20260922, exactly analysis.band_stats), class-B verdicts.
  3  the stakes network on own-pick-only portfolios against actual portfolios, all four curves, delta in
     {0.001, 0.003, 0.005}.
  4  (a) H3 on the team-games whose incentives the ban changes; (b) Table 5.6 with both bootstraps; (c) the
     argmin tie-break of j*; (d) H1 weighting.
Before any new number is written, the pass reproduces the registered values it shares with the primary tables
((H-a), (H-b), H2, the R16 counts, the median TP); a mismatch stops the run.
Outputs: results/exploratory_5/ - CSV files, LaTeX table bodies in tables/ (the paper's format), and
E5_checks.json. Usage: python exploratory_5.py [--workers N]
"""
import argparse
import csv
import json
import math
import re
import subprocess
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / 'ledgers'))
import analysis as S  # noqa: E402
from value import CURVES  # noqa: E402
from teams import TEAMS  # noqa: E402

OUT = S.OUT / 'exploratory_5'
TAB = OUT / 'tables'
A_VALUES = (0.1, 0.25, 0.5)
DELTAS = (0.001, S.DELTA, 0.005)
BANDS = [b[2] for b in S.BANDS] + ['all']
akey = lambda a: f'a{int(round(100 * a)):02d}'
dkey = lambda d: f'd{int(round(10000 * d)):02d}'


# ---------------------------------------------------------------- one pass over the primary day files
def day_worker(path):
    d = S.load_day(Path(path)); meta = d['meta']; season, day = meta['season'], meta['day']
    year = int(season[:4]) + 1
    ranks, _ = S.cutoff_ranks(meta)
    cl, _ = S.claims(year)
    DB, DBo = d['DB'], d['DB_own']
    jgrid = np.arange(1, 31, dtype=float)[None, :] / 30.0
    tg, games = [], []
    for g, (h, a) in enumerate(meta['focal_teams']):
        gid = meta['focal_game_ids'][g]
        sign = {}
        for side, c in ((0, h), (1, a)):
            sgn = 1.0 if side == 0 else -1.0
            for pf, src in (('actual', DB), ('own', DBo)):
                for ri, r in enumerate(S.RULES):
                    db = sgn * src[:, g, ri, c, :]
                    Cb = np.cumsum(db, axis=1)
                    m, se, crit = S.band_stats(Cb)
                    v0, j0 = S.verdict(m, se, crit['B'], 30)
                    up = m + crit['B'] * se
                    row = {'season': season, 'day': day, 'game_id': gid, 'side': side, 'team': TEAMS[c],
                           'rank': int(ranks[c]), 'band': S.band_of(int(ranks[c])), 'rule': r, 'portfolio': pf,
                           'verdict_B': v0, 'jstar_B': j0, 'M': float(m[29]),
                           'argmin_ties': int(np.sum(up == up.min())) if v0 == 'reversal' else 0}
                    for rho in S.RHOS:
                        Cr = Cb - rho * jgrid * Cb[:, 29:30]
                        mr, ser, cr = S.band_stats(Cr)
                        vr, jr = S.verdict(mr, ser, cr['B'], 30)
                        row[f'verdict_B_rho{int(100 * rho)}'] = vr
                    Mb = db.sum(1)
                    for cv, v in CURVES.items():
                        t = db @ v
                        mt, st = float(t.mean()), float(t.std(ddof=1) / math.sqrt(len(t)))
                        row[f'tau_{cv}'] = mt; row[f'se_{cv}'] = st
                        sign[(side, r, pf, cv)] = S.curve_sign(mt, st)
                        for a_ in A_VALUES:
                            ta = (1 - a_) * t + a_ * Mb
                            row[f'tau_{cv}_{akey(a_)}'] = float(ta.mean())
                            row[f'se_{cv}_{akey(a_)}'] = float(ta.std(ddof=1) / math.sqrt(len(ta)))
                    tg.append(row)
        third = np.array([x for x in range(30) if x not in (h, a)])
        h2s = S.third_party_claim(year, h, a, cl)
        for ri, r in enumerate(S.RULES):
            for pf, src in (('actual', DB), ('own', DBo)):
                mass = (-(src[:, g, ri].sum(-1))).mean(0)            # value of a home win under v = 1
                for cv, v in CURVES.items():
                    s = (-(src[:, g, ri] @ v)).mean(0)
                    rec = {'season': season, 'day': day, 'game_id': gid, 'rule': r, 'portfolio': pf, 'curve': cv,
                           'h2_sample': bool(h2s), 'type': S.typology(sign[(0, r, pf, cv)], sign[(1, r, pf, cv)])}
                    for dl in DELTAS:
                        mat = np.abs(s) >= dl
                        tot = float(np.abs(s[mat]).sum()); th = float(np.abs(s[third][mat[third]]).sum())
                        k = dkey(dl)
                        rec[f'tp_{k}'] = th / tot if tot >= dl else float('nan')
                        rec[f'mean_abs_third_{k}'] = th / len(third)
                    if cv == 'linear':
                        for a_ in A_VALUES:
                            sa = (1 - a_) * s + a_ * mass
                            mat = np.abs(sa) >= S.DELTA
                            rec[f'mean_abs_third_{akey(a_)}'] = float(np.abs(sa[third][mat[third]]).sum()) / len(third)
                    games.append(rec)
    return tg, games


def collect(workers):
    files = [str(f) for f in sorted((S.SIMULATIONS / 'primary').glob('*/exposures_*.npz'))]
    tg, games = [], []
    with ProcessPoolExecutor(max_workers=workers) as ex:              # map keeps the file order
        for a, b in ex.map(day_worker, files, chunksize=2):
            tg += a; games += b
    return tg, games, len(files)


# ---------------------------------------------------------------- bootstrap helpers
def boot_of(rows, two_level=True):
    days = sorted({(r['season'], r['day']) for r in rows})
    return S.Boot(days, [s for s, _ in days], two_level=two_level)


def day_sums(rows, boot, val, sel):
    num = np.zeros(len(boot.days)); den = np.zeros(len(boot.days))
    for r in rows:
        if sel(r):
            v = val(r)
            if v == v:
                i = boot.idx[(r['season'], r['day'])]
                num[i] += v; den[i] += 1
    return num, den


def mean_ci(rows, boot, val, sel):
    num, den = day_sums(rows, boot, val, sel)
    if not den.sum():
        return float('nan'), float('nan'), float('nan'), 0
    pt, lo, hi = boot.ratio(num[:, None], den[:, None])
    return float(pt[0]), float(lo[0]), float(hi[0]), int(den.sum())


def reps_of(boot, num, den):
    with np.errstate(invalid='ignore', divide='ignore'):
        return (boot.W @ num) / (boot.W @ den)


def q99(x):
    a = (1 - S.BOOT_LEVEL) / 2
    return float(np.nanquantile(x, a)), float(np.nanquantile(x, 1 - a))


def median_ci(rows, boot, val, sel):
    """Median over rows, with a two-level bootstrap interval: each replicate weights every row by the number of
    times its day is drawn (a weighted median over the resampled rows)."""
    pairs = sorted((val(r), boot.idx[(r['season'], r['day'])]) for r in rows if sel(r) and val(r) == val(r))
    if not pairs:
        return float('nan'), float('nan'), float('nan'), 0
    x = np.array([p[0] for p in pairs]); di = np.array([p[1] for p in pairs])
    w = boot.W[:, di]                                                  # (reps, rows), rows sorted by value
    cw = np.cumsum(w, axis=1)
    half = cw[:, -1:] / 2.0
    k = np.argmax(cw >= half, axis=1)
    lo, hi = q99(x[k])
    return float(np.median(x)), lo, hi, len(x)


# ---------------------------------------------------------------- part 1
def item1(tg, games, boot):
    out_mean, out_ratio, out_sign, out_h2 = [], [], [], []
    for pf in S.PORTFOLIOS:
        for cv in CURVES:
            for a_ in (0.0,) + A_VALUES:
                col = f'tau_{cv}' if a_ == 0 else f'tau_{cv}_{akey(a_)}'
                se_col = f'se_{cv}' if a_ == 0 else f'se_{cv}_{akey(a_)}'
                for rule in S.RULES:
                    for band in BANDS:
                        sel = lambda r, rule=rule, band=band: (r['rule'] == rule and r['portfolio'] == pf
                                                               and (band == 'all' or r['band'] == band))
                        pt, lo, hi, n = mean_ci(tg, boot, lambda r, col=col: r[col], sel)
                        out_mean.append(dict(portfolio=pf, curve=cv, a=a_, rule=rule, band=band, mean=pt, lo99=lo,
                                             hi99=hi, n=n))
                    sub = [r for r in tg if r['rule'] == rule and r['portfolio'] == pf]
                    base = np.array([r[f'tau_{cv}'] for r in sub]); new = np.array([r[col] for r in sub])
                    sen = np.array([r[se_col] for r in sub])
                    diff_sign = np.sign(new) != np.sign(base)
                    both = (np.abs(base) > S.DELTA) & (np.abs(new) > S.DELTA)
                    out_sign.append(dict(portfolio=pf, curve=cv, a=a_, rule=rule, n=len(sub),
                                         share_sign_differs=float(diff_sign.mean()),
                                         share_sign_differs_both_above_delta=float((diff_sign & both).mean()),
                                         share_sig_positive=float((new - S.Z * sen > 0).mean()),
                                         share_sig_negative=float((new + S.Z * sen < 0).mean())))
                # ratio new / old of the mean for ranks 4-10
                sel_n = lambda r: r['rule'] == 'new' and r['portfolio'] == pf and r['band'] == '4-10'
                sel_o = lambda r: r['rule'] == 'old' and r['portfolio'] == pf and r['band'] == '4-10'
                nn, dn = day_sums(tg, boot, lambda r, col=col: r[col], sel_n)
                no, do = day_sums(tg, boot, lambda r, col=col: r[col], sel_o)
                pt = (nn.sum() / dn.sum()) / (no.sum() / do.sum())
                lo, hi = q99(reps_of(boot, nn, dn) / reps_of(boot, no, do))
                out_ratio.append(dict(portfolio=pf, curve=cv, a=a_, ratio_new_over_old_4_10=float(pt), lo99=lo, hi99=hi))
    # H2 under tau_a, linear curve, registered sample
    by = {(x['season'], x['day'], x['game_id'], x['rule']): x for x in games
          if x['curve'] == 'linear' and x['portfolio'] == 'actual'}
    for a_ in (0.0,) + A_VALUES:
        col = f'mean_abs_third_{dkey(S.DELTA)}' if a_ == 0 else f'mean_abs_third_{akey(a_)}'
        num = np.zeros(len(boot.days)); den = np.zeros(len(boot.days))
        for (s, dd, g, r), x in by.items():
            if r == 'old' and x['h2_sample']:
                i = boot.idx[(s, dd)]
                num[i] += by[(s, dd, g, 'new')][col] - x[col]; den[i] += 1
        pt, lo, hi = boot.ratio(num[:, None], den[:, None])
        out_h2.append(dict(a=a_, n_games=int(den.sum()), h2_mean_diff_new_minus_old=float(pt[0]), lo99=float(lo[0]),
                           hi99=float(hi[0])))
    return out_mean, out_ratio, out_sign, out_h2


# ---------------------------------------------------------------- part 2
VFIELDS = [('0', 'verdict_B')] + [(str(int(100 * r)), f'verdict_B_rho{int(100 * r)}') for r in S.RHOS]


def item2(tg, boot):
    shares, heads, trans = [], [], []
    for rho, field in VFIELDS:
        for pf in S.PORTFOLIOS:
            for rule in S.RULES:
                sel = lambda r, rule=rule: r['rule'] == rule and r['portfolio'] == pf
                nums, dens = [], []
                for v in S.VERDICTS:
                    n, d_ = S.per_day(tg, boot, lambda r, v=v: r[field] == v, sel)
                    nums.append(n); dens.append(d_)
                pt, lo, hi = boot.ratio(np.stack(nums, 1), np.stack(dens, 1))
                for k, v in enumerate(S.VERDICTS):
                    shares.append(dict(rho=float(rho) / 100, portfolio=pf, rule=rule, verdict=v, share=float(pt[k]),
                                       lo99=float(lo[k]), hi99=float(hi[k]), n=int(dens[k].sum())))
            n1, d1 = S.per_day(tg, boot, lambda r: r[field] == 'reversal', lambda r: r['rule'] == 'new' and r['portfolio'] == pf)
            n2, d2 = S.per_day(tg, boot, lambda r: r[field] == 'reversal', lambda r: r['rule'] == 'old' and r['portfolio'] == pf)
            pt, lo, hi = boot.diff_of_ratios(n1, d1, n2, d2)
            heads.append(dict(rho=float(rho) / 100, quantity='(H-a)' if pf == 'actual' else '(H-b)', portfolio=pf,
                              share_new=float(n1.sum() / d1.sum()), share_old=float(n2.sum() / d2.sum()),
                              diff=float(pt), lo99=float(lo), hi99=float(hi)))
            if rho != '0':
                for rule in S.RULES:
                    c = Counter((r['verdict_B'], r[field]) for r in tg if r['rule'] == rule and r['portfolio'] == pf)
                    for (a, b), n in sorted(c.items()):
                        trans.append(dict(rho=float(rho) / 100, portfolio=pf, rule=rule, verdict_rho0=a,
                                          verdict_rho=b, n=n, changed=a != b))
    return shares, heads, trans


# ---------------------------------------------------------------- part 3
def item3(games, boot):
    rows, pairs = [], []
    h2 = lambda x: x['h2_sample']
    for rule in S.RULES:
        for cv in CURVES:
            for pf in S.PORTFOLIOS:
                sel = lambda x, pf=pf: x['rule'] == rule and x['curve'] == cv and x['portfolio'] == pf
                for dl in DELTAS:
                    k = dkey(dl)
                    med, mlo, mhi, n_def = median_ci(games, boot, lambda x, k=k: x[f'tp_{k}'], sel)
                    n, d_ = S.per_day(games, boot, lambda x, k=k: x[f'tp_{k}'] > 0.5,
                                      lambda x, k=k: sel(x) and x[f'tp_{k}'] == x[f'tp_{k}'])
                    dom, dlo, dhi = boot.ratio(n[:, None], d_[:, None])
                    rec = dict(rule=rule, curve=cv, portfolio=pf, delta=dl, tp_defined=n_def, tp_median=med,
                               tp_median_lo99=mlo, tp_median_hi99=mhi, tp_dominated_share=float(dom[0]),
                               tp_dominated_lo99=float(dlo[0]), tp_dominated_hi99=float(dhi[0]))
                    if dl == S.DELTA:
                        for lab, extra in (('all', lambda x: True), ('h2', h2)):
                            pt, lo, hi, nn = mean_ci(games, boot, lambda x, k=k: x[f'mean_abs_third_{k}'],
                                                     lambda x, extra=extra: sel(x) and extra(x))
                            rec[f'mean_abs_third_{lab}'] = pt; rec[f'mean_abs_third_{lab}_lo99'] = lo
                            rec[f'mean_abs_third_{lab}_hi99'] = hi; rec[f'n_games_{lab}'] = nn
                        nums, dens = [], []
                        for ty in S.TYPES:
                            n, d_ = S.per_day(games, boot, lambda x, ty=ty: x['type'] == ty, sel)
                            nums.append(n); dens.append(d_)
                        pt, lo, hi = boot.ratio(np.stack(nums, 1), np.stack(dens, 1))
                        for j, ty in enumerate(S.TYPES):
                            rec[f'type_{ty}'] = float(pt[j]); rec[f'type_{ty}_lo99'] = float(lo[j])
                            rec[f'type_{ty}_hi99'] = float(hi[j])
                    rows.append(rec)
    # paired differences actual - own on the same games, and the difference in differences (3-2-1 - old)
    k = dkey(S.DELTA)
    by = {(x['season'], x['day'], x['game_id'], x['rule'], x['curve'], x['portfolio']): x for x in games}
    keys = sorted({(s, d, g, c) for (s, d, g, r, c, p) in by})
    for cv in CURVES:
        for meas, need_def in (('mean_abs_third', False), ('tp', True)):
            col = f'{meas}_{k}'
            per = {}
            for rule in S.RULES:
                num = np.zeros(len(boot.days)); den = np.zeros(len(boot.days))
                for (s, d, g, c) in keys:
                    if c != cv:
                        continue
                    xa, xo = by[(s, d, g, rule, cv, 'actual')][col], by[(s, d, g, rule, cv, 'own')][col]
                    if need_def and not (xa == xa and xo == xo):
                        continue
                    i = boot.idx[(s, d)]; num[i] += xa - xo; den[i] += 1
                pt, lo, hi = boot.ratio(num[:, None], den[:, None]); per[rule] = (num, den)
                pairs.append(dict(curve=cv, measure=meas, contrast=f'actual - own, {rule}', n_games=int(den.sum()),
                                  diff=float(pt[0]), lo99=float(lo[0]), hi99=float(hi[0])))
            (nn, dn), (no, do) = per['new'], per['old']
            pt, lo, hi = boot.diff_of_ratios(nn, dn, no, do)
            pairs.append(dict(curve=cv, measure=meas, contrast='(actual - own), 3-2-1 minus old',
                              n_games=int(min(dn.sum(), do.sum())), diff=float(pt), lo99=float(lo), hi99=float(hi)))
    return rows, pairs


# ---------------------------------------------------------------- part 4 (a), (b): C3
def item4_c3():
    import c3_analysis as C3
    import pandas as pd
    out_a, out_b = [], []
    # (a) H3 on the team-games whose linear tau the ban changes (R11's definition), with both bootstraps
    c = pd.read_csv(S.OUT / 'c3' / 'c3_team_games.csv'); c['day'] = c['day'].astype(str)
    key = ['season', 'day', 'game', 'side']
    tau = c.pivot_table(index=key, columns='config', values='tau_linear', aggfunc='first')
    ver = c.pivot_table(index=key, columns='config', values='verdict_B', aggfunc='first')
    cond = c[c.config == 'F1L1R1_base'].set_index(key).holds_conditional_other
    days = sorted({(s, d) for s, d, _, _ in tau.index})
    boots = {'two-level': S.Boot(days, [s for s, _ in days]),
             'day-clustered': S.Boot(days, [s for s, _ in days], two_level=False)}
    for v, lab in (('F1L1R1_A', 'A: top-11'), ('F1L1R1_B', 'B: top-16')):
        aff = [k for k in tau.index if cond[k] and abs(tau.loc[k, v] - tau.loc[k, 'F1L1R1_base']) > 1e-12]
        for bname, bt in boots.items():
            vec = lambda f: _vec(bt, aff, f)
            rec = dict(reading=lab, bootstrap=bname, team_games=len(aff))
            nb, db_ = vec(lambda k: ver.loc[k, 'F1L1R1_base'] == 'reversal')
            nw, dw = vec(lambda k: ver.loc[k, v] == 'reversal')
            tb, _ = vec(lambda k: tau.loc[k, 'F1L1R1_base'])
            tw, _ = vec(lambda k: tau.loc[k, v])
            for name, n_, d_ in (('reversal_share_without', nb, db_), ('reversal_share_with', nw, dw),
                                 ('mean_tau_linear_without', tb, db_), ('mean_tau_linear_with', tw, dw)):
                pt, lo, hi = bt.ratio(n_[:, None], d_[:, None])
                rec[name] = float(pt[0]); rec[f'{name}_lo99'] = float(lo[0]); rec[f'{name}_hi99'] = float(hi[0])
            for name, (n1, d1, n2, d2) in (('reversal_share_change', (nw, dw, nb, db_)),
                                           ('mean_tau_linear_change', (tw, dw, tb, db_))):
                pt, lo, hi = bt.diff_of_ratios(n1, d1, n2, d2)
                rec[name] = float(pt); rec[f'{name}_lo99'] = float(lo); rec[f'{name}_hi99'] = float(hi)
            out_a.append(rec)
    # (b) Table 5.6, Panels A-C, recomputed with each bootstrap from the C3 day files
    tg, games, diags = C3.collect()
    days = sorted({(d['season'], d['day']) for d in diags})
    for bname, two in (('two-level', True), ('day-clustered', False)):
        T = C3.tables(tg, games, S.Boot(days, [s for s, _ in days], two_level=two), diags)
        for tname in ('C3_1_outcomes', 'C3_3_shapley', 'C3_4_H3'):
            for r in T[tname]:
                if r.get('band', 'all') == 'all':
                    out_b.append(dict(table=tname, bootstrap=bname, **r))
    return out_a, out_b


def _vec(bt, keys, f):
    num = np.zeros(len(bt.days)); den = np.zeros(len(bt.days))
    for k in keys:
        i = bt.idx[(k[0], k[1])]; num[i] += float(f(k)); den[i] += 1
    return num, den


# ---------------------------------------------------------------- part 4 (c), (d)
def item4_cd(tg, boot):
    out = []
    for rule in S.RULES:
        for pf in S.PORTFOLIOS:
            rev = [r for r in tg if r['rule'] == rule and r['portfolio'] == pf and r['verdict_B'] == 'reversal']
            out.append(dict(item='(c) reversals with a tie at the minimum of the upper band', rule=rule, portfolio=pf,
                            reversals=len(rev), with_tie=sum(r['argmin_ties'] > 1 for r in rev),
                            note='j* = numpy.argmin(upper band) + 1 (analysis.verdict): the smallest slot among ties'))
    inb = lambda r: S.H1_BAND[0] <= r['rank'] <= S.H1_BAND[1]
    sel = lambda rule: (lambda r: r['rule'] == rule and r['portfolio'] == 'own' and inb(r))
    win = lambda r: S.curve_sign(r['tau_linear'], r['se_linear']) == 'win'
    n1, d1 = S.per_day(tg, boot, win, sel('new')); n2, d2 = S.per_day(tg, boot, win, sel('old'))
    pt, lo, hi = boot.diff_of_ratios(n1, d1, n2, d2)
    per_season = []
    for s in sorted({r['season'] for r in tg}):
        a = [win(r) for r in tg if r['season'] == s and sel('new')(r)]; b = [win(r) for r in tg if r['season'] == s and sel('old')(r)]
        per_season.append(np.mean(a) - np.mean(b))
    per_season = np.array(per_season)
    from math import sqrt
    t99 = 4.032142983557536                                              # t quantile, 5 d.f., 0.995
    se = per_season.std(ddof=1) / sqrt(len(per_season))
    out.append(dict(item='(d) H1, pooled over team-games (two-level bootstrap; seasons weighted by team-games)',
                    rule='new-old', portfolio='own', value=float(pt), lo99=float(lo), hi99=float(hi), n=int(d1.sum())))
    out.append(dict(item='(d) H1, seasons weighted equally (mean of the six season differences; t, 5 d.f.)',
                    rule='new-old', portfolio='own', value=float(per_season.mean()),
                    lo99=float(per_season.mean() - t99 * se), hi99=float(per_season.mean() + t99 * se), n=len(per_season)))
    return out


# ---------------------------------------------------------------- part 4 (e): worked examples for the introduction
SLOTS_SHOWN = (1, 4, 10, 14, 15, 20, 30)


def ledger_footprint(led, team, opp):
    """The ledger entries that matter for `team` in a game against `opp`: its own native pick, every native pick it
    holds under any rule, and the opponent's native pick."""
    nat = led['natives']; out = []
    for n, e in nat.items():
        r = e['rule']; t = r['type']
        holds = ((t == 'to' and r.get('holder') == team) or (t == 'protected' and r.get('else') == team)
                 or (t == 'reverse' and r.get('holder') == team)
                 or (t == 'pool' and any(a.get('holder') == team for a in r.get('allocation', []))))
        if n == team or n == opp or holds:
            out.append(dict(native=n, role='own pick' if n == team else ('opponent pick' if n == opp else 'held'),
                            held_by_team=bool(holds), rule=r, text=e.get('text', ''), sources=e.get('sources', []),
                            confidence=e.get('confidence', '')))
    return out


def examples(n_candidates=3):
    import pandas as pd
    t = pd.read_csv(S.OUT / 'primary' / 'team_games.csv.gz'); t['day'] = t['day'].astype(str)
    key = ['season', 'day', 'game_id', 'side']
    own_old = t[(t.rule == 'old') & (t.portfolio == 'own')].set_index(key)
    cand = t[(t.rule == 'old') & (t.portfolio == 'actual') & (t.verdict_B == 'reversal') & ~t.holds_pooled_pick
             & (t.holds_opponent_pick | t.holds_conditional_other)].copy()
    cand = cand[[own_old.loc[tuple(r[k] for k in key)].verdict_B != 'reversal' for _, r in cand.iterrows()]]
    rows = []
    for _, r in cand.iterrows():
        year = int(r.season[:4]) + 1
        led = json.loads((HERE / 'ledgers' / f'ledger_{year}_draft.json').read_text(encoding='utf-8'))
        fp = ledger_footprint(led, r.team, r.opp)
        if len(fp) > 3 or any(e['rule']['type'] == 'pool' or e['confidence'] != 'high' for e in fp):
            continue
        rows.append((abs(r.tau_linear), r, fp, led))
    rows.sort(key=lambda x: -x[0])
    picked, seasons = [], set()
    for _, r, fp, led in rows:
        if r.season in seasons:
            continue
        seasons.add(r.season); picked.append((r, fp, led))
        if len(picked) == n_candidates:
            break
    out = []
    for r, fp, led in picked:
        d = S.load_day(S.SIMULATIONS / 'primary' / r.season / f'exposures_{r.day}.npz'); meta = d['meta']
        g = meta['focal_game_ids'].index(str(r.game_id)) if str(r.game_id) in meta['focal_game_ids'] else meta['focal_game_ids'].index(r.game_id)
        h, a = meta['focal_teams'][g]; side = int(r.side == 'away') if isinstance(r.side, str) else int(r.side)
        c = (h, a)[side]; sgn = 1.0 if side == 0 else -1.0
        ranks, _ = S.cutoff_ranks(meta)
        rec = dict(season=r.season, date=r.day, game_id=str(r.game_id), team=r.team, opponent=r.opp,
                   home=TEAMS[h], away=TEAMS[a], team_rank=int(ranks[c]), opponent_rank=int(ranks[(h, a)[1 - side]]),
                   ledger=[dict(e, source_urls=[s['url'] for s in led['sources'] if s['id'] in e['sources']]) for e in fp])
        for ri, rule in enumerate(S.RULES):
            for pf, src in (('actual', d['DB']), ('own', d['DB_own'])):
                db = sgn * src[:, g, ri, c, :]; Cb = np.cumsum(db, axis=1)
                m, se, crit = S.band_stats(Cb); v, j = S.verdict(m, se, crit['B'], 30); up = m + crit['B'] * se
                k = f'{rule}_{pf}'
                rec[f'verdict_{k}'] = v; rec[f'jstar_{k}'] = j; rec[f'min_upper_band_{k}'] = float(up.min())
                rec[f'tau_linear_{k}'] = float((db @ CURVES['linear']).mean()); rec[f'M_{k}'] = float(m[29])
                rec[f'C_{k}'] = {str(s): float(m[s - 1]) for s in SLOTS_SHOWN}
        out.append(rec)
    return out, len(cand)


# ---------------------------------------------------------------- checks against the registered tables
def checks(tg, games, heads, h2rows, n_files):
    def rd(p):
        with open(p, newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    reg = {r['portfolio']: float(r['diff']) for r in rd(S.OUT / 'primary' / 'T5_headline_reversal_diff.csv')
           if r['contrast'] == 'new_minus_old' and r['verdict'] == 'verdict_B'}
    h2 = [r for r in rd(S.OUT / 'primary' / 'H2.csv') if r['curve'] == 'linear' and r['sample'] == 'registered'][0]
    r16 = {(r['portfolio'], r['verdicts']): r for r in rd(S.OUT / 'exploratory_4' / 'R16_rollover_dominance.csv')}
    ours = {(h['rho'], h['portfolio']): h['diff'] for h in heads}
    c = []
    add = lambda name, got, want, tol: c.append(dict(check=name, got=got, want=want, ok=bool(abs(got - want) <= tol)))
    add('day files', n_files, 312, 0)
    add('team-game rows per rule and portfolio', sum(1 for r in tg if r['rule'] == 'new' and r['portfolio'] == 'actual'), 4896, 0)
    for pf, q in (('actual', '(H-a)'), ('own', '(H-b)')):
        add(f'{q} at rho = 0 equals the registered headline', ours[(0.0, pf)], reg[pf], 1e-12)
        for rho in S.RHOS:
            add(f'{q} at rho = {rho} equals R16', ours[(rho, pf)],
                float(r16[(pf, f'verdict_B_rho{int(100 * rho)}')]['diff_new_minus_old']), 1e-12)
    h0 = [r for r in h2rows if r['a'] == 0.0][0]
    add('H2 (a = 0) equals the registered H2', h0['h2_mean_diff_new_minus_old'], float(h2['mean_diff_new_minus_old']), 1e-12)
    add('H2 sample size', h0['n_games'], int(h2['n_games']), 0)
    own_m = max(abs(r['M']) for r in tg if r['portfolio'] == 'own')
    add('own-pick M = 0 (max |M|)', own_m, 0.0, 1e-6)
    own_changed = sum(1 for r in tg if r['portfolio'] == 'own' and any(r[f] != r['verdict_B'] for _, f in VFIELDS[1:]))
    add('own-pick verdicts identical under every rho', own_changed, 0, 0)
    stk = [r for r in rd(S.OUT / 'primary' / 'T5_5_stakes_distribution.csv')
           if r['rule'] == 'new' and r['curve'] == 'linear' and r['measure'] == 'tp_share']
    if stk:
        med = float(np.median([x[f'tp_{dkey(S.DELTA)}'] for x in games if x['rule'] == 'new' and x['curve'] == 'linear'
                               and x['portfolio'] == 'actual' and x[f'tp_{dkey(S.DELTA)}'] == x[f'tp_{dkey(S.DELTA)}']]))
        add('median TP, 3-2-1, linear, actual, equals T5_5', med, float(stk[0]['median']), 1e-9)
    return c


# ---------------------------------------------------------------- writing
def write_csv(name, rows):
    OUT.mkdir(parents=True, exist_ok=True)
    keys = list(dict.fromkeys(k for r in rows for k in r))
    with open(OUT / f'{name}.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=keys, lineterminator='\n'); w.writeheader(); w.writerows(rows)


def num(x, d=3, sign=False, scale=1.0):
    if x != x:
        return '—'
    v = x * scale
    s = f'{v:+.{d}f}' if sign else f'{v:.{d}f}'
    return s.replace('-', '−')


def ci(pt, lo, hi, d=3, sign=False, scale=1.0):
    return f'{num(pt, d, sign, scale)} [{num(lo, d, sign, scale)}, {num(hi, d, sign, scale)}]'


def _pct(cell):
    """Escape a bare percent sign (a LaTeX comment character); an escaped one is kept."""
    return re.sub(r'(?<!\\)%', r'\\%', cell)


def write_tex(name, header, rows, cols):
    TAB.mkdir(parents=True, exist_ok=True)
    body = ['% generated from the data; do not edit by hand', '\\begin{adjustbox}{max width=\\textwidth}',
            f'\\begin{{tabular}}{{{cols}}}', '\\toprule', ' & '.join(map(_pct, header)) + ' \\\\', '\\midrule']
    body += [' & '.join(map(_pct, r)) + ' \\\\' for r in rows]
    body += ['\\bottomrule', '\\end{tabular}', '\\end{adjustbox}', '']
    (TAB / f'{name}.tex').write_bytes('\n'.join(body).encode('utf-8'))


def tex_tables(m1, r1, s1, h1, sh2, hd2, tr2, st3, pr3, a4, cd4):
    look = lambda rows, **kw: next(r for r in rows if all(r[k] == v for k, v in kw.items()))
    # 1: mean tau_a on the linear curve by band, actual portfolio
    rows = []
    for rule, rn in (('old', 'old rule'), ('new', '3-2-1')):
        for band in BANDS:
            rows.append([rn, band.replace('-', '–')] + [ci(*[look(m1, portfolio='actual', curve='linear', a=a_, rule=rule, band=band)[k]
                                          for k in ('mean', 'lo99', 'hi99')], d=4, sign=True)
                                      for a_ in (0.0,) + A_VALUES])
    write_tex('tab_e5_1_tau_a', ['rule', 'ranks', '$a=0$', '$a=0.1$', '$a=0.25$', '$a=0.5$'], rows, 'llrrrr')
    rows = []
    for cv in CURVES:
        for pf in S.PORTFOLIOS:
            rows.append([cv, pf] + [ci(*[look(r1, portfolio=pf, curve=cv, a=a_)[k]
                                         for k in ('ratio_new_over_old_4_10', 'lo99', 'hi99')], d=2)
                                    for a_ in (0.0,) + A_VALUES])
    write_tex('tab_e5_1b_ratio_4_10', ['curve', 'portfolio', '$a=0$', '$a=0.1$', '$a=0.25$', '$a=0.5$'], rows, 'llrrrr')
    rows = []
    for a_ in A_VALUES:
        for rule, rn in (('old', 'old rule'), ('new', '3-2-1')):
            x = look(s1, portfolio='actual', curve='linear', a=a_, rule=rule)
            rows.append([f'{a_:g}', rn, num(100 * x['share_sign_differs'], 1), num(100 * x['share_sign_differs_both_above_delta'], 1),
                         num(100 * x['share_sig_positive'], 1), num(100 * x['share_sig_negative'], 1)])
    write_tex('tab_e5_1c_signs', ['$a$', 'rule', 'sign differs (%)', 'differs, both $|τ| > δ$ (%)',
                                  'significantly $> 0$ (%)', 'significantly $< 0$ (%)'], rows, 'llrrrr')
    rows = [[f'{x["a"]:g}', f'{x["n_games"]:,}', ci(x['h2_mean_diff_new_minus_old'], x['lo99'], x['hi99'], d=2,
                                                     sign=True, scale=1e4)] for x in h1]
    write_tex('tab_e5_1d_h2', ['$a$', 'H2 games', 'H2 (×0.0001)'], rows, 'lrr')
    # 2: verdict shares and headlines under rho
    rows = []
    for rho in (0.0,) + S.RHOS:
        for pf in S.PORTFOLIOS:
            for rule, rn in (('old', 'old rule'), ('new', '3-2-1')):
                cells = [ci(*[100 * look(sh2, rho=rho, portfolio=pf, rule=rule, verdict=v)[k] for k in ('share', 'lo99', 'hi99')], d=1)
                         for v in S.VERDICTS]
                rows.append([f'{rho:g}', pf, rn] + cells)
    write_tex('tab_e5_2_rollover_verdicts', ['$ρ$', 'portfolio', 'rule', 'dominance-positive', 'reversal',
                                             'negligible', 'unresolved'], rows, 'lllrrrr')
    rows = [[f'{h["rho"]:g}', h['quantity'], num(100 * h['share_new'], 1), num(100 * h['share_old'], 1),
             ci(100 * h['diff'], 100 * h['lo99'], 100 * h['hi99'], d=1, sign=True)] for h in hd2]
    write_tex('tab_e5_2b_rollover_headlines', ['$ρ$', 'quantity', '3-2-1 (%)', 'old (%)', 'difference (pts)'], rows, 'llrrr')
    # 3: network, linear curve
    rows = []
    for rule, rn in (('old', 'old rule'), ('new', '3-2-1')):
        for pf in S.PORTFOLIOS:
            x = look(st3, rule=rule, curve='linear', portfolio=pf, delta=S.DELTA)
            rows.append([rn, pf, ci(x['tp_median'], x['tp_median_lo99'], x['tp_median_hi99']),
                         ci(100 * x['tp_dominated_share'], 100 * x['tp_dominated_lo99'], 100 * x['tp_dominated_hi99'], d=1),
                         f'{x["tp_defined"]:,}', ci(x['mean_abs_third_all'], x['mean_abs_third_all_lo99'], x['mean_abs_third_all_hi99'], d=2, scale=1e3),
                         ci(x['mean_abs_third_h2'], x['mean_abs_third_h2_lo99'], x['mean_abs_third_h2_hi99'], d=2, scale=1e3)])
    write_tex('tab_e5_3_network', ['rule', 'portfolio', 'median TP', 'TP-dominated (%)', 'TP defined',
                                   'mean $|s|$, third (×0.001)', 'same, H2 games (×0.001)'], rows, 'llrrrrr')
    rows = [[x['curve'], x['measure'].replace('_', ' '), x['contrast'].replace(' - ', ' − ').replace('(actual - own)', '(actual − own)'), f'{x["n_games"]:,}',
             ci(x['diff'], x['lo99'], x['hi99'], d=4, sign=True)] for x in pr3 if x['curve'] == 'linear']
    write_tex('tab_e5_3b_network_pairs', ['curve', 'measure', 'contrast', 'games', 'difference'], rows, 'lllrr')
    rows = []
    for dl in (0.001, 0.005):
        for rule, rn in (('old', 'old rule'), ('new', '3-2-1')):
            for pf in S.PORTFOLIOS:
                x = look(st3, rule=rule, curve='linear', portfolio=pf, delta=dl)
                rows.append([f'{dl:g}', rn, pf, ci(x['tp_median'], x['tp_median_lo99'], x['tp_median_hi99']),
                             ci(100 * x['tp_dominated_share'], 100 * x['tp_dominated_lo99'], 100 * x['tp_dominated_hi99'], d=1)])
    write_tex('tab_e5_3c_delta', ['$δ$', 'rule', 'portfolio', 'median TP', 'TP-dominated (%)'], rows, 'lllrr')
    # 4 (a)
    rows = []
    for x in a4:
        rows.append([x['reading'], x['bootstrap'], str(x['team_games']),
                     ci(100 * x['reversal_share_with'], 100 * x['reversal_share_with_lo99'], 100 * x['reversal_share_with_hi99'], d=1),
                     num(100 * x['reversal_share_without'], 1),
                     ci(100 * x['reversal_share_change'], 100 * x['reversal_share_change_lo99'], 100 * x['reversal_share_change_hi99'], d=1, sign=True),
                     ci(x['mean_tau_linear_change'], x['mean_tau_linear_change_lo99'], x['mean_tau_linear_change_hi99'], d=4, sign=True)])
    write_tex('tab_e5_4a_h3_affected', ['ban reading', 'bootstrap', 'team-games', 'reversal share with ban (%)',
                                        'without (%)', 'change (pts)', 'change in mean $τ$'], rows, 'lllrrrr')


def tex_4b(b4):
    """Table 5.6, Panels A-C, with the two-level intervals (as printed) beside the day-clustered ones."""
    look = lambda **kw: next(r for r in b4 if all(str(r.get(k)) == str(v) for k, v in kw.items()))
    cfg = (('1: old rule', '0', 'A'), ('2: + field and balls', 'F', 'A'), ('3: + floor', 'FL', 'A'),
           ('4: + restrictions (3-2-1)', 'FLR', 'A'), ('5: + protection ban, reading A', 'FLRP', 'A'),
           ('6: + protection ban, reading B', 'FLRP', 'B'))
    fmt = {'Y1_reversal_share': dict(d=1, scale=100), 'Y2_mean_tau_linear': dict(d=4, sign=True),
           'Y3_mean_tp_share': dict(d=3)}
    rows = []
    for lab, sub, var in cfg:
        cells = []
        for out, f in fmt.items():
            for b in ('two-level', 'day-clustered'):
                x = look(table='C3_1_outcomes', bootstrap=b, variant=var, outcome=out, subset=sub)
                cells.append(ci(float(x['value']), float(x['lo99']), float(x['hi99']), **f))
        rows.append([lab] + cells)
    write_tex('tab_e5_4b_panel_a', ['configuration', 'Y1, two-level', 'Y1, day-clustered', 'Y2, two-level',
                                    'Y2, day-clustered', 'Y3, two-level', 'Y3, day-clustered'], rows, 'lrrrrrr')
    rows = []
    for comp, name in (('F', 'field and balls (F)'), ('L', 'floor (L)'), ('R', 'repeat restrictions (R)'),
                       ('P', 'protection ban (P)')):
        cells = []
        for out, f in (('Y1_reversal_share', dict(d=2, sign=True, scale=100)), ('Y2_mean_tau_linear', dict(d=4, sign=True))):
            for b in ('two-level', 'day-clustered'):
                x = look(table='C3_3_shapley', bootstrap=b, variant='A', outcome=out, component=comp)
                cells.append(ci(float(x['value_FbeforeR']), float(x['lo99']), float(x['hi99']), **f))
        rows.append([name] + cells)
    write_tex('tab_e5_4b_panel_b', ['component', 'Y1 (pts), two-level', 'Y1 (pts), day-clustered',
                                    'Y2, two-level', 'Y2, day-clustered'], rows, 'lrrrr')
    rows = []
    for var, name in (('A', 'A: top-11'), ('B', 'B: top-16')):
        cells = []
        for b in ('two-level', 'day-clustered'):
            x = look(table='C3_4_H3', bootstrap=b, variant=var)
            cells += [ci(float(x['share_config5']), float(x['lo99']), float(x['hi99']), d=1, scale=100),
                      ci(float(x['change']), float(x['change_lo99']), float(x['change_hi99']), d=1, sign=True, scale=100)]
        rows.append([name, str(look(table='C3_4_H3', bootstrap='two-level', variant=var)['n_team_games'])] + cells)
    write_tex('tab_e5_4b_panel_c', ['ban reading', 'team-games', 'with ban, two-level', 'change (pts), two-level',
                                    'with ban, day-clustered', 'change (pts), day-clustered'], rows, 'lrrrrr')


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--workers', type=int, default=20)
    ap.add_argument('--part', choices=('all', 'examples'), default='all')
    a = ap.parse_args(argv)
    t0 = time.time()
    ex, n_cand = examples()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'E5_4e_examples.json').write_text(json.dumps({'rule': 'old rule, actual portfolio, class-B reversal; '
        'own-pick verdict not a reversal; the team holds the opponent\'s pick (S3) or another pick conditionally '
        '(S2); no pooled right; at most three ledger entries matter, all of high confidence; largest |linear tau| first; one per season',
        'candidates_meeting_the_first_three_conditions': n_cand, 'examples': ex}, indent=1, ensure_ascii=False) + '\n',
        encoding='utf-8')
    if a.part == 'examples':
        print(json.dumps({'examples': [(e['date'], e['team'], e['opponent']) for e in ex], 'candidates': n_cand}))
        return
    tg, games, n_files = collect(a.workers)
    t_pass = time.time() - t0
    boot = boot_of(tg)
    m1, r1, s1, h1 = item1(tg, games, boot)
    sh2, hd2, tr2 = item2(tg, boot)
    chk = checks(tg, games, hd2, h1, n_files)
    if not all(c['ok'] for c in chk):
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / 'E5_checks_FAILED.json').write_text(json.dumps(chk, indent=1), encoding='utf-8')
        raise SystemExit(f'a check against the registered tables failed: {[c for c in chk if not c["ok"]]}')
    st3, pr3 = item3(games, boot)
    a4, b4 = item4_c3()
    cd4 = item4_cd(tg, boot)
    for name, rows in (('E5_1_tau_a_mean', m1), ('E5_1_ratio_4_10', r1), ('E5_1_signs', s1), ('E5_1_h2', h1),
                       ('E5_2_rollover_verdicts', sh2), ('E5_2_rollover_headlines', hd2), ('E5_2_transitions', tr2),
                       ('E5_3_network', st3), ('E5_3_network_pairs', pr3), ('E5_4a_h3_affected', a4),
                       ('E5_4b_table_5_6_bootstraps', b4), ('E5_4cd_argmin_h1', cd4)):
        write_csv(name, rows)
    tex_tables(m1, r1, s1, h1, sh2, hd2, tr2, st3, pr3, a4, cd4)
    tex_4b(b4)
    commit = subprocess.run(['git', '-C', str(S.ROOT), 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    (OUT / 'E5_checks.json').write_text(json.dumps({'code_commit': commit, 'checks': chk,
                                                    'day_pass_seconds': round(t_pass, 1), 'workers': a.workers,
                                                    'total_seconds': round(time.time() - t0, 1)}, indent=1) + '\n',
                                        encoding='utf-8')
    print(json.dumps({'checks_ok': True, 'day_pass_seconds': round(t_pass, 1), 'total_seconds': round(time.time() - t0, 1)}))


if __name__ == '__main__':
    main()

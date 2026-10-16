"""Exploratory analyses, seventh set (Online Appendix H.23, H.32 and H.35).

None of these is registered. They were computed after the results were opened, from the stored primary run,
without any new simulation, and none changes a registered table or headline quantity.

  margin   H.32: the primary run re-read at equivalence margins delta = 0.001 and 0.005 (registered: 0.003).
           Needs the simulation day files (simulations/primary). Writes results/exploratory_7/margin_<delta>/.
  blocks   H.32: the two-level bootstrap with weeks or two-week blocks in place of days as the within-season
           unit; headline differences (H-a), (H-b) and H1. Team-game table only.
  positive H.35: the positive part of the estimated linear-curve incentive, max(tau_hat, 0): mean, 90th
           percentile and the share with tau_hat > delta, by portfolio, rule and rank band, with the paired
           change in the same team-games (two-level bootstrap); the share whose lower 99% limit exceeds delta;
           and the normal-approximation plug-in bias of the mean positive part. Team-game table only.
  lastpick H.23: a positive value a for the last pick, v_a(k) = a + (1 - a) v(k), for a up to 0.8: linear-curve
           signs, rank-band means and the stake results. Needs the simulation day files.

Usage: python exploratory_7.py {margin|blocks|positive|lastpick|all}
Outputs: results/exploratory_7/
"""
import csv
import shutil
import sys
import tempfile
from collections import defaultdict
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / 'ledgers'))

import analysis as S  # noqa: E402
import exploratory_1 as P  # noqa: E402
import robustness_headlines as R  # noqa: E402
from value import CURVES  # noqa: E402

OUT = S.OUT / 'exploratory_7'
DELTA = 0.003
Z3 = 2.935199
BANDS = (('all', 1, 30), ('1-3', 1, 3), ('4-10', 4, 10), ('11-16', 11, 16), ('17-30', 17, 30))
A_ALL = (0.0, 0.05, 0.10, 0.20, 0.40, 0.60, 0.80)
MARGIN_FILES = ('H1.csv', 'H2.csv', 'T5_1_verdicts.csv', 'T5_4_typology.csv', 'T5_headline_reversal_diff.csv')


def write(name, rows):
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / f'{name}.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)


# ---------------------------------------------------------------- margin (needs the day files)
def margin():
    for d in (0.001, 0.005):
        S.DELTA = d
        with tempfile.TemporaryDirectory() as tmp:
            S.run('primary', out=Path(tmp))
            dst = OUT / f'margin_{d}'
            dst.mkdir(parents=True, exist_ok=True)
            for f in MARGIN_FILES:
                shutil.copy2(Path(tmp) / f, dst / f)
    S.DELTA = DELTA


# ---------------------------------------------------------------- blocks
class BlockBoot(S.Boot):
    """Two-level bootstrap with blocks of `block_days` consecutive calendar days (counted from each season's
    first window day) in place of single days as the within-season unit."""

    def __init__(self, day_keys, seasons, block_days=7, reps=S.BOOT_REPS, seed=S.BOOT_SEED):
        self.days = list(day_keys); self.idx = {k: i for i, k in enumerate(self.days)}
        rng = np.random.default_rng(seed); D = len(self.days)
        first = {}
        for s, d in self.days:
            dd = date.fromisoformat(d); first[s] = min(first.get(s, dd), dd)
        blocks = defaultdict(lambda: defaultdict(list))
        for i, (s, d) in enumerate(self.days):
            blocks[s][(date.fromisoformat(d) - first[s]).days // block_days].append(i)
        names = sorted(blocks)
        W = np.zeros((reps, D))
        pick = rng.integers(0, len(names), size=(reps, len(names)))
        for k, name in enumerate(names):
            bl = [np.array(v) for _, v in sorted(blocks[name].items())]; nb = len(bl)
            times = (pick == k).sum(1)
            for copy in range(len(names)):
                active = times > copy
                if not active.any():
                    break
                draw = rng.integers(0, nb, size=(reps, nb))
                for j in range(nb):
                    cnt = (draw == j).sum(1)
                    W[np.ix_(active, bl[j])] += cnt[active][:, None]
        self.W = W


def blocks():
    tg = P.load_tg('primary')
    days = sorted({(s, d) for s, d in zip(tg.season, tg.day)})
    seasons = [s for s, _ in days]
    out = []
    for label, boot in (('days (registered)', S.Boot(days, seasons)), ('weeks', BlockBoot(days, seasons, 7)),
                        ('two-week blocks', BlockBoot(days, seasons, 14))):
        P.boot_for = lambda t, b=boot: b
        rows = tg.to_dict('records')
        rec = {'resampling_unit': label}
        for pf, key in (('actual', 'H_a'), ('own', 'H_b')):
            rev = lambda x: x['verdict_B'] == 'reversal'
            n1, d1 = S.per_day(rows, boot, rev, lambda x, pf=pf: x['rule'] == 'new' and x['portfolio'] == pf)
            n2, d2 = S.per_day(rows, boot, rev, lambda x, pf=pf: x['rule'] == 'old' and x['portfolio'] == pf)
            pt, lo, hi = boot.diff_of_ratios(n1, d1, n2, d2)
            rec.update({key: float(pt), f'{key}_lo99': float(lo), f'{key}_hi99': float(hi)})
        h = R.h1(tg[tg.rule.isin(['old', 'new'])])
        rec.update(H1_diff=h['h1_diff'], H1_lo99=h['h1_lo99'], H1_hi99=h['h1_hi99'])
        out.append(rec)
    write('E7_2_block_bootstrap', out)


# ---------------------------------------------------------------- positive part
def positive():
    from scipy.stats import norm
    tg = P.load_tg('primary')
    boot = P.boot_for(tg); D = len(boot.days)
    a = tg[tg.portfolio.isin(['actual', 'own']) & tg.rule.isin(['old', 'new'])]
    key = ['season', 'day', 'game_id', 'team', 'portfolio']
    w = a.pivot_table(index=key, columns='rule', values='tau_linear', aggfunc='first').reset_index()
    w = w.merge(a[a.rule == 'old'][key + ['rank']], on=key)
    w['D'] = w['new'].clip(lower=0) - w['old'].clip(lower=0)
    w['E'] = (w['new'] > DELTA).astype(float) - (w['old'] > DELTA).astype(float)
    out = []
    for pf in ('own', 'actual'):
        for band, lo_r, hi_r in BANDS:
            rec = {'portfolio': pf, 'rank_band': band}
            for rule in ('old', 'new'):
                s = a[(a.portfolio == pf) & (a.rule == rule) & a['rank'].between(lo_r, hi_r)]
                num = np.zeros(D); den = np.zeros(D)
                for (se, d), g in s.groupby(['season', 'day']):
                    i = boot.idx[(se, d)]; num[i] = g.tau_linear.clip(lower=0).sum(); den[i] = len(g)
                pt, lo, hi = boot.ratio(num, den)
                pos = s.tau_linear.clip(lower=0)
                rec.update({'team_games': len(s), f'{rule}_mean_pos': float(pt[0]), f'{rule}_mean_pos_lo99': float(lo[0]),
                            f'{rule}_mean_pos_hi99': float(hi[0]), f'{rule}_p90': float(np.quantile(pos, 0.9)),
                            f'{rule}_share_above_delta': float((s.tau_linear > DELTA).mean())})
            s = w[(w.portfolio == pf) & w['rank'].between(lo_r, hi_r)]
            for col, name in (('D', 'paired_change_mean_pos'), ('E', 'paired_change_share')):
                num = np.zeros(D); den = np.zeros(D)
                for (se, d), g in s.groupby(['season', 'day']):
                    i = boot.idx[(se, d)]; num[i] = g[col].sum(); den[i] = len(g)
                pt, lo, hi = boot.ratio(num, den)
                rec.update({name: float(pt[0]), f'{name}_lo99': float(lo[0]), f'{name}_hi99': float(hi[0])})
            out.append(rec)
    write('E7_3_positive_part', out)
    diag = []
    for rule in ('old', 'new'):
        g = a[(a.portfolio == 'actual') & (a.rule == rule)]
        t, se = g.tau_linear.values, g.se_linear.values
        z = np.where(se > 0, t / np.where(se > 0, se, 1), 0)
        b = np.where(se > 0, se * norm.pdf(z) + t * norm.cdf(z) - np.maximum(t, 0), 0)
        diag.append({'portfolio': 'actual', 'rule': rule, 'team_games': len(g),
                     'share_lower_limit_above_delta': float(((t - Z3 * se) > DELTA).mean()),
                     'mean_plugin_bias': float(b.mean()), 'max_plugin_bias': float(b.max()),
                     'share_zero_se': float((se == 0).mean()), 'median_se': float(np.median(se)),
                     'p90_se': float(np.quantile(se, 0.9)),
                     'mean_pos_given_positive': float(t[t > 0].mean())})
    write('E7_3_positive_part_diagnostics', diag)


# ---------------------------------------------------------------- last pick (needs the day files)
def lastpick():
    v = np.asarray(CURVES['linear'], float)
    tg, games = [], []
    for f in sorted((S.SIMULATIONS / 'primary').glob('*/exposures_*.npz')):
        d = S.load_day(f); meta = d['meta']
        season, day = meta['season'], meta['day']
        year = int(season[:4]) + 1
        ranks, _ = S.cutoff_ranks(meta)
        cl, _ = S.claims(year)
        for g, (h, aw) in enumerate(meta['focal_teams']):
            for side, c in ((0, h), (1, aw)):
                sgn = 1.0 if side == 0 else -1.0
                for pf, src in (('actual', d['DB']), ('own', d['DB_own'])):
                    for ri, r in enumerate(S.RULES):
                        db = sgn * src[:, g, ri, c, :]
                        t = db @ v; Mb = db.sum(1)
                        row = dict(rank=int(ranks[c]), band=S.band_of(int(ranks[c])), rule=r, portfolio=pf)
                        for a_ in A_ALL:
                            ta = (1 - a_) * t + a_ * Mb
                            m, se = float(ta.mean()), float(ta.std(ddof=1) / np.sqrt(len(ta)))
                            row[f'tau_{a_:.2f}'] = m; row[f'sign_{a_:.2f}'] = S.curve_sign(m, se)
                        tg.append(row)
            third = [x for x in range(30) if x not in (h, aw)]
            h2 = S.third_party_claim(year, h, aw, cl)
            for ri, r in enumerate(S.RULES):
                DBg = d['DB'][:, g, ri]
                s = -(DBg @ v).mean(0); m = -(DBg.sum(-1)).mean(0)
                row = dict(season=season, day=day, game=int(g), rule=r, h2=h2)
                for a_ in A_ALL:
                    sa = (1 - a_) * s + a_ * m
                    mat = np.abs(sa) >= DELTA
                    tot = float(np.abs(sa[mat]).sum())
                    tp_m = [x for x in third if mat[x]]
                    row[f'tp_{a_:.2f}'] = float(np.abs(sa[tp_m]).sum() / tot) if tot >= DELTA else float('nan')
                    row[f'mat_{a_:.2f}'] = float(np.abs(sa[tp_m]).sum() / len(third))
                games.append(row)
    out = []
    for pf in ('actual', 'own'):
        for r in S.RULES:
            sub = [x for x in tg if x['portfolio'] == pf and x['rule'] == r]
            rec = dict(portfolio=pf, rule=r, n=len(sub))
            for a_ in A_ALL:
                k = f'{a_:.2f}'
                rec[f'lose_{k}'] = sum(x[f'sign_{k}'] == 'lose' for x in sub)
                rec[f'win_{k}'] = sum(x[f'sign_{k}'] == 'win' for x in sub)
                rec[f'class_changed_{k}'] = sum(x[f'sign_{k}'] != x['sign_0.00'] for x in sub)
                rec[f'point_flipped_{k}'] = sum((x['tau_0.00'] > 0) != (x[f'tau_{k}'] > 0) for x in sub if x['tau_0.00'] != 0)
            out.append(rec)
    write('E7_4_lastpick_signs', out)
    out = []
    for pf in ('actual', 'own'):
        for b in ('1-3', '4-10', '11-16', '17-30'):
            for r in S.RULES:
                sub = [x for x in tg if x['portfolio'] == pf and x['rule'] == r and x['band'] == b]
                rec = dict(portfolio=pf, band=b, rule=r, n=len(sub))
                for a_ in A_ALL:
                    rec[f'mean_{a_:.2f}'] = float(np.mean([x[f'tau_{a_:.2f}'] for x in sub]))
                out.append(rec)
    write('E7_4_lastpick_rank_means', out)
    days = sorted({(x['season'], x['day']) for x in games})
    boot = S.Boot(days, [s_ for s_, _ in days]); idx = {dd: i for i, dd in enumerate(days)}
    by = {(x['season'], x['day'], x['game'], x['rule']): x for x in games}
    out = []
    for a_ in A_ALL:
        k = f'{a_:.2f}'
        rec = dict(a=a_)
        for r in S.RULES:
            sub = [x for x in games if x['rule'] == r and not np.isnan(x[f'tp_{k}'])]
            rec[f'{r}_tp_defined'] = len(sub)
            rec[f'{r}_tp_dominated_share'] = float(np.mean([x[f'tp_{k}'] > 0.5 for x in sub]))
            rec[f'{r}_mean_abs_third'] = float(np.mean([x[f'mat_{k}'] for x in games if x['rule'] == r]))
        num = np.zeros(len(days)); den = np.zeros(len(days))
        for (s_, dd, g, r), x in by.items():
            if r == 'old' and x['h2']:
                i = idx[(s_, dd)]; num[i] += by[(s_, dd, g, 'new')][f'mat_{k}'] - x[f'mat_{k}']; den[i] += 1
        pt, lo, hi = boot.ratio(num[:, None], den[:, None])
        rec.update(h2_games=int(den.sum()), h2_diff=float(pt[0]), h2_lo99=float(lo[0]), h2_hi99=float(hi[0]))
        out.append(rec)
    write('E7_4_lastpick_stakes', out)


if __name__ == '__main__':
    part = sys.argv[1] if len(sys.argv) > 1 else 'all'
    steps = {'margin': margin, 'blocks': blocks, 'positive': positive, 'lastpick': lastpick}
    for name in (steps if part == 'all' else [part]):
        steps[name]()
    print('wrote', OUT)

"""Registered analysis of the C3 component run (C3 registration, sections 4 and 5).

Reads simulations/c3/<season>/exposures_<day>.npz and produces, for each of the 16
subsets of {F, L, R, P} and each ban variant:
  Y1 share of class-B reversals, Y2 mean linear-curve tau, Y3 mean third-party share,
  the chain increments along old -> +F -> +L -> +R -> +P, the Shapley value of each component, and H3.
Verdicts, bands, the equivalence margin and the day-clustered bootstrap are imported from the primary
analysis module, so both runs use one definition of everything.
Usage: python c3_analysis.py [--out DIR] [--exclude-imprecise]
"""
import argparse
import csv
import json
import math
import sys
from collections import defaultdict
from itertools import combinations, permutations
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
for p in (HERE, HERE / 'ledgers'):
    sys.path.insert(0, str(p))

import analysis as A  # noqa: E402
from teams import TEAMS  # noqa: E402
from value import CURVES  # noqa: E402

COMPONENTS = ('F', 'L', 'R', 'P')
VARIANTS = ('A', 'B')
CHAIN = ('', 'F', 'FL', 'FLR', 'FLRP')
OUTCOMES = ('Y1_reversal_share', 'Y2_mean_tau_linear', 'Y3_mean_tp_share')
SIM_C3 = A.SIMULATIONS / 'c3'


def subset_key(s):
    return ''.join(c for c in COMPONENTS if c in s)


def load_day(path):
    z = np.load(path)
    meta = json.loads(bytes(z['meta']).decode())
    return z['DOWN'].astype(float), z['STK'].astype(float), meta


def analyse_day(DOWN, STK, meta, ranks=None):
    """Per team-game and per game rows, one per configuration."""
    season, day = meta['season'], meta['day']
    year = int(season[:4]) + 1
    restricted = set(meta.get('min_pick_new', {}))
    if ranks is None:
        ranks, _ = A.cutoff_ranks(meta)
    curves = meta['curves']; ci_lin = curves.index('linear')
    configs, subsets = meta['configs'], meta['subsets']
    tg, games = [], []
    for g, (h, a) in enumerate(meta['focal_teams']):
        for side, (c, o) in enumerate(((h, a), (a, h))):
            feat = A.features(year, c, o, restricted)
            for ci, name in enumerate(configs):
                Cb = np.cumsum(DOWN[:, g, ci, side, :], axis=1)
                m, se, crit = A.band_stats(Cb)
                v, j = A.verdict(m, se, crit['B'], 30)
                t = DOWN[:, g, ci, side, :] @ CURVES['linear']
                tg.append(dict(season=season, day=day, game=meta['focal_game_ids'][g], side=side,
                               team=TEAMS[c], config=name, subset=subset_key(subsets[ci]),
                               variant=name.rsplit('_', 1)[1], rank=int(ranks[c]),
                               band=A.band_of(int(ranks[c])), verdict_B=v, jstar_B=j,
                               tau_linear=float(t.mean()), **feat))
        for ci, name in enumerate(configs):
            s = STK[:, g, ci, ci_lin, :].mean(axis=0)
            tot = float(np.abs(s).sum())
            third = [t for t in range(30) if t not in (h, a)]
            tp = float(np.abs(s[third]).sum() / tot) if tot >= A.DELTA else float('nan')
            games.append(dict(season=season, day=day, game=meta['focal_game_ids'][g], config=name,
                              subset=subset_key(meta['subsets'][ci]), variant=name.rsplit('_', 1)[1],
                              tp_share=tp, total_abs_stake=tot))
    diag = {'season': season, 'day': day, 'precision_met': bool(meta['precision_met']),
            'n_worlds': int(meta['n_worlds']), 'secs': meta.get('secs')}
    return tg, games, diag


def collect(root=SIM_C3, exclude_imprecise=False, ranks_fn=None):
    tg, games, diags = [], [], []
    for f in sorted(Path(root).glob('*/exposures_*.npz')):
        DOWN, STK, meta = load_day(f)
        if exclude_imprecise and not meta['precision_met']:
            continue
        a, b, d = analyse_day(DOWN, STK, meta, ranks_fn(meta) if ranks_fn else None)
        tg += a; games += b; diags.append(d)
    return tg, games, diags


# ---------------------------------------------------------------- outcomes with the day bootstrap
def _per_day(rows, boot, num_fn, den_fn=lambda r: 1.0):
    num = np.zeros(len(boot.days)); den = np.zeros(len(boot.days))
    for r in rows:
        i = boot.idx[(r['season'], r['day'])]
        w = den_fn(r)
        if not w:
            continue
        den[i] += w; num[i] += num_fn(r)
    return num, den


def common_tp_games(games):
    """Games whose third-party share is defined under every configuration (A1 amendment 9)."""
    by = defaultdict(list)
    for r in games:
        by[(r['season'], r['day'], r['game'])].append(r['tp_share'])
    return {k for k, v in by.items() if all(x == x for x in v)}


def outcome_arrays(tg, games, boot, variant, band=None):
    """Per subset: (numerator, denominator) day vectors for Y1, Y2 and Y3 under one ban variant."""
    common = common_tp_games(games)
    out = {}
    for sub in sorted({r['subset'] for r in tg}):
        if 'P' in sub:
            sel_tg = [r for r in tg if r['subset'] == sub and r['variant'] == variant]
            sel_g = [r for r in games if r['subset'] == sub and r['variant'] == variant]
        else:
            sel_tg = [r for r in tg if r['subset'] == sub and r['variant'] == 'base']
            sel_g = [r for r in games if r['subset'] == sub and r['variant'] == 'base']
        if band:
            sel_tg = [r for r in sel_tg if r['band'] == band]
        out[sub] = {
            'Y1_reversal_share': _per_day(sel_tg, boot, lambda r: r['verdict_B'] == 'reversal'),
            'Y2_mean_tau_linear': _per_day(sel_tg, boot, lambda r: r['tau_linear']),
            # A1 amendment 9: Y3 is averaged over the games where TP is defined in EVERY
            # configuration, so its increments compare levels rather than changing game sets.
            'Y3_mean_tp_share': _per_day([r for r in sel_g if (r['season'], r['day'], r['game']) in common],
                                         boot, lambda r: r['tp_share']),
        }
    return out


def ratio_reps(boot, num, den):
    """Point estimate and bootstrap replicates of sum(num)/sum(den)."""
    point = num.sum() / den.sum() if den.sum() else float('nan')
    with np.errstate(invalid='ignore', divide='ignore'):
        reps = (boot.W @ num) / (boot.W @ den)
    return point, reps


def ci(reps):
    a = (1 - A.BOOT_LEVEL) / 2
    return float(np.nanquantile(reps, a)), float(np.nanquantile(reps, 1 - a))


PRECEDENCE = (('F', 'R'),)      # A1 amendment 9: "R with F off" is an invented analogue, so the
                                # primary attribution only averages orderings in which F precedes R.


def shapley_constrained(values, precedence=PRECEDENCE):
    """Precedence-constrained (Faigle-Kern) value: average marginal contributions over the orderings that
    respect `precedence`. With F before R this drops the 12 orderings whose R-marginal is taken without the
    3-2-1 field. Efficiency still holds: the values sum to Y(full) - Y(empty)."""
    orders = [o for o in permutations(COMPONENTS)
              if all(o.index(a) < o.index(b) for a, b in precedence)]
    out = {k: 0.0 for k in COMPONENTS}
    for o in orders:
        prefix = ''
        for k in o:
            out[k] = out[k] + (values[subset_key(prefix + k)] - values[subset_key(prefix)]) / len(orders)
            prefix += k
    return out


def shapley(values):
    """values: subset key -> scalar (or vector of bootstrap replicates). Returns {component: value}."""
    n = len(COMPONENTS)
    fact = [math.factorial(i) for i in range(n + 1)]
    out = {}
    for k in COMPONENTS:
        rest = [c for c in COMPONENTS if c != k]
        tot = 0.0
        for size in range(n):
            for comb in combinations(rest, size):
                s = subset_key(''.join(comb))
                w = fact[size] * fact[n - size - 1] / fact[n]
                tot = tot + w * (values[subset_key(s + k)] - values[s])
        out[k] = tot
    return out


def tables(tg, games, boot, diags):
    T = {}
    T['C3_0_diagnostics'] = [{'states': len(diags), 'precision_met': sum(d['precision_met'] for d in diags),
                              'precision_missed': sum(not d['precision_met'] for d in diags),
                              'configs': len({r['config'] for r in tg}),
                              'subsets': len({r['subset'] for r in tg}),
                              'team_games_per_config': len(tg) // max(1, len({r['config'] for r in tg})),
                              'core_seconds': round(sum(d['secs'] or 0 for d in diags), 1)}]
    rows_y, rows_chain, rows_sh = [], [], []
    for variant in VARIANTS:
        for band in [None] + [b[2] for b in A.BANDS]:
            arr = outcome_arrays(tg, games, boot, variant, band)
            if band and not any(arr[s]['Y1_reversal_share'][1].sum() for s in arr):
                continue
            pts, reps = {}, {}
            for out in OUTCOMES:
                if band and out == 'Y3_mean_tp_share':
                    continue                                   # Y3 is a game-level measure, not banded
                pts[out], reps[out] = {}, {}
                for sub, d in arr.items():
                    num, den = d[out]
                    p, r = ratio_reps(boot, num, den)
                    pts[out][sub] = p; reps[out][sub] = r
                    lo, hi = ci(r)
                    rows_y.append(dict(variant=variant, band=band or 'all', outcome=out, subset=sub or '0',
                                       value=p, lo99=lo, hi99=hi, n_days=int((den > 0).sum()),
                                       n=int(den.sum())))
                for a_, b_ in zip(CHAIN[:-1], CHAIN[1:]):
                    d = pts[out][subset_key(b_)] - pts[out][subset_key(a_)]
                    r = reps[out][subset_key(b_)] - reps[out][subset_key(a_)]
                    lo, hi = ci(r)
                    rows_chain.append(dict(variant=variant, band=band or 'all', outcome=out,
                                           step=f'{a_ or "old"} -> {b_}', delta=d, lo99=lo, hi99=hi))
                phi = shapley(pts[out]); phi_r = shapley(reps[out])
                psi = shapley_constrained(pts[out]); psi_r = shapley_constrained(reps[out])
                for k in COMPONENTS:
                    lo, hi = ci(phi_r[k]); clo, chi = ci(psi_r[k])
                    rows_sh.append(dict(variant=variant, band=band or 'all', outcome=out, component=k,
                                        value_FbeforeR=psi[k], lo99=clo, hi99=chi,
                                        shapley_unconstrained=phi[k], unc_lo99=lo, unc_hi99=hi))
                rows_sh.append(dict(variant=variant, band=band or 'all', outcome=out, component='sum',
                                    value_FbeforeR=sum(psi.values()), lo99=float('nan'), hi99=float('nan'),
                                    shapley_unconstrained=sum(phi.values()),
                                    total_FLRP_minus_old=pts[out]['FLRP'] - pts[out]['']))
    T['C3_1_outcomes'] = rows_y
    T['C3_2_chain'] = rows_chain
    T['C3_3_shapley'] = rows_sh
    # H3: reversal share among team-games that hold another team's pick conditionally
    h3 = []
    for variant in VARIANTS:
        sel4 = [r for r in tg if r['subset'] == 'FLR' and r['variant'] == 'base' and r['holds_conditional_other']]
        sel5 = [r for r in tg if r['subset'] == 'FLRP' and r['variant'] == variant and r['holds_conditional_other']]
        n5, d5 = _per_day(sel5, boot, lambda r: r['verdict_B'] == 'reversal')
        n4, d4 = _per_day(sel4, boot, lambda r: r['verdict_B'] == 'reversal')
        p5, r5 = ratio_reps(boot, n5, d5); p4, r4 = ratio_reps(boot, n4, d4)
        lo5, hi5 = ci(r5); lod, hid = ci(r5 - r4)
        h3.append({'variant': variant, 'n_team_games': int(d5.sum()), 'share_config5': p5, 'lo99': lo5,
                   'hi99': hi5, 'share_config4': p4, 'change': p5 - p4, 'change_lo99': lod,
                   'change_hi99': hid,
                   # A1 amendment 9: (ii) is "the ban leaves some reversals, and fewer than without it":
                   # the STRICT inequality 0 < share(config 5) < share(config 4). The original C3 registration
                   # asked only that the change be smaller in absolute value than the config-4 share; with equal
                   # shares that wording would hold and this one does not (A1 amendment 15).
                   'supported': bool(lo5 > 0 and 0 < p5 < p4)})
    T['C3_4_H3'] = h3
    return T


def main(out=None, exclude_imprecise=False, root=SIM_C3, ranks_fn=None):
    tg, games, diags = collect(root, exclude_imprecise, ranks_fn)
    if not diags:
        raise SystemExit('no C3 output files found')
    days = sorted({(d['season'], d['day']) for d in diags})
    boot = A.Boot(days, [s for s, _ in days])
    T = tables(tg, games, boot, diags)
    out = Path(out) if out else A.OUT / 'c3'
    A.write_tables(T, out, f'C3 component decomposition; states={len(diags)}; '
                           f'exclude_imprecise={exclude_imprecise}')
    with open(out / 'c3_team_games.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(tg[0].keys())); w.writeheader(); w.writerows(tg)
    print(f'C3: {len(diags)} states, {len(tg)} team-game rows -> {out}')
    return T


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--out'); ap.add_argument('--exclude-imprecise', action='store_true')
    a = ap.parse_args()
    main(a.out, a.exclude_imprecise)

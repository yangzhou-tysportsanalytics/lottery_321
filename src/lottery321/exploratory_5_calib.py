"""Exploratory analyses, fifth set, parts 5 and 6: two new simulations
(exploratory, added after the results were opened; no registered quantity changes). Both reuse the registered pipeline unchanged
(day_run.run_day, simulate.save / rebatch, analysis.band_stats / verdict).

Part 5, pooled-rights convergence: every 12th primary game day from the first (26 days), rerun with 16 joint draft
orders per world and branch instead of 4; same seeds, same states, same stopping rule (looks 2,000 / 8,000 / 32,000).
The simulator draws lottery_draws x 16 uniforms per world from the same stream, so a different draw count shifts
every later draw: the two runs do not share common random numbers beyond the first world, and the comparison
carries the full Monte Carlo noise of both runs.

Part 6, calibration of the decision rule: every 26th primary game day (12 days). Design (leave-one-out
reference): on each day, R independent runs of the registered pipeline (independent seed streams, calib_seed),
each taken to 32,000 worlds with stopping switched off. Because look k of run_day always uses seed + k - 1, the run
with normal stopping is exactly the prefix of the run without stopping up to the look where the precision rule is
met (stop_look), so one run gives both the stopped and the fixed-32,000 verdict. The reference C(j) for run r is
the mean of the other R - 1 runs ((R - 1) x 32,000 worlds), which is independent of run r.

Usage:
  python exploratory_5_calib.py pool-run [--days all|first] [--workers N]    part 5 simulation
  python exploratory_5_calib.py pool-analyse                                  part 5 comparison
  python exploratory_5_calib.py calib-run --runs R [--days all|first] [--workers N]
  python exploratory_5_calib.py calib-analyse
"""
import argparse
import csv
import json
import math
import os
import sys
import time
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from datetime import timedelta
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / 'ledgers'))
import simulate as H  # noqa: E402
import analysis as S  # noqa: E402
from day_run import LOOKS, BATCH, run_day  # noqa: E402
from value import CURVES, precision_met, tau_table  # noqa: E402
from teams import TEAMS  # noqa: E402

OUT = S.OUT / 'exploratory_5'
POOL_DRAWS = 16
POOL_TAG = f'pool{POOL_DRAWS}'
CALIB_RUNS_MAX = 20
STOP_TARGET = 0.003                                   # day_run.TARGET
LOOKS_BATCHES = tuple(x // BATCH for x in LOOKS)      # 50, 200, 800
LEVEL_A3 = 1 - 0.01 / 3                               # alpha / 3 per look


# ---------------------------------------------------------------- day selection and seeds
def primary_files():
    return sorted((H.OUT / 'primary').glob('*/exposures_*.npz'))


def _day(f):
    return f.parent.name, f.stem[len('exposures_'):]


def pool_days():
    return [_day(f) for f in primary_files()[0::12]]


def calib_days():
    return [_day(f) for f in primary_files()[0::26]]


def calib_seed(day, r):
    """Seed of calibration run r (looks use seed, seed + 1, seed + 2): apart from the primary seed (the date as an
    integer) and from every other run."""
    if not 0 <= r < CALIB_RUNS_MAX:
        raise ValueError('run index out of range')
    return int(day.replace('-', '')) * 1000 + 500 + 3 * r


# ---------------------------------------------------------------- pipeline pieces
def stop_look(DB, focal_teams, target=STOP_TARGET, looks_batches=LOOKS_BATCHES):
    """The look at which the registered precision rule stops, applied to prefixes of a run without stopping."""
    worst = float('nan')
    for li, nb in enumerate(looks_batches):
        met, worst = precision_met(tau_table({'DB': DB[:nb]}, focal_teams), target)
        if met:
            return li + 1, worst
    return len(looks_batches), worst


def crit_B(Cb, level):
    """The multiplier sup-t critical value of analysis.band_stats at another level."""
    Cb = np.asarray(Cb, float); B = Cb.shape[0]
    m = Cb.mean(0); sd = Cb.std(0, ddof=1)
    ok = sd > 1e-12
    if not ok.any():
        return 0.0
    resid = (Cb[:, ok] - m[ok]) / (sd[ok] * math.sqrt(B - 1))
    return float(np.quantile(np.abs(S._xi(B) @ resid).max(1), level))


def ref_class(c):
    """Class of a reference C(j), j = 1..30 (part 6)."""
    c = np.asarray(c, float); mn = float(c.min())
    if float(np.abs(c).max()) < S.DELTA:
        cls = 'negligible'
    elif mn >= 0:
        cls = 'dominance'
    elif mn >= -S.DELTA:
        cls = 'approximate_dominance'
    else:
        cls = 'material_reversal'
    return {'cls': cls, 'min_c': mn, 'crossing': bool(mn < -S.DELTA and c[:29].max() > 0),
            'h1_crossing': bool(c[:11].min() < 0 and c[11:15].max() > 0)}


def leave_one_out(means):
    means = np.asarray(means, float); R = means.shape[0]
    return (means.sum(0)[None] - means) / (R - 1)


def _state(games, season, day):
    year = H.draft_year(season)
    todays = H.window_days(games, season)[day]
    cutoff = min(g['start'] for g in todays) - timedelta(hours=6)
    state = H.build_state(games, season, cutoff)
    ids = {g['game_id'] for g in todays}
    focal = [j for j, gid in enumerate(state['remaining_ids']) if gid in ids]
    if len(focal) != len(todays):
        raise ValueError(f'{day}: some games of the day are already known at the cutoff')
    return year, state, focal, cutoff


_GAMES = None


def _games():
    global _GAMES
    if _GAMES is None:
        _GAMES = H.E.load_games(H.GAMES)
    return _GAMES


def _env():
    for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
        os.environ[k] = '1'


def _log(path, rec):
    new = not path.exists()
    with open(path, 'a', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rec), lineterminator='\n')
        if new:
            w.writeheader()
        w.writerow(rec)


# ---------------------------------------------------------------- part 5
def pool_one(args):
    season, day = args
    path = OUT / POOL_TAG / season / f'exposures_{day}.npz'
    if path.exists():
        return {'season': season, 'day': day, 'status': 'exists'}
    games = _games()
    year, state, focal, cutoff = _state(games, season, day)
    meta_p = json.loads(bytes(np.load(H.OUT / 'primary' / season / f'exposures_{day}.npz')['meta']).decode())
    t0 = time.time()
    res = run_day(state, focal, seed=meta_p['seed'], router=H.router_for(year), min_pick_new=H.restrictions(year),
                  looks=LOOKS, lottery_draws=POOL_DRAWS)
    secs = round(time.time() - t0, 1)
    meta = dict(meta_p, run_tag=POOL_TAG, lottery_draws=POOL_DRAWS, looks=res['looks'],
                precision_met=res['precision_met'], n_worlds=res['n'], secs=secs,
                primary_n_worlds=meta_p['n_worlds'], primary_secs=meta_p.get('secs'))
    assert meta['focal_game_ids'] == [state['remaining_ids'][j] for j in focal]
    path.parent.mkdir(parents=True, exist_ok=True)
    H.save(path, res, meta)
    rec = {'season': season, 'day': day, 'status': 'done', 'secs': secs, 'worlds': res['n'],
           'primary_worlds': meta_p['n_worlds'], 'focal': len(focal), 'finished_unix': round(time.time())}
    _log(OUT / POOL_TAG / 'progress_log.csv', rec)
    return rec


def pool_team_games(season, day, root=None, draws=POOL_DRAWS):
    root = root or OUT / POOL_TAG
    dn = f'd{draws}'
    a = S.load_day(H.OUT / 'primary' / season / f'exposures_{day}.npz')
    b = S.load_day(root / season / f'exposures_{day}.npz')
    ma, mb = a['meta'], b['meta']
    assert ma['focal_game_ids'] == mb['focal_game_ids'] and ma['focal_teams'] == mb['focal_teams']
    year = int(season[:4]) + 1
    cl, pooled = S.claims(year)
    ranks, _ = S.cutoff_ranks(ma)
    v = CURVES['linear']
    tg, gm = [], []
    for g, (h, aw) in enumerate(ma['focal_teams']):
        gid = ma['focal_game_ids'][g]
        third = np.array([x for x in range(30) if x not in (h, aw)])
        pooled_game = any(S.features(year, c, o, set(), cl, pooled)['holds_pooled_pick'] for c, o in ((h, aw), (aw, h)))
        for ri, r in enumerate(S.RULES):
            rec_g = dict(season=season, day=day, game_id=gid, rule=r, pooled_game=pooled_game,
                         h2_sample=bool(S.third_party_claim(year, h, aw, cl)))
            for tag, src in (('d4', a['DB']), (dn, b['DB'])):
                s_ = (-(src[:, g, ri] @ v)).mean(0); mat = np.abs(s_) >= S.DELTA
                tot = float(np.abs(s_[mat]).sum()); th = float(np.abs(s_[third][mat[third]]).sum())
                rec_g[f'mean_abs_third_{tag}'] = th / len(third)
                rec_g[f'tp_{tag}'] = th / tot if tot >= S.DELTA else float('nan')
            gm.append(rec_g)
            for side, c in ((0, h), (1, aw)):
                o = aw if side == 0 else h
                sgn = 1.0 if side == 0 else -1.0
                hp = S.features(year, c, o, set(), cl, pooled)['holds_pooled_pick']
                for pf, key in (('actual', 'DB'), ('own', 'DB_own')):
                    rec = dict(season=season, day=day, game_id=gid, side=side, team=TEAMS[c], rank=int(ranks[c]),
                               rule=r, portfolio=pf, holds_pooled_pick=hp,
                               worlds_d4=ma['n_worlds'], **{f'worlds_{dn}': mb['n_worlds']})
                    for tag, src in (('d4', a[key]), (dn, b[key])):
                        db = sgn * src[:, g, ri, c, :]
                        m, se, crit = S.band_stats(np.cumsum(db, axis=1))
                        rec[f'verdict_{tag}'] = S.verdict(m, se, crit['B'], 30)[0]
                        rec[f'tau_{tag}'] = float((db @ v).mean())
                    tg.append(rec)
    return tg, gm


def pool_analyse(run_tag=POOL_TAG):
    root, sel, draws, prefix = POOL_RUNS[run_tag]()
    dn = f'd{draws}'
    days = [d for d in sel if (root / d[0] / f'exposures_{d[1]}.npz').exists()]
    tg, gm = [], []
    for season, day in days:
        a, b = pool_team_games(season, day, root, draws); tg += a; gm += b
    summ, trans = [], []
    for pf in S.PORTFOLIOS:
        for r in S.RULES:
            for scope in ('pooled holders', 'all'):
                sub = [x for x in tg if x['portfolio'] == pf and x['rule'] == r and (scope == 'all' or x['holds_pooled_pick'])]
                if not sub:
                    continue
                dt = np.array([x[f'tau_{dn}'] - x['tau_d4'] for x in sub])
                summ.append(dict(kind='team-games', portfolio=pf, rule=r, scope=scope, n=len(sub),
                                 mean_abs_dtau=float(np.abs(dt).mean()), max_abs_dtau=float(np.abs(dt).max()),
                                 share_abs_dtau_ge_delta=float((np.abs(dt) >= S.DELTA).mean()),
                                 verdicts_changed=sum(x[f'verdict_{dn}'] != x['verdict_d4'] for x in sub),
                                 reversals_d4=sum(x['verdict_d4'] == 'reversal' for x in sub),
                                 **{f'reversals_{dn}': sum(x[f'verdict_{dn}'] == 'reversal' for x in sub)}))
                if scope == 'pooled holders':
                    for (x4, x16), n in sorted(Counter((x['verdict_d4'], x[f'verdict_{dn}']) for x in sub).items()):
                        trans.append(dict(portfolio=pf, rule=r, verdict_draws4=x4, **{f'verdict_draws{draws}': x16}, n=n))
    for r in S.RULES:
        for scope in ('pooled games', 'all games'):
            sub = [x for x in gm if x['rule'] == r and (scope == 'all games' or x['pooled_game'])]
            rec = dict(kind='games', rule=r, scope=scope, n=len(sub))
            for tag in ('d4', dn):
                rec[f'mean_abs_third_{tag}'] = float(np.mean([x[f'mean_abs_third_{tag}'] for x in sub]))
                rec[f'tp_median_{tag}'] = float(np.nanmedian([x[f'tp_{tag}'] for x in sub]))
                rec[f'tp_mean_{tag}'] = float(np.nanmean([x[f'tp_{tag}'] for x in sub]))
            summ.append(rec)
    # H2 on the H2 games of these days: paired 3-2-1 minus old mean |third-party stake|
    key = lambda x: (x['season'], x['day'], x['game_id'])
    by = {(key(x), x['rule']): x for x in gm}
    h2 = [k for (k, r) in by if r == 'old' and by[(k, r)]['h2_sample']]
    rec = dict(kind='H2', scope='H2 games of the selected days', n=len(h2))
    for tag in ('d4', dn):
        rec[f'h2_{tag}'] = float(np.mean([by[(k, 'new')][f'mean_abs_third_{tag}'] - by[(k, 'old')][f'mean_abs_third_{tag}']
                                          for k in h2])) if h2 else float('nan')
    summ.append(rec)
    OUT.mkdir(parents=True, exist_ok=True)
    _write(OUT / f'{prefix}_team_games.csv', tg); _write(OUT / f'{prefix}_games.csv', gm)
    _write(OUT / f'{prefix}_summary.csv', summ); _write(OUT / f'{prefix}_transitions.csv', trans)
    pool_tex(prefix, summ, draws)
    print(json.dumps({'run': run_tag, 'days': len(days), 'team_games': len(tg) // 4,
                      'pooled_holder_team_games': sum(x['holds_pooled_pick'] for x in tg) // 4}))


def pool_tex(prefix, summ, draws):
    """Two table bodies in the paper's format: team-games (|Δτ| ×10⁻³, verdicts) and games (stakes, TP, H2)."""
    import exploratory_5 as E5
    E5.TAB = OUT / 'tables'
    dn = f'd{draws}'; rn = {'old': 'old rule', 'new': '3-2-1'}
    name = prefix.replace('E5_5_', 'tab_e5_5_')
    rows = [[rn[x['rule']], x['portfolio'], x['scope'], str(x['n']), E5.num(x['mean_abs_dtau'], 2, scale=1e3),
             E5.num(x['max_abs_dtau'], 2, scale=1e3), str(x['verdicts_changed']),
             f"{x['reversals_d4']} / {x[f'reversals_{dn}']}"] for x in summ if x['kind'] == 'team-games']
    E5.write_tex(f'{name}_team_games', ['rule', 'portfolio', 'team-games', 'n', 'mean $|Δτ|$ (×0.001)',
                                        'max $|Δτ|$ (×0.001)', 'verdicts changed', f'reversals, 4 / {draws} draws'],
                 rows, 'lllrrrrr')
    rows = []
    for x in summ:
        if x['kind'] == 'games':
            rows.append([rn[x['rule']], x['scope'], str(x['n']), E5.num(x['mean_abs_third_d4'], 2, scale=1e3),
                         E5.num(x[f'mean_abs_third_{dn}'], 2, scale=1e3), E5.num(x['tp_median_d4'], 3),
                         E5.num(x[f'tp_median_{dn}'], 3)])
        elif x['kind'] == 'H2':
            rows.append(['H2', x['scope'], str(x['n']), E5.num(x['h2_d4'], 3, scale=1e4),
                         E5.num(x[f'h2_{dn}'], 3, scale=1e4), '', ''])
    E5.write_tex(f'{name}_games', ['rule', 'games', 'n', 'mean $|s|$ third, 4 draws (×0.001; H2 row ×0.0001)',
                                   f'same, {draws} draws', 'median TP, 4 draws', f'median TP, {draws} draws'],
                 rows, 'llrrrrr')


def _pool32():
    import pool_convergence as PC
    return H.OUT / 'pool32', [(s, d) for s, d, _, _ in PC.SELECTED_DAYS], 32, 'E5_5_pool32'


# part 5 comparisons: run tag -> (directory of the day files, days, joint draws, output prefix). pool32 is the
# earlier run of pool_convergence.py (primary world counts), which the paper reports for part 5.
POOL_RUNS = {POOL_TAG: lambda: (OUT / POOL_TAG, pool_days(), POOL_DRAWS, 'E5_5_pool'), 'pool32': _pool32}


# ---------------------------------------------------------------- part 6
def calib_one(args):
    season, day, r = args
    path = OUT / 'calib' / season / f'calib_{day}_r{r:02d}.npz'
    if path.exists():
        return {'season': season, 'day': day, 'run': r, 'status': 'exists'}
    games = _games()
    year, state, focal, cutoff = _state(games, season, day)
    seed = calib_seed(day, r)
    t0 = time.time()
    res = run_day(state, focal, seed=seed, router=H.router_for(year), min_pick_new=H.restrictions(year),
                  looks=LOOKS, target=-1.0)                                   # stopping switched off
    secs = round(time.time() - t0, 1)
    ft = res['focal_teams']
    look, worst = stop_look(res['DB'], ft)
    G = len(focal)
    db = np.zeros((len(LOOKS_BATCHES), G, 2, 2, 2, H.STORE_BATCHES, 30), np.float32)  # look, game, rule, side, pf
    mean32 = np.zeros((G, 2, 2, 2, 30))
    for li, nb in enumerate(LOOKS_BATCHES):
        for pi, key in enumerate(('DB', 'DB_own')):
            reb = H.rebatch(res[key][:nb]).astype(np.float32)
            for g, (h, a) in enumerate(ft):
                for side, c in ((0, h), (1, a)):
                    sgn = np.float32(1.0 if side == 0 else -1.0)
                    db[li, g, :, side, pi] = np.moveaxis(sgn * reb[:, g, :, c, :], 1, 0)
                    if li == len(LOOKS_BATCHES) - 1:
                        mean32[g, :, side, pi] = (float(sgn) * res[key][:, g, :, c, :]).mean(0)
    meta = dict(season=season, day=day, run=r, seed=seed, stop_look=look, worst_halfwidth_at_stop=worst,
                focal_teams=[list(map(int, t)) for t in ft], focal_game_ids=[state['remaining_ids'][j] for j in focal],
                n_worlds=res['n'], secs=secs, looks=list(LOOKS), stored='db: float32 rebatched (50) per look prefix; '
                'mean32: float64 mean of the 800 raw batches; axes look, game, rule (old, new), side (home, away), '
                'portfolio (actual, own), batch, slot')
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix('.tmp.npz')
    np.savez_compressed(tmp, db=db, mean32=mean32, meta=np.frombuffer(json.dumps(meta).encode(), np.uint8))
    tmp.replace(path)
    rec = {'season': season, 'day': day, 'run': r, 'status': 'done', 'secs': secs, 'stop_look': look,
           'focal': G, 'finished_unix': round(time.time())}
    _log(OUT / 'calib' / 'progress_log.csv', rec)
    return rec


def _verdicts(Cb):
    m, se, crit = S.band_stats(Cb)
    out = {}
    for lab, c in (('99', crit['B']), ('a3', crit_B(Cb, LEVEL_A3))):
        v, _ = S.verdict(m, se, c, 30)
        lo = m - c * se
        out[f'verdict_{lab}'] = v
        out[f'crossing_{lab}'] = bool(v == 'reversal' and np.any(lo[:29] > 0))
        out[f'h1_crossing_{lab}'] = S.crossing(m, se, c)
    return out


def calib_analyse(n_runs=6):
    """Runs r = 0..n_runs-1 of every day (the first day also has r = 6..8 from the one-day measurement)."""
    rows = []
    for season, day in calib_days():
        files = [f for f in sorted((OUT / 'calib' / season).glob(f'calib_{day}_r*.npz')) if int(f.stem[-2:]) < n_runs]
        if len(files) < 2:
            continue
        runs = [np.load(f) for f in files]
        metas = [json.loads(bytes(x['meta']).decode()) for x in runs]
        ref = np.cumsum(leave_one_out(np.stack([x['mean32'] for x in runs])), axis=-1)   # (R, G, rule, side, pf, 30)
        for k, (x, meta) in enumerate(zip(runs, metas)):
            db = x['db']
            G = db.shape[1]
            for g in range(G):
                for ri, rule in enumerate(S.RULES):
                    for side in (0, 1):
                        for pi, pf in enumerate(S.PORTFOLIOS):
                            rc = ref_class(ref[k, g, ri, side, pi])
                            rec = dict(season=season, day=day, run=meta['run'], game=g, rule=rule, side=side,
                                       portfolio=pf, runs_on_day=len(runs), stop_look=meta['stop_look'],
                                       ref_class=rc['cls'], ref_min_c=rc['min_c'], ref_crossing=rc['crossing'],
                                       ref_h1_crossing=rc['h1_crossing'])
                            for mode, li in (('stopped', meta['stop_look'] - 1), ('fixed', len(LOOKS_BATCHES) - 1)):
                                Cb = np.cumsum(db[li, g, ri, side, pi], axis=1)
                                for kk, vv in _verdicts(Cb).items():
                                    rec[f'{mode}_{kk}'] = vv
                            rows.append(rec)
    if not rows:
        print('no calibration runs'); return
    _write(OUT / 'E5_6_calib_team_games.csv', rows)
    rates = []
    for pf in S.PORTFOLIOS + ('both',):
        for mode in ('stopped', 'fixed'):
            for band in ('99', 'a3'):
                for look in ('all', 1, 2, 3):
                    sub = [x for x in rows if (pf == 'both' or x['portfolio'] == pf)
                           and (look == 'all' or x['stop_look'] == look)]
                    if not sub:
                        continue
                    v = lambda x: x[f'{mode}_verdict_{band}']
                    rev = [x for x in sub if v(x) == 'reversal']
                    not_mat = [x for x in sub if x['ref_min_c'] >= -S.DELTA]
                    mat = [x for x in sub if x['ref_min_c'] < -S.DELTA]
                    dom = [x for x in sub if v(x) == 'dominance_positive']
                    cr = [x for x in sub if x[f'{mode}_crossing_{band}']]
                    h1 = [x for x in sub if x[f'{mode}_h1_crossing_{band}']]
                    rec = dict(portfolio=pf, mode=mode, band=band, stop_look=look, team_game_runs=len(sub),
                               reversal_calls=len(rev), false_reversal=sum(x['ref_min_c'] >= -S.DELTA for x in rev),
                               ref_not_material=len(not_mat),
                               ref_material_reversal=len(mat), missed_reversal=sum(v(x) != 'reversal' for x in mat),
                               dominance_calls=len(dom), false_approx_dominance=sum(x['ref_min_c'] < -S.DELTA for x in dom),
                               crossing_calls=len(cr), false_crossing=sum(not x['ref_crossing'] for x in cr),
                               h1_crossing_calls=len(h1), false_h1_crossing=sum(not x['ref_h1_crossing'] for x in h1))
                    for vv in S.VERDICTS:
                        rec[f'calls_{vv}'] = sum(v(x) == vv for x in sub)
                    rates.append(rec)
    _write(OUT / 'E5_6_calib_rates.csv', rates)
    calib_tex(rates)
    print(json.dumps({'team_game_runs': len(rows), 'days': len({(x['season'], x['day']) for x in rows})}))


def calib_tex(rates):
    """Table body in the paper's format: error counts over all stop looks, by portfolio, stopping and band."""
    import exploratory_5 as E5
    E5.TAB = OUT / 'tables'
    frac = lambda k, n: f'{k:,} / {n:,}'
    rows = []
    for x in rates:
        if x['stop_look'] != 'all' or x['portfolio'] == 'both':
            continue
        rows.append([x['portfolio'], 'registered stopping' if x['mode'] == 'stopped' else 'fixed 32,000 worlds',
                     '99\\%' if x['band'] == '99' else '$1 - 0.01/3$', f"{x['team_game_runs']:,}",
                     frac(x['false_reversal'], x['reversal_calls']), frac(x['missed_reversal'], x['ref_material_reversal']),
                     frac(x['false_approx_dominance'], x['dominance_calls']), frac(x['false_crossing'], x['crossing_calls']),
                     frac(x['false_h1_crossing'], x['h1_crossing_calls'])])
    E5.write_tex('tab_e5_6_calibration', ['portfolio', 'worlds', 'band', 'team-game runs', 'false reversals / calls',
                                          'missed / reference reversals', 'false approx. dominance / calls',
                                          'false crossings / calls', 'false H1 crossings / calls'], rows, 'lllrrrrrr')


# ---------------------------------------------------------------- common
def _write(path, rows):
    keys = list(dict.fromkeys(k for r in rows for k in r))
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=keys, lineterminator='\n'); w.writeheader(); w.writerows(rows)


def _pool(fn, jobs, workers):
    _env()
    with ProcessPoolExecutor(max_workers=workers) as ex:
        for rec in ex.map(fn, jobs):
            print(json.dumps(rec), flush=True)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('cmd', choices=('pool-run', 'pool-analyse', 'calib-run', 'calib-analyse'))
    ap.add_argument('--days', choices=('all', 'first'), default='first')
    ap.add_argument('--runs', type=int, default=6)
    ap.add_argument('--tag', choices=('pool16', 'pool32'), default=POOL_TAG)
    ap.add_argument('--workers', type=int, default=20)
    a = ap.parse_args(argv)
    if a.cmd == 'pool-run':
        days = pool_days() if a.days == 'all' else pool_days()[:1]
        _pool(pool_one, days, a.workers)
    elif a.cmd == 'pool-analyse':
        pool_analyse(a.tag)
    elif a.cmd == 'calib-run':
        days = calib_days() if a.days == 'all' else calib_days()[:1]
        _pool(calib_one, [(s, d, r) for s, d in days for r in range(a.runs)], a.workers)
    else:
        calib_analyse(a.runs)


if __name__ == '__main__':
    main()

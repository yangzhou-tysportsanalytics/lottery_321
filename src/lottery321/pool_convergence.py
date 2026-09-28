"""Pooled-rights convergence check (exploratory; the days were fixed before it was run).

Simple rights are routed from exact lottery marginals, but a native inside a pool or swap is routed on
`lottery_draws` sampled joint draft orders per world and branch (4 in the primary run). That sampling adds
Monte Carlo noise to actual portfolios that own-pick portfolios do not carry, and precision matching does not
align it (Online Appendix F.3). This script re-runs a small, rule-selected set of primary days with 32 joint
draws per world instead of 4, everything else identical (same seeds, same states, same number of worlds as
the primary run stopped at), and compares the two runs team-game by team-game.

Day selection (fixed here, before any run):
  for each of the six seasons, (i) the primary day with the largest number of actual-portfolio team-games that
  hold a pick routed through a pool (ties: the earliest day), and (ii) one further day drawn at random from the
  season's other days with seed 2026092602.  Twelve days in all.
Quantities compared on those days (linear curve, class B): tau per team-game (max and mean absolute change,
share changed by at least delta), verdict changes, H1 crossings, mean absolute third-party stake and the
third-party share TP per game, and the paired actual-minus-own reversal share.

Usage (runs the simulation):                     python pool_convergence.py run [--draws 32] [--worker i --workers n]
  Cost: 32 draws cost about 3.5 times the primary run per world (measured: 200 worlds in 25 s against 7 s), so a
  32,000-world day takes about an hour on an 8-core desktop; four workers in parallel finish the twelve
  days in about three hours.
Analysis, once the files exist:                  python pool_convergence.py analyse
Selected days only (no simulation):              python pool_convergence.py days
Re-derive the day list from the rule (needs pandas): python pool_convergence.py derive
"""
import csv
import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / 'ledgers'))

import simulate as H  # noqa: E402
import analysis as S  # noqa: E402
from day_run import run_day  # noqa: E402
from cutoff_state import build_state  # noqa: E402
from value import CURVES  # noqa: E402
from teams import TEAMS  # noqa: E402
from datetime import timedelta  # noqa: E402

SEASONS = ('2020-21', '2021-22', '2022-23', '2023-24', '2024-25', '2025-26')
SEED_RANDOM_DAY = 2026092602
DRAWS = 32
OUT_ANALYSIS = S.OUT / 'exploratory_4'


# The twelve days, fixed by the rule above before any pool run (derived once by
# `derive_selected_days`, which needs pandas; the runner uses this list so that a machine with
# numpy but not pandas does not need the analysed team-game table).
SELECTED_DAYS = (
    ('2020-21', '2021-04-16', 'most pooled holders', 8), ('2020-21', '2021-04-17', 'random', 1),
    ('2021-22', '2022-02-17', 'most pooled holders', 3), ('2021-22', '2022-03-16', 'random', 2),
    ('2022-23', '2023-04-09', 'most pooled holders', 9), ('2022-23', '2023-03-25', 'random', 6),
    ('2023-24', '2024-04-05', 'most pooled holders', 10), ('2023-24', '2024-03-31', 'random', 6),
    ('2024-25', '2025-04-11', 'most pooled holders', 8), ('2024-25', '2025-02-28', 'random', 7),
    ('2025-26', '2026-04-10', 'most pooled holders', 19), ('2025-26', '2026-03-31', 'random', 10),
)


def selected_days():
    return [dict(season=s, day=d, rule=r, pooled_team_games=n) for s, d, r, n in SELECTED_DAYS]


def derive_selected_days():
    """The rule that produced SELECTED_DAYS, from the analysed primary team-game table (needs pandas)."""
    import exploratory_1 as P
    tg = P.load_tg()
    act = tg[(tg.rule == 'old') & (tg.portfolio == 'actual')]
    rng = np.random.default_rng(SEED_RANDOM_DAY)
    out = []
    for s in SEASONS:
        sub = act[act.season == s]
        counts = sub.groupby('day').holds_pooled_pick.sum().sort_index()
        top = counts[counts == counts.max()].index[0]
        others = [d for d in counts.index if d != top]
        rnd = others[int(rng.integers(0, len(others)))]
        out.append(dict(season=s, day=str(top), rule='most pooled holders', pooled_team_games=int(counts[top])))
        out.append(dict(season=s, day=str(rnd), rule='random', pooled_team_games=int(counts[rnd])))
    return out


def run_one_day_pool(games, season, day, draws=DRAWS, looks_cap=None):
    """One selected day with `draws` joint draft orders per world. The world count is the one the primary
    run stopped at for this day (so only the pooled-rights routing differs); `looks_cap` overrides it for
    smoke tests. Returns (res, meta) like simulate.run_one_day."""
    year = H.draft_year(season)
    router = H.router_for(year); mp = H.restrictions(year)
    prim = H.OUT / 'primary' / season / f'exposures_{day}.npz'
    meta_p = json.loads(bytes(np.load(prim)['meta']).decode())
    todays = H.window_days(games, season)[day]
    cutoff = min(g['start'] for g in todays) - timedelta(hours=6)
    state = build_state(games, season, cutoff)
    ids = {g['game_id'] for g in todays}
    focal = [j for j, gid in enumerate(state['remaining_ids']) if gid in ids]
    if len(focal) != len(todays):
        raise ValueError(f'{day}: some games of the day are already known at the cutoff')
    looks = looks_cap or tuple(x for x in (2000, 8000, 32000) if x <= meta_p['n_worlds'])
    t0 = time.time()
    res = run_day(state, focal, seed=meta_p['seed'], router=router, min_pick_new=mp, looks=looks, lottery_draws=draws)
    meta = dict(meta_p, run_tag=f'pool{draws}', lottery_draws=draws, looks=res['looks'],
                precision_met=res['precision_met'], n_worlds=res['n'], secs=round(time.time() - t0, 1),
                primary_n_worlds=meta_p['n_worlds'])
    return res, meta


def run(draws=DRAWS, worker=0, n_workers=1):
    """Sequential runner (one process). On Windows use tools/simulation/run_pool.bat, which runs the same
    days through the simulation runner with all cores but one."""
    games = H.E.load_games(H.GAMES)
    out_root = H.OUT / f'pool{draws}'
    for i, d in enumerate(selected_days()):
        if i % n_workers != worker:
            continue
        season, day = d['season'], d['day']
        out = out_root / season; out.mkdir(parents=True, exist_ok=True)
        path = out / f'exposures_{day}.npz'
        if path.exists():
            continue
        res, meta = run_one_day_pool(games, season, day, draws)
        H.save(path, res, meta)
        print(json.dumps({'day': day, 'worlds': res['n'], 'secs': meta['secs']}), flush=True)


def analyse(draws=DRAWS):
    v = CURVES['linear']
    rows, games_rows = [], []
    for d in selected_days():
        season, day = d['season'], d['day']
        a = S.load_day(H.OUT / 'primary' / season / f'exposures_{day}.npz')
        b_path = H.OUT / f'pool{draws}' / season / f'exposures_{day}.npz'
        if not b_path.exists():
            continue
        b = S.load_day(b_path)
        ma, mb = a['meta'], b['meta']
        assert ma['focal_game_ids'] == mb['focal_game_ids'] and ma['n_worlds'] == mb['n_worlds']
        ranks, _ = S.cutoff_ranks(ma)
        for g, (h, aw) in enumerate(ma['focal_teams']):
            third = [x for x in range(30) if x not in (h, aw)]
            for ri, r in enumerate(S.RULES):
                for tag, src in (('primary', a['DB']), (f'pool{draws}', b['DB'])):
                    s_ = (-(src[:, g, ri] @ v)).mean(0); mat = np.abs(s_) >= S.DELTA
                    tot = float(np.abs(s_[mat]).sum()); th = float(np.abs(s_[third][mat[third]]).sum())
                    games_rows.append(dict(season=season, day=day, game_id=ma['focal_game_ids'][g], rule=r, run=tag,
                                           mean_abs_third=th / len(third), tp=th / tot if tot > 0 else float('nan')))
                for side, c in ((0, h), (1, aw)):
                    sgn = 1.0 if side == 0 else -1.0
                    for pf, key in (('actual', 'DB'), ('own', 'DB_own')):
                        rec = dict(season=season, day=day, game_id=ma['focal_game_ids'][g], team=TEAMS[c], rank=int(ranks[c]),
                                   rule=r, portfolio=pf)
                        for tag, src in (('primary', a[key]), ('pool', b[key])):
                            db = sgn * src[:, g, ri, c, :]
                            m, se, crit = S.band_stats(np.cumsum(db, axis=1))
                            vb, _ = S.verdict(m, se, crit['B'], 30)
                            rec[f'tau_{tag}'] = float((db @ v).mean()); rec[f'verdict_{tag}'] = vb
                            rec[f'crossing_{tag}'] = S.crossing(m, se, crit['B'])
                        rows.append(rec)
    if not rows:
        print('no pool run files found'); return
    OUT_ANALYSIS.mkdir(parents=True, exist_ok=True)
    with open(OUT_ANALYSIS / 'R23_pool_convergence_team_games.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    summary = []
    for pf in ('actual', 'own'):
        for r in S.RULES:
            sub = [x for x in rows if x['portfolio'] == pf and x['rule'] == r]
            dt = np.array([x['tau_pool'] - x['tau_primary'] for x in sub])
            summary.append(dict(portfolio=pf, rule=r, team_games=len(sub), mean_abs_dtau=float(np.abs(dt).mean()),
                                max_abs_dtau=float(np.abs(dt).max()), share_dtau_ge_delta=float((np.abs(dt) >= S.DELTA).mean()),
                                verdicts_changed=sum(x['verdict_pool'] != x['verdict_primary'] for x in sub),
                                reversals_primary=sum(x['verdict_primary'] == 'reversal' for x in sub),
                                reversals_pool=sum(x['verdict_pool'] == 'reversal' for x in sub),
                                crossings_changed=sum(x['crossing_pool'] != x['crossing_primary'] for x in sub)))
    for r in S.RULES:
        ga = [x for x in games_rows if x['rule'] == r and x['run'] == 'primary']; gb = [x for x in games_rows if x['rule'] == r and x['run'] != 'primary']
        summary.append(dict(portfolio='games', rule=r, team_games=len(ga),
                            mean_abs_third_primary=float(np.mean([x['mean_abs_third'] for x in ga])),
                            mean_abs_third_pool=float(np.mean([x['mean_abs_third'] for x in gb])),
                            tp_median_primary=float(np.nanmedian([x['tp'] for x in ga])), tp_median_pool=float(np.nanmedian([x['tp'] for x in gb]))))
    keys = sorted({k for s_ in summary for k in s_})
    with open(OUT_ANALYSIS / 'R23_pool_convergence.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(summary)
    for s_ in summary:
        print(s_)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'days'
    draws = int(sys.argv[sys.argv.index('--draws') + 1]) if '--draws' in sys.argv else DRAWS
    if cmd == 'days':
        for d in selected_days():
            print(d)
    elif cmd == 'derive':
        der = derive_selected_days()
        assert der == selected_days(), 'SELECTED_DAYS no longer matches the rule'
        print('SELECTED_DAYS matches the rule')
    elif cmd == 'run':
        worker = int(sys.argv[sys.argv.index('--worker') + 1]) if '--worker' in sys.argv else 0
        workers = int(sys.argv[sys.argv.index('--workers') + 1]) if '--workers' in sys.argv else 1
        run(draws, worker, workers)
    elif cmd == 'analyse':
        analyse(draws)
    else:
        raise SystemExit(__doc__)

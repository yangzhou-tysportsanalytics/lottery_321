"""simulation: league-wide historical exposure runs for the paper (2020-21..2025-26).

For every game day in the last LATE_WEEKS (8) weeks of each regular season:
  * one state per ET game day at the earliest scheduled tip minus 6 h;
  * focal = every game of that day (both teams of each game get tau via tau_table);
  * rules: old (2019-2026 flattened odds, the rule actually in force) and the 3-2-1 research scenario;
  * rights: the historical ledger router of that draft year (src/lottery321/ledgers), plus
    own-pick-only portfolios (DB_own) from the same worlds;
  * 3-2-1 repeat restrictions in the research scenario, applied as if 3-2-1 had been in force, using the
    ACTUAL native lottery results of the two previous drafts (no #1 in consecutive drafts -> min slot 2;
    top-5 in both previous drafts -> min slot 6). Sensitivity without restrictions is a separate run tag;
  * precision rule of day_run (linear curve, halfwidth <= 0.003 at 2k/8k/32k worlds).
Each day is written once to OUT/<tag>/<season>/exposures_<day>.npz (DB and DB_own stored as 50 super-batch
means in float32); existing files are skipped (resumable).
Usage: python simulate.py <season> [worker_index n_workers] [--no-restrictions]
"""
import importlib
import io
import json
import sys
import time
from datetime import timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
for p in (HERE, HERE / 'ledgers'):
    sys.path.insert(0, str(p))

import elo as E  # noqa: E402
from teams import TEAMS  # noqa: E402
from cutoff_state import build_state  # noqa: E402
from day_run import run_day  # noqa: E402

ET = ZoneInfo('America/New_York')
GAMES = ROOT / 'data/games.csv'
OUT = ROOT / 'simulations'
MAIN_SEASONS = ('2020-21', '2021-22', '2022-23', '2023-24', '2024-25', '2025-26')
# Native top-5 results of the 2019 draft (NBA.com "2019 NBA Draft results, picks 1-60"; pick 4 was the
# Lakers' native pick). 2020-2026 come from the ledgers' `realized` blocks.
TOP5_2019 = ('NOP', 'MEM', 'NYK', 'LAL', 'CLE')


def draft_year(season):
    return int(season[:4]) + 1


def native_top5(year):
    if year == 2019:
        return list(TOP5_2019)
    d = json.loads((HERE / 'ledgers' / f'ledger_{year}_draft.json').read_text(encoding='utf-8'))
    return [d['realized'][str(k)]['native'] for k in range(1, 6)]


def restrictions(year):
    """3-2-1 repeat restrictions as if in force in draft `year`: {team index: earliest slot}."""
    prev1, prev2 = native_top5(year - 1), native_top5(year - 2)
    out = {}
    out[TEAMS.index(prev1[0])] = 2                                  # #1 last year -> not #1 again
    for t in set(prev1) & set(prev2):                               # top-5 in both previous drafts
        out[TEAMS.index(t)] = max(out.get(TEAMS.index(t), 1), 6)
    return out


def router_for(year):
    mod = importlib.import_module(f'router_{year}')
    return getattr(mod, f'Router{year}')


def window_days(games, season):
    start = E.late_window_start(games, season)
    days = {}
    for g in games:
        if g['season'] == season and g['start'] >= start:
            days.setdefault(g['start'].astimezone(ET).date().isoformat(), []).append(g)
    return dict(sorted(days.items()))


def run_one_day(games, season, day, todays, router, min_pick_new, looks=(2000, 8000, 32000),
                new_procedure='sequential_feasible', win_mode=None):
    """One registered state. `new_procedure` and `win_mode` are the robustness switches of addendum A1
    section 5: 'draw_then_adjust' for the alternative joint lottery procedure, and a cutoff_state.late_override
    mode ('prior_late_link' or 'stress_slope_x1.25') for the win model. Defaults reproduce the primary run."""
    cutoff = min(g['start'] for g in todays) - timedelta(hours=6)
    state = build_state(games, season, cutoff)
    ids = {g['game_id'] for g in todays}
    focal = [j for j, gid in enumerate(state['remaining_ids']) if gid in ids]
    if len(focal) != len(todays):
        raise ValueError(f'{day}: some games of the day are already known at the cutoff')
    seed = int(day.replace('-', ''))
    probs = n_late = None
    if win_mode:
        from cutoff_state import late_override
        probs, n_late = late_override(state, games, season, win_mode)
    t0 = time.time()
    res = run_day(state, focal, seed=seed, router=router, min_pick_new=min_pick_new, looks=looks,
                  probs_override=probs, new_procedure=new_procedure)
    meta = {'season': season, 'day': day, 'cutoff_utc': cutoff.isoformat(), 'seed': seed,
            'focal_teams': [list(map(int, t)) for t in res['focal_teams']],
            'focal_game_ids': [state['remaining_ids'][j] for j in focal],
            'min_pick_new': {TEAMS[k]: v for k, v in (min_pick_new or {}).items()},
            'looks': res['looks'], 'precision_met': res['precision_met'], 'n_worlds': res['n'],
            'secs': round(time.time() - t0, 1), 'remaining_games': len(state['remaining']),
            'new_procedure': new_procedure, 'win_mode': win_mode or 'primary',
            'n_late_games_overridden': n_late}
    return res, meta


STORE_BATCHES = 50


def rebatch(DB, k=STORE_BATCHES):
    """Average consecutive batch means into k equal super-batches (k divides the batch count for every
    look size: 50, 200, 800). Batch-means standard errors stay valid with k batches; the precision
    decision itself was already taken on the full batches during the run."""
    B = DB.shape[0]
    if B % k:
        raise ValueError('batch count not divisible')
    return DB.reshape((k, B // k) + DB.shape[1:]).mean(axis=1)


def save(path, res, meta):
    meta = dict(meta, stored_batches=STORE_BATCHES, stored_dtype='float32 (DB, DB_own); float64 (Q, ST)')
    buf = io.BytesIO()
    np.savez_compressed(buf, Q=res['Q'], DB=rebatch(res['DB']).astype(np.float32),
                        DB_own=rebatch(res['DB_own']).astype(np.float32), ST=res['ST'],
                        meta=np.frombuffer(json.dumps(meta, sort_keys=True).encode(), dtype=np.uint8))
    tmp = path.with_suffix('.tmp')
    tmp.write_bytes(buf.getvalue()); tmp.replace(path)


def main(season, worker=0, n_workers=1, no_restrictions=False):
    games = E.load_games(GAMES)
    year = draft_year(season)
    router = router_for(year)
    mp = {} if no_restrictions else restrictions(year)
    tag = 'norestr' if no_restrictions else 'primary'
    out = OUT / tag / season; out.mkdir(parents=True, exist_ok=True)
    days = list(window_days(games, season).items())
    for i, (day, todays) in enumerate(days):
        if i % n_workers != worker:
            continue
        path = out / f'exposures_{day}.npz'
        if path.exists():
            continue
        res, meta = run_one_day(games, season, day, todays, router, mp)
        meta['run_tag'] = tag; meta['ledger'] = f'ledger_{year}_draft.json'
        save(path, res, meta)
        print(json.dumps({'day': day, 'focal': len(todays), 'secs': meta['secs'], 'worlds': meta['n_worlds'],
                          'precision_met': meta['precision_met']}), flush=True)


if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    main(a[0], int(a[1]) if len(a) > 1 else 0, int(a[2]) if len(a) > 2 else 1, '--no-restrictions' in sys.argv)

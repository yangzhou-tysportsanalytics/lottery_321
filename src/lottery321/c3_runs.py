"""C3 driver: the component decomposition run over the registered subsample (C3 registration, section 3).

One state per game day, the 81-day subsample (every 4th game day of each season), all 24 configurations on
common random numbers with the primary run. Stopping rule as in day_run: looks at 2,000 / 8,000 / 32,000
worlds, stop when the linear-curve tau of EVERY configuration and team-game has half-width <= 0.003.
Output: simulations/c3/<season>/exposures_<day>.npz with DOWN and STK stored as 50
super-batch means in float32, plus metadata. Existing files are skipped, so the run is resumable.
Usage: python c3_runs.py <season> [worker_index n_workers]
"""
import io
import json
import sys
import time
from datetime import timedelta
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
for p in (HERE, HERE / 'ledgers'):
    sys.path.insert(0, str(p))

import elo as E  # noqa: E402
import simulate as H  # noqa: E402
import protection_ban as BAN  # noqa: E402
from teams import TEAMS  # noqa: E402
from c3_sim import CURVE_NAMES, config_list, simulate_c3  # noqa: E402
from day_run import BATCH, LOOKS, TARGET  # noqa: E402
from cutoff_state import build_state  # noqa: E402
from value import CURVES, Z  # noqa: E402

OUT = H.OUT / 'c3'
SUBSAMPLE_STEP = 4
STORE_BATCHES = 50


def subsample_days(games, season):
    return list(H.window_days(games, season))[::SUBSAMPLE_STEP]


def routers_for(year):
    return {'base': H.router_for(year), 'A': BAN.make_router(year, 'A'), 'B': BAN.make_router(year, 'B')}


def halfwidth(DOWN):
    """Largest 99% half-width of the linear-curve tau over configurations, games and sides."""
    t = DOWN @ CURVES['linear']                         # (batches, G, C, 2)
    se = t.std(axis=0, ddof=1) / np.sqrt(t.shape[0])
    return float((Z * se).max())


def run_day(state, focal, seed, routers, min_pick_new, looks=LOOKS, batch=BATCH, target=TARGET):
    blocks_d, blocks_s, done, log = [], [], 0, []
    for li, goal in enumerate(looks):
        add = goal - done
        if add % batch:
            raise ValueError('look sizes must be multiples of the batch size')
        res = simulate_c3(state, focal, n=add, seed=seed + li, routers=routers,
                          min_pick_new=min_pick_new, batches=add // batch)
        blocks_d.append(res['DOWN']); blocks_s.append(res['STK']); done = goal
        DOWN = np.concatenate(blocks_d, axis=0); STK = np.concatenate(blocks_s, axis=0)
        hw = halfwidth(DOWN)
        met = hw <= target
        log.append({'look': li + 1, 'worlds': done, 'max_halfwidth_linear': hw, 'precision_met': met})
        if met:
            break
    out = dict(res); out.update({'DOWN': DOWN, 'STK': STK, 'n': done, 'batches': DOWN.shape[0],
                                 'looks': log, 'precision_met': log[-1]['precision_met']})
    return out


def rebatch(x, k=STORE_BATCHES):
    """Average consecutive batch means into k super-batches. A short smoke run with fewer than k batches
    is stored as it is (batch-means standard errors stay valid either way)."""
    B = x.shape[0]
    if B < k:
        return x
    if B % k:
        raise ValueError('batch count not divisible')
    return x.reshape((k, B // k) + x.shape[1:]).mean(axis=1)


def save(path, res, meta):
    meta = dict(meta, stored_batches=min(STORE_BATCHES, res['DOWN'].shape[0]), stored_dtype='float32', curves=list(CURVE_NAMES),
                configs=res['configs'], subsets=res['subsets'])
    buf = io.BytesIO()
    np.savez_compressed(buf, DOWN=rebatch(res['DOWN']).astype(np.float32),
                        STK=rebatch(res['STK']).astype(np.float32),
                        meta=np.frombuffer(json.dumps(meta, sort_keys=True).encode(), dtype=np.uint8))
    tmp = path.with_suffix('.tmp'); tmp.write_bytes(buf.getvalue()); tmp.replace(path)


def run_one_day(games, season, day, todays, looks=LOOKS):
    year = H.draft_year(season)
    cutoff = min(g['start'] for g in todays) - timedelta(hours=6)
    state = build_state(games, season, cutoff)
    ids = {g['game_id'] for g in todays}
    focal = [j for j, gid in enumerate(state['remaining_ids']) if gid in ids]
    if len(focal) != len(todays):
        raise ValueError(f'{day}: some games of the day are already known at the cutoff')
    seed = int(day.replace('-', ''))
    mp = H.restrictions(year)
    t0 = time.time()
    res = run_day(state, focal, seed, routers_for(year), mp, looks=looks)
    meta = {'season': season, 'day': day, 'cutoff_utc': cutoff.isoformat(), 'seed': seed, 'run_tag': 'c3',
            'focal_teams': [[int(a), int(b)] for a, b in res['focal_teams']],
            'focal_game_ids': [state['remaining_ids'][j] for j in focal],
            'min_pick_new': {TEAMS[k]: v for k, v in mp.items()},
            'looks': res['looks'], 'precision_met': res['precision_met'], 'n_worlds': res['n'],
            'secs': round(time.time() - t0, 1), 'remaining_games': len(state['remaining']),
            'ledger': f'ledger_{year}_draft.json + ban variants A/B'}
    return res, meta


def main(season, worker=0, n_workers=1):
    games = E.load_games(H.GAMES)
    out = OUT / season; out.mkdir(parents=True, exist_ok=True)
    days = subsample_days(games, season)
    allday = H.window_days(games, season)
    for i, day in enumerate(days):
        if i % n_workers != worker:
            continue
        path = out / f'exposures_{day}.npz'
        if path.exists():
            continue
        res, meta = run_one_day(games, season, day, allday[day])
        save(path, res, meta)
        print(json.dumps({'day': day, 'secs': meta['secs'], 'worlds': meta['n_worlds'],
                          'precision_met': meta['precision_met']}), flush=True)


if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    main(a[0], int(a[1]) if len(a) > 1 else 0, int(a[2]) if len(a) > 2 else 1)

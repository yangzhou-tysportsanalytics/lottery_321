"""Simulation runner for a Windows PC (parallel, resumable, keeps the PC awake).

Variants (registration + addendum A1 section 5):
    primary    the registered main run (default)
    norestr    no repeat restrictions, all days
    dta        draw-then-adjust joint lottery procedure, subsample
    latelink   win model refitted on earlier seasons' late windows, subsample
    stress     win-model slope x1.25, subsample
    alt6       2024 WAS 13-30 alternative router, the 25 registered 2023-24 days
    pool32     pooled-rights convergence check: 12 pre-selected days, 32 joint draft orders per world
               instead of 4, same seeds and world counts as the primary run (pool_convergence.py)

Runs every (season, game day) job of the registered simulation design (registration/run_registration.md) through
simulate.run_one_day / save, using N worker processes (default: all logical cores minus one).
Existing output files are skipped, so the run can be stopped and restarted at any time.

Usage (normally started by run_primary.bat):
    python run_simulation.py                 # primary run, all six seasons
    python run_simulation.py --norestr       # sensitivity run without repeat restrictions
    python run_simulation.py --workers 6     # choose the number of processes
    python run_simulation.py --smoke         # 40 worlds on one day per season, output to a temp folder
Progress: simulations/<tag>/progress_log.csv (one line per finished day).
"""
import argparse
import csv
import json
import multiprocessing as mp
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent                     # <repository>/tools/simulation
ROOT = HERE.parents[1]                                     # <repository>
SCRIPTS = ROOT / 'src' / 'lottery321'
for p in (SCRIPTS, SCRIPTS / 'ledgers'):
    sys.path.insert(0, str(p))

_G = {}


def _keep_awake(on=True):
    """Ask Windows not to sleep while the run is active (no admin rights needed)."""
    if os.name != 'nt':
        return
    import ctypes
    ES_CONTINUOUS, ES_SYSTEM_REQUIRED = 0x80000000, 0x00000001
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | (ES_SYSTEM_REQUIRED if on else 0))


def _init_worker():
    import warnings
    warnings.filterwarnings('ignore', category=RuntimeWarning)   # 1-batch smoke runs: undefined SE
    os.environ.setdefault('OMP_NUM_THREADS', '1')
    import elo as E
    import simulate as H
    _G['H'] = H
    _G['games'] = E.load_games(H.GAMES)


VARIANTS = {'primary': {}, 'norestr': {}, 'dta': {'new_procedure': 'draw_then_adjust'},
            'latelink': {'win_mode': 'prior_late_link'}, 'stress': {'win_mode': 'stress_slope_x1.25'},
            'alt6': {}, 'c3': {}, 'pool32': {}}
SUBSAMPLE_STEP = 4                      # addendum A1 section 5: every 4th game day of each season
ALT6_SEASON = '2023-24'


def _alt6_days():
    """The window days listed for the item-6 re-run (addendum A1 section 6)."""
    f = ROOT / 'results/ledger_assumption_check.json'
    d = json.loads(f.read_text(encoding='utf-8'))
    return set(d['summary']['item6']['days_at_or_above_threshold'])


def _job(args):
    """One day; a failure is returned as a row with status 'failed' and its traceback, so that the other
    days keep running and the message is kept in <tag>/errors.log."""
    season, day, tag, out_dir, looks = args
    try:
        return _job_inner(args)
    except Exception:
        import traceback
        tb = traceback.format_exc()
        try:
            with open(Path(out_dir) / 'errors.log', 'a', encoding='utf-8') as f:
                f.write(f'=== {datetime.now(timezone.utc).isoformat(timespec="seconds")} {season} {day}\n{tb}\n')
        except Exception:
            pass
        return {'season': season, 'day': day, 'status': 'failed', 'error': tb.strip().splitlines()[-1]}


def _job_inner(args):
    season, day, tag, out_dir, looks = args
    H = _G['H']; games = _G['games']
    path = Path(out_dir) / season / f'exposures_{day}.npz'
    if path.exists():
        return {'season': season, 'day': day, 'status': 'skipped'}
    if tag == 'pool32':
        import pool_convergence as PC
        t0 = time.time()
        res, meta = PC.run_one_day_pool(games, season, day, 32, looks_cap=(looks if len(looks) == 1 and looks[0] < 2000 else None))
        meta['host'] = 'windows_pc'
        path.parent.mkdir(parents=True, exist_ok=True)
        if len(looks) == 1 and looks[0] < 2000:
            meta['smoke'] = True
            import numpy as np, io
            buf = io.BytesIO(); np.savez_compressed(buf, Q=res['Q'], meta=np.frombuffer(json.dumps(meta).encode(), dtype=np.uint8))
            path.write_bytes(buf.getvalue())
        else:
            H.save(path, res, meta)
        return {'season': season, 'day': day, 'status': 'done', 'secs': round(time.time() - t0, 1),
                'worlds': meta['n_worlds'], 'precision_met': meta['precision_met'], 'focal': len(meta['focal_game_ids'])}
    if tag == 'c3':
        import c3_runs as C3
        t0 = time.time()
        res, meta = C3.run_one_day(games, season, day, H.window_days(games, season)[day], looks=looks)
        meta['host'] = 'windows_pc'
        path.parent.mkdir(parents=True, exist_ok=True)
        C3.save(path, res, meta)
        return {'season': season, 'day': day, 'status': 'done', 'secs': round(time.time() - t0, 1),
                'worlds': meta['n_worlds'], 'precision_met': meta['precision_met'],
                'focal': len(meta['focal_game_ids'])}
    year = H.draft_year(season)
    todays = H.window_days(games, season)[day]
    mp_new = {} if tag == 'norestr' else H.restrictions(year)
    router = H.router_for(year)
    if tag == 'alt6':
        import router_2024_alt6 as A6
        router = A6.Router2024Alt6
    t0 = time.time()
    res, meta = H.run_one_day(games, season, day, todays, router, mp_new, looks=looks, **VARIANTS[tag])
    meta['run_tag'] = tag; meta['ledger'] = f'ledger_{year}_draft.json'; meta['host'] = 'windows_pc'
    if tag == 'alt6':
        meta['ledger'] = 'ledger_2024_draft.json + alt reading of the WAS 13-30 branch (assumption item 6)'
    path.parent.mkdir(parents=True, exist_ok=True)
    if len(looks) == 1 and looks[0] < 2000:          # smoke test: batches not divisible by 50
        meta['smoke'] = True
        import numpy as np, io
        buf = io.BytesIO(); np.savez_compressed(buf, Q=res['Q'], meta=np.frombuffer(json.dumps(meta).encode(), dtype=np.uint8))
        path.write_bytes(buf.getvalue())
    else:
        H.save(path, res, meta)
    return {'season': season, 'day': day, 'status': 'done', 'secs': round(time.time() - t0, 1),
            'worlds': meta['n_worlds'], 'precision_met': meta['precision_met'], 'focal': len(todays)}


def _record_environment(out, tag, workers, todo):
    """Append one session record to <tag>/run_environment.json: what this run was produced on.

    The replication package needs the machine, interpreter and thread caps that produced the exposure
    files, and the per-day metadata only carries a host label. Appending keeps every session of a
    resumable run, including restarts on a different machine."""
    import platform
    import numpy as np
    path = Path(out) / 'run_environment.json'
    try:
        doc = json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        doc = {'tag': tag, 'sessions': []}
    doc['sessions'].append({
        'started_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'host': 'windows_pc', 'platform': platform.platform(),
        'machine': platform.machine(), 'python': sys.version.split()[0], 'numpy': np.__version__,
        'cpu_count': os.cpu_count(), 'workers': workers, 'days_to_run': todo,
        'threads': {k: os.environ.get(k) for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS',
                                                   'MKL_NUM_THREADS')}})
    try:
        path.write_text(json.dumps(doc, indent=1), encoding='utf-8')
    except Exception as e:                      # a run must never fail because the record cannot be written
        print(f'(could not write {path}: {e})', flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--norestr', action='store_true')
    ap.add_argument('--variant', choices=sorted(VARIANTS), default=None)
    ap.add_argument('--workers', type=int, default=max(1, (os.cpu_count() or 2) - 1))
    ap.add_argument('--smoke', action='store_true')
    a = ap.parse_args()
    import elo as E
    import simulate as H
    tag = a.variant or ('norestr' if a.norestr else 'primary')
    out = (ROOT / 'simulations_smoke' if a.smoke else H.OUT) / tag
    out.mkdir(parents=True, exist_ok=True)
    games = E.load_games(H.GAMES)
    looks = (40,) if a.smoke else (2000, 8000, 32000)
    jobs = []
    alt6_days = _alt6_days() if tag == 'alt6' else None
    for season in H.MAIN_SEASONS:
        days = list(H.window_days(games, season))
        if tag in ('dta', 'latelink', 'stress', 'c3'):
            days = days[::SUBSAMPLE_STEP]
        if tag == 'alt6':
            days = [d for d in days if season == ALT6_SEASON and d in alt6_days]
        if tag == 'pool32':
            import pool_convergence as PC
            keep = {x['day'] for x in PC.selected_days() if x['season'] == season}
            days = [d for d in days if d in keep]
        if a.smoke:
            days = days[:1]
        # longest days first within a season (more remaining games) so the pool stays busy at the end
        jobs += [(season, d, tag, str(out), looks) for d in days]
    todo = [j for j in jobs if not (out / j[0] / f'exposures_{j[1]}.npz').exists()]
    print(f'{len(jobs)} game days in total, {len(jobs) - len(todo)} already done, {len(todo)} to run, '
          f'{a.workers} worker processes. Output: {out}', flush=True)
    _record_environment(out, tag, a.workers, len(todo))
    log = out / 'progress_log.csv'
    new = not log.exists()
    _keep_awake(True)
    t0 = time.time(); n = 0; failed = []
    try:
        with open(log, 'a', newline='', encoding='utf-8') as f, mp.Pool(a.workers, initializer=_init_worker) as pool:
            w = csv.writer(f)
            if new:
                w.writerow(['finished_utc', 'season', 'day', 'status', 'secs', 'worlds', 'precision_met', 'focal'])
            for r in pool.imap_unordered(_job, todo):
                n += 1
                w.writerow([datetime.now(timezone.utc).isoformat(timespec='seconds'), r['season'], r['day'], r['status'],
                            r.get('secs', ''), r.get('worlds', ''), r.get('precision_met', ''), r.get('focal', '')])
                f.flush()
                el = time.time() - t0
                eta = el / n * (len(todo) - n) / 3600
                print(f'[{n}/{len(todo)}] {r["season"]} {r["day"]} {r["status"]} '
                      f'{r.get("secs", "")}s  elapsed {el / 3600:.1f} h, about {eta:.1f} h left'
                      + (f'  ERROR: {r["error"]}' if r['status'] == 'failed' else ''), flush=True)
                if r['status'] == 'failed':
                    failed.append((r['season'], r['day']))
    finally:
        _keep_awake(False)
    if failed:
        print(f'{len(failed)} day(s) FAILED: ' + ', '.join(f'{s} {d}' for s, d in failed)
              + f'\nThe tracebacks are in {out / "errors.log"}. See that file for details.', flush=True)
        sys.exit(1)
    print('ALL DONE' if n == len(todo) else 'stopped early', flush=True)


if __name__ == '__main__':
    mp.freeze_support()
    main()

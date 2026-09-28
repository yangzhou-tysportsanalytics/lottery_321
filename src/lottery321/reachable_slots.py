"""Reachable draft slots per season and rule (registration addendum A1, amendment 9 item 9).

`claims()` in the registered analysis applies each router to uniform random permutations of 1..30, so a
protection is scored as conditional ('some') even when the native can never reach the slots at which the
condition bites. `holds_conditional_other` and `third_party_claim` are selection variables for H3 and H2,
so that dilutes both samples. A1 amendment 9 keeps the registered feature and adds a state-conditional
version as a reported robustness split; this module supplies the slot sets it needs.

Definition (fixed here, before any simulation output was opened): a slot k is *reachable* for team t in a
season under a rule if t occupies slot k in at least one of N simulated worlds started from the FIRST
game day of that season's simulation window. The support of the final standings shrinks as games are
decided, so the first window day gives the widest set: the restriction is the weakest one consistent
with the window, which is the conservative choice for a selection variable.

No simulation output is read. Only the win model, the standings rules and the two lottery procedures are used.
Usage: python reachable_slots.py [worlds=20000] [processes]
"""
import json
import multiprocessing as mp
import sys
from datetime import timedelta
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / 'ledgers'))
import elo as E  # noqa: E402
import simulate as H  # noqa: E402
from teams import TEAMS  # noqa: E402
from standings import conference_orders  # noqa: E402
from league_sim import playin, old_draft, new_draft  # noqa: E402
from cutoff_state import build_state  # noqa: E402

ROOT = HERE.parents[1]
OUT = ROOT / 'results/reachable_slots.json'
SEASONS = ('2020-21', '2021-22', '2022-23', '2023-24', '2024-25', '2025-26')
WORLDS = 20_000
SEED_BASE = 907


def counts_for_season(season, n=WORLDS, seed=None, games=None):
    """Return {'old': (30, 30) int counts, 'new': ...} of how often team t lands at slot k."""
    games = games if games is not None else E.load_games(H.GAMES)
    day = next(iter(H.window_days(games, season)))
    todays = H.window_days(games, season)[day]
    cutoff = min(g['start'] for g in todays) - timedelta(hours=6)
    st = build_state(games, season, cutoff)
    mpn = H.restrictions(H.draft_year(season))
    rng = np.random.default_rng(SEED_BASE if seed is None else seed)
    probs = np.array([p for _, _, p in st['remaining']]); q = st['q']; hg = st['h2h_games_final']
    out = {'old': np.zeros((30, 30), int), 'new': np.zeros((30, 30), int)}
    for _ in range(n):
        w = st['wins'].copy(); h = st['h2h_wins'].copy()
        hw = rng.random(len(probs)) < probs
        for j, (a, b, _) in enumerate(st['remaining']):
            if hw[j]:
                w[a] += 1; h[a, b] += 1
            else:
                w[b] += 1; h[b, a] += 1
        us = rng.random(30); up = rng.random(6); ud = rng.random(30); ul = rng.random(16)
        pl = playin(conference_orders(w, h, hg, us, 'criteria'), up, q)
        for rule, order in (('old', old_draft(w, pl, ud, ul)), ('new', new_draft(w, pl, ud, ul, mpn))):
            out[rule][np.asarray(order), np.arange(30)] += 1
    return {'season': season, 'day': day, 'n': n,
            'old': out['old'].tolist(), 'new': out['new'].tolist()}


def load(path=OUT):
    """{(season, rule): (30, 30) boolean mask, True where the team can reach the slot}."""
    doc = json.loads(Path(path).read_text(encoding='utf-8'))
    return {(r['season'], rule): np.asarray(r[rule], int) > 0 for r in doc['seasons'] for rule in ('old', 'new')}


def _job(args):
    return counts_for_season(*args)


def main(n=WORLDS, procs=None):
    jobs = [(s, n, SEED_BASE + i) for i, s in enumerate(SEASONS)]
    with mp.Pool(procs) as pool:
        rows = pool.map(_job, jobs)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({'worlds': n, 'seed_base': SEED_BASE, 'teams': list(TEAMS),
                               'note': 'slot occupancy counts from the first window day of each season; '
                                       'reachable = count > 0; no simulation output read',
                               'seasons': rows}, indent=1), encoding='utf-8')
    for r in rows:
        o = np.asarray(r['old']) > 0; nw = np.asarray(r['new']) > 0
        print(f"{r['season']} from {r['day']}: mean reachable slots old {o.sum(1).mean():.1f}, new {nw.sum(1).mean():.1f}")


if __name__ == '__main__':
    a = sys.argv[1:]
    main(int(a[0]) if a else WORLDS, int(a[1]) if len(a) > 1 else None)

"""Registration addendum A1, section 5(d): can any of the four remaining ledger assumptions bind at a window state?

Uses ONLY the ledgers' routing conditions, the window states (known results at each cutoff) and the win
model. It simulates final standings, play-in and ONE sampled draft order per rule and world, and records
how often the configuration that an assumption decides is reached. It reads no simulation output and computes
no incentive, stake or holding.

Remaining assumptions (the ASSUMPTIONS of the routers, numbered as in addendum A1, section 5(d)):
  item 3 (2021) HOU/BKN swap choice rule            definitional: HOU gives up its least favorable eligible pick
  item 6 (2024) WAS 13-30 branch of WAS/PHX/MEM      consistent support, not explicit
  item 8 (2025) OKC choice between LAC and HOU swaps definitional: OKC takes the more favorable eligible pick
  item 9 (2026) UTA best-of right order MIN then CLE consistent support, not explicit
Trigger = the native slots fall in a configuration where the alternative reading routes differently.
Decision rule (fixed before running): a robustness re-run under the alternative reading is done for the
window days of an item with P(trigger) >= 0.0015 (half the precision target) under either rule. For the
definitional items the alternative gives the holder a pick it would not choose, so the trigger rate is
reported for transparency only.
Usage: python ledger_assumption_check.py [worlds_per_day=2000] [processes]
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
OUT = ROOT / 'results/ledger_assumption_check.json'
THRESHOLD = 0.0015


def trig_2021_item3(pos):
    """HOU/BKN swap: primary swaps HOU's least favorable eligible pick; alternative swaps only the step-1 pick."""
    if pos['HOU'] <= 4:
        step1 = 'HOU'
    else:
        step1 = max(['OKC', 'MIA', 'HOU'], key=lambda t: pos[t])
    eligible = [step1] + [t for t, lo in (('POR', 15), ('DET', 17)) if pos[t] >= lo]
    worst = max(eligible, key=lambda t: pos[t])
    return worst != step1 and pos['BKN'] < pos[worst]


def trig_2024_item6(pos):
    """WAS pick conveys to NYK (13-30): the branch the sources do not state explicitly."""
    return pos['WAS'] >= 13


def trig_2025_item8(pos):
    """OKC must choose: both LAC and HOU (11-30) picks are eligible and better than OKC's own."""
    return pos['HOU'] >= 11 and pos['LAC'] < pos['OKC'] and pos['HOU'] < pos['OKC']


def trig_2026_item9(pos):
    """UTA best-of (UTA 1-8) with CLE's pick the best of UTA/MIN/CLE: the order MIN-then-CLE decides."""
    return pos['UTA'] <= 8 and pos['CLE'] < min(pos['UTA'], pos['MIN'])


ITEMS = {'2020-21': ('item3', trig_2021_item3, 'definitional'),
         '2023-24': ('item6', trig_2024_item6, 'consistent_support'),
         '2024-25': ('item8', trig_2025_item8, 'definitional'),
         '2025-26': ('item9', trig_2026_item9, 'consistent_support')}

_G = {}


def _init():
    _G['games'] = E.load_games(H.GAMES)


def day_rate(args):
    season, day, n, seed = args
    games = _G['games']
    todays = H.window_days(games, season)[day]
    cutoff = min(g['start'] for g in todays) - timedelta(hours=6)
    st = build_state(games, season, cutoff)
    name, trig, kind = ITEMS[season]
    mpn = H.restrictions(H.draft_year(season))
    rng = np.random.default_rng(seed)
    probs = np.array([p for _, _, p in st['remaining']]); q = st['q']; hg = st['h2h_games_final']
    hits = np.zeros(2)
    for _ in range(n):
        w = st['wins'].copy(); h = st['h2h_wins'].copy()
        hw = rng.random(len(probs)) < probs
        for j, (a, b, _) in enumerate(st['remaining']):
            if hw[j]:
                w[a] += 1; h[a, b] += 1
            else:
                w[b] += 1; h[b, a] += 1
        us = rng.random(30); up = rng.random(6); ud = rng.random(30); ul = rng.random(16)
        orders = conference_orders(w, h, hg, us, 'criteria')
        pl = playin(orders, up, q)
        for r, order in enumerate((old_draft(w, pl, ud, ul), new_draft(w, pl, ud, ul, mpn))):
            pos = {TEAMS[t]: s + 1 for s, t in enumerate(order)}
            hits[r] += trig(pos)
    return {'season': season, 'day': day, 'item': name, 'p_old': float(hits[0] / n), 'p_new': float(hits[1] / n), 'n': n}


def main(n=2000, procs=None):
    games = E.load_games(H.GAMES)
    jobs = []
    for season in ITEMS:
        for day in H.window_days(games, season):
            jobs.append((season, day, n, int(day.replace('-', '')) + 7))
    with mp.Pool(procs, initializer=_init) as pool:
        rows = pool.map(day_rate, jobs)
    summary = {}
    for season, (name, _, kind) in ITEMS.items():
        rs = [r for r in rows if r['season'] == season]
        mx = max(max(r['p_old'], r['p_new']) for r in rs)
        days = [r['day'] for r in rs if max(r['p_old'], r['p_new']) >= THRESHOLD]
        summary[name] = {'season': season, 'kind': kind, 'days': len(rs),
                         'max_p_old': max(r['p_old'] for r in rs), 'max_p_new': max(r['p_new'] for r in rs),
                         'mean_p_old': float(np.mean([r['p_old'] for r in rs])),
                         'mean_p_new': float(np.mean([r['p_new'] for r in rs])),
                         'days_at_or_above_threshold': days,
                         'rerun_required': bool(kind == 'consistent_support' and mx >= THRESHOLD)}
    out = {'date': '2026-09-22', 'worlds_per_day': n, 'threshold': THRESHOLD,
           'note': 'standings/lottery configuration rates only; no simulation output read; no incentive computed',
           'summary': summary, 'by_day': rows}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=1), encoding='utf-8')
    print(json.dumps(summary, indent=1))


if __name__ == '__main__':
    a = sys.argv[1:]
    main(int(a[0]) if a else 2000, int(a[1]) if len(a) > 1 else None)

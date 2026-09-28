"""shared win-probability model: chronological Elo + logistic link fitted on prior seasons only.

Elo parameters are fixed a priori (K=20, home 65 Elo, season regression 0.75,
start 1500) and are NOT tuned on outcomes. The logistic link P(home win)=sigmoid(b0+b1*dElo/400) is
refitted with an expanding window that uses only seasons strictly before the target season.
Input: data/games.csv (verified scores; flags respected).
"""
import csv
import math
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np

TEAMS = ('ATL', 'BKN', 'BOS', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL',
         'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'TOR',
         'UTA', 'WAS')
IDX = {t: i for i, t in enumerate(TEAMS)}
ELO = {'k': 20.0, 'home': 65.0, 'regress': 0.75, 'start': 1500.0}
END_FALLBACK_HOURS = 4  # conservative completion time when no validated end wallclock exists


def utc(s): return datetime.fromisoformat(s.replace('Z', '+00:00'))


def load_games(path):
    rows = []
    for r in csv.DictReader(open(path, encoding='utf-8')):
        if r['standings_use'] != 'counts_for_standings':
            continue
        start = utc(r['start_utc'])
        end = utc(r['end_utc']) if r['end_utc'] else start + timedelta(hours=END_FALLBACK_HOURS)
        rows.append({'game_id': r['game_id'], 'season': r['season'], 'phase': r['phase_2019_20'],
                     'start': start, 'end': end, 'cutoff': utc(r['cutoff6h_utc']),
                     'h': IDX[r['home']], 'a': IDX[r['away']], 'home_win': int(r['winner'] == r['home']),
                     'neutral': r['phase_2019_20'] == 'bubble_seeding'})
    rows.sort(key=lambda g: (g['end'], g['game_id']))
    return rows


def elo_expect(dh):
    return 1.0 / (1.0 + 10 ** (-dh / 400.0))


def run_elo(games, until=None):
    """Replay Elo over games completed strictly before `until` (datetime) or all.
    Returns (ratings array, list of per-game pregame records for replayed games)."""
    r = np.full(30, ELO['start']); season = None; recs = []
    for g in games:
        if until is not None and g['end'] >= until:
            break
        if season is not None and g['season'] != season:
            r = ELO['start'] + ELO['regress'] * (r - ELO['start'])
        season = g['season']
        hca = 0.0 if g['neutral'] else ELO['home']
        d = r[g['h']] - r[g['a']]
        p = elo_expect(d + hca)
        recs.append({**g, 'elo_diff': d, 'p_elo': p})
        delta = ELO['k'] * (g['home_win'] - p)
        r[g['h']] += delta; r[g['a']] -= delta
    return r, recs


def season_start_ratings(games, season):
    """Ratings entering `season`: replay all earlier seasons, then apply the between-season regression."""
    prior = [g for g in games if g['season'] < season]
    r, _ = run_elo(prior)
    if prior:
        r = ELO['start'] + ELO['regress'] * (r - ELO['start'])
    return r


def sigmoid(x): return 1.0 / (1.0 + np.exp(-np.clip(x, -40, 40)))


def fit_link(recs, penalty=1.0):
    """Logistic regression of home_win on [1, elo_diff/400]; neutral-site games excluded."""
    rr = [x for x in recs if not x['neutral']]
    X = np.array([[1.0, x['elo_diff'] / 400.0] for x in rr]); y = np.array([x['home_win'] for x in rr], float)
    b = np.zeros(2); reg = np.diag([0.0, penalty])
    for _ in range(100):
        p = sigmoid(X @ b); H = (X.T * (p * (1 - p))) @ X + reg + 1e-10 * np.eye(2)
        step = np.linalg.solve(H, X.T @ (p - y) + reg @ b); b -= step
        if np.max(np.abs(step)) < 1e-12:
            break
    return b


def link_prob(b, elo_diff, neutral=False):
    x = elo_diff / 400.0
    if neutral:  # remove the home intercept for neutral sites
        return float(sigmoid(b[1] * x))
    return float(sigmoid(b[0] + b[1] * x))


def evaluate(games, seasons):
    """Out-of-season evaluation: link fitted on seasons strictly before each target season."""
    _, recs = run_elo(games)
    out = []
    for s in seasons:
        train = [x for x in recs if x['season'] < s]
        test = [x for x in recs if x['season'] == s and not x['neutral']]
        b = fit_link(train)
        p = np.array([link_prob(b, x['elo_diff']) for x in test]); y = np.array([x['home_win'] for x in test])
        pe = np.array([x['p_elo'] for x in test])
        bins = []
        for lo in np.arange(0, 1, 0.1):
            m = (p >= lo) & (p < lo + 0.1)
            if m.sum():
                bins.append({'bin': f'{lo:.1f}-{lo+0.1:.1f}', 'n': int(m.sum()), 'mean_p': float(p[m].mean()),
                             'win_rate': float(y[m].mean())})
        out.append({'season': s, 'n': len(test), 'coef': [float(v) for v in b],
                    'brier_link': float(np.mean((p - y) ** 2)), 'brier_elo': float(np.mean((pe - y) ** 2)),
                    'brier_home_rate': float(np.mean((np.mean([x['home_win'] for x in train]) - y) ** 2)),
                    'logloss_link': float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))),
                    'home_win_rate': float(y.mean()), 'calibration': bins})
    return out


# ------------------------------------------------------------------ late-season dispersion sensitivity
LATE_WEEKS = 8


def late_window_start(games, season):
    """Start of the last LATE_WEEKS weeks of a season's regular-season schedule (by scheduled start)."""
    from datetime import timedelta
    # 2019-20: the lottery-relevant season ended at the 2020-03-11 hiatus, so use pre-hiatus games only
    last = max(g['start'] for g in games if g['season'] == season and g['phase'] != 'bubble_seeding')
    return last - timedelta(weeks=LATE_WEEKS)


def fit_late_link(games, season, penalty=1.0):
    """Logistic link fitted ONLY on last-LATE_WEEKS-week games of seasons strictly before `season`.
    Elo differences come from the chronological replay (pregame ratings)."""
    _, recs = run_elo([g for g in games if g['season'] < season])
    starts = {s: late_window_start(games, s) for s in {g['season'] for g in recs}}
    late = [x for x in recs if x['start'] >= starts[x['season']] and x['phase'] != 'bubble_seeding']
    if len([x for x in late if not x['neutral']]) < 100:
        return None, len(late)
    return fit_link(late, penalty), len(late)


def favourite_gap(games, seasons):
    """Favourite calibration gap, by season and in the late window.
    For each target season, with the link fitted on earlier seasons and Elo replayed game by game, the favourite
    of a game is the side with the larger link probability; the gap is the favourites' observed win rate minus
    their mean predicted probability, in percentage points, over the whole season and over the late window
    (the last LATE_WEEKS weeks, the paper's sample window). Neutral-site games are excluded."""
    _, recs = run_elo(games)
    out = []
    for s in seasons:
        b = fit_link([x for x in recs if x['season'] < s])
        start = late_window_start(games, s)
        for window in ('season', 'late'):
            sel = [x for x in recs if x['season'] == s and not x['neutral'] and (window == 'season' or x['start'] >= start)]
            p = np.array([link_prob(b, x['elo_diff']) for x in sel]); y = np.array([x['home_win'] for x in sel])
            fav = np.where(p >= 0.5, p, 1 - p); won = np.where(p >= 0.5, y, 1 - y)
            out.append({'season': s, 'window': window, 'games': len(sel), 'predicted': float(fav.mean()),
                        'observed': float(won.mean()), 'gap_pts': float(100 * (won.mean() - fav.mean()))})
    return out

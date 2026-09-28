"""Cutoff states for simulations, built from the verified shared game table.

A game is KNOWN at cutoff c iff its (validated or conservative fallback) end time is < c.
Every other regular-season game of the same season is REMAINING (including games in progress).
Win probabilities come from Elo replayed over games ended before c and the logistic link fitted on
seasons strictly before the target season (elo). Team indices follow teams.TEAMS.
"""
import numpy as np

try:
    from teams import TEAMS
    import elo as E
except ImportError:
    from .teams import TEAMS
    from . import elo as E

TEAM_POS = {t: i for i, t in enumerate(TEAMS)}
A2P = np.array([TEAM_POS[t] for t in E.TEAMS])  # alphabetical index -> TEAMS index


def build_state(games, season, cutoff):
    """games: output of elo.load_games (all seasons). cutoff: aware datetime."""
    season_games = [g for g in games if g['season'] == season]
    if not season_games:
        raise ValueError('unknown season')
    known = [g for g in season_games if g['end'] < cutoff]
    remaining = [g for g in season_games if not g['end'] < cutoff]
    wins = np.zeros(30, int); h2h = np.zeros((30, 30), int); hg = np.zeros((30, 30), int)
    for g in season_games:
        h, a = A2P[g['h']], A2P[g['a']]; hg[h, a] += 1; hg[a, h] += 1
    for g in known:
        h, a = A2P[g['h']], A2P[g['a']]
        if g['home_win']:
            wins[h] += 1; h2h[h, a] += 1
        else:
            wins[a] += 1; h2h[a, h] += 1
    # ratings at cutoff (alphabetical order), with between-season regression if the season has not begun
    prior = [g for g in games if g['end'] < cutoff]
    r, _ = E.run_elo(prior)
    if not known:
        r = E.season_start_ratings(games, season)
    _, recs = E.run_elo([g for g in games if g['season'] < season])
    b = E.fit_link(recs)
    rp = np.zeros(30); rp[A2P] = r  # to TEAMS order
    q = np.zeros((30, 30))
    for i in range(30):
        for j in range(30):
            if i != j:
                q[i, j] = E.link_prob(b, rp[i] - rp[j])
    rem = [(int(A2P[g['h']]), int(A2P[g['a']]), float(q[A2P[g['h']], A2P[g['a']]])) for g in remaining]
    total = hg.sum(1)
    if not np.all(total == total[0]):
        raise ValueError('season game counts differ across teams (irregular season)')
    if wins.sum() != len(known) or len(known) + len(remaining) != len(season_games):
        raise ValueError('conservation failure')
    return {'season': season, 'cutoff': cutoff.isoformat(), 'wins': wins, 'h2h_wins': h2h, 'h2h_games_final': hg,
            'remaining': rem, 'remaining_ids': [g['game_id'] for g in remaining],
            'remaining_start': [g['start'].isoformat() for g in remaining], 'q': q, 'ratings': rp,
            'link': [float(x) for x in b], 'n_known': len(known)}


# ------------------------------------------------------------------ late-season probability sensitivities
STRESS_MULTIPLIER = 1.25  # pre-declared stress value (not estimated from outcomes)


def late_override(state, games, season, mode):
    """Return remaining-game home-win probabilities for a sensitivity run.
    mode 'prior_late_link': games in the target season's last LATE_WEEKS weeks use a link fitted only on
        late-window games of earlier seasons (elo.fit_late_link); earlier games unchanged.
    mode 'stress_slope_x1.25': late-window games use the main link with its slope multiplied by 1.25.
    Returns (probs array aligned with state['remaining'], n_late_games)."""
    from datetime import datetime
    start = E.late_window_start(games, season) if any(g['season'] == season for g in games) else None
    b = np.asarray(state['link'])
    if mode == 'prior_late_link':
        bl, _ = E.fit_late_link(games, season)
        if bl is None:
            raise ValueError('not enough prior late-window games')
    elif mode == 'stress_slope_x1.25':
        bl = np.array([b[0], b[1] * STRESS_MULTIPLIER])
    else:
        raise ValueError('unknown mode')
    rp = np.asarray(state['ratings']); out = []; n_late = 0
    for (h, a, p), st in zip(state['remaining'], state['remaining_start']):
        if start is not None and datetime.fromisoformat(st) >= start:
            out.append(E.link_prob(bl, rp[h] - rp[a])); n_late += 1
        else:
            out.append(p)
    return np.array(out), n_late

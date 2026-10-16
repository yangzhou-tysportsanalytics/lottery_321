"""Exploratory counts, sixth set, from stored outputs only (no new simulation; no registered quantity changes).

  two_kinds      class-B reversals under 3-2-1 for the actual portfolio against the own pick of the same
                 team-game, by league rank at the cutoff (Online Appendix H.30).
  concentration  where the old-rule actual-portfolio reversals fall: by season, team-season and day, and the
                 team-games in which a team held its opponent's pick (Online Appendix H.15).
  example        the example of Section 1 of the paper (Toronto v Indiana, 2024-04-09): how many team-games meet
                 the selection conditions that the team-game table can check, and the cumulative loss-minus-win
                 difference in expected holdings C(j) from the stored day file (Online Appendix H.31). The profile
                 needs simulations/primary/2023-24/exposures_2024-04-09.npz; without that file the stored CSV is
                 left as it is.
Outputs: results/exploratory_6/.  Usage: python exploratory_6.py
"""
import csv
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / 'ledgers'))
import analysis as S  # noqa: E402
from teams import TEAMS  # noqa: E402
from value import CURVES  # noqa: E402

OUT = S.OUT / 'exploratory_6'
BANDS = ['1-3', '4-10', '11-16', '17-30']
EXAMPLE = dict(season='2023-24', day='2024-04-09', team='TOR', opp='IND')
SLOTS = (6, 11, 14, 17, 20, 30)


def write(name, rows):
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / f'{name}.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)


def team_games():
    return pd.read_csv(S.OUT / 'primary' / 'team_games.csv.gz')


def two_kinds(tg):
    """Two kinds of reversal. One row per rank band and one for all team-games."""
    key = ['day', 'game_id', 'team']
    new = tg[tg.rule == 'new']
    a = new[new.portfolio == 'actual'].set_index(key)
    o = new[new.portfolio == 'own'].set_index(key).reindex(a.index)
    old = tg[(tg.rule == 'old') & (tg.portfolio == 'actual')].set_index(key).reindex(a.index)
    ra, ro, rold = a.verdict_B == 'reversal', o.verdict_B == 'reversal', old.verdict_B == 'reversal'
    rows = []
    for band in ['all'] + BANDS:
        m = pd.Series(True, index=a.index) if band == 'all' else (a.band == band)
        own_only = m & ro & ~ra
        rows.append(dict(rank=band, team_games=int(m.sum()), actual_reversals=int((m & ra).sum()),
                         own_pick_reversals=int((m & ro).sum()), both=int((m & ra & ro).sum()),
                         actual_only=int((m & ra & ~ro).sum()),
                         actual_only_and_old_rule_reversal=int((m & ra & ~ro & rold).sum()),
                         own_pick_only=int(own_only.sum()),
                         own_pick_only_actual_unresolved=int((own_only & (a.verdict_B == 'unresolved')).sum()),
                         own_pick_only_actual_negligible=int((own_only & (a.verdict_B == 'negligible')).sum()),
                         own_pick_only_actual_dominance=int((own_only & (a.verdict_B == 'dominance_positive')).sum())))
    return rows


def concentration(tg):
    """Concentration. Counts of the old-rule actual-portfolio reversals."""
    old = tg[(tg.rule == 'old') & (tg.portfolio == 'actual')]
    rev = old[old.verdict_B == 'reversal']
    rows = [dict(quantity='old-rule actual-portfolio reversals', value=len(rev))]
    for s, n in rev.groupby('season').size().items():
        rows.append(dict(quantity=f'reversals in {s}', value=int(n)))
    ts = rev.groupby(['season', 'team']).size().sort_values(ascending=False)
    rows += [dict(quantity='team-seasons with a reversal (of 180)', value=int(len(ts))),
             dict(quantity='days with a reversal (of 312)', value=int(rev.day.nunique())),
             dict(quantity='reversals in the team-season with the most', value=int(ts.iloc[0])),
             dict(quantity='reversals in the team-season with the second most', value=int(ts.iloc[1]))]
    opp = old[old.holds_opponent_pick == 1]
    rows += [dict(quantity="team-games holding the opponent's pick", value=len(opp)),
             dict(quantity='of which reversals', value=int((opp.verdict_B == 'reversal').sum())),
             dict(quantity="team-seasons holding the opponent's pick in some game", value=int(opp.groupby(['season', 'team']).ngroups))]
    return rows


def example_selection(tg):
    """The example, selection. The conditions on ledger entries (number and confidence) are not in the team-game table."""
    key = ['day', 'game_id', 'team']
    old = tg[(tg.rule == 'old') & (tg.portfolio == 'actual')].set_index(key)
    own = tg[(tg.rule == 'old') & (tg.portfolio == 'own')].set_index(key).reindex(old.index)
    c1 = old.verdict_B == 'reversal'
    c2 = c1 & (own.verdict_B != 'reversal')
    c3 = c2 & ((old.holds_opponent_pick == 1) | (old.holds_conditional_other == 1))
    c4 = c3 & (old.holds_pooled_pick == 0)
    ranked = old[c4].assign(abs_tau=lambda x: x.tau_linear.abs()).sort_values('abs_tau', ascending=False)
    pos = [i for i, (d, _, t) in enumerate(ranked.index, 1) if d == EXAMPLE['day'] and t == EXAMPLE['team']]
    return [dict(condition='old-rule actual-portfolio class-B reversal', team_games=int(c1.sum())),
            dict(condition='and the own-pick verdict is not a reversal', team_games=int(c2.sum())),
            dict(condition="and the team holds its opponent's pick or another pick conditionally", team_games=int(c3.sum())),
            dict(condition='and no pooled right', team_games=int(c4.sum())),
            dict(condition='rank of the example among the last set by |linear-curve tau|', team_games=pos[0] if pos else '')]


def example_profile():
    """The example, profile. C(j) of the example team under both rules and both portfolios, from the stored day file."""
    path = S.SIMULATIONS / 'primary' / EXAMPLE['season'] / f"exposures_{EXAMPLE['day']}.npz"
    if not path.exists():
        return None
    d = S.load_day(path); meta = d['meta']
    t = TEAMS.index(EXAMPLE['team'])
    g = [i for i, (h, a) in enumerate(meta['focal_teams']) if t in (h, a)][0]
    home = meta['focal_teams'][g][0] == t
    rows = []
    for name, key in (('actual', 'DB'), ('own pick', 'DB_own')):
        mean = d[key].mean(axis=0)[g]                      # rule, team, slot: holdings(away wins) - holdings(home wins)
        for r, rule in enumerate(('old rule', '3-2-1')):
            dk = mean[r, t] if home else -mean[r, t]       # loss minus win for the example team
            C = np.cumsum(dk)
            row = dict(rule=rule, portfolio=name)
            row.update({f'C_{j}': round(float(C[j - 1]), 4) + 0.0 for j in SLOTS})
            row.update(max_C_slots_1_11=round(float(C[:11].max()), 4) + 0.0, min_C=round(float(C.min()), 4) + 0.0,
                       slot_of_min=int(C.argmin()) + 1)
            row.update({f'tau_{c}': round(float(np.dot(np.asarray(v, float), dk)), 4) for c, v in CURVES.items()})
            rows.append(row)
    return rows


def main():
    tg = team_games()
    write('E6_two_kinds', two_kinds(tg))
    write('E6_concentration', concentration(tg))
    write('E6_example_selection', example_selection(tg))
    prof = example_profile()
    if prof:
        write('E6_example_profile', prof)
    print('wrote', OUT, '' if prof else '(E6_example_profile not rewritten: day file not found)')


if __name__ == '__main__':
    main()

"""Registered robustness reporting (addendum A1 §5 and amendment 11): the four headline quantities for each
robustness run and for the primary run restricted to the same days.

Reads the team-game tables written by analysis for `primary` and each robustness tag, and the
H1/H2 tables of the robustness runs. H1 for the primary run on the subsample is recomputed with the same
rule and the same two-level bootstrap as analysis. Writes
results/robustness_headlines.csv. Prints counts only.
Usage: python robustness_headlines.py dta latelink [stress alt6]
"""
import csv
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / 'ledgers'))
import analysis as S  # noqa: E402
import exploratory_1 as P  # noqa: E402

AN = S.OUT


def h1(tg):
    """H1 on a team-game table: own-pick, ranks 2-5, share significantly negative (linear) new vs old."""
    rows = tg.to_dict('records'); boot = P.boot_for(tg)
    band = lambda x, r: x['portfolio'] == 'own' and x['rule'] == r and 2 <= x['rank'] <= 5
    neg = lambda x: x['sign_linear'] == 'win'
    n1, d1 = S.per_day(rows, boot, neg, lambda x: band(x, 'new'))
    n2, d2 = S.per_day(rows, boot, neg, lambda x: band(x, 'old'))
    pt, lo, hi = boot.diff_of_ratios(n1, d1, n2, d2)
    rev = [x for x in rows if band(x, 'new') and x['verdict_B'] == 'reversal']
    cross = sum(bool(x['crossing']) for x in rev) / max(len(rev), 1)
    return dict(h1_n=int(d1.sum()), h1_diff=pt, h1_lo99=lo, h1_hi99=hi, h1_reversals=len(rev), h1_crossing_share=cross,
                h1_supported=bool(lo > 0 and cross > 0.5))


def main(tags):
    prim = P.load_tg('primary')
    out = []
    for tag in tags:
        tg = P.load_tg(tag) if (AN / tag / 'team_games.csv.gz').exists() else __import__('pandas').read_csv(AN / tag / 'team_games.csv')
        days = set(zip(tg.season, tg.day))
        sub = prim[[(s, d) in days for s, d in zip(prim.season, prim.day)]]
        for label, t in (('primary, same days', sub), (tag, tg)):
            t2 = t[t.rule.isin(['old', 'new'])]
            hd = {r['portfolio']: r for r in P.headline(t2, label=label)}
            row = dict(run=tag, version=label, n_days=len(days), n_team_games=int(hd['actual']['n_team_games']),
                       ha=hd['actual']['diff'], ha_lo=hd['actual']['lo99'], ha_hi=hd['actual']['hi99'],
                       hb=hd['own']['diff'], hb_lo=hd['own']['lo99'], hb_hi=hd['own']['hi99'])
            row.update(h1(t2))
            if label == tag:
                h2 = next(r for r in S_read(AN / tag / 'H2.csv') if r['curve'] == 'linear' and r['sample'] == 'registered')
                row.update(h2_diff=float(h2['mean_diff_new_minus_old']), h2_lo=float(h2['lo99']), h2_hi=float(h2['hi99']),
                           h2_supported=h2['supported'] == 'True')
            out.append(row)
    keys = sorted({k for r in out for k in r}, key=lambda k: list(out[0]).index(k) if k in out[0] else 99)
    with open(AN / 'robustness_headlines.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(out)
    print('wrote', AN / 'robustness_headlines.csv', len(out), 'rows')


def S_read(p):
    with open(p, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


if __name__ == '__main__':
    main(sys.argv[1:] or ['dta', 'latelink'])

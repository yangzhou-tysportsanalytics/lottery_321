"""Exploratory analyses, eighth set (Table 5.3 rows 2-4, Online Appendix H.16 and the note to Table 5.4).

None of these is registered. They were computed after the results were opened, from the stored team-game table
of the primary run, without any new simulation, and none changes a registered table or headline quantity.

  signsize  Table 5.3 and H.16: the registered sign rule classifies a linear-curve tau as negative when its
            pointwise interval (z = 2.935199) excludes zero and is not contained in [-delta, delta]. This part
            reports the two judgements separately for own-pick team-games at league ranks 2-5 (and, for
            reference, ranks 1-3 and all ranks, both portfolios): upper bound below zero; upper bound below
            -delta; upper bound below zero with the interval inside +-delta; and the registered rule. Shares
            under each rule, the 3-2-1 minus old-rule difference with the registered two-level bootstrap
            (9,999 replicates, seed 2026092201), and the season-level 99% t interval over the six seasons
            weighted equally.
  typology  Note to Table 5.4 and H.16: the game typology with participant signs that require the interval to
            lie wholly beyond +-delta, beside the registered typology.

Usage: python exploratory_8.py {signsize|typology|all}
Outputs: results/exploratory_8/
"""
import csv
import sys
from collections import Counter
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / 'ledgers'))

import analysis as S  # noqa: E402
import exploratory_1 as P  # noqa: E402

OUT = S.OUT / 'exploratory_8'
DELTA = 0.003
Z3 = 2.935199
BANDS = (('2-5', 2, 5), ('1-3', 1, 3), ('all', 1, 30))
MEASURES = {
    'registered': lambda m, se: m + Z3 * se < 0 and not (m - Z3 * se > -DELTA and m + Z3 * se < DELTA),
    'upper_below_0': lambda m, se: m + Z3 * se < 0,
    'upper_below_minus_delta': lambda m, se: m + Z3 * se < -DELTA,
    'upper_below_0_inside_delta': lambda m, se: m + Z3 * se < 0 and m - Z3 * se > -DELTA and m + Z3 * se < DELTA,
}
TYPES = {('lose', 'lose'): 'both_lose', ('win', 'win'): 'both_win', ('lose', 'neutral'): 'normal',
         ('lose', 'win'): 'opposed', ('neutral', 'win'): 'one_sided_win'}


def write(name, rows):
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / f'{name}.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)


def season_t(diffs, level=0.99):
    from scipy.stats import t
    d = np.asarray(diffs, float); m = d.mean()
    h = t.ppf(0.5 + level / 2, len(d) - 1) * d.std(ddof=1) / np.sqrt(len(d))
    return m, m - h, m + h


def signsize():
    tg = P.load_tg('primary')
    tg = tg[tg.rule.isin(['old', 'new'])]
    boot = P.boot_for(tg)
    rows = tg.to_dict('records')
    for r in rows:
        for k, f in MEASURES.items():
            r[k] = f(r['tau_linear'], r['se_linear'])
    assert all(r['registered'] == (r['sign_linear'] == 'win') for r in rows), 'registered rule not reproduced'
    seasons = sorted(tg.season.unique())
    out = []
    for pf in ('own', 'actual'):
        for band, lo_r, hi_r in BANDS:
            for k in MEASURES:
                sel = lambda x, rule: x['rule'] == rule and x['portfolio'] == pf and lo_r <= x['rank'] <= hi_r
                n1, d1 = S.per_day(rows, boot, lambda x, k=k: x[k], lambda x: sel(x, 'new'))
                n0, d0 = S.per_day(rows, boot, lambda x, k=k: x[k], lambda x: sel(x, 'old'))
                pt, lo, hi = boot.diff_of_ratios(n1, d1, n0, d0)
                by = [100 * (np.mean([x[k] for x in rows if sel(x, 'new') and x['season'] == s]) -
                             np.mean([x[k] for x in rows if sel(x, 'old') and x['season'] == s])) for s in seasons]
                tm, tlo, thi = season_t(by)
                out.append({'portfolio': pf, 'rank_band': band, 'measure': k, 'team_games': int(d1.sum()),
                            'share_new': 100 * n1.sum() / d1.sum(), 'share_old': 100 * n0.sum() / d0.sum(),
                            'diff': 100 * pt, 'diff_lo99': 100 * lo, 'diff_hi99': 100 * hi,
                            'season_t_lo99': tlo, 'season_t_hi99': min(thi, 100.0),
                            'by_season': ' '.join(f'{v:.1f}' for v in by)})
    write('E8_1_sign_and_size', out)


def strict_sign(m, se):
    if m - Z3 * se > DELTA:
        return 'lose'
    if m + Z3 * se < -DELTA:
        return 'win'
    return 'neutral'


def typology():
    tg = P.load_tg('primary')
    tg = tg[tg.rule.isin(['old', 'new']) & (tg.portfolio == 'actual')]
    out = []
    for rule in ('old', 'new'):
        g = tg[tg.rule == rule]
        strict = [strict_sign(m, se) for m, se in zip(g.tau_linear, g.se_linear)]
        changed = int(sum(a != b for a, b in zip(strict, g.sign_linear)))
        games = {}
        for (key, reg, st) in zip(zip(g.season, g.day, g.game_id), g.sign_linear, strict):
            games.setdefault(key, []).append((reg, st))
        typ = lambda s: TYPES.get(tuple(sorted(s)), 'no_own_stake')
        reg = Counter(typ([a for a, _ in v]) for v in games.values())
        stc = Counter(typ([b for _, b in v]) for v in games.values())
        for t_ in ('both_lose', 'both_win', 'normal', 'opposed', 'one_sided_win', 'no_own_stake'):
            out.append({'rule': rule, 'type': t_, 'games': len(games), 'share_registered': 100 * reg[t_] / len(games),
                        'share_strict': 100 * stc[t_] / len(games), 'signs_changed': changed, 'participants': len(g)})
    write('E8_2_typology_strict', out)


if __name__ == '__main__':
    part = sys.argv[1] if len(sys.argv) > 1 else 'all'
    steps = {'signsize': signsize, 'typology': typology}
    for name in (steps if part == 'all' else [part]):
        steps[name]()
    print('wrote', OUT)

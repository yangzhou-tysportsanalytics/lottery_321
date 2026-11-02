"""Figures of the SSAC27 full paper, drawn from the public repository's result files.

Figure 3 is the repository's own figure function, unchanged (Figure 3.1 of the longer version). Figure 4 redraws
the repository's two-panel summary figure (figures.figure_reversal_by_rank) with the panel titles reworded: the
left panel counts reversals, team-games in which at least one admissible draft-value chart values the loss below
the win, so it says "losing can cost" rather than "losing hurts"; data, layout and colours are unchanged.
Figures 1, 2 and 5 and Table 3 are descriptive displays made for this paper from stored results.

Usage: python3 make_figures.py <repository root> [output folder]
Writes the figures to <output folder>/figures and the derived tables to <output folder>/derived; the default
output folder is ./ssac27_output. In the repository this script is tools/ssac27/make_figures.py and its derived
tables are kept in results/ssac27/.
"""
import sys
from pathlib import Path

import numpy as np
import matplotlib.dates  # noqa: F401

REPO = Path(sys.argv[1]).resolve()
sys.path[:0] = [str(REPO / 'src'), str(REPO / 'src' / 'lottery321')]
from lottery321 import figures as F  # noqa: E402

BASE = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else Path.cwd() / 'ssac27_output'
OUT = BASE / 'figures'
RES = REPO / 'results'


def figure_2(rows, tau_rows, out):
    plt = F.plt
    rows = [r for r in rows if r['value_class'] == 'B' and r['verdict'] == 'reversal']
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.7))
    width = 0.38
    x = np.arange(len(F.BANDS), dtype=float)
    ax = axes[0]
    for k, rule in enumerate(('old', 'new')):
        m = [next(r for r in rows if r['rule'] == rule and r['portfolio'] == 'actual' and r['band'] == b) for b in F.BANDS]
        v = np.array([float(r['share']) for r in m])
        err = np.vstack([v - np.array([float(r['lo99']) for r in m]), np.array([float(r['hi99']) for r in m]) - v])
        p = x + (k - 0.5) * width
        ax.bar(p, v, width, color=F.RULE_COLOUR[rule], label='3-2-1' if rule == 'new' else 'old lottery',
               edgecolor='white', linewidth=0.5)
        ax.errorbar(p, v, yerr=np.clip(err, 0, None), fmt='none', ecolor='#444444', elinewidth=1, capsize=2)
    ax.set_xticks(x, list(F.BANDS), fontsize=8)
    F._style(ax, '', '')
    ax.set_xlabel('league rank at cutoff (1 = worst)', fontsize=8, color='#444444')
    ax.set_title('Games where losing can cost draft value\n(picks actually held)', fontsize=9, color='#222222')
    ax.set_ylabel('share of team-games', fontsize=8, color='#444444')
    ax.set_ylim(0, 0.9)
    ax.yaxis.set_major_formatter(F.matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax.legend(fontsize=8, frameon=False, loc='upper right')
    ax = axes[1]
    tr = [r for r in tau_rows if r['portfolio'] == 'own' and r['curve'] == 'linear']
    for k, rule in enumerate(('old', 'new')):
        m = [next(r for r in tr if r['band'] == b) for b in F.BANDS]
        v = np.array([float(r[f'mean_{rule}']) for r in m])
        lo = np.array([float(r[f'{rule}_lo99']) for r in m]); hi = np.array([float(r[f'{rule}_hi99']) for r in m])
        p = x + (k - 0.5) * width
        ax.bar(p, v, width, color=F.RULE_COLOUR[rule], edgecolor='white', linewidth=0.5)
        ax.errorbar(p, v, yerr=np.vstack([np.clip(v - lo, 0, None), np.clip(hi - v, 0, None)]), fmt='none',
                    ecolor='#444444', elinewidth=1, capsize=2)
    ax.axhline(0, color='#888888', linewidth=0.6)
    ax.set_xticks(x, list(F.BANDS), fontsize=8)
    F._style(ax, '', '')
    ax.set_xlabel('league rank at cutoff (1 = worst)', fontsize=8, color='#444444')
    ax.set_title('Average draft value of losing one game\n(own pick, linear chart)', fontsize=9, color='#222222')
    ax.set_ylabel("share of a No. 1 pick's value", fontsize=8, color='#444444')
    fig.tight_layout()
    return F.save(fig, out, 'ssac_figure_2_by_rank')


# ------------------------------------------------------------------ new for this paper (exploratory, descriptive)
import csv as _csv
import gzip as _gzip
from collections import defaultdict as _dd
import datetime as _dt

DERIVED = BASE / 'derived'

TOR_SLOTS = [6, 11, 14, 17, 20, 30]


def toronto_example():
    """C(j) at the six stored slots and the four-chart draft values for Toronto v Indiana, 2024-04-09, read from
    results/exploratory_6/E6_example_profile.csv (from the stored day file, 32,000 worlds); the own-pick values
    come from results/primary/team_games.csv.gz."""
    C, T = {}, {}
    for r in F.read(RES / 'exploratory_6' / 'E6_example_profile.csv'):
        rule = 'old' if r['rule'] == 'old rule' else 'new'
        port = 'actual' if r['portfolio'] == 'actual' else 'own'
        C[(rule, port)] = [float(r[f'C_{j}']) for j in TOR_SLOTS]
        T[(rule, port)] = {c: float(r[f'tau_{c}']) for c in ('linear', 'concave', 'convex', 'top3_stress')}
        C[(rule, port, 'min')] = (float(r['min_C']), int(float(r['slot_of_min'])) if r['slot_of_min'] else None)
    return C, T


def team_games():
    with _gzip.open(RES / 'primary' / 'team_games.csv.gz', 'rt', encoding='utf-8') as f:
        return list(_csv.DictReader(f))


def figure_1_example(out):
    plt = F.plt
    TOR_C, TT = toronto_example()
    TOR_TAU = {k: v['linear'] for k, v in TT.items()}
    fig = plt.figure(figsize=(7.2, 2.7))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.25, 0.85, 1.15], wspace=0.62)
    # (a) the chain
    ax = fig.add_subplot(gs[0]); ax.axis('off')
    steps = ['Toronto (6th-worst) loses\nat home to Indiana (17th-worst)',
             "Indiana's record improves",
             "Indiana's pick, which Toronto holds\n(top-3 protected), moves later",
             "Toronto's picks lose value:\n5.5% of a No. 1 pick"]
    ys = [0.9, 0.64, 0.38, 0.1]
    for i, (t, y) in enumerate(zip(steps, ys)):
        ax.text(0.5, y, t, ha='center', va='center', fontsize=7.5, color='#222222',
                bbox=dict(boxstyle='round,pad=0.35', fc='#F6F1F1' if i == 3 else '#F2F5F9',
                          ec='#7A1F2B' if i == 3 else '#9AA7B5', lw=0.8))
        if i < 3:
            ax.annotate('', xy=(0.5, ys[i + 1] + 0.1), xytext=(0.5, y - 0.1),
                        arrowprops=dict(arrowstyle='->', color='#555555', lw=0.9))
    ax.set_title('(a) How the loss costs Toronto', fontsize=8.5, color='#222222')
    # (b) the two views
    ax = fig.add_subplot(gs[1])
    x = np.arange(2); w = 0.36
    for k, rule in enumerate(('old', 'new')):
        v = [TOR_TAU[(rule, 'own')], TOR_TAU[(rule, 'actual')]]
        ax.bar(x + (k - 0.5) * w, v, w, color=F.RULE_COLOUR[rule], label='old lottery' if rule == 'old' else '3-2-1',
               edgecolor='white', linewidth=0.5)
    ax.axhline(0, color='#888888', linewidth=0.6)
    ax.set_xticks(x, ['own pick\nonly', 'picks\nheld'], fontsize=7.5)
    F._style(ax, '', '')
    ax.set_ylabel("share of a No. 1 pick", fontsize=7.5, color='#444444')
    ax.tick_params(labelsize=7)
    ax.set_ylim(-0.07, 0.03)
    ax.legend(fontsize=7, frameon=False, loc='upper right')
    ax.set_title('(b) Two views of one game', fontsize=8.5, color='#222222')
    # (c) cumulative holdings change
    ax = fig.add_subplot(gs[2])
    for k, (rule, port, mk) in enumerate((('old', 'actual', 'o'), ('new', 'actual', 'D'), ('old', 'own', 's'))):
        xs = np.array(TOR_SLOTS) + (k - 1) * 0.35
        ax.plot(xs, TOR_C[(rule, port)], linestyle='none', marker=mk, markersize=4.2,
                markerfacecolor=F.RULE_COLOUR[rule] if port == 'actual' else 'white', markeredgecolor=F.RULE_COLOUR[rule],
                label=f"{'old' if rule == 'old' else '3-2-1'}, {'picks held' if port == 'actual' else 'own pick'}")
    ax.axhline(0, color='#888888', linewidth=0.6)
    F._style(ax, 'slot j', 'C(j)', None)
    ax.xaxis.label.set_fontsize(7.5); ax.yaxis.label.set_fontsize(7.5); ax.tick_params(labelsize=7)
    ax.set_xticks(TOR_SLOTS)
    mo, so = TOR_C[('old', 'actual', 'min')]; mn, sn = TOR_C[('new', 'actual', 'min')]
    ax.annotate(f'minimum: {mo:.3f} at slot {so} (old)\n{mn:.3f} at slot {sn} (3-2-1)', xy=(17, mo), xytext=(19.0, -0.30),
                fontsize=6.5, color='#444444', arrowprops=dict(arrowstyle='-', color='#888888', lw=0.6))
    ax.legend(fontsize=6.3, frameon=False, loc='lower left')
    ax.set_title('(c) C(j) at the stored slots', fontsize=8.5, color='#222222')
    return F.save(fig, out, 'ssac_figure_1_example')


def figure_season_view(rows, out, season='2023-24', team='TOR'):
    plt = F.plt
    data = _dd(dict)
    for r in rows:
        if r['season'] == season and r['team'] == team and r['rule'] in ('old', 'new'):
            data[(r['day'], r['opp'])][(r['rule'], r['portfolio'])] = (float(r['tau_linear']), r['verdict_B'])
    keys = sorted(data)
    dates = [_dt.date.fromisoformat(d) for d, _ in keys]
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.6), sharey=True)
    for ax, rule in zip(axes, ('old', 'new')):
        for port, ls in (('actual', '-'), ('own', '--')):
            ys = [data[k][(rule, port)][0] for k in keys]
            ax.plot(dates, ys, ls, color=F.RULE_COLOUR[rule], linewidth=1.3, marker='o' if port == 'actual' else None,
                    markersize=2.5, label='picks held' if port == 'actual' else 'own pick only')
        for k, dte in zip(keys, dates):
            if data[k][(rule, 'actual')][1] == 'reversal':
                y = data[k][(rule, 'actual')][0]
                ax.plot([dte], [y], 'o', markersize=6, markerfacecolor='none', markeredgecolor='#222222', markeredgewidth=0.9)
                left = dte.month == 4
                ax.annotate(f'vs {k[1]}, {dte:%b} {dte.day}', xy=(dte, y), xytext=(-10 if left else 10, -2),
                            textcoords='offset points', ha='right' if left else 'left', va='center',
                            fontsize=6.5, color='#444444')
        ax.axhline(0, color='#888888', linewidth=0.6)
        F._style(ax, '', "draft value of losing\n(share of a No. 1 pick)" if rule == 'old' else '',
                 ('old lottery' if rule == 'old' else '3-2-1') + f', Toronto {season}')
        ax.xaxis.set_major_formatter(F.matplotlib.ticker.FuncFormatter(
            lambda x, _: (lambda d: f'{d:%b} {d.day}')(F.matplotlib.dates.num2date(x))))  # portable: no %-d
        ax.tick_params(labelsize=7); ax.yaxis.label.set_fontsize(7.5); ax.title.set_fontsize(8.5)
        ax.legend(fontsize=7, frameon=False, loc='lower left')
    axes[0].set_ylim(-0.085, 0.045)
    fig.tight_layout()
    return F.save(fig, out, 'ssac_figure_season_view')


def exposure_table(rows, out):
    n = _dd(int); rev = _dd(lambda: {'old': 0, 'new': 0})
    for r in rows:
        if r['portfolio'] != 'actual' or r['rule'] not in ('old', 'new'):
            continue
        key = (r['season'], r['team'])
        if r['rule'] == 'old':
            n[key] += 1
        if r['verdict_B'] == 'reversal':
            rev[key][r['rule']] += 1
    lines = sorted(n, key=lambda k: (-rev[k]['old'], -rev[k]['new'], k))
    out.mkdir(parents=True, exist_ok=True)
    with open(out / 'exposure_by_team_season.csv', 'w', newline='') as f:
        w = _csv.writer(f); w.writerow(['season', 'team', 'team_games', 'reversals_old', 'reversals_321'])
        for k in lines:
            w.writerow([k[0], k[1], n[k], rev[k]['old'], rev[k]['new']])
    return [out / 'exposure_by_team_season.csv']


# Holder and original team for the largest third-party stakes, 2025-26; wording from the 2026 ledger's text fields.
STAKE_LABEL = {
    ('ATL', 'SAS'): 'SAS in ATL games: chained swap, SAS takes the better of SAS/ATL',
    ('POR', 'CHI'): "CHI in POR games: holds POR's pick, top-14 protected",
    ('ORL', 'MEM'): 'MEM in ORL games: takes the best two of MEM, ORL, PHX picks',
    ('LAC', 'OKC'): 'OKC in LAC games: gets the best of OKC, HOU, LAC picks',
    ('HOU', 'PHI'): 'PHI in HOU games: gets the second-best of OKC, HOU, LAC picks',
    ('LAC', 'POR'): "POR in LAC games: POR's own pick owed to CHI, top-14 protected",
    ('LAC', 'CHI'): "CHI in LAC games: holds POR's pick, top-14 protected",
    ('PHI', 'OKC'): "OKC in PHI games: holds PHI's pick, top-4 protected",
}


def figure_stakes_bars(rows, out, season='2025-26', top=8):
    plt = F.plt
    w = _dd(lambda: {'old': 0.0, 'new': 0.0})
    for r in rows:
        if r['season'] == season and r['game_team'] != r['holder']:
            w[(r['game_team'], r['holder'])][r['rule']] += float(r['weight'])
    pairs = sorted(w, key=lambda k: -(w[k]['old'] + w[k]['new']))[:top]
    fig, ax = plt.subplots(figsize=(7.0, 3.0))
    y = np.arange(len(pairs))[::-1]; h = 0.38
    for k, rule in enumerate(('old', 'new')):
        ax.barh(y + (0.5 - k) * h, [w[p][rule] for p in pairs], h, color=F.RULE_COLOUR[rule],
                label='old lottery' if rule == 'old' else '3-2-1', edgecolor='white', linewidth=0.5)
    ax.set_yticks(y, [STAKE_LABEL.get(p, f'{p[1]} in {p[0]} games') for p in pairs], fontsize=7)
    F._style(ax, "summed absolute stake over the window (first pick = 1)", '', None)
    ax.xaxis.label.set_fontsize(7.5); ax.tick_params(axis='x', labelsize=7)
    ax.legend(fontsize=7, frameon=False, loc='lower right')
    fig.tight_layout()
    out.mkdir(parents=True, exist_ok=True)
    with open(DERIVED / 'top_third_party_stakes_2025-26.csv', 'w', newline='') as f:
        wr = _csv.writer(f); wr.writerow(['game_team', 'holder', 'old', 'new'])
        for p in pairs:
            wr.writerow([p[0], p[1], round(w[p]['old'], 4), round(w[p]['new'], 4)])
    return F.save(fig, out, 'ssac_figure_5_stakes')


def main():
    made = []
    made += F.figure_3_1(OUT)
    made += figure_2(F.read(RES / 'primary' / 'T5_2_verdicts_by_band.csv'),
                     F.read(RES / 'exploratory_2' / 'R1_tau_by_band_curves.csv'), OUT)
    made += figure_1_example(OUT)
    tg = team_games()
    made += figure_season_view(tg, OUT)
    made += exposure_table(tg, DERIVED)
    made += figure_stakes_bars(F.read(RES / 'primary' / 'F5_2_network_edges.csv'), OUT)
    print('\n'.join(str(p) for p in made))


if __name__ == '__main__':
    main()

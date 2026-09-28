"""Figures for the paper, built from the registered analysis tables (paper §5).

Inputs are the CSVs written by analysis.run(): F5_1_profiles.csv, F5_2_network_edges.csv,
T5_1_verdicts.csv, T5_2_verdicts_by_band.csv, T5_3_reversal_slot.csv. The module draws nothing from raw
exposure files, so it can be written and tested before any result exists.

Design rules followed: one axis per panel, a colourblind-safe pair (Okabe-Ito blue and vermillion) for the
two rules, line style (solid / dashed) as a second, non-colour encoding for the portfolio, a legend whenever
two or more series are drawn, recessive grid and axes, one sequential hue for the heatmap, and no dual axes.
Usage: python figures.py <analysis_dir> [out_dir]
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.ticker  # noqa: E402,F401
import numpy as np  # noqa: E402

RULE_COLOUR = {'old': '#0072B2', 'new': '#D55E00', 'delta': '#009E73'}   # Okabe-Ito, CVD-safe pair
PORTFOLIO_STYLE = {'actual': '-', 'own': '--'}
GRID = {'color': '#DDDDDD', 'linewidth': 0.6}
LABEL = {'old': 'old rule', 'new': '3-2-1', 'delta': 'difference'}
BANDS = ('1-3', '4-10', '11-16', '17-30')


def read(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def _style(ax, xlabel, ylabel, title=None):
    ax.grid(True, **GRID); ax.set_axisbelow(True)
    for side in ('top', 'right'):
        ax.spines[side].set_visible(False)
    for side in ('left', 'bottom'):
        ax.spines[side].set_color('#888888')
    ax.tick_params(colors='#444444', labelsize=8)
    ax.set_xlabel(xlabel, fontsize=9, color='#222222')
    ax.set_ylabel(ylabel, fontsize=9, color='#222222')
    if title:
        ax.set_title(title, fontsize=10, color='#222222')


def figure_5_1(rows, out, portfolios=('actual', 'own'), bands_rows=None):
    """Mean C(j) profiles by league rank at the cutoff, one panel per rank band on its own vertical scale
    (the four bands differ by an order of magnitude, so a shared scale would hide the rank 1-3
    crossing). Colour = rule, line style = portfolio. Shading is the two-level bootstrap 99% interval on the
    mean when `bands_rows` (exploratory_3/R14_profiles_band.csv) is given, else the 10th-90th percentile
    spread across team-games of the registered F5_1 table."""
    data = defaultdict(dict)
    src = bands_rows or rows
    lo_k, hi_k = ('lo99', 'hi99') if bands_rows else ('q10', 'q90')
    for r in src:
        data[(r['band'], r['rule'], r['portfolio'])][int(r['j'])] = (float(r['mean']), float(r[lo_k]), float(r[hi_k]))
    bands = [b for b in BANDS if any(k[0] == b for k in data)]
    fig, axes = plt.subplots(2, 2, figsize=(7.0, 5.6))
    axes = axes.ravel()
    for ax, band in zip(axes, bands):
        for rule in ('old', 'new'):
            for pf in portfolios:
                d = data.get((band, rule, pf))
                if not d:
                    continue
                js = sorted(d); m = [d[j][0] for j in js]
                ax.plot(js, m, PORTFOLIO_STYLE[pf], color=RULE_COLOUR[rule], linewidth=1.8,
                        label=f'{LABEL[rule]}, {"actual portfolio" if pf == "actual" else "own pick only"}')
                ax.fill_between(js, [d[j][1] for j in js], [d[j][2] for j in js],
                                color=RULE_COLOUR[rule], alpha=0.10 if pf == 'actual' else 0.06, linewidth=0)
        ax.axhline(0, color='#888888', linewidth=0.9)
        ax.axvline(11.5, color='#BBBBBB', linewidth=0.8, linestyle=':')
        ax.set_xlim(1, 30); ax.set_xticks([1, 5, 9, 12, 15, 20, 25, 30])
        _style(ax, 'slot j', 'mean C(j)', f'league rank {band} at the cutoff')
    for ax in axes[len(bands):]:
        ax.set_visible(False)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center', ncol=2, fontsize=8, frameon=False)
    fig.tight_layout(rect=(0, 0.09, 1, 1))
    return save(fig, out, 'figure_5_1_profiles')


def figure_5_2(rows, out, season=None, top=12):
    """Stakes network, old rule and 3-2-1 side by side: rows = teams playing, columns = stake holders, the
    same twelve teams in the same order in both panels (the twelve with the largest summed stake under the
    two rules together), one colour scale, and the diagonal (a team's stake in its own games) left blank."""
    rows = [r for r in rows if season is None or r['season'] == season]
    if not rows:
        raise ValueError('no edges for this season')
    weight = {'old': defaultdict(float), 'new': defaultdict(float)}
    for r in rows:
        weight[r['rule']][(r['game_team'], r['holder'])] += float(r['weight'])
    teams = sorted({t for w in weight.values() for (a, b) in w for t in (a, b)})
    strength = {t: sum(v for w in weight.values() for (a, b), v in w.items() if t in (a, b) and a != b) for t in teams}
    keep = sorted(teams, key=lambda t: -strength[t])[:top]      # ordered by summed stake, largest first
    mats = {}
    for rule in ('old', 'new'):
        M = np.array([[weight[rule].get((a, b), 0.0) for b in keep] for a in keep])
        np.fill_diagonal(M, np.nan)
        mats[rule] = M
    vmax = max(np.nanmax(M) for M in mats.values())
    # Sized so that, printed at 0.9 of a 6-inch text width, tick labels are about 8 pt.
    fig, axes = plt.subplots(1, 2, figsize=(0.27 * len(keep) * 2 + 2.6, 0.27 * len(keep) + 1.5))
    cmap = plt.get_cmap('Blues').copy(); cmap.set_bad('#D9D9D9')
    fs = 12
    for ax, rule in zip(axes, ('old', 'new')):
        im = ax.imshow(mats[rule], cmap=cmap, origin='upper', vmin=0, vmax=vmax)
        ax.set_xticks(range(len(keep)), keep, rotation=90, fontsize=fs)
        ax.set_yticks(range(len(keep)), keep, fontsize=fs)
        _style(ax, 'stake holder', 'team playing' if rule == 'old' else '', LABEL[rule] + (f', {season}' if season else ''))
        ax.xaxis.label.set_fontsize(fs); ax.yaxis.label.set_fontsize(fs); ax.title.set_fontsize(fs + 1)
        ax.grid(False)
    cb = fig.colorbar(im, ax=axes, fraction=0.025, pad=0.03)
    cb.set_label('summed |stake| over the window', fontsize=fs - 1)
    cb.ax.tick_params(labelsize=fs)
    return save(fig, out, 'figure_5_2_network' + (f'_{season}' if season else ''))


def figure_verdict_shares(rows, out, value_class='B', portfolio='actual'):
    """Verdict shares by band and rule, with the bootstrap interval as an error bar."""
    rows = [r for r in rows if r['value_class'] == value_class and r['portfolio'] == portfolio]
    verdicts = ['dominance_positive', 'reversal', 'negligible', 'unresolved']
    bands = [b for b in BANDS if any(r.get('band') == b for r in rows)] or ['all']
    fig, ax = plt.subplots(figsize=(2.2 * len(bands) + 2.0, 3.4))
    width = 0.38
    x = np.arange(len(verdicts) * len(bands), dtype=float)
    for k, rule in enumerate(('old', 'new')):
        vals, los, his, pos = [], [], [], []
        for bi, band in enumerate(bands):
            for vi, v in enumerate(verdicts):
                m = [r for r in rows if r['rule'] == rule and r['verdict'] == v
                     and (r.get('band', 'all') or 'all') == band]
                if not m:
                    continue
                vals.append(float(m[0]['share'])); los.append(float(m[0]['lo99'])); his.append(float(m[0]['hi99']))
                pos.append(bi * len(verdicts) + vi)
        p = np.array(pos, float) + (k - 0.5) * width
        v = np.array(vals); err = np.vstack([v - np.array(los), np.array(his) - v])
        ax.bar(p, v, width, color=RULE_COLOUR[rule], label=LABEL[rule], edgecolor='white', linewidth=0.5)
        ax.errorbar(p, v, yerr=np.clip(err, 0, None), fmt='none', ecolor='#444444', elinewidth=1, capsize=2)
    ticks = [bi * len(verdicts) + vi for bi in range(len(bands)) for vi in range(len(verdicts))]
    short = {'dominance_positive': 'dom.\npositive', 'reversal': 'reversal', 'negligible': 'negli-\ngible',
             'unresolved': 'unre-\nsolved'}
    ax.set_xticks(ticks, [short[v] for _ in bands for v in verdicts], fontsize=7)
    for bi, band in enumerate(bands[:-1]):
        ax.axvline(bi * len(verdicts) + len(verdicts) - 0.5, color='#CCCCCC', linewidth=1)
    for bi, band in enumerate(bands):
        ax.text(bi * len(verdicts) + (len(verdicts) - 1) / 2, 1.02, f'rank {band}', ha='center',
                fontsize=8, color='#444444', transform=ax.get_xaxis_transform())
    _style(ax, '', f'share of team-games (class {value_class})')
    ax.set_ylim(0, 1.08)
    ax.legend(fontsize=8, frameon=False, loc='upper right', bbox_to_anchor=(1.0, 0.97))
    fig.tight_layout()
    return save(fig, out, f'figure_verdict_shares_class{value_class}_{portfolio}')


def figure_reversal_by_rank(rows, out, value_class='B', tau_rows=None):
    """Summary figure. Left: reversal share by league rank at the cutoff for the rights actually
    held, old lottery against 3-2-1, with 99% intervals (frequency). Right, when `tau_rows` (the by-band mean
    linear-curve tau, exploratory table R1) is given: mean own-pick incentive to lose by rank under both rules,
    with 99% intervals (magnitude), so that the compression at ranks 4-10 and the rise at ranks 17-30 are
    visible beside the reversal counts. Panel titles are in plain language."""
    rows = [r for r in rows if r['value_class'] == value_class and r['verdict'] == 'reversal']
    two = tau_rows is not None
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.6))
    width = 0.38
    x = np.arange(len(BANDS), dtype=float)
    ax = axes[0]
    for k, rule in enumerate(('old', 'new')):
        m = [next(r for r in rows if r['rule'] == rule and r['portfolio'] == 'actual' and r['band'] == b) for b in BANDS]
        v = np.array([float(r['share']) for r in m])
        err = np.vstack([v - np.array([float(r['lo99']) for r in m]), np.array([float(r['hi99']) for r in m]) - v])
        p = x + (k - 0.5) * width
        ax.bar(p, v, width, color=RULE_COLOUR[rule], label=LABEL[rule] if rule == 'new' else 'old lottery',
               edgecolor='white', linewidth=0.5)
        ax.errorbar(p, v, yerr=np.clip(err, 0, None), fmt='none', ecolor='#444444', elinewidth=1, capsize=2)
    ax.set_xticks(x, [f'{b}' for b in BANDS], fontsize=8)
    _style(ax, '', '')
    ax.set_xlabel('league rank at cutoff (1 = worst)', fontsize=8, color='#444444')
    ax.set_title('Games where losing hurts (picks actually held)', fontsize=9, color='#222222')
    ax.set_ylabel('share of team-games', fontsize=8, color='#444444')
    ax.set_ylim(0, 0.9)
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax.legend(fontsize=8, frameon=False, loc='upper right')
    ax = axes[1]
    if two:
        tr = [r for r in tau_rows if r['portfolio'] == 'own' and r['curve'] == 'linear']
        for k, rule in enumerate(('old', 'new')):
            m = [next(r for r in tr if r['band'] == b) for b in BANDS]
            v = np.array([float(r[f'mean_{rule}']) for r in m])
            lo = np.array([float(r[f'{rule}_lo99']) for r in m]); hi = np.array([float(r[f'{rule}_hi99']) for r in m])
            p = x + (k - 0.5) * width
            ax.bar(p, v, width, color=RULE_COLOUR[rule], edgecolor='white', linewidth=0.5)
            ax.errorbar(p, v, yerr=np.vstack([np.clip(v - lo, 0, None), np.clip(hi - v, 0, None)]), fmt='none',
                        ecolor='#444444', elinewidth=1, capsize=2)
        ax.axhline(0, color='#888888', linewidth=0.6)
        ax.set_xticks(x, [f'{b}' for b in BANDS], fontsize=8)
        _style(ax, '', '')
        ax.set_xlabel('league rank at cutoff (1 = worst)', fontsize=8, color='#444444')
        ax.set_title('Average reward to losing, own pick', fontsize=9, color='#222222')
        ax.set_ylabel('share of a No. 1 pick\'s value', fontsize=8, color='#444444')
    else:
        ax.set_visible(False)
    fig.tight_layout()
    return save(fig, out, f'figure_reversal_by_rank_class{value_class}')


# ------------------------------------------------------------------ Section 3 (exact, no simulation)
def figure_3_1(out):
    """The 3-2-1 relegation boundary, from the exact kernels of theory (Proposition 1 of the paper).

    Left: F_r(j) - F_{r+1}(j) at the 3|4 boundary, the only non-monotone adjacent pair. Negative up to
    slot 11 and positive at 12 to 15, which is the crossing the floor creates.
    Right: expected slot by position under both rules."""
    import theory as TH
    K = TH.position_kernels()
    Fn = np.cumsum(K['new'], axis=1)
    diff = Fn[2] - Fn[3]
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.2))
    ax = axes[0]
    colours = ['#D55E00' if d < 0 else '#0072B2' for d in diff]
    ax.bar(np.arange(1, len(diff) + 1), diff, color=colours, width=0.72, edgecolor='white', linewidth=0.5)
    ax.axhline(0, color='#888888', linewidth=1)
    ax.axvline(11.5, color='#444444', linewidth=1, linestyle=':')
    ax.annotate('pick-12 floor', xy=(11.8, min(diff) * 0.85), fontsize=8, color='#444444')
    _style(ax, 'slot j', 'F(j | position 3) - F(j | position 4)',
           'Relegation boundary under 3-2-1')
    ax = axes[1]
    for rule, K_ in (('old', K['old']), ('new', K['new'])):
        exp = (K_ * np.arange(1, K_.shape[1] + 1)).sum(axis=1)
        ax.plot(np.arange(1, len(exp) + 1), exp, '-o', color=RULE_COLOUR[rule], linewidth=2,
                markersize=4, label=LABEL[rule])
    ax.axvspan(0.5, 3.5, color='#D55E00', alpha=0.08, linewidth=0)
    ax.annotate('relegated', xy=(2, ax.get_ylim()[1] * 0.96), ha='center', fontsize=8, color='#444444')
    _style(ax, 'position (worst = 1)', 'expected slot', 'Expected slot by position')
    ax.legend(fontsize=8, frameon=False)
    fig.tight_layout()
    return save(fig, out, 'figure_3_1_kernels')


def save(fig, out, stem):
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    paths = []
    for ext in ('pdf', 'png'):
        p = out / f'{stem}.{ext}'
        fig.savefig(p, dpi=200, bbox_inches='tight')
        paths.append(p)
    plt.close(fig)
    return paths


def main(analysis_dir, out_dir=None):
    a = Path(analysis_dir); out = Path(out_dir) if out_dir else a / 'figures'
    made = []
    made += figure_3_1(out)
    bands = a.parent / 'exploratory_3' / 'R14_profiles_band.csv'
    made += figure_5_1(read(a / 'F5_1_profiles.csv'), out, bands_rows=read(bands) if bands.exists() else None)
    made += figure_verdict_shares(read(a / 'T5_2_verdicts_by_band.csv'), out)
    edges = a / 'F5_2_network_edges.csv'
    if edges.exists():
        for s in sorted({r['season'] for r in read(edges)}):
            made += figure_5_2(read(edges), out, season=s)
    print('\n'.join(str(p) for p in made))


if __name__ == '__main__':
    main(*sys.argv[1:3])

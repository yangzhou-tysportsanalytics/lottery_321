"""Appendix C of the paper: every registered table that the body does not carry (A1 amendment 11).

Formats the CSVs written by analysis (primary, primary_asrun_boott, primary_precise_only, norestr
and the primary-norestr comparison) as markdown tables. Nothing is recomputed; a table whose input is
missing is emitted as a pending marker so that the gap is visible in the manuscript.
Usage: python appendix_c_tables.py [--analysis DIR] [--out FILE]
"""
import argparse
import csv
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ANALYSIS = ROOT / 'results'
OUT = ROOT / 'results/appendix_c_tables.md'

RULE = {'old': 'old rule', 'new': '3-2-1', 'delta': 'ΔC'}
PF = {'actual': 'actual', 'own': 'own pick'}
VERD = ('dominance_positive', 'negligible', 'reversal', 'unresolved')
VL = {'dominance_positive': 'dom.-pos.', 'negligible': 'negligible', 'reversal': 'reversal', 'unresolved': 'unresolved'}
CURVES = ('linear', 'concave', 'convex', 'top3_stress')
CL = {'linear': 'linear', 'concave': 'concave', 'convex': 'convex', 'top3_stress': 'top-3'}
RUN = {'dta': 'draw-then-adjust', 'latelink': 'late-window link', 'stress': 'slope ×1.25', 'alt6': '2023-24 ledger reading'}
BANDS = ('all', '1-3', '4-10', '11-16', '17-30')


def read(p):
    p = Path(p)
    if not p.exists():
        raise FileNotFoundError(p)
    with open(p, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def pct(x, d=1):
    return f'{100 * float(x):.{d}f}'


def f4u(x):
    v = abs(float(x))
    return '0.0000' if v < 5e-5 else f'{v:.4f}'


def f4(x):
    v = float(x)
    return '0.0000' if abs(v) < 5e-5 else f'{v:+.4f}'.replace('-', '−')


def ci(share, lo, hi, n=None):
    """A share with its interval; an interval with no bootstrap variation is shown as a count, since '[0.0, 0.0]' reads as a precise zero rather than as the absence of any case."""
    if float(lo) == float(hi):
        if n is not None:
            k = round(float(share) * int(n))
            return f'{pct(share)} ({k:,} of {int(n):,}; no variation)'
        return f'{pct(share)} (no variation)'
    return f'{pct(share)} [{pct(lo)}, {pct(hi)}]'


def p2(x):
    """Percentage points to two decimals, with no negative zero."""
    v = round(100 * float(x), 2)
    return f'{v + 0.0:.2f}'.replace('-', '−') if v != 0 else '0.00'


def dci(diff, lo, hi):
    """A difference of shares in points; a degenerate interval means no team-game changed its reversal status."""
    if float(lo) == float(hi) == float(diff):
        return f'{p2(diff)} (no reversal verdict changed)'
    return f'{p2(diff)} [{p2(lo)}, {p2(hi)}]'


def table(header, rows):
    out = ['| ' + ' | '.join(header) + ' |', '|' + '---|' * len(header)]
    out += ['| ' + ' | '.join(str(c) for c in r) + ' |' for r in rows]
    return out + ['']


def pending(what):
    return [f'\\pending{{{what}}}', '']


def c1(A):
    out = ['**Table C.1. Run diagnostics.** Counts of states by the look at which they stopped, precision, and '
           'the noise diagnostics of Section 5.0. Conservation checks are maxima of absolute deviations over all states.', '']
    keys = [('states', 'states'), ('games', 'focal games'), ('stopped_2000', 'met the target at 2,000 worlds'),
            ('stopped_8000', 'met the target at 8,000'), ('stopped_32000', 'met the target at 32,000'),
            ('missed_target', 'missed the target'), ('max_halfwidth_linear', 'max half-width, linear τ'),
            ('p95_halfwidth_linear', '95th pct half-width, linear τ'), ('max_halfwidth_delta_linear', 'max half-width, Δτ'),
            ('max_q_total_dev', 'slot-total conservation'), ('max_own_slot_dev', 'own-slot conservation'),
            ('max_per_slot_dev', 'per-slot check (noise diagnostic)'), ('per_slot_noise_scale', 'reference scale 1/√(draws·worlds)'),
            ('max_zero_sum_dev', 'league zero-sum, max over curves')]
    runs = [('primary', 'primary'), ('norestr', 'no restrictions')]
    d = {t: read(A / t / 'T5_0_diagnostics.csv')[0] for t, _ in runs}

    def fmt(k, v):
        v = float(v)
        return f'{int(v):,}' if k in ('states', 'games') or k.startswith('stopped') or k == 'missed_target' else f'{v:.4f}' if v >= 1e-4 or v == 0 else f'{v:.1e}'
    out += table(['quantity'] + [l for _, l in runs], [[lab] + [fmt(k, d[t][k]) for t, _ in runs] for k, lab in keys])
    z = read(A / 'primary' / 'T5_0b_zero_sum_by_curve.csv')
    out += ['*League zero-sum deviation by curve, primary run.*', '']
    out += table(['curve', 'rule', 'max', 'mean'], [[CL[r['curve']], RULE[r['rule']], f"{float(r['max_zero_sum_dev']):.4f}",
                                                     f"{float(r['mean_zero_sum_dev']):.5f}"] for r in z])
    return out


def c2(A):
    rows = read(A / 'primary' / 'T5_0c_verdict_by_look.csv')
    agg = defaultdict(int)
    for r in rows:
        agg[(r['rule'], r['portfolio'], r['stopped_at'], r['verdict_B'])] += int(r['count'])
    looks = ('2000', '8000', '32000', 'missed')
    out = ['**Table C.2. Verdicts against the look a day stopped at, and band width (primary run, class B).** Counts of '
           'team-games. The band-width ratio is c·max_j se(j)/δ; the precision-matched ratio restates it at the '
           'smallest world count among all days, n★: standard errors are multiplied by √(n/n★) (Section 4.5).', '']
    body = []
    for r in ('old', 'new', 'delta'):
        for pf in ('actual', 'own'):
            for lk in looks:
                cnt = [agg.get((r, pf, lk, v), 0) for v in VERD]
                if sum(cnt):
                    body.append([RULE[r], PF[pf], 'missed target' if lk == 'missed' else f'{int(lk):,}'] + cnt)
    out += table(['rule', 'portfolio', 'stopped at'] + [VL[v] for v in VERD], body)
    bw = read(A / 'primary' / 'T5_0d_band_width.csv')
    out += ['*Band-width ratio c·max_j se(j)/δ across team-games, registered and precision-matched.*', '']
    out += table(['rule', 'portfolio', 'measure', 'q25', 'median', 'q75', 'q90'],
                 [[RULE[r['rule']], PF[r['portfolio']], 'registered' if r['measure'] == 'band_ratio' else 'precision-matched',
                   f"{float(r['q25']):.2f}", f"{float(r['median']):.2f}", f"{float(r['q75']):.2f}", f"{float(r['q90']):.2f}"]
                  for r in bw])
    return out


def verdict_block(rows, classes, title):
    out = [title, '']
    body = []
    for vc in classes:
        for r in ('old', 'new', 'delta'):
            for pf in ('actual', 'own'):
                sel = {x['verdict']: x for x in rows if x['rule'] == r and x['portfolio'] == pf and x['value_class'] == vc}
                if not sel:
                    continue
                body.append([vc, RULE[r], PF[pf]] + [ci(sel[v]['share'], sel[v]['lo99'], sel[v]['hi99'], sel[v].get('n')) for v in VERD])
    return out + table(['class', 'rule', 'portfolio'] + [VL[v] for v in VERD], body)


def c3(A):
    return verdict_block(read(A / 'primary' / 'T5_1_verdicts.csv'), ('B_pm', 'C_pm'),
                         '**Table C.3. Verdict shares, precision-matched (%, 99% two-level bootstrap intervals).** Every '
                         'day\'s standard errors are multiplied by √(n/n★), n★ the smallest world count among the days '
                         'compared (Section 4.5); "B_pm" and "C_pm" are the class-B and class-C verdicts so restated. The '
                         'factor is the same for both portfolios on a day, so it does not align the extra Monte Carlo noise '
                         'of pooled rights (Online Appendix F.3).')


def c4(A):
    return verdict_block(read(A / 'primary_asrun_boott' / 'T5_1_verdicts.csv'), ('B',),
                         '**Table C.4. Verdict shares with the studentised bootstrap-t band as run (%, class B).** The band '
                         'of A1 amendment 9, before amendment 12 returned to the multiplier band. It degenerates on '
                         'coordinates that are zero in most super-batches, which inflates the unresolved share. The reversal '
                         'shares, (H-a) and (H-b) keep their sign and significance under both bands, with '
                         'different values; the H1 difference and H2 do not use the band and are unchanged (Table 5.7, '
                         'Online Appendix H.2). The dominance-positive and unresolved shares and the ΔC reversal share '
                         'change substantially in size. The as-run band was applied to the whole primary run, of which '
                         'this table, Table 5.2 by rank band (Online Appendix Table H.3), the headline quantities (Table 5.7; Online Appendix H.2) and the verdict changes (H.16) are printed; it was not applied to the robustness runs '
                         'or to the C3 decomposition, so Tables 5.6, C.10, C.12, C.15–C.17 and H3 exist under the multiplier band only.')


def c5(A):
    t = read(A / 'primary' / 'T5_curves_and_T5_6_delta.csv')
    out = ['**Table C.5. Curve-specific incentive τ on the four value curves.** Panel A: all team-games. Mean, median and the '
           'share significantly positive or negative (pointwise 99% interval at the three-look constant z = 2.935199). '
           'Rows Δτ give τ_new − τ_old.', '', '*Panel A*', '']
    body = []
    for r in ('old', 'new', 'delta'):
        for pf in ('actual', 'own'):
            for cv in CURVES:
                x = [y for y in t if y['rule'] == r and y['portfolio'] == pf and y['band'] == 'all' and y['curve'] == cv]
                if x:
                    x = x[0]
                    body.append([{'delta': 'Δτ'}.get(r, RULE[r]), PF[pf], CL[cv], f4(x['mean']), f4(x['median']),
                                 pct(x['share_sig_pos']), pct(x['share_sig_neg'])])
    out += table(['rule', 'portfolio', 'curve', 'mean', 'median', '% > 0', '% < 0'], body)
    out += ['*Panel B: Δτ = τ_new − τ_old by league rank at the cutoff, linear curve (the columns that Table 5.4 omits).*', '']
    body = []
    for b in BANDS:
        for pf in ('actual', 'own'):
            x = [y for y in t if y['rule'] == 'delta' and y['portfolio'] == pf and y['band'] == b and y['curve'] == 'linear']
            if x:
                x = x[0]
                body.append([b, PF[pf], x['n'], f4(x['mean']), f4(x['median']), f'[{f4(x["q25"])}, {f4(x["q75"])}]',
                             pct(x['share_sig_neg']), pct(x['share_sig_pos'])])
    return out + table(['rank', 'portfolio', 'n', 'mean', 'median', 'IQR', '% < 0', '% > 0'], body)


def c6(A):
    out = ['**Table C.6. Attribution.** Panel A: the portfolio effect $τ(\\text{actual}) − τ(\\text{own pick only})$, linear curve. '
           'Panel B: class-B reversal share by seeding stake (total-variation distance of end-of-season status '
           'between the branches). Panel C: class-B reversal share by ledger feature, registered and state-conditional.', '',
           '*Panel A*', '']
    pe = read(A / 'primary' / 'T5_attr_portfolio_effect.csv')
    lab = {'old': 'old rule', 'new': '3-2-1', 'delta': '3-2-1 − old'}
    out += table(['rule', 'rank', 'n', 'mean', 'median', 'q90', 'share \\|effect\\| ≥ δ'],
                 [[lab[r['rule']], r['band'], r['n'], f4(r['mean']), f4(r['median']), f4(r['q90']), pct(r['share_nonzero'])] for r in pe])
    out += ['*Panel B*', '']
    sd = [r for r in read(A / 'primary' / 'T5_attr_seeding.csv') if r['value_class'] == 'B' and r['verdict'] == 'reversal']
    out += table(['rule', 'portfolio', 'seeding stake', 'n', 'reversal share'],
                 [[RULE[r['rule']], PF[r['portfolio']], r['seed_group'], r['n'],
                   ci(r['share'], r['lo99'], r['hi99'], r['n'])] for r in sd])
    out += ['*Panel C*', '']
    lf = read(A / 'primary' / 'T5_attr_ledger_features.csv')
    out += table(['rule', 'feature', 'value', 'n', 'reversal share'],
                 [[RULE[r['rule']], r['feature'].replace('_', ' '), {'True': 'yes', 'False': 'no'}.get(r['value'], r['value']), r['n'],
                   ci(r['reversal_share'], r['lo99'], r['hi99'], r['n'])] for r in lf])
    return out


def c7(A):
    t = read(A / 'primary' / 'T5_7_rollover.csv')
    out = ['**Table C.7. The mass channel under the rollover valuation (A1 amendment 10), linear curve.** Mean τ_ρ = '
           'τ − ρv̄M and the share of team-games whose sign differs from ρ = 0. At ρ > 0 the valuation lies outside '
           'the registered class 𝒱_B (Section 3.2); the numbers are magnitudes, not verdicts.', '']
    body = []
    for r in ('old', 'new'):
        for pf in ('actual', 'own'):
            for b in BANDS:
                sel = {x['rho']: x for x in t if x['rule'] == r and x['portfolio'] == pf and x['band'] == b
                       and x['curve'] == 'linear' and x['measure'] == 'tau'}
                if not sel:
                    continue
                body.append([RULE[r], PF[pf], b] + [f4(sel[k]['mean']) for k in ('0.0', '0.5', '0.8')]
                            + [pct(sel['0.8']['share_sign_flip'])])
    return out + table(['rule', 'portfolio', 'rank', 'ρ = 0', 'ρ = 0.5', 'ρ = 0.8', '% sign change at 0.8'], body)


def c8(A):
    t = read(A / 'primary' / 'T5_6_transitions.csv')
    out = ['**Table C.8. Verdict transitions, old rule → 3-2-1, class B (counts of team-games).**', '']
    body = []
    for pf in ('actual', 'own'):
        for o in VERD:
            body.append([PF[pf], VL[o]] + [sum(int(x['count']) for x in t if x['portfolio'] == pf and x['old'] == o and x['new'] == n)
                                           for n in VERD])
    return out + table(['portfolio', 'old rule \\ 3-2-1'] + [VL[v] for v in VERD], body)


def c9(A):
    ty = read(A / 'primary' / 'T5_4_typology.csv')
    sd = read(A / 'primary' / 'T5_5_stakes_distribution.csv')
    types = ('both_lose', 'normal', 'no_own_stake', 'opposed', 'one_sided_win', 'both_win')
    out = ['**Table C.9. The stakes network on all four curves.** Panel A: typology shares (%). Panel B: '
           'third-party share TP over materially staked teams (median, and mean in brackets).', '', '*Panel A*', '']
    body = []
    for cv in CURVES:
        for r in ('old', 'new'):
            sel = {x['type']: x for x in ty if x['curve'] == cv and x['rule'] == r}
            body.append([CL[cv], RULE[r]] + [pct(sel[k]['share']) if k in sel else '—' for k in types])
    out += table(['curve', 'rule', 'both prefer to lose', 'one-sided lose', 'no own stake', 'opposed', 'one-sided win', 'both prefer to win'], body)
    out += ['*Panel B*', '']
    body = []
    for cv in CURVES:
        row = [CL[cv]]
        for r in ('old', 'new', 'new_minus_old'):
            x = [y for y in sd if y['curve'] == cv and y['rule'] == r and y['measure'] == 'tp_share']
            row.append(f"{float(x[0]['median']):.3f} [{float(x[0]['mean']):.3f}], n = {int(x[0]['n']):,}" if x else '—')
        body.append(row)
    out += table(['curve', 'old rule', '3-2-1', '3-2-1 − old (paired)'], body) + [
        'n is the number of games in which TP is defined (under both rules, for the paired difference). '
        '"One-sided lose" is the registered type *normal*.', '']
    h2 = read(A / 'primary' / 'H2.csv')
    out += ['*Panel C: H2 on the four curves and both samples (paired difference in the mean absolute third-party '
            'stake, 3-2-1 − old).* The linear curve on the registered sample is the registered test (Table 5.5).', '']
    out += table(['curve', 'sample', 'games', 'mean difference', '99% CI', 'positive, CI excludes 0'],
                 [[CL[r['curve']], r['sample'].replace('_', '-'), r['n_games'], f"{float(r['mean_diff_new_minus_old']):+.5f}",
                   f"[{float(r['lo99']):+.5f}, {float(r['hi99']):+.5f}]", 'yes' if r['supported'] == 'True' else 'no'] for r in h2])
    return out


def c10(A):
    d = A / 'compare_primary_norestr'
    out = ['**Table C.10. Repeat restrictions: primary run minus the run without repeat restrictions, on the same states and seeds.** '
           'Panel A: paired differences by rule and portfolio (linear curve) and the class-B reversal share in each run. '
           'Panel B: 3-2-1 only, by group (A1 amendment 3).', '', '*Panel A*', '']
    c = read(d / 'C_1_paired_differences.csv')
    out += table(['rule', 'portfolio', 'n', 'mean Δτ', 'max \\|Δτ\\|', '% \\|Δτ\\| ≥ δ', 'reversal, with', 'reversal, without',
                  'difference [99% CI]', 'verdicts changed'],
                 [[RULE[r['rule']], PF[r['portfolio']], r['n_team_games'], f4(r['mean_diff_linear']),
                   f"{float(r['max_abs_diff_linear']):.4f}", pct(r['share_abs_diff_over_delta_linear']),
                   pct(r['reversal_share_a']), pct(r['reversal_share_b']),
                   dci(r['reversal_share_diff'], r['diff_lo99'], r['diff_hi99']),
                   r['verdict_changed']] for r in c])
    out += ['*Panel B*', '']
    g = read(d / 'T5_4_restrictions.csv')
    lab = {'restricted_native': 'restricted native', 'holds_restricted_pick': "holds a restricted native's pick",
           'other': 'all other team-games'}
    out += table(['portfolio', 'group', 'n', 'Δ reversal share (pts)', 'mean Δτ', 'q25', 'median', 'q75'],
                 [[PF[r['portfolio']], lab[r['group']], r['n'], pct(r['delta_reversal_share'], 2), f4(r['mean']),
                   f4(r['q25']), f4(r['median']), f4(r['q75'])] for r in g])
    return out


def c11(A):
    d = A / 'primary_precise_only'
    out = ['**Table C.11. The headline quantities with the flagged days excluded** (163 days that met the precision '
           'target in the run, judged at the stopping constant 2.807034; 2,308 team-games per rule). Online Appendix '
           'Table H.11 gives the same quantities on the 141 days that meet the target at the three-look constant '
           '2.935199, recomputed from the stored batches.', '']
    h = read(d / 'T5_headline_reversal_diff.csv')
    out += table(['contrast', 'portfolio / rule', 'verdicts', 'share a', 'share b', 'difference [99% CI], pts'],
                 [[r['contrast'].replace('_', ' '), r['portfolio'], 'registered' if r['verdict'] == 'verdict_B' else 'precision-matched',
                   pct(r['share_a']), pct(r['share_b']), f"{pct(r['diff'])} [{pct(r['lo99'])}, {pct(r['hi99'])}]"] for r in h])
    h1 = read(d / 'H1.csv')[0]
    h2 = [r for r in read(d / 'H2.csv') if r['curve'] == 'linear' and r['sample'] == 'registered'][0]
    out += table(['test', 'n', 'estimate [99% CI]', 'verdict'],
                 [['H1', h1['n_team_games'], f"{pct(h1['diff_new_minus_old'])} pts [{pct(h1['diff_lo99'])}, {pct(h1['diff_hi99'])}]; crossings {pct(h1['crossing_share'])}%",
                   'supported' if h1['supported'] == 'True' else 'not supported'],
                  ['H2', h2['n_games'], f"{float(h2['mean_diff_new_minus_old']):+.5f} [{float(h2['lo99']):+.5f}, {float(h2['hi99']):+.5f}]",
                   'supported' if h2['supported'] == 'True' else 'not supported']])
    return out


def c12(A):
    out = ['**Table C.12. Robustness runs on the registered subsamples.** Each run is compared with the primary run '
           'on the same states: paired linear-curve differences (mean, and the largest absolute difference over team-games '
           'on the linear and the top-3 curve), the class-B reversal share in each, the difference '
           '(run minus primary) and the number of team-games whose verdict changes.', '']
    have = [t for t in ('compare_primary_dta', 'compare_primary_latelink', 'compare_primary_stress', 'compare_primary_alt6')
            if (A / t / 'C_1_paired_differences.csv').exists()]
    if not have:
        return out + pending('draw-then-adjust, late-window link, slope stress and the 2023-24 ledger re-run; filled when these runs exist')
    body = []
    for t in have:
        for r in read(A / t / 'C_1_paired_differences.csv'):
            neg = lambda x: -float(x)
            body.append([RUN.get(r['run_b'], r['run_b']), RULE[r['rule']], PF[r['portfolio']], r['n_team_games'],
                         f4(-float(r['mean_diff_linear'])), f4u(r['max_abs_diff_linear']), f4u(r['max_abs_diff_top3_stress']),
                         pct(r['share_abs_diff_over_delta_linear']),
                         pct(r['reversal_share_a']), pct(r['reversal_share_b']),
                         dci(neg(r['reversal_share_diff']), neg(r['diff_hi99']), neg(r['diff_lo99'])), r['verdict_changed']])
    return out + table(['run', 'rule', 'portfolio', 'n', 'mean Δτ', 'max \\|Δτ\\|', 'max \\|Δτ\\|, top-3', '% \\|Δτ\\| ≥ δ', 'reversal, primary', 'reversal, run',
                        'run − primary [99% CI], pts', 'verdicts changed'], body)


def c13(A):
    return verdict_block(read(A / 'primary' / 'T5_1_verdicts.csv'), ('C',),
                         '**Table C.13. Verdict shares, class C (%, 99% two-level bootstrap intervals).** Class C omits '
                         'slot 30 from the dominance comparison (Lemma 1). It differs from the class-B verdicts of Table '
                         '5.1 in 2 of the 19,584 team-game, rule and portfolio combinations.')


def c14(A):
    sd = read(A / 'primary' / 'T5_5_stakes_distribution.csv')
    out = ['**Table C.14. Third-party share, concentration and the number of materially staked teams, linear curve.** '
           'TP and HHI are computed over materially staked teams ($|\\hat{s}_c| ≥ δ$); the "raw" rows are the unrestricted '
           'diagnostic of A1 amendment 9, item 4, in which pure Monte Carlo noise inflates the share. The paired '
           'differences are over the games in which the measure is defined under both rules, so they need not equal '
           'the difference of the rule means. The identity of the largest third party is computed per game and not '
           'tabulated.', '']
    lab = {'tp_share': 'TP', 'tp_share_raw': 'TP, raw', 'hhi': 'HHI', 'n_material': 'teams materially staked',
           'mean_abs_third': 'mean absolute third-party stake', 'mean_abs_third_raw': 'same, raw'}
    body = []
    for m in ('tp_share', 'tp_share_raw', 'hhi', 'n_material', 'mean_abs_third', 'mean_abs_third_raw'):
        for r in ('old', 'new', 'new_minus_old'):
            x = [y for y in sd if y['rule'] == r and y['curve'] == 'linear' and y['measure'] == m]
            if not x:
                continue
            x = x[0]
            fmt = (lambda z: f'{float(z):.3f}') if not m.startswith('mean_abs') else (lambda z: f'{float(z):.5f}')
            if m == 'n_material':
                fmt = lambda z: f'{float(z):.1f}'
            body.append([lab[m], RULE.get(r, '3-2-1 − old (paired)'), f'{int(x["n"]):,}', fmt(x['mean']), fmt(x['median']),
                         f'[{fmt(x["q25"])}, {fmt(x["q75"])}]', fmt(x['q90'])])
    return out + table(['measure', 'rule', 'games', 'mean', 'median', 'IQR', '90th pct'], body)


C3LAB = {'0': 'old rule (∅)', 'F': 'F', 'L': 'L', 'R': 'R', 'P': 'P', 'FL': 'FL', 'FR': 'FR', 'FP': 'FP', 'LR': 'LR',
         'LP': 'LP', 'RP': 'RP', 'FLR': 'FLR (3-2-1)', 'FLP': 'FLP', 'FRP': 'FRP', 'LRP': 'LRP', 'FLRP': 'FLRP (3-2-1 with ban)'}
C3ORDER = ('0', 'F', 'L', 'R', 'P', 'FL', 'FR', 'FP', 'LR', 'LP', 'RP', 'FLR', 'FLP', 'FRP', 'LRP', 'FLRP')


def _c3_dir(A):
    d = A / 'c3'
    if not (d / 'C3_1_outcomes.csv').exists():
        raise FileNotFoundError(d / 'C3_1_outcomes.csv')
    return d


def _pts(x, d=2):
    v = round(100 * float(x), d) + 0.0
    return f'{v:+.{d}f}'.replace('-', '−')


def _t4(x):
    return f'{float(x):+.4f}'.replace('-', '−')


def c15(A):
    d = _c3_dir(A)
    y = read(d / 'C3_1_outcomes.csv')
    out = ['**Table C.15. Component decomposition (C3): the sixteen configurations, all team-games (actual portfolio, '
           '81 days, 1,252 team-games each; 99% two-level bootstrap intervals, seasons then days).** F: 3-2-1 field and ball '
           'allocation; L: floor; R: repeat restrictions; P: protection ban, under reading A (top-11) and reading B '
           '(top-16). Configurations without P do not depend on the reading. Y1: class-B reversal share (%); Y2: mean '
           'linear-curve τ; Y3: mean third-party share over the 590 games in which it is defined under every '
           'configuration.', '']
    body = []
    for sub in C3ORDER:
        for v in (('A', 'B') if 'P' in sub else ('A',)):
            g = {o: [r for r in y if r['variant'] == v and r['band'] == 'all' and r['subset'] == sub and r['outcome'] == o][0]
                 for o in ('Y1_reversal_share', 'Y2_mean_tau_linear', 'Y3_mean_tp_share')}
            r1, r2, r3 = g['Y1_reversal_share'], g['Y2_mean_tau_linear'], g['Y3_mean_tp_share']
            body.append([C3LAB[sub] + (f', reading {v}' if 'P' in sub else ''),
                         f'{pct(r1["value"])} [{pct(r1["lo99"])}, {pct(r1["hi99"])}]',
                         f'{_t4(r2["value"])} [{_t4(r2["lo99"])}, {_t4(r2["hi99"])}]',
                         f'{float(r3["value"]):.3f} [{float(r3["lo99"]):.3f}, {float(r3["hi99"]):.3f}]'])
    return out + table(['configuration', 'Y1, reversal share', 'Y2, mean τ', 'Y3, TP'], body)


def c16(A):
    d = _c3_dir(A)
    y = read(d / 'C3_1_outcomes.csv')
    chain = (('0', '1: old rule'), ('F', '2: + F'), ('FL', '3: + L'), ('FLR', '4: + R (3-2-1)'), ('FLRP', '+ P'))
    out = ['**Table C.16. Component decomposition (C3) by league rank at the cutoff: Y1 and Y2 along the registered '
           'chain (99% intervals).** Configuration 5 is the ban under reading A and configuration 6 under reading B; '
           'n is team-games per configuration.', '']
    body = []
    for b in ('1-3', '4-10', '11-16', '17-30'):
        for sub, lab in chain:
            for v in (('A', 'B') if 'P' in sub else ('A',)):
                r1 = [r for r in y if r['variant'] == v and r['band'] == b and r['subset'] == sub and r['outcome'] == 'Y1_reversal_share'][0]
                r2 = [r for r in y if r['variant'] == v and r['band'] == b and r['subset'] == sub and r['outcome'] == 'Y2_mean_tau_linear'][0]
                name = (f'{5 if v == "A" else 6}: ' + lab + f', reading {v}') if 'P' in sub else lab
                body.append([b, r1['n'], name, f'{pct(r1["value"])} [{pct(r1["lo99"])}, {pct(r1["hi99"])}]',
                             f'{_t4(r2["value"])} [{_t4(r2["lo99"])}, {_t4(r2["hi99"])}]'])
    return out + table(['rank', 'n', 'configuration', 'Y1, reversal share (%)', 'Y2, mean τ'], body)


def c17(A):
    d = _c3_dir(A)
    sh = read(d / 'C3_3_shapley.csv'); ch = read(d / 'C3_2_chain.csv')
    comp = {'F': 'field and balls (F)', 'L': 'floor (L)', 'R': 'repeat restrictions (R)', 'P': 'protection ban (P)'}
    out = ['**Table C.17. Component attribution (C3): reading B, by rank band, and the chain increments.** "F before '
           'R" averages the marginal contributions over the 12 orderings in which the field precedes the restrictions; '
           '"unconstrained" is the Shapley value over all 24 orderings; both with 99% two-level bootstrap intervals (seasons then days, as in the primary run; the day-clustered version is in Online Appendix H.24). '
           'Y1 in percentage points, Y2 in units of τ, Y3 in units of TP.', '',
           '*Panel A: all team-games, reading B (top-16).*', '']

    def att(f, v, lo, hi):
        if float(v) == float(lo) == float(hi) == 0.0:
            return '0 (no change in any resample)'
        return f'{f(v)} [{f(lo)}, {f(hi)}]'

    def blk(v, b, outs):
        body = []
        for o, lab, f in outs:
            for k in ('F', 'L', 'R', 'P'):
                r = [x for x in sh if x['variant'] == v and x['band'] == b and x['outcome'] == o and x['component'] == k][0]
                body.append([lab, comp[k], att(f, r['value_FbeforeR'], r['lo99'], r['hi99']),
                             att(f, r['shapley_unconstrained'], r['unc_lo99'], r['unc_hi99'])])
            tot = [x for x in sh if x['variant'] == v and x['band'] == b and x['outcome'] == o and x['component'] == 'sum'][0]
            body.append([lab, 'total (full − old)', f(tot['value_FbeforeR']), f(tot['shapley_unconstrained'])])
        return body
    f3 = lambda x: f'{float(x):+.3f}'.replace('-', '−')
    outs = (('Y1_reversal_share', 'Y1 (pts)', _pts), ('Y2_mean_tau_linear', 'Y2', _t4), ('Y3_mean_tp_share', 'Y3', f3))
    out += table(['outcome', 'component', 'F before R [99% CI]', 'unconstrained [99% CI]'], blk('B', 'all', outs))
    out += ['*Panel B: Y1 by league rank at the cutoff, reading A (top-11), percentage points.*', '']
    body = []
    for b in ('1-3', '4-10', '11-16', '17-30'):
        for row in blk('A', b, (('Y1_reversal_share', b, _pts),)):
            body.append(row)
    out += table(['rank', 'component', 'F before R [99% CI]', 'unconstrained [99% CI]'], body)
    out += ['*Panel C: chain increments, configurations 1 → 5 (reading A) and 1 → 6 (reading B), all team-games.*', '']
    steps = (('old -> F', '1 → 2: + F'), ('F -> FL', '2 → 3: + L'), ('FL -> FLR', '3 → 4: + R'), ('FLR -> FLRP', '4 → 5/6: + P'))
    body = []
    for st, lab in steps:
        for v in (('A', 'B') if st == 'FLR -> FLRP' else ('A',)):
            cells = []
            for o, f in (('Y1_reversal_share', _pts), ('Y2_mean_tau_linear', _t4), ('Y3_mean_tp_share', f3)):
                r = [x for x in ch if x['variant'] == v and x['band'] == 'all' and x['outcome'] == o and x['step'] == st][0]
                cells.append(att(f, r['delta'], r['lo99'], r['hi99']))
            body.append([lab + (f', reading {v}' if st == 'FLR -> FLRP' else '')] + cells)
    return out + table(['step', 'Y1 (pts)', 'Y2', 'Y3'], body)


def c18(A):
    t = read(A / 'primary' / 'T5_2_verdicts_by_band.csv')
    out = ['**Table C.18. Verdict shares by league rank at the cutoff (class B, %).** The reversal share with its '
           '99% two-level bootstrap interval, or as a count when the interval has no variation, and the other three '
           'verdicts; n is team-games per rule. Table 5.2 prints the reversal column.', '']
    body = []
    for b in ('1-3', '4-10', '11-16', '17-30'):
        for r in ('old', 'new'):
            for pf in ('actual', 'own'):
                g = {v: [x for x in t if x['rule'] == r and x['portfolio'] == pf and x['band'] == b
                         and x['value_class'] == 'B' and x['verdict'] == v][0] for v in VERD}
                body.append([b, g['reversal']['n'], RULE[r], PF[pf], ci(g['reversal']['share'], g['reversal']['lo99'], g['reversal']['hi99'], g['reversal']['n']),
                             pct(g['dominance_positive']['share']), pct(g['negligible']['share']), pct(g['unresolved']['share'])])
    return out + table(['rank', 'n', 'rule', 'portfolio', 'reversal', 'dom.-pos.', 'negligible', 'unresolved'], body)


def c19(A):
    s = read(A / 'primary' / 'T5_3_reversal_slot.csv')
    out = ['**Table C.19. Reversal slot j\\* among class-B reversals, by slot range (counts).** The registered j\\* '
           'is the slot at which the upper band is smallest; "argmin Ĉ" is the slot at which the point estimate Ĉ(j) '
           'itself is smallest, the quantity that Proposition 1 predicts (slot 9 for an own pick whose loss crosses '
           'the 3\\|4 boundary); "matched" is the precision-matched j\\* (of the precision-matched reversals, whose '
           'count is smaller).', '']
    body = []
    for r in ('old', 'new'):
        for pf in ('actual', 'own'):
            rows = [x for x in s if x['rule'] == r and x['portfolio'] == pf]
            def rng(col, lo, hi):
                return sum(int(x[col]) for x in rows if lo <= int(x['jstar']) <= hi)
            n = int(rows[0]['n_reversals']); npm = int(rows[0]['n_reversals_pm'])
            mode = max(rows, key=lambda x: int(x['count']))['jstar'] if n else '—'
            cells = [str(rng(c, lo, hi)) for c in ('count', 'count_argmin_C_hat', 'count_precision_matched')
                     for lo, hi in ((1, 11), (12, 15), (16, 30))]
            body.append([RULE[r], PF[pf], n, npm] + cells + [mode])
    return out + table(['rule', 'portfolio', 'reversals', 'matched reversals', 'j\\* 1–11', '12–15', '16–30', 'argmin Ĉ 1–11', '12–15', '16–30',
                        'matched 1–11', '12–15', '16–30', 'modal j\\*'], body)


def render(A=ANALYSIS):
    A = Path(A)
    parts = ['# Appendix C. Additional tables', '',
             'Registered tables that the body does not carry, generated by `src/lottery321/appendix_c_tables.py` '
             'from the analysis output. Class B verdicts and two-level bootstrap 99% intervals throughout unless a '
             'table says otherwise; an interval with no bootstrap variation is shown as a count. Not every registered '
             'table is published. The following are computed but not printed (Section 6.3, departure (v)): '
             'within-season intervals; precision-matched versions of the verdict tables other than C.3 and of the '
             'precision-matched reversal-slot counts beyond Table 5.3; the concentration, material-count and '
             'band-level Δτ tables on the three curves other than linear; class-C verdicts by band; the share of tie '
             'effects; the identity of the largest third party in each game (computed per game, not tabulated); the '
             'full set of Section 5.1–5.4 tables on the robustness subsamples (of which Tables 5.7, C.11 and C.12 print '
             'the headline quantities and the paired differences); and, for the C3 decomposition, Y3 by rank band and '
             'the attribution of Y2 and Y3 by band. No precision-matched version of the C3 outcomes was registered or '
             'computed. By-season estimates of the headline quantities, H1 and H2 are in Online Appendix H.', '']
    for fn in (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19):
        try:
            parts += fn(A)
        except FileNotFoundError as e:
            parts += [f'**Table from {fn.__name__}.**', ''] + pending(f'input missing: {Path(str(e)).name}')
    return '\n'.join(parts) + '\n'


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--analysis', default=str(ANALYSIS)); ap.add_argument('--out', default=str(OUT))
    a = ap.parse_args()
    Path(a.out).write_text(render(a.analysis), encoding='utf-8')
    print('written', a.out)

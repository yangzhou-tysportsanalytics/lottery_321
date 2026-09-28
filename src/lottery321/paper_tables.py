"""Body tables of paper Section 5, rendered as markdown from the registered analysis tables.

The six body tables were fixed before the primary run was opened (addendum A1, amendment 11). This script
only formats: every number comes from a CSV written by analysis.run() or c3_analysis, or from
the stored post-hoc tables of Online Appendix H; nothing is recomputed, and a table whose inputs are missing
is emitted as a marked placeholder rather than skipped.

Addendum A1, amendment 16, changed the presentation of the body tables without changing any
registered number: Table 5.1 prints class B only (class C is Online Appendix Table C.13); Table 5.2 prints the
reversal share by rank band only (Online Appendix Table C.18 has the full split); Table 5.3 prints H1 only (the
reversal-slot counts are Online Appendix Table C.19); Table 5.4 drops the
median and interquartile columns (Online Appendix Table C.5 keeps the full distribution); Table 5.5 drops the
stakes-distribution panel (Online Appendix Table C.14) and prints H2 on the registered curve only; a share
whose bootstrap interval has no variation is shown as a count; and Table 5.7 gathers the four headline
quantities of every robustness item in one table.
Usage: python paper_tables.py <analysis_dir> [--c3 DIR] [--out FILE]
"""
import argparse
import csv
from pathlib import Path

RULE = {'old': 'old rule', 'new': '3-2-1', 'delta': 'ΔC = C_new − C_old'}
PF = {'actual': 'actual portfolio', 'own': 'own pick only'}
VERD = ('dominance_positive', 'negligible', 'reversal', 'unresolved')
VLAB = {'dominance_positive': 'dominance-positive', 'negligible': 'negligible', 'reversal': 'reversal',
        'unresolved': 'unresolved'}
BANDS = ('1-3', '4-10', '11-16', '17-30')
TYPES = ('both_lose', 'normal', 'no_own_stake', 'opposed', 'one_sided_win', 'both_win')
TLAB = {'both_lose': 'both prefer to lose', 'normal': 'one-sided lose', 'no_own_stake': 'no own stake',
        'opposed': 'opposed', 'one_sided_win': 'one-sided win', 'both_win': 'both prefer to win'}


def read(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def pct(x, d=1):
    return f'{100 * float(x):.{d}f}'


def ci(r, d=1):
    """A share with its 99% interval. An interval with no bootstrap variation (every resample gives the same
    share, which happens only when no team-game, or every team-game, has the property) is shown as a count,
    since '0.0 [0.0, 0.0]' reads as a precise zero rather than as the absence of any case."""
    if float(r['lo99']) == float(r['hi99']) and 'n' in r:
        k = round(float(r['share']) * int(r['n']))
        return f'{pct(r["share"], d)} ({k:,} of {int(r["n"]):,})'
    return f'{pct(r["share"], d)} [{pct(r["lo99"], d)}, {pct(r["hi99"], d)}]'


def pick(rows, **w):
    m = [r for r in rows if all(str(r.get(k)) == str(v) for k, v in w.items())]
    if len(m) != 1:
        raise KeyError(f'{w}: {len(m)} rows')
    return m[0]


def table_5_1(A):
    t = read(A / 'T5_1_verdicts.csv')
    out = ['**Table 5.1. Verdict shares, all team-games (class B; %, 99% two-level bootstrap intervals).** '
           '4,896 team-games per rule. Rows "ΔC = C_new − C_old" classify the change ΔC(j) = C_new(j) − C_old(j). '
           'A share with no bootstrap variation is shown as a count. Class C, which differs from class B in '
           '2 of 19,584 verdicts, is Online Appendix Table C.13.', '',
           '| rule | portfolio | ' + ' | '.join(VLAB[v] for v in VERD) + ' |', '|---|---|' + '---|' * len(VERD)]
    for r in ('old', 'new', 'delta'):
        for pf in ('actual', 'own'):
            cells = [ci(pick(t, rule=r, portfolio=pf, value_class='B', verdict=v)) for v in VERD]
            out.append(f'| {RULE[r]} | {PF[pf]} | ' + ' | '.join(cells) + ' |')
    return out + ['']


def table_5_2(A):
    """The body prints the reversal share by rank band only; the full verdict split by band
    is Online Appendix Table C.18."""
    t = read(A / 'T5_2_verdicts_by_band.csv')
    ns = {b: int(pick(t, rule='old', portfolio='actual', band=b, value_class='B', verdict='reversal')['n']) for b in BANDS}
    out = ['**Table 5.2. Reversal share by league rank at the cutoff (class B, %, 99% two-level bootstrap intervals).** '
           'A share with no bootstrap variation is shown as a count; n is team-games per rule in each rank band. The '
           'dominance-positive, negligible and unresolved shares by rank band are in Online Appendix Table C.18.', '',
           '| rule | portfolio | ' + ' | '.join(f'ranks {b} (n = {ns[b]:,})' for b in BANDS) + ' |',
           '|---|---|' + '---|' * len(BANDS)]
    for r in ('old', 'new'):
        for pf in ('actual', 'own'):
            cells = [ci(pick(t, rule=r, portfolio=pf, band=b, value_class='B', verdict='reversal')) for b in BANDS]
            out.append(f'| {RULE[r]} | {PF[pf]} | ' + ' | '.join(cells) + ' |')
    return out + ['']


def table_5_3(A):
    """Panel B (reversal slots by range) is Online Appendix Table C.19."""
    h = read(A / 'H1.csv')[0]
    n_rev = int(h['n_new_reversals'])
    cross = (f'{pct(h["crossing_share"])} ({round(float(h["crossing_share"]) * n_rev)} of {n_rev})'
             if float(h['crossing_lo99']) == float(h['crossing_hi99'])
             else f'{pct(h["crossing_share"])} [{pct(h["crossing_lo99"])}, {pct(h["crossing_hi99"])}]')
    out = ['**Table 5.3. H1: own-pick-only team-games at league rank 2–5 at the cutoff.** Shares (%) with a '
           'significantly negative linear-curve τ under each rule and their difference (99% two-level bootstrap '
           f'interval); the old-rule share is 0 of {h["n_team_games"]} team-games, and the crossing share has no '
           'bootstrap variation because every reversal in the rank band is a crossing. The distribution of the reversal '
           'slot j\\* is Online Appendix Table C.19.', '',
           '| n | significantly negative linear-curve τ, 3-2-1 | same, old rule | difference [99% CI] | '
           '3-2-1 reversals | of which crossings | H1 |', '|---|---|---|---|---|---|---|',
           f'| {h["n_team_games"]} | {pct(h["share_neg_new"])} | {pct(h["share_neg_old"])} | '
           f'{pct(h["diff_new_minus_old"])} [{pct(h["diff_lo99"])}, {pct(h["diff_hi99"])}] | '
           f'{n_rev} | {cross} | {"supported" if h["supported"] == "True" else "not supported"} |']
    return out + ['']


def table_5_4(A):
    t = read(A / 'T5_curves_and_T5_6_delta.csv')
    tr = read(A / 'T5_6_transitions.csv')
    out = ['**Table 5.4. How 3-2-1 moves each team\'s incentive (linear curve).** Δτ = τ_new − τ_old; the shares '
           'significantly positive or negative use the pointwise 99% interval at the three-look constant, with '
           'their 99% bootstrap intervals. The median and interquartile range of Δτ, and the other curves, are '
           'in Online Appendix Table C.5.', '',
           '*Panel A: change in linear-curve τ by league rank at the cutoff.*', '',
           '| rank | portfolio | n | mean Δτ | significantly < 0 [99% CI] | significantly > 0 [99% CI] |',
           '|---|---|---|---|---|---|']  # a share with no bootstrap variation is shown as a count (ci)
    for b in ('all',) + BANDS:
        for pf in ('actual', 'own'):
            r = pick(t, rule='delta', portfolio=pf, band=b, curve='linear')
            neg = ci({'share': r['share_sig_neg'], 'lo99': r['neg_lo99'], 'hi99': r['neg_hi99'], 'n': r['n']})
            pos = ci({'share': r['share_sig_pos'], 'lo99': r['pos_lo99'], 'hi99': r['pos_hi99'], 'n': r['n']})
            out.append(f'| {b} | {PF[pf]} | {int(r["n"]):,} | {float(r["mean"]):+.4f} | {neg} | {pos} |')
    out += ['', '*Panel B: reversal transitions, old rule → 3-2-1, class B (counts).*', '',
            '| portfolio | reversal under both | created (not reversal → reversal) | removed (reversal → not) |',
            '|---|---|---|---|']
    for pf in ('actual', 'own'):
        rows = [x for x in tr if x['portfolio'] == pf]
        both = sum(int(x['count']) for x in rows if x['old'] == 'reversal' and x['new'] == 'reversal')
        cre = sum(int(x['count']) for x in rows if x['old'] != 'reversal' and x['new'] == 'reversal')
        rem = sum(int(x['count']) for x in rows if x['old'] == 'reversal' and x['new'] != 'reversal')
        out.append(f'| {PF[pf]} | {both} | {cre} | {rem} |')
    return out + ['']


CLAB = {'linear': 'linear', 'concave': 'concave', 'convex': 'convex', 'top3_stress': 'top-3'}
MLAB = {'tp_share': 'TP', 'hhi': 'HHI', 'n_material': 'teams materially staked', 'mean_abs_third': 'mean absolute third-party stake'}


def table_5_5(A):
    ty = read(A / 'T5_4_typology.csv')
    h2 = read(A / 'H2.csv')
    out = ['**Table 5.5. The draft-stakes network (linear curve).** 2,448 games per rule. The distribution of the '
           'third-party share and of the concentration of stakes is Online Appendix Table C.14.', '',
           '*Panel A: typology of games (%, 99% CI) and, within each type, the share that is third-party dominated (TP > ½).*',
           '', '| type | old rule | 3-2-1 | games, old / 3-2-1 | TP defined, old / 3-2-1 | TP-dominated, old | TP-dominated, 3-2-1 |',
           '|---|---|---|---|---|---|---|']
    undef = {}
    for k in TYPES:
        o, n = pick(ty, rule='old', curve='linear', type=k), pick(ty, rule='new', curve='linear', type=k)
        undef[k] = (int(o['n']) - int(o['n_tp_defined']), int(n['n']) - int(n['n_tp_defined']))
        out.append(f'| {TLAB[k]} | {ci(o)} | {ci(n)} | {int(o["n"]):,} / {int(n["n"]):,} | {int(o["n_tp_defined"]):,} / {int(n["n_tp_defined"]):,} | '
                   f'{pct(o["tp_dominated_share"])} | {pct(n["tp_dominated_share"])} |')
    out += ['', 'Type shares are over all games of a rule. The TP-dominated share within a type is over the games of '
            'that type in which TP is defined, that is, in which at least one team is materially staked. In '
            f'"no own stake" games on this curve no participant holds a material stake in these data, so when TP is '
            f'defined it is 100%; {undef["no_own_stake"][0]} (old) and {undef["no_own_stake"][1]} (3-2-1) of these games '
            'have no materially staked team at all. "One-sided lose" is the registered type *normal*.']
    out += ['', '*Panel B: H2, paired difference in the mean absolute third-party stake, 3-2-1 − old, linear curve, '
            'games with a routed right to a participant.* The three other curves are in Online Appendix Table C.9.',
            '', '| sample | games | mean difference | 99% CI | registered test | positive, CI excludes 0 |',
            '|---|---|---|---|---|---|']
    for r in h2:
        if r['curve'] != 'linear':
            continue
        out.append(f'| {r["sample"].replace("_", "-")} | {int(r["n_games"]):,} | '
                   f'{float(r["mean_diff_new_minus_old"]):+.5f} | [{float(r["lo99"]):+.5f}, {float(r["hi99"]):+.5f}] | '
                   f'{"yes" if r["registered"] == "True" else "no"} | {"yes" if r["supported"] == "True" else "no"} |')
    return out + ['']


COMP = {'F': 'field and balls (F)', 'L': 'floor (L)', 'R': 'repeat restrictions (R)', 'P': 'protection ban (P)'}
CHAIN_LAB = (('0', '1: old rule'), ('F', '2: + field and balls'), ('FL', '3: + floor'), ('FLR', '4: + restrictions (3-2-1)'),
             ('FLRP', '+ protection ban'))


def _pts(x, d=1):
    """A share difference in percentage points with sign, and no negative zero."""
    v = round(100 * float(x), d) + 0.0
    return f'{v:+.{d}f}'.replace('-', '−')


def _t(x):
    return f'{float(x):+.4f}'.replace('-', '−')


def table_5_6(C3):
    """C3 registration §4-5 and A1 amendment 11: outcomes along the registered chain, the component
    attribution (F before R, with the unconstrained Shapley value beside it) and H3, under both ban readings."""
    C3 = Path(C3) if C3 else None
    if C3 is None or not (C3 / 'C3_3_shapley.csv').exists():
        return ['**Table 5.6. Component decomposition of 3-2-1 (C3).** *[Pending: C3 output not found.]*', '']
    y = read(C3 / 'C3_1_outcomes.csv'); sh = read(C3 / 'C3_3_shapley.csv'); h3 = read(C3 / 'C3_4_H3.csv')
    n = pick(y, variant='A', band='all', outcome='Y1_reversal_share', subset='0')['n']
    out = [f'**Table 5.6. Component decomposition of 3-2-1 (C3), actual portfolios, 81 game days ({int(n):,} team-games '
           'per configuration).** Protection ban: every top-12 to top-15 protection in the ledgers (24 protections, 3 of '
           'them inside pools) becomes top-11 (reading A) or top-16 (reading B). Y3 is averaged over the 590 games in '
           'which TP is defined under every configuration (of 626). Intervals are the two-level bootstrap of §4.5 (seasons, '
           'then days), as in Table 5.7; Online Appendix H.24 gives the day-clustered version. The sixteen subsets and the results by rank band are in Online Appendix Tables C.15–C.17.', '',
           '*Panel A: outcomes along the registered chain (99% CI). Y1: class-B reversal share (%); Y2: mean '
           'linear-curve τ; Y3: mean third-party share of material stakes.*', '',
           '| configuration | Y1, reversal share | Y2, mean τ | Y3, TP |', '|---|---|---|---|']
    for sub, lab in CHAIN_LAB:
        for v in (('A', 'B') if 'P' in sub else ('A',)):
            r1 = pick(y, variant=v, band='all', outcome='Y1_reversal_share', subset=sub)
            r2 = pick(y, variant=v, band='all', outcome='Y2_mean_tau_linear', subset=sub)
            r3 = pick(y, variant=v, band='all', outcome='Y3_mean_tp_share', subset=sub)
            name = (f'{5 if v == "A" else 6}: ' + lab + f', reading {v}') if 'P' in sub else lab
            out.append(f'| {name} | {pct(r1["value"])} [{pct(r1["lo99"])}, {pct(r1["hi99"])}] | '
                       f'{_t(r2["value"])} [{_t(r2["lo99"])}, {_t(r2["hi99"])}] | '
                       f'{float(r3["value"]):.3f} [{float(r3["lo99"]):.3f}, {float(r3["hi99"]):.3f}] |')
    out += ['', '*Panel B: attribution of the change from the old rule to full 3-2-1 with the ban, reading A. '
            '"F before R" averages the marginal contributions over the 12 of the 24 orderings of the four components '
            'in which the field precedes the restrictions (primary); "unconstrained" is the Shapley value over all 24.*', '',
            '| component | Y1, F before R (pts) | Y1, unconstrained | Y2, F before R | Y2, unconstrained |',
            '|---|---|---|---|---|']
    for k in ('F', 'L', 'R', 'P', 'sum'):
        a = pick(sh, variant='A', band='all', outcome='Y1_reversal_share', component=k)
        b = pick(sh, variant='A', band='all', outcome='Y2_mean_tau_linear', component=k)
        if k == 'sum':
            out.append(f'| total (full − old) | {_pts(a["value_FbeforeR"], 2)} | {_pts(a["shapley_unconstrained"], 2)} | '
                       f'{_t(b["value_FbeforeR"])} | {_t(b["shapley_unconstrained"])} |')
        else:
            out.append(f'| {COMP[k]} | {_pts(a["value_FbeforeR"], 2)} [{_pts(a["lo99"], 2)}, {_pts(a["hi99"], 2)}] | '
                       f'{_pts(a["shapley_unconstrained"], 2)} | {_t(b["value_FbeforeR"])} [{_t(b["lo99"])}, {_t(b["hi99"])}] | '
                       f'{_t(b["shapley_unconstrained"])} |')
    out += ['', '*Panel C: H3, team-games in which the team holds another team\'s pick conditionally (class-B '
            'reversal share, %).* "With ban" is configuration 5 under reading A and configuration 6 under reading B; '
            '"without ban" is configuration 4.', '',
            '| ban reading | team-games | with ban | without ban | change (pts) | (i) lower bound > 0 | (ii) fewer with ban |',
            '|---|---|---|---|---|---|---|']
    for r in h3:
        out.append(f'| {r["variant"]}: top-{"11" if r["variant"] == "A" else "16"} | {int(r["n_team_games"]):,} | '
                   f'{pct(r["share_config5"])} [{pct(r["lo99"])}, {pct(r["hi99"])}] | {pct(r["share_config4"])} | '
                   f'{_pts(r["change"])} [{_pts(r["change_lo99"])}, {_pts(r["change_hi99"])}] | '
                   f'{"yes" if float(r["lo99"]) > 0 else "no"} | '
                   f'{"yes" if 0 < float(r["share_config5"]) < float(r["share_config4"]) else "no"} |')
    ok = all(r['supported'] == 'True' for r in h3)
    out += ['', f'H3 requires (i) and (ii) under both readings; it is {"supported" if ok else "not supported"}. The two '
            'rows coincide to the printed precision because on every one of the 81 days the number of reversals among '
            'these team-games is the same under the two readings (each reading changes it on the same two days, by '
            'one reversal lost and one gained), and the bootstrap resamples days; the readings differ in which '
            'team-games change verdict (5 under reading A, 2 under reading B; Online Appendix H.19).']
    return out + ['']


R8_ROWS = (('precision-matched verdicts (all 312 days)', 'precision-matched verdicts', 'pm'),
           ('no repeat restrictions (all 312 days)', 'no repeat restrictions', 'norestr'),
           ('days meeting the target in the run (z = 2.807034)', 'target met in the run', None),
           ('days flagged in the run', 'flagged in the run', None),
           ('days meeting the target at z = 2.935199 (stored batches)', 'target met, three-look constant', None),
           ('2025-26 excluded', '2025-26 excluded', None),
           ('primary run on the 81 robustness days', 'primary, 81 robustness days', None),
           ('primary run on the 25 alt6 days', 'primary, 25 ledger-check days', None))
RUN_ROWS = (('dta', 'draw-then-adjust draw'), ('latelink', 'late-window link'),
            ('stress', 'slope × 1.25'), ('alt6', '2023-24 ledger, alternative reading'))


def _iv(x, d=1):
    """Interval end point in points: no plus sign, no negative zero."""
    v = round(100 * float(x), d) + 0.0
    return f'{v:.{d}f}'.replace('-', '−')


def _hq(ha, lo, hi):
    return f'{_pts(ha)} [{_iv(lo)}, {_iv(hi)}]'


def _h1(diff, lo, hi, nrev, cross):
    assert abs(float(cross) - 1.0) < 1e-12, cross
    return f'{_pts(diff)} [{_iv(lo)}, {_iv(hi)}] ({int(nrev)})'


def _h2(d, lo, hi):
    f = lambda x: f'{1e4 * float(x):+.2f}'.replace('-', '−')
    g = lambda x: f'{1e4 * float(x):.2f}'.replace('-', '−')
    return f'{f(d)} [{g(lo)}, {g(hi)}]'


def table_5_7(A, H4=None):
    """Amendment 11 requires each robustness item to quote the same four headline quantities. Rows come from the
    primary tables (and the as-run band table), robustness_headlines.csv, the primary-to-run comparisons and the
    stored post-hoc table R8 (Online Appendix H.17); nothing is recomputed."""
    H4 = Path(H4) if H4 else A / 'exploratory_3'
    pri = A / 'primary'
    hd = {r['portfolio']: r for r in read(pri / 'T5_headline_reversal_diff.csv') if r['contrast'] == 'new_minus_old' and r['verdict'] == 'verdict_B'}
    h1 = read(pri / 'H1.csv')[0]
    h2 = pick(read(pri / 'H2.csv'), curve='linear', sample='registered')
    out = ['**Table 5.7. The four headline quantities under every robustness item.** (H-a), (H-b): reversal-share '
           'differences, 3-2-1 − old, actual portfolio and own pick (percentage points). H1: difference in the share '
           'of own-pick team-games at ranks 2–5 whose linear-curve τ is significantly negative, with the number of '
           '3-2-1 reversals in that rank band in parentheses (all crossings in every row). H2: paired difference in the mean '
           'absolute third-party stake, linear curve, in units of $10^{-4}$ of the first pick\'s value. Intervals are 99% '
           'two-level bootstrap intervals (the 2023-24-ledger rows resample days within one season). Rows: the primary '
           'run under the multiplier band, under the as-run bootstrap-t band, under the band with its critical value at '
           'level 1 − 0.01/3 (a Bonferroni adjustment over the three looks; Online Appendix H.27) and precision-matched; the run without '
           'repeat restrictions; subsets of the primary days; and the four registered robustness runs (Online Appendix '
           'Table C.12). "Verdicts changed" counts actual-portfolio class-B verdicts that differ from the primary table, '
           '3-2-1 / old rule; a dash means a subset of the primary run. H1 is supported by the registered bootstrap '
           'criterion in every row (its season-level 99% t interval includes zero; Online Appendix H.12) and H2 is not '
           'supported in every row.', '',
           '| analysis (days; team-games per rule) | (H-a) | (H-b) | H1 difference (3-2-1 reversals) | H2 (×0.0001) | verdicts changed |',
           '|---|---|---|---|---|---|']

    def row(label, days, n, ha, hb, h1t, h2t, chg):
        out.append(f'| {label} ({days}; {n:,}) | {ha} | {hb} | {h1t} | {h2t} | {chg} |')

    row('primary run', 312, 4896, _hq(hd['actual']['diff'], hd['actual']['lo99'], hd['actual']['hi99']),
        _hq(hd['own']['diff'], hd['own']['lo99'], hd['own']['hi99']),
        _h1(h1['diff_new_minus_old'], h1['diff_lo99'], h1['diff_hi99'], h1['n_new_reversals'], h1['crossing_share']),
        _h2(h2['mean_diff_new_minus_old'], h2['lo99'], h2['hi99']), '—')
    # the as-run bootstrap-t band
    asr = A / 'primary_asrun_boott'
    vc = {(r['comparison'], r['rule']): r for r in read(H4 / 'R15_verdict_changes.csv')} if (H4 / 'R15_verdict_changes.csv').exists() else {}
    if (asr / 'T5_headline_reversal_diff.csv').exists():
        hda = {r['portfolio']: r for r in read(asr / 'T5_headline_reversal_diff.csv') if r['contrast'] == 'new_minus_old' and r['verdict'] == 'verdict_B'}
        h1a = read(asr / 'H1.csv')[0]
        chg = (f'{int(vc[("as-run bootstrap-t band", "new")]["verdicts_changed"]):,} / {int(vc[("as-run bootstrap-t band", "old")]["verdicts_changed"]):,}'
               if vc else '')
        row('as-run bootstrap-t band', 312, 4896, _hq(hda['actual']['diff'], hda['actual']['lo99'], hda['actual']['hi99']),
            _hq(hda['own']['diff'], hda['own']['lo99'], hda['own']['hi99']),
            _h1(h1a['diff_new_minus_old'], h1a['diff_lo99'], h1a['diff_hi99'], h1a['n_new_reversals'], h1a['crossing_share']),
            _h2(h2['mean_diff_new_minus_old'], h2['lo99'], h2['hi99']), chg)
    # the band with a Bonferroni adjustment over the three looks (R22)
    H7 = A / 'exploratory_4'
    if (H7 / 'R22_look_adjusted.csv').exists():
        la = {(r['verdicts'], r['portfolio']): r for r in read(H7 / 'R22_look_adjusted.csv')}
        a_, o_ = la[('verdict_B_look', 'actual')], la[('verdict_B_look', 'own')]
        row('look-adjusted band (1 − 0.01/3)', 312, 4896, _hq(a_['diff_new_minus_old'], a_['lo99'], a_['hi99']),
            _hq(o_['diff_new_minus_old'], o_['lo99'], o_['hi99']),
            _h1(h1['diff_new_minus_old'], h1['diff_lo99'], h1['diff_hi99'], o_['h1_band_reversals'],
                int(o_['h1_band_crossings']) / int(o_['h1_band_reversals'])),
            _h2(h2['mean_diff_new_minus_old'], h2['lo99'], h2['hi99']),
            f"{int(a_['new_changed_vs_primary']):,} / {int(a_['old_changed_vs_primary']):,}")
    r8 = {r['analysis']: r for r in read(H4 / 'R8_four_quantities.csv')}
    cmp_dir = {'norestr': A / 'compare_primary_norestr'}
    for key, label, tag in R8_ROWS:
        r = r8[key]
        if tag == 'pm':
            chg = f'{int(vc[("precision-matched verdicts", "new")]["verdicts_changed"]):,} / {int(vc[("precision-matched verdicts", "old")]["verdicts_changed"]):,}' if vc else ''
        elif tag == 'norestr':
            c = {(x['rule'], x['portfolio']): x for x in read(cmp_dir['norestr'] / 'C_1_paired_differences.csv')}
            chg = f'{c[("new", "actual")]["verdict_changed"]} / {c[("old", "actual")]["verdict_changed"]}'
        else:
            chg = '—'
        row(label, int(r['n_days']), int(r['n_team_games']), _hq(r['ha'], r['ha_lo'], r['ha_hi']), _hq(r['hb'], r['hb_lo'], r['hb_hi']),
            _h1(r['h1_diff'], r['h1_lo99'], r['h1_hi99'], r['h1_reversals'], r['h1_crossing_share']),
            _h2(r['h2_diff'], r['h2_lo'], r['h2_hi']), chg)
    rh = read(A / 'robustness_headlines.csv')
    for run, label in RUN_ROWS:
        r = pick(rh, run=run, version=run)
        c = {(x['rule'], x['portfolio']): x for x in read(A / f'compare_primary_{run}' / 'C_1_paired_differences.csv')}
        chg = f'{c[("new", "actual")]["verdict_changed"]} / {c[("old", "actual")]["verdict_changed"]}'
        row(label, int(r['n_days']), int(r['n_team_games']), _hq(r['ha'], r['ha_lo'], r['ha_hi']), _hq(r['hb'], r['hb_lo'], r['hb_hi']),
            _h1(r['h1_diff'], r['h1_lo99'], r['h1_hi99'], r['h1_reversals'], r['h1_crossing_share']),
            _h2(r['h2_diff'], r['h2_lo'], r['h2_hi']), chg)
    return out + ['']


def build(template, A, C3=None):
    """Substitute {{TABLE_5_1}}..{{TABLE_5_7}} in the prose template with the rendered tables."""
    A = Path(A)
    fns = {'TABLE_5_1': lambda: table_5_1(A), 'TABLE_5_2': lambda: table_5_2(A), 'TABLE_5_3': lambda: table_5_3(A),
           'TABLE_5_4': lambda: table_5_4(A), 'TABLE_5_5': lambda: table_5_5(A), 'TABLE_5_6': lambda: table_5_6(C3),
           'TABLE_5_7': lambda: table_5_7(A.parent if A.name == 'primary' else A)}
    txt = Path(template).read_text(encoding='utf-8')
    for k, fn in fns.items():
        tag = '{{' + k + '}}'
        if k == 'TABLE_5_7' and txt.count(tag) == 0:
            continue                      # a template without a Table 5.7 marker is allowed
        if txt.count(tag) != 1:
            raise ValueError(f'{tag} must appear exactly once in the template')
        txt = txt.replace(tag, '\n'.join(fn()).rstrip('\n'))
    return txt


def render(A, C3=None):
    A = Path(A)
    blocks = [table_5_1(A), table_5_2(A), table_5_3(A), table_5_4(A), table_5_5(A), table_5_6(C3),
              table_5_7(A.parent if A.name == 'primary' else A)]
    return '\n'.join(line for b in blocks for line in b)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('analysis_dir'); ap.add_argument('--c3'); ap.add_argument('--out')
    ap.add_argument('--template', help='prose template with {{TABLE_5_n}} markers; output is the full section')
    a = ap.parse_args()
    md = build(a.template, a.analysis_dir, a.c3) if a.template else render(a.analysis_dir, a.c3)
    if a.out:
        Path(a.out).write_text(md + '\n', encoding='utf-8'); print('written', a.out)
    else:
        print(md)

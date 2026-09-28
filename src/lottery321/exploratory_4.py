"""Post-hoc analyses, fourth set, from stored outputs only.

Every analysis here is exploratory (addendum A1, amendment 16): nothing is registered, no new
simulation is run, and no registered table or headline quantity changes. Inputs are the stored primary
day files (50 super-batch means per team-game), the analysed team-game table and the C3 team-game table.

  R16  rollover-adjusted dominance. Under the registered rollover valuation tau_rho = tau - rho*vbar*M
       (A1 amendment 10), summation by parts gives tau_rho(v) = sum_j a_j [C(j) - rho*(j/30)*M] with
       a_j = v(j) - v(j+1) >= 0, so "tau_rho >= 0 for every v in V_B" is equivalent to
       C_rho(j) = C(j) - rho*(j/30)*C(30) >= 0 for every j. The class-B
       verdict rules are re-applied to C_rho with its own multiplier band from the same 50 batches.
  R17  a positive value for the last pick: v_a(k) = a + (1-a) v(k) gives tau_a = (1-a) tau + a M; the
       linear-curve sign is re-read for a in {0.05, 0.10, 0.20} with the batch standard error of tau_a.
  R18  C3 with the two-level bootstrap (seasons, then days) of the primary run, beside the day-clustered
       intervals the C3 registration fixed: H3's share with and without the ban, and the Y1 chain.
  R19  the first-window-day games that Table E.4's clock-time window excludes (H.20's 463/456, 377/376).
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / 'ledgers'))

import analysis as S  # noqa: E402
import exploratory_1 as P  # noqa: E402
import elo as E  # noqa: E402
import simulate as H  # noqa: E402
from value import CURVES  # noqa: E402
from teams import TEAMS  # noqa: E402

OUT = S.OUT / 'exploratory_4'
SEASONS = ('2020-21', '2021-22', '2022-23', '2023-24', '2024-25', '2025-26')
A_TAIL = (0.05, 0.10, 0.20)


def write(name, rows):
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / f'{name}.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)


def read(p):
    with open(p, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


# ---------------------------------------------------------------- R16 / R17: one pass over the day files
def c_rho_batches(db, rho):
    """db: (B, 30) batch slot differences. Returns the (B, 30) batch values of C_rho(j)."""
    Cb = np.cumsum(db, axis=1)
    M = Cb[:, 29:30]
    j = np.arange(1, 31, dtype=float)[None, :]
    return Cb - rho * (j / 30.0) * M


def day_pass(tag='primary'):
    rows = []
    v_lin = CURVES['linear']
    for f in sorted((S.SIMULATIONS / tag).glob('*/exposures_*.npz')):
        d = S.load_day(f); meta = d['meta']
        ranks, _ = S.cutoff_ranks(meta)
        for g, (h, a) in enumerate(meta['focal_teams']):
            gid = meta['focal_game_ids'][g]
            for side, c in ((0, h), (1, a)):
                sgn = 1.0 if side == 0 else -1.0
                for pf, src in (('actual', d['DB']), ('own', d['DB_own'])):
                    for ri, r in enumerate(S.RULES):
                        db = sgn * src[:, g, ri, c, :]
                        Cb = np.cumsum(db, axis=1)
                        m, se, crit = S.band_stats(Cb)
                        v0, _ = S.verdict(m, se, crit['B'], 30)
                        row = {'season': meta['season'], 'day': meta['day'], 'game_id': gid, 'team': TEAMS[c],
                               'rank': int(ranks[c]), 'band': S.band_of(int(ranks[c])), 'rule': r, 'portfolio': pf,
                               'verdict_B': v0, 'M': float(m[29])}
                        for rho in S.RHOS:
                            Cr = c_rho_batches(db, rho)
                            mr, ser, cr = S.band_stats(Cr)
                            vr, jr = S.verdict(mr, ser, cr['B'], 30)
                            tag_ = f'rho{int(rho * 100)}'
                            row[f'verdict_B_{tag_}'] = vr; row[f'jstar_B_{tag_}'] = jr
                        t = db @ v_lin; Mb = db.sum(1)
                        row['tau_linear'] = float(t.mean())
                        row['sign_linear'] = S.curve_sign(float(t.mean()), float(t.std(ddof=1) / np.sqrt(len(t))))
                        for a_ in A_TAIL:
                            ta = (1 - a_) * t + a_ * Mb
                            ma, sa = float(ta.mean()), float(ta.std(ddof=1) / np.sqrt(len(ta)))
                            row[f'tau_a{int(100 * a_):02d}'] = ma
                            row[f'sign_a{int(100 * a_):02d}'] = S.curve_sign(ma, sa)
                        rows.append(row)
    return rows


def summarise_rollover(rows):
    days = sorted({(r['season'], r['day']) for r in rows})
    boot = S.Boot(days, [s for s, _ in days])
    out = []
    for pf in ('actual', 'own'):
        for field in ['verdict_B'] + [f'verdict_B_rho{int(rho * 100)}' for rho in S.RHOS]:
            shares = {}
            for rule in S.RULES:
                sel = lambda x, rule=rule: x['rule'] == rule and x['portfolio'] == pf
                for v in S.VERDICTS:
                    n, d_ = S.per_day(rows, boot, lambda x, v=v, field=field: x[field] == v, sel)
                    shares[(rule, v)] = (float(n.sum() / d_.sum()), int(n.sum()), int(d_.sum()))
            n1, d1 = S.per_day(rows, boot, lambda x, field=field: x[field] == 'reversal', lambda x: x['rule'] == 'new' and x['portfolio'] == pf)
            n2, d2 = S.per_day(rows, boot, lambda x, field=field: x[field] == 'reversal', lambda x: x['rule'] == 'old' and x['portfolio'] == pf)
            pt, lo, hi = boot.diff_of_ratios(n1, d1, n2, d2)
            changed = {rule: sum(1 for x in rows if x['rule'] == rule and x['portfolio'] == pf and x[field] != x['verdict_B']) for rule in S.RULES}
            rec = dict(portfolio=pf, verdicts=field, n_per_rule=shares[('new', 'reversal')][2])
            for rule in S.RULES:
                for v in S.VERDICTS:
                    rec[f'{rule}_{v}'] = shares[(rule, v)][0]
                rec[f'{rule}_changed_vs_primary'] = changed[rule]
            rec.update(diff_new_minus_old=float(pt), lo99=lo, hi99=hi)
            out.append(rec)
    return out


def summarise_tail(rows):
    out = []
    for pf in ('actual', 'own'):
        for rule in S.RULES:
            sub = [r for r in rows if r['rule'] == rule and r['portfolio'] == pf]
            rec = dict(portfolio=pf, rule=rule, n=len(sub),
                       lose_a0=sum(r['sign_linear'] == 'lose' for r in sub),
                       win_a0=sum(r['sign_linear'] == 'win' for r in sub))
            for a_ in A_TAIL:
                k = f'a{int(100 * a_):02d}'
                rec[f'lose_{k}'] = sum(r[f'sign_{k}'] == 'lose' for r in sub)
                rec[f'win_{k}'] = sum(r[f'sign_{k}'] == 'win' for r in sub)
                rec[f'sign_changed_{k}'] = sum(r[f'sign_{k}'] != r['sign_linear'] for r in sub)
                rec[f'point_sign_flipped_{k}'] = sum((r['tau_linear'] > 0) != (r[f'tau_{k}'] > 0) for r in sub if r['tau_linear'] != 0)
            out.append(rec)
    return out


# ---------------------------------------------------------------- R18: C3 with the two-level bootstrap
def c3_two_level():
    import pandas as pd
    c = pd.read_csv(S.OUT / 'c3' / 'c3_team_games.csv')
    c['day'] = c['day'].astype(str)
    days = sorted({(s, d) for s, d in zip(c.season, c.day)})
    boot = S.Boot(days, [s for s, _ in days])
    boot_day = S.Boot(days, [s for s, _ in days], two_level=False)
    recs = [dict(x) for x in c.to_dict('records')]
    out = []

    def share(cfg, cond=False):
        sel = lambda x: x['config'] == cfg and (bool(x['holds_conditional_other']) if cond else True)
        return S.per_day(recs, boot, lambda x: x['verdict_B'] == 'reversal', sel)

    def both(label, a, b, cond=False):
        n1, d1 = share(a, cond); n2, d2 = share(b, cond)
        pt, lo, hi = boot.diff_of_ratios(n1, d1, n2, d2)
        _, lo_d, hi_d = boot_day.diff_of_ratios(n1, d1, n2, d2)
        out.append(dict(quantity=label, config_a=a, config_b=b, conditional_only=cond, n_a=int(d1.sum()),
                        share_a=float(n1.sum() / d1.sum()), share_b=float(n2.sum() / d2.sum()), diff=float(pt),
                        two_level_lo99=lo, two_level_hi99=hi, day_clustered_lo99=lo_d, day_clustered_hi99=hi_d))
    both('Y1: full 3-2-1 with ban (top-11) minus old rule', 'F1L1R1_A', 'F0L0R0_base')
    both('Y1: + field and balls (chain step 1)', 'F1L0R0_base', 'F0L0R0_base')
    both('Y1: + floor (chain step 2)', 'F1L1R0_base', 'F1L0R0_base')
    both('Y1: + restrictions (chain step 3)', 'F1L1R1_base', 'F1L1R0_base')
    both('Y1: + ban, top-11 (chain step 4)', 'F1L1R1_A', 'F1L1R1_base')
    both('Y1: + ban, top-16 (chain step 4)', 'F1L1R1_B', 'F1L1R1_base')
    both('H3: with ban (top-11) minus without, conditional holders', 'F1L1R1_A', 'F1L1R1_base', True)
    both('H3: with ban (top-16) minus without, conditional holders', 'F1L1R1_B', 'F1L1R1_base', True)
    return out


# ---------------------------------------------------------------- R19: first-window-day games before the clock-time mark
def first_day_games():
    import json
    from datetime import datetime
    games = E.load_games(H.GAMES)
    out = []
    for s in SEASONS:
        first = sorted((S.SIMULATIONS / 'primary' / s).glob('exposures_*.npz'))[0]
        meta = json.loads(bytes(np.load(first)['meta']).decode())
        cut = datetime.fromisoformat(meta['cutoff_utc'])
        start = E.late_window_start(games, s)
        rem = [g for g in games if g['season'] == s and not g['end'] < cut]
        before = [g for g in rem if g['start'] < start]
        focal = len(meta['focal_teams'])
        out.append(dict(season=s, first_window_day=meta['day'], focal_games_first_day=focal,
                        remaining_games_from_cutoff=len(rem), late_window_games_E4=len(rem) - len(before),
                        first_day_games_before_clock_mark=len(before),
                        before_mark_games_are_focal=any(g['start'] >= start for g in before)))   # by construction False: focal games start at or after the mark
    return out


# ---------------------------------------------------------------- R21: the stakes network, actual portfolios against own picks only
def network_contrast(tag='primary'):
    """Per focal game and rule, the linear-curve stake measures of Section 5.3 computed twice: on the actual
    portfolios (DB) and on the own-pick-only portfolios (DB_own), so that the part of the third-party network
    that traded and protected rights create can be separated from the part that rank interaction alone creates
    (a third party's own pick moves when the focal result moves the standings; Lemma 3). Materiality |s| >= delta
    as registered; TP is the share of the material stake held by teams not playing, defined when any team is
    materially staked."""
    v = CURVES['linear']
    rows = []
    for f in sorted((S.SIMULATIONS / tag).glob('*/exposures_*.npz')):
        d = S.load_day(f); meta = d['meta']
        for g, (h, a) in enumerate(meta['focal_teams']):
            third = np.array([x for x in range(30) if x not in (h, a)])
            for ri, r in enumerate(S.RULES):
                rec = dict(season=meta['season'], day=meta['day'], game_id=meta['focal_game_ids'][g], rule=r)
                for pf, src in (('actual', d['DB']), ('own', d['DB_own'])):
                    s_ = (-(src[:, g, ri] @ v)).mean(0)
                    mat = np.abs(s_) >= S.DELTA
                    tot = float(np.abs(s_[mat]).sum())
                    th = float(np.abs(s_[third][mat[third]]).sum())
                    rec[f'{pf}_n_material'] = int(mat.sum())
                    rec[f'{pf}_n_third_material'] = int(mat[third].sum())
                    rec[f'{pf}_mean_abs_third'] = th / len(third)
                    rec[f'{pf}_tp'] = th / tot if tot > 0 else float('nan')
                    rec[f'{pf}_third_dominated'] = bool(tot > 0 and th / tot > 0.5)
                rows.append(rec)
    return rows


def summarise_network(rows):
    days = sorted({(r['season'], r['day']) for r in rows})
    boot = S.Boot(days, [s for s, _ in days])
    out = []
    for rule in S.RULES:
        sub = [r for r in rows if r['rule'] == rule]
        rec = dict(rule=rule, games=len(sub))
        for pf in ('actual', 'own'):
            tp = [r[f'{pf}_tp'] for r in sub if r[f'{pf}_tp'] == r[f'{pf}_tp']]
            rec[f'{pf}_tp_defined'] = len(tp); rec[f'{pf}_tp_median'] = float(np.median(tp)); rec[f'{pf}_tp_mean'] = float(np.mean(tp))
            rec[f'{pf}_third_dominated_share'] = float(np.mean([r[f'{pf}_third_dominated'] for r in sub if r[f'{pf}_tp'] == r[f'{pf}_tp']]))
            rec[f'{pf}_mean_abs_third'] = float(np.mean([r[f'{pf}_mean_abs_third'] for r in sub]))
            rec[f'{pf}_mean_n_material'] = float(np.mean([r[f'{pf}_n_material'] for r in sub]))
            rec[f'{pf}_mean_n_third_material'] = float(np.mean([r[f'{pf}_n_third_material'] for r in sub]))
        # paired differences actual - own on the same games, two-level bootstrap by day
        for key, cond in (('mean_abs_third', lambda r: True), ('tp', lambda r: r['actual_tp'] == r['actual_tp'] and r['own_tp'] == r['own_tp']),
                          ('n_third_material', lambda r: True)):
            num = np.zeros(len(days)); den = np.zeros(len(days))
            for r in sub:
                if cond(r):
                    i = boot.idx[(r['season'], r['day'])]
                    num[i] += r[f'actual_{key}'] - r[f'own_{key}']; den[i] += 1
            pt, lo, hi = boot.ratio(num[:, None], den[:, None])
            rec[f'diff_{key}'] = float(pt[0]); rec[f'diff_{key}_lo99'] = float(lo[0]); rec[f'diff_{key}_hi99'] = float(hi[0]); rec[f'diff_{key}_n'] = int(den.sum())
        out.append(rec)
    return out


# ---------------------------------------------------------------- R22: the simultaneous band with a Bonferroni adjustment over the three looks
LOOK_LEVEL = 1 - 0.01 / 3


def crit_at(Cb, level):
    """The multiplier sup-t critical value of analysis.band_stats at an arbitrary level."""
    import math
    Cb = np.asarray(Cb, float); B = Cb.shape[0]
    m = Cb.mean(0); sd = Cb.std(0, ddof=1); se = sd / math.sqrt(B)
    ok = sd > 1e-12
    if not ok.any():
        return m, se, 0.0
    resid = (Cb[:, ok] - m[ok]) / (sd[ok] * math.sqrt(B - 1))
    Zs = np.abs(S._xi(B) @ resid)
    return m, se, float(np.quantile(Zs.max(1), level))


def look_adjusted(tag='primary'):
    """Every class-B verdict and H1 crossing re-read from the same 50 super-batches with the band's critical
    value taken at level 1 - 0.01/3 instead of 0.99, so that, by Bonferroni over the three looks, the event that
    the band fails to cover at some look has probability at most 1% whatever the dependence between looks.
    The run's stopping rule is unchanged; this is a post hoc re-reading of the final data, like precision matching."""
    rows = []
    for f in sorted((S.SIMULATIONS / tag).glob('*/exposures_*.npz')):
        d = S.load_day(f); meta = d['meta']
        ranks, _ = S.cutoff_ranks(meta)
        for g, (h, a) in enumerate(meta['focal_teams']):
            for side, c in ((0, h), (1, a)):
                sgn = 1.0 if side == 0 else -1.0
                for pf, src in (('actual', d['DB']), ('own', d['DB_own'])):
                    for ri, r in enumerate(S.RULES):
                        Cb = np.cumsum(sgn * src[:, g, ri, c, :], axis=1)
                        m, se, c99 = crit_at(Cb, 0.99)
                        _, _, cla = crit_at(Cb, LOOK_LEVEL)
                        v0, _ = S.verdict(m, se, c99, 30)
                        v1, j1 = S.verdict(m, se, cla, 30)
                        rows.append(dict(season=meta['season'], day=meta['day'], game_id=meta['focal_game_ids'][g], team=TEAMS[c],
                                         rank=int(ranks[c]), band=S.band_of(int(ranks[c])), rule=r, portfolio=pf,
                                         verdict_B=v0, crossing=S.crossing(m, se, c99), verdict_B_look=v1, jstar_B_look=j1,
                                         crossing_look=S.crossing(m, se, cla), crit_B=c99, crit_B_look=cla))
    return rows


def summarise_look_adjusted(rows):
    days = sorted({(r['season'], r['day']) for r in rows})
    boot = S.Boot(days, [s for s, _ in days])
    out = []
    for field in ('verdict_B', 'verdict_B_look'):
        cr = 'crossing' if field == 'verdict_B' else 'crossing_look'
        for pf in ('actual', 'own'):
            rec = dict(verdicts=field, portfolio=pf)
            for rule in S.RULES:
                sel = lambda x, rule=rule: x['rule'] == rule and x['portfolio'] == pf
                for v in S.VERDICTS:
                    n, d_ = S.per_day(rows, boot, lambda x, v=v: x[field] == v, sel)
                    rec[f'{rule}_{v}'] = float(n.sum() / d_.sum())
                rec[f'{rule}_changed_vs_primary'] = sum(1 for x in rows if sel(x) and x[field] != x['verdict_B'])
            n1, d1 = S.per_day(rows, boot, lambda x: x[field] == 'reversal', lambda x: x['rule'] == 'new' and x['portfolio'] == pf)
            n2, d2 = S.per_day(rows, boot, lambda x: x[field] == 'reversal', lambda x: x['rule'] == 'old' and x['portfolio'] == pf)
            pt, lo, hi = boot.diff_of_ratios(n1, d1, n2, d2)
            rec.update(diff_new_minus_old=float(pt), lo99=lo, hi99=hi)
            band = [x for x in rows if x['portfolio'] == pf and x['rule'] == 'new' and 2 <= x['rank'] <= 5]
            rev = [x for x in band if x[field] == 'reversal']
            rec['h1_band_reversals'] = len(rev); rec['h1_band_crossings'] = sum(1 for x in rev if x[cr])
            out.append(rec)
    return out


def main():
    rows = day_pass()
    write('R16_R17_team_games', rows)
    write('R16_rollover_dominance', summarise_rollover(rows))
    write('R17_tail_value', summarise_tail(rows))
    write('R18_c3_two_level', c3_two_level())
    write('R19_first_day_games', first_day_games())
    la = look_adjusted()
    write('R22_look_adjusted_team_games', la)
    write('R22_look_adjusted', summarise_look_adjusted(la))
    net = network_contrast()
    write('R21_network_games', net)
    write('R21_network_contrast', summarise_network(net))
    print('wrote', OUT)


if __name__ == '__main__':
    main()

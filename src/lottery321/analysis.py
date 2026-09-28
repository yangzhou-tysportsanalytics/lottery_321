"""simulation: registered analysis of the league-wide exposure files (paper Section 5).

Implements registration/run_registration.md and addendum A1 exactly; nothing here is tuned on outputs.
  * C1: per team-game verdicts from the curve-free bounds (sup-t simultaneous 99% band over j, A1 s.1),
        reversal slot j*, crossing flag, tau on the four curves, portfolio effect, attribution splits.
  * C2: per game stakes of all 30 teams, third-party share, HHI, typology, H2 sample, on all four curves.
  * Delta tau, H1 and H2 tests, day-clustered bootstrap intervals (A1 s.4), restriction comparison (s.5.4).
  * A1 amendment 9: bootstrap-t bands, the three-look constant, the delta margin on reversals,
    materiality-restricted stakes, the two-level bootstrap, precision-matched verdicts and the
    verdict x stopping-look table, the per-slot conservation diagnostic, all four curves,
    delta tau in the precision diagnostic, and both j* definitions and the state-conditional
    router features as reported splits.
Inputs: simulations/<tag>/<season>/exposures_<day>.npz (written by simulate.save).
Usage:
  python analysis.py <tag> [--exclude-imprecise] [--out DIR]
  python analysis.py --compare primary norestr [--out DIR]
Every table is written as CSV plus one markdown report. The script never prints team-level numbers to the
console; it prints counts only.
"""
import argparse
import csv
import io
import json
import math
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
for p in (HERE, HERE / 'ledgers'):
    sys.path.insert(0, str(p))

from teams import TEAMS  # noqa: E402
from value import CURVES  # noqa: E402

ROOT = HERE.parents[1]
SIMULATIONS = ROOT / 'simulations'
OUT = ROOT / 'results'

# ---------------------------------------------------------------- constants fixed by the registration / A1
Z = 2.935199                 # Phi^-1(1 - 0.01/6): two-sided 99%, Bonferroni over the three looks.
                             # A1 amendment 9: the runs' stopping rule used the two-look constant
                             # 2.807034; the difference is disclosed with the results.
DELTA = 0.003                # equivalence margin = precision target
SUPT_DRAWS = 10_000          # Gaussian multipliers, kept as the reported diagnostic band
SUPT_SEED = 20260922
BOOTT_REPS = 2_000           # A1 amendment 9: studentised bootstrap-t over the stored super-batches
BOOTT_SEED = 20260922
BOOT_REPS = 9_999
BOOT_SEED = 2026092201
BOOT_LEVEL = 0.99
BANDS = ((1, 3, '1-3'), (4, 10, '4-10'), (11, 16, '11-16'), (17, 30, '17-30'))
H1_BAND = (2, 5)
SEED_CUTS = (0.01, 0.05)
RULES = ('old', 'new')
PORTFOLIOS = ('actual', 'own')
VERDICTS = ('dominance_positive', 'reversal', 'negligible', 'unresolved')
TYPES = ('both_lose', 'both_win', 'normal', 'opposed', 'one_sided_win', 'no_own_stake')
# A1 amendment 10: rollover valuation of the mass channel. A right that fails to convey is worth rho of an
# average first-round pick in a later draft, so tau_rho = tau - rho * vbar * M with vbar = mean_k v(k) and
# M = C(30). rho = 0 is the registered primary. Reported as a magnitude under an explicitly different
# valuation, not as the tau of any curve in the registered class: at rho > 0 the no-pick outcome outranks
# slot 30, whose value is zero on all four curves, so the class ordering does not hold.
RHOS = (0.5, 0.8)
VBAR = {name: float(np.mean(v)) for name, v in CURVES.items()}

_XI = {}
_COUNTS = {}


def _xi(B):
    """Common Gaussian multipliers for the diagnostic sup-t band (fixed seed, one matrix per batch count)."""
    if B not in _XI:
        _XI[B] = np.random.default_rng(SUPT_SEED).standard_normal((SUPT_DRAWS, B))
    return _XI[B]


def _counts(B):
    """Resampling counts for the bootstrap-t: row r holds how often each batch is drawn (fixed seed)."""
    if B not in _COUNTS:
        rng = np.random.default_rng(BOOTT_SEED)
        draw = rng.integers(0, B, size=(BOOTT_REPS, B))
        _COUNTS[B] = np.stack([np.bincount(row, minlength=B) for row in draw]).astype(float)
    return _COUNTS[B]


# ---------------------------------------------------------------- per team-game statistics
def band_stats(Cb):
    """Cb: (B, 30) batch values of C(j). Returns mean, se and the simultaneous 99% critical values.

    'B' and 'C' are the Gaussian-multiplier sup-t values (Montiel Olea & Plagborg-Moller 2019), the band of
    the original registration, used everywhere. 'B_boott' and 'C_boott' are the studentised bootstrap-t
    values that A1 amendment 9 made primary; they are kept as a diagnostic only. After the primary
    tables were produced, the registered diagnostic T5_0d showed that the bootstrap-t degenerates on
    rare-event coordinates: where C(j) is zero (float32 noise, ~1e-9) in most batches and nonzero in a few,
    every resample that omits the few has se*(j) ~ 1e-10 against |C*(j) - C_hat(j)| ~ C_hat(j), and the 99%
    quantile explodes (to 1e15 in the data; 29% of team-games had c > 10). The band was re-chosen by a
    criterion fixed before the comparison (addendum A1, amendment 12):
    the multiplier band. It under-covers slightly (98.2% for a nominal 99% in the Gaussian design), which is
    stated with the results. Coordinates with zero batch variance are excluded from the maximum.
    """
    Cb = np.asarray(Cb, float); B = Cb.shape[0]
    m = Cb.mean(0); sd = Cb.std(0, ddof=1); se = sd / math.sqrt(B)
    ok = sd > 1e-12
    crit = {'B': 0.0, 'C': 0.0, 'B_boott': 0.0, 'C_boott': 0.0}
    if not ok.any():
        return m, se, crit
    idx = np.nonzero(ok)[0]
    sub = idx < 29
    X = Cb[:, ok]
    # multiplier band: the primary band (see the docstring)
    resid = (X - m[ok]) / (sd[ok] * math.sqrt(B - 1))
    Zs = np.abs(_xi(B) @ resid)
    crit['B'] = float(np.quantile(Zs.max(1), 0.99))
    crit['C'] = float(np.quantile(Zs[:, sub].max(1), 0.99)) if sub.any() else 0.0
    # studentised bootstrap-t (diagnostic): resampled means and standard errors from batch counts
    W = _counts(B)
    mb = (W @ X) / B
    sq = (W @ (X ** 2))
    var = np.maximum((sq - B * mb ** 2) / (B - 1), 0.0)
    seb = np.sqrt(var / B)
    T = np.abs(mb - m[ok]) / np.where(seb > 0, seb, np.inf)
    crit['B_boott'] = float(np.quantile(T.max(1), 0.99))
    crit['C_boott'] = float(np.quantile(T[:, sub].max(1), 0.99)) if sub.any() else 0.0
    return m, se, crit


def verdict(m, se, c, J):
    """A1 s.1 with amendment 9: negligible, reversal, dominance_positive, unresolved, in that order.
    Reversal now carries the same equivalence margin as dominance: the upper band must fall below -delta,
    so a dip smaller than delta is not called a reversal while its mirror image is called dominance."""
    m, se = m[:J], se[:J]
    up, lo = m + c * se, m - c * se
    if np.all(np.abs(m) + c * se < DELTA):
        return 'negligible', 0
    if np.any(up < -DELTA):
        return 'reversal', int(np.argmin(up)) + 1
    if np.all(lo >= -DELTA) and np.any(lo > 0):
        return 'dominance_positive', 0
    return 'unresolved', 0


def crossing(m, se, c):
    """H1 (ii): significantly negative at some j <= 11 and significantly positive at some j in 12..15."""
    up, lo = m + c * se, m - c * se
    return bool(np.any(up[:11] < 0) and np.any(lo[11:15] > 0))


def curve_sign(mean, se):
    lo, hi = mean - Z * se, mean + Z * se
    if lo > -DELTA and hi < DELTA:
        return 'neutral'
    if lo > 0:
        return 'lose'
    if hi < 0:
        return 'win'
    return 'neutral'


def tau_stats(db):
    """db: (B, 30) batch loss-minus-win slot differences. Returns {curve: (mean, se, sign)}."""
    out = {}
    for name, v in CURVES.items():
        t = db @ v
        m, se = float(t.mean()), float(t.std(ddof=1) / math.sqrt(len(t)))
        out[name] = (m, se, curve_sign(m, se))
    return out


def tau_rho(db, rho):
    """A1 amendment 10: tau under the rollover valuation, per curve, from the same batch means.

    tau_rho = tau - rho * vbar * M with M = C(30) = sum_k d(k). Computed batch by batch so that the
    standard error is the batch-means standard error of the adjusted quantity, not of tau alone."""
    M = db.sum(axis=1)
    out = {}
    for name, v in CURVES.items():
        t = db @ v - rho * VBAR[name] * M
        out[name] = (float(t.mean()), float(t.std(ddof=1) / math.sqrt(len(t))))
    return out


def band_of(rank):
    for lo, hi, name in BANDS:
        if lo <= rank <= hi:
            return name
    raise ValueError(rank)


def seed_group(tv):
    return '<0.01' if tv < SEED_CUTS[0] else ('0.01-0.05' if tv < SEED_CUTS[1] else '>=0.05')


# ---------------------------------------------------------------- ledger features (routers only)
_CLAIMS = {}
_CLAIM_SUM = {}


def slot_claims(year, n_perm=20000, seed=1):
    """Registered reading (A1 amendment 4): apply the router to 20,000 uniform complete draft orders, seed 1.

    Returns (seen, tot, pooled) with seen[native][holder][k] = the number of sampled orders in which the
    native sits at slot k+1 and the holder receives its pick, and tot[native][k] = orders with the native
    at that slot. Keeping the slot dimension is what lets the state-conditional variant of amendment 9
    item 9 be read off the same draws."""
    if year in _CLAIMS:
        return _CLAIMS[year]
    import importlib
    mod = importlib.import_module(f'router_{year}')
    rng = np.random.default_rng(seed)
    seen = {t_: defaultdict(lambda: np.zeros(30, int)) for t_ in TEAMS}
    tot = {t_: np.zeros(30, int) for t_ in TEAMS}
    for _ in range(n_perm):
        perm = rng.permutation(30) + 1
        pos = {t_: int(s) for t_, s in zip(TEAMS, perm)}
        route = mod.route(pos)
        for t_ in TEAMS:
            k = pos[t_] - 1
            seen[t_][route[pos[t_]]][k] += 1
            tot[t_][k] += 1
    pooled = {t_ for pl in getattr(mod, 'POOLS', ()) for t_ in pl}
    _CLAIMS[year] = ({t_: dict(hs) for t_, hs in seen.items()}, tot, pooled)
    return _CLAIMS[year]


def claims(year, reach=None, reach_key=None):
    """claims[native] = {holder: 'all'|'some'} over the sampled orders; 'all' = the holder receives the
    native's pick at every slot seen, 'some' = only at some.

    With `reach` — a (30, 30) boolean mask of the slots each native can actually reach in that season's
    window (`reachable_slots`) — only reachable slots are counted. That is the state-conditional
    version registered as a robustness split in A1 amendment 9 item 9: under uniform permutations a
    playoff team's top-14 protection is scored conditional even though its pick can never fall inside
    the protected range, which dilutes the H2 and H3 samples."""
    ck = (year, reach_key if reach is None else (reach_key or id(reach)))
    if ck in _CLAIM_SUM:
        return _CLAIM_SUM[ck]
    seen, tot, pooled = slot_claims(year)
    out = {}
    for i, t_ in enumerate(TEAMS):
        mask = tot[t_] > 0 if reach is None else (tot[t_] > 0) & np.asarray(reach)[i]
        d = {}
        for h, c in seen[t_].items():
            if not mask.any() or c[mask].sum() == 0:
                continue
            d[h] = 'all' if np.array_equal(c[mask], tot[t_][mask]) else 'some'
        out[t_] = d
    _CLAIM_SUM[ck] = (out, pooled)
    return _CLAIM_SUM[ck]


def features(year, c, o, restricted, cl=None, pooled=None):
    """Ledger features of team c (index) against opponent o (index) in draft `year`."""
    if cl is None:
        cl, pooled = claims(year)
    C, O = TEAMS[c], TEAMS[o]
    held = {n: k for n, hs in cl.items() for h, k in hs.items() if h == C and n != C}
    return {'holds_conditional_other': any(k == 'some' for k in held.values()),
            'holds_opponent_pick': O in held,
            'holds_pooled_pick': any(n in pooled for n in held) or (C in pooled),
            'self_restricted': C in restricted, 'opp_restricted': O in restricted}


def third_party_claim(year, h, a, cl=None):
    """True if a third team holds (fully or conditionally) the native first of h or a (H2 sample)."""
    if cl is None:
        cl, _ = claims(year)
    H_, A_ = (TEAMS[h], TEAMS[a]) if isinstance(h, (int, np.integer)) else (h, a)
    return any(hd not in (H_, A_) for n in (H_, A_) for hd in cl[n])


# ---------------------------------------------------------------- day context (cutoff ranks, recomputed)
_GAMES = None


def cutoff_ranks(meta):
    """League rank by winning percentage at the cutoff (worst = 1; A1 amendment 1); ties by the draft-tie priority of the first world of
    look 1 (rng = default_rng(seed); draws ug, us, up, ud in league_sim order). Returns (rank array, n_remaining)."""
    global _GAMES
    import elo as E
    import simulate as H
    from cutoff_state import build_state
    if _GAMES is None:
        _GAMES = E.load_games(H.GAMES)
    cut = datetime.fromisoformat(meta['cutoff_utc'])
    st = build_state(_GAMES, meta['season'], cut)
    G = len(st['remaining'])
    rng = np.random.default_rng(meta['seed'])
    rng.random(G); rng.random(30); rng.random(6); ud = rng.random(30)
    w = st['wins'].astype(float); l = st['h2h_wins'].sum(0).astype(float)
    pct = np.where(w + l > 0, w / np.maximum(w + l, 1), 0.5)
    order = sorted(range(30), key=lambda t: (pct[t], ud[t]))
    rank = np.empty(30, int)
    for r, t in enumerate(order):
        rank[t] = r + 1
    return rank, G


def load_day(path):
    z = np.load(path)
    meta = json.loads(bytes(z['meta']).decode())
    return {'DB': z['DB'].astype(float), 'DB_own': z['DB_own'].astype(float), 'Q': z['Q'], 'ST': z['ST'],
            'meta': meta}


# ---------------------------------------------------------------- per-day rows
def analyse_day(d, ranks=None):
    meta = d['meta']; season = meta['season']; day = meta['day']
    year = int(season[:4]) + 1
    restricted = set(meta.get('min_pick_new', {}))
    if ranks is None:
        ranks, G = cutoff_ranks(meta)
        if G != meta['remaining_games']:
            raise ValueError(f'{day}: remaining games differ from the run metadata')
    DB, DBo, ST = d['DB'], d['DB_own'], d['ST']
    cl, pooled = claims(year)
    nw = int(meta['n_worlds'])
    tg_rows, game_rows, prof = [], [], []
    for g, (h, a) in enumerate(meta['focal_teams']):
        gid = meta['focal_game_ids'][g]
        sides = ((0, h, a), (1, a, h))
        side_sign = {}
        for side, c, o in sides:
            sgn = 1.0 if side == 0 else -1.0
            tv = 0.5 * float(np.abs(ST[g, 1 if side == 0 else 0, c] - ST[g, 0 if side == 0 else 1, c]).sum())
            feat = features(year, c, o, restricted, cl, pooled)
            for pf, src in (('actual', DB), ('own', DBo)):
                series = {r: sgn * src[:, g, ri, c, :] for ri, r in enumerate(RULES)}
                series['delta'] = series['new'] - series['old']
                for r, db in series.items():
                    Cb = np.cumsum(db, axis=1)
                    m, se, crit = band_stats(Cb)
                    vB, jB = verdict(m, se, crit['B'], 30)
                    vC, jC = verdict(m, se, crit['C'], 29)
                    ts = tau_stats(db)
                    row = {'season': season, 'day': day, 'game_id': gid, 'side': 'home' if side == 0 else 'away',
                           'team': TEAMS[c], 'opp': TEAMS[o], 'rank': int(ranks[c]), 'band': band_of(int(ranks[c])),
                           'rule': r, 'portfolio': pf, 'verdict_B': vB, 'jstar_B': jB, 'verdict_C': vC,
                           'jstar_C': jC, 'crossing': crossing(m, se, crit['B']), 'crit_B': crit['B'],
                           'crit_C': crit['C'], 'crit_B_boott': crit['B_boott'],
                           # A1 amendment 9 item 9: the registered j* is the argmin of the upper band;
                           # the argmin of C_hat itself, which is what the exact kernel difference F3 - F4 predicts, is reported beside it
                           'jstar_hat_B': int(np.argmin(m)) + 1, 'jstar_hat_C': int(np.argmin(m[:29])) + 1,
                           'seeding_tv': tv, 'seed_group': seed_group(tv), 'n_worlds': nw,
                           'band_ratio': float(crit['B'] * np.max(se) / DELTA),
                           'precision_met': bool(meta['precision_met'])}
                    for name, (tm, tse, tsg) in ts.items():
                        row[f'tau_{name}'] = tm; row[f'se_{name}'] = tse; row[f'sign_{name}'] = tsg
                    row['M'] = float(m[29])                      # C(30), the mass channel
                    for rho in RHOS:                             # A1 amendment 10
                        tag = f'rho{int(rho * 100)}'
                        for name, (tm, tse) in tau_rho(db, rho).items():
                            row[f'tau_{name}_{tag}'] = tm; row[f'se_{name}_{tag}'] = tse
                    row.update(feat)
                    row['_m'] = m; row['_se'] = se           # kept in memory for the precision-matched pass only
                    tg_rows.append(row)
                    prof.append((season, day, band_of(int(ranks[c])), r, pf, m))
                    if pf == 'actual' and r in RULES:
                        for cvn, (_, _, tsg) in ts.items():
                            side_sign[(side, r, cvn)] = tsg
        # ---- C2: stakes of all 30 teams. A1 amendment 9 item 7: on all four curves, not the linear one only.
        for ri, r in enumerate(RULES):
            for cv, v in CURVES.items():
                s_b = -(DB[:, g, ri] @ v)                      # (B, 30): value to each team of a home win
                s = s_b.mean(0)
                third = [x for x in range(30) if x not in (h, a)]
                # A1 amendment 9: |s| of a noisy estimate is biased upward, so the stake measures are
                # computed on materially staked teams only. The unrestricted versions are kept as diagnostics.
                mat = np.abs(s) >= DELTA
                tot_m = float(np.abs(s[mat]).sum()); tot = float(np.abs(s).sum())
                third_m = [x for x in third if mat[x]]
                tp = float(np.abs(s[third_m]).sum() / tot_m) if tot_m >= DELTA else float('nan')
                tp_raw = float(np.abs(s[third]).sum() / tot) if tot >= DELTA else float('nan')
                hhi = float(((np.abs(s[mat]) / tot_m) ** 2).sum()) if tot_m >= DELTA else float('nan')
                big = max(third, key=lambda x: abs(s[x]))
                big_holds = any(TEAMS[big] in cl[TEAMS[x]] for x in (h, a))
                sh, sa = side_sign[(0, r, cv)], side_sign[(1, r, cv)]
                game_rows.append({'season': season, 'day': day, 'game_id': gid, 'home': TEAMS[h], 'away': TEAMS[a],
                                  'rule': r, 'curve': cv, 'type': typology(sh, sa), 'tp_share': tp,
                                  'tp_share_raw': tp_raw, 'hhi': hhi, 'n_material': int(mat.sum()),
                                  'total_abs_stake': tot, 'total_abs_stake_material': tot_m,
                                  'mean_abs_third': float(np.abs(s[third_m]).sum() / len(third)),
                                  'mean_abs_third_raw': float(np.abs(s[third]).mean()),
                                  'largest_third': TEAMS[big], 'largest_third_holds_participant_pick': big_holds,
                                  'h2_sample': third_party_claim(year, h, a, cl),
                                  'zero_sum_dev': float(abs(s.sum())), 'n_worlds': nw,
                                  'precision_met': bool(meta['precision_met']),
                                  'stakes': [float(x) for x in s]})
    hw = lambda pred: max((Z * r['se_linear'] for r in tg_rows if r['portfolio'] == 'actual' and pred(r)), default=0.0)
    draws = int(meta.get('lottery_draws', 4))
    diag = {'season': season, 'day': day, 'precision_met': bool(meta['precision_met']),
            'n_worlds': nw, 'looks': meta['looks'],
            'q_total_dev': float(np.abs(d['Q'].sum(axis=(3, 4)) - 30.0).max()),
            # A1 amendment 9 item 7: the registered check is per slot, sum_c q(k) = 1. Under the hybrid
            # estimator it holds only in expectation (pooled natives are sampled, simple ones are exact), so
            # this is a noise diagnostic: the reference scale is one pooled sampling standard error.
            'per_slot_dev': float(np.abs(d['Q'].sum(axis=3) - 1.0).max()),
            'per_slot_expected': 1.0 / math.sqrt(max(draws * nw, 1)),
            'own_slot_dev': float(np.abs(DBo.sum(axis=3)).max()),
            # A1 amendment 9 item 7: the stopping rule includes delta tau, so the diagnostic does too
            'max_hw_linear': hw(lambda r: True),
            'max_hw_linear_rules_only': hw(lambda r: r['rule'] in RULES),
            'max_hw_delta_linear': hw(lambda r: r['rule'] == 'delta')}
    return tg_rows, game_rows, prof, diag


def add_precision_matched(rows, n_match=None):
    """A1 amendment 9 item 6 and item 9: restate every verdict at a common band width.

    A day's band width is set by its world count, so a day that ran 32,000 worlds is more likely to be
    called resolved than one that stopped at 2,000, and the own-pick portfolio (which carries no lottery
    sampling noise at all) is measured more precisely than the actual one. Monte Carlo standard errors
    scale as 1/sqrt(worlds), so each row is put back on the footing of the least precise day compared by
    multiplying its standard errors by sqrt(n / n_match); the point estimates are untouched. Returns the
    matching world count."""
    rows = [r for r in rows if '_se' in r]
    if not rows:
        return None
    n_match = n_match or min(r['n_worlds'] for r in rows)
    for r in rows:
        sc = math.sqrt(r['n_worlds'] / n_match)
        m, se = r['_m'], r['_se'] * sc
        r['verdict_B_pm'], r['jstar_B_pm'] = verdict(m, se, r['crit_B'], 30)
        r['verdict_C_pm'], r['jstar_C_pm'] = verdict(m, se, r['crit_C'], 29)
        r['crossing_pm'] = crossing(m, se, r['crit_B'])
        r['band_ratio_pm'] = float(r['crit_B'] * np.max(se) / DELTA)
        r['n_worlds_match'] = n_match
    return n_match


def state_conditional(tg, games, reach=None):
    """A1 amendment 9 item 9: the state-conditional version of the router features, as a split.

    The registered features stay as they are; these carry the suffix `_state` and are None when the
    reachable-slot file has not been produced."""
    if reach is None:
        try:
            import reachable_slots as RS
            reach = RS.load()
        except Exception:
            reach = None
    if not reach:
        for x in tg:
            x['holds_conditional_other_state'] = None; x['holds_opponent_pick_state'] = None
        for g in games:
            g['h2_sample_state'] = None
        return False
    rule_of = lambda x: 'old' if x['rule'] == 'old' else 'new'
    get = lambda season, rule: claims(int(season[:4]) + 1, reach.get((season, rule)), reach_key=(season, rule))
    for x in tg:
        cl, _ = get(x['season'], rule_of(x))
        held = {n: k for n, hs in cl.items() for hh, k in hs.items() if hh == x['team'] and n != x['team']}
        x['holds_conditional_other_state'] = any(k == 'some' for k in held.values())
        x['holds_opponent_pick_state'] = x['opp'] in held
    for g in games:
        cl, _ = get(g['season'], rule_of(g))
        g['h2_sample_state'] = third_party_claim(None, g['home'], g['away'], cl)
    return True


def typology(sh, sa):
    s = sorted([sh, sa])
    if s == ['lose', 'lose']:
        return 'both_lose'
    if s == ['win', 'win']:
        return 'both_win'
    if s == ['lose', 'neutral']:
        return 'normal'
    if s == ['lose', 'win']:
        return 'opposed'
    if s == ['neutral', 'win']:
        return 'one_sided_win'
    return 'no_own_stake'


# ---------------------------------------------------------------- day-clustered bootstrap (A1 s.4)
class Boot:
    """Cluster bootstrap over the run's days (A1 s.4 with amendment 9).

    Primary (`two_level=True`): resample seasons with replacement, then the days within each resampled
    season. Holding the season weights fixed, as the first registration did, excludes the season-level
    variance component, which is the dominant one here: six seasons, each with its own rights ledger.
    The within-season version is kept and reported as the narrower diagnostic.
    num/den arrays are (days, cells).
    """

    def __init__(self, day_keys, seasons, two_level=True):
        self.days = list(day_keys)
        self.idx = {k: i for i, k in enumerate(self.days)}
        self.two_level = two_level
        rng = np.random.default_rng(BOOT_SEED)
        D = len(self.days)
        by_season = defaultdict(list)
        for i, s in enumerate(seasons):
            by_season[s].append(i)
        names = sorted(by_season)
        W = np.zeros((BOOT_REPS, D))
        if two_level:
            pick = rng.integers(0, len(names), size=(BOOT_REPS, len(names)))
            for k, name in enumerate(names):
                ids = np.array(by_season[name]); n = len(ids)
                # how often this season was drawn in each replicate, and which of its days each copy takes
                times = (pick == k).sum(1)
                for copy in range(len(names)):
                    active = times > copy
                    if not active.any():
                        break
                    draw = rng.integers(0, n, size=(BOOT_REPS, n))
                    add = np.zeros((BOOT_REPS, n))
                    for j in range(n):
                        add[:, j] = (draw == j).sum(1)
                    W[np.ix_(active, ids)] += add[active]
        else:
            for name in names:
                ids = np.array(by_season[name]); n = len(ids)
                draw = rng.integers(0, n, size=(BOOT_REPS, n))
                for j in range(n):
                    W[:, ids[j]] = (draw == j).sum(1)
        self.W = W

    def ratio(self, num, den):
        num = np.atleast_2d(np.asarray(num, float).T).T; den = np.atleast_2d(np.asarray(den, float).T).T
        point = num.sum(0) / np.where(den.sum(0) > 0, den.sum(0), np.nan)
        bn = self.W @ num; bd = self.W @ den
        with np.errstate(invalid='ignore', divide='ignore'):
            b = bn / bd
        a = (1 - BOOT_LEVEL) / 2
        return point, np.nanquantile(b, a, axis=0), np.nanquantile(b, 1 - a, axis=0)

    def diff_of_ratios(self, n1, d1, n2, d2):
        """(sum n1 / sum d1) - (sum n2 / sum d2) with the same day weights."""
        n1, d1, n2, d2 = (np.asarray(x, float) for x in (n1, d1, n2, d2))
        point = n1.sum() / d1.sum() - n2.sum() / d2.sum()
        with np.errstate(invalid='ignore', divide='ignore'):
            b = (self.W @ n1) / (self.W @ d1) - (self.W @ n2) / (self.W @ d2)
        a = (1 - BOOT_LEVEL) / 2
        return point, float(np.nanquantile(b, a)), float(np.nanquantile(b, 1 - a))


def per_day(rows, boot, pred, den_pred=lambda r: True):
    num = np.zeros(len(boot.days)); den = np.zeros(len(boot.days))
    for r in rows:
        if den_pred(r):
            i = boot.idx[(r['season'], r['day'])]
            den[i] += 1; num[i] += bool(pred(r))
    return num, den


# ---------------------------------------------------------------- tables
VERDICT_FIELDS = (('B', 'verdict_B'), ('C', 'verdict_C'), ('B_pm', 'verdict_B_pm'), ('C_pm', 'verdict_C_pm'))


def share_table(rows, boot, groups, verdict_field_list=VERDICT_FIELDS):
    """groups: list of (label dict, filter). One row per group x class x verdict with share and 99% CI.

    A1 amendment 9 item 6: the `_pm` classes are the precision-matched restatement of the same verdicts
    (`add_precision_matched`); they are skipped when that pass has not been run."""
    out = []
    have = set(rows[0]) if rows else set()
    for label, filt in groups:
        for cls, field in verdict_field_list:
            if field not in have:
                continue
            nums, dens = [], []
            for v in VERDICTS:
                n, d_ = per_day(rows, boot, lambda r, v=v: r[field] == v, filt)
                nums.append(n); dens.append(d_)
            pt, lo, hi = boot.ratio(np.stack(nums, 1), np.stack(dens, 1))
            for k, v in enumerate(VERDICTS):
                out.append(dict(label, value_class=cls, verdict=v, share=pt[k], lo99=lo[k], hi99=hi[k],
                                n=int(dens[k].sum())))
    return out


def quantiles(x):
    x = np.asarray([v for v in x if v == v], float)
    if not len(x):
        return {'n': 0}
    return {'n': len(x), 'mean': float(x.mean()), 'q25': float(np.quantile(x, .25)),
            'median': float(np.median(x)), 'q75': float(np.quantile(x, .75)), 'q90': float(np.quantile(x, .9))}



def headline_reversal(tg, boot):
    """A1 amendment 11, headline quantities (H-a) and (H-b): the reversal share under 3-2-1 and under the
    old rule, and their paired difference with a two-level bootstrap 99% interval, for each portfolio and
    for the registered and precision-matched class-B verdicts; plus the portfolio gap (actual minus own)
    under each rule."""
    out = []
    rev = lambda f: (lambda x: x.get(f) == 'reversal')
    sel = lambda r, pf: (lambda x: x['rule'] == r and x['portfolio'] == pf)
    for pf in PORTFOLIOS:
        for f in ('verdict_B', 'verdict_B_pm'):
            n1, d1 = per_day(tg, boot, rev(f), sel('new', pf))
            n2, d2 = per_day(tg, boot, rev(f), sel('old', pf))
            if d1.sum() == 0 or d2.sum() == 0:
                continue
            pt, lo, hi = boot.diff_of_ratios(n1, d1, n2, d2)
            out.append(dict(contrast='new_minus_old', portfolio=pf, verdict=f, share_a=float(n1.sum() / d1.sum()),
                            share_b=float(n2.sum() / d2.sum()), diff=float(pt), lo99=float(lo), hi99=float(hi),
                            n=int(d1.sum())))
    for r in RULES:
        n1, d1 = per_day(tg, boot, rev('verdict_B'), sel(r, 'actual'))
        n2, d2 = per_day(tg, boot, rev('verdict_B'), sel(r, 'own'))
        if d1.sum() == 0 or d2.sum() == 0:
            continue
        pt, lo, hi = boot.diff_of_ratios(n1, d1, n2, d2)
        out.append(dict(contrast='actual_minus_own', portfolio=r, verdict='verdict_B', share_a=float(n1.sum() / d1.sum()),
                        share_b=float(n2.sum() / d2.sum()), diff=float(pt), lo99=float(lo), hi99=float(hi),
                        n=int(d1.sum())))
    return out


def build_tables(tg, games, profs, diags, boot):
    T = {}
    rp = lambda r, rule, pf: r['rule'] == rule and r['portfolio'] == pf
    # 5.0 diagnostics
    looks = defaultdict(int)
    for dg in diags:
        looks[dg['n_worlds'] if dg['precision_met'] else 'missed'] += 1
    hw = [dg['max_hw_linear'] for dg in diags]
    hwr = [dg['max_hw_linear_rules_only'] for dg in diags]
    T['T5_0_diagnostics'] = [{'states': len(diags), 'games': len({(g['season'], g['day'], g['game_id']) for g in games}),
                              'stopped_2000': looks.get(2000, 0), 'stopped_8000': looks.get(8000, 0),
                              'stopped_32000': looks.get(32000, 0), 'missed_target': looks.get('missed', 0),
                              'n_worlds_match': tg[0].get('n_worlds_match') if tg else None,
                              'max_halfwidth_linear': max(hw) if hw else float('nan'),
                              'max_halfwidth_linear_rules_only': max(hwr) if hwr else float('nan'),
                              'max_halfwidth_delta_linear': max(dg['max_hw_delta_linear'] for dg in diags),
                              'p95_halfwidth_linear': float(np.quantile(hw, .95)) if hw else float('nan'),
                              'max_q_total_dev': max(dg['q_total_dev'] for dg in diags),
                              'max_per_slot_dev': max(dg['per_slot_dev'] for dg in diags),
                              'per_slot_noise_scale': max(dg['per_slot_expected'] for dg in diags),
                              'max_own_slot_dev': max(dg['own_slot_dev'] for dg in diags),
                              'max_zero_sum_dev': max(g['zero_sum_dev'] for g in games)}]
    T['T5_0b_zero_sum_by_curve'] = [{'curve': cv, 'rule': r,
                                     'max_zero_sum_dev': max(g['zero_sum_dev'] for g in games
                                                             if g['curve'] == cv and g['rule'] == r),
                                     'mean_zero_sum_dev': float(np.mean([g['zero_sum_dev'] for g in games
                                                                         if g['curve'] == cv and g['rule'] == r])),
                                     'n_games': sum(1 for g in games if g['curve'] == cv and g['rule'] == r)}
                                    for cv in CURVES for r in RULES]
    # A1 amendment 9 item 6: verdicts against the look a day stopped at, and item 9: the band
    # width each portfolio is measured at, so the portfolio contrast can be read against its precision gap.
    look = lambda x: str(x['n_worlds']) if x['precision_met'] else 'missed'
    ct = defaultdict(int)
    for x in tg:
        ct[(x['rule'], x['portfolio'], look(x), x['verdict_B'], x.get('verdict_B_pm', ''))] += 1
    T['T5_0c_verdict_by_look'] = [{'rule': r, 'portfolio': pf, 'stopped_at': lk, 'verdict_B': v,
                                   'verdict_B_pm': vpm, 'count': c}
                                  for (r, pf, lk, v, vpm), c in sorted(ct.items())]
    T['T5_0d_band_width'] = [dict(rule=r, portfolio=pf, measure=mm,
                                  **quantiles([x[mm] for x in tg if rp(x, r, pf)]))
                             for r in RULES + ('delta',) for pf in PORTFOLIOS
                             for mm in ('band_ratio', 'band_ratio_pm') if tg and mm in tg[0]]
    # 5.1 / 5.2
    groups = [({'rule': r, 'portfolio': pf}, lambda x, r=r, pf=pf: rp(x, r, pf)) for r in RULES + ('delta',) for pf in PORTFOLIOS]
    T['T5_1_verdicts'] = share_table(tg, boot, groups)
    groups = [({'rule': r, 'portfolio': pf, 'band': b}, lambda x, r=r, pf=pf, b=b: rp(x, r, pf) and x['band'] == b)
              for r in RULES for pf in PORTFOLIOS for _, _, b in BANDS]
    T['T5_2_verdicts_by_band'] = share_table(tg, boot, groups)
    # 5.3 reversal slot
    rows = []
    for r in RULES:
        for pf in PORTFOLIOS:
            sel = [x for x in tg if rp(x, r, pf) and x['verdict_B'] == 'reversal']
            js = [x['jstar_B'] for x in sel]
            jh = [x['jstar_hat_B'] for x in sel]           # A1 amendment 9 item 9
            spm = [x for x in tg if rp(x, r, pf) and x.get('verdict_B_pm') == 'reversal']
            jpm = [x['jstar_B_pm'] for x in spm]
            for j in range(1, 31):
                rows.append({'rule': r, 'portfolio': pf, 'jstar': j, 'count': js.count(j),
                             'count_argmin_C_hat': jh.count(j), 'count_precision_matched': jpm.count(j),
                             'n_reversals': len(js), 'n_reversals_pm': len(spm)})
    T['T5_3_reversal_slot'] = rows
    # figure 5.1 data
    acc = defaultdict(list)
    for season, day, b, r, pf, m in profs:
        acc[(b, r, pf)].append(m)
    T['F5_1_profiles'] = [dict(band=b, rule=r, portfolio=pf, j=j + 1, mean=float(np.mean([m[j] for m in ms])),
                               q10=float(np.quantile([m[j] for m in ms], .1)), q90=float(np.quantile([m[j] for m in ms], .9)),
                               n=len(ms)) for (b, r, pf), ms in sorted(acc.items()) for j in range(30)]
    # curve-specific
    rows = []
    for r in RULES + ('delta',):
        for pf in PORTFOLIOS:
            for b in [None] + [x[2] for x in BANDS]:
                sub = lambda x, r=r, pf=pf, b=b: rp(x, r, pf) and (b is None or x['band'] == b)
                for cv in CURVES:
                    q = quantiles([x[f'tau_{cv}'] for x in tg if sub(x)])
                    n1, d1 = per_day(tg, boot, lambda x, cv=cv: x[f'sign_{cv}'] == 'lose', sub)
                    n2, _ = per_day(tg, boot, lambda x, cv=cv: x[f'sign_{cv}'] == 'win', sub)
                    if d1.sum() == 0:
                        continue
                    pt, lo, hi = boot.ratio(np.stack([n1, n2], 1), np.stack([d1, d1], 1))
                    rows.append(dict(rule=r, portfolio=pf, band=b or 'all', curve=cv, **q,
                                     share_sig_pos=pt[0], pos_lo99=lo[0], pos_hi99=hi[0],
                                     share_sig_neg=pt[1], neg_lo99=lo[1], neg_hi99=hi[1]))
    T['T5_curves_and_T5_6_delta'] = rows
    # H1
    inb = lambda x: H1_BAND[0] <= x['rank'] <= H1_BAND[1]
    n_new, d_new = per_day(tg, boot, lambda x: x['sign_linear'] == 'win', lambda x: rp(x, 'new', 'own') and inb(x))
    n_old, d_old = per_day(tg, boot, lambda x: x['sign_linear'] == 'win', lambda x: rp(x, 'old', 'own') and inb(x))
    pt, lo, hi = boot.diff_of_ratios(n_new, d_new, n_old, d_old)
    nc, dc = per_day(tg, boot, lambda x: x['crossing'],
                     lambda x: rp(x, 'new', 'own') and inb(x) and x['verdict_B'] == 'reversal')
    cp, clo, chi = boot.ratio(nc[:, None], dc[:, None]) if dc.sum() else (np.array([np.nan]),) * 3
    T['H1'] = [{'n_team_games': int(d_new.sum()), 'share_neg_new': n_new.sum() / max(d_new.sum(), 1),
                'share_neg_old': n_old.sum() / max(d_old.sum(), 1), 'diff_new_minus_old': pt, 'diff_lo99': lo,
                'diff_hi99': hi, 'n_new_reversals': int(dc.sum()), 'crossing_share': float(cp[0]),
                'crossing_lo99': float(clo[0]), 'crossing_hi99': float(chi[0]),
                'supported': bool(lo > 0 and cp[0] > 0.5)}]
    # attribution: portfolio effect
    key = lambda x: (x['season'], x['day'], x['game_id'], x['side'])
    own = {(key(x), x['rule']): x for x in tg if x['portfolio'] == 'own'}
    rows = []
    for r in RULES + ('delta',):
        for b in [None] + [x[2] for x in BANDS]:
            eff = [x['tau_linear'] - own[(key(x), r)]['tau_linear'] for x in tg
                   if rp(x, r, 'actual') and (b is None or x['band'] == b)]
            rows.append(dict(rule=r, band=b or 'all', **quantiles(eff),
                             share_nonzero=float(np.mean(np.abs(eff) >= DELTA)) if eff else float('nan')))
    T['T5_attr_portfolio_effect'] = rows
    groups = [({'rule': r, 'portfolio': pf, 'seed_group': sg}, lambda x, r=r, pf=pf, sg=sg: rp(x, r, pf) and x['seed_group'] == sg)
              for r in RULES for pf in PORTFOLIOS for sg in ('<0.01', '0.01-0.05', '>=0.05')]
    # A1 amendment 10: the mass channel under the rollover valuation. Reported as magnitudes under an
    # explicitly different valuation of the "no pick" outcome, not as the tau of any registered curve.
    rows = []
    for r in RULES + ('delta',):
        for pf in PORTFOLIOS:
            for b in [None] + [x[2] for x in BANDS]:
                sub = lambda x, r=r, pf=pf, b=b: rp(x, r, pf) and (b is None or x['band'] == b)
                sel = [x for x in tg if sub(x)]
                if not sel:
                    continue
                rows.append(dict(rule=r, portfolio=pf, band=b or 'all', curve='-', rho=0.0,
                                 measure='M', **quantiles([x['M'] for x in sel])))
                for cv in CURVES:
                    base = [x[f'tau_{cv}'] for x in sel]
                    rows.append(dict(rule=r, portfolio=pf, band=b or 'all', curve=cv, rho=0.0,
                                     measure='tau', share_sign_flip=0.0, vbar=VBAR[cv], **quantiles(base)))
                    for rho in RHOS:
                        tag = f'rho{int(rho * 100)}'
                        adj = [x[f'tau_{cv}_{tag}'] for x in sel]
                        flip = float(np.mean([(a > 0) != (c > 0) for a, c in zip(adj, base)])) if base else float('nan')
                        rows.append(dict(rule=r, portfolio=pf, band=b or 'all', curve=cv, rho=rho,
                                         measure='tau', share_sign_flip=flip, vbar=VBAR[cv], **quantiles(adj)))
    T['T5_7_rollover'] = rows
    T['T5_attr_seeding'] = share_table(tg, boot, groups, (('B', 'verdict_B'),))
    rows = []
    for r in RULES:
        feats = ['holds_conditional_other', 'holds_opponent_pick', 'holds_pooled_pick', 'self_restricted',
                 'opp_restricted'] + [f for f in ('holds_conditional_other_state', 'holds_opponent_pick_state')
                                      if tg and tg[0].get(f) is not None]
        for f in feats:
            for val in (True, False):
                n, d_ = per_day(tg, boot, lambda x: x['verdict_B'] == 'reversal',
                                lambda x, r=r, f=f, val=val: rp(x, r, 'actual') and x[f] == val)
                if d_.sum() == 0:
                    rows.append(dict(rule=r, feature=f, value=val, n=0)); continue
                pt_, lo_, hi_ = boot.ratio(n[:, None], d_[:, None])
                rows.append(dict(rule=r, feature=f, value=val, n=int(d_.sum()), reversal_share=float(pt_[0]),
                                 lo99=float(lo_[0]), hi99=float(hi_[0])))
    T['T5_attr_ledger_features'] = rows
    # 5.3 transitions and delta verdicts are in T5_1 (rule = delta); transitions:
    newv = {(key(x), x['portfolio']): x['verdict_B'] for x in tg if x['rule'] == 'new'}
    trans = defaultdict(int)
    for x in tg:
        if x['rule'] == 'old':
            trans[(x['portfolio'], x['verdict_B'], newv[(key(x), x['portfolio'])])] += 1
    T['T5_6_transitions'] = [dict(portfolio=p, old=o, new=n, count=c) for (p, o, n), c in sorted(trans.items())]
    T['T5_headline_reversal_diff'] = headline_reversal(tg, boot)   # A1 amendment 11, (H-a) and (H-b)
    # C2. A1 amendment 9 item 7: every stake measure is reported on all four curves. The typology's
    # registered definition (A1 s.2) is the linear curve; the other three are reported beside it.
    rows = []
    for r in RULES:
        for cv in CURVES:
            sel = lambda x, r=r, cv=cv: x['rule'] == r and x['curve'] == cv
            nums, dens = [], []
            for ty in TYPES:
                n, d_ = per_day(games, boot, lambda x, ty=ty: x['type'] == ty, sel)
                nums.append(n); dens.append(d_)
            pt, lo, hi = boot.ratio(np.stack(nums, 1), np.stack(dens, 1))
            for k, ty in enumerate(TYPES):
                sub = [x for x in games if sel(x) and x['type'] == ty]
                dfn = [x for x in sub if x['tp_share'] == x['tp_share']]
                tpd = float(np.mean([x['tp_share'] > 0.5 for x in dfn])) if dfn else float('nan')
                # tp_dominated_share is a share of the games in which TP is defined; the count
                # of such games is kept so that the share can be aggregated over types correctly
                rows.append(dict(rule=r, curve=cv, type=ty, share=pt[k], lo99=lo[k], hi99=hi[k], n=len(sub),
                                 tp_dominated_share=tpd, n_tp_defined=len(dfn)))
    T['T5_4_typology'] = rows
    rows = []
    for r in RULES:
        for cv in CURVES:
            for m in ('tp_share', 'tp_share_raw', 'hhi', 'n_material', 'mean_abs_third', 'mean_abs_third_raw'):
                rows.append(dict(rule=r, curve=cv, measure=m,
                                 **quantiles([x[m] for x in games if x['rule'] == r and x['curve'] == cv])))
    by = {(x['season'], x['day'], x['game_id'], x['rule'], x['curve']): x for x in games}
    for cv in CURVES:
        for m in ('tp_share', 'hhi', 'mean_abs_third'):
            dif = [by[(s, dd, g, 'new', cv)][m] - by[(s, dd, g, 'old', cv)][m]
                   for (s, dd, g, r, c_) in by if r == 'old' and c_ == cv]
            rows.append(dict(rule='new_minus_old', curve=cv, measure=m, **quantiles(dif)))
    T['T5_5_stakes_distribution'] = rows
    # H2: mean paired difference in mean |third-party stake| over the H2 sample. Registered on the linear
    # curve and on the registered (uniform-permutation) sample; the other curves and the state-conditional
    # sample of amendment 9 item 9 are reported beside it.
    h2 = []
    samples = [('registered', 'h2_sample')] + ([('state_conditional', 'h2_sample_state')]
                                               if games and games[0].get('h2_sample_state') is not None else [])
    for cv in CURVES:
        for sname, sfield in samples:
            num = np.zeros(len(boot.days)); den = np.zeros(len(boot.days))
            for (s, dd, g, r, c_), x in by.items():
                if r == 'old' and c_ == cv and x[sfield]:
                    i = boot.idx[(s, dd)]
                    num[i] += by[(s, dd, g, 'new', cv)]['mean_abs_third'] - x['mean_abs_third']; den[i] += 1
            if not den.sum():
                h2.append({'curve': cv, 'sample': sname, 'n_games': 0}); continue
            pt, lo, hi = boot.ratio(num[:, None], den[:, None])
            h2.append({'curve': cv, 'sample': sname, 'n_games': int(den.sum()),
                       'mean_diff_new_minus_old': float(pt[0]), 'lo99': float(lo[0]), 'hi99': float(hi[0]),
                       'registered': bool(cv == 'linear' and sname == 'registered'),
                       'supported': bool(pt[0] > 0 and lo[0] > 0)})
    T['H2'] = h2
    # network edges (Figure 5.2; the linear curve, as the figure is defined)
    edges = defaultdict(float)
    for x in games:
        if x['curve'] != 'linear':
            continue
        for side_team in (x['home'], x['away']):
            for t, sv in zip(TEAMS, x['stakes']):
                if t not in (x['home'], x['away']):
                    edges[(x['season'], x['rule'], side_team, t)] += abs(sv)
    T['F5_2_network_edges'] = [dict(season=s, rule=r, game_team=a, holder=b, weight=w) for (s, r, a, b), w in sorted(edges.items())]
    return T


# ---------------------------------------------------------------- driver
def collect(tag, exclude_imprecise=False, root=SIMULATIONS, ranks_fn=None, n_match=None, reach=None):
    files = sorted((root / tag).glob('*/exposures_*.npz'))
    tg, games, profs, diags = [], [], [], []
    for f in files:
        d = load_day(f)
        if exclude_imprecise and not d['meta']['precision_met']:
            continue
        ranks = ranks_fn(d['meta']) if ranks_fn else None
        a, b, c, dg = analyse_day(d, ranks)
        tg += a; games += b; profs += c; diags.append(dg)
    add_precision_matched(tg, n_match)                 # A1 amendment 9 items 6 and 9
    state_conditional(tg, games, reach)                # A1 amendment 9 item 9
    return tg, games, profs, diags


def _public_cols(rows):
    """Column list for a CSV: the in-memory arrays kept for the precision-matched pass are dropped."""
    cols = []
    for r in rows:
        for k in r:
            if not k.startswith('_') and k not in cols:
                cols.append(k)
    return cols


def compare_restrictions(tg_p, tg_n):
    """Paper s.5.4: primary minus norestr on the same team-games (3-2-1 only). Groups: restricted natives,
    holders of a restricted native's pick (router claims), all other team-games."""
    key = lambda x: (x['season'], x['day'], x['game_id'], x['side'], x['portfolio'])
    nr = {key(x): x for x in tg_n if x['rule'] == 'new'}
    rows = defaultdict(list)
    for x in tg_p:
        if x['rule'] != 'new' or key(x) not in nr:
            continue
        year = int(x['season'][:4]) + 1
        cl, _ = claims(year)
        import simulate as H
        restricted = {TEAMS[t] for t in H.restrictions(year)}
        holds = any(x['team'] in cl[n] and n != x['team'] for n in restricted)
        grp = 'restricted_native' if x['team'] in restricted else ('holds_restricted_pick' if holds else 'other')
        rows[(x['portfolio'], grp)].append((x, nr[key(x)]))
    out = []
    for (pf, grp), pairs in sorted(rows.items()):
        dt = [p['tau_linear'] - n['tau_linear'] for p, n in pairs]
        rev = np.mean([p['verdict_B'] == 'reversal' for p, _ in pairs]) - np.mean([n['verdict_B'] == 'reversal' for _, n in pairs])
        out.append(dict(portfolio=pf, group=grp, delta_reversal_share=float(rev), **quantiles(dt)))
    return out


def compare_tags(tg_a, tg_b, label_a, label_b):
    """Generic run comparison on the team-games both runs share (paper §5.6 robustness).

    Rows are matched on (season, day, game, side, rule, portfolio). Reports, per rule and portfolio:
    the number of matched team-games, the mean and quartiles of the paired tau difference on every curve,
    the change in the class-B verdict shares, and the verdict transition counts. Days are the bootstrap
    clusters, restricted to the days both runs contain."""
    key = lambda x: (x['season'], x['day'], x['game_id'], x['side'], x['rule'], x['portfolio'])
    B = {key(x): x for x in tg_b}
    pairs = [(x, B[key(x)]) for x in tg_a if key(x) in B]
    if not pairs:
        return [], []
    days = sorted({(x['season'], x['day']) for x, _ in pairs})
    boot = Boot(days, [s for s, _ in days])
    rows, trans = [], defaultdict(int)
    for r in RULES + ('delta',):
        for pf in PORTFOLIOS:
            sel = [(x, y) for x, y in pairs if x['rule'] == r and x['portfolio'] == pf]
            if not sel:
                continue
            row = {'run_a': label_a, 'run_b': label_b, 'rule': r, 'portfolio': pf, 'n_team_games': len(sel),
                   'n_days': len(days)}
            for cv in CURVES:
                d = np.array([x[f'tau_{cv}'] - y[f'tau_{cv}'] for x, y in sel])
                row[f'mean_diff_{cv}'] = float(d.mean())
                row[f'max_abs_diff_{cv}'] = float(np.abs(d).max())
                row[f'share_abs_diff_over_delta_{cv}'] = float((np.abs(d) >= DELTA).mean())
            na, da = per_day([x for x, _ in sel], boot, lambda z: z['verdict_B'] == 'reversal')
            nb, db = per_day([y for _, y in sel], boot, lambda z: z['verdict_B'] == 'reversal')
            pt, lo, hi = boot.diff_of_ratios(na, da, nb, db)
            row.update({'reversal_share_a': na.sum() / max(da.sum(), 1),
                        'reversal_share_b': nb.sum() / max(db.sum(), 1),
                        'reversal_share_diff': pt, 'diff_lo99': lo, 'diff_hi99': hi,
                        'verdict_changed': sum(1 for x, y in sel if x['verdict_B'] != y['verdict_B'])})
            if all('verdict_B_pm' in z for z in (sel[0][0], sel[0][1])):
                na2, da2 = per_day([x for x, _ in sel], boot, lambda z: z['verdict_B_pm'] == 'reversal')
                nb2, db2 = per_day([y for _, y in sel], boot, lambda z: z['verdict_B_pm'] == 'reversal')
                row['reversal_share_a_pm'] = na2.sum() / max(da2.sum(), 1)
                row['reversal_share_b_pm'] = nb2.sum() / max(db2.sum(), 1)
                row['verdict_changed_pm'] = sum(1 for x, y in sel if x['verdict_B_pm'] != y['verdict_B_pm'])
            rows.append(row)
            for x, y in sel:
                if x['verdict_B'] != y['verdict_B']:
                    trans[(r, pf, y['verdict_B'], x['verdict_B'])] += 1
    trows = [{'run_a': label_a, 'run_b': label_b, 'rule': r, 'portfolio': pf, 'verdict_b': vb,
              'verdict_a': va, 'count': c} for (r, pf, vb, va), c in sorted(trans.items())]
    return rows, trows


def write_tables(T, out, extra_note=''):
    out.mkdir(parents=True, exist_ok=True)
    md = [f'# Registered analysis output\n\n{extra_note}\n']
    for name, rows in T.items():
        if not rows:
            continue
        cols = _public_cols(rows)
        with open(out / f'{name}.csv', 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
            for r in rows:
                w.writerow({k: (json.dumps(v) if isinstance(v, (list, dict)) else v)
                            for k, v in r.items() if not k.startswith('_')})
        if name.startswith('F5_') or len(rows) > 400:
            md.append(f'## {name}\n\n{len(rows)} rows in `{name}.csv`.\n')
            continue
        md.append(f'## {name}\n')
        md.append('| ' + ' | '.join(cols) + ' |'); md.append('|' + '---|' * len(cols))
        for r in rows:
            md.append('| ' + ' | '.join(_fmt(r.get(k, '')) for k in cols) + ' |')
        md.append('')
    (out / 'report.md').write_text('\n'.join(md), encoding='utf-8')


def _fmt(v):
    if isinstance(v, float):
        return 'nan' if v != v else f'{v:.4f}'
    if isinstance(v, np.floating):
        return f'{float(v):.4f}'
    return str(v)


def run(tag, exclude_imprecise=False, out=None, root=SIMULATIONS, ranks_fn=None):
    tg, games, profs, diags = collect(tag, exclude_imprecise, root, ranks_fn)
    days = sorted({(x['season'], x['day']) for x in diags})
    boot = Boot(days, [s for s, _ in days])
    T = build_tables(tg, games, profs, diags, boot)
    out = out or (OUT / (tag + ('_precise_only' if exclude_imprecise else '')))
    write_tables(T, out, f'tag `{tag}`; exclude_imprecise={exclude_imprecise}; states={len(diags)}')
    cols = _public_cols(tg)
    with open(out / 'team_games.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
        w.writeheader(); w.writerows(tg)
    print(f'{tag}: {len(diags)} states, {len(tg)} team-game rows, {len(games)} game rows -> {out}')
    return T, tg


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('tag', nargs='?')
    ap.add_argument('--exclude-imprecise', action='store_true')
    ap.add_argument('--compare', nargs=2)
    ap.add_argument('--out')
    a = ap.parse_args()
    if a.compare:
        ta, tb = a.compare
        tga = collect(ta)[0]; tgb = collect(tb)[0]
        # A1 amendment 9 item 6: a comparison of two runs is made at the widest band of the two
        nm = min(min(x['n_worlds'] for x in tga), min(x['n_worlds'] for x in tgb))
        add_precision_matched(tga, nm); add_precision_matched(tgb, nm)
        out = Path(a.out) if a.out else OUT / f'compare_{ta}_{tb}'
        rows, trows = compare_tags(tga, tgb, ta, tb)
        T = {'C_1_paired_differences': rows, 'C_2_verdict_transitions': trows}
        if {ta, tb} == {'primary', 'norestr'}:
            p_, n_ = (tga, tgb) if ta == 'primary' else (tgb, tga)
            T['T5_4_restrictions'] = compare_restrictions(p_, n_)
        write_tables(T, out, f'{ta} versus {tb}, matched team-games only')
        print(f'compare {ta} vs {tb}: {len(tga)} / {len(tgb)} rows, '
              f'{rows[0]["n_team_games"] if rows else 0} matched per cell -> {out}')
    else:
        run(a.tag, a.exclude_imprecise, Path(a.out) if a.out else None)

"""value layer: turn simulator batch means into tau, delta-tau, third-party stakes and
value-function-free bounds, each with Monte Carlo uncertainty from batch means.

Conventions (per focal game g with home team h and away team a, rule r in {0 old, 1 new}):
  D[g, r, team, slot] = E[holdings | away wins] - E[holdings | home wins]
  tau_home(v)  = D[g,r,h] . v            (home loses minus home wins)
  tau_away(v)  = -D[g,r,a] . v           (away loses minus away wins)
  stake_c(v)   = -D[g,r,c] . v           (value to team c of the HOME team winning)
  delta_tau    = tau(new) - tau(old)
Cumulative sums for the own-team loss-minus-win difference d(k): C(j) = sum_{k<=j} d(k), M = C(30).
Value classes (paper Section 3.1):
  class B (v nonincreasing, v >= 0, v(1) = 1): tau in [min_j C(j), max_j C(j)], j = 1..30
  class C (additionally v(30) = 0):             tau in [min_j C(j), max_j C(j)], j = 1..29
Uncertainty: batch means (B batches); halfwidth = z * SE with z = 2.807034 (99%, two-look).
"""
import math

import numpy as np

Z = 2.807034
_lin = np.arange(29, -1, -1, dtype=float) / 29
CURVES = {'linear': _lin, 'concave': np.sqrt(_lin), 'convex': _lin ** 2,
          'top3_stress': (np.arange(30) < 3).astype(float)}


def _stats(batch_values):
    """batch_values: array (B, ...) of batch means. Returns mean, se over axis 0."""
    x = np.asarray(batch_values, float); B = x.shape[0]
    return x.mean(0), x.std(0, ddof=1) / math.sqrt(B)


def own_difference(DB, focal_teams):
    """Own-team loss-minus-win slot difference per batch: (B, G, rule, 2 sides, 30 slots)."""
    B, G = DB.shape[:2]
    out = np.zeros((B, G, 2, 2, 30))
    for g, (h, a) in enumerate(focal_teams):
        out[:, g, :, 0, :] = DB[:, g, :, h, :]    # home: loss (away wins) minus win
        out[:, g, :, 1, :] = -DB[:, g, :, a, :]   # away: loss (home wins) minus win
    return out


def tau_table(res, focal_teams, curves=CURVES):
    """Rows: (focal game index, side, rule or delta, curve) with mean, se, halfwidth, sign."""
    own = own_difference(res['DB'], focal_teams)
    rows = []
    for name, v in curves.items():
        tau = own @ v                                    # (B, G, rule, side)
        for label, arr in (('tau_old', tau[:, :, 0]), ('tau_new', tau[:, :, 1]), ('delta_tau', tau[:, :, 1] - tau[:, :, 0])):
            m, se = _stats(arr)                          # (G, side)
            for g in range(m.shape[0]):
                for side in (0, 1):
                    mm, ss = float(m[g, side]), float(se[g, side]); hw = Z * ss
                    rows.append({'focal': g, 'side': 'home' if side == 0 else 'away', 'metric': label, 'curve': name,
                                 'mean': mm, 'se': ss, 'halfwidth': hw,
                                 'sign': 'positive' if mm - hw > 1e-12 else 'negative' if mm + hw < -1e-12 else 'unresolved'})
    return rows


def stakes(res, curves=CURVES):
    """Value to every team of the HOME team winning: (curve -> mean (G, rule, 30 teams), se)."""
    out = {}
    for name, v in curves.items():
        arr = -(res['DB'] @ v)                           # (B, G, rule, team)
        out[name] = _stats(arr)
    return out


def cumulative_bounds(res, focal_teams):
    """C(j) per focal game/side/rule with SE, and class-B/C bounds with an intersection-union verdict:
    'dominance_positive' if the lower 99% bound of every C(j) in the class is > 0 (tau > 0 for every v),
    'dominance_negative' if every upper bound < 0, else 'mixed_or_unresolved'."""
    own = own_difference(res['DB'], focal_teams)
    C = np.cumsum(own, axis=-1)                          # (B, G, rule, side, 30)
    m, se = _stats(C)
    lo, hi = m - Z * se, m + Z * se
    rows = []
    G = m.shape[0]
    for g in range(G):
        for r in (0, 1):
            for side in (0, 1):
                for cls, J in (('B', 30), ('C', 29)):
                    mm, l, u = m[g, r, side, :J], lo[g, r, side, :J], hi[g, r, side, :J]
                    verdict = ('dominance_positive' if np.all(l > 0) else 'dominance_negative' if np.all(u < 0)
                               else 'mixed_or_unresolved')
                    rows.append({'focal': g, 'rule': 'old' if r == 0 else 'new', 'side': 'home' if side == 0 else 'away',
                                 'class': cls, 'bound_min': float(mm.min()), 'bound_max': float(mm.max()),
                                 'argmin_j': int(mm.argmin()) + 1, 'argmax_j': int(mm.argmax()) + 1,
                                 'max_se': float(se[g, r, side, :J].max()), 'verdict': verdict})
    return rows, m, se


def precision_met(rows, target=0.003, curves=('linear',)):
    """Stopping rule: every tau/delta row of the listed curves has halfwidth <= target."""
    hw = [r['halfwidth'] for r in rows if r['curve'] in curves]
    return (max(hw) <= target if hw else True), (max(hw) if hw else 0.0)

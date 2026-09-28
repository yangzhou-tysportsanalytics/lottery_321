"""R20: calibration of the verdict rule (exploratory; no registered number changes).

The verdicts of Section 4.5 are read from a simultaneous multiplier band over thirty slots computed from
50 super-batch means. Online Appendix I.4 reports the band's coverage on synthetic designs; this script estimates the error
rate of the *decision rule* itself: how often a team-game whose true profile
satisfies C(j) >= 0 at every slot is called a reversal, how often a team-game with a material dip
(min C < -delta) is called dominance-positive, and how often a crossing is called where the true profile
has no positive part. This script estimates those rates by plug-in simulation on a random subset of the
primary days, taking each team-game's estimated profile as the truth:

  (a) fixed look, nonparametric: the day's 50 stored super-batches are resampled with replacement, so the
      noise keeps its real structure (rare-event coordinates, float32 storage, pooled-rights routing);
  (b) three looks with the run's stopping rule, parametric: batch means are drawn from a Gaussian with the
      team-game's batch covariance, scaled by n_final / n_look at looks of 2,000, 8,000 and 32,000 worlds,
      the day stops at the first look at which the largest linear-curve half-width (actual portfolio, both
      rules, constant 2.807034 as run) is at most delta, and the verdict is read at the stopping look with
      the reported constant. Batch values are cast to float32 as in storage.

Truth classes on the plug-in profile m: 'dominant' (min m >= 0), 'weak failure' (-delta <= min m < 0),
'material failure' (min m < -delta); 'has positive part' (max m > 0). The plug-in truth is itself an
estimate, so the rates are calibration under the estimated profiles, not under the unknown true ones.
"""
import csv
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / 'ledgers'))

import analysis as S  # noqa: E402
from value import CURVES  # noqa: E402

OUT = S.OUT / 'exploratory_4'
Z_RUN = 2.807034
LOOKS = (2000, 8000, 32000)
N_DAYS_PER_SEASON = 7
REPS = 60
SEED = 2026092601


def truth_class(m):
    mn = float(m.min())
    return 'material failure' if mn < -S.DELTA else ('weak failure' if mn < 0 else 'dominant')


def write(name, rows):
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / f'{name}.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)


def load_subset(rng):
    files = sorted((S.SIMULATIONS / 'primary').glob('*/exposures_*.npz'))
    by_season = {}
    for f in files:
        by_season.setdefault(f.parent.name, []).append(f)
    chosen = []
    for s in sorted(by_season):
        fs = by_season[s]
        chosen += [fs[i] for i in sorted(rng.choice(len(fs), size=min(N_DAYS_PER_SEASON, len(fs)), replace=False))]
    days = []
    for f in chosen:
        d = S.load_day(f); meta = d['meta']
        tgs = []
        for g, (h, a) in enumerate(meta['focal_teams']):
            for side, c in ((0, h), (1, a)):
                sgn = 1.0 if side == 0 else -1.0
                for pf, src in (('actual', d['DB']), ('own', d['DB_own'])):
                    for ri, r in enumerate(S.RULES):
                        db = sgn * src[:, g, ri, c, :]                     # (B, 30) batch slot differences
                        tgs.append(dict(pf=pf, rule=r, db=db))
        days.append(dict(season=meta['season'], day=meta['day'], n_worlds=int(meta['n_worlds']), tgs=tgs))
    return days


def classify(db):
    Cb = np.cumsum(db, axis=1)
    m, se, crit = S.band_stats(Cb)
    v, _ = S.verdict(m, se, crit['B'], 30)
    return v, S.crossing(m, se, crit['B'])


def run():
    rng = np.random.default_rng(SEED)
    days = load_subset(rng)
    v_lin = CURVES['linear']
    counts_a, counts_b, stop_looks = Counter(), Counter(), Counter()
    n_tg = sum(len(d['tgs']) for d in days)
    print(f'{len(days)} days, {n_tg} team-games, {REPS} reps', flush=True)
    t0 = time.time()
    for di, d in enumerate(days):
        B = d['tgs'][0]['db'].shape[0]
        truths = []
        for t in d['tgs']:
            m = np.cumsum(t['db'].mean(0))
            truths.append((truth_class(m), bool(m.max() > 0)))
        # (a) nonparametric, fixed look
        for rep in range(REPS):
            idx = rng.integers(0, B, size=B)
            for t, (tc, pos) in zip(d['tgs'], truths):
                v, cr = classify(t['db'][idx])
                counts_a[(t['pf'], t['rule'], tc, pos, v, cr)] += 1
        # (b) parametric with three looks and the day-level stopping rule
        chol = []
        for t in d['tgs']:
            db = t['db']; mu = db.mean(0); Sig = np.cov(db, rowvar=False, ddof=1) + 1e-18 * np.eye(30)
            try:
                L = np.linalg.cholesky(Sig)
            except np.linalg.LinAlgError:
                w, V = np.linalg.eigh(Sig); L = V * np.sqrt(np.clip(w, 0, None))
            chol.append((mu, L))
        n_final = d['n_worlds']
        for rep in range(REPS):
            stopped = None
            for look in LOOKS:
                scale = np.sqrt(n_final / look)      # batch-mean noise at this look relative to the stored batches
                sims = []
                hw = 0.0
                for t, (mu, L) in zip(d['tgs'], chol):
                    eps = rng.standard_normal((B, 30)) @ L.T
                    db = (mu[None, :] + scale * eps).astype(np.float32).astype(float)
                    sims.append(db)
                    if t['pf'] == 'actual':
                        tau = db @ v_lin
                        hw = max(hw, Z_RUN * float(tau.std(ddof=1) / np.sqrt(B)))
                if hw <= S.DELTA or look == LOOKS[-1]:
                    stopped = look; break
            stop_looks[stopped] += 1
            for t, (tc, pos), db in zip(d['tgs'], truths, sims):
                v, cr = classify(db)
                counts_b[(t['pf'], t['rule'], tc, pos, v, cr, stopped)] += 1
        print(f'day {di + 1}/{len(days)} done, {time.time() - t0:.0f}s', flush=True)
    rows = []
    for design, counts in (('a: nonparametric, fixed look', counts_a), ('b: parametric, three looks with stopping', counts_b)):
        for key, n in sorted(counts.items(), key=lambda kv: str(kv[0])):
            pf, rule, tc, pos, v, cr = key[:6]
            look = key[6] if len(key) > 6 else ''
            rows.append(dict(design=design, portfolio=pf, rule=rule, truth=tc, truth_has_positive_part=pos,
                             verdict=v, crossing=cr, stopped_at=look, count=n))
    write('R20_calibration_cells', rows)
    write('R20_stop_looks', [dict(look=k, days_x_reps=v) for k, v in sorted(stop_looks.items())])
    write('R20_subset_days', [dict(season=d['season'], day=d['day'], n_worlds=d['n_worlds'], team_games=len(d['tgs'])) for d in days])
    print('wrote', OUT)


if __name__ == '__main__':
    run()

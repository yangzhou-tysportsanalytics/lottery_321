# Stage 5 run registration (main paper): league-wide exposures, 2020-21..2025-26

Registered 2026-09-22, **before any stage-5 output was inspected**. The only earlier runs were one smoke test per season at 40 worlds and one timing run (2024-03-15, 400 worlds); only runtimes and slot conservation were looked at. Code: `scripts/lottery_321/p12_hist_runs.py`. Ledgers: `scripts/lottery_321/ledgers_hist/` v0.1, audited 2026-09-22.

## What is computed

- **Seasons.** 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26 (main sample). The supplementary 2019-20 season is not run here, because its lottery basis stops at the 2020-03-11 hiatus.
- **Window.** Every game day in the last 8 weeks of each regular season (`p12_elo.late_window_start`). In total 312 game days and 2,448 games.
- **State.** One per ET game day. The cutoff is that day's earliest scheduled tip minus 6 hours. Games that ended before the cutoff are known; all others are simulated. The Elo link is fitted only on earlier seasons.
- **Focal games.** Every game of the day. Both teams of each game get τ.
- **Rules.**
  - *Old*: the 2019–2026 flattened-odds lottery, the rule actually in force.
  - *New*: the 3-2-1 research scenario of rule contract v2 (16-team field, ball classes 2/3/2/1, floor at pick 12 for the relegated three, joint draw `sequential_feasible`).
- **Repeat restrictions in the 3-2-1 scenario.** Applied as if 3-2-1 had been in force, using the actual native results of the two previous drafts (2019 from NBA.com; 2020–2026 from the ledgers' realized draft orders):
  - a native that was #1 in the previous draft cannot be #1 (earliest slot 2);
  - a native in the top 5 in both previous drafts cannot be top 5 (earliest slot 6).
  - Resulting restrictions: 2021 MIN 2, CLE 6; 2022 DET 2, CLE 6; 2023 ORL 6, DET 6, HOU 6; 2024 SAS 2, DET 6, HOU 6; 2025 ATL 2, DET 6, SAS 6; 2026 DAL 2, SAS 6.
  - A sensitivity run without restrictions (tag `norestr`) follows the primary run.
- **Rights.**
  - The historical router of that draft year at the post-deadline state.
  - Own-pick-only portfolios come from the same worlds (`DB_own`).
  - Post-deadline changes (for example deferrals elected in June) are not applied, because the window state is the deadline state.
- **Randomness and precision.**
  - Common random numbers across the two forced branches and the two rules.
  - The seed is the day as an integer (YYYYMMDD).
  - Precision rule of `p12_run`: on the linear curve, halfwidth ≤ 0.003 with z = 2.807034, looks at 2,000, 8,000 and 32,000 worlds, batches of 40. Days that miss the target are kept and flagged.
- **Output.**
  - One file per day: `data/derived/lottery_321/p12/stage5/<tag>/<season>/exposures_<day>.npz`, containing `Q`, `DB`, `DB_own` and `ST`, plus metadata (cutoff, seed, focal ids, restrictions, looks, runtime).
  - Storage: `DB` and `DB_own` are stored as 50 super-batch means in float32 (consecutive batches averaged). This keeps batch-means standard errors valid; the precision decision is taken during the run on the full batches. It reduces the stored size from about 25 MB to about 1.7 MB per day. The first three days were written in the full format and converted the same way on 2026-09-22.
  - Files are written once, and existing days are skipped when the run resumes.

## What is reported (fixed now)

- **C1.** For each team-game:
  - class-B and class-C bounds and dominance verdicts for τ_old, τ_new and Δτ, using the intersection–union rule on C(j) with 99% bounds (`p12_value.cumulative_bounds`);
  - the share of team-games with a class-B reversal, by rule, by portfolio type (traded rights versus own-pick-only) and by standing band;
  - the Theorem 1 source attribution where it is exactly computable (own-pick and simple rights).
- **C2.** The third-party stakes for every game (`p12_value.stakes`):
  - the share of the total absolute stake held by third parties;
  - the concentration of stakes;
  - the game typology (both prefer to lose, both prefer to win, normal, third-party dominated), under both rules.
- **C3.** The component decomposition (balls → floor → restrictions → protection ban) with Shapley ordering effects. This is a separate registered run, specified before it starts.
- **Pre-specified curves.** Linear (primary), concave, convex and top-3 stress. Every result is reported for all four; none is chosen after the fact.
- **Not done here.** Nothing is joined to minutes or other behaviour data. The main paper makes no behavioural claim.

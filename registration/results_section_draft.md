<!-- Public copy of the pre-results draft; see the note below. -->

> **Note on this copy (added 2026-10-27).** This is the draft of the results section with empty cells that Online Appendix I.1 of the paper describes. It is the authors' stored file of that draft with references changed only: the internal label of the addendum, the internal name of the simulation ("stage 5") and the file name of an internal note on the design check are replaced by descriptions. No definition, decision rule, number or date was changed. Section, proposition and corollary numbers are those of the drafts of 2026-09-22/23 and can differ from the published paper (for example, "Proposition 1" here is Lemma 1 of the paper, "Proposition 3" is Proposition 1, "Corollary 2" is Corollary 1 and "Corollary 3" is Corollary 2).
>
> **Evidence of date.** The draft is dated 2026-09-22 and was revised on 2026-09-23 before the results were opened (20:18 UTC). The stored file was last saved at 21:11 UTC on 2026-09-23, about fifty minutes after the opening; a copy uploaded to a cloud workspace at 16:50 UTC that day states the decision rules of H1 and H2 in the same words and differs from it in one phrase of the remark on scale under "Reporting discipline" ("a little over a thousandth of the value of the first pick" there, "three thousandths of the value of the first pick" here). None of this was deposited with a third party. SHA-256 of the authors' stored file: `133477f5546c110909654b6c6f1e61681aa87715248aa92786a92620b3b7b1ee`.

# Section 5. Results: framework and pre-specified outputs

*Draft v0, 2026-09-22. Written before any output of the league-wide simulation was inspected. This file fixes every table, figure and test the results section will report. Numbers are left as [—] and are filled in only by the registered analysis script. Operational definitions that the registration left open are fixed in the addendum (same date, also written before any output was inspected). Every result is reported for all four curves and for both value classes. The linear curve and class B are the primary specification. Nothing is selected after the results are seen.*

*Revised 2026-09-23 to match amendment 9 of the addendum, which followed a check of the design and the analysis code. The revision was written before any simulation output was inspected and changes no estimand: the simultaneous band is now a studentised bootstrap-t over the stored super-batches rather than a Gaussian multiplier band, the pointwise constant is the three-look one, the reversal rule carries the same δ margin as dominance, the stake measures are restricted to materially staked teams, the bootstrap resamples seasons and then days within seasons, and every verdict table is reported a second time at a common band width. The passages below mark each change where it applies.*

## 5.0 Run diagnostics (reported first)

- **Coverage.** 312 states and 2,448 games in the primary run, and the same in `norestr`.
- **Precision.** For each run we report:
  - the number of states that met the target at 2,000, 8,000 and 32,000 worlds;
  - the number of states flagged as missing the target;
  - the maximum and the 95th-percentile half-width of the linear-curve τ, including Δτ, which is part of the stopping rule and usually the binding one (amendment 9, item 7).
  - States flagged as missing the target stay in every analysis. As a check, results are repeated without them.
- **Precision and verdicts (amendment 9, item 6).** Because a day's band width is set by the number of worlds it ran, we also report a cross-tabulation of verdicts against the look a day stopped at, and the distribution of the band width c·max_j se(j)/δ by rule and portfolio. The second of these makes visible that the own-pick-only portfolio carries no lottery sampling noise and is therefore measured more finely than the actual one.
- **Internal checks.** Each is reported as the maximum absolute deviation over all states:
  - slot conservation, Σ_c q(k) = 1 for every slot, branch and rule;
  - league zero-sum, Σ_c s_c = 0 for every game and curve (Proposition 2b).
  Under the hybrid estimator, exact marginals for simple rights and sampled joint orders for pooled ones, neither identity holds world by world; both hold in expectation. They are therefore reported as **noise diagnostics against an expected scale**, one pooled-sampling standard error, and not as identity checks (amendment 9, item 7).

## 5.1 How often does losing pay, for every value curve? (C1)

**Unit.** A team-game (c, g) under rule r. There are 4,896 team-games per rule.

**Verdicts (the addendum, §1).** Each team-game gets one of the following verdicts, computed from the curve-free bounds of Proposition 1. The four verdicts are exhaustive and mutually exclusive.
- **Dominance-positive.** Losing is weakly better for every v in the class, and strictly better for some v. The simultaneous 99% band for C(j) lies at or above zero for every j in the class, and above zero for at least one j.
- **Reversal.** The simultaneous upper band lies below −δ at some j. Losing is significantly worse under the step curve v_j, by more than the equivalence margin. The margin was added in amendment 9, item 3, so that a dip smaller than δ is not called a reversal while its mirror image is called dominance-positive.
- **Negligible.** |C(j)| stays below the equivalence margin δ = 0.003 for every j, within the band. There is no material draft stake either way.
- **Unresolved.** Everything else.

The simultaneous band is the studentised bootstrap-t over the 50 stored super-batch means (amendment 9, item 1); the Gaussian-multiplier band of the first registration under-covers and is reported beside it as a diagnostic. Pointwise intervals use z = Φ⁻¹(1 − 0.01/6), the three-look Bonferroni constant (item 2).

**Table 5.1.** Verdict shares.
- Rows: rule (old / 3-2-1), crossed with portfolio (actual portfolio, and own-pick-only from `DB_own`).
- Columns: the four verdicts, separately for class B and class C, and for each of these a **precision-matched** restatement (classes `B_pm` and `C_pm`) in which every day's standard errors are scaled to the widest band among the days compared, so that a day that ran more worlds is not more likely to be called resolved (amendment 9, item 6). The registered classes are the primary ones.
- Cells: share of team-games, with a bootstrap interval that resamples seasons and then days within each resampled season (the addendum, §4 as amended by item 5); the within-season interval is reported as the narrower diagnostic.

**Table 5.2.** The same shares by **standing band**, the team's league rank by record at the cutoff (worst = 1):
- 1–3, the relegation zone of 3-2-1;
- 4–10, the rest of the non-play-in zone;
- 11–16, the play-in zone;
- 17–30.

Bands are defined by the rank at the cutoff, not the final rank, because the cutoff rank is what a decision maker observes.

**Table 5.3.** Where reversals occur. Among reversal team-games, the distribution of the reversal slot j* by rule. The registered j* is the argmin of the upper band; because se(C(j)) is hump-shaped, that argmin is pushed toward the ends of the range, so the table also counts argmin_j Ĉ(j), which is the quantity Proposition 3 makes a prediction about, and the precision-matched j* (amendment 9, item 9). Proposition 3 predicts that under 3-2-1 j* concentrates in 1–11, with a mode near 9, for teams whose own pick is at the relegation boundary.

**Figure 5.1.** Mean C(j) profiles, from j = 1 to 30, with pointwise and simultaneous bands. One panel per standing band; rules overlaid; separate lines for the actual and the own-pick-only portfolio.

**Curve-specific results.** τ_old and τ_new on the four curves are summarised by the mean, the quartiles and the share significantly above and below zero. Results are reported by band and by portfolio type.

**Test of H1 (registered as a quantitative, structural test).** The test uses own-pick-only team-games in the **relegation-boundary band**, league rank 2–5 at the cutoff (within two places of the 3|4 boundary). The simulation does not store final league positions, so the band is defined by the rank at the cutoff; the addendum, §3 fixes this. We report two things:
- (i) the share with a significantly negative τ_new(linear), and the same share under the old rule for the same team-games;
- (ii) among 3-2-1 reversals in the band, the share that are crossings, with C(j) < 0 for some j ≤ 11 and C(j) > 0 for some j ∈ 12–15.

H1 is supported if (i) is significantly higher under 3-2-1 than under the old rule and (ii) is the majority. The magnitude is reported whatever the outcome.

**Attribution to the sources of Corollary 2.** The simulation stores portfolio-level holdings, not holdings by native pick. Exact term-by-term decomposition by Theorem 1 is therefore not available from these outputs. We report the attribution that the stored outputs identify exactly:
- **Portfolio effect.** τ(actual portfolio) − τ(own-pick-only), by rule and band. This is the joint contribution of S2–S4.
- **Membership.** Verdict shares split by the seeding stake (the total-variation distance in `ST`), with cut-points at 0.01 and 0.05 fixed in the addendum. Large seeding stakes signal membership changes, which fall outside (A1a).
- **Ledger features.** Reversal shares split by whether c holds a protected pick of another team (S2), holds its opponent's pick (S3), holds any pick routed through a pool, or plays a team with a repeat restriction.

A native-level decomposition for the reversal cases alone would require a targeted re-run that stores holdings by native pick. If it is done, it will be registered separately before it is run (see the addendum, §6).

## 5.2 The draft-stakes network (C2)

**Unit.** A game g under rule r, with stakes s_c(v) for all 30 teams, where s_c is the value to c of a home win. Write h and a for the two teams of the game.

**Measures (the addendum, §2, as amended by amendment 9, item 4).** TP and the concentration measures are ratios of sums of absolute values of noisy estimates, so pure Monte Carlo noise inflates them. They are therefore computed over **materially staked teams only**, |ŝ_c| ≥ δ, with the unrestricted versions reported as diagnostics. Every measure below is reported on all four value curves (item 7), not on the linear curve alone.
- **Third-party share.** TP = Σ_{c∉{h,a}, material} |s_c| / Σ_{c material} |s_c|, defined when the denominator is at least δ.
- **Concentration.** The Herfindahl index of the shares |s_c| / Σ|s| over materially staked teams, and the number of such teams.
- **Largest third party.** The team with the largest |s_c| outside the game, and whether it holds a pick of h or of a.

**Typology.** For each side we classify the draft incentive τ(linear) as *lose* (significantly > 0), *win* (significantly < 0) or *neutral* (the interval lies inside ±δ, or is not significant). Stakes here are draft stakes only, because the model contains no value of winning itself. So the conventional draft pattern is that both sides gain from losing. The registered labels map as follows:

| Label | Definition |
|---|---|
| **both prefer to lose** | lose / lose |
| **both prefer to win** | win / win |
| **normal** | exactly one side is lose and the other neutral, the standard one-sided tanking stake |
| **opposed** | lose / win |
| **no own stake** | neutral / neutral |
| **one-sided win** | exactly one side is win and the other neutral |

Separately, a game is **third-party dominated** if TP > 1/2. This flag overlays the typology rather than replacing it.

**Table 5.4.** Typology shares by rule and curve, with the third-party-dominated share within each type. The typology's registered definition is the linear curve; the other three are reported beside it.

**Table 5.5.** Distribution of TP and of concentration by rule and curve: mean, quartiles and 90th percentile, materiality-restricted and raw. Also the paired difference between rules for the same game, 3-2-1 minus old.

**Figure 5.2.** For each season, the stakes network aggregated over the window under both rules. An edge from game-team x to team c has weight Σ_g |s_c(g)| over the games that x plays. The figure is descriptive and shows no team-level in-season numbers for the prospective season.

**Test of H2.** The mean paired difference in the mean absolute third-party stake, over games with at least one routed right to a participant, is 3-2-1 minus old. H2 is supported if the difference is positive and its 99% interval excludes zero. The registered sample selects those games by applying each router to 20,000 uniform draft orders; a uniform order ignores the standings, so a protection is counted as conditional even at slots the native cannot reach. A **state-conditional** version of the sample, restricted to slots the native reaches in simulated worlds from the first day of that season's window, is reported beside the registered one, as are the other three curves (amendment 9, items 7 and 9). The same split is applied to the ledger-feature attribution of §5.1.

## 5.3 How the reform changes each team's incentive (Δτ)

- **Table 5.6.** Distribution of Δτ = τ_new − τ_old by band and portfolio type: the mean, the quartiles, and the share significantly positive or negative.
- **Class-B verdict for Δτ.** The same four verdicts as in §5.1, applied to ΔC(j) = C_new(j) − C_old(j). Corollary 4 implies that, for a fixed game, the sign pattern of Δτ is determined by the kernel differences at the boundaries the game moves teams across.
- **Transition table.** The verdict under the old rule against the verdict under 3-2-1, for the same team-game. This shows where the reform creates, removes or preserves a reversal.

## 5.4 Repeat restrictions

We compare the primary run with the `norestr` run on the same states and seeds:
- the Δ in verdict shares;
- the Δ in τ_new for the restricted native teams;
- the Δ in τ_new for teams that hold a restricted native's pick;
- the Δ in τ_new for the other teams in the same lottery field.

This quantifies Section 3.5's remark about restrictions (A3) league-wide.

## 5.5 Component decomposition of 3-2-1 (C3)

C3 is a separate registered run, specified before it starts. The same states and seeds are run under five rule configurations:
1. old rule;
2. + 3-2-1 field and balls;
3. + floor at 12;
4. + repeat restrictions;
5. + protection ban.

For the protection ban, existing top-12-to-15 protections are replaced by the pre-specified compliant alternatives, and every alternative is reported.

The contribution of each component to the verdict shares and to the mean τ is computed as a Shapley value over all 24 orderings. This requires the configurations for every subset of components (2⁴ = 16) on a subsample of states that is fixed in the C3 registration.

## 5.6 Robustness (all reported, none selected)

1. **Value curves and classes.** Four curves × classes B and C. Already part of every table.
2. **Precision.** Exclude states that missed the precision target.
3. **Joint lottery procedure.** Draw-then-adjust instead of sequential-feasible, on a registered subsample of states.
4. **Win model.**
   - Late-window link (fitted only on the late windows of earlier seasons).
   - Slope × 1.25 stress test.
   - Both use the same subsample and the same seeds.
5. **Old-rule tie effects.** Share of old-rule reversals among own-pick-only team-games that are within 10⁻³ of zero (Section 3.5, (A2)).
6. **Ledger assumptions.** Re-run of the team-days affected by the four assumption branches under the alternative reading, if any such team-day exists.

Items 3, 4 and 6 need additional runs. Their subsamples and seeds are fixed in the addendum, §5, before the primary results are opened.

## 5.7 Reporting discipline

- **Stated in advance.** H1 and H2 are stated in advance. H3 concerns C3 and is reported in §5.5. H4 concerns a repeat restriction that first binds in a season outside this paper's sample; it is stated and tested in the prospective study, not here.
- **Behaviour.** No outcome is joined to minutes, rest or other behavioural data. The main paper makes no behavioural claim.
- **Magnitudes.** Every share is reported with its interval and its denominator, and every null result is reported as such. The equivalence margin δ = 0.003 is in units of v(1) = 1, so it is three thousandths of the value of the first pick; for scale, the own-pick incentive across the 3-2-1 relegation boundary of Corollary 3 is τ = −0.022 on the linear curve, about seven times δ, and on that curve δ corresponds to a shift of about one tenth of a draft slot in expectation.
- **Recorded deviations.** Two, both from amendment 9 and neither discovered by looking at a result. The stopping rule as run used the two-look Bonferroni constant 2.807034 rather than the three-look constant now used for intervals, so some days stopped marginally earlier than the stated rule allows; and seeds are `YYYYMMDD` with look *i* using `seed + i`, so neighbouring days share Monte Carlo streams (the states differ, so the worlds differ; what remains is a correlation between days' Monte Carlo errors, which the season-level bootstrap covers). Both are stated in the limitations.
- **Residual coverage.** The bootstrap-t band still under-covers slightly at 50 super-batches, by roughly half a percentage point at a nominal 99%. The direction is stated with the results: it errs toward calling more team-games significant, not fewer.

# Losing for Whose Pick? Traded draft rights and the NBA's 3-2-1 lottery

Data and code for a study of how traded and protected first-round picks change the draft value of losing a
game, under the NBA's 2019–2026 lottery and under a specification of the 3-2-1 lottery adopted in 2026.

For every team in every game of the last eight weeks of six regular seasons (2020-21 to 2025-26; 312 game days,
2,448 games, 4,896 team-games), the simulator plays out the rest of the season, the play-in and both lotteries,
routes every simulated draft through that season's real post-deadline rights ledger, and compares a forced loss
with a forced win. The dominance check on the resulting change in holdings, and every table and figure of the
paper, are computed from the files here.

The results are simulated draft-value incentives. Nothing in this repository measures, or claims, team
behaviour.

## What is here

| Folder | Contents |
|---|---|
| `data/` | `games.csv`: every regular-season game 2019-20 to 2025-26 (date, start and end time, teams, score). `lottery_rules.json`: both lottery rules as simulated, including our specification of 3-2-1 |
| `src/lottery321/ledgers/` | The draft-rights ledgers, one per draft 2020–2026 (`ledger_<year>_draft.json`: who holds every first-round pick after the trade deadline, with protections and pools); the executable router for each draft (`router_<year>.py`); `SCHEMA.md`; router tests |
| `src/lottery321/` | The code: simulator, lottery rules, value curves, exact theory, analysis, tables and figures (module list below) |
| `results/` | All analysed results, one folder per run (list below), and the outputs of the ledger checks |
| `registration/` | The run registration and the decomposition registration, written before any incentive estimate was inspected |
| `tools/simulation/` | The parallel, resumable simulation runner (`run_simulation.py`) and Windows launchers |
| `tests/lottery321/` | Unit tests |

`DATA.md` describes every data file, its columns and its sources.

### Code modules (`src/lottery321/`)

| Module | Role |
|---|---|
| `lottery_rules.py`, `standings.py`, `teams.py` | The two lotteries (exact slot distributions), standings and tie-break rules, team codes |
| `elo.py`, `cutoff_state.py` | Win probabilities (Elo with a logistic link fitted on earlier seasons) and the known/remaining games at a game day's cutoff |
| `league_sim.py`, `day_run.py`, `value.py`, `simulate.py` | Simulation of the rest of a season, both lotteries and the routed draft for forced-loss and forced-win branches; stopping rule; value curves and stakes; one game day end to end |
| `ledgers/router_<year>.py`, `ledgers/protection_ban.py` | Routing a complete draft order to the holder of every slot; the protection-ban counterfactual |
| `analysis.py` | The registered analysis: verdicts, reversal shares, stakes, hypotheses H1 and H2, bootstrap intervals |
| `c3_rules.py`, `c3_sim.py`, `c3_runs.py`, `c3_analysis.py` | The component decomposition of 3-2-1 (field and balls, floor, repeat restrictions, protection ban) and hypothesis H3 |
| `robustness_headlines.py` | The headline quantities for each robustness run |
| `exploratory_1.py` … `exploratory_7.py`, `exploratory_4_calib.py`, `exploratory_5_calib.py`, `pool_convergence.py`, `native_contributions.py` | Exploratory analyses added after the results were opened |
| `dta_corrected.py` | The corrected repair of the draw-then-adjust reading, used by the `dta2` run |
| `theory.py`, `theory_numbers.py` | Exact computations behind the theory section |
| `paper_tables.py`, `appendix_c_tables.py`, `figures.py` | The paper's tables and figures |
| `reachable_slots.py`, `ledger_assumption_check.py` | Checks on the ledgers (which slots a pick can still reach; whether an unconfirmed condition can matter) |

### Result folders (`results/`)

| Folder | Run |
|---|---|
| `primary/` | The registered main run |
| `primary_asrun_boott/` | The main run under the simultaneous band as first run (bootstrap-t) |
| `primary_precise_only/` | The main run on the 163 game days that met the precision target |
| `norestr/`, `dta/`, `latelink/`, `stress/`, `alt6/` | Robustness runs: no repeat restrictions; draw-then-adjust 3-2-1 draw; late-window win-probability link; win-model slope × 1.25; alternative reading of one 2024 ledger condition |
| `compare_primary_<run>/` | Paired differences between the main run and each robustness run |
| `c3/` | The component decomposition of 3-2-1 |
| `exploratory_1/` … `exploratory_7/`, `defer/`, `native_contributions/` | Exploratory analyses; none changes a registered number |
| `dta2/` | The draw-then-adjust robustness run with its repair corrected |

Table files are named after the tables as registered: `T5_1_…` is registered Table 5.1, `H1.csv` and `H2.csv` are
the hypothesis tests, `F5_…` hold the data behind the figures, and `A…`/`B…`/`C…`/`R…`/`E5_…`/`E6_…` are exploratory tables cited
in the online appendix. The section "Which file is which table" below maps the tables of Sections 3 and 5 and of Online
Appendices B, C and H to their files.

## Reproducing the results

Python 3.10 or later with the packages in `requirements.txt`. Set the module path once:

```
export PYTHONPATH=$PWD/src/lottery321:$PWD/src/lottery321/ledgers
# Windows:  set PYTHONPATH=%CD%\src\lottery321;%CD%\src\lottery321\ledgers
```

**1. Tests (about 4 minutes).**
```
python -m unittest discover -s tests/lottery321 -p "test_*.py"
python -m unittest discover -s src/lottery321/ledgers -p "test_*.py"
```
The router tests check that every ledger reproduces that year's realized first round, conserves picks on
20,000 random draft orders, and routes pools consistently.

**2. The paper's tables and figures from the stored results (seconds).**
```
python src/lottery321/paper_tables.py results/primary --c3 results/c3
python src/lottery321/figures.py results/primary figures_out
python src/lottery321/robustness_headlines.py dta latelink stress alt6
python src/lottery321/robustness_headlines.py dta2 --out robustness_headlines_dta2.csv
python src/lottery321/robustness_headlines.py defer --out robustness_headlines_defer.csv
python src/lottery321/exploratory_7.py blocks
python src/lottery321/exploratory_7.py positive
```
The first command prints the seven tables of Section 5 as registered (Tables 5.1–5.7); the paper prints five of
them in the body and two in the online appendix (see "Which file is which table").

**3. The exact theory numbers (seconds).** `python src/lottery321/theory_numbers.py` recomputes the lottery
kernels and every exact number of the theory section (for example the 3-2-1 relegation boundary F3(j) − F4(j))
and writes `results/theory_numbers.md`; it fails if any number differs from the one printed in the paper.

**4. The analysis from simulation outputs (about 20 minutes per run).** `python src/lottery321/analysis.py primary`
reads `simulations/primary/<season>/exposures_<day>.npz` and rewrites `results/primary/`. The analysis is
deterministic: the bootstrap and the multiplier band use fixed seeds (2026092201, 20260922). The decomposition
is `c3_analysis.py`; the exploratory sets are `exploratory_1.py` to `exploratory_7.py`,
`exploratory_4_calib.py`, `exploratory_5_calib.py calib-analyse`, `pool_convergence.py analyse` and
`native_contributions.py` (`exploratory_5.py`, `exploratory_5_calib.py`, the profile of `exploratory_6.py`,
`exploratory_7.py margin` and `exploratory_7.py lastpick` read the simulation day files; `native_contributions.py`
re-simulates its four team-games).

**5. The simulations (about 240 core-hours for the main run).**
`python tools/simulation/run_simulation.py --variant primary` (on Windows, `tools/simulation/run_primary.bat`);
`--smoke` runs a one-minute check. Other variants: `norestr`, `dta`, `dta2`, `latelink`, `stress`, `alt6`, `c3`,
`pool32`, `defer` (`run_dta2.bat` and `run_defer.bat` start the last two with their tests). The re-runs behind Online Appendix H.29 are started with `python src/lottery321/exploratory_5_calib.py calib-run --runs 6`. Runs are resumable, and seeds are fixed by game day, so a rerun reproduces the stored day files bit
for bit apart from the recorded runtime. The simulation outputs (about 1.1 GB of `.npz` day files, written to
`simulations/`) are not in this repository because of their size; they are available on request, and this
step regenerates them.

## Where the headline numbers come from

| Result | File (under `results/`) |
|---|---|
| Reversal shares, old rule vs 3-2-1, own pick and actual portfolio, with 99% intervals | `primary/T5_1_verdicts.csv`, `primary/T5_headline_reversal_diff.csv` |
| Reversal shares by league rank at the cutoff | `primary/T5_2_verdicts_by_band.csv` |
| Relegation-boundary hypothesis (H1) | `primary/H1.csv` |
| Change in each team's incentive, 3-2-1 minus old | `primary/T5_curves_and_T5_6_delta.csv` |
| Old-rule reversals kept, created and removed by 3-2-1 | `primary/T5_6_transitions.csv` |
| Game typology, third-party share, third-party stake test (H2) | `primary/T5_4_typology.csv`, `primary/T5_5_stakes_distribution.csv`, `primary/H2.csv` |
| Mean own-pick incentive by rank and value curve, and the 3-2-1/old ratios | `exploratory_2/R1_tau_by_band_curves.csv` |
| Third-party stakes with and without traded rights | `exploratory_4/R21_network_contrast.csv` |
| Component decomposition and the protection-ban hypothesis (H3) | `c3/C3_1_outcomes.csv` … `c3/C3_4_H3.csv` |
| Robustness items | `robustness_headlines.csv`, `exploratory_3/R8_four_quantities.csv`, `primary_asrun_boott/`, `exploratory_4/R22_look_adjusted.csv` |

## Which file is which table

Code and result files keep the table numbers of the registration. The paper prints registered Tables 5.1, 5.2, 5.3,
5.5 and 5.6 as its Tables 5.1 to 5.5; registered Table 5.4 is Online Appendix Table C.5, Panel C, and Table 5.7 is
Online Appendix Table C.20. Paths are under `results/`.

| Paper | Files | Script |
|---|---|---|
| Table 3.1, Figure 3.1, Online Appendix Table B.1 | exact computations, no stored input | `theory_numbers.py`, `figures.py` |
| Table 5.1 | `primary/T5_1_verdicts.csv` | `analysis.py`, `paper_tables.py` |
| Table 5.2 | `primary/T5_2_verdicts_by_band.csv` | same |
| Table 5.3 | `primary/H1.csv` | same |
| Table 5.4 | `primary/T5_4_typology.csv`, `primary/H2.csv` | same |
| Table 5.5 | `c3/C3_1_outcomes.csv`, `c3/C3_3_shapley.csv`, `c3/C3_4_H3.csv` | `c3_analysis.py`, `paper_tables.py` |
| Figure 5.1 | `primary/F5_1_profiles.csv`, `exploratory_3/R14_profiles_band.csv` | `figures.py` |
| Figure 5.2, Figures H.1–H.5 | `primary/F5_2_network_edges.csv` | `figures.py` |
| C.1, C.2 | `primary/T5_0_diagnostics.csv`, `T5_0b_…`, `T5_0c_…`, `T5_0d_…` (and `norestr/`) | `appendix_c_tables.py` |
| C.3, C.13 | `primary/T5_1_verdicts.csv` | same |
| C.4 | `primary_asrun_boott/T5_1_verdicts.csv` | same |
| C.5 | `primary/T5_curves_and_T5_6_delta.csv` | same |
| C.6 | `primary/T5_attr_portfolio_effect.csv`, `T5_attr_seeding.csv`, `T5_attr_ledger_features.csv` | same |
| C.7 | `primary/T5_7_rollover.csv` | same |
| C.8 | `primary/T5_6_transitions.csv` | same |
| C.9, C.14 | `primary/T5_4_typology.csv`, `primary/T5_5_stakes_distribution.csv`, `primary/H2.csv` | same |
| C.10 | `compare_primary_norestr/C_1_paired_differences.csv`, `T5_4_restrictions.csv` | same |
| C.11 | `primary_precise_only/T5_headline_reversal_diff.csv`, `H1.csv`, `H2.csv` | same |
| C.12 | `compare_primary_<run>/C_1_paired_differences.csv` | same |
| C.15, C.16, C.17 | `c3/C3_1_outcomes.csv`, `c3/C3_2_chain.csv`, `c3/C3_3_shapley.csv` | same |
| C.18 | `primary/T5_2_verdicts_by_band.csv` | same |
| C.19 | `primary/T5_3_reversal_slot.csv` | same |
| C.20 | `robustness_headlines.csv`, `exploratory_3/R8_four_quantities.csv`, `exploratory_4/R22_look_adjusted.csv` | `robustness_headlines.py`, `paper_tables.py` |
| H.1 | `exploratory_1/A1_by_season.csv` | `exploratory_1.py` |
| H.2 | `exploratory_1/A2_deadline.csv`, `A3_jstar.csv`, `A7_headline_by_tercile.csv`; `primary_asrun_boott/T5_headline_reversal_diff.csv` | same |
| H.3 | `primary/T5_2_verdicts_by_band.csv`, `primary_asrun_boott/T5_2_verdicts_by_band.csv` | `analysis.py` |
| H.4 | `exploratory_1/B1_reversal_subtypes.csv`, `B2_mass.csv` | `exploratory_1.py` |
| H.5 | `exploratory_1/A10_h1_magnitudes.csv` | same |
| H.6 | `exploratory_1/A6_rollover_flips.csv` | same |
| H.7, H.7b | `exploratory_1/A7_summary.csv`, `exploratory_2/R2_crosstabs.csv` | `exploratory_1.py`, `exploratory_2.py` |
| H.8 | `exploratory_1/A9_restrictions.csv` | `exploratory_1.py` |
| H.9 | `exploratory_1/A4_seeding.csv`, `C1_seeding_merged.csv` | same |
| H.11 | `exploratory_2/R3_headlines.csv` | `exploratory_2.py` |
| H.12 | `exploratory_3/R7_season_inference.csv`, `R7b_h2_by_season.csv` | `exploratory_3.py` |
| H.12b | `exploratory_2/R5_h1_by_season.csv` | `exploratory_2.py` |
| H.13 | `exploratory_2/R4_flag_rates.csv` | same |
| H.14 | `exploratory_2/R1_tau_by_band_curves.csv` | same |
| H.15 (counts) | `exploratory_2/R6_misc.csv`, `exploratory_3/R10_sets.csv`, `exploratory_6/E6_concentration.csv` | `exploratory_2.py`, `exploratory_3.py`, `exploratory_6.py` |
| H.16 | `exploratory_3/R15_verdict_changes.csv`, `R8_four_quantities.csv` | `exploratory_3.py` |
| H.17 | `exploratory_3/R9_h1_band_by_season.csv` | same |
| H.18 (counts) | `exploratory_3/R10_sets.csv` | same |
| H.19 | `exploratory_3/R11_ban_treatment.csv` | same |
| H.20 | `exploratory_3/R12_e4_horizon.csv` | same |
| H.21 | `exploratory_3/R14_profiles_band.csv` | same |
| H.22 | `exploratory_4/R16_rollover_dominance.csv` | `exploratory_4.py` |
| H.23, H.23b | `exploratory_4/R17_tail_value.csv`, `R16_R17_team_games.csv` | same |
| H.24 | `exploratory_4/R18_c3_two_level.csv` | same |
| H.24b | `exploratory_5/E5_4a_h3_affected.csv` | `exploratory_5.py` |
| H.25 | `exploratory_4/R20_calibration_cells.csv`, `R20_stop_looks.csv`, `R20_subset_days.csv` | `exploratory_4_calib.py` |
| H.26 | `exploratory_4/R21_network_contrast.csv` | `exploratory_4.py` |
| H.27 | `exploratory_4/R22_look_adjusted.csv` | same |
| H.28 | `exploratory_4/R23_pool_convergence.csv`, `R23_pool_convergence_team_games.csv` | `pool_convergence.py` |
| H.29 | `exploratory_5/E5_6_calib_rates.csv`, `E5_6_calib_team_games.csv` | `exploratory_5_calib.py` |
| H.30 | `exploratory_6/E6_two_kinds.csv` | `exploratory_6.py` |
| H.31 | `exploratory_6/E6_example_profile.csv`, `E6_example_selection.csv` | same |
| C.12, C.20 (draw-then-adjust rows) | `compare_primary_dta2/C_1_paired_differences.csv`, `robustness_headlines_dta2.csv`; the first run: `compare_primary_dta/`, `robustness_headlines.csv` | `analysis.py --compare primary dta2`, `robustness_headlines.py` |
| H.23, H.23b (rows for a ≥ 0.4), H.23c | `exploratory_7/E7_4_lastpick_signs.csv`, `E7_4_lastpick_rank_means.csv`, `E7_4_lastpick_stakes.csv` | `exploratory_7.py lastpick` |
| H.32 | `exploratory_7/margin_0.001/`, `margin_0.005/`, `E7_2_block_bootstrap.csv` | `exploratory_7.py margin`, `exploratory_7.py blocks` |
| H.33 | `defer/`, `compare_primary_defer/`, `robustness_headlines_defer.csv` | `analysis.py`, `robustness_headlines.py` |
| H.34 | `native_contributions/case_1.json` … `case_4.json` | `native_contributions.py` |
| H.35 | `exploratory_7/E7_3_positive_part.csv`, `E7_3_positive_part_diagnostics.csv` | `exploratory_7.py positive` |

`exploratory_5/` holds every output of the fifth exploratory set. The paper uses two of them (H.24b and H.29). The
other `E5_1`–`E5_4` files repeat analyses of the fourth set with other parameter values, `E5_5_pool32_…` re-reads
the run behind H.28, and `E5_5_pool_…` is a single day run with 16 joint draws to measure its cost; none of these is
cited in the paper. Its design text describes a 26-day run with 16 joint draws that was not carried out.

## Registration

The analysis plan was written down before any incentive estimate from the simulations was inspected. It consists
of four dated documents of the authors: the run registration (sample, rules, rights, seeds, stopping rule and the
quantities to be reported), an addendum of operational definitions with its amendments (band, verdict rules,
margin, stake measures, bootstrap, robustness runs, headline quantities), a draft of the results section with
empty cells that states the decision rules of hypotheses H1 and H2, and the decomposition registration, which
states H3. The two registrations are in `registration/`; the addendum, its amendments and the draft are
summarised in the paper's Online Appendix I and are available from the authors. None of these documents was
deposited with a third-party registry, so their dates rest on the authors' record. One condition of H3 was
restated by an amendment written before the results were opened: `decomposition_registration.md` gives its first
wording, and Online Appendix I.2 gives both. The two texts in `registration/` are reproduced verbatim, so they keep the names used when they were
written: the simulation is "stage 5", `stage5_registration.md` is `run_registration.md`,
`stage5_C3_registration.md` is `decomposition_registration.md`, and code paths refer to an earlier folder
layout (`scripts/lottery_321/p12_<name>.py` is `src/lottery321/<name>.py` here, with `p12_hist_runs.py` now
`simulate.py`). Later amendments, and the one analysis choice changed after the results were opened (the
simultaneous band), are listed with their dates in the paper's online appendix. Tables produced under the band
as first run are kept in `results/primary_asrun_boott/`.

## Licences

Code: MIT (`LICENSE`). Data we compiled or computed (ledgers, rule specification, analysis results): CC BY 4.0
(`LICENSE-DATA.md`). `games.csv` records factual game results; third-party pages used to compile the ledgers
are cited by URL in `DATA.md` and are not redistributed.

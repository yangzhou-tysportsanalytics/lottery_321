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
| `registration/` | The two analysis registrations, written before any result was inspected |
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
| `exploratory_1.py` … `exploratory_4.py`, `exploratory_4_calib.py`, `pool_convergence.py` | Exploratory analyses added after the results were opened |
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
| `exploratory_1/` … `exploratory_4/` | Exploratory analyses; none changes a registered number |

Table files are named after the paper: `T5_1_…` is Table 5.1, `H1.csv` and `H2.csv` are the hypothesis tests,
`F5_…` hold the data behind the figures, and `R…`/`A…` are exploratory tables cited in the online appendix.

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
```
The first command prints the seven body tables (Tables 5.1–5.7).

**3. The exact theory numbers (seconds).** `python src/lottery321/theory_numbers.py` recomputes the lottery
kernels and every exact number of the theory section (for example the 3-2-1 relegation boundary F3(j) − F4(j))
and writes `results/theory_numbers.md`; it fails if any number differs from the one printed in the paper.

**4. The analysis from simulation outputs (about 20 minutes per run).** `python src/lottery321/analysis.py primary`
reads `simulations/primary/<season>/exposures_<day>.npz` and rewrites `results/primary/`. The analysis is
deterministic: the bootstrap and the multiplier band use fixed seeds (2026092201, 20260922). The decomposition
is `c3_analysis.py`; the exploratory sets are `exploratory_1.py` to `exploratory_4.py`,
`exploratory_4_calib.py` and `pool_convergence.py analyse`.

**5. The simulations (about 240 core-hours for the main run).**
`python tools/simulation/run_simulation.py --variant primary` (on Windows, `tools/simulation/run_primary.bat`);
`--smoke` runs a one-minute check. Other variants: `norestr`, `dta`, `latelink`, `stress`, `alt6`, `c3`,
`pool32`. Runs are resumable, and seeds are fixed by game day, so a rerun reproduces the stored day files bit
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

## Registration

The design, sample, verdict rules, hypotheses and headline quantities were registered before any result was
inspected. The two texts in `registration/` are reproduced verbatim, so they keep the names used when they were
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

# Stage 5 · C3 registration: component decomposition of the 3-2-1 scenario

Registered 2026-09-22, before any stage-5 output was inspected and before any C3 computation. This builds on `stage5_registration.md` and addendum A1, and fills in paper §5.5. It adds no new data. States, seeds, ledgers, win model, precision rule and verdict definitions are the same as in the primary run unless stated otherwise here.

## 1. Components and configurations

The 3-2-1 research scenario is split into four components.

| Code | Component | Off | On |
|---|---|---|---|
| **F** | Field and balls | The 2019–2026 lottery: 14 non-playoff teams; 140/140/140/125/105/90/75/60/45/30/20/15/10/5 combinations; top 4 drawn; the rest by record; tie-splitting. | The 3-2-1 field: 16 teams (10 non-play-in, the 9th and 10th seeds, the two 7-vs-8 losers); 2/3/2/1 balls, with the 3 worst at 2; all 16 picks drawn by sequential weighted draw. |
| **L** | Floor | No floor. | The three worst records cannot pick later than 12th. |
| **R** | Repeat restrictions | None. | The minimum-slot table of the primary registration: no #1 in consecutive drafts; no top 5 in three consecutive drafts. |
| **P** | Protection ban | Ledgers as written. | Every protection of the form "top-P protected" with P ∈ {12, 13, 14, 15} is replaced by a compliant alternative (§2). |

### Definitions when F is off

Two components also need a definition under the old lottery.
- **L with F off.** The floor applies to the three worst lottery teams. Under the old rule none of them can fall below 7th, so the floor never binds. Its value is zero by construction; it is computed, not assumed.
- **R with F off.**
  - In the four draws, a restricted team is not eligible for a pick earlier than its minimum slot. The draw is then made among the eligible teams, weighted by their combinations.
  - Slots 5–14 are filled in record order (worst first). A team whose minimum exceeds the current slot is skipped, and it takes the first later slot it is allowed.
  - This is the natural analogue of the 3-2-1 restriction for the old lottery. It exists only for this decomposition.

### Configurations

All 16 subsets of {F, L, R, P} are computed. Five of them form the registered chain:

| # | Configuration | Subset |
|---|---|---|
| 1 | Old rule | ∅ |
| 2 | + field and balls | {F} |
| 3 | + floor | {F, L} |
| 4 | + restrictions (= primary 3-2-1 scenario) | {F, L, R} |
| 5 | + protection ban | {F, L, R, P} |

Configurations 1 and 4 are recomputed in the C3 run, not taken from the primary files. This keeps every configuration on the same subsample and the same worlds.

**Validation before any C3 output is opened.**
- Configuration 1 must reproduce the primary run's old-rule Q on the same seed exactly.
- Configuration 4 must do the same for the 3-2-1 Q.
- Unit tests check the new code paths: the old lottery with restrictions, the 3-2-1 lottery without the floor, and the ban routers.

## 2. Protections affected by the ban, and compliant alternatives

Read from ledgers v0.2 (deadline state). The threshold is P, where the native keeps its pick at slots 1..P.

| Draft | Native pick (holder if conveyed) | P |
|---|---|---|
| 2021 | POR (HOU) | 14 |
| 2022 | CLE (IND), OKC (ATL), POR (CHI), TOR (SAS) | 14 |
| 2022 | PHX (OKC) | 12 |
| 2022 | MIA inside the BKN/HOU/MIA pool | 14 |
| 2023 | CLE (IND), DEN (CHA), NYK (POR), POR (CHI), WAS (NYK) | 14 |
| 2023 | BOS (IND) | 12 |
| 2024 | CHA (SAS), POR (CHI), SAC (ATL) | 14 |
| 2024 | WAS (NYK; also governs the WAS/PHX/MEM swaps) | 12 |
| 2025 | CHA (SAC), MEM (WAS), MIA (OKC), POR (CHI) | 14 |
| 2025 | DET (MIN) | 13 |
| 2025 | SAC (ATL) | 12 |
| 2026 | POR (CHI) | 14 |

There are 24 such protections in total. Three of them sit inside a pool, so the whole pool has to be replayed with the new threshold rather than just the native's own keep range: POR 2021 (inside the two-step Houston/Brooklyn swap), MIA 2022 (the BKN/HOU/MIA swap) and WAS 2024 (the WAS/PHX/MEM swaps).

**Out of scope.** The ban concerns top-12-to-15 protections. The following are therefore unchanged:
- conveyances that apply only inside a range, such as UTA 2021 (conveyed at slots 8–14) and IND 2026 (conveyed at slots 5–9);
- protections with P ≤ 11 or P ≥ 16.

**Alternatives.** There are two compliant alternatives, and both are run in full. Neither is preferred, and both are reported.
- **A (tighten):** P → 11. The native keeps its pick at 1..11 and conveys it from 12 onward.
- **B (loosen):** P → 16. The native keeps its pick at 1..16 and conveys it from 17 onward.

Ban routers are generated from the historical routers by changing only these thresholds (`scripts/lottery_321/ledgers_hist/p12_c3_ban.py`, tests in `tests/lottery_321/test_p12_c3_ban.py`). Their tests require three things:
- slot conservation;
- identical routing wherever the native's slot is outside the changed range;
- the intended change inside it.

## 3. Sample, seeds and precision

- **Subsample.** The 81 game days of A1 §5: every 4th game day of each season, in date order, starting with the first day.
- **Seeds.** The same seeds as the primary run. Common random numbers are used across all 16 configurations × 2 ban alternatives, since configurations without P are shared by A and B.
- **Engine.** The component kernels are in `scripts/lottery_321/p12_c3_rules.py` (tests: `tests/lottery_321/test_p12_c3_rules.py`): the old lottery with minimum slots by exact dynamic programming, and the 3-2-1 kernel with the floor switched off.
- **Precision.** The primary stopping rule applies. The looks are 2,000, 8,000 and 32,000 worlds. A day stops at the first look where linear-curve τ has a half-width ≤ 0.003 for every configuration. Days that miss are kept and flagged.

## 4. Outcomes and Shapley decomposition

For each configuration S, three outcomes are computed over all team-games of the subsample, both sides of every focal game, using the actual portfolio:
1. **Y1(S):** the share of class-B reversals (A1 §1 verdicts);
2. **Y2(S):** the mean linear-curve τ;
3. **Y3(S):** the mean third-party share TP (A1 §2).

Y1 and Y2 are also computed by standing band.

**Shapley value.** For component k, the Shapley value is

φ_k = Σ_{S ⊆ N∖{k}} |S|!(4−|S|−1)!/4! · [Y(S ∪ {k}) − Y(S)],

with N = {F, L, R, P}. The four values sum to Y(N) − Y(∅). Alongside φ we report the chain increments along configurations 1 → 5, each a marginal contribution in one ordering. Intervals for Y(S), for the increments and for φ use the day-clustered bootstrap of A1 §4, with the same weights for every configuration.

## 5. Test of H3

H3 says the ban removes only part of the incentive cliffs created by protections, and that protections of top 1–11 still produce reversals. It is tested on team-games in which the team holds another team's pick conditionally (the `holds_conditional_other` feature):
- **(i)** In configuration 5, the class-B reversal share among these team-games has a 99% lower bound above zero. This is checked under A and under B.
- **(ii)** Among the same team-games, the reversal share in configuration 5 is positive, and the change from configuration 4 to 5 is smaller in absolute value than the configuration-4 share. That is, the ban does not remove all reversals.

H3 is supported if (i) and (ii) both hold under both alternatives. Results are reported whether or not they support H3.

## 6. Scope notes

- The ban counterfactual applies the ban to every protection in the ledgers. The actual rule applies only to picks traded after 2026-05-28. C3 therefore measures what a fully compliant set of rights would do, not what the 2027 ledger will look like.
- Old-lottery restrictions (R with F off) exist only for this decomposition. Their Shapley share is interpreted with that in mind.
- The code for the C3 run (`p12_c3_runs.py`, the ban routers and the configuration-aware lottery engine) is written and tested before any stage-5 output is opened. The run starts after the primary and `norestr` runs finish.

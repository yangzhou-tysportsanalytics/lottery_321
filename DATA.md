# Data

All files are UTF-8 CSV or JSON unless stated. Team codes are the three-letter codes in
`src/lottery321/teams.py` (`TEAMS`), whose order is the index order of every array in the code.

## 1. Games: `data/games.csv`

Every regular-season game from 2019-20 to 2025-26 (8,292 rows, including three NBA Cup finals that do not count
in the standings). Extracted from ESPN game-summary data for each event id; only the header, competitors, status,
line scores and end-of-game wall clock were read. The cached summary pages themselves are not redistributed;
`body_sha256` identifies the page each row was read from.

| column | meaning |
|---|---|
| `game_id` | ESPN event id |
| `season` | e.g. `2023-24` |
| `phase_2019_20` | 2019-20 only: `pre_hiatus` (before the 2020-03-11 suspension) or `bubble_seeding` (seeding games after the restart) |
| `game_date_local` | local calendar date |
| `start_utc` | scheduled start (UTC) |
| `first_play_wallclock` | wall clock of the first play (UTC) |
| `cutoff6h_utc` | scheduled start minus six hours; a game day's simulation state uses the earliest of these |
| `end_utc` | end of game (UTC); a game is known at a cutoff only if it ended before it |
| `home`, `away`, `home_score`, `away_score`, `winner`, `n_periods` | result |
| `standings_use` | `counts_for_standings`, or `excluded_cup_final` |
| `extract_status`, `flags` | extraction check; `flags` notes the few games whose start or end time needed a fallback |
| `body_sha256` | SHA-256 of the source page body |

## 2. Rights ledgers: `src/lottery321/ledgers/ledger_<year>_draft.json`

One ledger per draft from 2020 to 2026, as the rights stood after that season's trade deadline (the 2020 ledger,
for the supplementary 2019-20 season, as of the 2020-03-11 suspension). Each of the 30 native first-round picks
has one rule from a small grammar: `own`, `to` (conveyed unconditionally), `protected` (kept in a listed slot
range, otherwise conveyed), `reverse` (conveyed only in a listed range) and `pool` (several natives' picks
handed out by rank: swaps, "best of", "worst of"). Each rule carries a short paraphrase, its sources and a
confidence grade; `realized` is the actual first round, and `open_issues` records every ambiguity and how it was
read. The grammar is in `SCHEMA.md`.

`router_<year>.py` compiles each ledger into a router that maps a complete draft order to the holder
of every slot. Each router reproduces that year's realized first round, except for picks that changed hands
after the trade deadline, which are deliberately not applied and are listed in the router
(`POST_DEADLINE_CHANGES`). Of the 67 protection and pool conditions checked against a second source, 63 are
confirmed and none conflict; the remaining four are recorded as `ASSUMPTIONS` in the routers, and
`results/ledger_assumption_check.json` shows how often each could bind in a sampled state (its items 3, 6, 8 and 9 are the four assumptions, described in `src/lottery321/ledger_assumption_check.py`).

`router_2024_alt6.py` is the alternative reading of one 2024 condition used as a robustness run, and
`protection_ban.py` rewrites every top-12 to top-15 protection for the protection-ban counterfactual.

Sources (conditions from post-deadline lists; realized holders from NBA.com and a second listing; individual
trades from team, league or news reports):

| draft | season | source | role | URL |
|---|---|---|---|---|
| 2020 | 2019-20 | Hoops Rumors: What Lottery, Draft Rules Mean For Traded 2020 First Round Picks | conditions (post-deadline, post-hiatus state; lottery seeding by 2020-03-11 records) | https://www.hoopsrumors.com/2020/06/what-lottery-draft-rules-mean-for-traded-2020-first-round-picks.html |
| 2020 | 2019-20 | Hoops Rumors: Checking In On 2020's Protected First-Round Picks | conditions (pre-deadline; original protection terms) | https://www.hoopsrumors.com/2020/01/checking-in-on-2020s-protected-first-round-picks.html |
| 2020 | 2019-20 | Hoops Rumors: Traded First Round Picks For 2020 NBA Draft | conditions (original terms, carryovers) | https://www.hoopsrumors.com/2019/08/traded-first-round-picks-for-2020-nba-draft.html |
| 2020 | 2019-20 | Hoops Rumors: Clippers Acquire Marcus Morris In Three-Team Trade | conditions (deadline trade: LAC 2020 first to NYK) | https://www.hoopsrumors.com/2020/02/clippers-knicks-finalizing-marcus-morris-trade.html |
| 2020 | 2019-20 | NBA.com: Clint Capela, Robert Covington on move in massive 4-team deal | conditions (deadline trade: HOU 2020 first to DEN; BKN 2020 first ATL->MIN) | https://www.nba.com/news/reports-four-team-trade-capela-covington |
| 2020 | 2019-20 | CBS Sports: 2020 NBA Draft order (first round with 'from' annotations) | realized holders | https://www.cbssports.com/nba/news/2020-nba-draft-order-knicks-move-up-bucks-get-another-pick-and-timberwolves-to-pick-no-1/ |
| 2020 | 2019-20 | Wikipedia: 2020 NBA draft | realized holders (second source; pre-draft vs draft-day trades) | https://en.wikipedia.org/wiki/2020_NBA_draft |
| 2021 | 2020-21 | Hoops Rumors: Checking In On Traded 2021 First-Round Picks | conditions (post-deadline state; deadline was 2021-03-25) | https://www.hoopsrumors.com/2021/04/checking-in-on-traded-2021-first-round-picks.html |
| 2021 | 2020-21 | Hoops Rumors: Early Check-In On Traded 2021 First-Round Picks | conditions (pre-deadline) | https://www.hoopsrumors.com/2021/02/early-check-in-on-traded-2021-first-round-picks.html |
| 2021 | 2020-21 | Hoops Rumors: Traded First-Round Picks For 2021 NBA Draft | conditions (original terms, carryovers; page appears to have been updated later) | https://www.hoopsrumors.com/2021/01/traded-first-round-picks-for-2021-nba-draft.html |
| 2021 | 2020-21 | Hoops Rumors: More Details On Draft Picks Traded From Rockets To Thunder | conditions (OKC/HOU 2021 swap mechanics) | https://www.hoopsrumors.com/2019/07/more-details-on-draft-picks-traded-from-rockets-to-thunder.html |
| 2021 | 2020-21 | Bleacher Report: Nets', Rockets' Updated Draft Pick List After James Harden Blockbuster Trade | conditions (HOU/BKN 2021 swap, unprotected) | https://bleacherreport.com/articles/10000147-nets-rockets-updated-draft-pick-list-after-james-harden-blockbuster-trade |
| 2021 | 2020-21 | Hoops Rumors: Clippers Acquire Marcus Morris In Three-Team Trade | conditions (NYK/LAC 2021 swap terms) | https://www.hoopsrumors.com/2020/02/clippers-knicks-finalizing-marcus-morris-trade.html |
| 2021 | 2020-21 | Larry Brown Sports: Details of draft picks Lakers traded to Pelicans revealed | conditions (initial reported LAL 2021 terms) | https://larrybrownsports.com/basketball/lakers-pelicans-draft-picks-trade-details/500339 |
| 2021 | 2020-21 | NBA.com: Celtics trade Kemba Walker, picks to Thunder | post-deadline trade of BOS 2021 first (No. 16) to OKC | https://www.nba.com/news/celtics-trade-kemba-walker-picks-to-thunder |
| 2021 | 2020-21 | NBA.com: 2021 NBA Draft results / order, picks 1-30 | realized holders | https://www.nba.com/news/2021-draft-order |
| 2021 | 2020-21 | Wikipedia: 2021 NBA draft | realized holders (second source) | https://en.wikipedia.org/wiki/2021_NBA_draft |
| 2022 | 2021-22 | Checking In On Traded 2022 First-Round Picks (Hoops Rumors) | conditions (post-deadline state; 2022 deadline was 2022-02-10) | https://www.hoopsrumors.com/2022/03/checking-in-on-traded-2022-first-round-picks-2.html |
| 2022 | 2021-22 | Traded First-Round Picks For 2022 NBA Draft (Hoops Rumors) | original terms (page evidently updated after publication: it already lists the Feb 2022 BOS->SAS and TOR->SAS deals) | https://www.hoopsrumors.com/2021/09/traded-first-round-picks-for-2022-nba-draft.html |
| 2022 | 2021-22 | 2022 NBA Draft results / order (NBA.com) | realized holders | https://www.nba.com/news/2022-nba-draft-order |
| 2022 | 2021-22 | 2022 NBA draft (Wikipedia) | realized holders with 'from' annotations (second source) | https://en.wikipedia.org/wiki/2022_NBA_draft |
| 2022 | 2021-22 | ProSportsTransactions transaction records, 2021-03-25 (Oladipo trade) | conditions | https://www.prosportstransactions.com/basketball/Search/SearchResults.php?BeginDate=2020-10-11&EndDate=&Player=&PlayerMovementChkBx=yes&Submit=Search&Team=&start=1375 |
| 2023 | 2022-23 | Checking In On Traded 2023 First-Round Picks (Hoops Rumors) | conditions (post-deadline state; 2023 deadline was 2023-02-09) | https://www.hoopsrumors.com/2023/03/checking-in-on-traded-2023-first-round-picks.html |
| 2023 | 2022-23 | Traded First Round Picks For 2023 NBA Draft (Hoops Rumors) | original terms (page evidently updated after publication: lists the Feb 2023 PHX->BKN deal) | https://www.hoopsrumors.com/2022/08/traded-first-round-picks-for-2023-nba-draft.html |
| 2023 | 2022-23 | 2023 NBA Draft Pick Swaps To Monitor (Hoops Rumors) | swap terms | https://www.hoopsrumors.com/2022/10/2023-nba-draft-pick-swaps-to-monitor.html |
| 2023 | 2022-23 | P.J. Tucker trade grades (CBS Sports) | origin of HOU's MIL 2023 first (unprotected) | https://www.cbssports.com/nba/news/p-j-tucker-trade-grades-bucks-add-rockets-forward-in-four-player-deal-that-also-involves-picks-per-report/ |
| 2023 | 2022-23 | 2023 NBA Draft results: picks 1-58 (NBA.com) | realized holders | https://www.nba.com/news/2023-nba-draft-order |
| 2023 | 2022-23 | 2023 NBA draft (Wikipedia) | realized holders with 'from' annotations (second source) | https://en.wikipedia.org/wiki/2023_NBA_draft |
| 2024 | 2023-24 | Checking In On Traded 2024 First-Round Picks (Hoops Rumors) | conditions | https://www.hoopsrumors.com/2024/03/checking-in-on-traded-2024-first-round-picks.html |
| 2024 | 2023-24 | Traded First Round Picks For 2024 NBA Draft (Hoops Rumors) | original terms (page may have been updated after publication) | https://www.hoopsrumors.com/2023/08/traded-first-round-picks-for-2024-nba-draft.html |
| 2024 | 2023-24 | 2024 NBA Draft order / results (NBA.com) | realized holders | https://www.nba.com/news/2024-nba-draft-order |
| 2024 | 2023-24 | 2024 NBA Draft order: complete list of picks (CBS Sports) | realized holders (native/via annotations) | https://www.cbssports.com/nba/news/2024-nba-draft-order-complete-list-of-picks-as-atlanta-hawks-win-no-1-selection-in-lottery |
| 2024 | 2023-24 | 2024 NBA draft (Wikipedia) | realized holders (second source) | https://en.wikipedia.org/wiki/2024_NBA_draft |
| 2024 | 2023-24 | Pelicans To Defer Lakers' First-Rounder To 2025 (Hoops Rumors) | post-deadline election | https://www.hoopsrumors.com/2024/06/pelicans-to-defer-lakers-first-rounder-to-2025.html |
| 2025 | 2024-25 | Checking In On Traded 2025 First-Round Picks (Hoops Rumors) | conditions | https://www.hoopsrumors.com/2025/03/checking-in-on-traded-2025-first-round-picks.html |
| 2025 | 2024-25 | Traded First-Round Picks For 2025 NBA Draft (Hoops Rumors) | original terms (page appears updated through June 2025; not a clean Aug 2024 snapshot) | https://www.hoopsrumors.com/2024/08/traded-first-round-picks-for-2025-nba-draft.html |
| 2025 | 2024-25 | 2025 NBA Draft order / results (NBA.com) | realized holders | https://www.nba.com/news/2025-nba-draft-order |
| 2025 | 2024-25 | Full 2025 NBA Draft Order (Hoops Rumors) | realized natives (from annotations) | https://www.hoopsrumors.com/2025/05/full-2025-nba-draft-order.html |
| 2025 | 2024-25 | 2025 NBA draft (Wikipedia) | realized holders (second source) | https://en.wikipedia.org/wiki/2025_NBA_draft |
| 2025 | 2024-25 | Pacers-Pelicans trade (NBA.com) | post-deadline trade | https://www.nba.com/news/pacers-pelicans-trade-2025-draft-pick |
| 2025 | 2024-25 | Magic-Grizzlies trade: Bane (NBA.com) | post-deadline trade | https://www.nba.com/news/magic-grizzlies-trade-bane-caldwell-pope |
| 2026 | 2025-26 | Traded First-Round Picks For 2026 NBA Draft (Hoops Rumors; page first posted 2025-08-27 and maintained; the version consulted already reflects the Feb 2026 deadline deals: IND->LAC, PHI's 2nd-most-favorable OKC-pool pick, DET-MIN swap) | conditions (post-deadline state) | https://www.hoopsrumors.com/2025/08/traded-first-round-picks-for-2026-nba-draft.html |
| 2026 | 2025-26 | 2026 NBA Trade Deadline Recap (Hoops Rumors) | conditions (deadline trades touching 2026 firsts) | https://www.hoopsrumors.com/2026/02/2026-nba-trade-deadline-recap.html |
| 2026 | 2025-26 | Mavericks Send Anthony Davis To Wizards In Three-Team Deal (Hoops Rumors) | conditions (least favorable OKC/HOU/LAC pick WAS->DAL) | https://www.hoopsrumors.com/2026/02/mavericks-to-trade-anthony-davis-to-wizards.html |
| 2026 | 2025-26 | Kevin Huerter / Jaden Ivey three-team trade (NBA.com) | conditions (DET-MIN 2026 protected swap) | https://www.nba.com/news/kevin-huerter-jaden-ivey-trade-2026 |
| 2026 | 2025-26 | Pistons' 2026 NBA Draft pick moves up thanks to Jaden Ivey trade (Yahoo Sports) | conditions (DET-MIN swap protection 1-19) and outcome | https://sports.yahoo.com/articles/pistons-2026-nba-draft-pick-172906186.html |
| 2026 | 2025-26 | How many picks do the OKC Thunder have in the 2026 NBA Draft (SI, pre-deadline) | conditions corroboration (PHI top-4, UTA top-8, OKC/HOU/LAC pool; pre-deadline holders) | https://www.si.com/nba/thunder/draft-coverage/how-many-picks-okc-thunder-have-2026-nba-draft |
| 2026 | 2025-26 | Five Owed 2026 First-Round Picks Worth Monitoring (Third Apron) | conditions corroboration (WAS top-8 to NYK) | https://www.thirdapron.com/p/five-owed-2026-first-round-picks |
| 2026 | 2025-26 | 2026 NBA Draft Lottery Primer (Hoops Rumors) | conditions corroboration (IND, NOP/MIL, LAC) and pre-lottery order | https://www.hoopsrumors.com/2026/05/2026-nba-draft-lottery-primer.html |
| 2026 | 2025-26 | Post-Play-In Update On 2026 Draft Order, Lottery Standings (Hoops Rumors) | projected holders 15-30 before tiebreak drawings | https://www.hoopsrumors.com/2026/04/post-play-in-update-on-2026-draft-order-lottery-standings.html |
| 2026 | 2025-26 | Full 2026 NBA Draft Order (Hoops Rumors) | realized order with from-annotations (page later updated for June trades) | https://www.hoopsrumors.com/2026/05/full-2026-nba-draft-order.html |
| 2026 | 2025-26 | 2026 NBA Draft Results (Hoops Rumors) | realized holders (from/via annotations) | https://www.hoopsrumors.com/2026/06/2026-nba-draft-results.html |
| 2026 | 2025-26 | 2026 NBA Draft Results: Picks 1-60 (NBA.com) | realized holders (selecting team, draft-night trades) | https://www.nba.com/news/2026-nba-draft-order |
| 2026 | 2025-26 | 2026 NBA draft (Wikipedia) | realized holders and natives (from/via annotations) | https://en.wikipedia.org/wiki/2026_NBA_draft |
| 2026 | 2025-26 | Giannis Antetokounmpo trade live updates (CBS Sports) | timing of MIA No. 13 pick trade (draft eve) | https://www.cbssports.com/nba/news/giannis-antetokounmpo-trade-rumors-updates-celtics-heat/live/ |
| 2026 | 2025-26 | Heat acquire Giannis Antetokounmpo in blockbuster deal (NBA.com) | MIA No. 13 pick conveyed to MIL (post-draft completion) | https://www.nba.com/news/reports-heat-acquire-giannis-antetokounmpo-in-blockbuster-deal |
| 2026 | 2025-26 | Sixers Trade Jared McCain To Thunder For Draft Compensation (Hoops Rumors) | conditions (PHI's OKC-pool right; wording conflict) | https://www.hoopsrumors.com/2026/02/sixers-to-trade-jared-mccain-to-thunder-for-draft-compensation.html |
| 2026 | 2025-26 | 2026 NBA Offseason Trades (Hoops Rumors) | check for post-deadline pre-draft trades (none) | https://www.hoopsrumors.com/2026/06/2026-nba-offseason-trades.html |

## 3. Lottery rules: `data/lottery_rules.json`

Both lotteries as simulated. The old rule: 14 non-playoff teams, 140, 140, 140, 125, 105, 90, 75, 60, 45, 30,
20, 15, 10 and 5 combinations per 1,000, four picks drawn. The 3-2-1 research scenario: 16 lottery teams sharing
37 balls (2 each for the three worst non-play-in records, which cannot pick later than 12th; 3 each for the
other seven non-play-in teams; 2 each for seeds 9–10; 1 each for the two 7-vs-8 play-in losers), all 16 lottery
picks drawn, and the repeat restrictions (a native pick cannot be first overall in two consecutive drafts or in
the top five in three consecutive drafts). The file records the sources and the reading taken where the
official release of 2026-05-28 is silent; the primary draw reproduces all 64 marginal probabilities printed in
the official attachment.

The previous-draft results that the repeat restrictions need come from the ledgers' `realized` orders (the 2019
top five, before the first ledger, is written in `simulate.py`).

## 4. Results: `results/`

| folder | contents |
|---|---|
| `primary/` | The registered primary run: every registered table (`T5_*.csv`, `H1.csv`, `H2.csv`, `F5_*.csv`), a readable `report.md`, and `team_games.csv.gz` |
| `primary_asrun_boott/` | The same tables under the simultaneous band as run (bootstrap-t) |
| `primary_precise_only/` | The same tables on the 163 game days that met the precision target |
| `norestr/`, `dta/`, `latelink/`, `stress/`, `alt6/` | Registered robustness runs: no repeat restrictions; draw-then-adjust 3-2-1 draw; late-window win-probability link; win-model slope × 1.25; alternative reading of one 2024 condition |
| `compare_primary_*/` | Paired differences between the primary run and each robustness run |
| `c3/` | Component decomposition of 3-2-1 (field and balls, floor, repeat restrictions, protection ban): outcomes, chain, Shapley values, H3 |
| `exploratory_1/` to `exploratory_4/` | Exploratory analyses added after the results were opened, in four sets; none changes a registered number |
| `robustness_headlines.csv` | The four headline quantities for each robustness run |

`team_games.csv(.gz)` has one row per team-game, rule (`old`, `new` = 3-2-1) and portfolio (`actual` = rights
held under the ledger, `own` = every native keeps its own pick). Main columns: `season`, `day`, `game_id`,
`team`, `opp`, `rank` (league rank at the cutoff, 1 = worst) and `band` (rank group); `verdict_B`, `verdict_C`
(dominance-positive, negligible, reversal or unresolved, for the two value classes) with the reversal slot
`jstar_*` and `crossing`; `tau_<curve>`, `se_<curve>` and `sign_<curve>` for the four value curves (linear,
concave, convex, top-3), also under rollover values `_rho50`, `_rho80`; `M` (change in the expected number of
picks held); `seeding_tv` (seeding stake); ledger features (`holds_conditional_other`, `holds_opponent_pick`,
`holds_pooled_pick`, `self_restricted`, `opp_restricted`); `n_worlds` and `precision_met`; and the
precision-matched verdicts (`*_pm`). τ is in units of the value of the first pick.

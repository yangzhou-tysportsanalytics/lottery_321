# Conference version: figures and derived tables

`make_figures.py` redraws the figures of the short conference version of the paper and writes its three derived
tables. It reads only files already in this repository (`results/primary/`, `results/exploratory_2/`,
`results/exploratory_6/`, `src/lottery321/`) and runs no simulation.

```
python tools/ssac27/make_figures.py . ssac27_output
```

Outputs: `ssac27_output/figures/` (Figures 1 to 5, A1, A2 and D1) and `ssac27_output/derived/`:

- `exposure_by_team_season.csv`: for every team-season, late-season team-games and reversals (picks held) under
  the old lottery and 3-2-1, counted from `results/primary/team_games.csv.gz` (the conference version's Table D2).
- `top_third_party_stakes_2025-26.csv`: the eight largest third-party stakes of the 2025-26 window, summed from
  `results/primary/F5_2_network_edges.csv` (the conference version's Figure D1).
- `reversal_signs_by_chart.csv`: reversals (picks held) under each lottery and how many of them have a negative draft
  value of losing on the linear chart and on all four pre-specified charts, as a point estimate and under the
  pre-specified per-chart classification, counted from `results/primary/team_games.csv.gz` (the conference version's Table D3).

Copies of the three tables are in `results/ssac27/`. These displays are descriptive and were made after the
registered analysis.

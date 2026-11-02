# Conference version: figures and derived tables

`make_figures.py` redraws the figures of the short conference version of the paper and writes its two derived
tables. It reads only files already in this repository (`results/primary/`, `results/exploratory_2/`,
`results/exploratory_6/`, `src/lottery321/`) and runs no simulation.

```
python tools/ssac27/make_figures.py . ssac27_output
```

Outputs: `ssac27_output/figures/` (Figures 1 to 5 and A1 to A3) and `ssac27_output/derived/`:

- `exposure_by_team_season.csv`: for every team-season, late-season team-games and reversals (picks held) under
  the old lottery and 3-2-1, counted from `results/primary/team_games.csv.gz` (the conference version's Table A4).
- `top_third_party_stakes_2025-26.csv`: the eight largest third-party stakes of the 2025-26 window, summed from
  `results/primary/F5_2_network_edges.csv` (the conference version's Figure A3).

Copies of both tables are in `results/ssac27/`. These displays are descriptive and were made after the
registered analysis.

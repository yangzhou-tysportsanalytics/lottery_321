# Registered analysis output

primary versus dta, matched team-games only

## C_1_paired_differences

| run_a | run_b | rule | portfolio | n_team_games | n_days | mean_diff_linear | max_abs_diff_linear | share_abs_diff_over_delta_linear | mean_diff_concave | max_abs_diff_concave | share_abs_diff_over_delta_concave | mean_diff_convex | max_abs_diff_convex | share_abs_diff_over_delta_convex | mean_diff_top3_stress | max_abs_diff_top3_stress | share_abs_diff_over_delta_top3_stress | reversal_share_a | reversal_share_b | reversal_share_diff | diff_lo99 | diff_hi99 | verdict_changed | reversal_share_a_pm | reversal_share_b_pm | verdict_changed_pm |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| primary | dta | old | actual | 1252 | 81 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0383 | 0.0383 | 0.0000 | 0.0000 | 0.0000 | 0 | 0.0272 | 0.0272 | 0 |
| primary | dta | old | own | 1252 | 81 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0 | 0.0000 | 0.0000 | 0 |
| primary | dta | new | actual | 1252 | 81 | 0.0001 | 0.0399 | 0.0232 | 0.0000 | 0.0332 | 0.0248 | 0.0002 | 0.0456 | 0.0256 | 0.0001 | 0.0138 | 0.0176 | 0.1278 | 0.1302 | -0.0024 | -0.0124 | 0.0056 | 30 | 0.1078 | 0.1070 | 16 |
| primary | dta | new | own | 1252 | 81 | 0.0002 | 0.0280 | 0.0120 | 0.0001 | 0.0168 | 0.0040 | 0.0003 | 0.0394 | 0.0224 | 0.0001 | 0.0116 | 0.0200 | 0.1022 | 0.1046 | -0.0024 | -0.0117 | 0.0043 | 17 | 0.0958 | 0.0950 | 15 |
| primary | dta | delta | actual | 1252 | 81 | 0.0001 | 0.0399 | 0.0232 | 0.0000 | 0.0332 | 0.0248 | 0.0002 | 0.0456 | 0.0256 | 0.0001 | 0.0138 | 0.0176 | 0.5407 | 0.5415 | -0.0008 | -0.0062 | 0.0025 | 7 | 0.4744 | 0.4760 | 11 |
| primary | dta | delta | own | 1252 | 81 | 0.0002 | 0.0280 | 0.0120 | 0.0001 | 0.0168 | 0.0040 | 0.0003 | 0.0394 | 0.0224 | 0.0001 | 0.0116 | 0.0200 | 0.6669 | 0.6677 | -0.0008 | -0.0049 | 0.0000 | 1 | 0.5599 | 0.5631 | 4 |

## C_2_verdict_transitions

| run_a | run_b | rule | portfolio | verdict_b | verdict_a | count |
|---|---|---|---|---|---|---|
| primary | dta | delta | actual | dominance_positive | negligible | 1 |
| primary | dta | delta | actual | dominance_positive | unresolved | 1 |
| primary | dta | delta | actual | reversal | unresolved | 2 |
| primary | dta | delta | actual | unresolved | dominance_positive | 2 |
| primary | dta | delta | actual | unresolved | reversal | 1 |
| primary | dta | delta | own | reversal | unresolved | 1 |
| primary | dta | new | actual | dominance_positive | negligible | 3 |
| primary | dta | new | actual | negligible | dominance_positive | 6 |
| primary | dta | new | actual | negligible | unresolved | 2 |
| primary | dta | new | actual | reversal | negligible | 1 |
| primary | dta | new | actual | reversal | unresolved | 6 |
| primary | dta | new | actual | unresolved | dominance_positive | 4 |
| primary | dta | new | actual | unresolved | negligible | 4 |
| primary | dta | new | actual | unresolved | reversal | 4 |
| primary | dta | new | own | dominance_positive | negligible | 2 |
| primary | dta | new | own | negligible | dominance_positive | 7 |
| primary | dta | new | own | reversal | negligible | 1 |
| primary | dta | new | own | reversal | unresolved | 3 |
| primary | dta | new | own | unresolved | dominance_positive | 3 |
| primary | dta | new | own | unresolved | reversal | 1 |

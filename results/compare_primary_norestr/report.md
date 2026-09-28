# Registered analysis output

primary versus norestr, matched team-games only

## C_1_paired_differences

| run_a | run_b | rule | portfolio | n_team_games | n_days | mean_diff_linear | max_abs_diff_linear | share_abs_diff_over_delta_linear | mean_diff_concave | max_abs_diff_concave | share_abs_diff_over_delta_concave | mean_diff_convex | max_abs_diff_convex | share_abs_diff_over_delta_convex | mean_diff_top3_stress | max_abs_diff_top3_stress | share_abs_diff_over_delta_top3_stress | reversal_share_a | reversal_share_b | reversal_share_diff | diff_lo99 | diff_hi99 | verdict_changed | reversal_share_a_pm | reversal_share_b_pm | verdict_changed_pm |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| primary | norestr | old | actual | 4896 | 312 | 0.0000 | 0.0009 | 0.0000 | -0.0000 | 0.0006 | 0.0000 | 0.0000 | 0.0013 | 0.0000 | -0.0000 | 0.0035 | 0.0002 | 0.0349 | 0.0349 | 0.0000 | 0.0000 | 0.0000 | 0 | 0.0251 | 0.0251 | 0 |
| primary | norestr | old | own | 4896 | 312 | 0.0000 | 0.0007 | 0.0000 | 0.0000 | 0.0006 | 0.0000 | 0.0000 | 0.0008 | 0.0000 | 0.0000 | 0.0004 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0 | 0.0000 | 0.0000 | 0 |
| primary | norestr | new | actual | 4896 | 312 | 0.0003 | 0.0548 | 0.0392 | 0.0002 | 0.0390 | 0.0321 | 0.0004 | 0.0761 | 0.0603 | 0.0005 | 0.1041 | 0.0844 | 0.1301 | 0.1299 | 0.0002 | -0.0023 | 0.0027 | 75 | 0.1078 | 0.1058 | 70 |
| primary | norestr | new | own | 4896 | 312 | 0.0003 | 0.0454 | 0.0272 | 0.0002 | 0.0258 | 0.0074 | 0.0005 | 0.0712 | 0.0637 | 0.0008 | 0.1041 | 0.1111 | 0.1033 | 0.1046 | -0.0012 | -0.0039 | 0.0013 | 29 | 0.0948 | 0.0944 | 29 |
| primary | norestr | delta | actual | 4896 | 312 | 0.0003 | 0.0548 | 0.0392 | 0.0002 | 0.0390 | 0.0321 | 0.0004 | 0.0761 | 0.0603 | 0.0005 | 0.1041 | 0.0844 | 0.5382 | 0.5368 | 0.0014 | -0.0043 | 0.0071 | 39 | 0.4767 | 0.4747 | 57 |
| primary | norestr | delta | own | 4896 | 312 | 0.0003 | 0.0454 | 0.0272 | 0.0002 | 0.0258 | 0.0074 | 0.0005 | 0.0712 | 0.0637 | 0.0008 | 0.1041 | 0.1111 | 0.6679 | 0.6679 | 0.0000 | -0.0014 | 0.0014 | 6 | 0.5643 | 0.5656 | 12 |

## C_2_verdict_transitions

| run_a | run_b | rule | portfolio | verdict_b | verdict_a | count |
|---|---|---|---|---|---|---|
| primary | norestr | delta | actual | dominance_positive | negligible | 1 |
| primary | norestr | delta | actual | dominance_positive | reversal | 8 |
| primary | norestr | delta | actual | dominance_positive | unresolved | 3 |
| primary | norestr | delta | actual | negligible | dominance_positive | 4 |
| primary | norestr | delta | actual | reversal | dominance_positive | 1 |
| primary | norestr | delta | actual | reversal | negligible | 1 |
| primary | norestr | delta | actual | reversal | unresolved | 8 |
| primary | norestr | delta | actual | unresolved | dominance_positive | 3 |
| primary | norestr | delta | actual | unresolved | negligible | 1 |
| primary | norestr | delta | actual | unresolved | reversal | 9 |
| primary | norestr | delta | own | dominance_positive | unresolved | 1 |
| primary | norestr | delta | own | reversal | unresolved | 2 |
| primary | norestr | delta | own | unresolved | dominance_positive | 1 |
| primary | norestr | delta | own | unresolved | reversal | 2 |
| primary | norestr | new | actual | dominance_positive | negligible | 16 |
| primary | norestr | new | actual | dominance_positive | reversal | 1 |
| primary | norestr | new | actual | dominance_positive | unresolved | 4 |
| primary | norestr | new | actual | negligible | dominance_positive | 14 |
| primary | norestr | new | actual | negligible | reversal | 2 |
| primary | norestr | new | actual | negligible | unresolved | 4 |
| primary | norestr | new | actual | reversal | negligible | 1 |
| primary | norestr | new | actual | reversal | unresolved | 7 |
| primary | norestr | new | actual | unresolved | dominance_positive | 8 |
| primary | norestr | new | actual | unresolved | negligible | 12 |
| primary | norestr | new | actual | unresolved | reversal | 6 |
| primary | norestr | new | own | dominance_positive | negligible | 2 |
| primary | norestr | new | own | dominance_positive | unresolved | 1 |
| primary | norestr | new | own | negligible | dominance_positive | 13 |
| primary | norestr | new | own | negligible | reversal | 2 |
| primary | norestr | new | own | reversal | unresolved | 9 |
| primary | norestr | new | own | unresolved | dominance_positive | 1 |
| primary | norestr | new | own | unresolved | reversal | 1 |

## T5_4_restrictions

| portfolio | group | delta_reversal_share | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| actual | holds_restricted_pick | 0.0059 | 341 | 0.0001 | -0.0000 | 0.0000 | 0.0002 | 0.0007 |
| actual | other | 0.0010 | 4145 | 0.0004 | 0.0000 | 0.0000 | 0.0003 | 0.0012 |
| actual | restricted_native | -0.0122 | 410 | -0.0008 | -0.0002 | 0.0000 | 0.0003 | 0.0008 |
| own | holds_restricted_pick | -0.0029 | 341 | 0.0003 | 0.0000 | 0.0001 | 0.0005 | 0.0009 |
| own | other | 0.0005 | 4145 | 0.0004 | 0.0000 | 0.0000 | 0.0004 | 0.0012 |
| own | restricted_native | -0.0171 | 410 | -0.0005 | -0.0003 | 0.0000 | 0.0002 | 0.0008 |

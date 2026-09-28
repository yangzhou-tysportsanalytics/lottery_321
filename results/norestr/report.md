# Registered analysis output

tag `norestr`; exclude_imprecise=False; states=312

## T5_0_diagnostics

| states | games | stopped_2000 | stopped_8000 | stopped_32000 | missed_target | n_worlds_match | max_halfwidth_linear | max_halfwidth_linear_rules_only | max_halfwidth_delta_linear | p95_halfwidth_linear | max_q_total_dev | max_per_slot_dev | per_slot_noise_scale | max_own_slot_dev | max_zero_sum_dev |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 312 | 2448 | 3 | 22 | 135 | 152 | 2000 | 0.0078 | 0.0078 | 0.0067 | 0.0049 | 0.0000 | 0.0109 | 0.0112 | 0.0000 | 0.0068 |

## T5_0b_zero_sum_by_curve

| curve | rule | max_zero_sum_dev | mean_zero_sum_dev | n_games |
|---|---|---|---|---|
| linear | old | 0.0012 | 0.0001 | 2448 |
| linear | new | 0.0019 | 0.0001 | 2448 |
| concave | old | 0.0007 | 0.0001 | 2448 |
| concave | new | 0.0011 | 0.0001 | 2448 |
| convex | old | 0.0020 | 0.0002 | 2448 |
| convex | new | 0.0028 | 0.0002 | 2448 |
| top3_stress | old | 0.0068 | 0.0004 | 2448 |
| top3_stress | new | 0.0037 | 0.0003 | 2448 |

## T5_0c_verdict_by_look

| rule | portfolio | stopped_at | verdict_B | verdict_B_pm | count |
|---|---|---|---|---|---|
| delta | actual | 2000 | dominance_positive | dominance_positive | 1 |
| delta | actual | 2000 | negligible | negligible | 3 |
| delta | actual | 2000 | reversal | reversal | 7 |
| delta | actual | 2000 | unresolved | unresolved | 1 |
| delta | actual | 32000 | dominance_positive | dominance_positive | 127 |
| delta | actual | 32000 | dominance_positive | unresolved | 97 |
| delta | actual | 32000 | negligible | dominance_positive | 1 |
| delta | actual | 32000 | negligible | negligible | 586 |
| delta | actual | 32000 | negligible | unresolved | 45 |
| delta | actual | 32000 | reversal | reversal | 944 |
| delta | actual | 32000 | reversal | unresolved | 140 |
| delta | actual | 32000 | unresolved | unresolved | 64 |
| delta | actual | 8000 | dominance_positive | dominance_positive | 6 |
| delta | actual | 8000 | dominance_positive | unresolved | 5 |
| delta | actual | 8000 | negligible | negligible | 79 |
| delta | actual | 8000 | negligible | unresolved | 8 |
| delta | actual | 8000 | reversal | reversal | 114 |
| delta | actual | 8000 | reversal | unresolved | 7 |
| delta | actual | 8000 | unresolved | unresolved | 11 |
| delta | actual | missed | dominance_positive | dominance_positive | 199 |
| delta | actual | missed | dominance_positive | unresolved | 136 |
| delta | actual | missed | negligible | dominance_positive | 6 |
| delta | actual | missed | negligible | negligible | 760 |
| delta | actual | missed | negligible | unresolved | 44 |
| delta | actual | missed | reversal | reversal | 1259 |
| delta | actual | missed | reversal | unresolved | 157 |
| delta | actual | missed | unresolved | unresolved | 89 |
| delta | own | 2000 | negligible | negligible | 1 |
| delta | own | 2000 | reversal | reversal | 10 |
| delta | own | 2000 | unresolved | unresolved | 1 |
| delta | own | 32000 | dominance_positive | dominance_positive | 3 |
| delta | own | 32000 | dominance_positive | unresolved | 136 |
| delta | own | 32000 | negligible | negligible | 348 |
| delta | own | 32000 | negligible | unresolved | 51 |
| delta | own | 32000 | reversal | reversal | 1106 |
| delta | own | 32000 | reversal | unresolved | 229 |
| delta | own | 32000 | unresolved | unresolved | 131 |
| delta | own | 8000 | dominance_positive | dominance_positive | 2 |
| delta | own | 8000 | dominance_positive | unresolved | 8 |
| delta | own | 8000 | negligible | negligible | 42 |
| delta | own | 8000 | negligible | unresolved | 10 |
| delta | own | 8000 | reversal | reversal | 130 |
| delta | own | 8000 | reversal | unresolved | 14 |
| delta | own | 8000 | unresolved | unresolved | 24 |
| delta | own | missed | dominance_positive | dominance_positive | 21 |
| delta | own | missed | dominance_positive | unresolved | 141 |
| delta | own | missed | negligible | negligible | 506 |
| delta | own | missed | negligible | unresolved | 66 |
| delta | own | missed | reversal | reversal | 1523 |
| delta | own | missed | reversal | unresolved | 258 |
| delta | own | missed | unresolved | unresolved | 135 |
| new | actual | 2000 | dominance_positive | dominance_positive | 3 |
| new | actual | 2000 | negligible | negligible | 3 |
| new | actual | 2000 | reversal | reversal | 5 |
| new | actual | 2000 | unresolved | unresolved | 1 |
| new | actual | 32000 | dominance_positive | dominance_positive | 1085 |
| new | actual | 32000 | dominance_positive | unresolved | 59 |
| new | actual | 32000 | negligible | dominance_positive | 20 |
| new | actual | 32000 | negligible | negligible | 472 |
| new | actual | 32000 | negligible | unresolved | 35 |
| new | actual | 32000 | reversal | reversal | 215 |
| new | actual | 32000 | reversal | unresolved | 60 |
| new | actual | 32000 | unresolved | unresolved | 58 |
| new | actual | 8000 | dominance_positive | dominance_positive | 123 |
| new | actual | 8000 | dominance_positive | unresolved | 3 |
| new | actual | 8000 | negligible | dominance_positive | 3 |
| new | actual | 8000 | negligible | negligible | 61 |
| new | actual | 8000 | negligible | unresolved | 1 |
| new | actual | 8000 | reversal | reversal | 29 |
| new | actual | 8000 | reversal | unresolved | 3 |
| new | actual | 8000 | unresolved | unresolved | 7 |
| new | actual | missed | dominance_positive | dominance_positive | 1321 |
| new | actual | missed | dominance_positive | unresolved | 82 |
| new | actual | missed | negligible | dominance_positive | 24 |
| new | actual | missed | negligible | negligible | 756 |
| new | actual | missed | negligible | unresolved | 54 |
| new | actual | missed | reversal | reversal | 269 |
| new | actual | missed | reversal | unresolved | 55 |
| new | actual | missed | unresolved | unresolved | 89 |
| new | own | 2000 | dominance_positive | dominance_positive | 7 |
| new | own | 2000 | reversal | reversal | 4 |
| new | own | 2000 | unresolved | unresolved | 1 |
| new | own | 32000 | dominance_positive | dominance_positive | 1510 |
| new | own | 32000 | dominance_positive | unresolved | 23 |
| new | own | 32000 | negligible | dominance_positive | 31 |
| new | own | 32000 | negligible | negligible | 188 |
| new | own | 32000 | negligible | unresolved | 3 |
| new | own | 32000 | reversal | reversal | 207 |
| new | own | 32000 | reversal | unresolved | 27 |
| new | own | 32000 | unresolved | unresolved | 15 |
| new | own | 8000 | dominance_positive | dominance_positive | 172 |
| new | own | 8000 | dominance_positive | unresolved | 1 |
| new | own | 8000 | negligible | dominance_positive | 2 |
| new | own | 8000 | negligible | negligible | 25 |
| new | own | 8000 | reversal | reversal | 28 |
| new | own | 8000 | reversal | unresolved | 1 |
| new | own | 8000 | unresolved | unresolved | 1 |
| new | own | missed | dominance_positive | dominance_positive | 1893 |
| new | own | missed | dominance_positive | unresolved | 32 |
| new | own | missed | negligible | dominance_positive | 33 |
| new | own | missed | negligible | negligible | 433 |
| new | own | missed | negligible | unresolved | 5 |
| new | own | missed | reversal | reversal | 223 |
| new | own | missed | reversal | unresolved | 22 |
| new | own | missed | unresolved | unresolved | 9 |
| old | actual | 2000 | dominance_positive | dominance_positive | 7 |
| old | actual | 2000 | negligible | negligible | 3 |
| old | actual | 2000 | reversal | reversal | 1 |
| old | actual | 2000 | unresolved | unresolved | 1 |
| old | actual | 32000 | dominance_positive | dominance_positive | 1367 |
| old | actual | 32000 | dominance_positive | unresolved | 113 |
| old | actual | 32000 | negligible | dominance_positive | 4 |
| old | actual | 32000 | negligible | negligible | 414 |
| old | actual | 32000 | negligible | unresolved | 13 |
| old | actual | 32000 | reversal | reversal | 37 |
| old | actual | 32000 | reversal | unresolved | 23 |
| old | actual | 32000 | unresolved | unresolved | 33 |
| old | actual | 8000 | dominance_positive | dominance_positive | 158 |
| old | actual | 8000 | dominance_positive | unresolved | 12 |
| old | actual | 8000 | negligible | negligible | 51 |
| old | actual | 8000 | reversal | reversal | 4 |
| old | actual | 8000 | unresolved | unresolved | 5 |
| old | actual | missed | dominance_positive | dominance_positive | 1716 |
| old | actual | missed | dominance_positive | unresolved | 145 |
| old | actual | missed | negligible | dominance_positive | 13 |
| old | actual | missed | negligible | negligible | 591 |
| old | actual | missed | negligible | unresolved | 23 |
| old | actual | missed | reversal | reversal | 81 |
| old | actual | missed | reversal | unresolved | 25 |
| old | actual | missed | unresolved | unresolved | 56 |
| old | own | 2000 | dominance_positive | dominance_positive | 12 |
| old | own | 32000 | dominance_positive | dominance_positive | 1954 |
| old | own | 32000 | dominance_positive | unresolved | 20 |
| old | own | 32000 | negligible | dominance_positive | 1 |
| old | own | 32000 | negligible | negligible | 27 |
| old | own | 32000 | negligible | unresolved | 2 |
| old | own | 8000 | dominance_positive | dominance_positive | 224 |
| old | own | 8000 | dominance_positive | unresolved | 2 |
| old | own | 8000 | negligible | negligible | 3 |
| old | own | 8000 | unresolved | unresolved | 1 |
| old | own | missed | dominance_positive | dominance_positive | 2539 |
| old | own | missed | dominance_positive | unresolved | 31 |
| old | own | missed | negligible | dominance_positive | 3 |
| old | own | missed | negligible | negligible | 70 |
| old | own | missed | negligible | unresolved | 6 |
| old | own | missed | unresolved | unresolved | 1 |

## T5_0d_band_width

| rule | portfolio | measure | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| old | actual | band_ratio | 4896 | 1.4085 | 0.2155 | 1.2540 | 2.4411 | 2.8982 |
| old | actual | band_ratio_pm | 4896 | 5.3476 | 0.8054 | 4.9419 | 9.6287 | 11.2357 |
| old | own | band_ratio | 4896 | 2.0516 | 1.0035 | 2.3270 | 2.7324 | 3.1165 |
| old | own | band_ratio_pm | 4896 | 7.7968 | 3.7896 | 9.2200 | 10.7859 | 12.0364 |
| new | actual | band_ratio | 4896 | 1.1023 | 0.0870 | 0.6222 | 2.1659 | 2.7095 |
| new | actual | band_ratio_pm | 4896 | 4.1826 | 0.3418 | 2.3917 | 8.4779 | 10.6236 |
| new | own | band_ratio | 4896 | 1.6416 | 0.2937 | 2.0233 | 2.5850 | 2.9412 |
| new | own | band_ratio_pm | 4896 | 6.2376 | 1.1546 | 8.0047 | 10.2272 | 11.4777 |
| delta | actual | band_ratio | 4896 | 1.0625 | 0.0614 | 0.6938 | 1.8048 | 2.6351 |
| delta | actual | band_ratio_pm | 4896 | 4.0639 | 0.2359 | 2.6791 | 7.0288 | 10.1804 |
| delta | own | band_ratio | 4896 | 1.3746 | 0.4151 | 1.0896 | 2.3309 | 2.8860 |
| delta | own | band_ratio_pm | 4896 | 5.2463 | 1.6366 | 4.0261 | 9.1284 | 11.2679 |

## T5_1_verdicts

| rule | portfolio | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|
| old | actual | B | dominance_positive | 0.7185 | 0.6380 | 0.8029 | 4896 |
| old | actual | B | reversal | 0.0349 | 0.0179 | 0.0645 | 4896 |
| old | actual | B | negligible | 0.2271 | 0.1583 | 0.2863 | 4896 |
| old | actual | B | unresolved | 0.0194 | 0.0120 | 0.0273 | 4896 |
| old | actual | C | dominance_positive | 0.7185 | 0.6380 | 0.8029 | 4896 |
| old | actual | C | reversal | 0.0349 | 0.0179 | 0.0645 | 4896 |
| old | actual | C | negligible | 0.2271 | 0.1583 | 0.2863 | 4896 |
| old | actual | C | unresolved | 0.0194 | 0.0120 | 0.0273 | 4896 |
| old | actual | B_pm | dominance_positive | 0.6669 | 0.5935 | 0.7514 | 4896 |
| old | actual | B_pm | reversal | 0.0251 | 0.0123 | 0.0474 | 4896 |
| old | actual | B_pm | negligible | 0.2163 | 0.1529 | 0.2728 | 4896 |
| old | actual | B_pm | unresolved | 0.0917 | 0.0714 | 0.1138 | 4896 |
| old | actual | C_pm | dominance_positive | 0.6669 | 0.5935 | 0.7514 | 4896 |
| old | actual | C_pm | reversal | 0.0251 | 0.0123 | 0.0474 | 4896 |
| old | actual | C_pm | negligible | 0.2163 | 0.1529 | 0.2728 | 4896 |
| old | actual | C_pm | unresolved | 0.0917 | 0.0714 | 0.1138 | 4896 |
| old | own | B | dominance_positive | 0.9767 | 0.9615 | 0.9896 | 4896 |
| old | own | B | reversal | 0.0000 | 0.0000 | 0.0000 | 4896 |
| old | own | B | negligible | 0.0229 | 0.0102 | 0.0383 | 4896 |
| old | own | B | unresolved | 0.0004 | 0.0000 | 0.0021 | 4896 |
| old | own | C | dominance_positive | 0.9767 | 0.9615 | 0.9896 | 4896 |
| old | own | C | reversal | 0.0000 | 0.0000 | 0.0000 | 4896 |
| old | own | C | negligible | 0.0229 | 0.0102 | 0.0383 | 4896 |
| old | own | C | unresolved | 0.0004 | 0.0000 | 0.0021 | 4896 |
| old | own | B_pm | dominance_positive | 0.9667 | 0.9456 | 0.9852 | 4896 |
| old | own | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 4896 |
| old | own | B_pm | negligible | 0.0204 | 0.0091 | 0.0347 | 4896 |
| old | own | B_pm | unresolved | 0.0129 | 0.0023 | 0.0251 | 4896 |
| old | own | C_pm | dominance_positive | 0.9667 | 0.9456 | 0.9852 | 4896 |
| old | own | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 4896 |
| old | own | C_pm | negligible | 0.0204 | 0.0091 | 0.0347 | 4896 |
| old | own | C_pm | unresolved | 0.0129 | 0.0023 | 0.0251 | 4896 |
| new | actual | B | dominance_positive | 0.5466 | 0.4563 | 0.6386 | 4896 |
| new | actual | B | reversal | 0.1299 | 0.0751 | 0.1670 | 4896 |
| new | actual | B | negligible | 0.2919 | 0.1996 | 0.3676 | 4896 |
| new | actual | B | unresolved | 0.0317 | 0.0148 | 0.0512 | 4896 |
| new | actual | C | dominance_positive | 0.5468 | 0.4563 | 0.6389 | 4896 |
| new | actual | C | reversal | 0.1297 | 0.0751 | 0.1669 | 4896 |
| new | actual | C | negligible | 0.2919 | 0.1996 | 0.3676 | 4896 |
| new | actual | C | unresolved | 0.0317 | 0.0148 | 0.0512 | 4896 |
| new | actual | B_pm | dominance_positive | 0.5268 | 0.4345 | 0.6192 | 4896 |
| new | actual | B_pm | reversal | 0.1058 | 0.0613 | 0.1348 | 4896 |
| new | actual | B_pm | negligible | 0.2639 | 0.1806 | 0.3393 | 4896 |
| new | actual | B_pm | unresolved | 0.1036 | 0.0669 | 0.1550 | 4896 |
| new | actual | C_pm | dominance_positive | 0.5272 | 0.4345 | 0.6206 | 4896 |
| new | actual | C_pm | reversal | 0.1058 | 0.0613 | 0.1348 | 4896 |
| new | actual | C_pm | negligible | 0.2639 | 0.1806 | 0.3393 | 4896 |
| new | actual | C_pm | unresolved | 0.1031 | 0.0664 | 0.1550 | 4896 |
| new | own | B | dominance_positive | 0.7431 | 0.6822 | 0.8077 | 4896 |
| new | own | B | reversal | 0.1046 | 0.0561 | 0.1454 | 4896 |
| new | own | B | negligible | 0.1471 | 0.0874 | 0.1939 | 4896 |
| new | own | B | unresolved | 0.0053 | 0.0026 | 0.0083 | 4896 |
| new | own | C | dominance_positive | 0.7431 | 0.6822 | 0.8077 | 4896 |
| new | own | C | reversal | 0.1046 | 0.0561 | 0.1454 | 4896 |
| new | own | C | negligible | 0.1471 | 0.0874 | 0.1939 | 4896 |
| new | own | C | unresolved | 0.0053 | 0.0026 | 0.0083 | 4896 |
| new | own | B_pm | dominance_positive | 0.7451 | 0.6818 | 0.8094 | 4896 |
| new | own | B_pm | reversal | 0.0944 | 0.0492 | 0.1357 | 4896 |
| new | own | B_pm | negligible | 0.1319 | 0.0765 | 0.1763 | 4896 |
| new | own | B_pm | unresolved | 0.0286 | 0.0173 | 0.0434 | 4896 |
| new | own | C_pm | dominance_positive | 0.7451 | 0.6818 | 0.8094 | 4896 |
| new | own | C_pm | reversal | 0.0944 | 0.0492 | 0.1357 | 4896 |
| new | own | C_pm | negligible | 0.1319 | 0.0765 | 0.1763 | 4896 |
| new | own | C_pm | unresolved | 0.0286 | 0.0173 | 0.0434 | 4896 |
| delta | actual | B | dominance_positive | 0.1166 | 0.0778 | 0.1500 | 4896 |
| delta | actual | B | reversal | 0.5368 | 0.4888 | 0.5904 | 4896 |
| delta | actual | B | negligible | 0.3129 | 0.2773 | 0.3590 | 4896 |
| delta | actual | B | unresolved | 0.0337 | 0.0224 | 0.0456 | 4896 |
| delta | actual | C | dominance_positive | 0.1166 | 0.0778 | 0.1500 | 4896 |
| delta | actual | C | reversal | 0.5368 | 0.4888 | 0.5904 | 4896 |
| delta | actual | C | negligible | 0.3129 | 0.2773 | 0.3590 | 4896 |
| delta | actual | C | unresolved | 0.0337 | 0.0224 | 0.0456 | 4896 |
| delta | actual | B_pm | dominance_positive | 0.0694 | 0.0369 | 0.0998 | 4896 |
| delta | actual | B_pm | reversal | 0.4747 | 0.4308 | 0.5187 | 4896 |
| delta | actual | B_pm | negligible | 0.2917 | 0.2558 | 0.3310 | 4896 |
| delta | actual | B_pm | unresolved | 0.1642 | 0.1357 | 0.1935 | 4896 |
| delta | actual | C_pm | dominance_positive | 0.0694 | 0.0369 | 0.0998 | 4896 |
| delta | actual | C_pm | reversal | 0.4747 | 0.4308 | 0.5187 | 4896 |
| delta | actual | C_pm | negligible | 0.2917 | 0.2558 | 0.3310 | 4896 |
| delta | actual | C_pm | unresolved | 0.1642 | 0.1357 | 0.1935 | 4896 |
| delta | own | B | dominance_positive | 0.0635 | 0.0471 | 0.0798 | 4896 |
| delta | own | B | reversal | 0.6679 | 0.6378 | 0.6995 | 4896 |
| delta | own | B | negligible | 0.2092 | 0.1786 | 0.2403 | 4896 |
| delta | own | B | unresolved | 0.0594 | 0.0445 | 0.0755 | 4896 |
| delta | own | C | dominance_positive | 0.0635 | 0.0471 | 0.0798 | 4896 |
| delta | own | C | reversal | 0.6679 | 0.6378 | 0.6995 | 4896 |
| delta | own | C | negligible | 0.2092 | 0.1786 | 0.2403 | 4896 |
| delta | own | C | unresolved | 0.0594 | 0.0445 | 0.0755 | 4896 |
| delta | own | B_pm | dominance_positive | 0.0053 | 0.0025 | 0.0089 | 4896 |
| delta | own | B_pm | reversal | 0.5656 | 0.5130 | 0.6163 | 4896 |
| delta | own | B_pm | negligible | 0.1832 | 0.1488 | 0.2161 | 4896 |
| delta | own | B_pm | unresolved | 0.2459 | 0.2118 | 0.2813 | 4896 |
| delta | own | C_pm | dominance_positive | 0.0053 | 0.0025 | 0.0089 | 4896 |
| delta | own | C_pm | reversal | 0.5656 | 0.5130 | 0.6163 | 4896 |
| delta | own | C_pm | negligible | 0.1832 | 0.1488 | 0.2161 | 4896 |
| delta | own | C_pm | unresolved | 0.2459 | 0.2118 | 0.2813 | 4896 |

## T5_2_verdicts_by_band

| rule | portfolio | band | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| old | actual | 1-3 | B | dominance_positive | 0.7778 | 0.6411 | 0.9015 | 495 |
| old | actual | 1-3 | B | reversal | 0.0343 | 0.0043 | 0.0738 | 495 |
| old | actual | 1-3 | B | negligible | 0.0727 | 0.0020 | 0.1715 | 495 |
| old | actual | 1-3 | B | unresolved | 0.1152 | 0.0366 | 0.2031 | 495 |
| old | actual | 1-3 | C | dominance_positive | 0.7778 | 0.6411 | 0.9015 | 495 |
| old | actual | 1-3 | C | reversal | 0.0343 | 0.0043 | 0.0738 | 495 |
| old | actual | 1-3 | C | negligible | 0.0727 | 0.0020 | 0.1715 | 495 |
| old | actual | 1-3 | C | unresolved | 0.1152 | 0.0366 | 0.2031 | 495 |
| old | actual | 1-3 | B_pm | dominance_positive | 0.6081 | 0.3606 | 0.8235 | 495 |
| old | actual | 1-3 | B_pm | reversal | 0.0283 | 0.0042 | 0.0584 | 495 |
| old | actual | 1-3 | B_pm | negligible | 0.0707 | 0.0020 | 0.1664 | 495 |
| old | actual | 1-3 | B_pm | unresolved | 0.2929 | 0.1197 | 0.4531 | 495 |
| old | actual | 1-3 | C_pm | dominance_positive | 0.6081 | 0.3606 | 0.8235 | 495 |
| old | actual | 1-3 | C_pm | reversal | 0.0283 | 0.0042 | 0.0584 | 495 |
| old | actual | 1-3 | C_pm | negligible | 0.0707 | 0.0020 | 0.1664 | 495 |
| old | actual | 1-3 | C_pm | unresolved | 0.2929 | 0.1197 | 0.4531 | 495 |
| old | actual | 4-10 | B | dominance_positive | 0.8717 | 0.7925 | 0.9447 | 1146 |
| old | actual | 4-10 | B | reversal | 0.0419 | 0.0172 | 0.0749 | 1146 |
| old | actual | 4-10 | B | negligible | 0.0750 | 0.0251 | 0.1317 | 1146 |
| old | actual | 4-10 | B | unresolved | 0.0113 | 0.0000 | 0.0297 | 1146 |
| old | actual | 4-10 | C | dominance_positive | 0.8717 | 0.7925 | 0.9447 | 1146 |
| old | actual | 4-10 | C | reversal | 0.0419 | 0.0172 | 0.0749 | 1146 |
| old | actual | 4-10 | C | negligible | 0.0750 | 0.0251 | 0.1317 | 1146 |
| old | actual | 4-10 | C | unresolved | 0.0113 | 0.0000 | 0.0297 | 1146 |
| old | actual | 4-10 | B_pm | dominance_positive | 0.7880 | 0.6551 | 0.9028 | 1146 |
| old | actual | 4-10 | B_pm | reversal | 0.0271 | 0.0089 | 0.0512 | 1146 |
| old | actual | 4-10 | B_pm | negligible | 0.0733 | 0.0227 | 0.1309 | 1146 |
| old | actual | 4-10 | B_pm | unresolved | 0.1117 | 0.0458 | 0.1898 | 1146 |
| old | actual | 4-10 | C_pm | dominance_positive | 0.7880 | 0.6551 | 0.9028 | 1146 |
| old | actual | 4-10 | C_pm | reversal | 0.0271 | 0.0089 | 0.0512 | 1146 |
| old | actual | 4-10 | C_pm | negligible | 0.0733 | 0.0227 | 0.1309 | 1146 |
| old | actual | 4-10 | C_pm | unresolved | 0.1117 | 0.0458 | 0.1898 | 1146 |
| old | actual | 11-16 | B | dominance_positive | 0.7822 | 0.6563 | 0.8986 | 978 |
| old | actual | 11-16 | B | reversal | 0.0286 | 0.0020 | 0.0712 | 978 |
| old | actual | 11-16 | B | negligible | 0.1759 | 0.0811 | 0.2910 | 978 |
| old | actual | 11-16 | B | unresolved | 0.0133 | 0.0000 | 0.0417 | 978 |
| old | actual | 11-16 | C | dominance_positive | 0.7822 | 0.6563 | 0.8986 | 978 |
| old | actual | 11-16 | C | reversal | 0.0286 | 0.0020 | 0.0712 | 978 |
| old | actual | 11-16 | C | negligible | 0.1759 | 0.0811 | 0.2910 | 978 |
| old | actual | 11-16 | C | unresolved | 0.0133 | 0.0000 | 0.0417 | 978 |
| old | actual | 11-16 | B_pm | dominance_positive | 0.7495 | 0.6204 | 0.8843 | 978 |
| old | actual | 11-16 | B_pm | reversal | 0.0184 | 0.0010 | 0.0434 | 978 |
| old | actual | 11-16 | B_pm | negligible | 0.1626 | 0.0782 | 0.2734 | 978 |
| old | actual | 11-16 | B_pm | unresolved | 0.0695 | 0.0129 | 0.1403 | 978 |
| old | actual | 11-16 | C_pm | dominance_positive | 0.7495 | 0.6204 | 0.8843 | 978 |
| old | actual | 11-16 | C_pm | reversal | 0.0184 | 0.0010 | 0.0434 | 978 |
| old | actual | 11-16 | C_pm | negligible | 0.1626 | 0.0782 | 0.2734 | 978 |
| old | actual | 11-16 | C_pm | unresolved | 0.0695 | 0.0129 | 0.1403 | 978 |
| old | actual | 17-30 | B | dominance_positive | 0.6012 | 0.4142 | 0.7580 | 2277 |
| old | actual | 17-30 | B | reversal | 0.0343 | 0.0075 | 0.0898 | 2277 |
| old | actual | 17-30 | B | negligible | 0.3592 | 0.2304 | 0.5045 | 2277 |
| old | actual | 17-30 | B | unresolved | 0.0053 | 0.0000 | 0.0134 | 2277 |
| old | actual | 17-30 | C | dominance_positive | 0.6012 | 0.4142 | 0.7580 | 2277 |
| old | actual | 17-30 | C | reversal | 0.0343 | 0.0075 | 0.0898 | 2277 |
| old | actual | 17-30 | C | negligible | 0.3592 | 0.2304 | 0.5045 | 2277 |
| old | actual | 17-30 | C | unresolved | 0.0053 | 0.0000 | 0.0134 | 2277 |
| old | actual | 17-30 | B_pm | dominance_positive | 0.5832 | 0.3860 | 0.7519 | 2277 |
| old | actual | 17-30 | B_pm | reversal | 0.0264 | 0.0043 | 0.0712 | 2277 |
| old | actual | 17-30 | B_pm | negligible | 0.3430 | 0.2181 | 0.4828 | 2277 |
| old | actual | 17-30 | B_pm | unresolved | 0.0474 | 0.0147 | 0.0817 | 2277 |
| old | actual | 17-30 | C_pm | dominance_positive | 0.5832 | 0.3860 | 0.7519 | 2277 |
| old | actual | 17-30 | C_pm | reversal | 0.0264 | 0.0043 | 0.0712 | 2277 |
| old | actual | 17-30 | C_pm | negligible | 0.3430 | 0.2181 | 0.4828 | 2277 |
| old | actual | 17-30 | C_pm | unresolved | 0.0474 | 0.0147 | 0.0817 | 2277 |
| old | own | 1-3 | B | dominance_positive | 0.9758 | 0.9407 | 0.9980 | 495 |
| old | own | 1-3 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 495 |
| old | own | 1-3 | B | negligible | 0.0242 | 0.0020 | 0.0593 | 495 |
| old | own | 1-3 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 495 |
| old | own | 1-3 | C | dominance_positive | 0.9758 | 0.9407 | 0.9980 | 495 |
| old | own | 1-3 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 495 |
| old | own | 1-3 | C | negligible | 0.0242 | 0.0020 | 0.0593 | 495 |
| old | own | 1-3 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 495 |
| old | own | 1-3 | B_pm | dominance_positive | 0.9778 | 0.9414 | 1.0000 | 495 |
| old | own | 1-3 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 495 |
| old | own | 1-3 | B_pm | negligible | 0.0222 | 0.0000 | 0.0586 | 495 |
| old | own | 1-3 | B_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 495 |
| old | own | 1-3 | C_pm | dominance_positive | 0.9778 | 0.9414 | 1.0000 | 495 |
| old | own | 1-3 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 495 |
| old | own | 1-3 | C_pm | negligible | 0.0222 | 0.0000 | 0.0586 | 495 |
| old | own | 1-3 | C_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 495 |
| old | own | 4-10 | B | dominance_positive | 0.9729 | 0.9381 | 0.9965 | 1146 |
| old | own | 4-10 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 1146 |
| old | own | 4-10 | B | negligible | 0.0253 | 0.0027 | 0.0611 | 1146 |
| old | own | 4-10 | B | unresolved | 0.0017 | 0.0000 | 0.0089 | 1146 |
| old | own | 4-10 | C | dominance_positive | 0.9729 | 0.9381 | 0.9965 | 1146 |
| old | own | 4-10 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 1146 |
| old | own | 4-10 | C | negligible | 0.0253 | 0.0027 | 0.0611 | 1146 |
| old | own | 4-10 | C | unresolved | 0.0017 | 0.0000 | 0.0089 | 1146 |
| old | own | 4-10 | B_pm | dominance_positive | 0.9642 | 0.9293 | 0.9937 | 1146 |
| old | own | 4-10 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 1146 |
| old | own | 4-10 | B_pm | negligible | 0.0227 | 0.0026 | 0.0540 | 1146 |
| old | own | 4-10 | B_pm | unresolved | 0.0131 | 0.0000 | 0.0439 | 1146 |
| old | own | 4-10 | C_pm | dominance_positive | 0.9642 | 0.9293 | 0.9937 | 1146 |
| old | own | 4-10 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 1146 |
| old | own | 4-10 | C_pm | negligible | 0.0227 | 0.0026 | 0.0540 | 1146 |
| old | own | 4-10 | C_pm | unresolved | 0.0131 | 0.0000 | 0.0439 | 1146 |
| old | own | 11-16 | B | dominance_positive | 0.9959 | 0.9875 | 1.0000 | 978 |
| old | own | 11-16 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 978 |
| old | own | 11-16 | B | negligible | 0.0041 | 0.0000 | 0.0125 | 978 |
| old | own | 11-16 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 978 |
| old | own | 11-16 | C | dominance_positive | 0.9959 | 0.9875 | 1.0000 | 978 |
| old | own | 11-16 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 978 |
| old | own | 11-16 | C | negligible | 0.0041 | 0.0000 | 0.0125 | 978 |
| old | own | 11-16 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 978 |
| old | own | 11-16 | B_pm | dominance_positive | 0.9703 | 0.9383 | 0.9940 | 978 |
| old | own | 11-16 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 978 |
| old | own | 11-16 | B_pm | negligible | 0.0031 | 0.0000 | 0.0095 | 978 |
| old | own | 11-16 | B_pm | unresolved | 0.0266 | 0.0030 | 0.0568 | 978 |
| old | own | 11-16 | C_pm | dominance_positive | 0.9703 | 0.9383 | 0.9940 | 978 |
| old | own | 11-16 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 978 |
| old | own | 11-16 | C_pm | negligible | 0.0031 | 0.0000 | 0.0095 | 978 |
| old | own | 11-16 | C_pm | unresolved | 0.0266 | 0.0030 | 0.0568 | 978 |
| old | own | 17-30 | B | dominance_positive | 0.9706 | 0.9397 | 0.9945 | 2277 |
| old | own | 17-30 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 2277 |
| old | own | 17-30 | B | negligible | 0.0294 | 0.0055 | 0.0603 | 2277 |
| old | own | 17-30 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 2277 |
| old | own | 17-30 | C | dominance_positive | 0.9706 | 0.9397 | 0.9945 | 2277 |
| old | own | 17-30 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 2277 |
| old | own | 17-30 | C | negligible | 0.0294 | 0.0055 | 0.0603 | 2277 |
| old | own | 17-30 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 2277 |
| old | own | 17-30 | B_pm | dominance_positive | 0.9640 | 0.9313 | 0.9908 | 2277 |
| old | own | 17-30 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 2277 |
| old | own | 17-30 | B_pm | negligible | 0.0264 | 0.0050 | 0.0539 | 2277 |
| old | own | 17-30 | B_pm | unresolved | 0.0097 | 0.0021 | 0.0184 | 2277 |
| old | own | 17-30 | C_pm | dominance_positive | 0.9640 | 0.9313 | 0.9908 | 2277 |
| old | own | 17-30 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 2277 |
| old | own | 17-30 | C_pm | negligible | 0.0264 | 0.0050 | 0.0539 | 2277 |
| old | own | 17-30 | C_pm | unresolved | 0.0097 | 0.0021 | 0.0184 | 2277 |
| new | actual | 1-3 | B | dominance_positive | 0.0808 | 0.0299 | 0.1401 | 495 |
| new | actual | 1-3 | B | reversal | 0.5596 | 0.3103 | 0.7782 | 495 |
| new | actual | 1-3 | B | negligible | 0.2384 | 0.1012 | 0.3988 | 495 |
| new | actual | 1-3 | B | unresolved | 0.1212 | 0.0425 | 0.2246 | 495 |
| new | actual | 1-3 | C | dominance_positive | 0.0808 | 0.0299 | 0.1401 | 495 |
| new | actual | 1-3 | C | reversal | 0.5596 | 0.3103 | 0.7782 | 495 |
| new | actual | 1-3 | C | negligible | 0.2384 | 0.1012 | 0.3988 | 495 |
| new | actual | 1-3 | C | unresolved | 0.1212 | 0.0425 | 0.2246 | 495 |
| new | actual | 1-3 | B_pm | dominance_positive | 0.0444 | 0.0139 | 0.0771 | 495 |
| new | actual | 1-3 | B_pm | reversal | 0.4667 | 0.2484 | 0.6448 | 495 |
| new | actual | 1-3 | B_pm | negligible | 0.1939 | 0.0751 | 0.3376 | 495 |
| new | actual | 1-3 | B_pm | unresolved | 0.2949 | 0.1832 | 0.4020 | 495 |
| new | actual | 1-3 | C_pm | dominance_positive | 0.0444 | 0.0139 | 0.0771 | 495 |
| new | actual | 1-3 | C_pm | reversal | 0.4667 | 0.2484 | 0.6448 | 495 |
| new | actual | 1-3 | C_pm | negligible | 0.1939 | 0.0751 | 0.3376 | 495 |
| new | actual | 1-3 | C_pm | unresolved | 0.2949 | 0.1832 | 0.4020 | 495 |
| new | actual | 4-10 | B | dominance_positive | 0.4311 | 0.2157 | 0.6341 | 1146 |
| new | actual | 4-10 | B | reversal | 0.2077 | 0.1230 | 0.2716 | 1146 |
| new | actual | 4-10 | B | negligible | 0.3054 | 0.1630 | 0.4213 | 1146 |
| new | actual | 4-10 | B | unresolved | 0.0558 | 0.0115 | 0.1338 | 1146 |
| new | actual | 4-10 | C | dominance_positive | 0.4311 | 0.2157 | 0.6341 | 1146 |
| new | actual | 4-10 | C | reversal | 0.2077 | 0.1230 | 0.2716 | 1146 |
| new | actual | 4-10 | C | negligible | 0.3054 | 0.1630 | 0.4213 | 1146 |
| new | actual | 4-10 | C | unresolved | 0.0558 | 0.0115 | 0.1338 | 1146 |
| new | actual | 4-10 | B_pm | dominance_positive | 0.4049 | 0.1672 | 0.6085 | 1146 |
| new | actual | 4-10 | B_pm | reversal | 0.1693 | 0.1098 | 0.2196 | 1146 |
| new | actual | 4-10 | B_pm | negligible | 0.2452 | 0.1366 | 0.3345 | 1146 |
| new | actual | 4-10 | B_pm | unresolved | 0.1806 | 0.0503 | 0.3449 | 1146 |
| new | actual | 4-10 | C_pm | dominance_positive | 0.4049 | 0.1672 | 0.6085 | 1146 |
| new | actual | 4-10 | C_pm | reversal | 0.1693 | 0.1098 | 0.2196 | 1146 |
| new | actual | 4-10 | C_pm | negligible | 0.2452 | 0.1366 | 0.3345 | 1146 |
| new | actual | 4-10 | C_pm | unresolved | 0.1806 | 0.0503 | 0.3449 | 1146 |
| new | actual | 11-16 | B | dominance_positive | 0.7342 | 0.5807 | 0.8777 | 978 |
| new | actual | 11-16 | B | reversal | 0.0184 | 0.0000 | 0.0470 | 978 |
| new | actual | 11-16 | B | negligible | 0.2352 | 0.1097 | 0.3762 | 978 |
| new | actual | 11-16 | B | unresolved | 0.0123 | 0.0010 | 0.0296 | 978 |
| new | actual | 11-16 | C | dominance_positive | 0.7342 | 0.5807 | 0.8777 | 978 |
| new | actual | 11-16 | C | reversal | 0.0184 | 0.0000 | 0.0470 | 978 |
| new | actual | 11-16 | C | negligible | 0.2352 | 0.1097 | 0.3762 | 978 |
| new | actual | 11-16 | C | unresolved | 0.0123 | 0.0010 | 0.0296 | 978 |
| new | actual | 11-16 | B_pm | dominance_positive | 0.7157 | 0.5689 | 0.8667 | 978 |
| new | actual | 11-16 | B_pm | reversal | 0.0112 | 0.0000 | 0.0315 | 978 |
| new | actual | 11-16 | B_pm | negligible | 0.2219 | 0.1070 | 0.3529 | 978 |
| new | actual | 11-16 | B_pm | unresolved | 0.0511 | 0.0155 | 0.0876 | 978 |
| new | actual | 11-16 | C_pm | dominance_positive | 0.7157 | 0.5689 | 0.8667 | 978 |
| new | actual | 11-16 | C_pm | reversal | 0.0112 | 0.0000 | 0.0315 | 978 |
| new | actual | 11-16 | C_pm | negligible | 0.2219 | 0.1070 | 0.3529 | 978 |
| new | actual | 11-16 | C_pm | unresolved | 0.0511 | 0.0155 | 0.0876 | 978 |
| new | actual | 17-30 | B | dominance_positive | 0.6254 | 0.4750 | 0.7505 | 2277 |
| new | actual | 17-30 | B | reversal | 0.0452 | 0.0124 | 0.0915 | 2277 |
| new | actual | 17-30 | B | negligible | 0.3210 | 0.2074 | 0.4447 | 2277 |
| new | actual | 17-30 | B | unresolved | 0.0083 | 0.0034 | 0.0143 | 2277 |
| new | actual | 17-30 | C | dominance_positive | 0.6258 | 0.4750 | 0.7515 | 2277 |
| new | actual | 17-30 | C | reversal | 0.0448 | 0.0124 | 0.0915 | 2277 |
| new | actual | 17-30 | C | negligible | 0.3210 | 0.2074 | 0.4447 | 2277 |
| new | actual | 17-30 | C | unresolved | 0.0083 | 0.0034 | 0.0145 | 2277 |
| new | actual | 17-30 | B_pm | dominance_positive | 0.6118 | 0.4592 | 0.7442 | 2277 |
| new | actual | 17-30 | B_pm | reversal | 0.0360 | 0.0084 | 0.0764 | 2277 |
| new | actual | 17-30 | B_pm | negligible | 0.3065 | 0.1965 | 0.4270 | 2277 |
| new | actual | 17-30 | B_pm | unresolved | 0.0457 | 0.0215 | 0.0777 | 2277 |
| new | actual | 17-30 | C_pm | dominance_positive | 0.6126 | 0.4592 | 0.7460 | 2277 |
| new | actual | 17-30 | C_pm | reversal | 0.0360 | 0.0084 | 0.0764 | 2277 |
| new | actual | 17-30 | C_pm | negligible | 0.3065 | 0.1965 | 0.4270 | 2277 |
| new | actual | 17-30 | C_pm | unresolved | 0.0448 | 0.0200 | 0.0776 | 2277 |
| new | own | 1-3 | B | dominance_positive | 0.0525 | 0.0126 | 0.1006 | 495 |
| new | own | 1-3 | B | reversal | 0.5879 | 0.3231 | 0.8205 | 495 |
| new | own | 1-3 | B | negligible | 0.3333 | 0.1273 | 0.5880 | 495 |
| new | own | 1-3 | B | unresolved | 0.0263 | 0.0083 | 0.0472 | 495 |
| new | own | 1-3 | C | dominance_positive | 0.0525 | 0.0126 | 0.1006 | 495 |
| new | own | 1-3 | C | reversal | 0.5879 | 0.3231 | 0.8205 | 495 |
| new | own | 1-3 | C | negligible | 0.3333 | 0.1273 | 0.5880 | 495 |
| new | own | 1-3 | C | unresolved | 0.0263 | 0.0083 | 0.0472 | 495 |
| new | own | 1-3 | B_pm | dominance_positive | 0.0566 | 0.0121 | 0.1052 | 495 |
| new | own | 1-3 | B_pm | reversal | 0.5293 | 0.2751 | 0.7663 | 495 |
| new | own | 1-3 | B_pm | negligible | 0.2768 | 0.1047 | 0.5175 | 495 |
| new | own | 1-3 | B_pm | unresolved | 0.1374 | 0.0858 | 0.1904 | 495 |
| new | own | 1-3 | C_pm | dominance_positive | 0.0566 | 0.0121 | 0.1052 | 495 |
| new | own | 1-3 | C_pm | reversal | 0.5293 | 0.2751 | 0.7663 | 495 |
| new | own | 1-3 | C_pm | negligible | 0.2768 | 0.1047 | 0.5175 | 495 |
| new | own | 1-3 | C_pm | unresolved | 0.1374 | 0.0858 | 0.1904 | 495 |
| new | own | 4-10 | B | dominance_positive | 0.4241 | 0.1886 | 0.6316 | 1146 |
| new | own | 4-10 | B | reversal | 0.1928 | 0.0951 | 0.2785 | 1146 |
| new | own | 4-10 | B | negligible | 0.3717 | 0.1794 | 0.5437 | 1146 |
| new | own | 4-10 | B | unresolved | 0.0113 | 0.0026 | 0.0221 | 1146 |
| new | own | 4-10 | C | dominance_positive | 0.4241 | 0.1886 | 0.6316 | 1146 |
| new | own | 4-10 | C | reversal | 0.1928 | 0.0951 | 0.2785 | 1146 |
| new | own | 4-10 | C | negligible | 0.3717 | 0.1794 | 0.5437 | 1146 |
| new | own | 4-10 | C | unresolved | 0.0113 | 0.0026 | 0.0221 | 1146 |
| new | own | 4-10 | B_pm | dominance_positive | 0.4424 | 0.2103 | 0.6387 | 1146 |
| new | own | 4-10 | B_pm | reversal | 0.1745 | 0.0862 | 0.2605 | 1146 |
| new | own | 4-10 | B_pm | negligible | 0.3412 | 0.1600 | 0.5149 | 1146 |
| new | own | 4-10 | B_pm | unresolved | 0.0419 | 0.0143 | 0.0750 | 1146 |
| new | own | 4-10 | C_pm | dominance_positive | 0.4424 | 0.2103 | 0.6387 | 1146 |
| new | own | 4-10 | C_pm | reversal | 0.1745 | 0.0862 | 0.2605 | 1146 |
| new | own | 4-10 | C_pm | negligible | 0.3412 | 0.1600 | 0.5149 | 1146 |
| new | own | 4-10 | C_pm | unresolved | 0.0419 | 0.0143 | 0.0750 | 1146 |
| new | own | 11-16 | B | dominance_positive | 0.9366 | 0.8860 | 0.9788 | 978 |
| new | own | 11-16 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 978 |
| new | own | 11-16 | B | negligible | 0.0634 | 0.0212 | 0.1140 | 978 |
| new | own | 11-16 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 978 |
| new | own | 11-16 | C | dominance_positive | 0.9366 | 0.8860 | 0.9788 | 978 |
| new | own | 11-16 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 978 |
| new | own | 11-16 | C | negligible | 0.0634 | 0.0212 | 0.1140 | 978 |
| new | own | 11-16 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 978 |
| new | own | 11-16 | B_pm | dominance_positive | 0.9366 | 0.8845 | 0.9788 | 978 |
| new | own | 11-16 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 978 |
| new | own | 11-16 | B_pm | negligible | 0.0593 | 0.0210 | 0.1049 | 978 |
| new | own | 11-16 | B_pm | unresolved | 0.0041 | 0.0000 | 0.0196 | 978 |
| new | own | 11-16 | C_pm | dominance_positive | 0.9366 | 0.8845 | 0.9788 | 978 |
| new | own | 11-16 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 978 |
| new | own | 11-16 | C_pm | negligible | 0.0593 | 0.0210 | 0.1049 | 978 |
| new | own | 11-16 | C_pm | unresolved | 0.0041 | 0.0000 | 0.0196 | 978 |
| new | own | 17-30 | B | dominance_positive | 0.9706 | 0.9397 | 0.9945 | 2277 |
| new | own | 17-30 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 2277 |
| new | own | 17-30 | B | negligible | 0.0294 | 0.0055 | 0.0603 | 2277 |
| new | own | 17-30 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 2277 |
| new | own | 17-30 | C | dominance_positive | 0.9706 | 0.9397 | 0.9945 | 2277 |
| new | own | 17-30 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 2277 |
| new | own | 17-30 | C | negligible | 0.0294 | 0.0055 | 0.0603 | 2277 |
| new | own | 17-30 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 2277 |
| new | own | 17-30 | B_pm | dominance_positive | 0.9649 | 0.9318 | 0.9921 | 2277 |
| new | own | 17-30 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 2277 |
| new | own | 17-30 | B_pm | negligible | 0.0264 | 0.0050 | 0.0539 | 2277 |
| new | own | 17-30 | B_pm | unresolved | 0.0088 | 0.0013 | 0.0176 | 2277 |
| new | own | 17-30 | C_pm | dominance_positive | 0.9649 | 0.9318 | 0.9921 | 2277 |
| new | own | 17-30 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 2277 |
| new | own | 17-30 | C_pm | negligible | 0.0264 | 0.0050 | 0.0539 | 2277 |
| new | own | 17-30 | C_pm | unresolved | 0.0088 | 0.0013 | 0.0176 | 2277 |

## T5_3_reversal_slot

| rule | portfolio | jstar | count | count_argmin_C_hat | count_precision_matched | n_reversals | n_reversals_pm |
|---|---|---|---|---|---|---|---|
| old | actual | 1 | 0 | 0 | 0 | 171 | 123 |
| old | actual | 2 | 0 | 0 | 0 | 171 | 123 |
| old | actual | 3 | 0 | 0 | 0 | 171 | 123 |
| old | actual | 4 | 2 | 2 | 1 | 171 | 123 |
| old | actual | 5 | 2 | 2 | 2 | 171 | 123 |
| old | actual | 6 | 1 | 1 | 1 | 171 | 123 |
| old | actual | 7 | 1 | 1 | 1 | 171 | 123 |
| old | actual | 8 | 0 | 0 | 0 | 171 | 123 |
| old | actual | 9 | 4 | 4 | 4 | 171 | 123 |
| old | actual | 10 | 8 | 8 | 5 | 171 | 123 |
| old | actual | 11 | 5 | 5 | 5 | 171 | 123 |
| old | actual | 12 | 1 | 1 | 1 | 171 | 123 |
| old | actual | 13 | 5 | 5 | 3 | 171 | 123 |
| old | actual | 14 | 2 | 4 | 1 | 171 | 123 |
| old | actual | 15 | 6 | 6 | 3 | 171 | 123 |
| old | actual | 16 | 16 | 17 | 11 | 171 | 123 |
| old | actual | 17 | 9 | 9 | 4 | 171 | 123 |
| old | actual | 18 | 12 | 12 | 9 | 171 | 123 |
| old | actual | 19 | 22 | 20 | 15 | 171 | 123 |
| old | actual | 20 | 11 | 11 | 10 | 171 | 123 |
| old | actual | 21 | 7 | 7 | 7 | 171 | 123 |
| old | actual | 22 | 6 | 6 | 2 | 171 | 123 |
| old | actual | 23 | 7 | 7 | 5 | 171 | 123 |
| old | actual | 24 | 5 | 5 | 4 | 171 | 123 |
| old | actual | 25 | 5 | 5 | 4 | 171 | 123 |
| old | actual | 26 | 5 | 6 | 4 | 171 | 123 |
| old | actual | 27 | 16 | 15 | 11 | 171 | 123 |
| old | actual | 28 | 5 | 5 | 6 | 171 | 123 |
| old | actual | 29 | 7 | 7 | 4 | 171 | 123 |
| old | actual | 30 | 1 | 0 | 0 | 171 | 123 |
| old | own | 1 | 0 | 0 | 0 | 0 | 0 |
| old | own | 2 | 0 | 0 | 0 | 0 | 0 |
| old | own | 3 | 0 | 0 | 0 | 0 | 0 |
| old | own | 4 | 0 | 0 | 0 | 0 | 0 |
| old | own | 5 | 0 | 0 | 0 | 0 | 0 |
| old | own | 6 | 0 | 0 | 0 | 0 | 0 |
| old | own | 7 | 0 | 0 | 0 | 0 | 0 |
| old | own | 8 | 0 | 0 | 0 | 0 | 0 |
| old | own | 9 | 0 | 0 | 0 | 0 | 0 |
| old | own | 10 | 0 | 0 | 0 | 0 | 0 |
| old | own | 11 | 0 | 0 | 0 | 0 | 0 |
| old | own | 12 | 0 | 0 | 0 | 0 | 0 |
| old | own | 13 | 0 | 0 | 0 | 0 | 0 |
| old | own | 14 | 0 | 0 | 0 | 0 | 0 |
| old | own | 15 | 0 | 0 | 0 | 0 | 0 |
| old | own | 16 | 0 | 0 | 0 | 0 | 0 |
| old | own | 17 | 0 | 0 | 0 | 0 | 0 |
| old | own | 18 | 0 | 0 | 0 | 0 | 0 |
| old | own | 19 | 0 | 0 | 0 | 0 | 0 |
| old | own | 20 | 0 | 0 | 0 | 0 | 0 |
| old | own | 21 | 0 | 0 | 0 | 0 | 0 |
| old | own | 22 | 0 | 0 | 0 | 0 | 0 |
| old | own | 23 | 0 | 0 | 0 | 0 | 0 |
| old | own | 24 | 0 | 0 | 0 | 0 | 0 |
| old | own | 25 | 0 | 0 | 0 | 0 | 0 |
| old | own | 26 | 0 | 0 | 0 | 0 | 0 |
| old | own | 27 | 0 | 0 | 0 | 0 | 0 |
| old | own | 28 | 0 | 0 | 0 | 0 | 0 |
| old | own | 29 | 0 | 0 | 0 | 0 | 0 |
| old | own | 30 | 0 | 0 | 0 | 0 | 0 |
| new | actual | 1 | 0 | 0 | 0 | 636 | 518 |
| new | actual | 2 | 0 | 0 | 0 | 636 | 518 |
| new | actual | 3 | 11 | 11 | 10 | 636 | 518 |
| new | actual | 4 | 21 | 20 | 19 | 636 | 518 |
| new | actual | 5 | 2 | 1 | 1 | 636 | 518 |
| new | actual | 6 | 4 | 5 | 0 | 636 | 518 |
| new | actual | 7 | 12 | 12 | 9 | 636 | 518 |
| new | actual | 8 | 45 | 44 | 17 | 636 | 518 |
| new | actual | 9 | 374 | 376 | 327 | 636 | 518 |
| new | actual | 10 | 3 | 3 | 3 | 636 | 518 |
| new | actual | 11 | 1 | 3 | 0 | 636 | 518 |
| new | actual | 12 | 4 | 4 | 4 | 636 | 518 |
| new | actual | 13 | 2 | 0 | 1 | 636 | 518 |
| new | actual | 14 | 2 | 2 | 1 | 636 | 518 |
| new | actual | 15 | 3 | 3 | 3 | 636 | 518 |
| new | actual | 16 | 2 | 2 | 1 | 636 | 518 |
| new | actual | 17 | 6 | 7 | 6 | 636 | 518 |
| new | actual | 18 | 11 | 10 | 8 | 636 | 518 |
| new | actual | 19 | 21 | 21 | 18 | 636 | 518 |
| new | actual | 20 | 15 | 15 | 12 | 636 | 518 |
| new | actual | 21 | 6 | 6 | 5 | 636 | 518 |
| new | actual | 22 | 5 | 6 | 3 | 636 | 518 |
| new | actual | 23 | 11 | 10 | 11 | 636 | 518 |
| new | actual | 24 | 11 | 11 | 9 | 636 | 518 |
| new | actual | 25 | 6 | 6 | 5 | 636 | 518 |
| new | actual | 26 | 8 | 9 | 11 | 636 | 518 |
| new | actual | 27 | 19 | 18 | 12 | 636 | 518 |
| new | actual | 28 | 9 | 9 | 7 | 636 | 518 |
| new | actual | 29 | 11 | 11 | 7 | 636 | 518 |
| new | actual | 30 | 11 | 11 | 8 | 636 | 518 |
| new | own | 1 | 0 | 0 | 0 | 512 | 462 |
| new | own | 2 | 0 | 0 | 0 | 512 | 462 |
| new | own | 3 | 0 | 0 | 0 | 512 | 462 |
| new | own | 4 | 0 | 0 | 0 | 512 | 462 |
| new | own | 5 | 0 | 0 | 0 | 512 | 462 |
| new | own | 6 | 0 | 0 | 0 | 512 | 462 |
| new | own | 7 | 0 | 0 | 0 | 512 | 462 |
| new | own | 8 | 0 | 0 | 0 | 512 | 462 |
| new | own | 9 | 512 | 512 | 462 | 512 | 462 |
| new | own | 10 | 0 | 0 | 0 | 512 | 462 |
| new | own | 11 | 0 | 0 | 0 | 512 | 462 |
| new | own | 12 | 0 | 0 | 0 | 512 | 462 |
| new | own | 13 | 0 | 0 | 0 | 512 | 462 |
| new | own | 14 | 0 | 0 | 0 | 512 | 462 |
| new | own | 15 | 0 | 0 | 0 | 512 | 462 |
| new | own | 16 | 0 | 0 | 0 | 512 | 462 |
| new | own | 17 | 0 | 0 | 0 | 512 | 462 |
| new | own | 18 | 0 | 0 | 0 | 512 | 462 |
| new | own | 19 | 0 | 0 | 0 | 512 | 462 |
| new | own | 20 | 0 | 0 | 0 | 512 | 462 |
| new | own | 21 | 0 | 0 | 0 | 512 | 462 |
| new | own | 22 | 0 | 0 | 0 | 512 | 462 |
| new | own | 23 | 0 | 0 | 0 | 512 | 462 |
| new | own | 24 | 0 | 0 | 0 | 512 | 462 |
| new | own | 25 | 0 | 0 | 0 | 512 | 462 |
| new | own | 26 | 0 | 0 | 0 | 512 | 462 |
| new | own | 27 | 0 | 0 | 0 | 512 | 462 |
| new | own | 28 | 0 | 0 | 0 | 512 | 462 |
| new | own | 29 | 0 | 0 | 0 | 512 | 462 |
| new | own | 30 | 0 | 0 | 0 | 512 | 462 |

## F5_1_profiles

720 rows in `F5_1_profiles.csv`.

## T5_curves_and_T5_6_delta

| rule | portfolio | band | curve | n | mean | q25 | median | q75 | q90 | share_sig_pos | pos_lo99 | pos_hi99 | share_sig_neg | neg_lo99 | neg_hi99 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| old | actual | all | linear | 4896 | 0.0179 | 0.0007 | 0.0115 | 0.0300 | 0.0426 | 0.6716 | 0.5569 | 0.7966 | 0.0161 | 0.0046 | 0.0346 |
| old | actual | all | concave | 4896 | 0.0167 | 0.0006 | 0.0091 | 0.0279 | 0.0396 | 0.6334 | 0.5123 | 0.7676 | 0.0190 | 0.0070 | 0.0379 |
| old | actual | all | convex | 4896 | 0.0162 | 0.0004 | 0.0088 | 0.0279 | 0.0417 | 0.6769 | 0.5832 | 0.7643 | 0.0114 | 0.0042 | 0.0202 |
| old | actual | all | top3_stress | 4896 | 0.0068 | 0.0000 | 0.0008 | 0.0107 | 0.0233 | 0.4181 | 0.3793 | 0.4740 | 0.0020 | 0.0002 | 0.0045 |
| old | actual | 1-3 | linear | 495 | 0.0033 | 0.0017 | 0.0027 | 0.0049 | 0.0073 | 0.4828 | 0.2490 | 0.6974 | 0.0242 | 0.0040 | 0.0501 |
| old | actual | 1-3 | concave | 495 | 0.0020 | 0.0010 | 0.0016 | 0.0029 | 0.0049 | 0.2586 | 0.0806 | 0.4879 | 0.0263 | 0.0041 | 0.0558 |
| old | actual | 1-3 | convex | 495 | 0.0052 | 0.0027 | 0.0043 | 0.0073 | 0.0109 | 0.7455 | 0.6410 | 0.8648 | 0.0202 | 0.0020 | 0.0469 |
| old | actual | 1-3 | top3_stress | 495 | 0.0045 | 0.0003 | 0.0016 | 0.0059 | 0.0127 | 0.3960 | 0.1789 | 0.6032 | 0.0020 | 0.0000 | 0.0127 |
| old | actual | 4-10 | linear | 1146 | 0.0183 | 0.0063 | 0.0142 | 0.0260 | 0.0384 | 0.8656 | 0.7896 | 0.9459 | 0.0140 | 0.0000 | 0.0410 |
| old | actual | 4-10 | concave | 1146 | 0.0139 | 0.0036 | 0.0088 | 0.0173 | 0.0340 | 0.7897 | 0.6441 | 0.9195 | 0.0218 | 0.0041 | 0.0509 |
| old | actual | 4-10 | convex | 1146 | 0.0233 | 0.0098 | 0.0198 | 0.0349 | 0.0453 | 0.8944 | 0.8361 | 0.9583 | 0.0079 | 0.0000 | 0.0228 |
| old | actual | 4-10 | top3_stress | 1146 | 0.0183 | 0.0095 | 0.0178 | 0.0268 | 0.0338 | 0.8752 | 0.7946 | 0.9587 | 0.0017 | 0.0000 | 0.0096 |
| old | actual | 11-16 | linear | 978 | 0.0275 | 0.0061 | 0.0261 | 0.0381 | 0.0532 | 0.7863 | 0.6451 | 0.9075 | 0.0072 | 0.0000 | 0.0244 |
| old | actual | 11-16 | concave | 978 | 0.0226 | 0.0056 | 0.0180 | 0.0283 | 0.0411 | 0.7832 | 0.6383 | 0.9051 | 0.0082 | 0.0000 | 0.0254 |
| old | actual | 11-16 | convex | 978 | 0.0285 | 0.0053 | 0.0294 | 0.0409 | 0.0603 | 0.7761 | 0.6287 | 0.9065 | 0.0061 | 0.0000 | 0.0204 |
| old | actual | 11-16 | top3_stress | 978 | 0.0090 | 0.0014 | 0.0065 | 0.0139 | 0.0220 | 0.7045 | 0.5906 | 0.8337 | 0.0020 | 0.0000 | 0.0108 |
| old | actual | 17-30 | linear | 2277 | 0.0167 | 0.0000 | 0.0103 | 0.0308 | 0.0422 | 0.5657 | 0.3499 | 0.7476 | 0.0193 | 0.0026 | 0.0521 |
| old | actual | 17-30 | concave | 2277 | 0.0187 | 0.0000 | 0.0153 | 0.0325 | 0.0432 | 0.5718 | 0.3556 | 0.7504 | 0.0206 | 0.0022 | 0.0569 |
| old | actual | 17-30 | convex | 2277 | 0.0098 | 0.0000 | 0.0032 | 0.0173 | 0.0300 | 0.5099 | 0.3186 | 0.6557 | 0.0136 | 0.0025 | 0.0289 |
| old | actual | 17-30 | top3_stress | 2277 | 0.0006 | 0.0000 | 0.0000 | 0.0003 | 0.0018 | 0.0698 | 0.0329 | 0.1094 | 0.0022 | 0.0000 | 0.0059 |
| old | own | all | linear | 4896 | 0.0242 | 0.0089 | 0.0234 | 0.0351 | 0.0462 | 0.8915 | 0.8431 | 0.9409 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | concave | 4896 | 0.0212 | 0.0067 | 0.0214 | 0.0318 | 0.0393 | 0.8523 | 0.7967 | 0.9095 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | convex | 4896 | 0.0219 | 0.0065 | 0.0187 | 0.0327 | 0.0447 | 0.8754 | 0.8405 | 0.9106 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | top3_stress | 4896 | 0.0078 | 0.0000 | 0.0026 | 0.0130 | 0.0244 | 0.4922 | 0.4551 | 0.5331 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | linear | 495 | 0.0034 | 0.0018 | 0.0025 | 0.0043 | 0.0063 | 0.4061 | 0.1540 | 0.6862 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | concave | 495 | 0.0018 | 0.0010 | 0.0014 | 0.0023 | 0.0035 | 0.1616 | 0.0139 | 0.3509 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | convex | 495 | 0.0057 | 0.0031 | 0.0043 | 0.0072 | 0.0107 | 0.7818 | 0.6466 | 0.9223 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | top3_stress | 495 | 0.0046 | 0.0003 | 0.0014 | 0.0062 | 0.0129 | 0.4020 | 0.1745 | 0.6437 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | linear | 1146 | 0.0162 | 0.0070 | 0.0123 | 0.0236 | 0.0325 | 0.9145 | 0.8322 | 0.9885 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | concave | 1146 | 0.0095 | 0.0039 | 0.0070 | 0.0138 | 0.0194 | 0.8351 | 0.6890 | 0.9671 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | convex | 1146 | 0.0240 | 0.0114 | 0.0192 | 0.0350 | 0.0460 | 0.9494 | 0.8969 | 0.9923 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | top3_stress | 1146 | 0.0198 | 0.0117 | 0.0193 | 0.0273 | 0.0340 | 0.9511 | 0.8995 | 0.9927 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | linear | 978 | 0.0326 | 0.0224 | 0.0306 | 0.0404 | 0.0545 | 0.9918 | 0.9761 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | concave | 978 | 0.0220 | 0.0147 | 0.0206 | 0.0285 | 0.0362 | 0.9847 | 0.9666 | 0.9978 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | convex | 978 | 0.0373 | 0.0264 | 0.0344 | 0.0447 | 0.0639 | 0.9918 | 0.9761 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | top3_stress | 978 | 0.0114 | 0.0052 | 0.0084 | 0.0163 | 0.0240 | 0.9100 | 0.8313 | 0.9711 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | linear | 2277 | 0.0291 | 0.0179 | 0.0288 | 0.0388 | 0.0489 | 0.9425 | 0.8974 | 0.9852 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | concave | 2277 | 0.0310 | 0.0246 | 0.0307 | 0.0370 | 0.0464 | 0.9543 | 0.9201 | 0.9884 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | convex | 2277 | 0.0177 | 0.0048 | 0.0151 | 0.0271 | 0.0378 | 0.8085 | 0.7622 | 0.8638 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | top3_stress | 2277 | 0.0009 | 0.0000 | 0.0000 | 0.0007 | 0.0029 | 0.1014 | 0.0426 | 0.1753 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | all | linear | 4896 | 0.0157 | 0.0000 | 0.0036 | 0.0279 | 0.0458 | 0.5192 | 0.4009 | 0.6344 | 0.0598 | 0.0169 | 0.1053 |
| new | actual | all | concave | 4896 | 0.0152 | 0.0000 | 0.0039 | 0.0284 | 0.0417 | 0.5259 | 0.4142 | 0.6290 | 0.0411 | 0.0140 | 0.0694 |
| new | actual | all | convex | 4896 | 0.0132 | 0.0000 | 0.0023 | 0.0214 | 0.0440 | 0.4900 | 0.3886 | 0.5964 | 0.0784 | 0.0375 | 0.1188 |
| new | actual | all | top3_stress | 4896 | 0.0042 | 0.0000 | 0.0000 | 0.0069 | 0.0193 | 0.3356 | 0.2632 | 0.4134 | 0.0944 | 0.0513 | 0.1345 |
| new | actual | 1-3 | linear | 495 | -0.0023 | -0.0030 | -0.0004 | 0.0003 | 0.0022 | 0.0768 | 0.0259 | 0.1359 | 0.2747 | 0.0581 | 0.4886 |
| new | actual | 1-3 | concave | 495 | -0.0013 | -0.0016 | -0.0002 | 0.0006 | 0.0043 | 0.1475 | 0.0380 | 0.2935 | 0.1535 | 0.0330 | 0.2774 |
| new | actual | 1-3 | convex | 495 | -0.0038 | -0.0055 | -0.0013 | -0.0001 | 0.0002 | 0.0485 | 0.0081 | 0.0998 | 0.4020 | 0.2104 | 0.5722 |
| new | actual | 1-3 | top3_stress | 495 | -0.0057 | -0.0095 | -0.0028 | -0.0006 | 0.0000 | 0.0081 | 0.0000 | 0.0309 | 0.5232 | 0.2944 | 0.7464 |
| new | actual | 4-10 | linear | 1146 | 0.0040 | 0.0000 | 0.0008 | 0.0064 | 0.0151 | 0.3630 | 0.1702 | 0.5472 | 0.1021 | 0.0311 | 0.2098 |
| new | actual | 4-10 | concave | 1146 | 0.0036 | 0.0000 | 0.0007 | 0.0054 | 0.0137 | 0.3630 | 0.1906 | 0.5257 | 0.0724 | 0.0200 | 0.1536 |
| new | actual | 4-10 | convex | 1146 | 0.0040 | -0.0001 | 0.0004 | 0.0072 | 0.0171 | 0.3621 | 0.1613 | 0.5574 | 0.1414 | 0.0589 | 0.2340 |
| new | actual | 4-10 | top3_stress | 1146 | 0.0017 | -0.0003 | 0.0002 | 0.0050 | 0.0123 | 0.3281 | 0.1280 | 0.5283 | 0.1667 | 0.0839 | 0.2420 |
| new | actual | 11-16 | linear | 978 | 0.0260 | 0.0006 | 0.0214 | 0.0406 | 0.0549 | 0.7168 | 0.5593 | 0.8722 | 0.0072 | 0.0000 | 0.0219 |
| new | actual | 11-16 | concave | 978 | 0.0204 | 0.0004 | 0.0157 | 0.0290 | 0.0419 | 0.7045 | 0.5407 | 0.8636 | 0.0051 | 0.0000 | 0.0192 |
| new | actual | 11-16 | convex | 978 | 0.0288 | 0.0005 | 0.0247 | 0.0456 | 0.0613 | 0.7096 | 0.5361 | 0.8724 | 0.0072 | 0.0000 | 0.0244 |
| new | actual | 11-16 | top3_stress | 978 | 0.0142 | 0.0000 | 0.0128 | 0.0218 | 0.0305 | 0.6943 | 0.5265 | 0.8556 | 0.0072 | 0.0000 | 0.0306 |
| new | actual | 17-30 | linear | 2277 | 0.0210 | 0.0000 | 0.0159 | 0.0360 | 0.0511 | 0.6091 | 0.4124 | 0.7720 | 0.0145 | 0.0008 | 0.0419 |
| new | actual | 17-30 | concave | 2277 | 0.0223 | 0.0000 | 0.0216 | 0.0356 | 0.0512 | 0.6135 | 0.4190 | 0.7741 | 0.0162 | 0.0008 | 0.0464 |
| new | actual | 17-30 | convex | 2277 | 0.0148 | 0.0000 | 0.0048 | 0.0239 | 0.0431 | 0.5560 | 0.3938 | 0.6814 | 0.0070 | 0.0000 | 0.0174 |
| new | actual | 17-30 | top3_stress | 2277 | 0.0034 | 0.0000 | 0.0000 | 0.0029 | 0.0125 | 0.2565 | 0.1921 | 0.3292 | 0.0022 | 0.0000 | 0.0070 |
| new | own | all | linear | 4896 | 0.0231 | 0.0003 | 0.0177 | 0.0387 | 0.0548 | 0.6961 | 0.6391 | 0.7651 | 0.0445 | 0.0151 | 0.0737 |
| new | own | all | concave | 4896 | 0.0206 | 0.0003 | 0.0206 | 0.0341 | 0.0447 | 0.6842 | 0.6292 | 0.7499 | 0.0092 | 0.0011 | 0.0214 |
| new | own | all | convex | 4896 | 0.0203 | 0.0001 | 0.0100 | 0.0339 | 0.0560 | 0.6430 | 0.5812 | 0.7079 | 0.0733 | 0.0351 | 0.1092 |
| new | own | all | top3_stress | 4896 | 0.0063 | 0.0000 | 0.0008 | 0.0117 | 0.0227 | 0.4357 | 0.3731 | 0.5039 | 0.0901 | 0.0456 | 0.1324 |
| new | own | 1-3 | linear | 495 | -0.0017 | -0.0028 | -0.0008 | -0.0002 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.2384 | 0.0732 | 0.4097 |
| new | own | 1-3 | concave | 495 | -0.0008 | -0.0014 | -0.0004 | -0.0001 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0465 | 0.0042 | 0.1034 |
| new | own | 1-3 | convex | 495 | -0.0031 | -0.0052 | -0.0015 | -0.0003 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.3980 | 0.1905 | 0.6037 |
| new | own | 1-3 | top3_stress | 495 | -0.0056 | -0.0094 | -0.0027 | -0.0006 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.4970 | 0.2540 | 0.7358 |
| new | own | 4-10 | linear | 1146 | 0.0036 | -0.0000 | 0.0002 | 0.0052 | 0.0127 | 0.3237 | 0.1352 | 0.5144 | 0.0873 | 0.0323 | 0.1441 |
| new | own | 4-10 | concave | 1146 | 0.0023 | -0.0000 | 0.0001 | 0.0032 | 0.0078 | 0.2670 | 0.0979 | 0.4501 | 0.0192 | 0.0017 | 0.0481 |
| new | own | 4-10 | convex | 1146 | 0.0046 | -0.0000 | 0.0002 | 0.0075 | 0.0177 | 0.3569 | 0.1538 | 0.5497 | 0.1414 | 0.0647 | 0.2140 |
| new | own | 4-10 | top3_stress | 1146 | 0.0022 | -0.0001 | 0.0002 | 0.0065 | 0.0136 | 0.3464 | 0.1501 | 0.5361 | 0.1702 | 0.0819 | 0.2534 |
| new | own | 11-16 | linear | 978 | 0.0335 | 0.0133 | 0.0313 | 0.0459 | 0.0624 | 0.9121 | 0.8488 | 0.9679 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | concave | 978 | 0.0221 | 0.0084 | 0.0205 | 0.0313 | 0.0415 | 0.8906 | 0.8179 | 0.9582 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | convex | 978 | 0.0406 | 0.0172 | 0.0377 | 0.0543 | 0.0748 | 0.9192 | 0.8588 | 0.9700 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | top3_stress | 978 | 0.0198 | 0.0106 | 0.0177 | 0.0256 | 0.0358 | 0.9070 | 0.8397 | 0.9639 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | linear | 2277 | 0.0339 | 0.0175 | 0.0308 | 0.0455 | 0.0609 | 0.9420 | 0.8974 | 0.9840 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | concave | 2277 | 0.0339 | 0.0255 | 0.0328 | 0.0414 | 0.0516 | 0.9543 | 0.9201 | 0.9884 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | convex | 2277 | 0.0246 | 0.0048 | 0.0162 | 0.0374 | 0.0586 | 0.8081 | 0.7622 | 0.8627 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | top3_stress | 2277 | 0.0053 | 0.0000 | 0.0004 | 0.0068 | 0.0178 | 0.3729 | 0.3141 | 0.4309 | 0.0000 | 0.0000 | 0.0000 |
| delta | actual | all | linear | 4896 | -0.0022 | -0.0069 | 0.0000 | 0.0008 | 0.0102 | 0.2108 | 0.1626 | 0.2654 | 0.3368 | 0.2664 | 0.3877 |
| delta | actual | all | concave | 4896 | -0.0015 | -0.0044 | 0.0000 | 0.0009 | 0.0074 | 0.1959 | 0.1586 | 0.2483 | 0.3029 | 0.2191 | 0.3734 |
| delta | actual | all | convex | 4896 | -0.0030 | -0.0105 | 0.0000 | 0.0012 | 0.0130 | 0.2267 | 0.1757 | 0.2828 | 0.3640 | 0.3277 | 0.3949 |
| delta | actual | all | top3_stress | 4896 | -0.0026 | -0.0072 | 0.0000 | 0.0011 | 0.0100 | 0.2190 | 0.1732 | 0.2668 | 0.2943 | 0.2612 | 0.3310 |
| delta | actual | 1-3 | linear | 495 | -0.0056 | -0.0077 | -0.0027 | -0.0014 | -0.0004 | 0.0182 | 0.0000 | 0.0549 | 0.5111 | 0.2149 | 0.7712 |
| delta | actual | 1-3 | concave | 495 | -0.0033 | -0.0044 | -0.0015 | -0.0005 | 0.0013 | 0.0606 | 0.0000 | 0.1716 | 0.3717 | 0.0823 | 0.6218 |
| delta | actual | 1-3 | convex | 495 | -0.0090 | -0.0131 | -0.0053 | -0.0027 | -0.0011 | 0.0040 | 0.0000 | 0.0164 | 0.7697 | 0.6431 | 0.8942 |
| delta | actual | 1-3 | top3_stress | 495 | -0.0102 | -0.0158 | -0.0043 | -0.0009 | -0.0000 | 0.0020 | 0.0000 | 0.0125 | 0.5535 | 0.2884 | 0.7860 |
| delta | actual | 4-10 | linear | 1146 | -0.0143 | -0.0206 | -0.0118 | -0.0057 | -0.0006 | 0.0148 | 0.0000 | 0.0469 | 0.8386 | 0.7204 | 0.9409 |
| delta | actual | 4-10 | concave | 1146 | -0.0103 | -0.0129 | -0.0069 | -0.0033 | 0.0000 | 0.0358 | 0.0000 | 0.0939 | 0.7696 | 0.5895 | 0.9201 |
| delta | actual | 4-10 | convex | 1146 | -0.0192 | -0.0277 | -0.0181 | -0.0100 | -0.0011 | 0.0096 | 0.0000 | 0.0298 | 0.8874 | 0.8301 | 0.9543 |
| delta | actual | 4-10 | top3_stress | 1146 | -0.0166 | -0.0227 | -0.0156 | -0.0094 | -0.0007 | 0.0061 | 0.0000 | 0.0236 | 0.8647 | 0.7775 | 0.9523 |
| delta | actual | 11-16 | linear | 978 | -0.0016 | -0.0091 | 0.0000 | 0.0061 | 0.0152 | 0.3425 | 0.2154 | 0.4711 | 0.3763 | 0.2508 | 0.5215 |
| delta | actual | 11-16 | concave | 978 | -0.0022 | -0.0067 | 0.0000 | 0.0036 | 0.0110 | 0.2914 | 0.1853 | 0.4013 | 0.3558 | 0.2077 | 0.5132 |
| delta | actual | 11-16 | convex | 978 | 0.0003 | -0.0083 | 0.0000 | 0.0090 | 0.0202 | 0.3926 | 0.2673 | 0.5219 | 0.3487 | 0.2473 | 0.4695 |
| delta | actual | 11-16 | top3_stress | 978 | 0.0053 | 0.0000 | 0.0026 | 0.0107 | 0.0177 | 0.5041 | 0.3860 | 0.6089 | 0.1748 | 0.1049 | 0.2358 |
| delta | actual | 17-30 | linear | 2277 | 0.0044 | 0.0000 | 0.0000 | 0.0041 | 0.0154 | 0.2947 | 0.2230 | 0.3751 | 0.0294 | 0.0111 | 0.0505 |
| delta | actual | 17-30 | concave | 2277 | 0.0036 | 0.0000 | 0.0000 | 0.0028 | 0.0128 | 0.2648 | 0.1958 | 0.3360 | 0.0303 | 0.0117 | 0.0543 |
| delta | actual | 17-30 | convex | 2277 | 0.0050 | 0.0000 | 0.0000 | 0.0055 | 0.0178 | 0.3131 | 0.2358 | 0.3990 | 0.0189 | 0.0071 | 0.0321 |
| delta | actual | 17-30 | top3_stress | 2277 | 0.0028 | 0.0000 | 0.0000 | 0.0026 | 0.0098 | 0.2508 | 0.1890 | 0.3210 | 0.0022 | 0.0000 | 0.0065 |
| delta | own | all | linear | 4896 | -0.0010 | -0.0078 | -0.0000 | 0.0034 | 0.0131 | 0.2729 | 0.2424 | 0.3004 | 0.3770 | 0.3377 | 0.4096 |
| delta | own | all | concave | 4896 | -0.0006 | -0.0045 | -0.0000 | 0.0018 | 0.0077 | 0.2312 | 0.2069 | 0.2550 | 0.3258 | 0.2778 | 0.3617 |
| delta | own | all | convex | 4896 | -0.0016 | -0.0118 | 0.0000 | 0.0055 | 0.0189 | 0.2980 | 0.2668 | 0.3282 | 0.3975 | 0.3690 | 0.4225 |
| delta | own | all | top3_stress | 4896 | -0.0015 | -0.0090 | 0.0000 | 0.0051 | 0.0147 | 0.3068 | 0.2645 | 0.3453 | 0.3160 | 0.2772 | 0.3560 |
| delta | own | 1-3 | linear | 495 | -0.0050 | -0.0069 | -0.0034 | -0.0020 | -0.0014 | 0.0000 | 0.0000 | 0.0000 | 0.5636 | 0.3041 | 0.8138 |
| delta | own | 1-3 | concave | 495 | -0.0027 | -0.0036 | -0.0018 | -0.0011 | -0.0008 | 0.0000 | 0.0000 | 0.0000 | 0.3152 | 0.1002 | 0.5478 |
| delta | own | 1-3 | convex | 495 | -0.0088 | -0.0122 | -0.0058 | -0.0035 | -0.0024 | 0.0000 | 0.0000 | 0.0000 | 0.8444 | 0.7343 | 0.9422 |
| delta | own | 1-3 | top3_stress | 495 | -0.0102 | -0.0157 | -0.0042 | -0.0009 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.5697 | 0.2956 | 0.8132 |
| delta | own | 4-10 | linear | 1146 | -0.0126 | -0.0179 | -0.0114 | -0.0072 | -0.0040 | 0.0009 | 0.0000 | 0.0055 | 0.9311 | 0.8701 | 0.9887 |
| delta | own | 4-10 | concave | 1146 | -0.0072 | -0.0104 | -0.0063 | -0.0041 | -0.0022 | 0.0000 | 0.0000 | 0.0000 | 0.8647 | 0.7396 | 0.9741 |
| delta | own | 4-10 | convex | 1146 | -0.0194 | -0.0270 | -0.0184 | -0.0115 | -0.0064 | 0.0009 | 0.0000 | 0.0055 | 0.9485 | 0.8978 | 0.9902 |
| delta | own | 4-10 | top3_stress | 1146 | -0.0176 | -0.0230 | -0.0163 | -0.0108 | -0.0055 | 0.0105 | 0.0000 | 0.0291 | 0.9354 | 0.8803 | 0.9785 |
| delta | own | 11-16 | linear | 978 | 0.0009 | -0.0099 | 0.0009 | 0.0089 | 0.0174 | 0.4734 | 0.3627 | 0.5890 | 0.4254 | 0.2934 | 0.5455 |
| delta | own | 11-16 | concave | 978 | 0.0001 | -0.0065 | 0.0002 | 0.0048 | 0.0102 | 0.3804 | 0.2781 | 0.4933 | 0.3906 | 0.2482 | 0.5194 |
| delta | own | 11-16 | convex | 978 | 0.0033 | -0.0121 | 0.0033 | 0.0148 | 0.0275 | 0.5368 | 0.4202 | 0.6556 | 0.3947 | 0.2749 | 0.4995 |
| delta | own | 11-16 | top3_stress | 978 | 0.0083 | -0.0001 | 0.0079 | 0.0153 | 0.0234 | 0.6779 | 0.5794 | 0.7737 | 0.1973 | 0.0926 | 0.2899 |
| delta | own | 17-30 | linear | 2277 | 0.0048 | 0.0000 | 0.0002 | 0.0077 | 0.0158 | 0.3830 | 0.3406 | 0.4220 | 0.0369 | 0.0112 | 0.0751 |
| delta | own | 17-30 | concave | 2277 | 0.0029 | 0.0000 | 0.0001 | 0.0047 | 0.0096 | 0.3338 | 0.2881 | 0.3721 | 0.0290 | 0.0111 | 0.0504 |
| delta | own | 17-30 | convex | 2277 | 0.0069 | 0.0000 | 0.0003 | 0.0104 | 0.0223 | 0.4097 | 0.3625 | 0.4532 | 0.0242 | 0.0057 | 0.0467 |
| delta | own | 17-30 | top3_stress | 2277 | 0.0044 | 0.0000 | 0.0004 | 0.0060 | 0.0144 | 0.3632 | 0.3027 | 0.4229 | 0.0000 | 0.0000 | 0.0000 |

## H1

| n_team_games | share_neg_new | share_neg_old | diff_new_minus_old | diff_lo99 | diff_hi99 | n_new_reversals | crossing_share | crossing_lo99 | crossing_hi99 | supported |
|---|---|---|---|---|---|---|---|---|---|---|
| 649 | 0.3159 | 0.0000 | 0.3159 | 0.1139 | 0.5158 | 439 | 1.0000 | 1.0000 | 1.0000 | True |

## T5_attr_portfolio_effect

| rule | band | n | mean | q25 | median | q75 | q90 | share_nonzero |
|---|---|---|---|---|---|---|---|---|
| old | all | 4896 | -0.0063 | -0.0133 | 0.0000 | 0.0000 | 0.0022 | 0.4277 |
| old | 1-3 | 495 | -0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.0014 | 0.0970 |
| old | 4-10 | 1146 | 0.0021 | -0.0000 | 0.0000 | 0.0017 | 0.0123 | 0.3307 |
| old | 11-16 | 978 | -0.0051 | -0.0196 | 0.0000 | 0.0000 | 0.0054 | 0.4806 |
| old | 17-30 | 2277 | -0.0124 | -0.0241 | -0.0032 | 0.0000 | 0.0000 | 0.5257 |
| new | all | 4896 | -0.0075 | -0.0110 | 0.0000 | 0.0000 | 0.0029 | 0.4365 |
| new | 1-3 | 495 | -0.0006 | -0.0001 | 0.0000 | 0.0008 | 0.0043 | 0.2444 |
| new | 4-10 | 1146 | 0.0004 | 0.0000 | 0.0000 | 0.0009 | 0.0051 | 0.2740 |
| new | 11-16 | 978 | -0.0076 | -0.0115 | 0.0000 | 0.0000 | 0.0058 | 0.4571 |
| new | 17-30 | 2277 | -0.0129 | -0.0219 | -0.0036 | 0.0000 | 0.0000 | 0.5512 |
| delta | all | 4896 | -0.0012 | -0.0002 | 0.0000 | 0.0001 | 0.0047 | 0.2902 |
| delta | 1-3 | 495 | -0.0005 | -0.0001 | 0.0000 | 0.0006 | 0.0034 | 0.2101 |
| delta | 4-10 | 1146 | -0.0017 | -0.0006 | 0.0000 | 0.0001 | 0.0053 | 0.3054 |
| delta | 11-16 | 978 | -0.0025 | -0.0029 | 0.0000 | 0.0000 | 0.0086 | 0.3998 |
| delta | 17-30 | 2277 | -0.0005 | -0.0000 | 0.0000 | 0.0000 | 0.0043 | 0.2530 |

## T5_7_rollover

| rule | portfolio | band | curve | rho | measure | n | mean | q25 | median | q75 | q90 | share_sign_flip | vbar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| old | actual | all | - | 0.0000 | M | 4896 | 0.0062 | -0.0000 | 0.0000 | 0.0000 | 0.0120 |  |  |
| old | actual | all | linear | 0.0000 | tau | 4896 | 0.0179 | 0.0007 | 0.0115 | 0.0300 | 0.0426 | 0.0000 | 0.5000 |
| old | actual | all | linear | 0.5000 | tau | 4896 | 0.0163 | 0.0006 | 0.0105 | 0.0283 | 0.0401 | 0.0018 | 0.5000 |
| old | actual | all | linear | 0.8000 | tau | 4896 | 0.0154 | 0.0005 | 0.0096 | 0.0270 | 0.0391 | 0.0039 | 0.5000 |
| old | actual | all | concave | 0.0000 | tau | 4896 | 0.0167 | 0.0006 | 0.0091 | 0.0279 | 0.0396 | 0.0000 | 0.6599 |
| old | actual | all | concave | 0.5000 | tau | 4896 | 0.0146 | 0.0006 | 0.0081 | 0.0261 | 0.0361 | 0.0045 | 0.6599 |
| old | actual | all | concave | 0.8000 | tau | 4896 | 0.0134 | 0.0005 | 0.0072 | 0.0244 | 0.0347 | 0.0067 | 0.6599 |
| old | actual | all | convex | 0.0000 | tau | 4896 | 0.0162 | 0.0004 | 0.0088 | 0.0279 | 0.0417 | 0.0000 | 0.3391 |
| old | actual | all | convex | 0.5000 | tau | 4896 | 0.0152 | 0.0004 | 0.0082 | 0.0266 | 0.0398 | 0.0016 | 0.3391 |
| old | actual | all | convex | 0.8000 | tau | 4896 | 0.0146 | 0.0003 | 0.0078 | 0.0255 | 0.0389 | 0.0059 | 0.3391 |
| old | actual | all | top3_stress | 0.0000 | tau | 4896 | 0.0068 | 0.0000 | 0.0008 | 0.0107 | 0.0233 | 0.0000 | 0.1000 |
| old | actual | all | top3_stress | 0.5000 | tau | 4896 | 0.0065 | 0.0000 | 0.0006 | 0.0102 | 0.0227 | 0.1048 | 0.1000 |
| old | actual | all | top3_stress | 0.8000 | tau | 4896 | 0.0063 | 0.0000 | 0.0005 | 0.0100 | 0.0226 | 0.1121 | 0.1000 |
| old | actual | 1-3 | - | 0.0000 | M | 495 | 0.0007 | -0.0000 | 0.0000 | 0.0000 | 0.0005 |  |  |
| old | actual | 1-3 | linear | 0.0000 | tau | 495 | 0.0033 | 0.0017 | 0.0027 | 0.0049 | 0.0073 | 0.0000 | 0.5000 |
| old | actual | 1-3 | linear | 0.5000 | tau | 495 | 0.0031 | 0.0017 | 0.0027 | 0.0048 | 0.0072 | 0.0020 | 0.5000 |
| old | actual | 1-3 | linear | 0.8000 | tau | 495 | 0.0030 | 0.0017 | 0.0027 | 0.0048 | 0.0071 | 0.0020 | 0.5000 |
| old | actual | 1-3 | concave | 0.0000 | tau | 495 | 0.0020 | 0.0010 | 0.0016 | 0.0029 | 0.0049 | 0.0000 | 0.6599 |
| old | actual | 1-3 | concave | 0.5000 | tau | 495 | 0.0018 | 0.0010 | 0.0016 | 0.0028 | 0.0045 | 0.0061 | 0.6599 |
| old | actual | 1-3 | concave | 0.8000 | tau | 495 | 0.0017 | 0.0010 | 0.0015 | 0.0027 | 0.0044 | 0.0101 | 0.6599 |
| old | actual | 1-3 | convex | 0.0000 | tau | 495 | 0.0052 | 0.0027 | 0.0043 | 0.0073 | 0.0109 | 0.0000 | 0.3391 |
| old | actual | 1-3 | convex | 0.5000 | tau | 495 | 0.0051 | 0.0026 | 0.0043 | 0.0073 | 0.0105 | 0.0000 | 0.3391 |
| old | actual | 1-3 | convex | 0.8000 | tau | 495 | 0.0050 | 0.0026 | 0.0043 | 0.0073 | 0.0105 | 0.0020 | 0.3391 |
| old | actual | 1-3 | top3_stress | 0.0000 | tau | 495 | 0.0045 | 0.0003 | 0.0016 | 0.0059 | 0.0127 | 0.0000 | 0.1000 |
| old | actual | 1-3 | top3_stress | 0.5000 | tau | 495 | 0.0045 | 0.0003 | 0.0016 | 0.0059 | 0.0127 | 0.0061 | 0.1000 |
| old | actual | 1-3 | top3_stress | 0.8000 | tau | 495 | 0.0045 | 0.0003 | 0.0016 | 0.0059 | 0.0127 | 0.0061 | 0.1000 |
| old | actual | 4-10 | - | 0.0000 | M | 1146 | 0.0077 | -0.0000 | 0.0000 | 0.0011 | 0.0314 |  |  |
| old | actual | 4-10 | linear | 0.0000 | tau | 1146 | 0.0183 | 0.0063 | 0.0142 | 0.0260 | 0.0384 | 0.0000 | 0.5000 |
| old | actual | 4-10 | linear | 0.5000 | tau | 1146 | 0.0164 | 0.0062 | 0.0133 | 0.0245 | 0.0328 | 0.0035 | 0.5000 |
| old | actual | 4-10 | linear | 0.8000 | tau | 1146 | 0.0152 | 0.0062 | 0.0127 | 0.0229 | 0.0309 | 0.0070 | 0.5000 |
| old | actual | 4-10 | concave | 0.0000 | tau | 1146 | 0.0139 | 0.0036 | 0.0088 | 0.0173 | 0.0340 | 0.0000 | 0.6599 |
| old | actual | 4-10 | concave | 0.5000 | tau | 1146 | 0.0114 | 0.0036 | 0.0083 | 0.0159 | 0.0255 | 0.0079 | 0.6599 |
| old | actual | 4-10 | concave | 0.8000 | tau | 1146 | 0.0098 | 0.0036 | 0.0079 | 0.0147 | 0.0206 | 0.0140 | 0.6599 |
| old | actual | 4-10 | convex | 0.0000 | tau | 1146 | 0.0233 | 0.0098 | 0.0198 | 0.0349 | 0.0453 | 0.0000 | 0.3391 |
| old | actual | 4-10 | convex | 0.5000 | tau | 1146 | 0.0220 | 0.0098 | 0.0188 | 0.0323 | 0.0437 | 0.0017 | 0.3391 |
| old | actual | 4-10 | convex | 0.8000 | tau | 1146 | 0.0212 | 0.0095 | 0.0180 | 0.0312 | 0.0428 | 0.0035 | 0.3391 |
| old | actual | 4-10 | top3_stress | 0.0000 | tau | 1146 | 0.0183 | 0.0095 | 0.0178 | 0.0268 | 0.0338 | 0.0000 | 0.1000 |
| old | actual | 4-10 | top3_stress | 0.5000 | tau | 1146 | 0.0179 | 0.0093 | 0.0177 | 0.0263 | 0.0331 | 0.0035 | 0.1000 |
| old | actual | 4-10 | top3_stress | 0.8000 | tau | 1146 | 0.0177 | 0.0090 | 0.0173 | 0.0259 | 0.0329 | 0.0052 | 0.1000 |
| old | actual | 11-16 | - | 0.0000 | M | 978 | 0.0115 | -0.0000 | 0.0000 | 0.0012 | 0.0344 |  |  |
| old | actual | 11-16 | linear | 0.0000 | tau | 978 | 0.0275 | 0.0061 | 0.0261 | 0.0381 | 0.0532 | 0.0000 | 0.5000 |
| old | actual | 11-16 | linear | 0.5000 | tau | 978 | 0.0246 | 0.0045 | 0.0255 | 0.0368 | 0.0501 | 0.0010 | 0.5000 |
| old | actual | 11-16 | linear | 0.8000 | tau | 978 | 0.0229 | 0.0036 | 0.0240 | 0.0362 | 0.0477 | 0.0031 | 0.5000 |
| old | actual | 11-16 | concave | 0.0000 | tau | 978 | 0.0226 | 0.0056 | 0.0180 | 0.0283 | 0.0411 | 0.0000 | 0.6599 |
| old | actual | 11-16 | concave | 0.5000 | tau | 978 | 0.0188 | 0.0043 | 0.0173 | 0.0268 | 0.0357 | 0.0031 | 0.6599 |
| old | actual | 11-16 | concave | 0.8000 | tau | 978 | 0.0165 | 0.0031 | 0.0164 | 0.0256 | 0.0335 | 0.0041 | 0.6599 |
| old | actual | 11-16 | convex | 0.0000 | tau | 978 | 0.0285 | 0.0053 | 0.0294 | 0.0409 | 0.0603 | 0.0000 | 0.3391 |
| old | actual | 11-16 | convex | 0.5000 | tau | 978 | 0.0265 | 0.0043 | 0.0278 | 0.0398 | 0.0570 | 0.0051 | 0.3391 |
| old | actual | 11-16 | convex | 0.8000 | tau | 978 | 0.0253 | 0.0036 | 0.0264 | 0.0391 | 0.0541 | 0.0123 | 0.3391 |
| old | actual | 11-16 | top3_stress | 0.0000 | tau | 978 | 0.0090 | 0.0014 | 0.0065 | 0.0139 | 0.0220 | 0.0000 | 0.1000 |
| old | actual | 11-16 | top3_stress | 0.5000 | tau | 978 | 0.0084 | 0.0010 | 0.0059 | 0.0133 | 0.0211 | 0.0348 | 0.1000 |
| old | actual | 11-16 | top3_stress | 0.8000 | tau | 978 | 0.0081 | 0.0001 | 0.0056 | 0.0129 | 0.0211 | 0.0573 | 0.1000 |
| old | actual | 17-30 | - | 0.0000 | M | 2277 | 0.0042 | -0.0000 | 0.0000 | 0.0000 | 0.0024 |  |  |
| old | actual | 17-30 | linear | 0.0000 | tau | 2277 | 0.0167 | 0.0000 | 0.0103 | 0.0308 | 0.0422 | 0.0000 | 0.5000 |
| old | actual | 17-30 | linear | 0.5000 | tau | 2277 | 0.0156 | 0.0000 | 0.0080 | 0.0292 | 0.0408 | 0.0013 | 0.5000 |
| old | actual | 17-30 | linear | 0.8000 | tau | 2277 | 0.0150 | 0.0000 | 0.0064 | 0.0286 | 0.0401 | 0.0031 | 0.5000 |
| old | actual | 17-30 | concave | 0.0000 | tau | 2277 | 0.0187 | 0.0000 | 0.0153 | 0.0325 | 0.0432 | 0.0000 | 0.6599 |
| old | actual | 17-30 | concave | 0.5000 | tau | 2277 | 0.0173 | 0.0000 | 0.0121 | 0.0317 | 0.0412 | 0.0031 | 0.6599 |
| old | actual | 17-30 | concave | 0.8000 | tau | 2277 | 0.0164 | 0.0000 | 0.0090 | 0.0312 | 0.0400 | 0.0035 | 0.6599 |
| old | actual | 17-30 | convex | 0.0000 | tau | 2277 | 0.0098 | 0.0000 | 0.0032 | 0.0173 | 0.0300 | 0.0000 | 0.3391 |
| old | actual | 17-30 | convex | 0.5000 | tau | 2277 | 0.0091 | 0.0000 | 0.0029 | 0.0157 | 0.0287 | 0.0004 | 0.3391 |
| old | actual | 17-30 | convex | 0.8000 | tau | 2277 | 0.0087 | 0.0000 | 0.0022 | 0.0147 | 0.0283 | 0.0053 | 0.3391 |
| old | actual | 17-30 | top3_stress | 0.0000 | tau | 2277 | 0.0006 | 0.0000 | 0.0000 | 0.0003 | 0.0018 | 0.0000 | 0.1000 |
| old | actual | 17-30 | top3_stress | 0.5000 | tau | 2277 | 0.0004 | 0.0000 | 0.0000 | 0.0001 | 0.0013 | 0.2073 | 0.1000 |
| old | actual | 17-30 | top3_stress | 0.8000 | tau | 2277 | 0.0003 | 0.0000 | 0.0000 | 0.0001 | 0.0013 | 0.2126 | 0.1000 |
| old | own | all | - | 0.0000 | M | 4896 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | all | linear | 0.0000 | tau | 4896 | 0.0242 | 0.0089 | 0.0234 | 0.0351 | 0.0462 | 0.0000 | 0.5000 |
| old | own | all | linear | 0.5000 | tau | 4896 | 0.0242 | 0.0089 | 0.0234 | 0.0351 | 0.0462 | 0.0000 | 0.5000 |
| old | own | all | linear | 0.8000 | tau | 4896 | 0.0242 | 0.0089 | 0.0234 | 0.0351 | 0.0462 | 0.0000 | 0.5000 |
| old | own | all | concave | 0.0000 | tau | 4896 | 0.0212 | 0.0067 | 0.0214 | 0.0318 | 0.0393 | 0.0000 | 0.6599 |
| old | own | all | concave | 0.5000 | tau | 4896 | 0.0212 | 0.0067 | 0.0214 | 0.0318 | 0.0393 | 0.0000 | 0.6599 |
| old | own | all | concave | 0.8000 | tau | 4896 | 0.0212 | 0.0067 | 0.0214 | 0.0318 | 0.0393 | 0.0000 | 0.6599 |
| old | own | all | convex | 0.0000 | tau | 4896 | 0.0219 | 0.0065 | 0.0187 | 0.0327 | 0.0447 | 0.0000 | 0.3391 |
| old | own | all | convex | 0.5000 | tau | 4896 | 0.0219 | 0.0065 | 0.0187 | 0.0327 | 0.0447 | 0.0000 | 0.3391 |
| old | own | all | convex | 0.8000 | tau | 4896 | 0.0219 | 0.0065 | 0.0187 | 0.0327 | 0.0447 | 0.0000 | 0.3391 |
| old | own | all | top3_stress | 0.0000 | tau | 4896 | 0.0078 | 0.0000 | 0.0026 | 0.0130 | 0.0244 | 0.0000 | 0.1000 |
| old | own | all | top3_stress | 0.5000 | tau | 4896 | 0.0078 | 0.0000 | 0.0026 | 0.0130 | 0.0244 | 0.0727 | 0.1000 |
| old | own | all | top3_stress | 0.8000 | tau | 4896 | 0.0078 | 0.0000 | 0.0026 | 0.0130 | 0.0244 | 0.0731 | 0.1000 |
| old | own | 1-3 | - | 0.0000 | M | 495 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 1-3 | linear | 0.0000 | tau | 495 | 0.0034 | 0.0018 | 0.0025 | 0.0043 | 0.0063 | 0.0000 | 0.5000 |
| old | own | 1-3 | linear | 0.5000 | tau | 495 | 0.0034 | 0.0018 | 0.0025 | 0.0043 | 0.0063 | 0.0000 | 0.5000 |
| old | own | 1-3 | linear | 0.8000 | tau | 495 | 0.0034 | 0.0018 | 0.0025 | 0.0043 | 0.0063 | 0.0000 | 0.5000 |
| old | own | 1-3 | concave | 0.0000 | tau | 495 | 0.0018 | 0.0010 | 0.0014 | 0.0023 | 0.0035 | 0.0000 | 0.6599 |
| old | own | 1-3 | concave | 0.5000 | tau | 495 | 0.0018 | 0.0010 | 0.0014 | 0.0023 | 0.0035 | 0.0000 | 0.6599 |
| old | own | 1-3 | concave | 0.8000 | tau | 495 | 0.0018 | 0.0010 | 0.0014 | 0.0023 | 0.0035 | 0.0000 | 0.6599 |
| old | own | 1-3 | convex | 0.0000 | tau | 495 | 0.0057 | 0.0031 | 0.0043 | 0.0072 | 0.0107 | 0.0000 | 0.3391 |
| old | own | 1-3 | convex | 0.5000 | tau | 495 | 0.0057 | 0.0031 | 0.0043 | 0.0072 | 0.0107 | 0.0000 | 0.3391 |
| old | own | 1-3 | convex | 0.8000 | tau | 495 | 0.0057 | 0.0031 | 0.0043 | 0.0072 | 0.0107 | 0.0000 | 0.3391 |
| old | own | 1-3 | top3_stress | 0.0000 | tau | 495 | 0.0046 | 0.0003 | 0.0014 | 0.0062 | 0.0129 | 0.0000 | 0.1000 |
| old | own | 1-3 | top3_stress | 0.5000 | tau | 495 | 0.0046 | 0.0003 | 0.0014 | 0.0062 | 0.0129 | 0.0040 | 0.1000 |
| old | own | 1-3 | top3_stress | 0.8000 | tau | 495 | 0.0046 | 0.0003 | 0.0014 | 0.0062 | 0.0129 | 0.0040 | 0.1000 |
| old | own | 4-10 | - | 0.0000 | M | 1146 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 4-10 | linear | 0.0000 | tau | 1146 | 0.0162 | 0.0070 | 0.0123 | 0.0236 | 0.0325 | 0.0000 | 0.5000 |
| old | own | 4-10 | linear | 0.5000 | tau | 1146 | 0.0162 | 0.0070 | 0.0123 | 0.0236 | 0.0325 | 0.0000 | 0.5000 |
| old | own | 4-10 | linear | 0.8000 | tau | 1146 | 0.0162 | 0.0070 | 0.0123 | 0.0236 | 0.0325 | 0.0000 | 0.5000 |
| old | own | 4-10 | concave | 0.0000 | tau | 1146 | 0.0095 | 0.0039 | 0.0070 | 0.0138 | 0.0194 | 0.0000 | 0.6599 |
| old | own | 4-10 | concave | 0.5000 | tau | 1146 | 0.0095 | 0.0039 | 0.0070 | 0.0138 | 0.0194 | 0.0000 | 0.6599 |
| old | own | 4-10 | concave | 0.8000 | tau | 1146 | 0.0095 | 0.0039 | 0.0070 | 0.0138 | 0.0194 | 0.0000 | 0.6599 |
| old | own | 4-10 | convex | 0.0000 | tau | 1146 | 0.0240 | 0.0114 | 0.0192 | 0.0350 | 0.0460 | 0.0000 | 0.3391 |
| old | own | 4-10 | convex | 0.5000 | tau | 1146 | 0.0240 | 0.0114 | 0.0192 | 0.0350 | 0.0460 | 0.0000 | 0.3391 |
| old | own | 4-10 | convex | 0.8000 | tau | 1146 | 0.0240 | 0.0114 | 0.0192 | 0.0350 | 0.0460 | 0.0000 | 0.3391 |
| old | own | 4-10 | top3_stress | 0.0000 | tau | 1146 | 0.0198 | 0.0117 | 0.0193 | 0.0273 | 0.0340 | 0.0000 | 0.1000 |
| old | own | 4-10 | top3_stress | 0.5000 | tau | 1146 | 0.0198 | 0.0117 | 0.0193 | 0.0273 | 0.0340 | 0.0000 | 0.1000 |
| old | own | 4-10 | top3_stress | 0.8000 | tau | 1146 | 0.0198 | 0.0117 | 0.0193 | 0.0273 | 0.0340 | 0.0000 | 0.1000 |
| old | own | 11-16 | - | 0.0000 | M | 978 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 11-16 | linear | 0.0000 | tau | 978 | 0.0326 | 0.0224 | 0.0306 | 0.0404 | 0.0545 | 0.0000 | 0.5000 |
| old | own | 11-16 | linear | 0.5000 | tau | 978 | 0.0326 | 0.0224 | 0.0306 | 0.0404 | 0.0545 | 0.0000 | 0.5000 |
| old | own | 11-16 | linear | 0.8000 | tau | 978 | 0.0326 | 0.0224 | 0.0306 | 0.0404 | 0.0545 | 0.0000 | 0.5000 |
| old | own | 11-16 | concave | 0.0000 | tau | 978 | 0.0220 | 0.0147 | 0.0206 | 0.0285 | 0.0362 | 0.0000 | 0.6599 |
| old | own | 11-16 | concave | 0.5000 | tau | 978 | 0.0220 | 0.0147 | 0.0206 | 0.0285 | 0.0362 | 0.0000 | 0.6599 |
| old | own | 11-16 | concave | 0.8000 | tau | 978 | 0.0220 | 0.0147 | 0.0206 | 0.0285 | 0.0362 | 0.0000 | 0.6599 |
| old | own | 11-16 | convex | 0.0000 | tau | 978 | 0.0373 | 0.0264 | 0.0344 | 0.0447 | 0.0639 | 0.0000 | 0.3391 |
| old | own | 11-16 | convex | 0.5000 | tau | 978 | 0.0373 | 0.0264 | 0.0344 | 0.0447 | 0.0639 | 0.0000 | 0.3391 |
| old | own | 11-16 | convex | 0.8000 | tau | 978 | 0.0373 | 0.0264 | 0.0344 | 0.0447 | 0.0639 | 0.0000 | 0.3391 |
| old | own | 11-16 | top3_stress | 0.0000 | tau | 978 | 0.0114 | 0.0052 | 0.0084 | 0.0163 | 0.0240 | 0.0000 | 0.1000 |
| old | own | 11-16 | top3_stress | 0.5000 | tau | 978 | 0.0114 | 0.0052 | 0.0084 | 0.0163 | 0.0240 | 0.0000 | 0.1000 |
| old | own | 11-16 | top3_stress | 0.8000 | tau | 978 | 0.0114 | 0.0052 | 0.0084 | 0.0163 | 0.0240 | 0.0000 | 0.1000 |
| old | own | 17-30 | - | 0.0000 | M | 2277 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 17-30 | linear | 0.0000 | tau | 2277 | 0.0291 | 0.0179 | 0.0288 | 0.0388 | 0.0489 | 0.0000 | 0.5000 |
| old | own | 17-30 | linear | 0.5000 | tau | 2277 | 0.0291 | 0.0179 | 0.0288 | 0.0388 | 0.0489 | 0.0000 | 0.5000 |
| old | own | 17-30 | linear | 0.8000 | tau | 2277 | 0.0291 | 0.0179 | 0.0288 | 0.0388 | 0.0489 | 0.0000 | 0.5000 |
| old | own | 17-30 | concave | 0.0000 | tau | 2277 | 0.0310 | 0.0246 | 0.0307 | 0.0370 | 0.0464 | 0.0000 | 0.6599 |
| old | own | 17-30 | concave | 0.5000 | tau | 2277 | 0.0310 | 0.0246 | 0.0307 | 0.0370 | 0.0464 | 0.0000 | 0.6599 |
| old | own | 17-30 | concave | 0.8000 | tau | 2277 | 0.0310 | 0.0246 | 0.0307 | 0.0370 | 0.0464 | 0.0000 | 0.6599 |
| old | own | 17-30 | convex | 0.0000 | tau | 2277 | 0.0177 | 0.0048 | 0.0151 | 0.0271 | 0.0378 | 0.0000 | 0.3391 |
| old | own | 17-30 | convex | 0.5000 | tau | 2277 | 0.0177 | 0.0048 | 0.0151 | 0.0271 | 0.0378 | 0.0000 | 0.3391 |
| old | own | 17-30 | convex | 0.8000 | tau | 2277 | 0.0177 | 0.0048 | 0.0151 | 0.0271 | 0.0378 | 0.0000 | 0.3391 |
| old | own | 17-30 | top3_stress | 0.0000 | tau | 2277 | 0.0009 | 0.0000 | 0.0000 | 0.0007 | 0.0029 | 0.0000 | 0.1000 |
| old | own | 17-30 | top3_stress | 0.5000 | tau | 2277 | 0.0009 | 0.0000 | 0.0000 | 0.0007 | 0.0029 | 0.1555 | 0.1000 |
| old | own | 17-30 | top3_stress | 0.8000 | tau | 2277 | 0.0009 | 0.0000 | 0.0000 | 0.0007 | 0.0029 | 0.1563 | 0.1000 |
| new | actual | all | - | 0.0000 | M | 4896 | 0.0056 | -0.0000 | 0.0000 | 0.0000 | 0.0121 |  |  |
| new | actual | all | linear | 0.0000 | tau | 4896 | 0.0157 | 0.0000 | 0.0036 | 0.0279 | 0.0458 | 0.0000 | 0.5000 |
| new | actual | all | linear | 0.5000 | tau | 4896 | 0.0143 | 0.0000 | 0.0031 | 0.0262 | 0.0434 | 0.0266 | 0.5000 |
| new | actual | all | linear | 0.8000 | tau | 4896 | 0.0135 | 0.0000 | 0.0028 | 0.0247 | 0.0422 | 0.0317 | 0.5000 |
| new | actual | all | concave | 0.0000 | tau | 4896 | 0.0152 | 0.0000 | 0.0039 | 0.0284 | 0.0417 | 0.0000 | 0.6599 |
| new | actual | all | concave | 0.5000 | tau | 4896 | 0.0133 | 0.0000 | 0.0029 | 0.0268 | 0.0382 | 0.0031 | 0.6599 |
| new | actual | all | concave | 0.8000 | tau | 4896 | 0.0122 | 0.0000 | 0.0022 | 0.0248 | 0.0365 | 0.0082 | 0.6599 |
| new | actual | all | convex | 0.0000 | tau | 4896 | 0.0132 | 0.0000 | 0.0023 | 0.0214 | 0.0440 | 0.0000 | 0.3391 |
| new | actual | all | convex | 0.5000 | tau | 4896 | 0.0123 | 0.0000 | 0.0021 | 0.0199 | 0.0414 | 0.0043 | 0.3391 |
| new | actual | all | convex | 0.8000 | tau | 4896 | 0.0117 | 0.0000 | 0.0020 | 0.0190 | 0.0401 | 0.0086 | 0.3391 |
| new | actual | all | top3_stress | 0.0000 | tau | 4896 | 0.0042 | 0.0000 | 0.0000 | 0.0069 | 0.0193 | 0.0000 | 0.1000 |
| new | actual | all | top3_stress | 0.5000 | tau | 4896 | 0.0040 | 0.0000 | 0.0000 | 0.0064 | 0.0184 | 0.0629 | 0.1000 |
| new | actual | all | top3_stress | 0.8000 | tau | 4896 | 0.0038 | 0.0000 | 0.0000 | 0.0059 | 0.0176 | 0.0639 | 0.1000 |
| new | actual | 1-3 | - | 0.0000 | M | 495 | 0.0001 | -0.0000 | -0.0000 | 0.0000 | 0.0057 |  |  |
| new | actual | 1-3 | linear | 0.0000 | tau | 495 | -0.0023 | -0.0030 | -0.0004 | 0.0003 | 0.0022 | 0.0000 | 0.5000 |
| new | actual | 1-3 | linear | 0.5000 | tau | 495 | -0.0023 | -0.0028 | -0.0006 | 0.0000 | 0.0008 | 0.0990 | 0.5000 |
| new | actual | 1-3 | linear | 0.8000 | tau | 495 | -0.0024 | -0.0031 | -0.0007 | 0.0000 | 0.0002 | 0.1091 | 0.5000 |
| new | actual | 1-3 | concave | 0.0000 | tau | 495 | -0.0013 | -0.0016 | -0.0002 | 0.0006 | 0.0043 | 0.0000 | 0.6599 |
| new | actual | 1-3 | concave | 0.5000 | tau | 495 | -0.0013 | -0.0015 | -0.0002 | 0.0004 | 0.0022 | 0.0121 | 0.6599 |
| new | actual | 1-3 | concave | 0.8000 | tau | 495 | -0.0013 | -0.0015 | -0.0002 | 0.0001 | 0.0010 | 0.0444 | 0.6599 |
| new | actual | 1-3 | convex | 0.0000 | tau | 495 | -0.0038 | -0.0055 | -0.0013 | -0.0001 | 0.0002 | 0.0000 | 0.3391 |
| new | actual | 1-3 | convex | 0.5000 | tau | 495 | -0.0038 | -0.0056 | -0.0017 | -0.0002 | 0.0001 | 0.0121 | 0.3391 |
| new | actual | 1-3 | convex | 0.8000 | tau | 495 | -0.0038 | -0.0058 | -0.0018 | -0.0002 | 0.0001 | 0.0222 | 0.3391 |
| new | actual | 1-3 | top3_stress | 0.0000 | tau | 495 | -0.0057 | -0.0095 | -0.0028 | -0.0006 | 0.0000 | 0.0000 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.5000 | tau | 495 | -0.0057 | -0.0095 | -0.0028 | -0.0006 | 0.0000 | 0.0081 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.8000 | tau | 495 | -0.0057 | -0.0093 | -0.0029 | -0.0006 | 0.0000 | 0.0101 | 0.1000 |
| new | actual | 4-10 | - | 0.0000 | M | 1146 | 0.0028 | -0.0000 | 0.0000 | 0.0007 | 0.0116 |  |  |
| new | actual | 4-10 | linear | 0.0000 | tau | 1146 | 0.0040 | 0.0000 | 0.0008 | 0.0064 | 0.0151 | 0.0000 | 0.5000 |
| new | actual | 4-10 | linear | 0.5000 | tau | 1146 | 0.0033 | -0.0000 | 0.0004 | 0.0057 | 0.0130 | 0.0689 | 0.5000 |
| new | actual | 4-10 | linear | 0.8000 | tau | 1146 | 0.0029 | -0.0001 | 0.0003 | 0.0053 | 0.0119 | 0.0820 | 0.5000 |
| new | actual | 4-10 | concave | 0.0000 | tau | 1146 | 0.0036 | 0.0000 | 0.0007 | 0.0054 | 0.0137 | 0.0000 | 0.6599 |
| new | actual | 4-10 | concave | 0.5000 | tau | 1146 | 0.0027 | 0.0000 | 0.0006 | 0.0042 | 0.0104 | 0.0052 | 0.6599 |
| new | actual | 4-10 | concave | 0.8000 | tau | 1146 | 0.0021 | 0.0000 | 0.0004 | 0.0037 | 0.0088 | 0.0122 | 0.6599 |
| new | actual | 4-10 | convex | 0.0000 | tau | 1146 | 0.0040 | -0.0001 | 0.0004 | 0.0072 | 0.0171 | 0.0000 | 0.3391 |
| new | actual | 4-10 | convex | 0.5000 | tau | 1146 | 0.0036 | -0.0001 | 0.0004 | 0.0066 | 0.0156 | 0.0061 | 0.3391 |
| new | actual | 4-10 | convex | 0.8000 | tau | 1146 | 0.0033 | -0.0001 | 0.0004 | 0.0065 | 0.0150 | 0.0140 | 0.3391 |
| new | actual | 4-10 | top3_stress | 0.0000 | tau | 1146 | 0.0017 | -0.0003 | 0.0002 | 0.0050 | 0.0123 | 0.0000 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.5000 | tau | 1146 | 0.0015 | -0.0002 | 0.0002 | 0.0049 | 0.0120 | 0.0183 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.8000 | tau | 1146 | 0.0015 | -0.0003 | 0.0002 | 0.0047 | 0.0119 | 0.0201 | 0.1000 |
| new | actual | 11-16 | - | 0.0000 | M | 978 | 0.0091 | -0.0000 | 0.0000 | 0.0000 | 0.0298 |  |  |
| new | actual | 11-16 | linear | 0.0000 | tau | 978 | 0.0260 | 0.0006 | 0.0214 | 0.0406 | 0.0549 | 0.0000 | 0.5000 |
| new | actual | 11-16 | linear | 0.5000 | tau | 978 | 0.0237 | 0.0005 | 0.0188 | 0.0387 | 0.0502 | 0.0010 | 0.5000 |
| new | actual | 11-16 | linear | 0.8000 | tau | 978 | 0.0223 | 0.0006 | 0.0172 | 0.0373 | 0.0490 | 0.0020 | 0.5000 |
| new | actual | 11-16 | concave | 0.0000 | tau | 978 | 0.0204 | 0.0004 | 0.0157 | 0.0290 | 0.0419 | 0.0000 | 0.6599 |
| new | actual | 11-16 | concave | 0.5000 | tau | 978 | 0.0174 | 0.0004 | 0.0141 | 0.0273 | 0.0373 | 0.0010 | 0.6599 |
| new | actual | 11-16 | concave | 0.8000 | tau | 978 | 0.0156 | 0.0004 | 0.0120 | 0.0260 | 0.0337 | 0.0010 | 0.6599 |
| new | actual | 11-16 | convex | 0.0000 | tau | 978 | 0.0288 | 0.0005 | 0.0247 | 0.0456 | 0.0613 | 0.0000 | 0.3391 |
| new | actual | 11-16 | convex | 0.5000 | tau | 978 | 0.0272 | 0.0007 | 0.0228 | 0.0432 | 0.0584 | 0.0010 | 0.3391 |
| new | actual | 11-16 | convex | 0.8000 | tau | 978 | 0.0263 | 0.0007 | 0.0210 | 0.0422 | 0.0565 | 0.0010 | 0.3391 |
| new | actual | 11-16 | top3_stress | 0.0000 | tau | 978 | 0.0142 | 0.0000 | 0.0128 | 0.0218 | 0.0305 | 0.0000 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.5000 | tau | 978 | 0.0138 | 0.0000 | 0.0123 | 0.0213 | 0.0295 | 0.0123 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.8000 | tau | 978 | 0.0135 | 0.0000 | 0.0119 | 0.0211 | 0.0293 | 0.0123 | 0.1000 |
| new | actual | 17-30 | - | 0.0000 | M | 2277 | 0.0066 | -0.0000 | 0.0000 | 0.0000 | 0.0099 |  |  |
| new | actual | 17-30 | linear | 0.0000 | tau | 2277 | 0.0210 | 0.0000 | 0.0159 | 0.0360 | 0.0511 | 0.0000 | 0.5000 |
| new | actual | 17-30 | linear | 0.5000 | tau | 2277 | 0.0194 | 0.0000 | 0.0151 | 0.0342 | 0.0474 | 0.0004 | 0.5000 |
| new | actual | 17-30 | linear | 0.8000 | tau | 2277 | 0.0184 | 0.0000 | 0.0137 | 0.0323 | 0.0463 | 0.0022 | 0.5000 |
| new | actual | 17-30 | concave | 0.0000 | tau | 2277 | 0.0223 | 0.0000 | 0.0216 | 0.0356 | 0.0512 | 0.0000 | 0.6599 |
| new | actual | 17-30 | concave | 0.5000 | tau | 2277 | 0.0201 | 0.0000 | 0.0203 | 0.0345 | 0.0456 | 0.0009 | 0.6599 |
| new | actual | 17-30 | concave | 0.8000 | tau | 2277 | 0.0188 | 0.0000 | 0.0172 | 0.0334 | 0.0435 | 0.0013 | 0.6599 |
| new | actual | 17-30 | convex | 0.0000 | tau | 2277 | 0.0148 | 0.0000 | 0.0048 | 0.0239 | 0.0431 | 0.0000 | 0.3391 |
| new | actual | 17-30 | convex | 0.5000 | tau | 2277 | 0.0137 | 0.0000 | 0.0046 | 0.0221 | 0.0402 | 0.0031 | 0.3391 |
| new | actual | 17-30 | convex | 0.8000 | tau | 2277 | 0.0130 | 0.0000 | 0.0046 | 0.0211 | 0.0383 | 0.0061 | 0.3391 |
| new | actual | 17-30 | top3_stress | 0.0000 | tau | 2277 | 0.0034 | 0.0000 | 0.0000 | 0.0029 | 0.0125 | 0.0000 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.5000 | tau | 2277 | 0.0030 | 0.0000 | 0.0000 | 0.0027 | 0.0109 | 0.1190 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.8000 | tau | 2277 | 0.0029 | 0.0000 | 0.0000 | 0.0026 | 0.0100 | 0.1199 | 0.1000 |
| new | own | all | - | 0.0000 | M | 4896 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | all | linear | 0.0000 | tau | 4896 | 0.0231 | 0.0003 | 0.0177 | 0.0387 | 0.0548 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.5000 | tau | 4896 | 0.0231 | 0.0003 | 0.0177 | 0.0387 | 0.0548 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.8000 | tau | 4896 | 0.0231 | 0.0003 | 0.0177 | 0.0387 | 0.0548 | 0.0000 | 0.5000 |
| new | own | all | concave | 0.0000 | tau | 4896 | 0.0206 | 0.0003 | 0.0206 | 0.0341 | 0.0447 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.5000 | tau | 4896 | 0.0206 | 0.0003 | 0.0206 | 0.0341 | 0.0447 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.8000 | tau | 4896 | 0.0206 | 0.0003 | 0.0206 | 0.0341 | 0.0447 | 0.0000 | 0.6599 |
| new | own | all | convex | 0.0000 | tau | 4896 | 0.0203 | 0.0001 | 0.0100 | 0.0339 | 0.0560 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.5000 | tau | 4896 | 0.0203 | 0.0001 | 0.0100 | 0.0339 | 0.0560 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.8000 | tau | 4896 | 0.0203 | 0.0001 | 0.0100 | 0.0339 | 0.0560 | 0.0000 | 0.3391 |
| new | own | all | top3_stress | 0.0000 | tau | 4896 | 0.0063 | 0.0000 | 0.0008 | 0.0117 | 0.0227 | 0.0000 | 0.1000 |
| new | own | all | top3_stress | 0.5000 | tau | 4896 | 0.0063 | 0.0000 | 0.0008 | 0.0117 | 0.0227 | 0.0711 | 0.1000 |
| new | own | all | top3_stress | 0.8000 | tau | 4896 | 0.0063 | 0.0000 | 0.0008 | 0.0117 | 0.0227 | 0.0713 | 0.1000 |
| new | own | 1-3 | - | 0.0000 | M | 495 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 1-3 | linear | 0.0000 | tau | 495 | -0.0017 | -0.0028 | -0.0008 | -0.0002 | -0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.5000 | tau | 495 | -0.0017 | -0.0028 | -0.0008 | -0.0002 | -0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.8000 | tau | 495 | -0.0017 | -0.0028 | -0.0008 | -0.0002 | -0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | concave | 0.0000 | tau | 495 | -0.0008 | -0.0014 | -0.0004 | -0.0001 | -0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.5000 | tau | 495 | -0.0008 | -0.0014 | -0.0004 | -0.0001 | -0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.8000 | tau | 495 | -0.0008 | -0.0014 | -0.0004 | -0.0001 | -0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | convex | 0.0000 | tau | 495 | -0.0031 | -0.0052 | -0.0015 | -0.0003 | -0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.5000 | tau | 495 | -0.0031 | -0.0052 | -0.0015 | -0.0003 | -0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.8000 | tau | 495 | -0.0031 | -0.0052 | -0.0015 | -0.0003 | -0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | top3_stress | 0.0000 | tau | 495 | -0.0056 | -0.0094 | -0.0027 | -0.0006 | -0.0000 | 0.0000 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.5000 | tau | 495 | -0.0056 | -0.0094 | -0.0027 | -0.0006 | -0.0000 | 0.0000 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.8000 | tau | 495 | -0.0056 | -0.0094 | -0.0027 | -0.0006 | -0.0000 | 0.0000 | 0.1000 |
| new | own | 4-10 | - | 0.0000 | M | 1146 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 4-10 | linear | 0.0000 | tau | 1146 | 0.0036 | -0.0000 | 0.0002 | 0.0052 | 0.0127 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.5000 | tau | 1146 | 0.0036 | -0.0000 | 0.0002 | 0.0052 | 0.0127 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.8000 | tau | 1146 | 0.0036 | -0.0000 | 0.0002 | 0.0052 | 0.0127 | 0.0000 | 0.5000 |
| new | own | 4-10 | concave | 0.0000 | tau | 1146 | 0.0023 | -0.0000 | 0.0001 | 0.0032 | 0.0078 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.5000 | tau | 1146 | 0.0023 | -0.0000 | 0.0001 | 0.0032 | 0.0078 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.8000 | tau | 1146 | 0.0023 | -0.0000 | 0.0001 | 0.0032 | 0.0078 | 0.0000 | 0.6599 |
| new | own | 4-10 | convex | 0.0000 | tau | 1146 | 0.0046 | -0.0000 | 0.0002 | 0.0075 | 0.0177 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.5000 | tau | 1146 | 0.0046 | -0.0000 | 0.0002 | 0.0075 | 0.0177 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.8000 | tau | 1146 | 0.0046 | -0.0000 | 0.0002 | 0.0075 | 0.0177 | 0.0000 | 0.3391 |
| new | own | 4-10 | top3_stress | 0.0000 | tau | 1146 | 0.0022 | -0.0001 | 0.0002 | 0.0065 | 0.0136 | 0.0000 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.5000 | tau | 1146 | 0.0022 | -0.0001 | 0.0002 | 0.0065 | 0.0136 | 0.0000 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.8000 | tau | 1146 | 0.0022 | -0.0001 | 0.0002 | 0.0065 | 0.0136 | 0.0000 | 0.1000 |
| new | own | 11-16 | - | 0.0000 | M | 978 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 11-16 | linear | 0.0000 | tau | 978 | 0.0335 | 0.0133 | 0.0313 | 0.0459 | 0.0624 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.5000 | tau | 978 | 0.0335 | 0.0133 | 0.0313 | 0.0459 | 0.0624 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.8000 | tau | 978 | 0.0335 | 0.0133 | 0.0313 | 0.0459 | 0.0624 | 0.0000 | 0.5000 |
| new | own | 11-16 | concave | 0.0000 | tau | 978 | 0.0221 | 0.0084 | 0.0205 | 0.0313 | 0.0415 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.5000 | tau | 978 | 0.0221 | 0.0084 | 0.0205 | 0.0313 | 0.0415 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.8000 | tau | 978 | 0.0221 | 0.0084 | 0.0205 | 0.0313 | 0.0415 | 0.0000 | 0.6599 |
| new | own | 11-16 | convex | 0.0000 | tau | 978 | 0.0406 | 0.0172 | 0.0377 | 0.0543 | 0.0748 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.5000 | tau | 978 | 0.0406 | 0.0172 | 0.0377 | 0.0543 | 0.0748 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.8000 | tau | 978 | 0.0406 | 0.0172 | 0.0377 | 0.0543 | 0.0748 | 0.0000 | 0.3391 |
| new | own | 11-16 | top3_stress | 0.0000 | tau | 978 | 0.0198 | 0.0106 | 0.0177 | 0.0256 | 0.0358 | 0.0000 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.5000 | tau | 978 | 0.0198 | 0.0106 | 0.0177 | 0.0256 | 0.0358 | 0.0010 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.8000 | tau | 978 | 0.0198 | 0.0106 | 0.0177 | 0.0256 | 0.0358 | 0.0010 | 0.1000 |
| new | own | 17-30 | - | 0.0000 | M | 2277 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 17-30 | linear | 0.0000 | tau | 2277 | 0.0339 | 0.0175 | 0.0308 | 0.0455 | 0.0609 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.5000 | tau | 2277 | 0.0339 | 0.0175 | 0.0308 | 0.0455 | 0.0609 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.8000 | tau | 2277 | 0.0339 | 0.0175 | 0.0308 | 0.0455 | 0.0609 | 0.0000 | 0.5000 |
| new | own | 17-30 | concave | 0.0000 | tau | 2277 | 0.0339 | 0.0255 | 0.0328 | 0.0414 | 0.0516 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.5000 | tau | 2277 | 0.0339 | 0.0255 | 0.0328 | 0.0414 | 0.0516 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.8000 | tau | 2277 | 0.0339 | 0.0255 | 0.0328 | 0.0414 | 0.0516 | 0.0000 | 0.6599 |
| new | own | 17-30 | convex | 0.0000 | tau | 2277 | 0.0246 | 0.0048 | 0.0162 | 0.0374 | 0.0586 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.5000 | tau | 2277 | 0.0246 | 0.0048 | 0.0162 | 0.0374 | 0.0586 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.8000 | tau | 2277 | 0.0246 | 0.0048 | 0.0162 | 0.0374 | 0.0586 | 0.0000 | 0.3391 |
| new | own | 17-30 | top3_stress | 0.0000 | tau | 2277 | 0.0053 | 0.0000 | 0.0004 | 0.0068 | 0.0178 | 0.0000 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.5000 | tau | 2277 | 0.0053 | 0.0000 | 0.0004 | 0.0068 | 0.0178 | 0.1524 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.8000 | tau | 2277 | 0.0053 | 0.0000 | 0.0004 | 0.0068 | 0.0178 | 0.1528 | 0.1000 |
| delta | actual | all | - | 0.0000 | M | 4896 | -0.0006 | -0.0000 | 0.0000 | 0.0000 | 0.0030 |  |  |
| delta | actual | all | linear | 0.0000 | tau | 4896 | -0.0022 | -0.0069 | 0.0000 | 0.0008 | 0.0102 | 0.0000 | 0.5000 |
| delta | actual | all | linear | 0.5000 | tau | 4896 | -0.0020 | -0.0068 | 0.0000 | 0.0007 | 0.0094 | 0.0074 | 0.5000 |
| delta | actual | all | linear | 0.8000 | tau | 4896 | -0.0020 | -0.0068 | 0.0000 | 0.0007 | 0.0089 | 0.0108 | 0.5000 |
| delta | actual | all | concave | 0.0000 | tau | 4896 | -0.0015 | -0.0044 | 0.0000 | 0.0009 | 0.0074 | 0.0000 | 0.6599 |
| delta | actual | all | concave | 0.5000 | tau | 4896 | -0.0013 | -0.0041 | 0.0000 | 0.0005 | 0.0063 | 0.0188 | 0.6599 |
| delta | actual | all | concave | 0.8000 | tau | 4896 | -0.0012 | -0.0039 | 0.0000 | 0.0005 | 0.0058 | 0.0357 | 0.6599 |
| delta | actual | all | convex | 0.0000 | tau | 4896 | -0.0030 | -0.0105 | 0.0000 | 0.0012 | 0.0130 | 0.0000 | 0.3391 |
| delta | actual | all | convex | 0.5000 | tau | 4896 | -0.0029 | -0.0104 | 0.0000 | 0.0013 | 0.0125 | 0.0049 | 0.3391 |
| delta | actual | all | convex | 0.8000 | tau | 4896 | -0.0029 | -0.0101 | 0.0000 | 0.0012 | 0.0123 | 0.0092 | 0.3391 |
| delta | actual | all | top3_stress | 0.0000 | tau | 4896 | -0.0026 | -0.0072 | 0.0000 | 0.0011 | 0.0100 | 0.0000 | 0.1000 |
| delta | actual | all | top3_stress | 0.5000 | tau | 4896 | -0.0026 | -0.0072 | 0.0000 | 0.0012 | 0.0097 | 0.0406 | 0.1000 |
| delta | actual | all | top3_stress | 0.8000 | tau | 4896 | -0.0025 | -0.0071 | 0.0000 | 0.0013 | 0.0097 | 0.0413 | 0.1000 |
| delta | actual | 1-3 | - | 0.0000 | M | 495 | -0.0006 | -0.0000 | -0.0000 | 0.0000 | 0.0038 |  |  |
| delta | actual | 1-3 | linear | 0.0000 | tau | 495 | -0.0056 | -0.0077 | -0.0027 | -0.0014 | -0.0004 | 0.0000 | 0.5000 |
| delta | actual | 1-3 | linear | 0.5000 | tau | 495 | -0.0054 | -0.0077 | -0.0031 | -0.0016 | -0.0006 | 0.0182 | 0.5000 |
| delta | actual | 1-3 | linear | 0.8000 | tau | 495 | -0.0054 | -0.0077 | -0.0032 | -0.0017 | -0.0007 | 0.0263 | 0.5000 |
| delta | actual | 1-3 | concave | 0.0000 | tau | 495 | -0.0033 | -0.0044 | -0.0015 | -0.0005 | 0.0013 | 0.0000 | 0.6599 |
| delta | actual | 1-3 | concave | 0.5000 | tau | 495 | -0.0031 | -0.0041 | -0.0015 | -0.0007 | 0.0000 | 0.0727 | 0.6599 |
| delta | actual | 1-3 | concave | 0.8000 | tau | 495 | -0.0030 | -0.0041 | -0.0016 | -0.0008 | -0.0003 | 0.1354 | 0.6599 |
| delta | actual | 1-3 | convex | 0.0000 | tau | 495 | -0.0090 | -0.0131 | -0.0053 | -0.0027 | -0.0011 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | convex | 0.5000 | tau | 495 | -0.0089 | -0.0124 | -0.0056 | -0.0030 | -0.0012 | 0.0081 | 0.3391 |
| delta | actual | 1-3 | convex | 0.8000 | tau | 495 | -0.0088 | -0.0125 | -0.0056 | -0.0030 | -0.0011 | 0.0081 | 0.3391 |
| delta | actual | 1-3 | top3_stress | 0.0000 | tau | 495 | -0.0102 | -0.0158 | -0.0043 | -0.0009 | -0.0000 | 0.0000 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.5000 | tau | 495 | -0.0102 | -0.0156 | -0.0044 | -0.0009 | -0.0000 | 0.0141 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.8000 | tau | 495 | -0.0102 | -0.0156 | -0.0044 | -0.0009 | -0.0000 | 0.0141 | 0.1000 |
| delta | actual | 4-10 | - | 0.0000 | M | 1146 | -0.0049 | -0.0006 | -0.0000 | 0.0000 | 0.0007 |  |  |
| delta | actual | 4-10 | linear | 0.0000 | tau | 1146 | -0.0143 | -0.0206 | -0.0118 | -0.0057 | -0.0006 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | linear | 0.5000 | tau | 1146 | -0.0131 | -0.0192 | -0.0115 | -0.0061 | -0.0006 | 0.0017 | 0.5000 |
| delta | actual | 4-10 | linear | 0.8000 | tau | 1146 | -0.0123 | -0.0182 | -0.0111 | -0.0062 | -0.0006 | 0.0026 | 0.5000 |
| delta | actual | 4-10 | concave | 0.0000 | tau | 1146 | -0.0103 | -0.0129 | -0.0069 | -0.0033 | 0.0000 | 0.0000 | 0.6599 |
| delta | actual | 4-10 | concave | 0.5000 | tau | 1146 | -0.0087 | -0.0124 | -0.0068 | -0.0032 | 0.0000 | 0.0288 | 0.6599 |
| delta | actual | 4-10 | concave | 0.8000 | tau | 1146 | -0.0077 | -0.0115 | -0.0065 | -0.0033 | -0.0004 | 0.0515 | 0.6599 |
| delta | actual | 4-10 | convex | 0.0000 | tau | 1146 | -0.0192 | -0.0277 | -0.0181 | -0.0100 | -0.0011 | 0.0000 | 0.3391 |
| delta | actual | 4-10 | convex | 0.5000 | tau | 1146 | -0.0184 | -0.0271 | -0.0177 | -0.0102 | -0.0013 | 0.0044 | 0.3391 |
| delta | actual | 4-10 | convex | 0.8000 | tau | 1146 | -0.0179 | -0.0264 | -0.0171 | -0.0099 | -0.0013 | 0.0061 | 0.3391 |
| delta | actual | 4-10 | top3_stress | 0.0000 | tau | 1146 | -0.0166 | -0.0227 | -0.0156 | -0.0094 | -0.0007 | 0.0000 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.5000 | tau | 1146 | -0.0164 | -0.0226 | -0.0154 | -0.0091 | -0.0005 | 0.0061 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.8000 | tau | 1146 | -0.0162 | -0.0224 | -0.0153 | -0.0087 | -0.0004 | 0.0070 | 0.1000 |
| delta | actual | 11-16 | - | 0.0000 | M | 978 | -0.0025 | -0.0000 | 0.0000 | 0.0000 | 0.0013 |  |  |
| delta | actual | 11-16 | linear | 0.0000 | tau | 978 | -0.0016 | -0.0091 | 0.0000 | 0.0061 | 0.0152 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | linear | 0.5000 | tau | 978 | -0.0009 | -0.0078 | 0.0000 | 0.0056 | 0.0140 | 0.0051 | 0.5000 |
| delta | actual | 11-16 | linear | 0.8000 | tau | 978 | -0.0006 | -0.0068 | 0.0000 | 0.0054 | 0.0133 | 0.0092 | 0.5000 |
| delta | actual | 11-16 | concave | 0.0000 | tau | 978 | -0.0022 | -0.0067 | 0.0000 | 0.0036 | 0.0110 | 0.0000 | 0.6599 |
| delta | actual | 11-16 | concave | 0.5000 | tau | 978 | -0.0014 | -0.0060 | 0.0000 | 0.0035 | 0.0091 | 0.0061 | 0.6599 |
| delta | actual | 11-16 | concave | 0.8000 | tau | 978 | -0.0009 | -0.0053 | 0.0000 | 0.0033 | 0.0083 | 0.0123 | 0.6599 |
| delta | actual | 11-16 | convex | 0.0000 | tau | 978 | 0.0003 | -0.0083 | 0.0000 | 0.0090 | 0.0202 | 0.0000 | 0.3391 |
| delta | actual | 11-16 | convex | 0.5000 | tau | 978 | 0.0007 | -0.0077 | 0.0000 | 0.0087 | 0.0192 | 0.0082 | 0.3391 |
| delta | actual | 11-16 | convex | 0.8000 | tau | 978 | 0.0010 | -0.0070 | 0.0000 | 0.0087 | 0.0184 | 0.0225 | 0.3391 |
| delta | actual | 11-16 | top3_stress | 0.0000 | tau | 978 | 0.0053 | 0.0000 | 0.0026 | 0.0107 | 0.0177 | 0.0000 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.5000 | tau | 978 | 0.0054 | 0.0000 | 0.0031 | 0.0108 | 0.0170 | 0.0368 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.8000 | tau | 978 | 0.0055 | 0.0000 | 0.0033 | 0.0109 | 0.0169 | 0.0389 | 0.1000 |
| delta | actual | 17-30 | - | 0.0000 | M | 2277 | 0.0024 | 0.0000 | 0.0000 | 0.0000 | 0.0050 |  |  |
| delta | actual | 17-30 | linear | 0.0000 | tau | 2277 | 0.0044 | 0.0000 | 0.0000 | 0.0041 | 0.0154 | 0.0000 | 0.5000 |
| delta | actual | 17-30 | linear | 0.5000 | tau | 2277 | 0.0038 | 0.0000 | 0.0000 | 0.0039 | 0.0138 | 0.0088 | 0.5000 |
| delta | actual | 17-30 | linear | 0.8000 | tau | 2277 | 0.0034 | 0.0000 | 0.0000 | 0.0038 | 0.0126 | 0.0123 | 0.5000 |
| delta | actual | 17-30 | concave | 0.0000 | tau | 2277 | 0.0036 | 0.0000 | 0.0000 | 0.0028 | 0.0128 | 0.0000 | 0.6599 |
| delta | actual | 17-30 | concave | 0.5000 | tau | 2277 | 0.0028 | 0.0000 | 0.0000 | 0.0025 | 0.0103 | 0.0075 | 0.6599 |
| delta | actual | 17-30 | concave | 0.8000 | tau | 2277 | 0.0024 | 0.0000 | 0.0000 | 0.0023 | 0.0088 | 0.0162 | 0.6599 |
| delta | actual | 17-30 | convex | 0.0000 | tau | 2277 | 0.0050 | 0.0000 | 0.0000 | 0.0055 | 0.0178 | 0.0000 | 0.3391 |
| delta | actual | 17-30 | convex | 0.5000 | tau | 2277 | 0.0046 | 0.0000 | 0.0000 | 0.0052 | 0.0165 | 0.0031 | 0.3391 |
| delta | actual | 17-30 | convex | 0.8000 | tau | 2277 | 0.0044 | 0.0000 | 0.0000 | 0.0052 | 0.0155 | 0.0053 | 0.3391 |
| delta | actual | 17-30 | top3_stress | 0.0000 | tau | 2277 | 0.0028 | 0.0000 | 0.0000 | 0.0026 | 0.0098 | 0.0000 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.5000 | tau | 2277 | 0.0027 | 0.0000 | 0.0000 | 0.0026 | 0.0094 | 0.0654 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.8000 | tau | 2277 | 0.0026 | 0.0000 | 0.0000 | 0.0026 | 0.0091 | 0.0654 | 0.1000 |
| delta | own | all | - | 0.0000 | M | 4896 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | all | linear | 0.0000 | tau | 4896 | -0.0010 | -0.0078 | -0.0000 | 0.0034 | 0.0131 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.5000 | tau | 4896 | -0.0010 | -0.0078 | -0.0000 | 0.0034 | 0.0131 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.8000 | tau | 4896 | -0.0010 | -0.0078 | -0.0000 | 0.0034 | 0.0131 | 0.0004 | 0.5000 |
| delta | own | all | concave | 0.0000 | tau | 4896 | -0.0006 | -0.0045 | -0.0000 | 0.0018 | 0.0077 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.5000 | tau | 4896 | -0.0006 | -0.0045 | -0.0000 | 0.0018 | 0.0077 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.8000 | tau | 4896 | -0.0006 | -0.0045 | -0.0000 | 0.0018 | 0.0077 | 0.0000 | 0.6599 |
| delta | own | all | convex | 0.0000 | tau | 4896 | -0.0016 | -0.0118 | 0.0000 | 0.0055 | 0.0189 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.5000 | tau | 4896 | -0.0016 | -0.0118 | 0.0000 | 0.0055 | 0.0189 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.8000 | tau | 4896 | -0.0016 | -0.0118 | 0.0000 | 0.0055 | 0.0189 | 0.0000 | 0.3391 |
| delta | own | all | top3_stress | 0.0000 | tau | 4896 | -0.0015 | -0.0090 | 0.0000 | 0.0051 | 0.0147 | 0.0000 | 0.1000 |
| delta | own | all | top3_stress | 0.5000 | tau | 4896 | -0.0015 | -0.0090 | 0.0000 | 0.0051 | 0.0147 | 0.0188 | 0.1000 |
| delta | own | all | top3_stress | 0.8000 | tau | 4896 | -0.0015 | -0.0090 | 0.0000 | 0.0051 | 0.0147 | 0.0188 | 0.1000 |
| delta | own | 1-3 | - | 0.0000 | M | 495 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 1-3 | linear | 0.0000 | tau | 495 | -0.0050 | -0.0069 | -0.0034 | -0.0020 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.5000 | tau | 495 | -0.0050 | -0.0069 | -0.0034 | -0.0020 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.8000 | tau | 495 | -0.0050 | -0.0069 | -0.0034 | -0.0020 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | concave | 0.0000 | tau | 495 | -0.0027 | -0.0036 | -0.0018 | -0.0011 | -0.0008 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.5000 | tau | 495 | -0.0027 | -0.0036 | -0.0018 | -0.0011 | -0.0008 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.8000 | tau | 495 | -0.0027 | -0.0036 | -0.0018 | -0.0011 | -0.0008 | 0.0000 | 0.6599 |
| delta | own | 1-3 | convex | 0.0000 | tau | 495 | -0.0088 | -0.0122 | -0.0058 | -0.0035 | -0.0024 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.5000 | tau | 495 | -0.0088 | -0.0122 | -0.0058 | -0.0035 | -0.0024 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.8000 | tau | 495 | -0.0088 | -0.0122 | -0.0058 | -0.0035 | -0.0024 | 0.0000 | 0.3391 |
| delta | own | 1-3 | top3_stress | 0.0000 | tau | 495 | -0.0102 | -0.0157 | -0.0042 | -0.0009 | -0.0000 | 0.0000 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.5000 | tau | 495 | -0.0102 | -0.0157 | -0.0042 | -0.0009 | -0.0000 | 0.0121 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.8000 | tau | 495 | -0.0102 | -0.0157 | -0.0042 | -0.0009 | -0.0000 | 0.0121 | 0.1000 |
| delta | own | 4-10 | - | 0.0000 | M | 1146 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 4-10 | linear | 0.0000 | tau | 1146 | -0.0126 | -0.0179 | -0.0114 | -0.0072 | -0.0040 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.5000 | tau | 1146 | -0.0126 | -0.0179 | -0.0114 | -0.0072 | -0.0040 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.8000 | tau | 1146 | -0.0126 | -0.0179 | -0.0114 | -0.0072 | -0.0040 | 0.0000 | 0.5000 |
| delta | own | 4-10 | concave | 0.0000 | tau | 1146 | -0.0072 | -0.0104 | -0.0063 | -0.0041 | -0.0022 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.5000 | tau | 1146 | -0.0072 | -0.0104 | -0.0063 | -0.0041 | -0.0022 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.8000 | tau | 1146 | -0.0072 | -0.0104 | -0.0063 | -0.0041 | -0.0022 | 0.0000 | 0.6599 |
| delta | own | 4-10 | convex | 0.0000 | tau | 1146 | -0.0194 | -0.0270 | -0.0184 | -0.0115 | -0.0064 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.5000 | tau | 1146 | -0.0194 | -0.0270 | -0.0184 | -0.0115 | -0.0064 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.8000 | tau | 1146 | -0.0194 | -0.0270 | -0.0184 | -0.0115 | -0.0064 | 0.0000 | 0.3391 |
| delta | own | 4-10 | top3_stress | 0.0000 | tau | 1146 | -0.0176 | -0.0230 | -0.0163 | -0.0108 | -0.0055 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.5000 | tau | 1146 | -0.0176 | -0.0230 | -0.0163 | -0.0108 | -0.0055 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.8000 | tau | 1146 | -0.0176 | -0.0230 | -0.0163 | -0.0108 | -0.0055 | 0.0000 | 0.1000 |
| delta | own | 11-16 | - | 0.0000 | M | 978 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 11-16 | linear | 0.0000 | tau | 978 | 0.0009 | -0.0099 | 0.0009 | 0.0089 | 0.0174 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.5000 | tau | 978 | 0.0009 | -0.0099 | 0.0009 | 0.0089 | 0.0174 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.8000 | tau | 978 | 0.0009 | -0.0099 | 0.0009 | 0.0089 | 0.0174 | 0.0000 | 0.5000 |
| delta | own | 11-16 | concave | 0.0000 | tau | 978 | 0.0001 | -0.0065 | 0.0002 | 0.0048 | 0.0102 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.5000 | tau | 978 | 0.0001 | -0.0065 | 0.0002 | 0.0048 | 0.0102 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.8000 | tau | 978 | 0.0001 | -0.0065 | 0.0002 | 0.0048 | 0.0102 | 0.0000 | 0.6599 |
| delta | own | 11-16 | convex | 0.0000 | tau | 978 | 0.0033 | -0.0121 | 0.0033 | 0.0148 | 0.0275 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.5000 | tau | 978 | 0.0033 | -0.0121 | 0.0033 | 0.0148 | 0.0275 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.8000 | tau | 978 | 0.0033 | -0.0121 | 0.0033 | 0.0148 | 0.0275 | 0.0000 | 0.3391 |
| delta | own | 11-16 | top3_stress | 0.0000 | tau | 978 | 0.0083 | -0.0001 | 0.0079 | 0.0153 | 0.0234 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.5000 | tau | 978 | 0.0083 | -0.0001 | 0.0079 | 0.0153 | 0.0234 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.8000 | tau | 978 | 0.0083 | -0.0001 | 0.0079 | 0.0153 | 0.0234 | 0.0000 | 0.1000 |
| delta | own | 17-30 | - | 0.0000 | M | 2277 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 17-30 | linear | 0.0000 | tau | 2277 | 0.0048 | 0.0000 | 0.0002 | 0.0077 | 0.0158 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.5000 | tau | 2277 | 0.0048 | 0.0000 | 0.0002 | 0.0077 | 0.0158 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.8000 | tau | 2277 | 0.0048 | 0.0000 | 0.0002 | 0.0077 | 0.0158 | 0.0009 | 0.5000 |
| delta | own | 17-30 | concave | 0.0000 | tau | 2277 | 0.0029 | 0.0000 | 0.0001 | 0.0047 | 0.0096 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.5000 | tau | 2277 | 0.0029 | 0.0000 | 0.0001 | 0.0047 | 0.0096 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.8000 | tau | 2277 | 0.0029 | 0.0000 | 0.0001 | 0.0047 | 0.0096 | 0.0000 | 0.6599 |
| delta | own | 17-30 | convex | 0.0000 | tau | 2277 | 0.0069 | 0.0000 | 0.0003 | 0.0104 | 0.0223 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.5000 | tau | 2277 | 0.0069 | 0.0000 | 0.0003 | 0.0104 | 0.0223 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.8000 | tau | 2277 | 0.0069 | 0.0000 | 0.0003 | 0.0104 | 0.0223 | 0.0000 | 0.3391 |
| delta | own | 17-30 | top3_stress | 0.0000 | tau | 2277 | 0.0044 | 0.0000 | 0.0004 | 0.0060 | 0.0144 | 0.0000 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.5000 | tau | 2277 | 0.0044 | 0.0000 | 0.0004 | 0.0060 | 0.0144 | 0.0378 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.8000 | tau | 2277 | 0.0044 | 0.0000 | 0.0004 | 0.0060 | 0.0144 | 0.0378 | 0.1000 |

## T5_attr_seeding

| rule | portfolio | seed_group | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| old | actual | <0.01 | B | dominance_positive | 0.7417 | 0.6773 | 0.7933 | 1382 |
| old | actual | <0.01 | B | reversal | 0.0405 | 0.0218 | 0.0615 | 1382 |
| old | actual | <0.01 | B | negligible | 0.1700 | 0.1170 | 0.2250 | 1382 |
| old | actual | <0.01 | B | unresolved | 0.0478 | 0.0181 | 0.0902 | 1382 |
| old | actual | 0.01-0.05 | B | dominance_positive | 0.6871 | 0.5639 | 0.8750 | 326 |
| old | actual | 0.01-0.05 | B | reversal | 0.0460 | 0.0036 | 0.0973 | 326 |
| old | actual | 0.01-0.05 | B | negligible | 0.2515 | 0.0940 | 0.3534 | 326 |
| old | actual | 0.01-0.05 | B | unresolved | 0.0153 | 0.0000 | 0.0507 | 326 |
| old | actual | >=0.05 | B | dominance_positive | 0.7117 | 0.5853 | 0.8178 | 3188 |
| old | actual | >=0.05 | B | reversal | 0.0314 | 0.0090 | 0.0770 | 3188 |
| old | actual | >=0.05 | B | negligible | 0.2494 | 0.1676 | 0.3279 | 3188 |
| old | actual | >=0.05 | B | unresolved | 0.0075 | 0.0000 | 0.0217 | 3188 |
| old | own | <0.01 | B | dominance_positive | 0.9175 | 0.8669 | 0.9620 | 1382 |
| old | own | <0.01 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 1382 |
| old | own | <0.01 | B | negligible | 0.0810 | 0.0373 | 0.1324 | 1382 |
| old | own | <0.01 | B | unresolved | 0.0014 | 0.0000 | 0.0070 | 1382 |
| old | own | 0.01-0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 326 |
| old | own | 0.01-0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 326 |
| old | own | 0.01-0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 326 |
| old | own | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 326 |
| old | own | >=0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 3188 |
| old | own | >=0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 3188 |
| old | own | >=0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 3188 |
| old | own | >=0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 3188 |
| new | actual | <0.01 | B | dominance_positive | 0.1136 | 0.0603 | 0.1725 | 1382 |
| new | actual | <0.01 | B | reversal | 0.3647 | 0.2275 | 0.5062 | 1382 |
| new | actual | <0.01 | B | negligible | 0.4342 | 0.3130 | 0.5513 | 1382 |
| new | actual | <0.01 | B | unresolved | 0.0876 | 0.0367 | 0.1390 | 1382 |
| new | actual | 0.01-0.05 | B | dominance_positive | 0.5736 | 0.4719 | 0.7173 | 326 |
| new | actual | 0.01-0.05 | B | reversal | 0.0337 | 0.0036 | 0.0924 | 326 |
| new | actual | 0.01-0.05 | B | negligible | 0.3558 | 0.1542 | 0.4923 | 326 |
| new | actual | 0.01-0.05 | B | unresolved | 0.0368 | 0.0020 | 0.1095 | 326 |
| new | actual | >=0.05 | B | dominance_positive | 0.7315 | 0.6287 | 0.8092 | 3188 |
| new | actual | >=0.05 | B | reversal | 0.0380 | 0.0160 | 0.0742 | 3188 |
| new | actual | >=0.05 | B | negligible | 0.2237 | 0.1552 | 0.2997 | 3188 |
| new | actual | >=0.05 | B | unresolved | 0.0069 | 0.0030 | 0.0118 | 3188 |
| new | own | <0.01 | B | dominance_positive | 0.1237 | 0.0686 | 0.2018 | 1382 |
| new | own | <0.01 | B | reversal | 0.3683 | 0.2170 | 0.5219 | 1382 |
| new | own | <0.01 | B | negligible | 0.4906 | 0.3640 | 0.6057 | 1382 |
| new | own | <0.01 | B | unresolved | 0.0174 | 0.0084 | 0.0295 | 1382 |
| new | own | 0.01-0.05 | B | dominance_positive | 0.8558 | 0.7599 | 0.9372 | 326 |
| new | own | 0.01-0.05 | B | reversal | 0.0092 | 0.0000 | 0.0556 | 326 |
| new | own | 0.01-0.05 | B | negligible | 0.1288 | 0.0433 | 0.2264 | 326 |
| new | own | 0.01-0.05 | B | unresolved | 0.0061 | 0.0000 | 0.0360 | 326 |
| new | own | >=0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 3188 |
| new | own | >=0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 3188 |
| new | own | >=0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 3188 |
| new | own | >=0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 3188 |

## T5_attr_ledger_features

| rule | feature | value | n | reversal_share | lo99 | hi99 |
|---|---|---|---|---|---|---|
| old | holds_conditional_other | True | 2100 | 0.0810 | 0.0442 | 0.1371 |
| old | holds_conditional_other | False | 2796 | 0.0004 | 0.0000 | 0.0022 |
| old | holds_opponent_pick | True | 157 | 0.4522 | 0.3175 | 0.5928 |
| old | holds_opponent_pick | False | 4739 | 0.0211 | 0.0070 | 0.0500 |
| old | holds_pooled_pick | True | 1562 | 0.0640 | 0.0157 | 0.1809 |
| old | holds_pooled_pick | False | 3334 | 0.0213 | 0.0106 | 0.0332 |
| old | self_restricted | True | 0 |  |  |  |
| old | self_restricted | False | 4896 | 0.0349 | 0.0179 | 0.0645 |
| old | opp_restricted | True | 0 |  |  |  |
| old | opp_restricted | False | 4896 | 0.0349 | 0.0179 | 0.0645 |
| old | holds_conditional_other_state | True | 1884 | 0.0897 | 0.0485 | 0.1635 |
| old | holds_conditional_other_state | False | 3012 | 0.0007 | 0.0000 | 0.0034 |
| old | holds_opponent_pick_state | True | 141 | 0.5035 | 0.3559 | 0.6377 |
| old | holds_opponent_pick_state | False | 4755 | 0.0210 | 0.0070 | 0.0497 |
| new | holds_conditional_other | True | 2100 | 0.1786 | 0.1057 | 0.2423 |
| new | holds_conditional_other | False | 2796 | 0.0933 | 0.0410 | 0.1490 |
| new | holds_opponent_pick | True | 157 | 0.4841 | 0.3288 | 0.6265 |
| new | holds_opponent_pick | False | 4739 | 0.1182 | 0.0635 | 0.1532 |
| new | holds_pooled_pick | True | 1562 | 0.1440 | 0.0452 | 0.2685 |
| new | holds_pooled_pick | False | 3334 | 0.1233 | 0.0739 | 0.1837 |
| new | self_restricted | True | 0 |  |  |  |
| new | self_restricted | False | 4896 | 0.1299 | 0.0751 | 0.1670 |
| new | opp_restricted | True | 0 |  |  |  |
| new | opp_restricted | False | 4896 | 0.1299 | 0.0751 | 0.1670 |
| new | holds_conditional_other_state | True | 1992 | 0.1712 | 0.0945 | 0.2328 |
| new | holds_conditional_other_state | False | 2904 | 0.1016 | 0.0506 | 0.1554 |
| new | holds_opponent_pick_state | True | 149 | 0.4966 | 0.3448 | 0.6370 |
| new | holds_opponent_pick_state | False | 4747 | 0.1184 | 0.0643 | 0.1534 |

## T5_6_transitions

| portfolio | old | new | count |
|---|---|---|---|
| actual | dominance_positive | dominance_positive | 2528 |
| actual | dominance_positive | negligible | 418 |
| actual | dominance_positive | reversal | 487 |
| actual | dominance_positive | unresolved | 85 |
| actual | negligible | dominance_positive | 112 |
| actual | negligible | negligible | 987 |
| actual | negligible | reversal | 7 |
| actual | negligible | unresolved | 6 |
| actual | reversal | dominance_positive | 16 |
| actual | reversal | negligible | 11 |
| actual | reversal | reversal | 134 |
| actual | reversal | unresolved | 10 |
| actual | unresolved | dominance_positive | 20 |
| actual | unresolved | negligible | 13 |
| actual | unresolved | reversal | 8 |
| actual | unresolved | unresolved | 54 |
| own | dominance_positive | dominance_positive | 3637 |
| own | dominance_positive | negligible | 607 |
| own | dominance_positive | reversal | 512 |
| own | dominance_positive | unresolved | 26 |
| own | negligible | dominance_positive | 1 |
| own | negligible | negligible | 111 |
| own | unresolved | negligible | 2 |

## T5_headline_reversal_diff

| contrast | portfolio | verdict | share_a | share_b | diff | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| new_minus_old | actual | verdict_B | 0.1299 | 0.0349 | 0.0950 | 0.0478 | 0.1340 | 4896 |
| new_minus_old | actual | verdict_B_pm | 0.1058 | 0.0251 | 0.0807 | 0.0437 | 0.1077 | 4896 |
| new_minus_old | own | verdict_B | 0.1046 | 0.0000 | 0.1046 | 0.0561 | 0.1454 | 4896 |
| new_minus_old | own | verdict_B_pm | 0.0944 | 0.0000 | 0.0944 | 0.0492 | 0.1357 | 4896 |
| actual_minus_own | old | verdict_B | 0.0349 | 0.0000 | 0.0349 | 0.0179 | 0.0645 | 4896 |
| actual_minus_own | new | verdict_B | 0.1299 | 0.1046 | 0.0253 | 0.0103 | 0.0509 | 4896 |

## T5_4_typology

| rule | curve | type | share | lo99 | hi99 | n | tp_dominated_share |
|---|---|---|---|---|---|---|---|
| old | linear | both_lose | 0.4624 | 0.3082 | 0.6470 | 1132 | 0.2544 |
| old | linear | both_win | 0.0012 | 0.0000 | 0.0046 | 3 | 0.0000 |
| old | linear | normal | 0.4052 | 0.2937 | 0.4863 | 992 | 0.7490 |
| old | linear | opposed | 0.0131 | 0.0023 | 0.0285 | 32 | 0.9062 |
| old | linear | one_sided_win | 0.0167 | 0.0038 | 0.0363 | 41 | 0.8049 |
| old | linear | no_own_stake | 0.1013 | 0.0443 | 0.1608 | 248 | 1.0000 |
| old | concave | both_lose | 0.4158 | 0.2653 | 0.6051 | 1018 | 0.2809 |
| old | concave | both_win | 0.0016 | 0.0000 | 0.0050 | 4 | 0.2500 |
| old | concave | normal | 0.4191 | 0.3184 | 0.4883 | 1026 | 0.7302 |
| old | concave | opposed | 0.0159 | 0.0038 | 0.0328 | 39 | 0.8205 |
| old | concave | one_sided_win | 0.0188 | 0.0059 | 0.0414 | 46 | 0.8261 |
| old | concave | no_own_stake | 0.1287 | 0.0594 | 0.1971 | 315 | 1.0000 |
| old | convex | both_lose | 0.4636 | 0.3438 | 0.5868 | 1135 | 0.2088 |
| old | convex | both_win | 0.0004 | 0.0000 | 0.0026 | 1 | 0.0000 |
| old | convex | normal | 0.4163 | 0.3485 | 0.4764 | 1019 | 0.6087 |
| old | convex | opposed | 0.0102 | 0.0017 | 0.0208 | 25 | 0.6800 |
| old | convex | one_sided_win | 0.0118 | 0.0030 | 0.0229 | 29 | 0.6552 |
| old | convex | no_own_stake | 0.0976 | 0.0468 | 0.1578 | 239 | 1.0000 |
| old | top3_stress | both_lose | 0.1846 | 0.1452 | 0.2426 | 452 | 0.0133 |
| old | top3_stress | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan |
| old | top3_stress | normal | 0.4665 | 0.4324 | 0.5026 | 1142 | 0.1190 |
| old | top3_stress | opposed | 0.0004 | 0.0000 | 0.0025 | 1 | 0.0000 |
| old | top3_stress | one_sided_win | 0.0037 | 0.0004 | 0.0084 | 9 | 0.3750 |
| old | top3_stress | no_own_stake | 0.3448 | 0.2880 | 0.3895 | 844 | 0.9888 |
| new | linear | both_lose | 0.2896 | 0.1785 | 0.4152 | 709 | 0.2412 |
| new | linear | both_win | 0.0061 | 0.0004 | 0.0145 | 15 | 0.1333 |
| new | linear | normal | 0.4028 | 0.3318 | 0.4777 | 986 | 0.6094 |
| new | linear | opposed | 0.0564 | 0.0153 | 0.1005 | 138 | 0.3723 |
| new | linear | one_sided_win | 0.0511 | 0.0158 | 0.0964 | 125 | 0.7250 |
| new | linear | no_own_stake | 0.1940 | 0.0964 | 0.2929 | 475 | 1.0000 |
| new | concave | both_lose | 0.2974 | 0.1887 | 0.4051 | 728 | 0.2953 |
| new | concave | both_win | 0.0049 | 0.0000 | 0.0124 | 12 | 0.3333 |
| new | concave | normal | 0.4212 | 0.3785 | 0.4694 | 1031 | 0.6634 |
| new | concave | opposed | 0.0359 | 0.0144 | 0.0586 | 88 | 0.5227 |
| new | concave | one_sided_win | 0.0364 | 0.0124 | 0.0660 | 89 | 0.7045 |
| new | concave | no_own_stake | 0.2042 | 0.1164 | 0.2938 | 500 | 1.0000 |
| new | convex | both_lose | 0.2578 | 0.1652 | 0.3633 | 631 | 0.2076 |
| new | convex | both_win | 0.0094 | 0.0024 | 0.0187 | 23 | 0.1304 |
| new | convex | normal | 0.3934 | 0.3352 | 0.4551 | 963 | 0.4854 |
| new | convex | opposed | 0.0711 | 0.0320 | 0.1176 | 174 | 0.2414 |
| new | convex | one_sided_win | 0.0670 | 0.0302 | 0.1098 | 164 | 0.5750 |
| new | convex | no_own_stake | 0.2014 | 0.1066 | 0.2969 | 493 | 1.0000 |
| new | top3_stress | both_lose | 0.1250 | 0.0794 | 0.1760 | 306 | 0.0229 |
| new | top3_stress | both_win | 0.0106 | 0.0025 | 0.0220 | 26 | 0.1154 |
| new | top3_stress | normal | 0.3607 | 0.2949 | 0.4330 | 883 | 0.2145 |
| new | top3_stress | opposed | 0.0605 | 0.0321 | 0.0924 | 148 | 0.0473 |
| new | top3_stress | one_sided_win | 0.1070 | 0.0527 | 0.1581 | 262 | 0.2056 |
| new | top3_stress | no_own_stake | 0.3362 | 0.2521 | 0.4080 | 823 | 1.0000 |

## T5_5_stakes_distribution

| rule | curve | measure | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| old | linear | tp_share | 2416 | 0.5648 | 0.4030 | 0.5219 | 0.7542 | 0.9645 |
| old | linear | tp_share_raw | 2440 | 0.6163 | 0.4922 | 0.5751 | 0.7772 | 0.9417 |
| old | linear | hhi | 2416 | 0.3011 | 0.2139 | 0.2789 | 0.3640 | 0.4595 |
| old | linear | n_material | 2448 | 6.4984 | 4.0000 | 7.0000 | 9.0000 | 10.0000 |
| old | linear | mean_abs_third | 2448 | 0.0018 | 0.0008 | 0.0015 | 0.0023 | 0.0034 |
| old | linear | mean_abs_third_raw | 2448 | 0.0021 | 0.0012 | 0.0018 | 0.0027 | 0.0037 |
| old | concave | tp_share | 2399 | 0.5901 | 0.4250 | 0.5548 | 0.8076 | 1.0000 |
| old | concave | tp_share_raw | 2431 | 0.6408 | 0.4995 | 0.6050 | 0.8225 | 0.9614 |
| old | concave | hhi | 2399 | 0.3086 | 0.2165 | 0.2817 | 0.3761 | 0.4841 |
| old | concave | n_material | 2448 | 5.9408 | 4.0000 | 6.0000 | 8.0000 | 10.0000 |
| old | concave | mean_abs_third | 2448 | 0.0019 | 0.0008 | 0.0016 | 0.0025 | 0.0035 |
| old | concave | mean_abs_third_raw | 2448 | 0.0022 | 0.0012 | 0.0019 | 0.0028 | 0.0038 |
| old | convex | tp_share | 2408 | 0.5038 | 0.3464 | 0.4828 | 0.6772 | 0.9317 |
| old | convex | tp_share_raw | 2434 | 0.5932 | 0.4852 | 0.5399 | 0.7312 | 0.9281 |
| old | convex | hhi | 2408 | 0.3635 | 0.2422 | 0.3179 | 0.4097 | 0.5266 |
| old | convex | n_material | 2448 | 5.5266 | 3.0000 | 5.5000 | 7.0000 | 9.0000 |
| old | convex | mean_abs_third | 2448 | 0.0013 | 0.0005 | 0.0011 | 0.0018 | 0.0027 |
| old | convex | mean_abs_third_raw | 2448 | 0.0017 | 0.0009 | 0.0015 | 0.0022 | 0.0030 |
| old | top3_stress | tp_share | 1774 | 0.3688 | 0.1194 | 0.3898 | 0.4784 | 1.0000 |
| old | top3_stress | tp_share_raw | 1955 | 0.5310 | 0.4815 | 0.5013 | 0.5229 | 0.9088 |
| old | top3_stress | hhi | 1774 | 0.5460 | 0.3638 | 0.4835 | 0.6003 | 1.0000 |
| old | top3_stress | n_material | 2448 | 2.2353 | 0.0000 | 2.0000 | 4.0000 | 5.0000 |
| old | top3_stress | mean_abs_third | 2448 | 0.0003 | 0.0000 | 0.0001 | 0.0005 | 0.0009 |
| old | top3_stress | mean_abs_third_raw | 2448 | 0.0005 | 0.0001 | 0.0004 | 0.0008 | 0.0011 |
| new | linear | tp_share | 2292 | 0.5901 | 0.4315 | 0.5190 | 0.7896 | 1.0000 |
| new | linear | tp_share_raw | 2354 | 0.6353 | 0.5004 | 0.5773 | 0.8026 | 0.9780 |
| new | linear | hhi | 2292 | 0.3174 | 0.2240 | 0.2982 | 0.3738 | 0.5000 |
| new | linear | n_material | 2448 | 5.8284 | 3.0000 | 6.0000 | 8.0000 | 10.0000 |
| new | linear | mean_abs_third | 2448 | 0.0017 | 0.0006 | 0.0014 | 0.0024 | 0.0036 |
| new | linear | mean_abs_third_raw | 2448 | 0.0020 | 0.0009 | 0.0017 | 0.0027 | 0.0038 |
| new | concave | tp_share | 2290 | 0.6093 | 0.4530 | 0.5526 | 0.8180 | 1.0000 |
| new | concave | tp_share_raw | 2362 | 0.6504 | 0.5023 | 0.6059 | 0.8195 | 0.9825 |
| new | concave | hhi | 2290 | 0.3082 | 0.2152 | 0.2832 | 0.3725 | 0.5000 |
| new | concave | n_material | 2448 | 5.7958 | 4.0000 | 6.0000 | 8.0000 | 10.0000 |
| new | concave | mean_abs_third | 2448 | 0.0018 | 0.0007 | 0.0015 | 0.0025 | 0.0035 |
| new | concave | mean_abs_third_raw | 2448 | 0.0020 | 0.0010 | 0.0018 | 0.0027 | 0.0038 |
| new | convex | tp_share | 2228 | 0.5302 | 0.3830 | 0.4876 | 0.7204 | 1.0000 |
| new | convex | tp_share_raw | 2331 | 0.6155 | 0.5000 | 0.5449 | 0.7561 | 0.9693 |
| new | convex | hhi | 2228 | 0.3931 | 0.2631 | 0.3347 | 0.4378 | 0.6158 |
| new | convex | n_material | 2448 | 4.6368 | 2.0000 | 5.0000 | 7.0000 | 8.0000 |
| new | convex | mean_abs_third | 2448 | 0.0014 | 0.0003 | 0.0009 | 0.0020 | 0.0032 |
| new | convex | mean_abs_third_raw | 2448 | 0.0016 | 0.0005 | 0.0013 | 0.0023 | 0.0035 |
| new | top3_stress | tp_share | 1823 | 0.4465 | 0.2858 | 0.4397 | 0.5079 | 1.0000 |
| new | top3_stress | tp_share_raw | 2005 | 0.5699 | 0.4956 | 0.5040 | 0.5925 | 0.9714 |
| new | top3_stress | hhi | 1823 | 0.4874 | 0.3472 | 0.4275 | 0.5210 | 1.0000 |
| new | top3_stress | n_material | 2448 | 2.3775 | 0.0000 | 2.0000 | 4.0000 | 5.0000 |
| new | top3_stress | mean_abs_third | 2448 | 0.0004 | 0.0000 | 0.0002 | 0.0007 | 0.0012 |
| new | top3_stress | mean_abs_third_raw | 2448 | 0.0006 | 0.0001 | 0.0004 | 0.0008 | 0.0013 |
| new_minus_old | linear | tp_share | 2289 | 0.0203 | -0.0239 | 0.0058 | 0.0782 | 0.1669 |
| new_minus_old | linear | hhi | 2289 | 0.0240 | -0.0320 | 0.0009 | 0.0620 | 0.1429 |
| new_minus_old | linear | mean_abs_third | 2448 | -0.0001 | -0.0004 | 0.0000 | 0.0004 | 0.0010 |
| new_minus_old | concave | tp_share | 2281 | 0.0139 | -0.0235 | 0.0014 | 0.0695 | 0.1601 |
| new_minus_old | concave | hhi | 2281 | 0.0076 | -0.0408 | -0.0000 | 0.0430 | 0.1198 |
| new_minus_old | concave | mean_abs_third | 2448 | -0.0001 | -0.0003 | 0.0000 | 0.0004 | 0.0009 |
| new_minus_old | convex | tp_share | 2228 | 0.0197 | -0.0380 | 0.0075 | 0.1012 | 0.2112 |
| new_minus_old | convex | hhi | 2228 | 0.0383 | -0.0488 | 0.0003 | 0.0878 | 0.2075 |
| new_minus_old | convex | mean_abs_third | 2448 | 0.0000 | -0.0005 | 0.0000 | 0.0005 | 0.0013 |
| new_minus_old | top3_stress | tp_share | 1502 | 0.0989 | -0.0166 | 0.0562 | 0.2801 | 0.4553 |
| new_minus_old | top3_stress | hhi | 1502 | -0.1159 | -0.3226 | -0.0552 | 0.0712 | 0.2305 |
| new_minus_old | top3_stress | mean_abs_third | 2448 | 0.0001 | -0.0002 | 0.0000 | 0.0004 | 0.0009 |

## H2

| curve | sample | n_games | mean_diff_new_minus_old | lo99 | hi99 | registered | supported |
|---|---|---|---|---|---|---|---|
| linear | registered | 2048 | -0.0001 | -0.0003 | 0.0002 | True | False |
| linear | state_conditional | 1898 | -0.0000 | -0.0003 | 0.0002 | False | False |
| concave | registered | 2048 | -0.0001 | -0.0004 | 0.0001 | False | False |
| concave | state_conditional | 1898 | -0.0001 | -0.0004 | 0.0001 | False | False |
| convex | registered | 2048 | 0.0001 | -0.0002 | 0.0003 | False | False |
| convex | state_conditional | 1898 | 0.0001 | -0.0001 | 0.0003 | False | False |
| top3_stress | registered | 2048 | 0.0002 | 0.0001 | 0.0002 | False | True |
| top3_stress | state_conditional | 1898 | 0.0002 | 0.0001 | 0.0003 | False | True |

## F5_2_network_edges

10440 rows in `F5_2_network_edges.csv`.

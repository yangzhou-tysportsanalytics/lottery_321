# Registered analysis output

tag `primary`; exclude_imprecise=False; states=312

## T5_0_diagnostics

| states | games | stopped_2000 | stopped_8000 | stopped_32000 | missed_target | n_worlds_match | max_halfwidth_linear | max_halfwidth_linear_rules_only | max_halfwidth_delta_linear | p95_halfwidth_linear | max_q_total_dev | max_per_slot_dev | per_slot_noise_scale | max_own_slot_dev | max_zero_sum_dev |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 312 | 2448 | 3 | 20 | 140 | 149 | 2000 | 0.0078 | 0.0078 | 0.0067 | 0.0050 | 0.0000 | 0.0116 | 0.0112 | 0.0000 | 0.0068 |

## T5_0b_zero_sum_by_curve

| curve | rule | max_zero_sum_dev | mean_zero_sum_dev | n_games |
|---|---|---|---|---|
| linear | old | 0.0012 | 0.0001 | 2448 |
| linear | new | 0.0017 | 0.0001 | 2448 |
| concave | old | 0.0007 | 0.0001 | 2448 |
| concave | new | 0.0010 | 0.0001 | 2448 |
| convex | old | 0.0020 | 0.0002 | 2448 |
| convex | new | 0.0025 | 0.0002 | 2448 |
| top3_stress | old | 0.0068 | 0.0004 | 2448 |
| top3_stress | new | 0.0053 | 0.0003 | 2448 |

## T5_0c_verdict_by_look

| rule | portfolio | stopped_at | verdict_B | verdict_B_pm | count |
|---|---|---|---|---|---|
| delta | actual | 2000 | negligible | negligible | 3 |
| delta | actual | 2000 | reversal | reversal | 6 |
| delta | actual | 2000 | unresolved | unresolved | 3 |
| delta | actual | 32000 | dominance_positive | dominance_positive | 111 |
| delta | actual | 32000 | dominance_positive | unresolved | 59 |
| delta | actual | 32000 | negligible | dominance_positive | 1 |
| delta | actual | 32000 | negligible | negligible | 510 |
| delta | actual | 32000 | negligible | unresolved | 25 |
| delta | actual | 32000 | reversal | reversal | 713 |
| delta | actual | 32000 | reversal | unresolved | 109 |
| delta | actual | 32000 | unresolved | unresolved | 558 |
| delta | actual | 8000 | dominance_positive | dominance_positive | 4 |
| delta | actual | 8000 | negligible | negligible | 67 |
| delta | actual | 8000 | negligible | unresolved | 1 |
| delta | actual | 8000 | reversal | reversal | 72 |
| delta | actual | 8000 | reversal | unresolved | 5 |
| delta | actual | 8000 | unresolved | unresolved | 61 |
| delta | actual | missed | dominance_positive | dominance_positive | 185 |
| delta | actual | missed | dominance_positive | unresolved | 95 |
| delta | actual | missed | negligible | dominance_positive | 5 |
| delta | actual | missed | negligible | negligible | 675 |
| delta | actual | missed | negligible | unresolved | 28 |
| delta | actual | missed | reversal | reversal | 977 |
| delta | actual | missed | reversal | unresolved | 101 |
| delta | actual | missed | unresolved | unresolved | 522 |
| delta | own | 2000 | negligible | negligible | 1 |
| delta | own | 2000 | reversal | reversal | 7 |
| delta | own | 2000 | unresolved | unresolved | 4 |
| delta | own | 32000 | dominance_positive | dominance_positive | 2 |
| delta | own | 32000 | dominance_positive | unresolved | 49 |
| delta | own | 32000 | negligible | negligible | 262 |
| delta | own | 32000 | negligible | unresolved | 18 |
| delta | own | 32000 | reversal | reversal | 746 |
| delta | own | 32000 | reversal | unresolved | 128 |
| delta | own | 32000 | unresolved | unresolved | 881 |
| delta | own | 8000 | negligible | negligible | 31 |
| delta | own | 8000 | negligible | unresolved | 1 |
| delta | own | 8000 | reversal | reversal | 81 |
| delta | own | 8000 | reversal | unresolved | 10 |
| delta | own | 8000 | unresolved | unresolved | 87 |
| delta | own | missed | dominance_positive | dominance_positive | 10 |
| delta | own | missed | dominance_positive | unresolved | 54 |
| delta | own | missed | negligible | negligible | 417 |
| delta | own | missed | negligible | unresolved | 21 |
| delta | own | missed | reversal | reversal | 1026 |
| delta | own | missed | reversal | unresolved | 130 |
| delta | own | missed | unresolved | unresolved | 930 |
| new | actual | 2000 | dominance_positive | dominance_positive | 2 |
| new | actual | 2000 | negligible | negligible | 3 |
| new | actual | 2000 | reversal | reversal | 5 |
| new | actual | 2000 | unresolved | unresolved | 2 |
| new | actual | 32000 | dominance_positive | dominance_positive | 700 |
| new | actual | 32000 | dominance_positive | unresolved | 99 |
| new | actual | 32000 | negligible | dominance_positive | 16 |
| new | actual | 32000 | negligible | negligible | 467 |
| new | actual | 32000 | negligible | unresolved | 36 |
| new | actual | 32000 | reversal | reversal | 211 |
| new | actual | 32000 | reversal | unresolved | 49 |
| new | actual | 32000 | unresolved | unresolved | 508 |
| new | actual | 8000 | dominance_positive | dominance_positive | 66 |
| new | actual | 8000 | dominance_positive | unresolved | 14 |
| new | actual | 8000 | negligible | dominance_positive | 1 |
| new | actual | 8000 | negligible | negligible | 54 |
| new | actual | 8000 | negligible | unresolved | 1 |
| new | actual | 8000 | reversal | reversal | 26 |
| new | actual | 8000 | reversal | unresolved | 1 |
| new | actual | 8000 | unresolved | unresolved | 47 |
| new | actual | missed | dominance_positive | dominance_positive | 901 |
| new | actual | missed | dominance_positive | unresolved | 126 |
| new | actual | missed | negligible | dominance_positive | 15 |
| new | actual | missed | negligible | negligible | 729 |
| new | actual | missed | negligible | unresolved | 53 |
| new | actual | missed | reversal | reversal | 236 |
| new | actual | missed | reversal | unresolved | 47 |
| new | actual | missed | unresolved | unresolved | 481 |
| new | own | 2000 | dominance_positive | dominance_positive | 2 |
| new | own | 2000 | reversal | reversal | 4 |
| new | own | 2000 | unresolved | unresolved | 6 |
| new | own | 32000 | dominance_positive | dominance_positive | 821 |
| new | own | 32000 | dominance_positive | unresolved | 79 |
| new | own | 32000 | negligible | dominance_positive | 22 |
| new | own | 32000 | negligible | negligible | 180 |
| new | own | 32000 | negligible | unresolved | 8 |
| new | own | 32000 | reversal | reversal | 212 |
| new | own | 32000 | reversal | unresolved | 16 |
| new | own | 32000 | unresolved | unresolved | 748 |
| new | own | 8000 | dominance_positive | dominance_positive | 89 |
| new | own | 8000 | dominance_positive | unresolved | 11 |
| new | own | 8000 | negligible | dominance_positive | 1 |
| new | own | 8000 | negligible | negligible | 19 |
| new | own | 8000 | reversal | reversal | 26 |
| new | own | 8000 | reversal | unresolved | 1 |
| new | own | 8000 | unresolved | unresolved | 63 |
| new | own | missed | dominance_positive | dominance_positive | 1074 |
| new | own | missed | dominance_positive | unresolved | 103 |
| new | own | missed | negligible | dominance_positive | 24 |
| new | own | missed | negligible | negligible | 393 |
| new | own | missed | negligible | unresolved | 12 |
| new | own | missed | reversal | reversal | 213 |
| new | own | missed | reversal | unresolved | 23 |
| new | own | missed | unresolved | unresolved | 746 |
| old | actual | 2000 | negligible | negligible | 3 |
| old | actual | 2000 | reversal | reversal | 1 |
| old | actual | 2000 | unresolved | unresolved | 8 |
| old | actual | 32000 | dominance_positive | dominance_positive | 772 |
| old | actual | 32000 | dominance_positive | unresolved | 221 |
| old | actual | 32000 | negligible | dominance_positive | 3 |
| old | actual | 32000 | negligible | negligible | 416 |
| old | actual | 32000 | negligible | unresolved | 5 |
| old | actual | 32000 | reversal | reversal | 31 |
| old | actual | 32000 | reversal | unresolved | 18 |
| old | actual | 32000 | unresolved | unresolved | 620 |
| old | actual | 8000 | dominance_positive | dominance_positive | 74 |
| old | actual | 8000 | dominance_positive | unresolved | 18 |
| old | actual | 8000 | negligible | negligible | 47 |
| old | actual | 8000 | reversal | reversal | 3 |
| old | actual | 8000 | unresolved | unresolved | 68 |
| old | actual | missed | dominance_positive | dominance_positive | 1060 |
| old | actual | missed | dominance_positive | unresolved | 232 |
| old | actual | missed | negligible | dominance_positive | 13 |
| old | actual | missed | negligible | negligible | 566 |
| old | actual | missed | negligible | unresolved | 17 |
| old | actual | missed | reversal | reversal | 53 |
| old | actual | missed | reversal | unresolved | 27 |
| old | actual | missed | unresolved | unresolved | 620 |
| old | own | 2000 | unresolved | unresolved | 12 |
| old | own | 32000 | dominance_positive | dominance_positive | 973 |
| old | own | 32000 | dominance_positive | unresolved | 232 |
| old | own | 32000 | negligible | negligible | 25 |
| old | own | 32000 | negligible | unresolved | 3 |
| old | own | 32000 | unresolved | unresolved | 853 |
| old | own | 8000 | dominance_positive | dominance_positive | 84 |
| old | own | 8000 | dominance_positive | unresolved | 23 |
| old | own | 8000 | negligible | negligible | 3 |
| old | own | 8000 | unresolved | unresolved | 100 |
| old | own | missed | dominance_positive | dominance_positive | 1406 |
| old | own | missed | dominance_positive | unresolved | 200 |
| old | own | missed | negligible | dominance_positive | 3 |
| old | own | missed | negligible | negligible | 66 |
| old | own | missed | negligible | unresolved | 6 |
| old | own | missed | unresolved | unresolved | 907 |

## T5_0d_band_width

| rule | portfolio | measure | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| old | actual | band_ratio | 4896 | 88892374569.7559 | 0.2870 | 2.2381 | 15.3657 | 128819.7485 |
| old | actual | band_ratio_pm | 4896 | 355569468809.4250 | 1.1271 | 8.8081 | 59.4943 | 510613.2968 |
| old | own | band_ratio | 4896 | 16718769500.1688 | 2.3637 | 3.6173 | 76012.0401 | 174088.7002 |
| old | own | band_ratio_pm | 4896 | 66874824354.8681 | 9.2841 | 14.1968 | 304048.1606 | 687073.9209 |
| new | actual | band_ratio | 4896 | 239817.6881 | 0.1039 | 0.9411 | 3.2149 | 163625.3585 |
| new | actual | band_ratio_pm | 4896 | 923538.4806 | 0.3870 | 3.6772 | 12.6508 | 653482.2167 |
| new | own | band_ratio | 4896 | 451119.1420 | 0.4034 | 2.9261 | 96643.1912 | 261589.9267 |
| new | own | band_ratio_pm | 4896 | 1738275.4284 | 1.5551 | 11.6093 | 386572.7646 | 1033705.6477 |
| delta | actual | band_ratio | 4896 | 22547733688.4224 | 0.0997 | 1.1089 | 3.3049 | 71380.9875 |
| delta | actual | band_ratio_pm | 4896 | 90190898872.3389 | 0.3861 | 4.2946 | 12.6199 | 284551.2632 |
| delta | own | band_ratio | 4896 | 265131.2117 | 0.5874 | 2.5571 | 46821.8174 | 111196.2799 |
| delta | own | band_ratio_pm | 4896 | 1015776.5008 | 2.3146 | 9.9973 | 187052.4293 | 440428.2623 |

## T5_1_verdicts

| rule | portfolio | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|
| old | actual | B | dominance_positive | 0.4855 | 0.4301 | 0.5396 | 4896 |
| old | actual | B | reversal | 0.0272 | 0.0139 | 0.0483 | 4896 |
| old | actual | B | negligible | 0.2185 | 0.1551 | 0.2718 | 4896 |
| old | actual | B | unresolved | 0.2688 | 0.2376 | 0.3074 | 4896 |
| old | actual | C | dominance_positive | 0.4857 | 0.4304 | 0.5401 | 4896 |
| old | actual | C | reversal | 0.0272 | 0.0139 | 0.0483 | 4896 |
| old | actual | C | negligible | 0.2185 | 0.1551 | 0.2718 | 4896 |
| old | actual | C | unresolved | 0.2686 | 0.2376 | 0.3068 | 4896 |
| old | actual | B_pm | dominance_positive | 0.3926 | 0.3423 | 0.4491 | 4896 |
| old | actual | B_pm | reversal | 0.0180 | 0.0084 | 0.0326 | 4896 |
| old | actual | B_pm | negligible | 0.2108 | 0.1509 | 0.2630 | 4896 |
| old | actual | B_pm | unresolved | 0.3787 | 0.3479 | 0.4095 | 4896 |
| old | actual | C_pm | dominance_positive | 0.3926 | 0.3423 | 0.4491 | 4896 |
| old | actual | C_pm | reversal | 0.0180 | 0.0084 | 0.0326 | 4896 |
| old | actual | C_pm | negligible | 0.2108 | 0.1509 | 0.2630 | 4896 |
| old | actual | C_pm | unresolved | 0.3787 | 0.3479 | 0.4095 | 4896 |
| old | own | B | dominance_positive | 0.5960 | 0.5547 | 0.6355 | 4896 |
| old | own | B | reversal | 0.0000 | 0.0000 | 0.0000 | 4896 |
| old | own | B | negligible | 0.0217 | 0.0089 | 0.0373 | 4896 |
| old | own | B | unresolved | 0.3824 | 0.3378 | 0.4313 | 4896 |
| old | own | C | dominance_positive | 0.5962 | 0.5549 | 0.6359 | 4896 |
| old | own | C | reversal | 0.0000 | 0.0000 | 0.0000 | 4896 |
| old | own | C | negligible | 0.0217 | 0.0089 | 0.0373 | 4896 |
| old | own | C | unresolved | 0.3821 | 0.3378 | 0.4312 | 4896 |
| old | own | B_pm | dominance_positive | 0.5037 | 0.4567 | 0.5482 | 4896 |
| old | own | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 4896 |
| old | own | B_pm | negligible | 0.0192 | 0.0078 | 0.0332 | 4896 |
| old | own | B_pm | unresolved | 0.4771 | 0.4304 | 0.5267 | 4896 |
| old | own | C_pm | dominance_positive | 0.5039 | 0.4567 | 0.5486 | 4896 |
| old | own | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 4896 |
| old | own | C_pm | negligible | 0.0192 | 0.0078 | 0.0332 | 4896 |
| old | own | C_pm | unresolved | 0.4769 | 0.4303 | 0.5267 | 4896 |
| new | actual | B | dominance_positive | 0.3897 | 0.3307 | 0.4398 | 4896 |
| new | actual | B | reversal | 0.1174 | 0.0691 | 0.1512 | 4896 |
| new | actual | B | negligible | 0.2808 | 0.1964 | 0.3507 | 4896 |
| new | actual | B | unresolved | 0.2120 | 0.1629 | 0.2615 | 4896 |
| new | actual | C | dominance_positive | 0.3901 | 0.3307 | 0.4406 | 4896 |
| new | actual | C | reversal | 0.1172 | 0.0691 | 0.1508 | 4896 |
| new | actual | C | negligible | 0.2808 | 0.1964 | 0.3507 | 4896 |
| new | actual | C | unresolved | 0.2118 | 0.1629 | 0.2610 | 4896 |
| new | actual | B_pm | dominance_positive | 0.3474 | 0.2863 | 0.3985 | 4896 |
| new | actual | B_pm | reversal | 0.0976 | 0.0573 | 0.1222 | 4896 |
| new | actual | B_pm | negligible | 0.2559 | 0.1801 | 0.3247 | 4896 |
| new | actual | B_pm | unresolved | 0.2990 | 0.2445 | 0.3481 | 4896 |
| new | actual | C_pm | dominance_positive | 0.3480 | 0.2864 | 0.4002 | 4896 |
| new | actual | C_pm | reversal | 0.0976 | 0.0573 | 0.1222 | 4896 |
| new | actual | C_pm | negligible | 0.2559 | 0.1801 | 0.3247 | 4896 |
| new | actual | C_pm | unresolved | 0.2984 | 0.2444 | 0.3474 | 4896 |
| new | own | B | dominance_positive | 0.4451 | 0.4028 | 0.4814 | 4896 |
| new | own | B | reversal | 0.1011 | 0.0533 | 0.1436 | 4896 |
| new | own | B | negligible | 0.1346 | 0.0815 | 0.1761 | 4896 |
| new | own | B | unresolved | 0.3192 | 0.2720 | 0.3715 | 4896 |
| new | own | C | dominance_positive | 0.4453 | 0.4029 | 0.4816 | 4896 |
| new | own | C | reversal | 0.1011 | 0.0533 | 0.1436 | 4896 |
| new | own | C | negligible | 0.1346 | 0.0815 | 0.1761 | 4896 |
| new | own | C | unresolved | 0.3190 | 0.2713 | 0.3714 | 4896 |
| new | own | B_pm | dominance_positive | 0.4152 | 0.3675 | 0.4562 | 4896 |
| new | own | B_pm | reversal | 0.0929 | 0.0481 | 0.1352 | 4896 |
| new | own | B_pm | negligible | 0.1209 | 0.0708 | 0.1621 | 4896 |
| new | own | B_pm | unresolved | 0.3709 | 0.3190 | 0.4256 | 4896 |
| new | own | C_pm | dominance_positive | 0.4154 | 0.3675 | 0.4564 | 4896 |
| new | own | C_pm | reversal | 0.0929 | 0.0481 | 0.1352 | 4896 |
| new | own | C_pm | negligible | 0.1209 | 0.0708 | 0.1621 | 4896 |
| new | own | C_pm | unresolved | 0.3707 | 0.3184 | 0.4252 | 4896 |
| delta | actual | B | dominance_positive | 0.0927 | 0.0564 | 0.1255 | 4896 |
| delta | actual | B | reversal | 0.4050 | 0.3748 | 0.4340 | 4896 |
| delta | actual | B | negligible | 0.2686 | 0.2309 | 0.3109 | 4896 |
| delta | actual | B | unresolved | 0.2337 | 0.1899 | 0.2777 | 4896 |
| delta | actual | C | dominance_positive | 0.0927 | 0.0564 | 0.1255 | 4896 |
| delta | actual | C | reversal | 0.4052 | 0.3748 | 0.4342 | 4896 |
| delta | actual | C | negligible | 0.2686 | 0.2309 | 0.3109 | 4896 |
| delta | actual | C | unresolved | 0.2335 | 0.1893 | 0.2777 | 4896 |
| delta | actual | B_pm | dominance_positive | 0.0625 | 0.0336 | 0.0926 | 4896 |
| delta | actual | B_pm | reversal | 0.3611 | 0.3346 | 0.3866 | 4896 |
| delta | actual | B_pm | negligible | 0.2563 | 0.2185 | 0.2927 | 4896 |
| delta | actual | B_pm | unresolved | 0.3201 | 0.2787 | 0.3565 | 4896 |
| delta | actual | C_pm | dominance_positive | 0.0625 | 0.0336 | 0.0926 | 4896 |
| delta | actual | C_pm | reversal | 0.3613 | 0.3347 | 0.3871 | 4896 |
| delta | actual | C_pm | negligible | 0.2563 | 0.2185 | 0.2927 | 4896 |
| delta | actual | C_pm | unresolved | 0.3199 | 0.2778 | 0.3565 | 4896 |
| delta | own | B | dominance_positive | 0.0235 | 0.0166 | 0.0307 | 4896 |
| delta | own | B | reversal | 0.4346 | 0.3888 | 0.4706 | 4896 |
| delta | own | B | negligible | 0.1534 | 0.1203 | 0.1869 | 4896 |
| delta | own | B | unresolved | 0.3885 | 0.3335 | 0.4345 | 4896 |
| delta | own | C | dominance_positive | 0.0235 | 0.0166 | 0.0307 | 4896 |
| delta | own | C | reversal | 0.4346 | 0.3888 | 0.4706 | 4896 |
| delta | own | C | negligible | 0.1534 | 0.1203 | 0.1869 | 4896 |
| delta | own | C | unresolved | 0.3885 | 0.3335 | 0.4345 | 4896 |
| delta | own | B_pm | dominance_positive | 0.0025 | 0.0004 | 0.0056 | 4896 |
| delta | own | B_pm | reversal | 0.3799 | 0.3272 | 0.4161 | 4896 |
| delta | own | B_pm | negligible | 0.1452 | 0.1133 | 0.1786 | 4896 |
| delta | own | B_pm | unresolved | 0.4724 | 0.4290 | 0.5157 | 4896 |
| delta | own | C_pm | dominance_positive | 0.0025 | 0.0004 | 0.0056 | 4896 |
| delta | own | C_pm | reversal | 0.3799 | 0.3272 | 0.4161 | 4896 |
| delta | own | C_pm | negligible | 0.1452 | 0.1133 | 0.1786 | 4896 |
| delta | own | C_pm | unresolved | 0.4724 | 0.4290 | 0.5157 | 4896 |

## T5_2_verdicts_by_band

| rule | portfolio | band | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| old | actual | 1-3 | B | dominance_positive | 0.5253 | 0.3622 | 0.6909 | 495 |
| old | actual | 1-3 | B | reversal | 0.0263 | 0.0040 | 0.0598 | 495 |
| old | actual | 1-3 | B | negligible | 0.0687 | 0.0020 | 0.1593 | 495 |
| old | actual | 1-3 | B | unresolved | 0.3798 | 0.1926 | 0.4980 | 495 |
| old | actual | 1-3 | C | dominance_positive | 0.5273 | 0.3688 | 0.6909 | 495 |
| old | actual | 1-3 | C | reversal | 0.0263 | 0.0040 | 0.0598 | 495 |
| old | actual | 1-3 | C | negligible | 0.0687 | 0.0020 | 0.1593 | 495 |
| old | actual | 1-3 | C | unresolved | 0.3778 | 0.1913 | 0.4959 | 495 |
| old | actual | 1-3 | B_pm | dominance_positive | 0.4040 | 0.2409 | 0.5278 | 495 |
| old | actual | 1-3 | B_pm | reversal | 0.0202 | 0.0021 | 0.0453 | 495 |
| old | actual | 1-3 | B_pm | negligible | 0.0687 | 0.0020 | 0.1593 | 495 |
| old | actual | 1-3 | B_pm | unresolved | 0.5071 | 0.3838 | 0.6191 | 495 |
| old | actual | 1-3 | C_pm | dominance_positive | 0.4040 | 0.2409 | 0.5278 | 495 |
| old | actual | 1-3 | C_pm | reversal | 0.0202 | 0.0021 | 0.0453 | 495 |
| old | actual | 1-3 | C_pm | negligible | 0.0687 | 0.0020 | 0.1593 | 495 |
| old | actual | 1-3 | C_pm | unresolved | 0.5071 | 0.3838 | 0.6191 | 495 |
| old | actual | 4-10 | B | dominance_positive | 0.5742 | 0.5206 | 0.6270 | 1146 |
| old | actual | 4-10 | B | reversal | 0.0349 | 0.0124 | 0.0656 | 1146 |
| old | actual | 4-10 | B | negligible | 0.0733 | 0.0226 | 0.1311 | 1146 |
| old | actual | 4-10 | B | unresolved | 0.3176 | 0.2633 | 0.3746 | 1146 |
| old | actual | 4-10 | C | dominance_positive | 0.5742 | 0.5206 | 0.6270 | 1146 |
| old | actual | 4-10 | C | reversal | 0.0349 | 0.0124 | 0.0656 | 1146 |
| old | actual | 4-10 | C | negligible | 0.0733 | 0.0226 | 0.1311 | 1146 |
| old | actual | 4-10 | C | unresolved | 0.3176 | 0.2633 | 0.3746 | 1146 |
| old | actual | 4-10 | B_pm | dominance_positive | 0.4572 | 0.3637 | 0.5562 | 1146 |
| old | actual | 4-10 | B_pm | reversal | 0.0201 | 0.0051 | 0.0411 | 1146 |
| old | actual | 4-10 | B_pm | negligible | 0.0724 | 0.0215 | 0.1308 | 1146 |
| old | actual | 4-10 | B_pm | unresolved | 0.4503 | 0.3819 | 0.5126 | 1146 |
| old | actual | 4-10 | C_pm | dominance_positive | 0.4572 | 0.3637 | 0.5562 | 1146 |
| old | actual | 4-10 | C_pm | reversal | 0.0201 | 0.0051 | 0.0411 | 1146 |
| old | actual | 4-10 | C_pm | negligible | 0.0724 | 0.0215 | 0.1308 | 1146 |
| old | actual | 4-10 | C_pm | unresolved | 0.4503 | 0.3819 | 0.5126 | 1146 |
| old | actual | 11-16 | B | dominance_positive | 0.4519 | 0.3788 | 0.5329 | 978 |
| old | actual | 11-16 | B | reversal | 0.0225 | 0.0011 | 0.0585 | 978 |
| old | actual | 11-16 | B | negligible | 0.1677 | 0.0809 | 0.2720 | 978 |
| old | actual | 11-16 | B | unresolved | 0.3579 | 0.2535 | 0.4826 | 978 |
| old | actual | 11-16 | C | dominance_positive | 0.4519 | 0.3788 | 0.5329 | 978 |
| old | actual | 11-16 | C | reversal | 0.0225 | 0.0011 | 0.0585 | 978 |
| old | actual | 11-16 | C | negligible | 0.1677 | 0.0809 | 0.2720 | 978 |
| old | actual | 11-16 | C | unresolved | 0.3579 | 0.2535 | 0.4826 | 978 |
| old | actual | 11-16 | B_pm | dominance_positive | 0.3967 | 0.3265 | 0.4705 | 978 |
| old | actual | 11-16 | B_pm | reversal | 0.0123 | 0.0000 | 0.0273 | 978 |
| old | actual | 11-16 | B_pm | negligible | 0.1595 | 0.0782 | 0.2621 | 978 |
| old | actual | 11-16 | B_pm | unresolved | 0.4315 | 0.3483 | 0.5273 | 978 |
| old | actual | 11-16 | C_pm | dominance_positive | 0.3967 | 0.3265 | 0.4705 | 978 |
| old | actual | 11-16 | C_pm | reversal | 0.0123 | 0.0000 | 0.0273 | 978 |
| old | actual | 11-16 | C_pm | negligible | 0.1595 | 0.0782 | 0.2621 | 978 |
| old | actual | 11-16 | C_pm | unresolved | 0.4315 | 0.3483 | 0.5273 | 978 |
| old | actual | 17-30 | B | dominance_positive | 0.4466 | 0.2993 | 0.5883 | 2277 |
| old | actual | 17-30 | B | reversal | 0.0255 | 0.0046 | 0.0620 | 2277 |
| old | actual | 17-30 | B | negligible | 0.3461 | 0.2280 | 0.4760 | 2277 |
| old | actual | 17-30 | B | unresolved | 0.1818 | 0.1490 | 0.2223 | 2277 |
| old | actual | 17-30 | C | dominance_positive | 0.4466 | 0.2993 | 0.5883 | 2277 |
| old | actual | 17-30 | C | reversal | 0.0255 | 0.0046 | 0.0620 | 2277 |
| old | actual | 17-30 | C | negligible | 0.3461 | 0.2280 | 0.4760 | 2277 |
| old | actual | 17-30 | C | unresolved | 0.1818 | 0.1490 | 0.2223 | 2277 |
| old | actual | 17-30 | B_pm | dominance_positive | 0.3557 | 0.2137 | 0.5017 | 2277 |
| old | actual | 17-30 | B_pm | reversal | 0.0189 | 0.0017 | 0.0484 | 2277 |
| old | actual | 17-30 | B_pm | negligible | 0.3333 | 0.2173 | 0.4620 | 2277 |
| old | actual | 17-30 | B_pm | unresolved | 0.2921 | 0.2487 | 0.3404 | 2277 |
| old | actual | 17-30 | C_pm | dominance_positive | 0.3557 | 0.2137 | 0.5017 | 2277 |
| old | actual | 17-30 | C_pm | reversal | 0.0189 | 0.0017 | 0.0484 | 2277 |
| old | actual | 17-30 | C_pm | negligible | 0.3333 | 0.2173 | 0.4620 | 2277 |
| old | actual | 17-30 | C_pm | unresolved | 0.2921 | 0.2487 | 0.3404 | 2277 |
| old | own | 1-3 | B | dominance_positive | 0.7172 | 0.5936 | 0.8340 | 495 |
| old | own | 1-3 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 495 |
| old | own | 1-3 | B | negligible | 0.0202 | 0.0020 | 0.0475 | 495 |
| old | own | 1-3 | B | unresolved | 0.2626 | 0.1498 | 0.3829 | 495 |
| old | own | 1-3 | C | dominance_positive | 0.7172 | 0.5936 | 0.8340 | 495 |
| old | own | 1-3 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 495 |
| old | own | 1-3 | C | negligible | 0.0202 | 0.0020 | 0.0475 | 495 |
| old | own | 1-3 | C | unresolved | 0.2626 | 0.1498 | 0.3829 | 495 |
| old | own | 1-3 | B_pm | dominance_positive | 0.6162 | 0.4329 | 0.7778 | 495 |
| old | own | 1-3 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 495 |
| old | own | 1-3 | B_pm | negligible | 0.0182 | 0.0000 | 0.0466 | 495 |
| old | own | 1-3 | B_pm | unresolved | 0.3657 | 0.2032 | 0.5379 | 495 |
| old | own | 1-3 | C_pm | dominance_positive | 0.6162 | 0.4329 | 0.7778 | 495 |
| old | own | 1-3 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 495 |
| old | own | 1-3 | C_pm | negligible | 0.0182 | 0.0000 | 0.0466 | 495 |
| old | own | 1-3 | C_pm | unresolved | 0.3657 | 0.2032 | 0.5379 | 495 |
| old | own | 4-10 | B | dominance_positive | 0.5960 | 0.4416 | 0.7452 | 1146 |
| old | own | 4-10 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 1146 |
| old | own | 4-10 | B | negligible | 0.0218 | 0.0027 | 0.0515 | 1146 |
| old | own | 4-10 | B | unresolved | 0.3822 | 0.2463 | 0.5262 | 1146 |
| old | own | 4-10 | C | dominance_positive | 0.5960 | 0.4416 | 0.7452 | 1146 |
| old | own | 4-10 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 1146 |
| old | own | 4-10 | C | negligible | 0.0218 | 0.0027 | 0.0515 | 1146 |
| old | own | 4-10 | C | unresolved | 0.3822 | 0.2463 | 0.5262 | 1146 |
| old | own | 4-10 | B_pm | dominance_positive | 0.5305 | 0.3812 | 0.6895 | 1146 |
| old | own | 4-10 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 1146 |
| old | own | 4-10 | B_pm | negligible | 0.0201 | 0.0026 | 0.0476 | 1146 |
| old | own | 4-10 | B_pm | unresolved | 0.4494 | 0.3021 | 0.5910 | 1146 |
| old | own | 4-10 | C_pm | dominance_positive | 0.5305 | 0.3812 | 0.6895 | 1146 |
| old | own | 4-10 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 1146 |
| old | own | 4-10 | C_pm | negligible | 0.0201 | 0.0026 | 0.0476 | 1146 |
| old | own | 4-10 | C_pm | unresolved | 0.4494 | 0.3021 | 0.5910 | 1146 |
| old | own | 11-16 | B | dominance_positive | 0.3681 | 0.2996 | 0.4369 | 978 |
| old | own | 11-16 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 978 |
| old | own | 11-16 | B | negligible | 0.0041 | 0.0000 | 0.0125 | 978 |
| old | own | 11-16 | B | unresolved | 0.6278 | 0.5574 | 0.6981 | 978 |
| old | own | 11-16 | C | dominance_positive | 0.3681 | 0.2996 | 0.4369 | 978 |
| old | own | 11-16 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 978 |
| old | own | 11-16 | C | negligible | 0.0041 | 0.0000 | 0.0125 | 978 |
| old | own | 11-16 | C | unresolved | 0.6278 | 0.5574 | 0.6981 | 978 |
| old | own | 11-16 | B_pm | dominance_positive | 0.3119 | 0.2549 | 0.3762 | 978 |
| old | own | 11-16 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 978 |
| old | own | 11-16 | B_pm | negligible | 0.0031 | 0.0000 | 0.0095 | 978 |
| old | own | 11-16 | B_pm | unresolved | 0.6851 | 0.6203 | 0.7431 | 978 |
| old | own | 11-16 | C_pm | dominance_positive | 0.3119 | 0.2549 | 0.3762 | 978 |
| old | own | 11-16 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 978 |
| old | own | 11-16 | C_pm | negligible | 0.0031 | 0.0000 | 0.0095 | 978 |
| old | own | 11-16 | C_pm | unresolved | 0.6851 | 0.6203 | 0.7431 | 978 |
| old | own | 17-30 | B | dominance_positive | 0.6675 | 0.6164 | 0.7122 | 2277 |
| old | own | 17-30 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 2277 |
| old | own | 17-30 | B | negligible | 0.0294 | 0.0055 | 0.0603 | 2277 |
| old | own | 17-30 | B | unresolved | 0.3030 | 0.2554 | 0.3542 | 2277 |
| old | own | 17-30 | C | dominance_positive | 0.6680 | 0.6164 | 0.7131 | 2277 |
| old | own | 17-30 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 2277 |
| old | own | 17-30 | C | negligible | 0.0294 | 0.0055 | 0.0603 | 2277 |
| old | own | 17-30 | C | unresolved | 0.3026 | 0.2550 | 0.3542 | 2277 |
| old | own | 17-30 | B_pm | dominance_positive | 0.5481 | 0.4753 | 0.6102 | 2277 |
| old | own | 17-30 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 2277 |
| old | own | 17-30 | B_pm | negligible | 0.0259 | 0.0050 | 0.0524 | 2277 |
| old | own | 17-30 | B_pm | unresolved | 0.4260 | 0.3715 | 0.4848 | 2277 |
| old | own | 17-30 | C_pm | dominance_positive | 0.5485 | 0.4753 | 0.6110 | 2277 |
| old | own | 17-30 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 2277 |
| old | own | 17-30 | C_pm | negligible | 0.0259 | 0.0050 | 0.0524 | 2277 |
| old | own | 17-30 | C_pm | unresolved | 0.4256 | 0.3704 | 0.4848 | 2277 |
| new | actual | 1-3 | B | dominance_positive | 0.0848 | 0.0271 | 0.1784 | 495 |
| new | actual | 1-3 | B | reversal | 0.5273 | 0.2915 | 0.7327 | 495 |
| new | actual | 1-3 | B | negligible | 0.2162 | 0.0893 | 0.3599 | 495 |
| new | actual | 1-3 | B | unresolved | 0.1717 | 0.0854 | 0.2783 | 495 |
| new | actual | 1-3 | C | dominance_positive | 0.0848 | 0.0271 | 0.1784 | 495 |
| new | actual | 1-3 | C | reversal | 0.5273 | 0.2915 | 0.7327 | 495 |
| new | actual | 1-3 | C | negligible | 0.2162 | 0.0893 | 0.3599 | 495 |
| new | actual | 1-3 | C | unresolved | 0.1717 | 0.0854 | 0.2783 | 495 |
| new | actual | 1-3 | B_pm | dominance_positive | 0.0545 | 0.0126 | 0.1165 | 495 |
| new | actual | 1-3 | B_pm | reversal | 0.4545 | 0.2528 | 0.6225 | 495 |
| new | actual | 1-3 | B_pm | negligible | 0.1737 | 0.0639 | 0.2994 | 495 |
| new | actual | 1-3 | B_pm | unresolved | 0.3172 | 0.2176 | 0.4208 | 495 |
| new | actual | 1-3 | C_pm | dominance_positive | 0.0545 | 0.0126 | 0.1165 | 495 |
| new | actual | 1-3 | C_pm | reversal | 0.4545 | 0.2528 | 0.6225 | 495 |
| new | actual | 1-3 | C_pm | negligible | 0.1737 | 0.0639 | 0.2994 | 495 |
| new | actual | 1-3 | C_pm | unresolved | 0.3172 | 0.2176 | 0.4208 | 495 |
| new | actual | 4-10 | B | dominance_positive | 0.2853 | 0.1404 | 0.4118 | 1146 |
| new | actual | 4-10 | B | reversal | 0.1937 | 0.1105 | 0.2617 | 1146 |
| new | actual | 4-10 | B | negligible | 0.2792 | 0.1518 | 0.3978 | 1146 |
| new | actual | 4-10 | B | unresolved | 0.2417 | 0.1519 | 0.3272 | 1146 |
| new | actual | 4-10 | C | dominance_positive | 0.2853 | 0.1404 | 0.4118 | 1146 |
| new | actual | 4-10 | C | reversal | 0.1937 | 0.1105 | 0.2617 | 1146 |
| new | actual | 4-10 | C | negligible | 0.2792 | 0.1518 | 0.3978 | 1146 |
| new | actual | 4-10 | C | unresolved | 0.2417 | 0.1519 | 0.3272 | 1146 |
| new | actual | 4-10 | B_pm | dominance_positive | 0.2496 | 0.0918 | 0.3896 | 1146 |
| new | actual | 4-10 | B_pm | reversal | 0.1597 | 0.0973 | 0.2100 | 1146 |
| new | actual | 4-10 | B_pm | negligible | 0.2304 | 0.1257 | 0.3149 | 1146 |
| new | actual | 4-10 | B_pm | unresolved | 0.3604 | 0.2688 | 0.4571 | 1146 |
| new | actual | 4-10 | C_pm | dominance_positive | 0.2496 | 0.0918 | 0.3896 | 1146 |
| new | actual | 4-10 | C_pm | reversal | 0.1597 | 0.0973 | 0.2100 | 1146 |
| new | actual | 4-10 | C_pm | negligible | 0.2304 | 0.1257 | 0.3149 | 1146 |
| new | actual | 4-10 | C_pm | unresolved | 0.3604 | 0.2688 | 0.4571 | 1146 |
| new | actual | 11-16 | B | dominance_positive | 0.4356 | 0.3736 | 0.5045 | 978 |
| new | actual | 11-16 | B | reversal | 0.0102 | 0.0000 | 0.0274 | 978 |
| new | actual | 11-16 | B | negligible | 0.2362 | 0.1135 | 0.3591 | 978 |
| new | actual | 11-16 | B | unresolved | 0.3180 | 0.1931 | 0.4552 | 978 |
| new | actual | 11-16 | C | dominance_positive | 0.4356 | 0.3736 | 0.5045 | 978 |
| new | actual | 11-16 | C | reversal | 0.0102 | 0.0000 | 0.0274 | 978 |
| new | actual | 11-16 | C | negligible | 0.2362 | 0.1135 | 0.3591 | 978 |
| new | actual | 11-16 | C | unresolved | 0.3180 | 0.1931 | 0.4552 | 978 |
| new | actual | 11-16 | B_pm | dominance_positive | 0.3947 | 0.3333 | 0.4633 | 978 |
| new | actual | 11-16 | B_pm | reversal | 0.0072 | 0.0000 | 0.0198 | 978 |
| new | actual | 11-16 | B_pm | negligible | 0.2260 | 0.1108 | 0.3445 | 978 |
| new | actual | 11-16 | B_pm | unresolved | 0.3722 | 0.2686 | 0.4921 | 978 |
| new | actual | 11-16 | C_pm | dominance_positive | 0.3947 | 0.3333 | 0.4633 | 978 |
| new | actual | 11-16 | C_pm | reversal | 0.0072 | 0.0000 | 0.0198 | 978 |
| new | actual | 11-16 | C_pm | negligible | 0.2260 | 0.1108 | 0.3445 | 978 |
| new | actual | 11-16 | C_pm | unresolved | 0.3722 | 0.2686 | 0.4921 | 978 |
| new | actual | 17-30 | B | dominance_positive | 0.4888 | 0.3741 | 0.5929 | 2277 |
| new | actual | 17-30 | B | reversal | 0.0360 | 0.0119 | 0.0635 | 2277 |
| new | actual | 17-30 | B | negligible | 0.3149 | 0.2062 | 0.4353 | 2277 |
| new | actual | 17-30 | B | unresolved | 0.1603 | 0.1292 | 0.1955 | 2277 |
| new | actual | 17-30 | C | dominance_positive | 0.4897 | 0.3741 | 0.5944 | 2277 |
| new | actual | 17-30 | C | reversal | 0.0356 | 0.0119 | 0.0630 | 2277 |
| new | actual | 17-30 | C | negligible | 0.3149 | 0.2062 | 0.4353 | 2277 |
| new | actual | 17-30 | C | unresolved | 0.1599 | 0.1286 | 0.1950 | 2277 |
| new | actual | 17-30 | B_pm | dominance_positive | 0.4401 | 0.3311 | 0.5419 | 2277 |
| new | actual | 17-30 | B_pm | reversal | 0.0277 | 0.0079 | 0.0523 | 2277 |
| new | actual | 17-30 | B_pm | negligible | 0.2995 | 0.1940 | 0.4190 | 2277 |
| new | actual | 17-30 | B_pm | unresolved | 0.2328 | 0.1844 | 0.2938 | 2277 |
| new | actual | 17-30 | C_pm | dominance_positive | 0.4414 | 0.3311 | 0.5444 | 2277 |
| new | actual | 17-30 | C_pm | reversal | 0.0277 | 0.0079 | 0.0523 | 2277 |
| new | actual | 17-30 | C_pm | negligible | 0.2995 | 0.1940 | 0.4190 | 2277 |
| new | actual | 17-30 | C_pm | unresolved | 0.2314 | 0.1836 | 0.2934 | 2277 |
| new | own | 1-3 | B | dominance_positive | 0.0747 | 0.0191 | 0.1491 | 495 |
| new | own | 1-3 | B | reversal | 0.5737 | 0.2998 | 0.8151 | 495 |
| new | own | 1-3 | B | negligible | 0.3030 | 0.1134 | 0.5265 | 495 |
| new | own | 1-3 | B | unresolved | 0.0485 | 0.0205 | 0.0829 | 495 |
| new | own | 1-3 | C | dominance_positive | 0.0747 | 0.0191 | 0.1491 | 495 |
| new | own | 1-3 | C | reversal | 0.5737 | 0.2998 | 0.8151 | 495 |
| new | own | 1-3 | C | negligible | 0.3030 | 0.1134 | 0.5265 | 495 |
| new | own | 1-3 | C | unresolved | 0.0485 | 0.0205 | 0.0829 | 495 |
| new | own | 1-3 | B_pm | dominance_positive | 0.0747 | 0.0140 | 0.1544 | 495 |
| new | own | 1-3 | B_pm | reversal | 0.5253 | 0.2714 | 0.7678 | 495 |
| new | own | 1-3 | B_pm | negligible | 0.2465 | 0.0884 | 0.4505 | 495 |
| new | own | 1-3 | B_pm | unresolved | 0.1535 | 0.0958 | 0.2093 | 495 |
| new | own | 1-3 | C_pm | dominance_positive | 0.0747 | 0.0140 | 0.1544 | 495 |
| new | own | 1-3 | C_pm | reversal | 0.5253 | 0.2714 | 0.7678 | 495 |
| new | own | 1-3 | C_pm | negligible | 0.2465 | 0.0884 | 0.4505 | 495 |
| new | own | 1-3 | C_pm | unresolved | 0.1535 | 0.0958 | 0.2093 | 495 |
| new | own | 4-10 | B | dominance_positive | 0.1841 | 0.0840 | 0.2699 | 1146 |
| new | own | 4-10 | B | reversal | 0.1832 | 0.0918 | 0.2710 | 1146 |
| new | own | 4-10 | B | negligible | 0.3394 | 0.1657 | 0.4996 | 1146 |
| new | own | 4-10 | B | unresolved | 0.2932 | 0.1506 | 0.4701 | 1146 |
| new | own | 4-10 | C | dominance_positive | 0.1841 | 0.0840 | 0.2699 | 1146 |
| new | own | 4-10 | C | reversal | 0.1832 | 0.0918 | 0.2710 | 1146 |
| new | own | 4-10 | C | negligible | 0.3394 | 0.1657 | 0.4996 | 1146 |
| new | own | 4-10 | C | unresolved | 0.2932 | 0.1506 | 0.4701 | 1146 |
| new | own | 4-10 | B_pm | dominance_positive | 0.1894 | 0.0915 | 0.2842 | 1146 |
| new | own | 4-10 | B_pm | reversal | 0.1693 | 0.0843 | 0.2545 | 1146 |
| new | own | 4-10 | B_pm | negligible | 0.3124 | 0.1468 | 0.4693 | 1146 |
| new | own | 4-10 | B_pm | unresolved | 0.3290 | 0.1853 | 0.5070 | 1146 |
| new | own | 4-10 | C_pm | dominance_positive | 0.1894 | 0.0915 | 0.2842 | 1146 |
| new | own | 4-10 | C_pm | reversal | 0.1693 | 0.0843 | 0.2545 | 1146 |
| new | own | 4-10 | C_pm | negligible | 0.3124 | 0.1468 | 0.4693 | 1146 |
| new | own | 4-10 | C_pm | unresolved | 0.3290 | 0.1853 | 0.5070 | 1146 |
| new | own | 11-16 | B | dominance_positive | 0.3436 | 0.2750 | 0.4060 | 978 |
| new | own | 11-16 | B | reversal | 0.0010 | 0.0000 | 0.0064 | 978 |
| new | own | 11-16 | B | negligible | 0.0542 | 0.0199 | 0.0958 | 978 |
| new | own | 11-16 | B | unresolved | 0.6012 | 0.5274 | 0.6762 | 978 |
| new | own | 11-16 | C | dominance_positive | 0.3436 | 0.2750 | 0.4060 | 978 |
| new | own | 11-16 | C | reversal | 0.0010 | 0.0000 | 0.0064 | 978 |
| new | own | 11-16 | C | negligible | 0.0542 | 0.0199 | 0.0958 | 978 |
| new | own | 11-16 | C | unresolved | 0.6012 | 0.5274 | 0.6762 | 978 |
| new | own | 11-16 | B_pm | dominance_positive | 0.3180 | 0.2472 | 0.3843 | 978 |
| new | own | 11-16 | B_pm | reversal | 0.0010 | 0.0000 | 0.0064 | 978 |
| new | own | 11-16 | B_pm | negligible | 0.0542 | 0.0199 | 0.0958 | 978 |
| new | own | 11-16 | B_pm | unresolved | 0.6268 | 0.5490 | 0.7050 | 978 |
| new | own | 11-16 | C_pm | dominance_positive | 0.3180 | 0.2472 | 0.3843 | 978 |
| new | own | 11-16 | C_pm | reversal | 0.0010 | 0.0000 | 0.0064 | 978 |
| new | own | 11-16 | C_pm | negligible | 0.0542 | 0.0199 | 0.0958 | 978 |
| new | own | 11-16 | C_pm | unresolved | 0.6268 | 0.5490 | 0.7050 | 978 |
| new | own | 17-30 | B | dominance_positive | 0.7005 | 0.6555 | 0.7426 | 2277 |
| new | own | 17-30 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 2277 |
| new | own | 17-30 | B | negligible | 0.0294 | 0.0055 | 0.0603 | 2277 |
| new | own | 17-30 | B | unresolved | 0.2701 | 0.2223 | 0.3187 | 2277 |
| new | own | 17-30 | C | dominance_positive | 0.7009 | 0.6556 | 0.7434 | 2277 |
| new | own | 17-30 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 2277 |
| new | own | 17-30 | C | negligible | 0.0294 | 0.0055 | 0.0603 | 2277 |
| new | own | 17-30 | C | unresolved | 0.2697 | 0.2214 | 0.3184 | 2277 |
| new | own | 17-30 | B_pm | dominance_positive | 0.6447 | 0.5919 | 0.6919 | 2277 |
| new | own | 17-30 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 2277 |
| new | own | 17-30 | B_pm | negligible | 0.0259 | 0.0050 | 0.0524 | 2277 |
| new | own | 17-30 | B_pm | unresolved | 0.3294 | 0.2805 | 0.3823 | 2277 |
| new | own | 17-30 | C_pm | dominance_positive | 0.6451 | 0.5919 | 0.6928 | 2277 |
| new | own | 17-30 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 2277 |
| new | own | 17-30 | C_pm | negligible | 0.0259 | 0.0050 | 0.0524 | 2277 |
| new | own | 17-30 | C_pm | unresolved | 0.3289 | 0.2796 | 0.3821 | 2277 |

## T5_3_reversal_slot

| rule | portfolio | jstar | count | count_argmin_C_hat | count_precision_matched | n_reversals | n_reversals_pm |
|---|---|---|---|---|---|---|---|
| old | actual | 1 | 0 | 0 | 0 | 133 | 88 |
| old | actual | 2 | 0 | 0 | 0 | 133 | 88 |
| old | actual | 3 | 0 | 0 | 0 | 133 | 88 |
| old | actual | 4 | 0 | 0 | 0 | 133 | 88 |
| old | actual | 5 | 2 | 2 | 2 | 133 | 88 |
| old | actual | 6 | 1 | 1 | 1 | 133 | 88 |
| old | actual | 7 | 1 | 1 | 1 | 133 | 88 |
| old | actual | 8 | 0 | 0 | 0 | 133 | 88 |
| old | actual | 9 | 3 | 3 | 3 | 133 | 88 |
| old | actual | 10 | 8 | 8 | 5 | 133 | 88 |
| old | actual | 11 | 3 | 3 | 3 | 133 | 88 |
| old | actual | 12 | 1 | 1 | 1 | 133 | 88 |
| old | actual | 13 | 5 | 5 | 3 | 133 | 88 |
| old | actual | 14 | 1 | 3 | 1 | 133 | 88 |
| old | actual | 15 | 5 | 5 | 3 | 133 | 88 |
| old | actual | 16 | 15 | 16 | 8 | 133 | 88 |
| old | actual | 17 | 8 | 7 | 3 | 133 | 88 |
| old | actual | 18 | 7 | 8 | 6 | 133 | 88 |
| old | actual | 19 | 13 | 11 | 5 | 133 | 88 |
| old | actual | 20 | 8 | 8 | 7 | 133 | 88 |
| old | actual | 21 | 4 | 4 | 5 | 133 | 88 |
| old | actual | 22 | 6 | 6 | 2 | 133 | 88 |
| old | actual | 23 | 6 | 6 | 4 | 133 | 88 |
| old | actual | 24 | 3 | 3 | 2 | 133 | 88 |
| old | actual | 25 | 4 | 4 | 3 | 133 | 88 |
| old | actual | 26 | 5 | 6 | 3 | 133 | 88 |
| old | actual | 27 | 15 | 14 | 11 | 133 | 88 |
| old | actual | 28 | 2 | 2 | 3 | 133 | 88 |
| old | actual | 29 | 6 | 6 | 3 | 133 | 88 |
| old | actual | 30 | 1 | 0 | 0 | 133 | 88 |
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
| new | actual | 1 | 0 | 0 | 0 | 575 | 478 |
| new | actual | 2 | 0 | 0 | 0 | 575 | 478 |
| new | actual | 3 | 10 | 10 | 10 | 575 | 478 |
| new | actual | 4 | 21 | 20 | 19 | 575 | 478 |
| new | actual | 5 | 5 | 5 | 4 | 575 | 478 |
| new | actual | 6 | 1 | 2 | 4 | 575 | 478 |
| new | actual | 7 | 10 | 8 | 7 | 575 | 478 |
| new | actual | 8 | 51 | 50 | 19 | 575 | 478 |
| new | actual | 9 | 343 | 346 | 313 | 575 | 478 |
| new | actual | 10 | 1 | 1 | 2 | 575 | 478 |
| new | actual | 11 | 2 | 2 | 0 | 575 | 478 |
| new | actual | 12 | 4 | 4 | 4 | 575 | 478 |
| new | actual | 13 | 1 | 1 | 1 | 575 | 478 |
| new | actual | 14 | 1 | 1 | 1 | 575 | 478 |
| new | actual | 15 | 2 | 2 | 2 | 575 | 478 |
| new | actual | 16 | 2 | 2 | 1 | 575 | 478 |
| new | actual | 17 | 5 | 6 | 3 | 575 | 478 |
| new | actual | 18 | 8 | 7 | 7 | 575 | 478 |
| new | actual | 19 | 8 | 8 | 6 | 575 | 478 |
| new | actual | 20 | 10 | 11 | 8 | 575 | 478 |
| new | actual | 21 | 4 | 3 | 3 | 575 | 478 |
| new | actual | 22 | 7 | 7 | 3 | 575 | 478 |
| new | actual | 23 | 11 | 11 | 11 | 575 | 478 |
| new | actual | 24 | 10 | 10 | 8 | 575 | 478 |
| new | actual | 25 | 6 | 6 | 5 | 575 | 478 |
| new | actual | 26 | 7 | 8 | 6 | 575 | 478 |
| new | actual | 27 | 18 | 16 | 13 | 575 | 478 |
| new | actual | 28 | 6 | 7 | 4 | 575 | 478 |
| new | actual | 29 | 10 | 10 | 6 | 575 | 478 |
| new | actual | 30 | 11 | 11 | 8 | 575 | 478 |
| new | own | 1 | 0 | 0 | 0 | 495 | 455 |
| new | own | 2 | 0 | 0 | 0 | 495 | 455 |
| new | own | 3 | 0 | 0 | 0 | 495 | 455 |
| new | own | 4 | 0 | 0 | 0 | 495 | 455 |
| new | own | 5 | 2 | 2 | 2 | 495 | 455 |
| new | own | 6 | 0 | 0 | 0 | 495 | 455 |
| new | own | 7 | 0 | 0 | 0 | 495 | 455 |
| new | own | 8 | 1 | 1 | 1 | 495 | 455 |
| new | own | 9 | 492 | 492 | 452 | 495 | 455 |
| new | own | 10 | 0 | 0 | 0 | 495 | 455 |
| new | own | 11 | 0 | 0 | 0 | 495 | 455 |
| new | own | 12 | 0 | 0 | 0 | 495 | 455 |
| new | own | 13 | 0 | 0 | 0 | 495 | 455 |
| new | own | 14 | 0 | 0 | 0 | 495 | 455 |
| new | own | 15 | 0 | 0 | 0 | 495 | 455 |
| new | own | 16 | 0 | 0 | 0 | 495 | 455 |
| new | own | 17 | 0 | 0 | 0 | 495 | 455 |
| new | own | 18 | 0 | 0 | 0 | 495 | 455 |
| new | own | 19 | 0 | 0 | 0 | 495 | 455 |
| new | own | 20 | 0 | 0 | 0 | 495 | 455 |
| new | own | 21 | 0 | 0 | 0 | 495 | 455 |
| new | own | 22 | 0 | 0 | 0 | 495 | 455 |
| new | own | 23 | 0 | 0 | 0 | 495 | 455 |
| new | own | 24 | 0 | 0 | 0 | 495 | 455 |
| new | own | 25 | 0 | 0 | 0 | 495 | 455 |
| new | own | 26 | 0 | 0 | 0 | 495 | 455 |
| new | own | 27 | 0 | 0 | 0 | 495 | 455 |
| new | own | 28 | 0 | 0 | 0 | 495 | 455 |
| new | own | 29 | 0 | 0 | 0 | 495 | 455 |
| new | own | 30 | 0 | 0 | 0 | 495 | 455 |

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
| old | actual | 11-16 | linear | 978 | 0.0275 | 0.0061 | 0.0262 | 0.0381 | 0.0532 | 0.7863 | 0.6451 | 0.9075 | 0.0072 | 0.0000 | 0.0244 |
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
| old | own | all | top3_stress | 4896 | 0.0078 | 0.0000 | 0.0026 | 0.0130 | 0.0245 | 0.4922 | 0.4551 | 0.5331 | 0.0000 | 0.0000 | 0.0000 |
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
| new | actual | all | linear | 4896 | 0.0159 | 0.0000 | 0.0034 | 0.0284 | 0.0464 | 0.5161 | 0.4010 | 0.6332 | 0.0584 | 0.0176 | 0.1029 |
| new | actual | all | concave | 4896 | 0.0153 | 0.0000 | 0.0039 | 0.0287 | 0.0418 | 0.5229 | 0.4129 | 0.6252 | 0.0404 | 0.0137 | 0.0695 |
| new | actual | all | convex | 4896 | 0.0136 | 0.0000 | 0.0021 | 0.0220 | 0.0455 | 0.4849 | 0.3852 | 0.5915 | 0.0766 | 0.0355 | 0.1164 |
| new | actual | all | top3_stress | 4896 | 0.0048 | 0.0000 | 0.0000 | 0.0072 | 0.0214 | 0.3305 | 0.2591 | 0.4117 | 0.0915 | 0.0455 | 0.1328 |
| new | actual | 1-3 | linear | 495 | -0.0023 | -0.0029 | -0.0002 | 0.0004 | 0.0019 | 0.0788 | 0.0233 | 0.1489 | 0.2707 | 0.0609 | 0.4788 |
| new | actual | 1-3 | concave | 495 | -0.0013 | -0.0016 | -0.0001 | 0.0006 | 0.0042 | 0.1394 | 0.0296 | 0.2820 | 0.1394 | 0.0167 | 0.2657 |
| new | actual | 1-3 | convex | 495 | -0.0037 | -0.0054 | -0.0012 | -0.0000 | 0.0002 | 0.0404 | 0.0068 | 0.0845 | 0.3859 | 0.1766 | 0.5642 |
| new | actual | 1-3 | top3_stress | 495 | -0.0056 | -0.0093 | -0.0025 | -0.0001 | 0.0000 | 0.0101 | 0.0000 | 0.0394 | 0.5152 | 0.2500 | 0.7531 |
| new | actual | 4-10 | linear | 1146 | 0.0042 | 0.0000 | 0.0008 | 0.0065 | 0.0154 | 0.3595 | 0.1685 | 0.5358 | 0.0969 | 0.0315 | 0.2058 |
| new | actual | 4-10 | concave | 1146 | 0.0038 | 0.0000 | 0.0007 | 0.0053 | 0.0144 | 0.3613 | 0.1911 | 0.5200 | 0.0742 | 0.0255 | 0.1540 |
| new | actual | 4-10 | convex | 1146 | 0.0043 | -0.0001 | 0.0004 | 0.0073 | 0.0178 | 0.3560 | 0.1585 | 0.5438 | 0.1396 | 0.0632 | 0.2280 |
| new | actual | 4-10 | top3_stress | 1146 | 0.0021 | -0.0001 | 0.0000 | 0.0055 | 0.0136 | 0.3211 | 0.1317 | 0.5062 | 0.1579 | 0.0806 | 0.2250 |
| new | actual | 11-16 | linear | 978 | 0.0267 | 0.0001 | 0.0225 | 0.0416 | 0.0560 | 0.7055 | 0.5511 | 0.8617 | 0.0072 | 0.0000 | 0.0219 |
| new | actual | 11-16 | concave | 978 | 0.0209 | 0.0001 | 0.0161 | 0.0298 | 0.0425 | 0.6963 | 0.5369 | 0.8604 | 0.0051 | 0.0000 | 0.0192 |
| new | actual | 11-16 | convex | 978 | 0.0298 | 0.0002 | 0.0261 | 0.0472 | 0.0639 | 0.6984 | 0.5289 | 0.8619 | 0.0072 | 0.0000 | 0.0244 |
| new | actual | 11-16 | top3_stress | 978 | 0.0159 | 0.0000 | 0.0143 | 0.0244 | 0.0346 | 0.6871 | 0.5223 | 0.8521 | 0.0072 | 0.0000 | 0.0306 |
| new | actual | 17-30 | linear | 2277 | 0.0212 | 0.0000 | 0.0160 | 0.0360 | 0.0516 | 0.6087 | 0.4139 | 0.7703 | 0.0149 | 0.0012 | 0.0420 |
| new | actual | 17-30 | concave | 2277 | 0.0224 | 0.0000 | 0.0216 | 0.0357 | 0.0511 | 0.6131 | 0.4204 | 0.7730 | 0.0171 | 0.0013 | 0.0468 |
| new | actual | 17-30 | convex | 2277 | 0.0150 | 0.0000 | 0.0048 | 0.0239 | 0.0440 | 0.5547 | 0.3866 | 0.6821 | 0.0075 | 0.0004 | 0.0176 |
| new | actual | 17-30 | top3_stress | 2277 | 0.0036 | 0.0000 | 0.0000 | 0.0026 | 0.0134 | 0.2516 | 0.1878 | 0.3284 | 0.0022 | 0.0000 | 0.0070 |
| new | own | all | linear | 4896 | 0.0234 | 0.0004 | 0.0178 | 0.0391 | 0.0556 | 0.6953 | 0.6384 | 0.7632 | 0.0437 | 0.0168 | 0.0734 |
| new | own | all | concave | 4896 | 0.0208 | 0.0003 | 0.0208 | 0.0343 | 0.0454 | 0.6850 | 0.6309 | 0.7504 | 0.0094 | 0.0023 | 0.0202 |
| new | own | all | convex | 4896 | 0.0208 | 0.0002 | 0.0101 | 0.0346 | 0.0576 | 0.6422 | 0.5806 | 0.7075 | 0.0709 | 0.0325 | 0.1079 |
| new | own | all | top3_stress | 4896 | 0.0071 | 0.0000 | 0.0006 | 0.0127 | 0.0250 | 0.4306 | 0.3670 | 0.5006 | 0.0882 | 0.0418 | 0.1308 |
| new | own | 1-3 | linear | 495 | -0.0016 | -0.0028 | -0.0008 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.2384 | 0.0811 | 0.4210 |
| new | own | 1-3 | concave | 495 | -0.0008 | -0.0014 | -0.0004 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0424 | 0.0082 | 0.0984 |
| new | own | 1-3 | convex | 495 | -0.0030 | -0.0051 | -0.0015 | -0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.3939 | 0.1750 | 0.6090 |
| new | own | 1-3 | top3_stress | 495 | -0.0055 | -0.0092 | -0.0027 | -0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.4949 | 0.2284 | 0.7403 |
| new | own | 4-10 | linear | 1146 | 0.0037 | -0.0000 | 0.0002 | 0.0053 | 0.0130 | 0.3211 | 0.1356 | 0.5045 | 0.0838 | 0.0348 | 0.1326 |
| new | own | 4-10 | concave | 1146 | 0.0024 | -0.0000 | 0.0001 | 0.0032 | 0.0079 | 0.2705 | 0.1043 | 0.4508 | 0.0218 | 0.0053 | 0.0457 |
| new | own | 4-10 | convex | 1146 | 0.0048 | -0.0000 | 0.0003 | 0.0077 | 0.0181 | 0.3543 | 0.1544 | 0.5428 | 0.1326 | 0.0605 | 0.2005 |
| new | own | 4-10 | top3_stress | 1146 | 0.0027 | -0.0001 | 0.0000 | 0.0071 | 0.0151 | 0.3386 | 0.1521 | 0.5116 | 0.1632 | 0.0774 | 0.2455 |
| new | own | 11-16 | linear | 978 | 0.0344 | 0.0136 | 0.0318 | 0.0470 | 0.0638 | 0.9110 | 0.8462 | 0.9677 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | concave | 978 | 0.0226 | 0.0085 | 0.0208 | 0.0317 | 0.0425 | 0.8906 | 0.8142 | 0.9603 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | convex | 978 | 0.0419 | 0.0179 | 0.0388 | 0.0560 | 0.0772 | 0.9182 | 0.8558 | 0.9706 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | top3_stress | 978 | 0.0219 | 0.0114 | 0.0193 | 0.0281 | 0.0411 | 0.9029 | 0.8269 | 0.9654 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | linear | 2277 | 0.0341 | 0.0175 | 0.0307 | 0.0455 | 0.0622 | 0.9420 | 0.8974 | 0.9840 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | concave | 2277 | 0.0340 | 0.0255 | 0.0329 | 0.0417 | 0.0522 | 0.9543 | 0.9201 | 0.9884 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | convex | 2277 | 0.0249 | 0.0048 | 0.0163 | 0.0377 | 0.0596 | 0.8081 | 0.7622 | 0.8627 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | top3_stress | 2277 | 0.0058 | 0.0000 | 0.0003 | 0.0072 | 0.0197 | 0.3676 | 0.2854 | 0.4401 | 0.0000 | 0.0000 | 0.0000 |
| delta | actual | all | linear | 4896 | -0.0019 | -0.0069 | 0.0000 | 0.0009 | 0.0107 | 0.2143 | 0.1618 | 0.2720 | 0.3321 | 0.2684 | 0.3819 |
| delta | actual | all | concave | 4896 | -0.0013 | -0.0044 | 0.0000 | 0.0010 | 0.0076 | 0.1971 | 0.1556 | 0.2528 | 0.3015 | 0.2222 | 0.3693 |
| delta | actual | all | convex | 4896 | -0.0026 | -0.0104 | 0.0000 | 0.0014 | 0.0140 | 0.2320 | 0.1764 | 0.2888 | 0.3597 | 0.3241 | 0.3895 |
| delta | actual | all | top3_stress | 4896 | -0.0020 | -0.0068 | 0.0000 | 0.0012 | 0.0116 | 0.2251 | 0.1725 | 0.2792 | 0.2906 | 0.2480 | 0.3310 |
| delta | actual | 1-3 | linear | 495 | -0.0055 | -0.0075 | -0.0027 | -0.0014 | -0.0005 | 0.0182 | 0.0000 | 0.0489 | 0.4869 | 0.1878 | 0.7592 |
| delta | actual | 1-3 | concave | 495 | -0.0033 | -0.0044 | -0.0015 | -0.0005 | 0.0013 | 0.0586 | 0.0000 | 0.1764 | 0.3697 | 0.0848 | 0.6100 |
| delta | actual | 1-3 | convex | 495 | -0.0089 | -0.0130 | -0.0053 | -0.0026 | -0.0011 | 0.0101 | 0.0000 | 0.0270 | 0.7515 | 0.6144 | 0.8858 |
| delta | actual | 1-3 | top3_stress | 495 | -0.0101 | -0.0158 | -0.0039 | -0.0006 | -0.0000 | 0.0040 | 0.0000 | 0.0217 | 0.5495 | 0.2815 | 0.7753 |
| delta | actual | 4-10 | linear | 1146 | -0.0141 | -0.0203 | -0.0117 | -0.0056 | -0.0004 | 0.0157 | 0.0000 | 0.0480 | 0.8394 | 0.7265 | 0.9410 |
| delta | actual | 4-10 | concave | 1146 | -0.0101 | -0.0127 | -0.0069 | -0.0032 | 0.0000 | 0.0332 | 0.0000 | 0.0864 | 0.7679 | 0.5878 | 0.9195 |
| delta | actual | 4-10 | convex | 1146 | -0.0190 | -0.0273 | -0.0179 | -0.0102 | -0.0006 | 0.0148 | 0.0000 | 0.0415 | 0.8857 | 0.8273 | 0.9535 |
| delta | actual | 4-10 | top3_stress | 1146 | -0.0162 | -0.0224 | -0.0152 | -0.0089 | -0.0000 | 0.0140 | 0.0000 | 0.0514 | 0.8560 | 0.7664 | 0.9509 |
| delta | actual | 11-16 | linear | 978 | -0.0008 | -0.0088 | 0.0000 | 0.0071 | 0.0166 | 0.3609 | 0.2381 | 0.4898 | 0.3661 | 0.2536 | 0.4891 |
| delta | actual | 11-16 | concave | 978 | -0.0017 | -0.0067 | 0.0000 | 0.0041 | 0.0120 | 0.3006 | 0.1962 | 0.4111 | 0.3507 | 0.2144 | 0.4894 |
| delta | actual | 11-16 | convex | 978 | 0.0014 | -0.0080 | 0.0000 | 0.0105 | 0.0225 | 0.4110 | 0.2924 | 0.5299 | 0.3395 | 0.2489 | 0.4433 |
| delta | actual | 11-16 | top3_stress | 978 | 0.0069 | 0.0000 | 0.0041 | 0.0131 | 0.0211 | 0.5368 | 0.4079 | 0.6441 | 0.1605 | 0.0992 | 0.2133 |
| delta | actual | 17-30 | linear | 2277 | 0.0045 | 0.0000 | 0.0000 | 0.0042 | 0.0153 | 0.2938 | 0.2133 | 0.3807 | 0.0285 | 0.0108 | 0.0498 |
| delta | actual | 17-30 | concave | 2277 | 0.0037 | 0.0000 | 0.0000 | 0.0027 | 0.0123 | 0.2653 | 0.1949 | 0.3415 | 0.0307 | 0.0129 | 0.0539 |
| delta | actual | 17-30 | convex | 2277 | 0.0052 | 0.0000 | 0.0000 | 0.0055 | 0.0181 | 0.3127 | 0.2269 | 0.4063 | 0.0184 | 0.0066 | 0.0322 |
| delta | actual | 17-30 | top3_stress | 2277 | 0.0030 | 0.0000 | 0.0000 | 0.0025 | 0.0110 | 0.2455 | 0.1820 | 0.3228 | 0.0057 | 0.0000 | 0.0143 |
| delta | own | all | linear | 4896 | -0.0007 | -0.0077 | -0.0000 | 0.0036 | 0.0137 | 0.2778 | 0.2418 | 0.3107 | 0.3740 | 0.3299 | 0.4105 |
| delta | own | all | concave | 4896 | -0.0004 | -0.0045 | -0.0000 | 0.0020 | 0.0082 | 0.2384 | 0.2082 | 0.2653 | 0.3241 | 0.2774 | 0.3614 |
| delta | own | all | convex | 4896 | -0.0011 | -0.0116 | 0.0000 | 0.0060 | 0.0200 | 0.3029 | 0.2677 | 0.3343 | 0.3932 | 0.3611 | 0.4227 |
| delta | own | all | top3_stress | 4896 | -0.0007 | -0.0084 | 0.0000 | 0.0058 | 0.0168 | 0.3109 | 0.2525 | 0.3593 | 0.3121 | 0.2590 | 0.3584 |
| delta | own | 1-3 | linear | 495 | -0.0050 | -0.0068 | -0.0033 | -0.0019 | -0.0013 | 0.0000 | 0.0000 | 0.0000 | 0.5576 | 0.2784 | 0.8103 |
| delta | own | 1-3 | concave | 495 | -0.0026 | -0.0036 | -0.0018 | -0.0010 | -0.0007 | 0.0000 | 0.0000 | 0.0000 | 0.3232 | 0.1077 | 0.5487 |
| delta | own | 1-3 | convex | 495 | -0.0087 | -0.0119 | -0.0057 | -0.0033 | -0.0023 | 0.0000 | 0.0000 | 0.0000 | 0.8303 | 0.6938 | 0.9406 |
| delta | own | 1-3 | top3_stress | 495 | -0.0101 | -0.0153 | -0.0039 | -0.0005 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.5616 | 0.2766 | 0.8070 |
| delta | own | 4-10 | linear | 1146 | -0.0125 | -0.0178 | -0.0113 | -0.0072 | -0.0040 | 0.0017 | 0.0000 | 0.0093 | 0.9293 | 0.8659 | 0.9887 |
| delta | own | 4-10 | concave | 1146 | -0.0071 | -0.0103 | -0.0063 | -0.0040 | -0.0022 | 0.0009 | 0.0000 | 0.0055 | 0.8665 | 0.7469 | 0.9735 |
| delta | own | 4-10 | convex | 1146 | -0.0191 | -0.0266 | -0.0182 | -0.0116 | -0.0062 | 0.0017 | 0.0000 | 0.0093 | 0.9476 | 0.8950 | 0.9902 |
| delta | own | 4-10 | top3_stress | 1146 | -0.0171 | -0.0226 | -0.0160 | -0.0102 | -0.0046 | 0.0166 | 0.0000 | 0.0482 | 0.9258 | 0.8431 | 0.9790 |
| delta | own | 11-16 | linear | 978 | 0.0017 | -0.0094 | 0.0015 | 0.0102 | 0.0188 | 0.4898 | 0.3745 | 0.6025 | 0.4100 | 0.2904 | 0.5104 |
| delta | own | 11-16 | concave | 978 | 0.0006 | -0.0061 | 0.0005 | 0.0056 | 0.0111 | 0.4059 | 0.3043 | 0.5047 | 0.3753 | 0.2446 | 0.4807 |
| delta | own | 11-16 | convex | 978 | 0.0046 | -0.0111 | 0.0042 | 0.0168 | 0.0289 | 0.5542 | 0.4481 | 0.6623 | 0.3804 | 0.2670 | 0.4768 |
| delta | own | 11-16 | top3_stress | 978 | 0.0104 | 0.0003 | 0.0099 | 0.0175 | 0.0267 | 0.7025 | 0.5989 | 0.7962 | 0.1851 | 0.0836 | 0.2840 |
| delta | own | 17-30 | linear | 2277 | 0.0050 | 0.0000 | 0.0002 | 0.0079 | 0.0166 | 0.3860 | 0.3359 | 0.4314 | 0.0391 | 0.0106 | 0.0840 |
| delta | own | 17-30 | concave | 2277 | 0.0030 | 0.0000 | 0.0001 | 0.0049 | 0.0102 | 0.3377 | 0.2859 | 0.3858 | 0.0294 | 0.0105 | 0.0540 |
| delta | own | 17-30 | convex | 2277 | 0.0072 | 0.0000 | 0.0004 | 0.0108 | 0.0238 | 0.4124 | 0.3617 | 0.4598 | 0.0246 | 0.0056 | 0.0492 |
| delta | own | 17-30 | top3_stress | 2277 | 0.0048 | 0.0000 | 0.0003 | 0.0065 | 0.0158 | 0.3584 | 0.2702 | 0.4341 | 0.0035 | 0.0000 | 0.0125 |

## H1

| n_team_games | share_neg_new | share_neg_old | diff_new_minus_old | diff_lo99 | diff_hi99 | n_new_reversals | crossing_share | crossing_lo99 | crossing_hi99 | supported |
|---|---|---|---|---|---|---|---|---|---|---|
| 649 | 0.3159 | 0.0000 | 0.3159 | 0.1246 | 0.5172 | 426 | 1.0000 | 1.0000 | 1.0000 | True |

## T5_attr_portfolio_effect

| rule | band | n | mean | q25 | median | q75 | q90 | share_nonzero |
|---|---|---|---|---|---|---|---|---|
| old | all | 4896 | -0.0063 | -0.0133 | 0.0000 | 0.0000 | 0.0022 | 0.4277 |
| old | 1-3 | 495 | -0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.0014 | 0.0970 |
| old | 4-10 | 1146 | 0.0021 | -0.0000 | 0.0000 | 0.0017 | 0.0123 | 0.3307 |
| old | 11-16 | 978 | -0.0051 | -0.0196 | 0.0000 | 0.0000 | 0.0054 | 0.4806 |
| old | 17-30 | 2277 | -0.0124 | -0.0241 | -0.0032 | 0.0000 | 0.0000 | 0.5257 |
| new | all | 4896 | -0.0075 | -0.0109 | 0.0000 | 0.0000 | 0.0029 | 0.4363 |
| new | 1-3 | 495 | -0.0006 | -0.0001 | 0.0000 | 0.0008 | 0.0042 | 0.2424 |
| new | 4-10 | 1146 | 0.0005 | 0.0000 | 0.0000 | 0.0009 | 0.0059 | 0.2766 |
| new | 11-16 | 978 | -0.0077 | -0.0113 | 0.0000 | 0.0000 | 0.0058 | 0.4550 |
| new | 17-30 | 2277 | -0.0129 | -0.0220 | -0.0036 | 0.0000 | 0.0000 | 0.5507 |
| delta | all | 4896 | -0.0012 | -0.0003 | 0.0000 | 0.0001 | 0.0045 | 0.2935 |
| delta | 1-3 | 495 | -0.0005 | -0.0001 | 0.0000 | 0.0007 | 0.0033 | 0.2141 |
| delta | 4-10 | 1146 | -0.0016 | -0.0005 | 0.0000 | 0.0002 | 0.0053 | 0.3080 |
| delta | 11-16 | 978 | -0.0025 | -0.0030 | 0.0000 | 0.0000 | 0.0094 | 0.4039 |
| delta | 17-30 | 2277 | -0.0006 | -0.0000 | 0.0000 | 0.0000 | 0.0037 | 0.2560 |

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
| old | actual | 11-16 | linear | 0.0000 | tau | 978 | 0.0275 | 0.0061 | 0.0262 | 0.0381 | 0.0532 | 0.0000 | 0.5000 |
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
| old | actual | 17-30 | linear | 0.8000 | tau | 2277 | 0.0150 | 0.0000 | 0.0064 | 0.0286 | 0.0402 | 0.0031 | 0.5000 |
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
| old | own | all | top3_stress | 0.0000 | tau | 4896 | 0.0078 | 0.0000 | 0.0026 | 0.0130 | 0.0245 | 0.0000 | 0.1000 |
| old | own | all | top3_stress | 0.5000 | tau | 4896 | 0.0078 | 0.0000 | 0.0026 | 0.0130 | 0.0245 | 0.0729 | 0.1000 |
| old | own | all | top3_stress | 0.8000 | tau | 4896 | 0.0078 | 0.0000 | 0.0026 | 0.0130 | 0.0245 | 0.0733 | 0.1000 |
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
| old | own | 17-30 | top3_stress | 0.5000 | tau | 2277 | 0.0009 | 0.0000 | 0.0000 | 0.0007 | 0.0029 | 0.1559 | 0.1000 |
| old | own | 17-30 | top3_stress | 0.8000 | tau | 2277 | 0.0009 | 0.0000 | 0.0000 | 0.0007 | 0.0029 | 0.1568 | 0.1000 |
| new | actual | all | - | 0.0000 | M | 4896 | 0.0056 | -0.0000 | 0.0000 | 0.0000 | 0.0128 |  |  |
| new | actual | all | linear | 0.0000 | tau | 4896 | 0.0159 | 0.0000 | 0.0034 | 0.0284 | 0.0464 | 0.0000 | 0.5000 |
| new | actual | all | linear | 0.5000 | tau | 4896 | 0.0145 | 0.0000 | 0.0029 | 0.0265 | 0.0442 | 0.0270 | 0.5000 |
| new | actual | all | linear | 0.8000 | tau | 4896 | 0.0137 | 0.0000 | 0.0027 | 0.0251 | 0.0428 | 0.0364 | 0.5000 |
| new | actual | all | concave | 0.0000 | tau | 4896 | 0.0153 | 0.0000 | 0.0039 | 0.0287 | 0.0418 | 0.0000 | 0.6599 |
| new | actual | all | concave | 0.5000 | tau | 4896 | 0.0135 | 0.0000 | 0.0028 | 0.0271 | 0.0388 | 0.0033 | 0.6599 |
| new | actual | all | concave | 0.8000 | tau | 4896 | 0.0124 | 0.0000 | 0.0022 | 0.0252 | 0.0367 | 0.0098 | 0.6599 |
| new | actual | all | convex | 0.0000 | tau | 4896 | 0.0136 | 0.0000 | 0.0021 | 0.0220 | 0.0455 | 0.0000 | 0.3391 |
| new | actual | all | convex | 0.5000 | tau | 4896 | 0.0126 | 0.0000 | 0.0020 | 0.0205 | 0.0424 | 0.0035 | 0.3391 |
| new | actual | all | convex | 0.8000 | tau | 4896 | 0.0121 | 0.0000 | 0.0019 | 0.0193 | 0.0414 | 0.0084 | 0.3391 |
| new | actual | all | top3_stress | 0.0000 | tau | 4896 | 0.0048 | 0.0000 | 0.0000 | 0.0072 | 0.0214 | 0.0000 | 0.1000 |
| new | actual | all | top3_stress | 0.5000 | tau | 4896 | 0.0045 | 0.0000 | 0.0000 | 0.0068 | 0.0204 | 0.0741 | 0.1000 |
| new | actual | all | top3_stress | 0.8000 | tau | 4896 | 0.0043 | 0.0000 | 0.0000 | 0.0064 | 0.0197 | 0.0748 | 0.1000 |
| new | actual | 1-3 | - | 0.0000 | M | 495 | 0.0001 | -0.0000 | -0.0000 | 0.0000 | 0.0055 |  |  |
| new | actual | 1-3 | linear | 0.0000 | tau | 495 | -0.0023 | -0.0029 | -0.0002 | 0.0004 | 0.0019 | 0.0000 | 0.5000 |
| new | actual | 1-3 | linear | 0.5000 | tau | 495 | -0.0023 | -0.0029 | -0.0005 | 0.0000 | 0.0009 | 0.1010 | 0.5000 |
| new | actual | 1-3 | linear | 0.8000 | tau | 495 | -0.0023 | -0.0030 | -0.0007 | 0.0000 | 0.0003 | 0.1576 | 0.5000 |
| new | actual | 1-3 | concave | 0.0000 | tau | 495 | -0.0013 | -0.0016 | -0.0001 | 0.0006 | 0.0042 | 0.0000 | 0.6599 |
| new | actual | 1-3 | concave | 0.5000 | tau | 495 | -0.0013 | -0.0015 | -0.0001 | 0.0004 | 0.0021 | 0.0141 | 0.6599 |
| new | actual | 1-3 | concave | 0.8000 | tau | 495 | -0.0013 | -0.0015 | -0.0001 | 0.0001 | 0.0009 | 0.0343 | 0.6599 |
| new | actual | 1-3 | convex | 0.0000 | tau | 495 | -0.0037 | -0.0054 | -0.0012 | -0.0000 | 0.0002 | 0.0000 | 0.3391 |
| new | actual | 1-3 | convex | 0.5000 | tau | 495 | -0.0037 | -0.0057 | -0.0015 | -0.0000 | 0.0001 | 0.0121 | 0.3391 |
| new | actual | 1-3 | convex | 0.8000 | tau | 495 | -0.0037 | -0.0056 | -0.0015 | -0.0000 | 0.0001 | 0.0263 | 0.3391 |
| new | actual | 1-3 | top3_stress | 0.0000 | tau | 495 | -0.0056 | -0.0093 | -0.0025 | -0.0001 | 0.0000 | 0.0000 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.5000 | tau | 495 | -0.0056 | -0.0093 | -0.0027 | -0.0001 | 0.0000 | 0.0626 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.8000 | tau | 495 | -0.0056 | -0.0093 | -0.0028 | -0.0001 | 0.0000 | 0.0626 | 0.1000 |
| new | actual | 4-10 | - | 0.0000 | M | 1146 | 0.0029 | -0.0000 | 0.0000 | 0.0004 | 0.0120 |  |  |
| new | actual | 4-10 | linear | 0.0000 | tau | 1146 | 0.0042 | 0.0000 | 0.0008 | 0.0065 | 0.0154 | 0.0000 | 0.5000 |
| new | actual | 4-10 | linear | 0.5000 | tau | 1146 | 0.0035 | -0.0000 | 0.0004 | 0.0057 | 0.0132 | 0.0689 | 0.5000 |
| new | actual | 4-10 | linear | 0.8000 | tau | 1146 | 0.0031 | -0.0000 | 0.0003 | 0.0054 | 0.0123 | 0.0812 | 0.5000 |
| new | actual | 4-10 | concave | 0.0000 | tau | 1146 | 0.0038 | 0.0000 | 0.0007 | 0.0053 | 0.0144 | 0.0000 | 0.6599 |
| new | actual | 4-10 | concave | 0.5000 | tau | 1146 | 0.0028 | 0.0000 | 0.0006 | 0.0043 | 0.0107 | 0.0061 | 0.6599 |
| new | actual | 4-10 | concave | 0.8000 | tau | 1146 | 0.0022 | 0.0000 | 0.0003 | 0.0038 | 0.0091 | 0.0236 | 0.6599 |
| new | actual | 4-10 | convex | 0.0000 | tau | 1146 | 0.0043 | -0.0001 | 0.0004 | 0.0073 | 0.0178 | 0.0000 | 0.3391 |
| new | actual | 4-10 | convex | 0.5000 | tau | 1146 | 0.0038 | -0.0001 | 0.0004 | 0.0071 | 0.0166 | 0.0044 | 0.3391 |
| new | actual | 4-10 | convex | 0.8000 | tau | 1146 | 0.0035 | -0.0001 | 0.0004 | 0.0066 | 0.0161 | 0.0113 | 0.3391 |
| new | actual | 4-10 | top3_stress | 0.0000 | tau | 1146 | 0.0021 | -0.0001 | 0.0000 | 0.0055 | 0.0136 | 0.0000 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.5000 | tau | 1146 | 0.0020 | -0.0001 | 0.0000 | 0.0054 | 0.0134 | 0.0305 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.8000 | tau | 1146 | 0.0019 | -0.0001 | 0.0000 | 0.0052 | 0.0133 | 0.0323 | 0.1000 |
| new | actual | 11-16 | - | 0.0000 | M | 978 | 0.0092 | -0.0000 | 0.0000 | 0.0000 | 0.0317 |  |  |
| new | actual | 11-16 | linear | 0.0000 | tau | 978 | 0.0267 | 0.0001 | 0.0225 | 0.0416 | 0.0560 | 0.0000 | 0.5000 |
| new | actual | 11-16 | linear | 0.5000 | tau | 978 | 0.0244 | 0.0001 | 0.0199 | 0.0396 | 0.0522 | 0.0031 | 0.5000 |
| new | actual | 11-16 | linear | 0.8000 | tau | 978 | 0.0230 | 0.0001 | 0.0183 | 0.0387 | 0.0503 | 0.0041 | 0.5000 |
| new | actual | 11-16 | concave | 0.0000 | tau | 978 | 0.0209 | 0.0001 | 0.0161 | 0.0298 | 0.0425 | 0.0000 | 0.6599 |
| new | actual | 11-16 | concave | 0.5000 | tau | 978 | 0.0178 | 0.0001 | 0.0144 | 0.0283 | 0.0383 | 0.0010 | 0.6599 |
| new | actual | 11-16 | concave | 0.8000 | tau | 978 | 0.0160 | 0.0001 | 0.0126 | 0.0267 | 0.0345 | 0.0031 | 0.6599 |
| new | actual | 11-16 | convex | 0.0000 | tau | 978 | 0.0298 | 0.0002 | 0.0261 | 0.0472 | 0.0639 | 0.0000 | 0.3391 |
| new | actual | 11-16 | convex | 0.5000 | tau | 978 | 0.0283 | 0.0002 | 0.0241 | 0.0449 | 0.0614 | 0.0010 | 0.3391 |
| new | actual | 11-16 | convex | 0.8000 | tau | 978 | 0.0273 | 0.0002 | 0.0221 | 0.0443 | 0.0599 | 0.0031 | 0.3391 |
| new | actual | 11-16 | top3_stress | 0.0000 | tau | 978 | 0.0159 | 0.0000 | 0.0143 | 0.0244 | 0.0346 | 0.0000 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.5000 | tau | 978 | 0.0154 | 0.0000 | 0.0135 | 0.0235 | 0.0339 | 0.0102 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.8000 | tau | 978 | 0.0152 | 0.0000 | 0.0132 | 0.0231 | 0.0337 | 0.0112 | 0.1000 |
| new | actual | 17-30 | - | 0.0000 | M | 2277 | 0.0066 | -0.0000 | 0.0000 | 0.0000 | 0.0099 |  |  |
| new | actual | 17-30 | linear | 0.0000 | tau | 2277 | 0.0212 | 0.0000 | 0.0160 | 0.0360 | 0.0516 | 0.0000 | 0.5000 |
| new | actual | 17-30 | linear | 0.5000 | tau | 2277 | 0.0195 | 0.0000 | 0.0151 | 0.0344 | 0.0479 | 0.0000 | 0.5000 |
| new | actual | 17-30 | linear | 0.8000 | tau | 2277 | 0.0185 | 0.0000 | 0.0138 | 0.0326 | 0.0465 | 0.0013 | 0.5000 |
| new | actual | 17-30 | concave | 0.0000 | tau | 2277 | 0.0224 | 0.0000 | 0.0216 | 0.0357 | 0.0511 | 0.0000 | 0.6599 |
| new | actual | 17-30 | concave | 0.5000 | tau | 2277 | 0.0202 | 0.0000 | 0.0207 | 0.0347 | 0.0459 | 0.0004 | 0.6599 |
| new | actual | 17-30 | concave | 0.8000 | tau | 2277 | 0.0189 | 0.0000 | 0.0173 | 0.0336 | 0.0435 | 0.0004 | 0.6599 |
| new | actual | 17-30 | convex | 0.0000 | tau | 2277 | 0.0150 | 0.0000 | 0.0048 | 0.0239 | 0.0440 | 0.0000 | 0.3391 |
| new | actual | 17-30 | convex | 0.5000 | tau | 2277 | 0.0139 | 0.0000 | 0.0046 | 0.0222 | 0.0411 | 0.0022 | 0.3391 |
| new | actual | 17-30 | convex | 0.8000 | tau | 2277 | 0.0132 | 0.0000 | 0.0046 | 0.0212 | 0.0388 | 0.0053 | 0.3391 |
| new | actual | 17-30 | top3_stress | 0.0000 | tau | 2277 | 0.0036 | 0.0000 | 0.0000 | 0.0026 | 0.0134 | 0.0000 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.5000 | tau | 2277 | 0.0032 | 0.0000 | 0.0000 | 0.0026 | 0.0118 | 0.1260 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.8000 | tau | 2277 | 0.0030 | 0.0000 | 0.0000 | 0.0025 | 0.0113 | 0.1260 | 0.1000 |
| new | own | all | - | 0.0000 | M | 4896 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | all | linear | 0.0000 | tau | 4896 | 0.0234 | 0.0004 | 0.0178 | 0.0391 | 0.0556 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.5000 | tau | 4896 | 0.0234 | 0.0004 | 0.0178 | 0.0391 | 0.0556 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.8000 | tau | 4896 | 0.0234 | 0.0004 | 0.0178 | 0.0391 | 0.0556 | 0.0000 | 0.5000 |
| new | own | all | concave | 0.0000 | tau | 4896 | 0.0208 | 0.0003 | 0.0208 | 0.0343 | 0.0454 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.5000 | tau | 4896 | 0.0208 | 0.0003 | 0.0208 | 0.0343 | 0.0454 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.8000 | tau | 4896 | 0.0208 | 0.0003 | 0.0208 | 0.0343 | 0.0454 | 0.0000 | 0.6599 |
| new | own | all | convex | 0.0000 | tau | 4896 | 0.0208 | 0.0002 | 0.0101 | 0.0346 | 0.0576 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.5000 | tau | 4896 | 0.0208 | 0.0002 | 0.0101 | 0.0346 | 0.0576 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.8000 | tau | 4896 | 0.0208 | 0.0002 | 0.0101 | 0.0346 | 0.0576 | 0.0000 | 0.3391 |
| new | own | all | top3_stress | 0.0000 | tau | 4896 | 0.0071 | 0.0000 | 0.0006 | 0.0127 | 0.0250 | 0.0000 | 0.1000 |
| new | own | all | top3_stress | 0.5000 | tau | 4896 | 0.0071 | 0.0000 | 0.0006 | 0.0127 | 0.0250 | 0.0970 | 0.1000 |
| new | own | all | top3_stress | 0.8000 | tau | 4896 | 0.0071 | 0.0000 | 0.0006 | 0.0127 | 0.0250 | 0.0972 | 0.1000 |
| new | own | 1-3 | - | 0.0000 | M | 495 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 1-3 | linear | 0.0000 | tau | 495 | -0.0016 | -0.0028 | -0.0008 | -0.0000 | 0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.5000 | tau | 495 | -0.0016 | -0.0028 | -0.0008 | -0.0000 | 0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.8000 | tau | 495 | -0.0016 | -0.0028 | -0.0008 | -0.0000 | 0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | concave | 0.0000 | tau | 495 | -0.0008 | -0.0014 | -0.0004 | -0.0000 | 0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.5000 | tau | 495 | -0.0008 | -0.0014 | -0.0004 | -0.0000 | 0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.8000 | tau | 495 | -0.0008 | -0.0014 | -0.0004 | -0.0000 | 0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | convex | 0.0000 | tau | 495 | -0.0030 | -0.0051 | -0.0015 | -0.0001 | 0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.5000 | tau | 495 | -0.0030 | -0.0051 | -0.0015 | -0.0001 | 0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.8000 | tau | 495 | -0.0030 | -0.0051 | -0.0015 | -0.0001 | 0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | top3_stress | 0.0000 | tau | 495 | -0.0055 | -0.0092 | -0.0027 | -0.0001 | 0.0000 | 0.0000 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.5000 | tau | 495 | -0.0055 | -0.0092 | -0.0027 | -0.0001 | 0.0000 | 0.0646 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.8000 | tau | 495 | -0.0055 | -0.0092 | -0.0027 | -0.0001 | 0.0000 | 0.0646 | 0.1000 |
| new | own | 4-10 | - | 0.0000 | M | 1146 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 4-10 | linear | 0.0000 | tau | 1146 | 0.0037 | -0.0000 | 0.0002 | 0.0053 | 0.0130 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.5000 | tau | 1146 | 0.0037 | -0.0000 | 0.0002 | 0.0053 | 0.0130 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.8000 | tau | 1146 | 0.0037 | -0.0000 | 0.0002 | 0.0053 | 0.0130 | 0.0000 | 0.5000 |
| new | own | 4-10 | concave | 0.0000 | tau | 1146 | 0.0024 | -0.0000 | 0.0001 | 0.0032 | 0.0079 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.5000 | tau | 1146 | 0.0024 | -0.0000 | 0.0001 | 0.0032 | 0.0079 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.8000 | tau | 1146 | 0.0024 | -0.0000 | 0.0001 | 0.0032 | 0.0079 | 0.0000 | 0.6599 |
| new | own | 4-10 | convex | 0.0000 | tau | 1146 | 0.0048 | -0.0000 | 0.0003 | 0.0077 | 0.0181 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.5000 | tau | 1146 | 0.0048 | -0.0000 | 0.0003 | 0.0077 | 0.0181 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.8000 | tau | 1146 | 0.0048 | -0.0000 | 0.0003 | 0.0077 | 0.0181 | 0.0000 | 0.3391 |
| new | own | 4-10 | top3_stress | 0.0000 | tau | 1146 | 0.0027 | -0.0001 | 0.0000 | 0.0071 | 0.0151 | 0.0000 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.5000 | tau | 1146 | 0.0027 | -0.0001 | 0.0000 | 0.0071 | 0.0151 | 0.0436 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.8000 | tau | 1146 | 0.0027 | -0.0001 | 0.0000 | 0.0071 | 0.0151 | 0.0436 | 0.1000 |
| new | own | 11-16 | - | 0.0000 | M | 978 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 11-16 | linear | 0.0000 | tau | 978 | 0.0344 | 0.0136 | 0.0318 | 0.0470 | 0.0638 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.5000 | tau | 978 | 0.0344 | 0.0136 | 0.0318 | 0.0470 | 0.0638 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.8000 | tau | 978 | 0.0344 | 0.0136 | 0.0318 | 0.0470 | 0.0638 | 0.0000 | 0.5000 |
| new | own | 11-16 | concave | 0.0000 | tau | 978 | 0.0226 | 0.0085 | 0.0208 | 0.0317 | 0.0425 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.5000 | tau | 978 | 0.0226 | 0.0085 | 0.0208 | 0.0317 | 0.0425 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.8000 | tau | 978 | 0.0226 | 0.0085 | 0.0208 | 0.0317 | 0.0425 | 0.0000 | 0.6599 |
| new | own | 11-16 | convex | 0.0000 | tau | 978 | 0.0419 | 0.0179 | 0.0388 | 0.0560 | 0.0772 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.5000 | tau | 978 | 0.0419 | 0.0179 | 0.0388 | 0.0560 | 0.0772 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.8000 | tau | 978 | 0.0419 | 0.0179 | 0.0388 | 0.0560 | 0.0772 | 0.0000 | 0.3391 |
| new | own | 11-16 | top3_stress | 0.0000 | tau | 978 | 0.0219 | 0.0114 | 0.0193 | 0.0281 | 0.0411 | 0.0000 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.5000 | tau | 978 | 0.0219 | 0.0114 | 0.0193 | 0.0281 | 0.0411 | 0.0123 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.8000 | tau | 978 | 0.0219 | 0.0114 | 0.0193 | 0.0281 | 0.0411 | 0.0123 | 0.1000 |
| new | own | 17-30 | - | 0.0000 | M | 2277 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 17-30 | linear | 0.0000 | tau | 2277 | 0.0341 | 0.0175 | 0.0307 | 0.0455 | 0.0622 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.5000 | tau | 2277 | 0.0341 | 0.0175 | 0.0307 | 0.0455 | 0.0622 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.8000 | tau | 2277 | 0.0341 | 0.0175 | 0.0307 | 0.0455 | 0.0622 | 0.0000 | 0.5000 |
| new | own | 17-30 | concave | 0.0000 | tau | 2277 | 0.0340 | 0.0255 | 0.0329 | 0.0417 | 0.0522 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.5000 | tau | 2277 | 0.0340 | 0.0255 | 0.0329 | 0.0417 | 0.0522 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.8000 | tau | 2277 | 0.0340 | 0.0255 | 0.0329 | 0.0417 | 0.0522 | 0.0000 | 0.6599 |
| new | own | 17-30 | convex | 0.0000 | tau | 2277 | 0.0249 | 0.0048 | 0.0163 | 0.0377 | 0.0596 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.5000 | tau | 2277 | 0.0249 | 0.0048 | 0.0163 | 0.0377 | 0.0596 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.8000 | tau | 2277 | 0.0249 | 0.0048 | 0.0163 | 0.0377 | 0.0596 | 0.0000 | 0.3391 |
| new | own | 17-30 | top3_stress | 0.0000 | tau | 2277 | 0.0058 | 0.0000 | 0.0003 | 0.0072 | 0.0197 | 0.0000 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.5000 | tau | 2277 | 0.0058 | 0.0000 | 0.0003 | 0.0072 | 0.0197 | 0.1673 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.8000 | tau | 2277 | 0.0058 | 0.0000 | 0.0003 | 0.0072 | 0.0197 | 0.1678 | 0.1000 |
| delta | actual | all | - | 0.0000 | M | 4896 | -0.0005 | -0.0000 | 0.0000 | 0.0000 | 0.0026 |  |  |
| delta | actual | all | linear | 0.0000 | tau | 4896 | -0.0019 | -0.0069 | 0.0000 | 0.0009 | 0.0107 | 0.0000 | 0.5000 |
| delta | actual | all | linear | 0.5000 | tau | 4896 | -0.0018 | -0.0068 | 0.0000 | 0.0008 | 0.0101 | 0.0092 | 0.5000 |
| delta | actual | all | linear | 0.8000 | tau | 4896 | -0.0017 | -0.0067 | 0.0000 | 0.0008 | 0.0095 | 0.0129 | 0.5000 |
| delta | actual | all | concave | 0.0000 | tau | 4896 | -0.0013 | -0.0044 | 0.0000 | 0.0010 | 0.0076 | 0.0000 | 0.6599 |
| delta | actual | all | concave | 0.5000 | tau | 4896 | -0.0011 | -0.0041 | 0.0000 | 0.0005 | 0.0066 | 0.0196 | 0.6599 |
| delta | actual | all | concave | 0.8000 | tau | 4896 | -0.0010 | -0.0039 | 0.0000 | 0.0005 | 0.0061 | 0.0345 | 0.6599 |
| delta | actual | all | convex | 0.0000 | tau | 4896 | -0.0026 | -0.0104 | 0.0000 | 0.0014 | 0.0140 | 0.0000 | 0.3391 |
| delta | actual | all | convex | 0.5000 | tau | 4896 | -0.0026 | -0.0102 | 0.0000 | 0.0014 | 0.0134 | 0.0051 | 0.3391 |
| delta | actual | all | convex | 0.8000 | tau | 4896 | -0.0025 | -0.0101 | 0.0000 | 0.0014 | 0.0132 | 0.0090 | 0.3391 |
| delta | actual | all | top3_stress | 0.0000 | tau | 4896 | -0.0020 | -0.0068 | 0.0000 | 0.0012 | 0.0116 | 0.0000 | 0.1000 |
| delta | actual | all | top3_stress | 0.5000 | tau | 4896 | -0.0020 | -0.0067 | 0.0000 | 0.0014 | 0.0115 | 0.0404 | 0.1000 |
| delta | actual | all | top3_stress | 0.8000 | tau | 4896 | -0.0020 | -0.0065 | 0.0000 | 0.0014 | 0.0115 | 0.0419 | 0.1000 |
| delta | actual | 1-3 | - | 0.0000 | M | 495 | -0.0006 | -0.0000 | -0.0000 | 0.0000 | 0.0035 |  |  |
| delta | actual | 1-3 | linear | 0.0000 | tau | 495 | -0.0055 | -0.0075 | -0.0027 | -0.0014 | -0.0005 | 0.0000 | 0.5000 |
| delta | actual | 1-3 | linear | 0.5000 | tau | 495 | -0.0054 | -0.0076 | -0.0030 | -0.0015 | -0.0006 | 0.0162 | 0.5000 |
| delta | actual | 1-3 | linear | 0.8000 | tau | 495 | -0.0053 | -0.0076 | -0.0032 | -0.0016 | -0.0007 | 0.0222 | 0.5000 |
| delta | actual | 1-3 | concave | 0.0000 | tau | 495 | -0.0033 | -0.0044 | -0.0015 | -0.0005 | 0.0013 | 0.0000 | 0.6599 |
| delta | actual | 1-3 | concave | 0.5000 | tau | 495 | -0.0031 | -0.0040 | -0.0014 | -0.0006 | 0.0000 | 0.0667 | 0.6599 |
| delta | actual | 1-3 | concave | 0.8000 | tau | 495 | -0.0030 | -0.0040 | -0.0016 | -0.0008 | -0.0003 | 0.1273 | 0.6599 |
| delta | actual | 1-3 | convex | 0.0000 | tau | 495 | -0.0089 | -0.0130 | -0.0053 | -0.0026 | -0.0011 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | convex | 0.5000 | tau | 495 | -0.0088 | -0.0125 | -0.0055 | -0.0027 | -0.0011 | 0.0081 | 0.3391 |
| delta | actual | 1-3 | convex | 0.8000 | tau | 495 | -0.0088 | -0.0125 | -0.0057 | -0.0027 | -0.0011 | 0.0081 | 0.3391 |
| delta | actual | 1-3 | top3_stress | 0.0000 | tau | 495 | -0.0101 | -0.0158 | -0.0039 | -0.0006 | -0.0000 | 0.0000 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.5000 | tau | 495 | -0.0101 | -0.0157 | -0.0040 | -0.0006 | -0.0000 | 0.0141 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.8000 | tau | 495 | -0.0101 | -0.0154 | -0.0039 | -0.0006 | -0.0000 | 0.0162 | 0.1000 |
| delta | actual | 4-10 | - | 0.0000 | M | 1146 | -0.0048 | -0.0006 | -0.0000 | 0.0000 | 0.0007 |  |  |
| delta | actual | 4-10 | linear | 0.0000 | tau | 1146 | -0.0141 | -0.0203 | -0.0117 | -0.0056 | -0.0004 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | linear | 0.5000 | tau | 1146 | -0.0129 | -0.0190 | -0.0114 | -0.0062 | -0.0004 | 0.0017 | 0.5000 |
| delta | actual | 4-10 | linear | 0.8000 | tau | 1146 | -0.0122 | -0.0182 | -0.0110 | -0.0062 | -0.0004 | 0.0026 | 0.5000 |
| delta | actual | 4-10 | concave | 0.0000 | tau | 1146 | -0.0101 | -0.0127 | -0.0069 | -0.0032 | 0.0000 | 0.0000 | 0.6599 |
| delta | actual | 4-10 | concave | 0.5000 | tau | 1146 | -0.0086 | -0.0123 | -0.0066 | -0.0032 | -0.0000 | 0.0384 | 0.6599 |
| delta | actual | 4-10 | concave | 0.8000 | tau | 1146 | -0.0076 | -0.0113 | -0.0065 | -0.0033 | -0.0002 | 0.0489 | 0.6599 |
| delta | actual | 4-10 | convex | 0.0000 | tau | 1146 | -0.0190 | -0.0273 | -0.0179 | -0.0102 | -0.0006 | 0.0000 | 0.3391 |
| delta | actual | 4-10 | convex | 0.5000 | tau | 1146 | -0.0181 | -0.0267 | -0.0174 | -0.0102 | -0.0012 | 0.0035 | 0.3391 |
| delta | actual | 4-10 | convex | 0.8000 | tau | 1146 | -0.0177 | -0.0258 | -0.0168 | -0.0101 | -0.0012 | 0.0052 | 0.3391 |
| delta | actual | 4-10 | top3_stress | 0.0000 | tau | 1146 | -0.0162 | -0.0224 | -0.0152 | -0.0089 | -0.0000 | 0.0000 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.5000 | tau | 1146 | -0.0159 | -0.0223 | -0.0149 | -0.0086 | -0.0001 | 0.0026 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.8000 | tau | 1146 | -0.0158 | -0.0222 | -0.0148 | -0.0084 | -0.0000 | 0.0044 | 0.1000 |
| delta | actual | 11-16 | - | 0.0000 | M | 978 | -0.0023 | -0.0000 | 0.0000 | 0.0000 | 0.0010 |  |  |
| delta | actual | 11-16 | linear | 0.0000 | tau | 978 | -0.0008 | -0.0088 | 0.0000 | 0.0071 | 0.0166 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | linear | 0.5000 | tau | 978 | -0.0002 | -0.0075 | 0.0000 | 0.0066 | 0.0153 | 0.0051 | 0.5000 |
| delta | actual | 11-16 | linear | 0.8000 | tau | 978 | 0.0001 | -0.0064 | 0.0000 | 0.0061 | 0.0147 | 0.0102 | 0.5000 |
| delta | actual | 11-16 | concave | 0.0000 | tau | 978 | -0.0017 | -0.0067 | 0.0000 | 0.0041 | 0.0120 | 0.0000 | 0.6599 |
| delta | actual | 11-16 | concave | 0.5000 | tau | 978 | -0.0010 | -0.0059 | 0.0000 | 0.0040 | 0.0100 | 0.0041 | 0.6599 |
| delta | actual | 11-16 | concave | 0.8000 | tau | 978 | -0.0005 | -0.0051 | 0.0000 | 0.0037 | 0.0092 | 0.0082 | 0.6599 |
| delta | actual | 11-16 | convex | 0.0000 | tau | 978 | 0.0014 | -0.0080 | 0.0000 | 0.0105 | 0.0225 | 0.0000 | 0.3391 |
| delta | actual | 11-16 | convex | 0.5000 | tau | 978 | 0.0018 | -0.0066 | 0.0000 | 0.0103 | 0.0212 | 0.0092 | 0.3391 |
| delta | actual | 11-16 | convex | 0.8000 | tau | 978 | 0.0020 | -0.0061 | 0.0000 | 0.0098 | 0.0203 | 0.0215 | 0.3391 |
| delta | actual | 11-16 | top3_stress | 0.0000 | tau | 978 | 0.0069 | 0.0000 | 0.0041 | 0.0131 | 0.0211 | 0.0000 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.5000 | tau | 978 | 0.0070 | 0.0000 | 0.0047 | 0.0130 | 0.0204 | 0.0286 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.8000 | tau | 978 | 0.0071 | 0.0000 | 0.0048 | 0.0129 | 0.0202 | 0.0307 | 0.1000 |
| delta | actual | 17-30 | - | 0.0000 | M | 2277 | 0.0024 | 0.0000 | 0.0000 | 0.0000 | 0.0042 |  |  |
| delta | actual | 17-30 | linear | 0.0000 | tau | 2277 | 0.0045 | 0.0000 | 0.0000 | 0.0042 | 0.0153 | 0.0000 | 0.5000 |
| delta | actual | 17-30 | linear | 0.5000 | tau | 2277 | 0.0039 | 0.0000 | 0.0000 | 0.0040 | 0.0137 | 0.0132 | 0.5000 |
| delta | actual | 17-30 | linear | 0.8000 | tau | 2277 | 0.0035 | 0.0000 | 0.0000 | 0.0039 | 0.0127 | 0.0171 | 0.5000 |
| delta | actual | 17-30 | concave | 0.0000 | tau | 2277 | 0.0037 | 0.0000 | 0.0000 | 0.0027 | 0.0123 | 0.0000 | 0.6599 |
| delta | actual | 17-30 | concave | 0.5000 | tau | 2277 | 0.0029 | 0.0000 | 0.0000 | 0.0026 | 0.0103 | 0.0066 | 0.6599 |
| delta | actual | 17-30 | concave | 0.8000 | tau | 2277 | 0.0025 | 0.0000 | 0.0000 | 0.0024 | 0.0089 | 0.0184 | 0.6599 |
| delta | actual | 17-30 | convex | 0.0000 | tau | 2277 | 0.0052 | 0.0000 | 0.0000 | 0.0055 | 0.0181 | 0.0000 | 0.3391 |
| delta | actual | 17-30 | convex | 0.5000 | tau | 2277 | 0.0048 | 0.0000 | 0.0000 | 0.0053 | 0.0173 | 0.0035 | 0.3391 |
| delta | actual | 17-30 | convex | 0.8000 | tau | 2277 | 0.0046 | 0.0000 | 0.0000 | 0.0052 | 0.0163 | 0.0057 | 0.3391 |
| delta | actual | 17-30 | top3_stress | 0.0000 | tau | 2277 | 0.0030 | 0.0000 | 0.0000 | 0.0025 | 0.0110 | 0.0000 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.5000 | tau | 2277 | 0.0029 | 0.0000 | 0.0000 | 0.0026 | 0.0106 | 0.0703 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.8000 | tau | 2277 | 0.0028 | 0.0000 | 0.0000 | 0.0026 | 0.0105 | 0.0711 | 0.1000 |
| delta | own | all | - | 0.0000 | M | 4896 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | all | linear | 0.0000 | tau | 4896 | -0.0007 | -0.0077 | -0.0000 | 0.0036 | 0.0137 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.5000 | tau | 4896 | -0.0007 | -0.0077 | -0.0000 | 0.0036 | 0.0137 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.8000 | tau | 4896 | -0.0007 | -0.0077 | -0.0000 | 0.0036 | 0.0137 | 0.0004 | 0.5000 |
| delta | own | all | concave | 0.0000 | tau | 4896 | -0.0004 | -0.0045 | -0.0000 | 0.0020 | 0.0082 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.5000 | tau | 4896 | -0.0004 | -0.0045 | -0.0000 | 0.0020 | 0.0082 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.8000 | tau | 4896 | -0.0004 | -0.0045 | -0.0000 | 0.0020 | 0.0082 | 0.0000 | 0.6599 |
| delta | own | all | convex | 0.0000 | tau | 4896 | -0.0011 | -0.0116 | 0.0000 | 0.0060 | 0.0200 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.5000 | tau | 4896 | -0.0011 | -0.0116 | 0.0000 | 0.0060 | 0.0200 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.8000 | tau | 4896 | -0.0011 | -0.0116 | 0.0000 | 0.0060 | 0.0200 | 0.0000 | 0.3391 |
| delta | own | all | top3_stress | 0.0000 | tau | 4896 | -0.0007 | -0.0084 | 0.0000 | 0.0058 | 0.0168 | 0.0000 | 0.1000 |
| delta | own | all | top3_stress | 0.5000 | tau | 4896 | -0.0007 | -0.0084 | 0.0000 | 0.0058 | 0.0168 | 0.0188 | 0.1000 |
| delta | own | all | top3_stress | 0.8000 | tau | 4896 | -0.0007 | -0.0084 | 0.0000 | 0.0058 | 0.0168 | 0.0188 | 0.1000 |
| delta | own | 1-3 | - | 0.0000 | M | 495 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 1-3 | linear | 0.0000 | tau | 495 | -0.0050 | -0.0068 | -0.0033 | -0.0019 | -0.0013 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.5000 | tau | 495 | -0.0050 | -0.0068 | -0.0033 | -0.0019 | -0.0013 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.8000 | tau | 495 | -0.0050 | -0.0068 | -0.0033 | -0.0019 | -0.0013 | 0.0000 | 0.5000 |
| delta | own | 1-3 | concave | 0.0000 | tau | 495 | -0.0026 | -0.0036 | -0.0018 | -0.0010 | -0.0007 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.5000 | tau | 495 | -0.0026 | -0.0036 | -0.0018 | -0.0010 | -0.0007 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.8000 | tau | 495 | -0.0026 | -0.0036 | -0.0018 | -0.0010 | -0.0007 | 0.0000 | 0.6599 |
| delta | own | 1-3 | convex | 0.0000 | tau | 495 | -0.0087 | -0.0119 | -0.0057 | -0.0033 | -0.0023 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.5000 | tau | 495 | -0.0087 | -0.0119 | -0.0057 | -0.0033 | -0.0023 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.8000 | tau | 495 | -0.0087 | -0.0119 | -0.0057 | -0.0033 | -0.0023 | 0.0000 | 0.3391 |
| delta | own | 1-3 | top3_stress | 0.0000 | tau | 495 | -0.0101 | -0.0153 | -0.0039 | -0.0005 | -0.0000 | 0.0000 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.5000 | tau | 495 | -0.0101 | -0.0153 | -0.0039 | -0.0005 | -0.0000 | 0.0121 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.8000 | tau | 495 | -0.0101 | -0.0153 | -0.0039 | -0.0005 | -0.0000 | 0.0121 | 0.1000 |
| delta | own | 4-10 | - | 0.0000 | M | 1146 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 4-10 | linear | 0.0000 | tau | 1146 | -0.0125 | -0.0178 | -0.0113 | -0.0072 | -0.0040 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.5000 | tau | 1146 | -0.0125 | -0.0178 | -0.0113 | -0.0072 | -0.0040 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.8000 | tau | 1146 | -0.0125 | -0.0178 | -0.0113 | -0.0072 | -0.0040 | 0.0000 | 0.5000 |
| delta | own | 4-10 | concave | 0.0000 | tau | 1146 | -0.0071 | -0.0103 | -0.0063 | -0.0040 | -0.0022 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.5000 | tau | 1146 | -0.0071 | -0.0103 | -0.0063 | -0.0040 | -0.0022 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.8000 | tau | 1146 | -0.0071 | -0.0103 | -0.0063 | -0.0040 | -0.0022 | 0.0000 | 0.6599 |
| delta | own | 4-10 | convex | 0.0000 | tau | 1146 | -0.0191 | -0.0266 | -0.0182 | -0.0116 | -0.0062 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.5000 | tau | 1146 | -0.0191 | -0.0266 | -0.0182 | -0.0116 | -0.0062 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.8000 | tau | 1146 | -0.0191 | -0.0266 | -0.0182 | -0.0116 | -0.0062 | 0.0000 | 0.3391 |
| delta | own | 4-10 | top3_stress | 0.0000 | tau | 1146 | -0.0171 | -0.0226 | -0.0160 | -0.0102 | -0.0046 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.5000 | tau | 1146 | -0.0171 | -0.0226 | -0.0160 | -0.0102 | -0.0046 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.8000 | tau | 1146 | -0.0171 | -0.0226 | -0.0160 | -0.0102 | -0.0046 | 0.0000 | 0.1000 |
| delta | own | 11-16 | - | 0.0000 | M | 978 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 11-16 | linear | 0.0000 | tau | 978 | 0.0017 | -0.0094 | 0.0015 | 0.0102 | 0.0188 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.5000 | tau | 978 | 0.0017 | -0.0094 | 0.0015 | 0.0102 | 0.0188 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.8000 | tau | 978 | 0.0017 | -0.0094 | 0.0015 | 0.0102 | 0.0188 | 0.0000 | 0.5000 |
| delta | own | 11-16 | concave | 0.0000 | tau | 978 | 0.0006 | -0.0061 | 0.0005 | 0.0056 | 0.0111 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.5000 | tau | 978 | 0.0006 | -0.0061 | 0.0005 | 0.0056 | 0.0111 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.8000 | tau | 978 | 0.0006 | -0.0061 | 0.0005 | 0.0056 | 0.0111 | 0.0000 | 0.6599 |
| delta | own | 11-16 | convex | 0.0000 | tau | 978 | 0.0046 | -0.0111 | 0.0042 | 0.0168 | 0.0289 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.5000 | tau | 978 | 0.0046 | -0.0111 | 0.0042 | 0.0168 | 0.0289 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.8000 | tau | 978 | 0.0046 | -0.0111 | 0.0042 | 0.0168 | 0.0289 | 0.0000 | 0.3391 |
| delta | own | 11-16 | top3_stress | 0.0000 | tau | 978 | 0.0104 | 0.0003 | 0.0099 | 0.0175 | 0.0267 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.5000 | tau | 978 | 0.0104 | 0.0003 | 0.0099 | 0.0175 | 0.0267 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.8000 | tau | 978 | 0.0104 | 0.0003 | 0.0099 | 0.0175 | 0.0267 | 0.0000 | 0.1000 |
| delta | own | 17-30 | - | 0.0000 | M | 2277 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 17-30 | linear | 0.0000 | tau | 2277 | 0.0050 | 0.0000 | 0.0002 | 0.0079 | 0.0166 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.5000 | tau | 2277 | 0.0050 | 0.0000 | 0.0002 | 0.0079 | 0.0166 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.8000 | tau | 2277 | 0.0050 | 0.0000 | 0.0002 | 0.0079 | 0.0166 | 0.0009 | 0.5000 |
| delta | own | 17-30 | concave | 0.0000 | tau | 2277 | 0.0030 | 0.0000 | 0.0001 | 0.0049 | 0.0102 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.5000 | tau | 2277 | 0.0030 | 0.0000 | 0.0001 | 0.0049 | 0.0102 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.8000 | tau | 2277 | 0.0030 | 0.0000 | 0.0001 | 0.0049 | 0.0102 | 0.0000 | 0.6599 |
| delta | own | 17-30 | convex | 0.0000 | tau | 2277 | 0.0072 | 0.0000 | 0.0004 | 0.0108 | 0.0238 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.5000 | tau | 2277 | 0.0072 | 0.0000 | 0.0004 | 0.0108 | 0.0238 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.8000 | tau | 2277 | 0.0072 | 0.0000 | 0.0004 | 0.0108 | 0.0238 | 0.0000 | 0.3391 |
| delta | own | 17-30 | top3_stress | 0.0000 | tau | 2277 | 0.0048 | 0.0000 | 0.0003 | 0.0065 | 0.0158 | 0.0000 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.5000 | tau | 2277 | 0.0048 | 0.0000 | 0.0003 | 0.0065 | 0.0158 | 0.0378 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.8000 | tau | 2277 | 0.0048 | 0.0000 | 0.0003 | 0.0065 | 0.0158 | 0.0378 | 0.1000 |

## T5_attr_seeding

| rule | portfolio | seed_group | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| old | actual | <0.01 | B | dominance_positive | 0.5289 | 0.4466 | 0.6023 | 1382 |
| old | actual | <0.01 | B | reversal | 0.0333 | 0.0160 | 0.0543 | 1382 |
| old | actual | <0.01 | B | negligible | 0.1650 | 0.1119 | 0.2181 | 1382 |
| old | actual | <0.01 | B | unresolved | 0.2728 | 0.2060 | 0.3435 | 1382 |
| old | actual | 0.01-0.05 | B | dominance_positive | 0.4693 | 0.3913 | 0.5512 | 326 |
| old | actual | 0.01-0.05 | B | reversal | 0.0429 | 0.0036 | 0.0954 | 326 |
| old | actual | 0.01-0.05 | B | negligible | 0.2485 | 0.0912 | 0.3529 | 326 |
| old | actual | 0.01-0.05 | B | unresolved | 0.2393 | 0.1336 | 0.4038 | 326 |
| old | actual | >=0.05 | B | dominance_positive | 0.4683 | 0.3932 | 0.5387 | 3188 |
| old | actual | >=0.05 | B | reversal | 0.0229 | 0.0060 | 0.0545 | 3188 |
| old | actual | >=0.05 | B | negligible | 0.2387 | 0.1652 | 0.3056 | 3188 |
| old | actual | >=0.05 | B | unresolved | 0.2701 | 0.2248 | 0.3116 | 3188 |
| old | own | <0.01 | B | dominance_positive | 0.7229 | 0.6419 | 0.7969 | 1382 |
| old | own | <0.01 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 1382 |
| old | own | <0.01 | B | negligible | 0.0767 | 0.0340 | 0.1258 | 1382 |
| old | own | <0.01 | B | unresolved | 0.2004 | 0.1450 | 0.2757 | 1382 |
| old | own | 0.01-0.05 | B | dominance_positive | 0.5491 | 0.4170 | 0.6667 | 326 |
| old | own | 0.01-0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 326 |
| old | own | 0.01-0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 326 |
| old | own | 0.01-0.05 | B | unresolved | 0.4509 | 0.3333 | 0.5830 | 326 |
| old | own | >=0.05 | B | dominance_positive | 0.5458 | 0.5050 | 0.5906 | 3188 |
| old | own | >=0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 3188 |
| old | own | >=0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 3188 |
| old | own | >=0.05 | B | unresolved | 0.4542 | 0.4094 | 0.4950 | 3188 |
| new | actual | <0.01 | B | dominance_positive | 0.1027 | 0.0504 | 0.1778 | 1382 |
| new | actual | <0.01 | B | reversal | 0.3437 | 0.2144 | 0.4717 | 1382 |
| new | actual | <0.01 | B | negligible | 0.4038 | 0.2996 | 0.5214 | 1382 |
| new | actual | <0.01 | B | unresolved | 0.1498 | 0.1089 | 0.1979 | 1382 |
| new | actual | 0.01-0.05 | B | dominance_positive | 0.4049 | 0.2795 | 0.5167 | 326 |
| new | actual | 0.01-0.05 | B | reversal | 0.0245 | 0.0028 | 0.0698 | 326 |
| new | actual | 0.01-0.05 | B | negligible | 0.3497 | 0.1614 | 0.4816 | 326 |
| new | actual | 0.01-0.05 | B | unresolved | 0.2209 | 0.1250 | 0.3910 | 326 |
| new | actual | >=0.05 | B | dominance_positive | 0.5125 | 0.4457 | 0.5794 | 3188 |
| new | actual | >=0.05 | B | reversal | 0.0289 | 0.0126 | 0.0497 | 3188 |
| new | actual | >=0.05 | B | negligible | 0.2205 | 0.1562 | 0.2888 | 3188 |
| new | actual | >=0.05 | B | unresolved | 0.2381 | 0.1797 | 0.2890 | 3188 |
| new | own | <0.01 | B | dominance_positive | 0.1259 | 0.0664 | 0.2037 | 1382 |
| new | own | <0.01 | B | reversal | 0.3582 | 0.2072 | 0.5035 | 1382 |
| new | own | <0.01 | B | negligible | 0.4595 | 0.3473 | 0.5583 | 1382 |
| new | own | <0.01 | B | unresolved | 0.0564 | 0.0363 | 0.0828 | 1382 |
| new | own | 0.01-0.05 | B | dominance_positive | 0.5337 | 0.4000 | 0.6871 | 326 |
| new | own | 0.01-0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 326 |
| new | own | 0.01-0.05 | B | negligible | 0.0736 | 0.0117 | 0.1369 | 326 |
| new | own | 0.01-0.05 | B | unresolved | 0.3926 | 0.2741 | 0.5316 | 326 |
| new | own | >=0.05 | B | dominance_positive | 0.5743 | 0.5302 | 0.6240 | 3188 |
| new | own | >=0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 3188 |
| new | own | >=0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 3188 |
| new | own | >=0.05 | B | unresolved | 0.4257 | 0.3760 | 0.4698 | 3188 |

## T5_attr_ledger_features

| rule | feature | value | n | reversal_share | lo99 | hi99 |
|---|---|---|---|---|---|---|
| old | holds_conditional_other | True | 2100 | 0.0629 | 0.0327 | 0.1043 |
| old | holds_conditional_other | False | 2796 | 0.0004 | 0.0000 | 0.0022 |
| old | holds_opponent_pick | True | 157 | 0.3376 | 0.2061 | 0.4774 |
| old | holds_opponent_pick | False | 4739 | 0.0169 | 0.0065 | 0.0370 |
| old | holds_pooled_pick | True | 1562 | 0.0435 | 0.0093 | 0.1263 |
| old | holds_pooled_pick | False | 3334 | 0.0195 | 0.0098 | 0.0307 |
| old | self_restricted | True | 410 | 0.0439 | 0.0000 | 0.1018 |
| old | self_restricted | False | 4486 | 0.0256 | 0.0119 | 0.0446 |
| old | opp_restricted | True | 410 | 0.0293 | 0.0000 | 0.0684 |
| old | opp_restricted | False | 4486 | 0.0270 | 0.0137 | 0.0476 |
| old | holds_conditional_other_state | True | 1884 | 0.0695 | 0.0360 | 0.1238 |
| old | holds_conditional_other_state | False | 3012 | 0.0007 | 0.0000 | 0.0034 |
| old | holds_opponent_pick_state | True | 141 | 0.3759 | 0.2295 | 0.5267 |
| old | holds_opponent_pick_state | False | 4755 | 0.0168 | 0.0065 | 0.0369 |
| new | holds_conditional_other | True | 2100 | 0.1519 | 0.0917 | 0.2014 |
| new | holds_conditional_other | False | 2796 | 0.0916 | 0.0390 | 0.1476 |
| new | holds_opponent_pick | True | 157 | 0.3885 | 0.2658 | 0.5529 |
| new | holds_opponent_pick | False | 4739 | 0.1085 | 0.0602 | 0.1426 |
| new | holds_pooled_pick | True | 1562 | 0.1133 | 0.0388 | 0.1977 |
| new | holds_pooled_pick | False | 3334 | 0.1194 | 0.0696 | 0.1812 |
| new | self_restricted | True | 410 | 0.2049 | 0.0444 | 0.3806 |
| new | self_restricted | False | 4486 | 0.1095 | 0.0541 | 0.1542 |
| new | opp_restricted | True | 410 | 0.1024 | 0.0435 | 0.1716 |
| new | opp_restricted | False | 4486 | 0.1188 | 0.0698 | 0.1531 |
| new | holds_conditional_other_state | True | 1992 | 0.1436 | 0.0794 | 0.1912 |
| new | holds_conditional_other_state | False | 2904 | 0.0995 | 0.0474 | 0.1552 |
| new | holds_opponent_pick_state | True | 149 | 0.3960 | 0.2699 | 0.5578 |
| new | holds_opponent_pick_state | False | 4747 | 0.1087 | 0.0608 | 0.1425 |

## T5_6_transitions

| portfolio | old | new | count |
|---|---|---|---|
| actual | dominance_positive | dominance_positive | 1608 |
| actual | dominance_positive | negligible | 309 |
| actual | dominance_positive | reversal | 357 |
| actual | dominance_positive | unresolved | 103 |
| actual | negligible | dominance_positive | 97 |
| actual | negligible | negligible | 963 |
| actual | negligible | reversal | 5 |
| actual | negligible | unresolved | 5 |
| actual | reversal | dominance_positive | 12 |
| actual | reversal | negligible | 10 |
| actual | reversal | reversal | 90 |
| actual | reversal | unresolved | 21 |
| actual | unresolved | dominance_positive | 191 |
| actual | unresolved | negligible | 93 |
| actual | unresolved | reversal | 123 |
| actual | unresolved | unresolved | 909 |
| own | dominance_positive | dominance_positive | 1972 |
| own | dominance_positive | negligible | 447 |
| own | dominance_positive | reversal | 375 |
| own | dominance_positive | unresolved | 124 |
| own | negligible | dominance_positive | 1 |
| own | negligible | negligible | 105 |
| own | unresolved | dominance_positive | 206 |
| own | unresolved | negligible | 107 |
| own | unresolved | reversal | 120 |
| own | unresolved | unresolved | 1439 |

## T5_headline_reversal_diff

| contrast | portfolio | verdict | share_a | share_b | diff | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| new_minus_old | actual | verdict_B | 0.1174 | 0.0272 | 0.0903 | 0.0462 | 0.1275 | 4896 |
| new_minus_old | actual | verdict_B_pm | 0.0976 | 0.0180 | 0.0797 | 0.0447 | 0.1053 | 4896 |
| new_minus_old | own | verdict_B | 0.1011 | 0.0000 | 0.1011 | 0.0533 | 0.1436 | 4896 |
| new_minus_old | own | verdict_B_pm | 0.0929 | 0.0000 | 0.0929 | 0.0481 | 0.1352 | 4896 |
| actual_minus_own | old | verdict_B | 0.0272 | 0.0000 | 0.0272 | 0.0139 | 0.0483 | 4896 |
| actual_minus_own | new | verdict_B | 0.1174 | 0.1011 | 0.0163 | 0.0033 | 0.0318 | 4896 |

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
| new | linear | both_lose | 0.2884 | 0.1798 | 0.4137 | 706 | 0.2465 |
| new | linear | both_win | 0.0061 | 0.0004 | 0.0145 | 15 | 0.1333 |
| new | linear | normal | 0.4016 | 0.3338 | 0.4726 | 983 | 0.6088 |
| new | linear | opposed | 0.0539 | 0.0148 | 0.0958 | 132 | 0.3740 |
| new | linear | one_sided_win | 0.0507 | 0.0162 | 0.0980 | 124 | 0.7213 |
| new | linear | no_own_stake | 0.1993 | 0.1045 | 0.2921 | 488 | 1.0000 |
| new | concave | both_lose | 0.2937 | 0.1876 | 0.4011 | 719 | 0.2976 |
| new | concave | both_win | 0.0053 | 0.0000 | 0.0130 | 13 | 0.3077 |
| new | concave | normal | 0.4236 | 0.3795 | 0.4731 | 1037 | 0.6628 |
| new | concave | opposed | 0.0347 | 0.0124 | 0.0577 | 85 | 0.4588 |
| new | concave | one_sided_win | 0.0355 | 0.0133 | 0.0648 | 87 | 0.7126 |
| new | concave | no_own_stake | 0.2071 | 0.1214 | 0.2936 | 507 | 1.0000 |
| new | convex | both_lose | 0.2533 | 0.1629 | 0.3587 | 620 | 0.2097 |
| new | convex | both_win | 0.0090 | 0.0023 | 0.0182 | 22 | 0.1364 |
| new | convex | normal | 0.3958 | 0.3434 | 0.4539 | 969 | 0.4995 |
| new | convex | opposed | 0.0674 | 0.0296 | 0.1100 | 165 | 0.2545 |
| new | convex | one_sided_win | 0.0678 | 0.0286 | 0.1128 | 166 | 0.6012 |
| new | convex | no_own_stake | 0.2067 | 0.1146 | 0.2954 | 506 | 1.0000 |
| new | top3_stress | both_lose | 0.1225 | 0.0765 | 0.1754 | 300 | 0.0367 |
| new | top3_stress | both_win | 0.0098 | 0.0021 | 0.0213 | 24 | 0.1250 |
| new | top3_stress | normal | 0.3587 | 0.2902 | 0.4390 | 878 | 0.2215 |
| new | top3_stress | opposed | 0.0572 | 0.0260 | 0.0875 | 140 | 0.0500 |
| new | top3_stress | one_sided_win | 0.1062 | 0.0497 | 0.1597 | 260 | 0.2449 |
| new | top3_stress | no_own_stake | 0.3456 | 0.2669 | 0.4115 | 846 | 1.0000 |

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
| old | concave | hhi | 2399 | 0.3086 | 0.2164 | 0.2818 | 0.3761 | 0.4841 |
| old | concave | n_material | 2448 | 5.9404 | 4.0000 | 6.0000 | 8.0000 | 10.0000 |
| old | concave | mean_abs_third | 2448 | 0.0019 | 0.0008 | 0.0016 | 0.0025 | 0.0035 |
| old | concave | mean_abs_third_raw | 2448 | 0.0022 | 0.0012 | 0.0019 | 0.0028 | 0.0038 |
| old | convex | tp_share | 2408 | 0.5037 | 0.3464 | 0.4828 | 0.6772 | 0.9317 |
| old | convex | tp_share_raw | 2434 | 0.5932 | 0.4852 | 0.5399 | 0.7312 | 0.9281 |
| old | convex | hhi | 2408 | 0.3635 | 0.2422 | 0.3179 | 0.4097 | 0.5266 |
| old | convex | n_material | 2448 | 5.5261 | 3.0000 | 5.5000 | 7.0000 | 9.0000 |
| old | convex | mean_abs_third | 2448 | 0.0013 | 0.0005 | 0.0011 | 0.0018 | 0.0027 |
| old | convex | mean_abs_third_raw | 2448 | 0.0017 | 0.0009 | 0.0015 | 0.0022 | 0.0030 |
| old | top3_stress | tp_share | 1774 | 0.3688 | 0.1194 | 0.3898 | 0.4784 | 1.0000 |
| old | top3_stress | tp_share_raw | 1955 | 0.5311 | 0.4815 | 0.5014 | 0.5229 | 0.9088 |
| old | top3_stress | hhi | 1774 | 0.5460 | 0.3638 | 0.4835 | 0.6003 | 1.0000 |
| old | top3_stress | n_material | 2448 | 2.2353 | 0.0000 | 2.0000 | 4.0000 | 5.0000 |
| old | top3_stress | mean_abs_third | 2448 | 0.0003 | 0.0000 | 0.0001 | 0.0005 | 0.0009 |
| old | top3_stress | mean_abs_third_raw | 2448 | 0.0005 | 0.0001 | 0.0004 | 0.0008 | 0.0011 |
| new | linear | tp_share | 2289 | 0.5921 | 0.4323 | 0.5219 | 0.7922 | 1.0000 |
| new | linear | tp_share_raw | 2353 | 0.6369 | 0.5007 | 0.5779 | 0.8059 | 0.9792 |
| new | linear | hhi | 2289 | 0.3177 | 0.2243 | 0.2982 | 0.3740 | 0.5000 |
| new | linear | n_material | 2448 | 5.8415 | 3.0000 | 6.0000 | 8.0000 | 10.0000 |
| new | linear | mean_abs_third | 2448 | 0.0017 | 0.0006 | 0.0014 | 0.0024 | 0.0036 |
| new | linear | mean_abs_third_raw | 2448 | 0.0020 | 0.0009 | 0.0017 | 0.0027 | 0.0039 |
| new | concave | tp_share | 2286 | 0.6113 | 0.4547 | 0.5524 | 0.8172 | 1.0000 |
| new | concave | tp_share_raw | 2360 | 0.6515 | 0.5036 | 0.6057 | 0.8211 | 0.9833 |
| new | concave | hhi | 2286 | 0.3062 | 0.2143 | 0.2827 | 0.3710 | 0.4879 |
| new | concave | n_material | 2448 | 5.8231 | 4.0000 | 6.0000 | 8.0000 | 10.0000 |
| new | concave | mean_abs_third | 2448 | 0.0018 | 0.0008 | 0.0015 | 0.0025 | 0.0036 |
| new | concave | mean_abs_third_raw | 2448 | 0.0020 | 0.0011 | 0.0018 | 0.0028 | 0.0038 |
| new | convex | tp_share | 2224 | 0.5334 | 0.3845 | 0.4908 | 0.7244 | 1.0000 |
| new | convex | tp_share_raw | 2328 | 0.6188 | 0.5000 | 0.5488 | 0.7594 | 0.9732 |
| new | convex | hhi | 2224 | 0.3931 | 0.2643 | 0.3337 | 0.4380 | 0.6159 |
| new | convex | n_material | 2448 | 4.6605 | 2.0000 | 5.0000 | 7.0000 | 8.3000 |
| new | convex | mean_abs_third | 2448 | 0.0014 | 0.0003 | 0.0009 | 0.0020 | 0.0033 |
| new | convex | mean_abs_third_raw | 2448 | 0.0017 | 0.0005 | 0.0013 | 0.0023 | 0.0036 |
| new | top3_stress | tp_share | 1836 | 0.4646 | 0.3167 | 0.4438 | 0.5408 | 1.0000 |
| new | top3_stress | tp_share_raw | 2000 | 0.5842 | 0.4952 | 0.5056 | 0.6504 | 0.9915 |
| new | top3_stress | hhi | 1836 | 0.4771 | 0.3385 | 0.4194 | 0.5146 | 1.0000 |
| new | top3_stress | n_material | 2448 | 2.5078 | 0.7500 | 2.0000 | 4.0000 | 5.0000 |
| new | top3_stress | mean_abs_third | 2448 | 0.0005 | 0.0000 | 0.0003 | 0.0007 | 0.0013 |
| new | top3_stress | mean_abs_third_raw | 2448 | 0.0007 | 0.0001 | 0.0005 | 0.0009 | 0.0015 |
| new_minus_old | linear | tp_share | 2286 | 0.0225 | -0.0235 | 0.0067 | 0.0803 | 0.1684 |
| new_minus_old | linear | hhi | 2286 | 0.0243 | -0.0325 | 0.0009 | 0.0606 | 0.1479 |
| new_minus_old | linear | mean_abs_third | 2448 | -0.0000 | -0.0004 | 0.0000 | 0.0004 | 0.0011 |
| new_minus_old | concave | tp_share | 2277 | 0.0161 | -0.0245 | 0.0014 | 0.0703 | 0.1653 |
| new_minus_old | concave | hhi | 2277 | 0.0056 | -0.0424 | -0.0000 | 0.0419 | 0.1190 |
| new_minus_old | concave | mean_abs_third | 2448 | -0.0001 | -0.0003 | 0.0000 | 0.0004 | 0.0009 |
| new_minus_old | convex | tp_share | 2224 | 0.0233 | -0.0369 | 0.0089 | 0.1038 | 0.2176 |
| new_minus_old | convex | hhi | 2224 | 0.0379 | -0.0512 | 0.0003 | 0.0882 | 0.2056 |
| new_minus_old | convex | mean_abs_third | 2448 | 0.0001 | -0.0005 | 0.0000 | 0.0006 | 0.0014 |
| new_minus_old | top3_stress | tp_share | 1508 | 0.1142 | -0.0178 | 0.0682 | 0.3098 | 0.4681 |
| new_minus_old | top3_stress | hhi | 1508 | -0.1229 | -0.3332 | -0.0617 | 0.0653 | 0.2235 |
| new_minus_old | top3_stress | mean_abs_third | 2448 | 0.0002 | -0.0002 | 0.0000 | 0.0005 | 0.0011 |

## H2

| curve | sample | n_games | mean_diff_new_minus_old | lo99 | hi99 | registered | supported |
|---|---|---|---|---|---|---|---|
| linear | registered | 2048 | -0.0000 | -0.0003 | 0.0002 | True | False |
| linear | state_conditional | 1898 | -0.0000 | -0.0003 | 0.0002 | False | False |
| concave | registered | 2048 | -0.0001 | -0.0004 | 0.0002 | False | False |
| concave | state_conditional | 1898 | -0.0001 | -0.0004 | 0.0002 | False | False |
| convex | registered | 2048 | 0.0001 | -0.0001 | 0.0003 | False | False |
| convex | state_conditional | 1898 | 0.0001 | -0.0001 | 0.0003 | False | False |
| top3_stress | registered | 2048 | 0.0002 | 0.0001 | 0.0004 | False | True |
| top3_stress | state_conditional | 1898 | 0.0002 | 0.0001 | 0.0004 | False | True |

## F5_2_network_edges

10440 rows in `F5_2_network_edges.csv`.

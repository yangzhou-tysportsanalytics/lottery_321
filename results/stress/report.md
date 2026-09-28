# Registered analysis output

tag `stress`; exclude_imprecise=False; states=81

## T5_0_diagnostics

| states | games | stopped_2000 | stopped_8000 | stopped_32000 | missed_target | n_worlds_match | max_halfwidth_linear | max_halfwidth_linear_rules_only | max_halfwidth_delta_linear | p95_halfwidth_linear | max_q_total_dev | max_per_slot_dev | per_slot_noise_scale | max_own_slot_dev | max_zero_sum_dev |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 81 | 626 | 2 | 3 | 38 | 38 | 2000 | 0.0063 | 0.0062 | 0.0063 | 0.0046 | 0.0000 | 0.0094 | 0.0112 | 0.0000 | 0.0050 |

## T5_0b_zero_sum_by_curve

| curve | rule | max_zero_sum_dev | mean_zero_sum_dev | n_games |
|---|---|---|---|---|
| linear | old | 0.0007 | 0.0001 | 626 |
| linear | new | 0.0008 | 0.0001 | 626 |
| concave | old | 0.0003 | 0.0000 | 626 |
| concave | new | 0.0005 | 0.0001 | 626 |
| convex | old | 0.0012 | 0.0001 | 626 |
| convex | new | 0.0013 | 0.0002 | 626 |
| top3_stress | old | 0.0050 | 0.0003 | 626 |
| top3_stress | new | 0.0027 | 0.0003 | 626 |

## T5_0c_verdict_by_look

| rule | portfolio | stopped_at | verdict_B | verdict_B_pm | count |
|---|---|---|---|---|---|
| delta | actual | 2000 | dominance_positive | dominance_positive | 1 |
| delta | actual | 2000 | negligible | negligible | 3 |
| delta | actual | 2000 | reversal | reversal | 5 |
| delta | actual | 2000 | unresolved | unresolved | 1 |
| delta | actual | 32000 | dominance_positive | dominance_positive | 36 |
| delta | actual | 32000 | dominance_positive | unresolved | 26 |
| delta | actual | 32000 | negligible | negligible | 168 |
| delta | actual | 32000 | negligible | unresolved | 10 |
| delta | actual | 32000 | reversal | reversal | 266 |
| delta | actual | 32000 | reversal | unresolved | 39 |
| delta | actual | 32000 | unresolved | unresolved | 15 |
| delta | actual | 8000 | dominance_positive | unresolved | 1 |
| delta | actual | 8000 | negligible | negligible | 8 |
| delta | actual | 8000 | negligible | unresolved | 2 |
| delta | actual | 8000 | reversal | reversal | 14 |
| delta | actual | 8000 | unresolved | unresolved | 1 |
| delta | actual | missed | dominance_positive | dominance_positive | 55 |
| delta | actual | missed | dominance_positive | unresolved | 33 |
| delta | actual | missed | negligible | dominance_positive | 4 |
| delta | actual | missed | negligible | negligible | 190 |
| delta | actual | missed | negligible | unresolved | 6 |
| delta | actual | missed | reversal | reversal | 309 |
| delta | actual | missed | reversal | unresolved | 42 |
| delta | actual | missed | unresolved | unresolved | 17 |
| delta | own | 2000 | negligible | negligible | 1 |
| delta | own | 2000 | reversal | reversal | 8 |
| delta | own | 2000 | unresolved | unresolved | 1 |
| delta | own | 32000 | dominance_positive | dominance_positive | 3 |
| delta | own | 32000 | dominance_positive | unresolved | 32 |
| delta | own | 32000 | negligible | negligible | 104 |
| delta | own | 32000 | negligible | unresolved | 15 |
| delta | own | 32000 | reversal | reversal | 308 |
| delta | own | 32000 | reversal | unresolved | 69 |
| delta | own | 32000 | unresolved | unresolved | 29 |
| delta | own | 8000 | dominance_positive | unresolved | 1 |
| delta | own | 8000 | negligible | negligible | 8 |
| delta | own | 8000 | reversal | reversal | 15 |
| delta | own | 8000 | unresolved | unresolved | 2 |
| delta | own | missed | dominance_positive | dominance_positive | 5 |
| delta | own | missed | dominance_positive | unresolved | 35 |
| delta | own | missed | negligible | negligible | 135 |
| delta | own | missed | negligible | unresolved | 11 |
| delta | own | missed | reversal | reversal | 369 |
| delta | own | missed | reversal | unresolved | 68 |
| delta | own | missed | unresolved | unresolved | 33 |
| new | actual | 2000 | dominance_positive | dominance_positive | 3 |
| new | actual | 2000 | negligible | negligible | 3 |
| new | actual | 2000 | reversal | reversal | 3 |
| new | actual | 2000 | unresolved | unresolved | 1 |
| new | actual | 32000 | dominance_positive | dominance_positive | 297 |
| new | actual | 32000 | dominance_positive | unresolved | 17 |
| new | actual | 32000 | negligible | dominance_positive | 4 |
| new | actual | 32000 | negligible | negligible | 144 |
| new | actual | 32000 | negligible | unresolved | 8 |
| new | actual | 32000 | reversal | reversal | 64 |
| new | actual | 32000 | reversal | unresolved | 11 |
| new | actual | 32000 | unresolved | unresolved | 15 |
| new | actual | 8000 | dominance_positive | dominance_positive | 15 |
| new | actual | 8000 | dominance_positive | unresolved | 1 |
| new | actual | 8000 | negligible | negligible | 4 |
| new | actual | 8000 | reversal | reversal | 5 |
| new | actual | 8000 | unresolved | unresolved | 1 |
| new | actual | missed | dominance_positive | dominance_positive | 328 |
| new | actual | missed | dominance_positive | unresolved | 17 |
| new | actual | missed | negligible | dominance_positive | 8 |
| new | actual | missed | negligible | negligible | 202 |
| new | actual | missed | negligible | unresolved | 12 |
| new | actual | missed | reversal | reversal | 58 |
| new | actual | missed | reversal | unresolved | 13 |
| new | actual | missed | unresolved | unresolved | 18 |
| new | own | 2000 | dominance_positive | dominance_positive | 6 |
| new | own | 2000 | negligible | negligible | 1 |
| new | own | 2000 | reversal | reversal | 2 |
| new | own | 2000 | unresolved | unresolved | 1 |
| new | own | 32000 | dominance_positive | dominance_positive | 415 |
| new | own | 32000 | dominance_positive | unresolved | 10 |
| new | own | 32000 | negligible | dominance_positive | 6 |
| new | own | 32000 | negligible | negligible | 64 |
| new | own | 32000 | negligible | unresolved | 2 |
| new | own | 32000 | reversal | reversal | 58 |
| new | own | 32000 | reversal | unresolved | 2 |
| new | own | 32000 | unresolved | unresolved | 3 |
| new | own | 8000 | dominance_positive | dominance_positive | 19 |
| new | own | 8000 | negligible | negligible | 2 |
| new | own | 8000 | reversal | reversal | 5 |
| new | own | missed | dominance_positive | dominance_positive | 466 |
| new | own | missed | dominance_positive | unresolved | 6 |
| new | own | missed | negligible | dominance_positive | 5 |
| new | own | missed | negligible | negligible | 122 |
| new | own | missed | reversal | reversal | 49 |
| new | own | missed | reversal | unresolved | 5 |
| new | own | missed | unresolved | unresolved | 3 |
| old | actual | 2000 | dominance_positive | dominance_positive | 5 |
| old | actual | 2000 | negligible | negligible | 3 |
| old | actual | 2000 | reversal | reversal | 1 |
| old | actual | 2000 | unresolved | unresolved | 1 |
| old | actual | 32000 | dominance_positive | dominance_positive | 379 |
| old | actual | 32000 | dominance_positive | unresolved | 27 |
| old | actual | 32000 | negligible | negligible | 114 |
| old | actual | 32000 | negligible | unresolved | 5 |
| old | actual | 32000 | reversal | reversal | 17 |
| old | actual | 32000 | reversal | unresolved | 2 |
| old | actual | 32000 | unresolved | unresolved | 16 |
| old | actual | 8000 | dominance_positive | dominance_positive | 20 |
| old | actual | 8000 | dominance_positive | unresolved | 3 |
| old | actual | 8000 | negligible | negligible | 3 |
| old | actual | missed | dominance_positive | dominance_positive | 427 |
| old | actual | missed | dominance_positive | unresolved | 32 |
| old | actual | missed | negligible | dominance_positive | 4 |
| old | actual | missed | negligible | negligible | 148 |
| old | actual | missed | negligible | unresolved | 5 |
| old | actual | missed | reversal | reversal | 15 |
| old | actual | missed | reversal | unresolved | 10 |
| old | actual | missed | unresolved | unresolved | 15 |
| old | own | 2000 | dominance_positive | dominance_positive | 10 |
| old | own | 32000 | dominance_positive | dominance_positive | 539 |
| old | own | 32000 | dominance_positive | unresolved | 7 |
| old | own | 32000 | negligible | negligible | 12 |
| old | own | 32000 | negligible | unresolved | 2 |
| old | own | 8000 | dominance_positive | dominance_positive | 26 |
| old | own | missed | dominance_positive | dominance_positive | 620 |
| old | own | missed | dominance_positive | unresolved | 11 |
| old | own | missed | negligible | negligible | 25 |

## T5_0d_band_width

| rule | portfolio | measure | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| old | actual | band_ratio | 1252 | 1.3750 | 0.2188 | 1.2345 | 2.4196 | 2.8958 |
| old | actual | band_ratio_pm | 1252 | 5.3137 | 0.8751 | 4.8812 | 9.5623 | 11.3958 |
| old | own | band_ratio | 1252 | 2.0038 | 0.9089 | 2.3010 | 2.7205 | 3.0741 |
| old | own | band_ratio_pm | 1252 | 7.7038 | 3.4478 | 9.1571 | 10.8045 | 12.0412 |
| new | actual | band_ratio | 1252 | 1.0526 | 0.0695 | 0.6019 | 2.0761 | 2.6468 |
| new | actual | band_ratio_pm | 1252 | 4.0655 | 0.2769 | 2.2115 | 8.1925 | 10.5134 |
| new | own | band_ratio | 1252 | 1.5973 | 0.2539 | 1.9573 | 2.5898 | 2.9042 |
| new | own | band_ratio_pm | 1252 | 6.1237 | 0.9992 | 7.7558 | 10.3159 | 11.4678 |
| delta | actual | band_ratio | 1252 | 1.0450 | 0.0338 | 0.6996 | 1.7398 | 2.6338 |
| delta | actual | band_ratio_pm | 1252 | 4.0508 | 0.1352 | 2.7076 | 6.8841 | 10.3445 |
| delta | own | band_ratio | 1252 | 1.3565 | 0.4040 | 1.1074 | 2.3271 | 2.8983 |
| delta | own | band_ratio_pm | 1252 | 5.2353 | 1.6048 | 4.0892 | 9.2075 | 11.4479 |

## T5_1_verdicts

| rule | portfolio | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|
| old | actual | B | dominance_positive | 0.7133 | 0.6166 | 0.7973 | 1252 |
| old | actual | B | reversal | 0.0359 | 0.0146 | 0.0637 | 1252 |
| old | actual | B | negligible | 0.2252 | 0.1544 | 0.3063 | 1252 |
| old | actual | B | unresolved | 0.0256 | 0.0143 | 0.0398 | 1252 |
| old | actual | C | dominance_positive | 0.7133 | 0.6166 | 0.7973 | 1252 |
| old | actual | C | reversal | 0.0359 | 0.0146 | 0.0637 | 1252 |
| old | actual | C | negligible | 0.2252 | 0.1544 | 0.3063 | 1252 |
| old | actual | C | unresolved | 0.0256 | 0.0143 | 0.0398 | 1252 |
| old | actual | B_pm | dominance_positive | 0.6669 | 0.5679 | 0.7579 | 1252 |
| old | actual | B_pm | reversal | 0.0264 | 0.0096 | 0.0495 | 1252 |
| old | actual | B_pm | negligible | 0.2141 | 0.1468 | 0.2941 | 1252 |
| old | actual | B_pm | unresolved | 0.0927 | 0.0607 | 0.1254 | 1252 |
| old | actual | C_pm | dominance_positive | 0.6669 | 0.5679 | 0.7579 | 1252 |
| old | actual | C_pm | reversal | 0.0264 | 0.0096 | 0.0495 | 1252 |
| old | actual | C_pm | negligible | 0.2141 | 0.1468 | 0.2941 | 1252 |
| old | actual | C_pm | unresolved | 0.0927 | 0.0607 | 0.1254 | 1252 |
| old | own | B | dominance_positive | 0.9688 | 0.9264 | 0.9946 | 1252 |
| old | own | B | reversal | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | B | negligible | 0.0312 | 0.0054 | 0.0736 | 1252 |
| old | own | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | C | dominance_positive | 0.9688 | 0.9264 | 0.9946 | 1252 |
| old | own | C | reversal | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | C | negligible | 0.0312 | 0.0054 | 0.0736 | 1252 |
| old | own | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | B_pm | dominance_positive | 0.9545 | 0.9026 | 0.9847 | 1252 |
| old | own | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | B_pm | negligible | 0.0296 | 0.0038 | 0.0725 | 1252 |
| old | own | B_pm | unresolved | 0.0160 | 0.0034 | 0.0314 | 1252 |
| old | own | C_pm | dominance_positive | 0.9553 | 0.9032 | 0.9855 | 1252 |
| old | own | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | C_pm | negligible | 0.0296 | 0.0038 | 0.0725 | 1252 |
| old | own | C_pm | unresolved | 0.0152 | 0.0033 | 0.0297 | 1252 |
| new | actual | B | dominance_positive | 0.5415 | 0.4324 | 0.6393 | 1252 |
| new | actual | B | reversal | 0.1230 | 0.0633 | 0.1597 | 1252 |
| new | actual | B | negligible | 0.3075 | 0.2135 | 0.4080 | 1252 |
| new | actual | B | unresolved | 0.0280 | 0.0111 | 0.0581 | 1252 |
| new | actual | C | dominance_positive | 0.5415 | 0.4324 | 0.6393 | 1252 |
| new | actual | C | reversal | 0.1222 | 0.0622 | 0.1590 | 1252 |
| new | actual | C | negligible | 0.3075 | 0.2135 | 0.4080 | 1252 |
| new | actual | C | unresolved | 0.0288 | 0.0117 | 0.0584 | 1252 |
| new | actual | B_pm | dominance_positive | 0.5232 | 0.4144 | 0.6209 | 1252 |
| new | actual | B_pm | reversal | 0.1038 | 0.0538 | 0.1362 | 1252 |
| new | actual | B_pm | negligible | 0.2819 | 0.1948 | 0.3806 | 1252 |
| new | actual | B_pm | unresolved | 0.0911 | 0.0508 | 0.1509 | 1252 |
| new | actual | C_pm | dominance_positive | 0.5232 | 0.4144 | 0.6209 | 1252 |
| new | actual | C_pm | reversal | 0.1038 | 0.0538 | 0.1362 | 1252 |
| new | actual | C_pm | negligible | 0.2819 | 0.1948 | 0.3806 | 1252 |
| new | actual | C_pm | unresolved | 0.0911 | 0.0508 | 0.1509 | 1252 |
| new | own | B | dominance_positive | 0.7364 | 0.6607 | 0.8167 | 1252 |
| new | own | B | reversal | 0.0966 | 0.0469 | 0.1361 | 1252 |
| new | own | B | negligible | 0.1613 | 0.0966 | 0.2320 | 1252 |
| new | own | B | unresolved | 0.0056 | 0.0000 | 0.0139 | 1252 |
| new | own | C | dominance_positive | 0.7364 | 0.6607 | 0.8167 | 1252 |
| new | own | C | reversal | 0.0966 | 0.0469 | 0.1361 | 1252 |
| new | own | C | negligible | 0.1613 | 0.0966 | 0.2320 | 1252 |
| new | own | C | unresolved | 0.0056 | 0.0000 | 0.0139 | 1252 |
| new | own | B_pm | dominance_positive | 0.7324 | 0.6550 | 0.8162 | 1252 |
| new | own | B_pm | reversal | 0.0911 | 0.0436 | 0.1300 | 1252 |
| new | own | B_pm | negligible | 0.1510 | 0.0847 | 0.2232 | 1252 |
| new | own | B_pm | unresolved | 0.0256 | 0.0092 | 0.0416 | 1252 |
| new | own | C_pm | dominance_positive | 0.7332 | 0.6560 | 0.8162 | 1252 |
| new | own | C_pm | reversal | 0.0911 | 0.0436 | 0.1300 | 1252 |
| new | own | C_pm | negligible | 0.1510 | 0.0847 | 0.2232 | 1252 |
| new | own | C_pm | unresolved | 0.0248 | 0.0089 | 0.0401 | 1252 |
| delta | actual | B | dominance_positive | 0.1214 | 0.0738 | 0.1689 | 1252 |
| delta | actual | B | reversal | 0.5391 | 0.4834 | 0.5908 | 1252 |
| delta | actual | B | negligible | 0.3123 | 0.2558 | 0.3758 | 1252 |
| delta | actual | B | unresolved | 0.0272 | 0.0127 | 0.0448 | 1252 |
| delta | actual | C | dominance_positive | 0.1214 | 0.0738 | 0.1689 | 1252 |
| delta | actual | C | reversal | 0.5391 | 0.4834 | 0.5908 | 1252 |
| delta | actual | C | negligible | 0.3123 | 0.2558 | 0.3758 | 1252 |
| delta | actual | C | unresolved | 0.0272 | 0.0127 | 0.0448 | 1252 |
| delta | actual | B_pm | dominance_positive | 0.0767 | 0.0419 | 0.1148 | 1252 |
| delta | actual | B_pm | reversal | 0.4744 | 0.4208 | 0.5232 | 1252 |
| delta | actual | B_pm | negligible | 0.2947 | 0.2392 | 0.3484 | 1252 |
| delta | actual | B_pm | unresolved | 0.1542 | 0.1135 | 0.2000 | 1252 |
| delta | actual | C_pm | dominance_positive | 0.0767 | 0.0419 | 0.1148 | 1252 |
| delta | actual | C_pm | reversal | 0.4744 | 0.4208 | 0.5232 | 1252 |
| delta | actual | C_pm | negligible | 0.2947 | 0.2392 | 0.3484 | 1252 |
| delta | actual | C_pm | unresolved | 0.1542 | 0.1135 | 0.2000 | 1252 |
| delta | own | B | dominance_positive | 0.0607 | 0.0425 | 0.0786 | 1252 |
| delta | own | B | reversal | 0.6685 | 0.6256 | 0.7234 | 1252 |
| delta | own | B | negligible | 0.2188 | 0.1661 | 0.2685 | 1252 |
| delta | own | B | unresolved | 0.0519 | 0.0326 | 0.0728 | 1252 |
| delta | own | C | dominance_positive | 0.0607 | 0.0425 | 0.0786 | 1252 |
| delta | own | C | reversal | 0.6685 | 0.6256 | 0.7234 | 1252 |
| delta | own | C | negligible | 0.2188 | 0.1661 | 0.2685 | 1252 |
| delta | own | C | unresolved | 0.0519 | 0.0326 | 0.0728 | 1252 |
| delta | own | B_pm | dominance_positive | 0.0064 | 0.0007 | 0.0166 | 1252 |
| delta | own | B_pm | reversal | 0.5591 | 0.5073 | 0.6118 | 1252 |
| delta | own | B_pm | negligible | 0.1981 | 0.1439 | 0.2478 | 1252 |
| delta | own | B_pm | unresolved | 0.2364 | 0.1932 | 0.2838 | 1252 |
| delta | own | C_pm | dominance_positive | 0.0064 | 0.0007 | 0.0166 | 1252 |
| delta | own | C_pm | reversal | 0.5591 | 0.5073 | 0.6118 | 1252 |
| delta | own | C_pm | negligible | 0.1981 | 0.1439 | 0.2478 | 1252 |
| delta | own | C_pm | unresolved | 0.2364 | 0.1932 | 0.2838 | 1252 |

## T5_2_verdicts_by_band

| rule | portfolio | band | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| old | actual | 1-3 | B | dominance_positive | 0.7656 | 0.5854 | 0.9051 | 128 |
| old | actual | 1-3 | B | reversal | 0.0312 | 0.0000 | 0.0887 | 128 |
| old | actual | 1-3 | B | negligible | 0.0703 | 0.0000 | 0.1862 | 128 |
| old | actual | 1-3 | B | unresolved | 0.1328 | 0.0301 | 0.2581 | 128 |
| old | actual | 1-3 | C | dominance_positive | 0.7656 | 0.5854 | 0.9051 | 128 |
| old | actual | 1-3 | C | reversal | 0.0312 | 0.0000 | 0.0887 | 128 |
| old | actual | 1-3 | C | negligible | 0.0703 | 0.0000 | 0.1862 | 128 |
| old | actual | 1-3 | C | unresolved | 0.1328 | 0.0301 | 0.2581 | 128 |
| old | actual | 1-3 | B_pm | dominance_positive | 0.6406 | 0.3873 | 0.8548 | 128 |
| old | actual | 1-3 | B_pm | reversal | 0.0234 | 0.0000 | 0.0682 | 128 |
| old | actual | 1-3 | B_pm | negligible | 0.0703 | 0.0000 | 0.1862 | 128 |
| old | actual | 1-3 | B_pm | unresolved | 0.2656 | 0.0764 | 0.4385 | 128 |
| old | actual | 1-3 | C_pm | dominance_positive | 0.6406 | 0.3873 | 0.8548 | 128 |
| old | actual | 1-3 | C_pm | reversal | 0.0234 | 0.0000 | 0.0682 | 128 |
| old | actual | 1-3 | C_pm | negligible | 0.0703 | 0.0000 | 0.1862 | 128 |
| old | actual | 1-3 | C_pm | unresolved | 0.2656 | 0.0764 | 0.4385 | 128 |
| old | actual | 4-10 | B | dominance_positive | 0.8407 | 0.7160 | 0.9470 | 295 |
| old | actual | 4-10 | B | reversal | 0.0441 | 0.0074 | 0.0960 | 295 |
| old | actual | 4-10 | B | negligible | 0.0915 | 0.0231 | 0.1782 | 295 |
| old | actual | 4-10 | B | unresolved | 0.0237 | 0.0000 | 0.0645 | 295 |
| old | actual | 4-10 | C | dominance_positive | 0.8407 | 0.7160 | 0.9470 | 295 |
| old | actual | 4-10 | C | reversal | 0.0441 | 0.0074 | 0.0960 | 295 |
| old | actual | 4-10 | C | negligible | 0.0915 | 0.0231 | 0.1782 | 295 |
| old | actual | 4-10 | C | unresolved | 0.0237 | 0.0000 | 0.0645 | 295 |
| old | actual | 4-10 | B_pm | dominance_positive | 0.7831 | 0.6312 | 0.9206 | 295 |
| old | actual | 4-10 | B_pm | reversal | 0.0339 | 0.0065 | 0.0705 | 295 |
| old | actual | 4-10 | B_pm | negligible | 0.0915 | 0.0231 | 0.1782 | 295 |
| old | actual | 4-10 | B_pm | unresolved | 0.0915 | 0.0121 | 0.1801 | 295 |
| old | actual | 4-10 | C_pm | dominance_positive | 0.7831 | 0.6312 | 0.9206 | 295 |
| old | actual | 4-10 | C_pm | reversal | 0.0339 | 0.0065 | 0.0705 | 295 |
| old | actual | 4-10 | C_pm | negligible | 0.0915 | 0.0231 | 0.1782 | 295 |
| old | actual | 4-10 | C_pm | unresolved | 0.0915 | 0.0121 | 0.1801 | 295 |
| old | actual | 11-16 | B | dominance_positive | 0.7942 | 0.6402 | 0.9016 | 243 |
| old | actual | 11-16 | B | reversal | 0.0247 | 0.0000 | 0.0677 | 243 |
| old | actual | 11-16 | B | negligible | 0.1728 | 0.0822 | 0.3067 | 243 |
| old | actual | 11-16 | B | unresolved | 0.0082 | 0.0000 | 0.0329 | 243 |
| old | actual | 11-16 | C | dominance_positive | 0.7942 | 0.6402 | 0.9016 | 243 |
| old | actual | 11-16 | C | reversal | 0.0247 | 0.0000 | 0.0677 | 243 |
| old | actual | 11-16 | C | negligible | 0.1728 | 0.0822 | 0.3067 | 243 |
| old | actual | 11-16 | C | unresolved | 0.0082 | 0.0000 | 0.0329 | 243 |
| old | actual | 11-16 | B_pm | dominance_positive | 0.7490 | 0.5983 | 0.8700 | 243 |
| old | actual | 11-16 | B_pm | reversal | 0.0165 | 0.0000 | 0.0518 | 243 |
| old | actual | 11-16 | B_pm | negligible | 0.1687 | 0.0822 | 0.2990 | 243 |
| old | actual | 11-16 | B_pm | unresolved | 0.0658 | 0.0168 | 0.1322 | 243 |
| old | actual | 11-16 | C_pm | dominance_positive | 0.7490 | 0.5983 | 0.8700 | 243 |
| old | actual | 11-16 | C_pm | reversal | 0.0165 | 0.0000 | 0.0518 | 243 |
| old | actual | 11-16 | C_pm | negligible | 0.1687 | 0.0822 | 0.2990 | 243 |
| old | actual | 11-16 | C_pm | unresolved | 0.0658 | 0.0168 | 0.1322 | 243 |
| old | actual | 17-30 | B | dominance_positive | 0.6041 | 0.3980 | 0.7672 | 586 |
| old | actual | 17-30 | B | reversal | 0.0375 | 0.0036 | 0.0909 | 586 |
| old | actual | 17-30 | B | negligible | 0.3481 | 0.2200 | 0.5148 | 586 |
| old | actual | 17-30 | B | unresolved | 0.0102 | 0.0000 | 0.0283 | 586 |
| old | actual | 17-30 | C | dominance_positive | 0.6041 | 0.3980 | 0.7672 | 586 |
| old | actual | 17-30 | C | reversal | 0.0375 | 0.0036 | 0.0909 | 586 |
| old | actual | 17-30 | C | negligible | 0.3481 | 0.2200 | 0.5148 | 586 |
| old | actual | 17-30 | C | unresolved | 0.0102 | 0.0000 | 0.0283 | 586 |
| old | actual | 17-30 | B_pm | dominance_positive | 0.5802 | 0.3624 | 0.7640 | 586 |
| old | actual | 17-30 | B_pm | reversal | 0.0273 | 0.0000 | 0.0737 | 586 |
| old | actual | 17-30 | B_pm | negligible | 0.3259 | 0.1959 | 0.4888 | 586 |
| old | actual | 17-30 | B_pm | unresolved | 0.0666 | 0.0178 | 0.1176 | 586 |
| old | actual | 17-30 | C_pm | dominance_positive | 0.5802 | 0.3624 | 0.7640 | 586 |
| old | actual | 17-30 | C_pm | reversal | 0.0273 | 0.0000 | 0.0737 | 586 |
| old | actual | 17-30 | C_pm | negligible | 0.3259 | 0.1959 | 0.4888 | 586 |
| old | actual | 17-30 | C_pm | unresolved | 0.0666 | 0.0178 | 0.1176 | 586 |
| old | own | 1-3 | B | dominance_positive | 0.9688 | 0.8934 | 1.0000 | 128 |
| old | own | 1-3 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 128 |
| old | own | 1-3 | B | negligible | 0.0312 | 0.0000 | 0.1066 | 128 |
| old | own | 1-3 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 128 |
| old | own | 1-3 | C | dominance_positive | 0.9688 | 0.8934 | 1.0000 | 128 |
| old | own | 1-3 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 128 |
| old | own | 1-3 | C | negligible | 0.0312 | 0.0000 | 0.1066 | 128 |
| old | own | 1-3 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 128 |
| old | own | 1-3 | B_pm | dominance_positive | 0.9688 | 0.8934 | 1.0000 | 128 |
| old | own | 1-3 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 128 |
| old | own | 1-3 | B_pm | negligible | 0.0312 | 0.0000 | 0.1066 | 128 |
| old | own | 1-3 | B_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 128 |
| old | own | 1-3 | C_pm | dominance_positive | 0.9688 | 0.8934 | 1.0000 | 128 |
| old | own | 1-3 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 128 |
| old | own | 1-3 | C_pm | negligible | 0.0312 | 0.0000 | 0.1066 | 128 |
| old | own | 1-3 | C_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 128 |
| old | own | 4-10 | B | dominance_positive | 0.9593 | 0.8771 | 1.0000 | 295 |
| old | own | 4-10 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 295 |
| old | own | 4-10 | B | negligible | 0.0407 | 0.0000 | 0.1229 | 295 |
| old | own | 4-10 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 295 |
| old | own | 4-10 | C | dominance_positive | 0.9593 | 0.8771 | 1.0000 | 295 |
| old | own | 4-10 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 295 |
| old | own | 4-10 | C | negligible | 0.0407 | 0.0000 | 0.1229 | 295 |
| old | own | 4-10 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 295 |
| old | own | 4-10 | B_pm | dominance_positive | 0.9525 | 0.8734 | 0.9965 | 295 |
| old | own | 4-10 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 295 |
| old | own | 4-10 | B_pm | negligible | 0.0407 | 0.0000 | 0.1229 | 295 |
| old | own | 4-10 | B_pm | unresolved | 0.0068 | 0.0000 | 0.0330 | 295 |
| old | own | 4-10 | C_pm | dominance_positive | 0.9525 | 0.8734 | 0.9965 | 295 |
| old | own | 4-10 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 295 |
| old | own | 4-10 | C_pm | negligible | 0.0407 | 0.0000 | 0.1229 | 295 |
| old | own | 4-10 | C_pm | unresolved | 0.0068 | 0.0000 | 0.0330 | 295 |
| old | own | 11-16 | B | dominance_positive | 0.9918 | 0.9706 | 1.0000 | 243 |
| old | own | 11-16 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| old | own | 11-16 | B | negligible | 0.0082 | 0.0000 | 0.0294 | 243 |
| old | own | 11-16 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 243 |
| old | own | 11-16 | C | dominance_positive | 0.9918 | 0.9706 | 1.0000 | 243 |
| old | own | 11-16 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| old | own | 11-16 | C | negligible | 0.0082 | 0.0000 | 0.0294 | 243 |
| old | own | 11-16 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 243 |
| old | own | 11-16 | B_pm | dominance_positive | 0.9547 | 0.8950 | 0.9954 | 243 |
| old | own | 11-16 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| old | own | 11-16 | B_pm | negligible | 0.0082 | 0.0000 | 0.0294 | 243 |
| old | own | 11-16 | B_pm | unresolved | 0.0370 | 0.0042 | 0.0886 | 243 |
| old | own | 11-16 | C_pm | dominance_positive | 0.9547 | 0.8950 | 0.9954 | 243 |
| old | own | 11-16 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| old | own | 11-16 | C_pm | negligible | 0.0082 | 0.0000 | 0.0294 | 243 |
| old | own | 11-16 | C_pm | unresolved | 0.0370 | 0.0042 | 0.0886 | 243 |
| old | own | 17-30 | B | dominance_positive | 0.9642 | 0.9128 | 1.0000 | 586 |
| old | own | 17-30 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | B | negligible | 0.0358 | 0.0000 | 0.0872 | 586 |
| old | own | 17-30 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | C | dominance_positive | 0.9642 | 0.9128 | 1.0000 | 586 |
| old | own | 17-30 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | C | negligible | 0.0358 | 0.0000 | 0.0872 | 586 |
| old | own | 17-30 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | B_pm | dominance_positive | 0.9522 | 0.8946 | 0.9965 | 586 |
| old | own | 17-30 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | B_pm | negligible | 0.0324 | 0.0000 | 0.0853 | 586 |
| old | own | 17-30 | B_pm | unresolved | 0.0154 | 0.0000 | 0.0374 | 586 |
| old | own | 17-30 | C_pm | dominance_positive | 0.9539 | 0.8958 | 0.9969 | 586 |
| old | own | 17-30 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | C_pm | negligible | 0.0324 | 0.0000 | 0.0853 | 586 |
| old | own | 17-30 | C_pm | unresolved | 0.0137 | 0.0000 | 0.0315 | 586 |
| new | actual | 1-3 | B | dominance_positive | 0.1484 | 0.0320 | 0.3162 | 128 |
| new | actual | 1-3 | B | reversal | 0.5156 | 0.2477 | 0.7414 | 128 |
| new | actual | 1-3 | B | negligible | 0.2422 | 0.0968 | 0.4535 | 128 |
| new | actual | 1-3 | B | unresolved | 0.0938 | 0.0312 | 0.1692 | 128 |
| new | actual | 1-3 | C | dominance_positive | 0.1484 | 0.0320 | 0.3162 | 128 |
| new | actual | 1-3 | C | reversal | 0.5156 | 0.2477 | 0.7414 | 128 |
| new | actual | 1-3 | C | negligible | 0.2422 | 0.0968 | 0.4535 | 128 |
| new | actual | 1-3 | C | unresolved | 0.0938 | 0.0312 | 0.1692 | 128 |
| new | actual | 1-3 | B_pm | dominance_positive | 0.0781 | 0.0160 | 0.1624 | 128 |
| new | actual | 1-3 | B_pm | reversal | 0.4219 | 0.2018 | 0.6293 | 128 |
| new | actual | 1-3 | B_pm | negligible | 0.2109 | 0.0435 | 0.4393 | 128 |
| new | actual | 1-3 | B_pm | unresolved | 0.2891 | 0.1802 | 0.4030 | 128 |
| new | actual | 1-3 | C_pm | dominance_positive | 0.0781 | 0.0160 | 0.1624 | 128 |
| new | actual | 1-3 | C_pm | reversal | 0.4219 | 0.2018 | 0.6293 | 128 |
| new | actual | 1-3 | C_pm | negligible | 0.2109 | 0.0435 | 0.4393 | 128 |
| new | actual | 1-3 | C_pm | unresolved | 0.2891 | 0.1802 | 0.4030 | 128 |
| new | actual | 4-10 | B | dominance_positive | 0.3966 | 0.1886 | 0.6391 | 295 |
| new | actual | 4-10 | B | reversal | 0.2068 | 0.1107 | 0.2812 | 295 |
| new | actual | 4-10 | B | negligible | 0.3492 | 0.1882 | 0.4982 | 295 |
| new | actual | 4-10 | B | unresolved | 0.0475 | 0.0033 | 0.1493 | 295 |
| new | actual | 4-10 | C | dominance_positive | 0.3966 | 0.1886 | 0.6391 | 295 |
| new | actual | 4-10 | C | reversal | 0.2068 | 0.1107 | 0.2812 | 295 |
| new | actual | 4-10 | C | negligible | 0.3492 | 0.1882 | 0.4982 | 295 |
| new | actual | 4-10 | C | unresolved | 0.0475 | 0.0033 | 0.1493 | 295 |
| new | actual | 4-10 | B_pm | dominance_positive | 0.3864 | 0.1533 | 0.6285 | 295 |
| new | actual | 4-10 | B_pm | reversal | 0.1797 | 0.0889 | 0.2534 | 295 |
| new | actual | 4-10 | B_pm | negligible | 0.2949 | 0.1566 | 0.4111 | 295 |
| new | actual | 4-10 | B_pm | unresolved | 0.1390 | 0.0290 | 0.3321 | 295 |
| new | actual | 4-10 | C_pm | dominance_positive | 0.3864 | 0.1533 | 0.6285 | 295 |
| new | actual | 4-10 | C_pm | reversal | 0.1797 | 0.0889 | 0.2534 | 295 |
| new | actual | 4-10 | C_pm | negligible | 0.2949 | 0.1566 | 0.4111 | 295 |
| new | actual | 4-10 | C_pm | unresolved | 0.1390 | 0.0290 | 0.3321 | 295 |
| new | actual | 11-16 | B | dominance_positive | 0.7284 | 0.5556 | 0.8734 | 243 |
| new | actual | 11-16 | B | reversal | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | actual | 11-16 | B | negligible | 0.2593 | 0.1213 | 0.4304 | 243 |
| new | actual | 11-16 | B | unresolved | 0.0082 | 0.0000 | 0.0357 | 243 |
| new | actual | 11-16 | C | dominance_positive | 0.7284 | 0.5556 | 0.8734 | 243 |
| new | actual | 11-16 | C | reversal | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | actual | 11-16 | C | negligible | 0.2593 | 0.1213 | 0.4304 | 243 |
| new | actual | 11-16 | C | unresolved | 0.0082 | 0.0000 | 0.0357 | 243 |
| new | actual | 11-16 | B_pm | dominance_positive | 0.7160 | 0.5407 | 0.8655 | 243 |
| new | actual | 11-16 | B_pm | reversal | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | actual | 11-16 | B_pm | negligible | 0.2510 | 0.1207 | 0.4104 | 243 |
| new | actual | 11-16 | B_pm | unresolved | 0.0288 | 0.0000 | 0.0802 | 243 |
| new | actual | 11-16 | C_pm | dominance_positive | 0.7160 | 0.5407 | 0.8655 | 243 |
| new | actual | 11-16 | C_pm | reversal | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | actual | 11-16 | C_pm | negligible | 0.2510 | 0.1207 | 0.4104 | 243 |
| new | actual | 11-16 | C_pm | unresolved | 0.0288 | 0.0000 | 0.0802 | 243 |
| new | actual | 17-30 | B | dominance_positive | 0.6229 | 0.4512 | 0.7762 | 586 |
| new | actual | 17-30 | B | reversal | 0.0444 | 0.0036 | 0.0903 | 586 |
| new | actual | 17-30 | B | negligible | 0.3208 | 0.1902 | 0.4768 | 586 |
| new | actual | 17-30 | B | unresolved | 0.0119 | 0.0000 | 0.0280 | 586 |
| new | actual | 17-30 | C | dominance_positive | 0.6229 | 0.4512 | 0.7762 | 586 |
| new | actual | 17-30 | C | reversal | 0.0427 | 0.0036 | 0.0882 | 586 |
| new | actual | 17-30 | C | negligible | 0.3208 | 0.1902 | 0.4768 | 586 |
| new | actual | 17-30 | C | unresolved | 0.0137 | 0.0000 | 0.0304 | 586 |
| new | actual | 17-30 | B_pm | dominance_positive | 0.6092 | 0.4321 | 0.7675 | 586 |
| new | actual | 17-30 | B_pm | reversal | 0.0375 | 0.0000 | 0.0841 | 586 |
| new | actual | 17-30 | B_pm | negligible | 0.3038 | 0.1768 | 0.4539 | 586 |
| new | actual | 17-30 | B_pm | unresolved | 0.0495 | 0.0115 | 0.0944 | 586 |
| new | actual | 17-30 | C_pm | dominance_positive | 0.6092 | 0.4321 | 0.7675 | 586 |
| new | actual | 17-30 | C_pm | reversal | 0.0375 | 0.0000 | 0.0841 | 586 |
| new | actual | 17-30 | C_pm | negligible | 0.3038 | 0.1768 | 0.4539 | 586 |
| new | actual | 17-30 | C_pm | unresolved | 0.0495 | 0.0115 | 0.0944 | 586 |
| new | own | 1-3 | B | dominance_positive | 0.0938 | 0.0000 | 0.2564 | 128 |
| new | own | 1-3 | B | reversal | 0.5312 | 0.2455 | 0.8067 | 128 |
| new | own | 1-3 | B | negligible | 0.3516 | 0.1376 | 0.6477 | 128 |
| new | own | 1-3 | B | unresolved | 0.0234 | 0.0000 | 0.0840 | 128 |
| new | own | 1-3 | C | dominance_positive | 0.0938 | 0.0000 | 0.2564 | 128 |
| new | own | 1-3 | C | reversal | 0.5312 | 0.2455 | 0.8067 | 128 |
| new | own | 1-3 | C | negligible | 0.3516 | 0.1376 | 0.6477 | 128 |
| new | own | 1-3 | C | unresolved | 0.0234 | 0.0000 | 0.0840 | 128 |
| new | own | 1-3 | B_pm | dominance_positive | 0.0781 | 0.0074 | 0.1825 | 128 |
| new | own | 1-3 | B_pm | reversal | 0.4766 | 0.2231 | 0.7383 | 128 |
| new | own | 1-3 | B_pm | negligible | 0.3125 | 0.0853 | 0.6214 | 128 |
| new | own | 1-3 | B_pm | unresolved | 0.1328 | 0.0374 | 0.2203 | 128 |
| new | own | 1-3 | C_pm | dominance_positive | 0.0781 | 0.0074 | 0.1825 | 128 |
| new | own | 1-3 | C_pm | reversal | 0.4766 | 0.2231 | 0.7383 | 128 |
| new | own | 1-3 | C_pm | negligible | 0.3125 | 0.0853 | 0.6214 | 128 |
| new | own | 1-3 | C_pm | unresolved | 0.1328 | 0.0374 | 0.2203 | 128 |
| new | own | 4-10 | B | dominance_positive | 0.4068 | 0.1901 | 0.6278 | 295 |
| new | own | 4-10 | B | reversal | 0.1797 | 0.0906 | 0.2509 | 295 |
| new | own | 4-10 | B | negligible | 0.4000 | 0.2128 | 0.5758 | 295 |
| new | own | 4-10 | B | unresolved | 0.0136 | 0.0000 | 0.0439 | 295 |
| new | own | 4-10 | C | dominance_positive | 0.4068 | 0.1901 | 0.6278 | 295 |
| new | own | 4-10 | C | reversal | 0.1797 | 0.0906 | 0.2509 | 295 |
| new | own | 4-10 | C | negligible | 0.4000 | 0.2128 | 0.5758 | 295 |
| new | own | 4-10 | C | unresolved | 0.0136 | 0.0000 | 0.0439 | 295 |
| new | own | 4-10 | B_pm | dominance_positive | 0.4203 | 0.2006 | 0.6330 | 295 |
| new | own | 4-10 | B_pm | reversal | 0.1797 | 0.0906 | 0.2509 | 295 |
| new | own | 4-10 | B_pm | negligible | 0.3797 | 0.1970 | 0.5573 | 295 |
| new | own | 4-10 | B_pm | unresolved | 0.0203 | 0.0000 | 0.0487 | 295 |
| new | own | 4-10 | C_pm | dominance_positive | 0.4203 | 0.2006 | 0.6330 | 295 |
| new | own | 4-10 | C_pm | reversal | 0.1797 | 0.0906 | 0.2509 | 295 |
| new | own | 4-10 | C_pm | negligible | 0.3797 | 0.1970 | 0.5573 | 295 |
| new | own | 4-10 | C_pm | unresolved | 0.0203 | 0.0000 | 0.0487 | 295 |
| new | own | 11-16 | B | dominance_positive | 0.9259 | 0.8042 | 1.0000 | 243 |
| new | own | 11-16 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | B | negligible | 0.0741 | 0.0000 | 0.1958 | 243 |
| new | own | 11-16 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | C | dominance_positive | 0.9259 | 0.8042 | 1.0000 | 243 |
| new | own | 11-16 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | C | negligible | 0.0741 | 0.0000 | 0.1958 | 243 |
| new | own | 11-16 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | B_pm | dominance_positive | 0.9218 | 0.7963 | 1.0000 | 243 |
| new | own | 11-16 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | B_pm | negligible | 0.0741 | 0.0000 | 0.1958 | 243 |
| new | own | 11-16 | B_pm | unresolved | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | own | 11-16 | C_pm | dominance_positive | 0.9218 | 0.7963 | 1.0000 | 243 |
| new | own | 11-16 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | C_pm | negligible | 0.0741 | 0.0000 | 0.1958 | 243 |
| new | own | 11-16 | C_pm | unresolved | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | own | 17-30 | B | dominance_positive | 0.9642 | 0.9128 | 1.0000 | 586 |
| new | own | 17-30 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | B | negligible | 0.0358 | 0.0000 | 0.0872 | 586 |
| new | own | 17-30 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | C | dominance_positive | 0.9642 | 0.9128 | 1.0000 | 586 |
| new | own | 17-30 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | C | negligible | 0.0358 | 0.0000 | 0.0872 | 586 |
| new | own | 17-30 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | B_pm | dominance_positive | 0.9539 | 0.8980 | 0.9965 | 586 |
| new | own | 17-30 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | B_pm | negligible | 0.0324 | 0.0000 | 0.0853 | 586 |
| new | own | 17-30 | B_pm | unresolved | 0.0137 | 0.0000 | 0.0366 | 586 |
| new | own | 17-30 | C_pm | dominance_positive | 0.9556 | 0.8997 | 0.9969 | 586 |
| new | own | 17-30 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | C_pm | negligible | 0.0324 | 0.0000 | 0.0853 | 586 |
| new | own | 17-30 | C_pm | unresolved | 0.0119 | 0.0000 | 0.0304 | 586 |

## T5_3_reversal_slot

| rule | portfolio | jstar | count | count_argmin_C_hat | count_precision_matched | n_reversals | n_reversals_pm |
|---|---|---|---|---|---|---|---|
| old | actual | 1 | 0 | 0 | 0 | 45 | 33 |
| old | actual | 2 | 0 | 0 | 0 | 45 | 33 |
| old | actual | 3 | 0 | 0 | 0 | 45 | 33 |
| old | actual | 4 | 0 | 0 | 0 | 45 | 33 |
| old | actual | 5 | 1 | 1 | 1 | 45 | 33 |
| old | actual | 6 | 0 | 0 | 0 | 45 | 33 |
| old | actual | 7 | 1 | 1 | 1 | 45 | 33 |
| old | actual | 8 | 0 | 0 | 1 | 45 | 33 |
| old | actual | 9 | 2 | 2 | 1 | 45 | 33 |
| old | actual | 10 | 1 | 1 | 1 | 45 | 33 |
| old | actual | 11 | 0 | 0 | 0 | 45 | 33 |
| old | actual | 12 | 1 | 0 | 1 | 45 | 33 |
| old | actual | 13 | 2 | 2 | 1 | 45 | 33 |
| old | actual | 14 | 2 | 2 | 1 | 45 | 33 |
| old | actual | 15 | 3 | 4 | 1 | 45 | 33 |
| old | actual | 16 | 2 | 2 | 1 | 45 | 33 |
| old | actual | 17 | 3 | 3 | 2 | 45 | 33 |
| old | actual | 18 | 3 | 3 | 3 | 45 | 33 |
| old | actual | 19 | 5 | 5 | 4 | 45 | 33 |
| old | actual | 20 | 3 | 3 | 3 | 45 | 33 |
| old | actual | 21 | 2 | 2 | 1 | 45 | 33 |
| old | actual | 22 | 1 | 1 | 1 | 45 | 33 |
| old | actual | 23 | 2 | 2 | 2 | 45 | 33 |
| old | actual | 24 | 2 | 2 | 1 | 45 | 33 |
| old | actual | 25 | 2 | 2 | 1 | 45 | 33 |
| old | actual | 26 | 2 | 2 | 2 | 45 | 33 |
| old | actual | 27 | 1 | 1 | 1 | 45 | 33 |
| old | actual | 28 | 0 | 0 | 0 | 45 | 33 |
| old | actual | 29 | 2 | 2 | 1 | 45 | 33 |
| old | actual | 30 | 2 | 2 | 1 | 45 | 33 |
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
| new | actual | 1 | 0 | 0 | 0 | 154 | 130 |
| new | actual | 2 | 0 | 0 | 0 | 154 | 130 |
| new | actual | 3 | 1 | 1 | 1 | 154 | 130 |
| new | actual | 4 | 2 | 2 | 1 | 154 | 130 |
| new | actual | 5 | 0 | 0 | 0 | 154 | 130 |
| new | actual | 6 | 2 | 2 | 0 | 154 | 130 |
| new | actual | 7 | 3 | 3 | 2 | 154 | 130 |
| new | actual | 8 | 10 | 12 | 5 | 154 | 130 |
| new | actual | 9 | 96 | 94 | 87 | 154 | 130 |
| new | actual | 10 | 0 | 0 | 0 | 154 | 130 |
| new | actual | 11 | 0 | 0 | 0 | 154 | 130 |
| new | actual | 12 | 0 | 0 | 0 | 154 | 130 |
| new | actual | 13 | 0 | 0 | 0 | 154 | 130 |
| new | actual | 14 | 0 | 0 | 0 | 154 | 130 |
| new | actual | 15 | 2 | 2 | 2 | 154 | 130 |
| new | actual | 16 | 1 | 1 | 1 | 154 | 130 |
| new | actual | 17 | 3 | 3 | 3 | 154 | 130 |
| new | actual | 18 | 1 | 1 | 0 | 154 | 130 |
| new | actual | 19 | 6 | 7 | 6 | 154 | 130 |
| new | actual | 20 | 3 | 2 | 3 | 154 | 130 |
| new | actual | 21 | 2 | 2 | 1 | 154 | 130 |
| new | actual | 22 | 1 | 1 | 1 | 154 | 130 |
| new | actual | 23 | 4 | 4 | 4 | 154 | 130 |
| new | actual | 24 | 2 | 2 | 2 | 154 | 130 |
| new | actual | 25 | 2 | 2 | 1 | 154 | 130 |
| new | actual | 26 | 4 | 4 | 4 | 154 | 130 |
| new | actual | 27 | 2 | 2 | 1 | 154 | 130 |
| new | actual | 28 | 0 | 0 | 0 | 154 | 130 |
| new | actual | 29 | 4 | 4 | 3 | 154 | 130 |
| new | actual | 30 | 3 | 3 | 2 | 154 | 130 |
| new | own | 1 | 0 | 0 | 0 | 121 | 114 |
| new | own | 2 | 0 | 0 | 0 | 121 | 114 |
| new | own | 3 | 0 | 0 | 0 | 121 | 114 |
| new | own | 4 | 0 | 0 | 0 | 121 | 114 |
| new | own | 5 | 0 | 0 | 0 | 121 | 114 |
| new | own | 6 | 0 | 0 | 0 | 121 | 114 |
| new | own | 7 | 0 | 0 | 0 | 121 | 114 |
| new | own | 8 | 0 | 0 | 0 | 121 | 114 |
| new | own | 9 | 121 | 121 | 114 | 121 | 114 |
| new | own | 10 | 0 | 0 | 0 | 121 | 114 |
| new | own | 11 | 0 | 0 | 0 | 121 | 114 |
| new | own | 12 | 0 | 0 | 0 | 121 | 114 |
| new | own | 13 | 0 | 0 | 0 | 121 | 114 |
| new | own | 14 | 0 | 0 | 0 | 121 | 114 |
| new | own | 15 | 0 | 0 | 0 | 121 | 114 |
| new | own | 16 | 0 | 0 | 0 | 121 | 114 |
| new | own | 17 | 0 | 0 | 0 | 121 | 114 |
| new | own | 18 | 0 | 0 | 0 | 121 | 114 |
| new | own | 19 | 0 | 0 | 0 | 121 | 114 |
| new | own | 20 | 0 | 0 | 0 | 121 | 114 |
| new | own | 21 | 0 | 0 | 0 | 121 | 114 |
| new | own | 22 | 0 | 0 | 0 | 121 | 114 |
| new | own | 23 | 0 | 0 | 0 | 121 | 114 |
| new | own | 24 | 0 | 0 | 0 | 121 | 114 |
| new | own | 25 | 0 | 0 | 0 | 121 | 114 |
| new | own | 26 | 0 | 0 | 0 | 121 | 114 |
| new | own | 27 | 0 | 0 | 0 | 121 | 114 |
| new | own | 28 | 0 | 0 | 0 | 121 | 114 |
| new | own | 29 | 0 | 0 | 0 | 121 | 114 |
| new | own | 30 | 0 | 0 | 0 | 121 | 114 |

## F5_1_profiles

720 rows in `F5_1_profiles.csv`.

## T5_curves_and_T5_6_delta

| rule | portfolio | band | curve | n | mean | q25 | median | q75 | q90 | share_sig_pos | pos_lo99 | pos_hi99 | share_sig_neg | neg_lo99 | neg_hi99 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| old | actual | all | linear | 1252 | 0.0171 | 0.0006 | 0.0095 | 0.0290 | 0.0420 | 0.6653 | 0.5210 | 0.7981 | 0.0176 | 0.0026 | 0.0368 |
| old | actual | all | concave | 1252 | 0.0159 | 0.0005 | 0.0085 | 0.0271 | 0.0387 | 0.6302 | 0.4903 | 0.7661 | 0.0176 | 0.0041 | 0.0360 |
| old | actual | all | convex | 1252 | 0.0156 | 0.0004 | 0.0086 | 0.0268 | 0.0399 | 0.6693 | 0.5576 | 0.7660 | 0.0112 | 0.0009 | 0.0244 |
| old | actual | all | top3_stress | 1252 | 0.0066 | 0.0000 | 0.0007 | 0.0106 | 0.0225 | 0.4065 | 0.3525 | 0.4719 | 0.0024 | 0.0000 | 0.0089 |
| old | actual | 1-3 | linear | 128 | 0.0029 | 0.0017 | 0.0024 | 0.0054 | 0.0078 | 0.4453 | 0.1875 | 0.6970 | 0.0156 | 0.0000 | 0.0580 |
| old | actual | 1-3 | concave | 128 | 0.0015 | 0.0009 | 0.0014 | 0.0029 | 0.0044 | 0.2656 | 0.0909 | 0.4722 | 0.0234 | 0.0000 | 0.0682 |
| old | actual | 1-3 | convex | 128 | 0.0050 | 0.0027 | 0.0040 | 0.0074 | 0.0116 | 0.7500 | 0.6160 | 0.8750 | 0.0156 | 0.0000 | 0.0580 |
| old | actual | 1-3 | top3_stress | 128 | 0.0043 | 0.0002 | 0.0011 | 0.0054 | 0.0125 | 0.3516 | 0.1333 | 0.6000 | 0.0078 | 0.0000 | 0.0484 |
| old | actual | 4-10 | linear | 295 | 0.0173 | 0.0051 | 0.0135 | 0.0258 | 0.0380 | 0.8339 | 0.6967 | 0.9524 | 0.0271 | 0.0000 | 0.0736 |
| old | actual | 4-10 | concave | 295 | 0.0132 | 0.0030 | 0.0079 | 0.0176 | 0.0335 | 0.7525 | 0.5679 | 0.9371 | 0.0271 | 0.0000 | 0.0721 |
| old | actual | 4-10 | convex | 295 | 0.0222 | 0.0088 | 0.0184 | 0.0349 | 0.0448 | 0.8712 | 0.7616 | 0.9636 | 0.0102 | 0.0000 | 0.0308 |
| old | actual | 4-10 | top3_stress | 295 | 0.0177 | 0.0090 | 0.0161 | 0.0269 | 0.0331 | 0.8678 | 0.7625 | 0.9591 | 0.0034 | 0.0000 | 0.0193 |
| old | actual | 11-16 | linear | 243 | 0.0272 | 0.0077 | 0.0255 | 0.0363 | 0.0503 | 0.8107 | 0.6548 | 0.9153 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 11-16 | concave | 243 | 0.0218 | 0.0063 | 0.0171 | 0.0277 | 0.0364 | 0.8066 | 0.6535 | 0.9109 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 11-16 | convex | 243 | 0.0286 | 0.0074 | 0.0285 | 0.0403 | 0.0583 | 0.7984 | 0.6429 | 0.9098 | 0.0041 | 0.0000 | 0.0262 |
| old | actual | 11-16 | top3_stress | 243 | 0.0088 | 0.0019 | 0.0062 | 0.0146 | 0.0209 | 0.6955 | 0.5746 | 0.8110 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 17-30 | linear | 586 | 0.0158 | 0.0000 | 0.0072 | 0.0291 | 0.0415 | 0.5683 | 0.3345 | 0.7508 | 0.0205 | 0.0000 | 0.0566 |
| old | actual | 17-30 | concave | 586 | 0.0180 | 0.0000 | 0.0112 | 0.0316 | 0.0414 | 0.5751 | 0.3406 | 0.7609 | 0.0188 | 0.0000 | 0.0564 |
| old | actual | 17-30 | convex | 586 | 0.0092 | 0.0000 | 0.0027 | 0.0157 | 0.0283 | 0.4966 | 0.3002 | 0.6516 | 0.0137 | 0.0000 | 0.0358 |
| old | actual | 17-30 | top3_stress | 586 | 0.0006 | 0.0000 | 0.0000 | 0.0003 | 0.0018 | 0.0666 | 0.0297 | 0.1100 | 0.0017 | 0.0000 | 0.0105 |
| old | own | all | linear | 1252 | 0.0234 | 0.0080 | 0.0230 | 0.0344 | 0.0455 | 0.8746 | 0.7967 | 0.9362 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | concave | 1252 | 0.0206 | 0.0057 | 0.0203 | 0.0312 | 0.0393 | 0.8419 | 0.7595 | 0.9208 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | convex | 1252 | 0.0212 | 0.0060 | 0.0179 | 0.0321 | 0.0436 | 0.8594 | 0.8048 | 0.9048 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | top3_stress | 1252 | 0.0075 | 0.0000 | 0.0023 | 0.0122 | 0.0231 | 0.4776 | 0.4203 | 0.5340 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | linear | 128 | 0.0033 | 0.0018 | 0.0023 | 0.0040 | 0.0063 | 0.3359 | 0.0968 | 0.6312 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | concave | 128 | 0.0018 | 0.0010 | 0.0013 | 0.0022 | 0.0034 | 0.1875 | 0.0164 | 0.4228 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | convex | 128 | 0.0055 | 0.0030 | 0.0040 | 0.0067 | 0.0106 | 0.7656 | 0.5818 | 0.9237 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | top3_stress | 128 | 0.0043 | 0.0002 | 0.0010 | 0.0056 | 0.0126 | 0.3516 | 0.1327 | 0.6154 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | linear | 295 | 0.0157 | 0.0068 | 0.0118 | 0.0239 | 0.0316 | 0.9119 | 0.7893 | 0.9879 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | concave | 295 | 0.0092 | 0.0037 | 0.0068 | 0.0139 | 0.0187 | 0.8203 | 0.6637 | 0.9713 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | convex | 295 | 0.0232 | 0.0108 | 0.0184 | 0.0350 | 0.0446 | 0.9458 | 0.8520 | 0.9965 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | top3_stress | 295 | 0.0191 | 0.0108 | 0.0172 | 0.0270 | 0.0331 | 0.9525 | 0.8669 | 0.9966 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | linear | 243 | 0.0321 | 0.0217 | 0.0301 | 0.0391 | 0.0536 | 0.9918 | 0.9706 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | concave | 243 | 0.0216 | 0.0145 | 0.0202 | 0.0278 | 0.0364 | 0.9794 | 0.9388 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | convex | 243 | 0.0367 | 0.0257 | 0.0334 | 0.0439 | 0.0630 | 0.9918 | 0.9706 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | top3_stress | 243 | 0.0109 | 0.0049 | 0.0081 | 0.0157 | 0.0225 | 0.8889 | 0.7593 | 0.9769 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | linear | 586 | 0.0281 | 0.0168 | 0.0280 | 0.0377 | 0.0481 | 0.9249 | 0.8540 | 0.9871 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | concave | 586 | 0.0300 | 0.0227 | 0.0301 | 0.0365 | 0.0444 | 0.9386 | 0.8792 | 0.9922 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | convex | 586 | 0.0172 | 0.0043 | 0.0147 | 0.0266 | 0.0362 | 0.7816 | 0.7054 | 0.8569 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | top3_stress | 586 | 0.0009 | 0.0000 | 0.0000 | 0.0007 | 0.0027 | 0.0956 | 0.0365 | 0.1811 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | all | linear | 1252 | 0.0157 | 0.0000 | 0.0034 | 0.0286 | 0.0453 | 0.5136 | 0.3831 | 0.6347 | 0.0623 | 0.0203 | 0.1070 |
| new | actual | all | concave | 1252 | 0.0152 | 0.0000 | 0.0037 | 0.0281 | 0.0405 | 0.5216 | 0.3924 | 0.6325 | 0.0391 | 0.0121 | 0.0682 |
| new | actual | all | convex | 1252 | 0.0134 | 0.0000 | 0.0019 | 0.0211 | 0.0439 | 0.4768 | 0.3597 | 0.5940 | 0.0703 | 0.0277 | 0.1116 |
| new | actual | all | top3_stress | 1252 | 0.0048 | 0.0000 | 0.0000 | 0.0068 | 0.0211 | 0.3259 | 0.2402 | 0.4180 | 0.0895 | 0.0405 | 0.1315 |
| new | actual | 1-3 | linear | 128 | -0.0027 | -0.0032 | -0.0002 | 0.0002 | 0.0017 | 0.0859 | 0.0087 | 0.1690 | 0.2891 | 0.0556 | 0.5739 |
| new | actual | 1-3 | concave | 128 | -0.0017 | -0.0018 | -0.0001 | 0.0002 | 0.0040 | 0.1406 | 0.0082 | 0.3147 | 0.1562 | 0.0219 | 0.3188 |
| new | actual | 1-3 | convex | 128 | -0.0040 | -0.0059 | -0.0010 | 0.0000 | 0.0005 | 0.0703 | 0.0079 | 0.1544 | 0.3594 | 0.1415 | 0.6021 |
| new | actual | 1-3 | top3_stress | 128 | -0.0055 | -0.0095 | -0.0022 | -0.0000 | 0.0000 | 0.0156 | 0.0000 | 0.0630 | 0.4766 | 0.2202 | 0.7383 |
| new | actual | 4-10 | linear | 295 | 0.0044 | 0.0000 | 0.0007 | 0.0061 | 0.0162 | 0.3458 | 0.1486 | 0.5563 | 0.1051 | 0.0428 | 0.1791 |
| new | actual | 4-10 | concave | 295 | 0.0043 | 0.0000 | 0.0006 | 0.0052 | 0.0151 | 0.3661 | 0.1905 | 0.5500 | 0.0644 | 0.0197 | 0.1309 |
| new | actual | 4-10 | convex | 295 | 0.0043 | -0.0001 | 0.0002 | 0.0071 | 0.0187 | 0.3390 | 0.1514 | 0.5563 | 0.1288 | 0.0518 | 0.1985 |
| new | actual | 4-10 | top3_stress | 295 | 0.0022 | -0.0001 | 0.0000 | 0.0059 | 0.0127 | 0.3254 | 0.1283 | 0.5496 | 0.1627 | 0.0676 | 0.2379 |
| new | actual | 11-16 | linear | 243 | 0.0268 | 0.0004 | 0.0206 | 0.0393 | 0.0545 | 0.7160 | 0.5372 | 0.8690 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 11-16 | concave | 243 | 0.0205 | 0.0003 | 0.0162 | 0.0289 | 0.0434 | 0.6872 | 0.5040 | 0.8478 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 11-16 | convex | 243 | 0.0305 | 0.0005 | 0.0258 | 0.0439 | 0.0600 | 0.7037 | 0.5124 | 0.8596 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 11-16 | top3_stress | 243 | 0.0164 | 0.0003 | 0.0131 | 0.0240 | 0.0339 | 0.6831 | 0.4961 | 0.8389 | 0.0041 | 0.0000 | 0.0260 |
| new | actual | 17-30 | linear | 586 | 0.0207 | 0.0000 | 0.0145 | 0.0359 | 0.0496 | 0.6075 | 0.3951 | 0.7816 | 0.0171 | 0.0000 | 0.0549 |
| new | actual | 17-30 | concave | 586 | 0.0222 | 0.0000 | 0.0199 | 0.0359 | 0.0511 | 0.6143 | 0.4010 | 0.7886 | 0.0171 | 0.0000 | 0.0549 |
| new | actual | 17-30 | convex | 586 | 0.0147 | 0.0000 | 0.0046 | 0.0234 | 0.0436 | 0.5410 | 0.3599 | 0.6840 | 0.0068 | 0.0000 | 0.0285 |
| new | actual | 17-30 | top3_stress | 586 | 0.0036 | 0.0000 | 0.0000 | 0.0024 | 0.0128 | 0.2457 | 0.1661 | 0.3636 | 0.0034 | 0.0000 | 0.0140 |
| new | own | all | linear | 1252 | 0.0230 | 0.0002 | 0.0158 | 0.0388 | 0.0537 | 0.6837 | 0.6048 | 0.7804 | 0.0415 | 0.0138 | 0.0709 |
| new | own | all | concave | 1252 | 0.0204 | 0.0002 | 0.0202 | 0.0342 | 0.0442 | 0.6685 | 0.5918 | 0.7693 | 0.0072 | 0.0000 | 0.0223 |
| new | own | all | convex | 1252 | 0.0206 | 0.0001 | 0.0094 | 0.0334 | 0.0570 | 0.6238 | 0.5541 | 0.7024 | 0.0623 | 0.0274 | 0.0912 |
| new | own | all | top3_stress | 1252 | 0.0071 | 0.0000 | 0.0005 | 0.0115 | 0.0248 | 0.4233 | 0.3343 | 0.5198 | 0.0831 | 0.0377 | 0.1201 |
| new | own | 1-3 | linear | 128 | -0.0016 | -0.0027 | -0.0007 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.2266 | 0.0348 | 0.4706 |
| new | own | 1-3 | concave | 128 | -0.0008 | -0.0013 | -0.0003 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0391 | 0.0000 | 0.1298 |
| new | own | 1-3 | convex | 128 | -0.0029 | -0.0051 | -0.0012 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.3438 | 0.1442 | 0.5630 |
| new | own | 1-3 | top3_stress | 128 | -0.0053 | -0.0092 | -0.0022 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.4531 | 0.2069 | 0.7132 |
| new | own | 4-10 | linear | 295 | 0.0036 | -0.0000 | 0.0002 | 0.0053 | 0.0108 | 0.3356 | 0.1452 | 0.5445 | 0.0780 | 0.0278 | 0.1266 |
| new | own | 4-10 | concave | 295 | 0.0023 | 0.0000 | 0.0002 | 0.0032 | 0.0066 | 0.2746 | 0.0787 | 0.5038 | 0.0136 | 0.0000 | 0.0451 |
| new | own | 4-10 | convex | 295 | 0.0046 | -0.0000 | 0.0003 | 0.0076 | 0.0151 | 0.3559 | 0.1667 | 0.5644 | 0.1153 | 0.0489 | 0.1716 |
| new | own | 4-10 | top3_stress | 295 | 0.0027 | -0.0000 | 0.0000 | 0.0072 | 0.0129 | 0.3492 | 0.1653 | 0.5491 | 0.1559 | 0.0659 | 0.2270 |
| new | own | 11-16 | linear | 243 | 0.0343 | 0.0129 | 0.0333 | 0.0457 | 0.0674 | 0.8848 | 0.7460 | 0.9828 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | concave | 243 | 0.0224 | 0.0078 | 0.0213 | 0.0308 | 0.0439 | 0.8477 | 0.7061 | 0.9670 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | convex | 243 | 0.0420 | 0.0164 | 0.0398 | 0.0551 | 0.0813 | 0.8971 | 0.7603 | 0.9919 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | top3_stress | 243 | 0.0222 | 0.0102 | 0.0189 | 0.0276 | 0.0453 | 0.8724 | 0.7435 | 0.9717 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | linear | 586 | 0.0335 | 0.0159 | 0.0300 | 0.0446 | 0.0630 | 0.9249 | 0.8540 | 0.9871 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | concave | 586 | 0.0332 | 0.0240 | 0.0324 | 0.0398 | 0.0525 | 0.9386 | 0.8792 | 0.9922 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | convex | 586 | 0.0248 | 0.0043 | 0.0157 | 0.0367 | 0.0609 | 0.7816 | 0.7054 | 0.8569 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | top3_stress | 586 | 0.0058 | 0.0000 | 0.0002 | 0.0070 | 0.0205 | 0.3669 | 0.2645 | 0.4817 | 0.0000 | 0.0000 | 0.0000 |
| delta | actual | all | linear | 1252 | -0.0014 | -0.0068 | 0.0000 | 0.0011 | 0.0114 | 0.2212 | 0.1683 | 0.2932 | 0.3227 | 0.2412 | 0.3934 |
| delta | actual | all | concave | 1252 | -0.0007 | -0.0041 | 0.0000 | 0.0011 | 0.0091 | 0.2005 | 0.1532 | 0.2657 | 0.2947 | 0.2086 | 0.3866 |
| delta | actual | all | convex | 1252 | -0.0022 | -0.0101 | 0.0000 | 0.0015 | 0.0141 | 0.2340 | 0.1799 | 0.3021 | 0.3586 | 0.3112 | 0.4004 |
| delta | actual | all | top3_stress | 1252 | -0.0018 | -0.0066 | 0.0000 | 0.0011 | 0.0121 | 0.2212 | 0.1641 | 0.2920 | 0.2907 | 0.2375 | 0.3444 |
| delta | actual | 1-3 | linear | 128 | -0.0055 | -0.0079 | -0.0024 | -0.0014 | -0.0003 | 0.0234 | 0.0000 | 0.0813 | 0.4375 | 0.1261 | 0.7317 |
| delta | actual | 1-3 | concave | 128 | -0.0032 | -0.0044 | -0.0013 | -0.0004 | 0.0013 | 0.0625 | 0.0000 | 0.1892 | 0.3281 | 0.0536 | 0.6116 |
| delta | actual | 1-3 | convex | 128 | -0.0090 | -0.0139 | -0.0045 | -0.0028 | -0.0011 | 0.0078 | 0.0000 | 0.0473 | 0.7500 | 0.6031 | 0.8829 |
| delta | actual | 1-3 | top3_stress | 128 | -0.0098 | -0.0155 | -0.0033 | -0.0004 | -0.0000 | 0.0078 | 0.0000 | 0.0473 | 0.5312 | 0.2555 | 0.7623 |
| delta | actual | 4-10 | linear | 295 | -0.0129 | -0.0205 | -0.0114 | -0.0048 | 0.0000 | 0.0271 | 0.0000 | 0.0751 | 0.8034 | 0.6452 | 0.9428 |
| delta | actual | 4-10 | concave | 295 | -0.0089 | -0.0132 | -0.0065 | -0.0024 | 0.0000 | 0.0441 | 0.0000 | 0.1224 | 0.7390 | 0.5578 | 0.9290 |
| delta | actual | 4-10 | convex | 295 | -0.0178 | -0.0262 | -0.0172 | -0.0095 | 0.0000 | 0.0237 | 0.0000 | 0.0593 | 0.8576 | 0.7516 | 0.9512 |
| delta | actual | 4-10 | top3_stress | 295 | -0.0155 | -0.0211 | -0.0145 | -0.0079 | 0.0000 | 0.0169 | 0.0000 | 0.0704 | 0.8542 | 0.7449 | 0.9516 |
| delta | actual | 11-16 | linear | 243 | -0.0004 | -0.0100 | 0.0000 | 0.0072 | 0.0202 | 0.3827 | 0.2488 | 0.5148 | 0.3745 | 0.1953 | 0.5219 |
| delta | actual | 11-16 | concave | 243 | -0.0013 | -0.0072 | 0.0000 | 0.0041 | 0.0134 | 0.3169 | 0.2043 | 0.4228 | 0.3621 | 0.1514 | 0.5311 |
| delta | actual | 11-16 | convex | 243 | 0.0019 | -0.0100 | 0.0000 | 0.0102 | 0.0236 | 0.4198 | 0.2842 | 0.5588 | 0.3498 | 0.1855 | 0.4847 |
| delta | actual | 11-16 | top3_stress | 243 | 0.0076 | 0.0000 | 0.0038 | 0.0135 | 0.0215 | 0.5350 | 0.3849 | 0.6714 | 0.1564 | 0.0568 | 0.2500 |
| delta | actual | 17-30 | linear | 586 | 0.0049 | 0.0000 | 0.0000 | 0.0042 | 0.0170 | 0.2952 | 0.2023 | 0.4174 | 0.0341 | 0.0036 | 0.0725 |
| delta | actual | 17-30 | concave | 586 | 0.0042 | 0.0000 | 0.0000 | 0.0029 | 0.0153 | 0.2611 | 0.1830 | 0.3617 | 0.0358 | 0.0020 | 0.0755 |
| delta | actual | 17-30 | convex | 586 | 0.0055 | 0.0000 | 0.0000 | 0.0055 | 0.0187 | 0.3123 | 0.2142 | 0.4379 | 0.0256 | 0.0018 | 0.0611 |
| delta | actual | 17-30 | top3_stress | 586 | 0.0030 | 0.0000 | 0.0000 | 0.0022 | 0.0108 | 0.2406 | 0.1638 | 0.3542 | 0.0102 | 0.0000 | 0.0267 |
| delta | own | all | linear | 1252 | -0.0004 | -0.0074 | 0.0000 | 0.0039 | 0.0142 | 0.2819 | 0.2327 | 0.3290 | 0.3650 | 0.3175 | 0.4111 |
| delta | own | all | concave | 1252 | -0.0002 | -0.0043 | -0.0000 | 0.0021 | 0.0085 | 0.2396 | 0.1911 | 0.2817 | 0.3163 | 0.2609 | 0.3736 |
| delta | own | all | convex | 1252 | -0.0006 | -0.0113 | 0.0000 | 0.0065 | 0.0210 | 0.3051 | 0.2571 | 0.3517 | 0.3922 | 0.3507 | 0.4299 |
| delta | own | all | top3_stress | 1252 | -0.0004 | -0.0080 | 0.0000 | 0.0050 | 0.0172 | 0.3083 | 0.2325 | 0.3817 | 0.3107 | 0.2526 | 0.3623 |
| delta | own | 1-3 | linear | 128 | -0.0048 | -0.0063 | -0.0030 | -0.0019 | -0.0014 | 0.0000 | 0.0000 | 0.0000 | 0.5156 | 0.2364 | 0.7840 |
| delta | own | 1-3 | concave | 128 | -0.0026 | -0.0033 | -0.0016 | -0.0010 | -0.0007 | 0.0000 | 0.0000 | 0.0000 | 0.2812 | 0.0846 | 0.5221 |
| delta | own | 1-3 | convex | 128 | -0.0084 | -0.0110 | -0.0051 | -0.0033 | -0.0024 | 0.0000 | 0.0000 | 0.0000 | 0.8203 | 0.6439 | 0.9520 |
| delta | own | 1-3 | top3_stress | 128 | -0.0096 | -0.0155 | -0.0031 | -0.0004 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.5312 | 0.2476 | 0.8018 |
| delta | own | 4-10 | linear | 295 | -0.0121 | -0.0168 | -0.0107 | -0.0070 | -0.0041 | 0.0000 | 0.0000 | 0.0000 | 0.9153 | 0.8168 | 0.9795 |
| delta | own | 4-10 | concave | 295 | -0.0069 | -0.0099 | -0.0059 | -0.0040 | -0.0023 | 0.0000 | 0.0000 | 0.0000 | 0.8644 | 0.7322 | 0.9701 |
| delta | own | 4-10 | convex | 295 | -0.0186 | -0.0253 | -0.0172 | -0.0112 | -0.0070 | 0.0034 | 0.0000 | 0.0226 | 0.9390 | 0.8387 | 0.9926 |
| delta | own | 4-10 | top3_stress | 295 | -0.0164 | -0.0211 | -0.0158 | -0.0099 | -0.0042 | 0.0203 | 0.0000 | 0.0739 | 0.9288 | 0.8185 | 0.9908 |
| delta | own | 11-16 | linear | 243 | 0.0022 | -0.0103 | 0.0026 | 0.0107 | 0.0198 | 0.5185 | 0.3686 | 0.7213 | 0.3992 | 0.2197 | 0.5236 |
| delta | own | 11-16 | concave | 243 | 0.0008 | -0.0066 | 0.0012 | 0.0060 | 0.0113 | 0.4239 | 0.2982 | 0.5415 | 0.3663 | 0.1643 | 0.5035 |
| delta | own | 11-16 | convex | 243 | 0.0054 | -0.0115 | 0.0059 | 0.0177 | 0.0309 | 0.5679 | 0.4268 | 0.7615 | 0.3827 | 0.2085 | 0.5079 |
| delta | own | 11-16 | top3_stress | 243 | 0.0112 | -0.0002 | 0.0096 | 0.0180 | 0.0287 | 0.6955 | 0.5350 | 0.8535 | 0.1811 | 0.0632 | 0.3108 |
| delta | own | 17-30 | linear | 586 | 0.0054 | 0.0000 | 0.0001 | 0.0078 | 0.0176 | 0.3874 | 0.3125 | 0.4722 | 0.0410 | 0.0035 | 0.1009 |
| delta | own | 17-30 | concave | 586 | 0.0033 | 0.0000 | 0.0000 | 0.0048 | 0.0107 | 0.3362 | 0.2508 | 0.4279 | 0.0273 | 0.0034 | 0.0607 |
| delta | own | 17-30 | convex | 586 | 0.0076 | 0.0000 | 0.0003 | 0.0108 | 0.0247 | 0.4147 | 0.3386 | 0.4985 | 0.0273 | 0.0020 | 0.0668 |
| delta | own | 17-30 | top3_stress | 586 | 0.0049 | 0.0000 | 0.0002 | 0.0063 | 0.0167 | 0.3601 | 0.2605 | 0.4740 | 0.0051 | 0.0000 | 0.0181 |

## H1

| n_team_games | share_neg_new | share_neg_old | diff_new_minus_old | diff_lo99 | diff_hi99 | n_new_reversals | crossing_share | crossing_lo99 | crossing_hi99 | supported |
|---|---|---|---|---|---|---|---|---|---|---|
| 163 | 0.3006 | 0.0000 | 0.3006 | 0.1032 | 0.5188 | 103 | 1.0000 | 1.0000 | 1.0000 | True |

## T5_attr_portfolio_effect

| rule | band | n | mean | q25 | median | q75 | q90 | share_nonzero |
|---|---|---|---|---|---|---|---|---|
| old | all | 1252 | -0.0063 | -0.0126 | 0.0000 | 0.0000 | 0.0018 | 0.4225 |
| old | 1-3 | 128 | -0.0004 | -0.0000 | 0.0000 | 0.0000 | 0.0012 | 0.0859 |
| old | 4-10 | 295 | 0.0016 | -0.0000 | 0.0000 | 0.0020 | 0.0137 | 0.3559 |
| old | 11-16 | 243 | -0.0049 | -0.0151 | 0.0000 | 0.0000 | 0.0017 | 0.4239 |
| old | 17-30 | 586 | -0.0123 | -0.0235 | -0.0033 | 0.0000 | 0.0000 | 0.5290 |
| new | all | 1252 | -0.0073 | -0.0096 | 0.0000 | 0.0000 | 0.0030 | 0.4201 |
| new | 1-3 | 128 | -0.0011 | -0.0001 | 0.0000 | 0.0003 | 0.0039 | 0.2109 |
| new | 4-10 | 295 | 0.0008 | 0.0000 | 0.0000 | 0.0012 | 0.0062 | 0.2814 |
| new | 11-16 | 243 | -0.0074 | -0.0085 | 0.0000 | 0.0000 | 0.0032 | 0.3827 |
| new | 17-30 | 586 | -0.0128 | -0.0212 | -0.0032 | 0.0000 | 0.0000 | 0.5512 |
| delta | all | 1252 | -0.0010 | -0.0002 | 0.0000 | 0.0000 | 0.0048 | 0.2971 |
| delta | 1-3 | 128 | -0.0007 | -0.0000 | 0.0000 | 0.0005 | 0.0029 | 0.1719 |
| delta | 4-10 | 295 | -0.0008 | -0.0005 | 0.0000 | 0.0001 | 0.0062 | 0.3356 |
| delta | 11-16 | 243 | -0.0025 | -0.0017 | 0.0000 | 0.0000 | 0.0069 | 0.3704 |
| delta | 17-30 | 586 | -0.0005 | -0.0000 | 0.0000 | 0.0000 | 0.0046 | 0.2747 |

## T5_7_rollover

| rule | portfolio | band | curve | rho | measure | n | mean | q25 | median | q75 | q90 | share_sign_flip | vbar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| old | actual | all | - | 0.0000 | M | 1252 | 0.0059 | -0.0000 | 0.0000 | 0.0000 | 0.0148 |  |  |
| old | actual | all | linear | 0.0000 | tau | 1252 | 0.0171 | 0.0006 | 0.0095 | 0.0290 | 0.0420 | 0.0000 | 0.5000 |
| old | actual | all | linear | 0.5000 | tau | 1252 | 0.0156 | 0.0006 | 0.0093 | 0.0268 | 0.0396 | 0.0024 | 0.5000 |
| old | actual | all | linear | 0.8000 | tau | 1252 | 0.0147 | 0.0005 | 0.0083 | 0.0258 | 0.0382 | 0.0048 | 0.5000 |
| old | actual | all | concave | 0.0000 | tau | 1252 | 0.0159 | 0.0005 | 0.0085 | 0.0271 | 0.0387 | 0.0000 | 0.6599 |
| old | actual | all | concave | 0.5000 | tau | 1252 | 0.0140 | 0.0005 | 0.0075 | 0.0242 | 0.0356 | 0.0064 | 0.6599 |
| old | actual | all | concave | 0.8000 | tau | 1252 | 0.0128 | 0.0004 | 0.0064 | 0.0225 | 0.0342 | 0.0104 | 0.6599 |
| old | actual | all | convex | 0.0000 | tau | 1252 | 0.0156 | 0.0004 | 0.0086 | 0.0268 | 0.0399 | 0.0000 | 0.3391 |
| old | actual | all | convex | 0.5000 | tau | 1252 | 0.0146 | 0.0003 | 0.0077 | 0.0252 | 0.0389 | 0.0024 | 0.3391 |
| old | actual | all | convex | 0.8000 | tau | 1252 | 0.0140 | 0.0003 | 0.0073 | 0.0244 | 0.0381 | 0.0064 | 0.3391 |
| old | actual | all | top3_stress | 0.0000 | tau | 1252 | 0.0066 | 0.0000 | 0.0007 | 0.0106 | 0.0225 | 0.0000 | 0.1000 |
| old | actual | all | top3_stress | 0.5000 | tau | 1252 | 0.0063 | 0.0000 | 0.0004 | 0.0101 | 0.0218 | 0.1278 | 0.1000 |
| old | actual | all | top3_stress | 0.8000 | tau | 1252 | 0.0061 | 0.0000 | 0.0004 | 0.0100 | 0.0216 | 0.1318 | 0.1000 |
| old | actual | 1-3 | - | 0.0000 | M | 128 | -0.0001 | -0.0000 | 0.0000 | 0.0000 | 0.0001 |  |  |
| old | actual | 1-3 | linear | 0.0000 | tau | 128 | 0.0029 | 0.0017 | 0.0024 | 0.0054 | 0.0078 | 0.0000 | 0.5000 |
| old | actual | 1-3 | linear | 0.5000 | tau | 128 | 0.0029 | 0.0017 | 0.0026 | 0.0054 | 0.0077 | 0.0000 | 0.5000 |
| old | actual | 1-3 | linear | 0.8000 | tau | 128 | 0.0029 | 0.0017 | 0.0026 | 0.0054 | 0.0077 | 0.0000 | 0.5000 |
| old | actual | 1-3 | concave | 0.0000 | tau | 128 | 0.0015 | 0.0009 | 0.0014 | 0.0029 | 0.0044 | 0.0000 | 0.6599 |
| old | actual | 1-3 | concave | 0.5000 | tau | 128 | 0.0015 | 0.0009 | 0.0014 | 0.0030 | 0.0043 | 0.0234 | 0.6599 |
| old | actual | 1-3 | concave | 0.8000 | tau | 128 | 0.0015 | 0.0009 | 0.0014 | 0.0030 | 0.0043 | 0.0234 | 0.6599 |
| old | actual | 1-3 | convex | 0.0000 | tau | 128 | 0.0050 | 0.0027 | 0.0040 | 0.0074 | 0.0116 | 0.0000 | 0.3391 |
| old | actual | 1-3 | convex | 0.5000 | tau | 128 | 0.0051 | 0.0027 | 0.0041 | 0.0075 | 0.0110 | 0.0000 | 0.3391 |
| old | actual | 1-3 | convex | 0.8000 | tau | 128 | 0.0051 | 0.0027 | 0.0042 | 0.0075 | 0.0113 | 0.0000 | 0.3391 |
| old | actual | 1-3 | top3_stress | 0.0000 | tau | 128 | 0.0043 | 0.0002 | 0.0011 | 0.0054 | 0.0125 | 0.0000 | 0.1000 |
| old | actual | 1-3 | top3_stress | 0.5000 | tau | 128 | 0.0043 | 0.0002 | 0.0012 | 0.0055 | 0.0123 | 0.0156 | 0.1000 |
| old | actual | 1-3 | top3_stress | 0.8000 | tau | 128 | 0.0043 | 0.0002 | 0.0011 | 0.0056 | 0.0121 | 0.0156 | 0.1000 |
| old | actual | 4-10 | - | 0.0000 | M | 295 | 0.0073 | -0.0000 | 0.0000 | 0.0010 | 0.0332 |  |  |
| old | actual | 4-10 | linear | 0.0000 | tau | 295 | 0.0173 | 0.0051 | 0.0135 | 0.0258 | 0.0380 | 0.0000 | 0.5000 |
| old | actual | 4-10 | linear | 0.5000 | tau | 295 | 0.0155 | 0.0054 | 0.0125 | 0.0243 | 0.0324 | 0.0034 | 0.5000 |
| old | actual | 4-10 | linear | 0.8000 | tau | 295 | 0.0144 | 0.0054 | 0.0118 | 0.0229 | 0.0315 | 0.0102 | 0.5000 |
| old | actual | 4-10 | concave | 0.0000 | tau | 295 | 0.0132 | 0.0030 | 0.0079 | 0.0176 | 0.0335 | 0.0000 | 0.6599 |
| old | actual | 4-10 | concave | 0.5000 | tau | 295 | 0.0108 | 0.0028 | 0.0077 | 0.0160 | 0.0245 | 0.0102 | 0.6599 |
| old | actual | 4-10 | concave | 0.8000 | tau | 295 | 0.0093 | 0.0030 | 0.0075 | 0.0148 | 0.0205 | 0.0237 | 0.6599 |
| old | actual | 4-10 | convex | 0.0000 | tau | 295 | 0.0222 | 0.0088 | 0.0184 | 0.0349 | 0.0448 | 0.0000 | 0.3391 |
| old | actual | 4-10 | convex | 0.5000 | tau | 295 | 0.0209 | 0.0085 | 0.0179 | 0.0329 | 0.0436 | 0.0034 | 0.3391 |
| old | actual | 4-10 | convex | 0.8000 | tau | 295 | 0.0202 | 0.0085 | 0.0164 | 0.0319 | 0.0427 | 0.0068 | 0.3391 |
| old | actual | 4-10 | top3_stress | 0.0000 | tau | 295 | 0.0177 | 0.0090 | 0.0161 | 0.0269 | 0.0331 | 0.0000 | 0.1000 |
| old | actual | 4-10 | top3_stress | 0.5000 | tau | 295 | 0.0174 | 0.0089 | 0.0161 | 0.0265 | 0.0328 | 0.0034 | 0.1000 |
| old | actual | 4-10 | top3_stress | 0.8000 | tau | 295 | 0.0172 | 0.0088 | 0.0158 | 0.0259 | 0.0327 | 0.0034 | 0.1000 |
| old | actual | 11-16 | - | 0.0000 | M | 243 | 0.0098 | -0.0000 | 0.0000 | 0.0001 | 0.0169 |  |  |
| old | actual | 11-16 | linear | 0.0000 | tau | 243 | 0.0272 | 0.0077 | 0.0255 | 0.0363 | 0.0503 | 0.0000 | 0.5000 |
| old | actual | 11-16 | linear | 0.5000 | tau | 243 | 0.0248 | 0.0058 | 0.0243 | 0.0350 | 0.0496 | 0.0000 | 0.5000 |
| old | actual | 11-16 | linear | 0.8000 | tau | 243 | 0.0233 | 0.0047 | 0.0236 | 0.0347 | 0.0466 | 0.0041 | 0.5000 |
| old | actual | 11-16 | concave | 0.0000 | tau | 243 | 0.0218 | 0.0063 | 0.0171 | 0.0277 | 0.0364 | 0.0000 | 0.6599 |
| old | actual | 11-16 | concave | 0.5000 | tau | 243 | 0.0186 | 0.0056 | 0.0169 | 0.0255 | 0.0341 | 0.0041 | 0.6599 |
| old | actual | 11-16 | concave | 0.8000 | tau | 243 | 0.0167 | 0.0038 | 0.0157 | 0.0248 | 0.0329 | 0.0041 | 0.6599 |
| old | actual | 11-16 | convex | 0.0000 | tau | 243 | 0.0286 | 0.0074 | 0.0285 | 0.0403 | 0.0583 | 0.0000 | 0.3391 |
| old | actual | 11-16 | convex | 0.5000 | tau | 243 | 0.0269 | 0.0059 | 0.0272 | 0.0396 | 0.0550 | 0.0082 | 0.3391 |
| old | actual | 11-16 | convex | 0.8000 | tau | 243 | 0.0259 | 0.0051 | 0.0272 | 0.0386 | 0.0548 | 0.0165 | 0.3391 |
| old | actual | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0088 | 0.0019 | 0.0062 | 0.0146 | 0.0209 | 0.0000 | 0.1000 |
| old | actual | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0083 | 0.0013 | 0.0057 | 0.0140 | 0.0207 | 0.0288 | 0.1000 |
| old | actual | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0080 | 0.0004 | 0.0056 | 0.0136 | 0.0207 | 0.0494 | 0.1000 |
| old | actual | 17-30 | - | 0.0000 | M | 586 | 0.0050 | -0.0000 | 0.0000 | 0.0000 | 0.0045 |  |  |
| old | actual | 17-30 | linear | 0.0000 | tau | 586 | 0.0158 | 0.0000 | 0.0072 | 0.0291 | 0.0415 | 0.0000 | 0.5000 |
| old | actual | 17-30 | linear | 0.5000 | tau | 586 | 0.0146 | 0.0000 | 0.0056 | 0.0273 | 0.0398 | 0.0034 | 0.5000 |
| old | actual | 17-30 | linear | 0.8000 | tau | 586 | 0.0139 | 0.0000 | 0.0042 | 0.0266 | 0.0393 | 0.0034 | 0.5000 |
| old | actual | 17-30 | concave | 0.0000 | tau | 586 | 0.0180 | 0.0000 | 0.0112 | 0.0316 | 0.0414 | 0.0000 | 0.6599 |
| old | actual | 17-30 | concave | 0.5000 | tau | 586 | 0.0164 | 0.0000 | 0.0088 | 0.0308 | 0.0395 | 0.0017 | 0.6599 |
| old | actual | 17-30 | concave | 0.8000 | tau | 586 | 0.0154 | 0.0000 | 0.0065 | 0.0304 | 0.0391 | 0.0034 | 0.6599 |
| old | actual | 17-30 | convex | 0.0000 | tau | 586 | 0.0092 | 0.0000 | 0.0027 | 0.0157 | 0.0283 | 0.0000 | 0.3391 |
| old | actual | 17-30 | convex | 0.5000 | tau | 586 | 0.0084 | 0.0000 | 0.0022 | 0.0140 | 0.0274 | 0.0000 | 0.3391 |
| old | actual | 17-30 | convex | 0.8000 | tau | 586 | 0.0079 | 0.0000 | 0.0018 | 0.0123 | 0.0272 | 0.0034 | 0.3391 |
| old | actual | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0006 | 0.0000 | 0.0000 | 0.0003 | 0.0018 | 0.0000 | 0.1000 |
| old | actual | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0003 | 0.0000 | 0.0000 | 0.0001 | 0.0012 | 0.2560 | 0.1000 |
| old | actual | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0002 | 0.0000 | 0.0000 | 0.0001 | 0.0012 | 0.2560 | 0.1000 |
| old | own | all | - | 0.0000 | M | 1252 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | all | linear | 0.0000 | tau | 1252 | 0.0234 | 0.0080 | 0.0230 | 0.0344 | 0.0455 | 0.0000 | 0.5000 |
| old | own | all | linear | 0.5000 | tau | 1252 | 0.0234 | 0.0080 | 0.0230 | 0.0344 | 0.0455 | 0.0000 | 0.5000 |
| old | own | all | linear | 0.8000 | tau | 1252 | 0.0234 | 0.0080 | 0.0230 | 0.0344 | 0.0455 | 0.0000 | 0.5000 |
| old | own | all | concave | 0.0000 | tau | 1252 | 0.0206 | 0.0057 | 0.0203 | 0.0312 | 0.0393 | 0.0000 | 0.6599 |
| old | own | all | concave | 0.5000 | tau | 1252 | 0.0206 | 0.0057 | 0.0203 | 0.0312 | 0.0393 | 0.0000 | 0.6599 |
| old | own | all | concave | 0.8000 | tau | 1252 | 0.0206 | 0.0057 | 0.0203 | 0.0312 | 0.0393 | 0.0000 | 0.6599 |
| old | own | all | convex | 0.0000 | tau | 1252 | 0.0212 | 0.0060 | 0.0179 | 0.0321 | 0.0436 | 0.0000 | 0.3391 |
| old | own | all | convex | 0.5000 | tau | 1252 | 0.0212 | 0.0060 | 0.0179 | 0.0321 | 0.0436 | 0.0000 | 0.3391 |
| old | own | all | convex | 0.8000 | tau | 1252 | 0.0212 | 0.0060 | 0.0179 | 0.0321 | 0.0436 | 0.0000 | 0.3391 |
| old | own | all | top3_stress | 0.0000 | tau | 1252 | 0.0075 | 0.0000 | 0.0023 | 0.0122 | 0.0231 | 0.0000 | 0.1000 |
| old | own | all | top3_stress | 0.5000 | tau | 1252 | 0.0075 | 0.0000 | 0.0023 | 0.0122 | 0.0231 | 0.0799 | 0.1000 |
| old | own | all | top3_stress | 0.8000 | tau | 1252 | 0.0075 | 0.0000 | 0.0023 | 0.0122 | 0.0231 | 0.0791 | 0.1000 |
| old | own | 1-3 | - | 0.0000 | M | 128 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 1-3 | linear | 0.0000 | tau | 128 | 0.0033 | 0.0018 | 0.0023 | 0.0040 | 0.0063 | 0.0000 | 0.5000 |
| old | own | 1-3 | linear | 0.5000 | tau | 128 | 0.0033 | 0.0018 | 0.0023 | 0.0040 | 0.0063 | 0.0000 | 0.5000 |
| old | own | 1-3 | linear | 0.8000 | tau | 128 | 0.0033 | 0.0018 | 0.0023 | 0.0040 | 0.0063 | 0.0000 | 0.5000 |
| old | own | 1-3 | concave | 0.0000 | tau | 128 | 0.0018 | 0.0010 | 0.0013 | 0.0022 | 0.0034 | 0.0000 | 0.6599 |
| old | own | 1-3 | concave | 0.5000 | tau | 128 | 0.0018 | 0.0010 | 0.0013 | 0.0022 | 0.0034 | 0.0000 | 0.6599 |
| old | own | 1-3 | concave | 0.8000 | tau | 128 | 0.0018 | 0.0010 | 0.0013 | 0.0022 | 0.0034 | 0.0000 | 0.6599 |
| old | own | 1-3 | convex | 0.0000 | tau | 128 | 0.0055 | 0.0030 | 0.0040 | 0.0067 | 0.0106 | 0.0000 | 0.3391 |
| old | own | 1-3 | convex | 0.5000 | tau | 128 | 0.0055 | 0.0030 | 0.0040 | 0.0067 | 0.0106 | 0.0000 | 0.3391 |
| old | own | 1-3 | convex | 0.8000 | tau | 128 | 0.0055 | 0.0030 | 0.0040 | 0.0067 | 0.0106 | 0.0000 | 0.3391 |
| old | own | 1-3 | top3_stress | 0.0000 | tau | 128 | 0.0043 | 0.0002 | 0.0010 | 0.0056 | 0.0126 | 0.0000 | 0.1000 |
| old | own | 1-3 | top3_stress | 0.5000 | tau | 128 | 0.0043 | 0.0002 | 0.0010 | 0.0056 | 0.0126 | 0.0078 | 0.1000 |
| old | own | 1-3 | top3_stress | 0.8000 | tau | 128 | 0.0043 | 0.0002 | 0.0010 | 0.0056 | 0.0126 | 0.0078 | 0.1000 |
| old | own | 4-10 | - | 0.0000 | M | 295 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 4-10 | linear | 0.0000 | tau | 295 | 0.0157 | 0.0068 | 0.0118 | 0.0239 | 0.0316 | 0.0000 | 0.5000 |
| old | own | 4-10 | linear | 0.5000 | tau | 295 | 0.0157 | 0.0068 | 0.0118 | 0.0239 | 0.0316 | 0.0000 | 0.5000 |
| old | own | 4-10 | linear | 0.8000 | tau | 295 | 0.0157 | 0.0068 | 0.0118 | 0.0239 | 0.0316 | 0.0000 | 0.5000 |
| old | own | 4-10 | concave | 0.0000 | tau | 295 | 0.0092 | 0.0037 | 0.0068 | 0.0139 | 0.0187 | 0.0000 | 0.6599 |
| old | own | 4-10 | concave | 0.5000 | tau | 295 | 0.0092 | 0.0037 | 0.0068 | 0.0139 | 0.0187 | 0.0000 | 0.6599 |
| old | own | 4-10 | concave | 0.8000 | tau | 295 | 0.0092 | 0.0037 | 0.0068 | 0.0139 | 0.0187 | 0.0000 | 0.6599 |
| old | own | 4-10 | convex | 0.0000 | tau | 295 | 0.0232 | 0.0108 | 0.0184 | 0.0350 | 0.0446 | 0.0000 | 0.3391 |
| old | own | 4-10 | convex | 0.5000 | tau | 295 | 0.0232 | 0.0108 | 0.0184 | 0.0350 | 0.0446 | 0.0000 | 0.3391 |
| old | own | 4-10 | convex | 0.8000 | tau | 295 | 0.0232 | 0.0108 | 0.0184 | 0.0350 | 0.0446 | 0.0000 | 0.3391 |
| old | own | 4-10 | top3_stress | 0.0000 | tau | 295 | 0.0191 | 0.0108 | 0.0172 | 0.0270 | 0.0331 | 0.0000 | 0.1000 |
| old | own | 4-10 | top3_stress | 0.5000 | tau | 295 | 0.0191 | 0.0108 | 0.0172 | 0.0270 | 0.0331 | 0.0000 | 0.1000 |
| old | own | 4-10 | top3_stress | 0.8000 | tau | 295 | 0.0191 | 0.0108 | 0.0172 | 0.0270 | 0.0331 | 0.0000 | 0.1000 |
| old | own | 11-16 | - | 0.0000 | M | 243 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 11-16 | linear | 0.0000 | tau | 243 | 0.0321 | 0.0217 | 0.0301 | 0.0391 | 0.0536 | 0.0000 | 0.5000 |
| old | own | 11-16 | linear | 0.5000 | tau | 243 | 0.0321 | 0.0217 | 0.0301 | 0.0391 | 0.0536 | 0.0000 | 0.5000 |
| old | own | 11-16 | linear | 0.8000 | tau | 243 | 0.0321 | 0.0217 | 0.0301 | 0.0391 | 0.0536 | 0.0000 | 0.5000 |
| old | own | 11-16 | concave | 0.0000 | tau | 243 | 0.0216 | 0.0145 | 0.0202 | 0.0278 | 0.0364 | 0.0000 | 0.6599 |
| old | own | 11-16 | concave | 0.5000 | tau | 243 | 0.0216 | 0.0145 | 0.0202 | 0.0278 | 0.0364 | 0.0000 | 0.6599 |
| old | own | 11-16 | concave | 0.8000 | tau | 243 | 0.0216 | 0.0145 | 0.0202 | 0.0278 | 0.0364 | 0.0000 | 0.6599 |
| old | own | 11-16 | convex | 0.0000 | tau | 243 | 0.0367 | 0.0257 | 0.0334 | 0.0439 | 0.0630 | 0.0000 | 0.3391 |
| old | own | 11-16 | convex | 0.5000 | tau | 243 | 0.0367 | 0.0257 | 0.0334 | 0.0439 | 0.0630 | 0.0000 | 0.3391 |
| old | own | 11-16 | convex | 0.8000 | tau | 243 | 0.0367 | 0.0257 | 0.0334 | 0.0439 | 0.0630 | 0.0000 | 0.3391 |
| old | own | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0109 | 0.0049 | 0.0081 | 0.0157 | 0.0225 | 0.0000 | 0.1000 |
| old | own | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0109 | 0.0049 | 0.0081 | 0.0157 | 0.0225 | 0.0000 | 0.1000 |
| old | own | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0109 | 0.0049 | 0.0081 | 0.0157 | 0.0225 | 0.0000 | 0.1000 |
| old | own | 17-30 | - | 0.0000 | M | 586 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 17-30 | linear | 0.0000 | tau | 586 | 0.0281 | 0.0168 | 0.0280 | 0.0377 | 0.0481 | 0.0000 | 0.5000 |
| old | own | 17-30 | linear | 0.5000 | tau | 586 | 0.0281 | 0.0168 | 0.0280 | 0.0377 | 0.0481 | 0.0000 | 0.5000 |
| old | own | 17-30 | linear | 0.8000 | tau | 586 | 0.0281 | 0.0168 | 0.0280 | 0.0377 | 0.0481 | 0.0000 | 0.5000 |
| old | own | 17-30 | concave | 0.0000 | tau | 586 | 0.0300 | 0.0227 | 0.0301 | 0.0365 | 0.0444 | 0.0000 | 0.6599 |
| old | own | 17-30 | concave | 0.5000 | tau | 586 | 0.0300 | 0.0227 | 0.0301 | 0.0365 | 0.0444 | 0.0000 | 0.6599 |
| old | own | 17-30 | concave | 0.8000 | tau | 586 | 0.0300 | 0.0227 | 0.0301 | 0.0365 | 0.0444 | 0.0000 | 0.6599 |
| old | own | 17-30 | convex | 0.0000 | tau | 586 | 0.0172 | 0.0043 | 0.0147 | 0.0266 | 0.0362 | 0.0000 | 0.3391 |
| old | own | 17-30 | convex | 0.5000 | tau | 586 | 0.0172 | 0.0043 | 0.0147 | 0.0266 | 0.0362 | 0.0000 | 0.3391 |
| old | own | 17-30 | convex | 0.8000 | tau | 586 | 0.0172 | 0.0043 | 0.0147 | 0.0266 | 0.0362 | 0.0000 | 0.3391 |
| old | own | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0009 | 0.0000 | 0.0000 | 0.0007 | 0.0027 | 0.0000 | 0.1000 |
| old | own | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0009 | 0.0000 | 0.0000 | 0.0007 | 0.0027 | 0.1689 | 0.1000 |
| old | own | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0009 | 0.0000 | 0.0000 | 0.0007 | 0.0027 | 0.1672 | 0.1000 |
| new | actual | all | - | 0.0000 | M | 1252 | 0.0061 | -0.0000 | 0.0000 | 0.0000 | 0.0154 |  |  |
| new | actual | all | linear | 0.0000 | tau | 1252 | 0.0157 | 0.0000 | 0.0034 | 0.0286 | 0.0453 | 0.0000 | 0.5000 |
| new | actual | all | linear | 0.5000 | tau | 1252 | 0.0141 | 0.0000 | 0.0032 | 0.0260 | 0.0429 | 0.0304 | 0.5000 |
| new | actual | all | linear | 0.8000 | tau | 1252 | 0.0132 | 0.0000 | 0.0027 | 0.0244 | 0.0414 | 0.0367 | 0.5000 |
| new | actual | all | concave | 0.0000 | tau | 1252 | 0.0152 | 0.0000 | 0.0037 | 0.0281 | 0.0405 | 0.0000 | 0.6599 |
| new | actual | all | concave | 0.5000 | tau | 1252 | 0.0132 | 0.0000 | 0.0027 | 0.0255 | 0.0379 | 0.0024 | 0.6599 |
| new | actual | all | concave | 0.8000 | tau | 1252 | 0.0120 | 0.0000 | 0.0022 | 0.0237 | 0.0363 | 0.0080 | 0.6599 |
| new | actual | all | convex | 0.0000 | tau | 1252 | 0.0134 | 0.0000 | 0.0019 | 0.0211 | 0.0439 | 0.0000 | 0.3391 |
| new | actual | all | convex | 0.5000 | tau | 1252 | 0.0124 | 0.0000 | 0.0018 | 0.0196 | 0.0411 | 0.0048 | 0.3391 |
| new | actual | all | convex | 0.8000 | tau | 1252 | 0.0118 | 0.0000 | 0.0017 | 0.0187 | 0.0404 | 0.0112 | 0.3391 |
| new | actual | all | top3_stress | 0.0000 | tau | 1252 | 0.0048 | 0.0000 | 0.0000 | 0.0068 | 0.0211 | 0.0000 | 0.1000 |
| new | actual | all | top3_stress | 0.5000 | tau | 1252 | 0.0045 | 0.0000 | 0.0000 | 0.0064 | 0.0195 | 0.0759 | 0.1000 |
| new | actual | all | top3_stress | 0.8000 | tau | 1252 | 0.0043 | 0.0000 | 0.0000 | 0.0059 | 0.0190 | 0.0759 | 0.1000 |
| new | actual | 1-3 | - | 0.0000 | M | 128 | -0.0004 | -0.0000 | -0.0000 | 0.0000 | 0.0029 |  |  |
| new | actual | 1-3 | linear | 0.0000 | tau | 128 | -0.0027 | -0.0032 | -0.0002 | 0.0002 | 0.0017 | 0.0000 | 0.5000 |
| new | actual | 1-3 | linear | 0.5000 | tau | 128 | -0.0026 | -0.0031 | -0.0004 | 0.0000 | 0.0006 | 0.1094 | 0.5000 |
| new | actual | 1-3 | linear | 0.8000 | tau | 128 | -0.0025 | -0.0032 | -0.0005 | 0.0000 | 0.0004 | 0.1406 | 0.5000 |
| new | actual | 1-3 | concave | 0.0000 | tau | 128 | -0.0017 | -0.0018 | -0.0001 | 0.0002 | 0.0040 | 0.0000 | 0.6599 |
| new | actual | 1-3 | concave | 0.5000 | tau | 128 | -0.0016 | -0.0017 | -0.0001 | 0.0002 | 0.0023 | 0.0156 | 0.6599 |
| new | actual | 1-3 | concave | 0.8000 | tau | 128 | -0.0015 | -0.0016 | -0.0001 | 0.0001 | 0.0008 | 0.0391 | 0.6599 |
| new | actual | 1-3 | convex | 0.0000 | tau | 128 | -0.0040 | -0.0059 | -0.0010 | 0.0000 | 0.0005 | 0.0000 | 0.3391 |
| new | actual | 1-3 | convex | 0.5000 | tau | 128 | -0.0039 | -0.0063 | -0.0011 | 0.0000 | 0.0002 | 0.0078 | 0.3391 |
| new | actual | 1-3 | convex | 0.8000 | tau | 128 | -0.0039 | -0.0058 | -0.0011 | 0.0000 | 0.0002 | 0.0156 | 0.3391 |
| new | actual | 1-3 | top3_stress | 0.0000 | tau | 128 | -0.0055 | -0.0095 | -0.0022 | -0.0000 | 0.0000 | 0.0000 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.5000 | tau | 128 | -0.0054 | -0.0096 | -0.0023 | -0.0000 | 0.0000 | 0.0469 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.8000 | tau | 128 | -0.0054 | -0.0096 | -0.0022 | -0.0000 | 0.0000 | 0.0469 | 0.1000 |
| new | actual | 4-10 | - | 0.0000 | M | 295 | 0.0038 | -0.0000 | 0.0000 | 0.0014 | 0.0153 |  |  |
| new | actual | 4-10 | linear | 0.0000 | tau | 295 | 0.0044 | 0.0000 | 0.0007 | 0.0061 | 0.0162 | 0.0000 | 0.5000 |
| new | actual | 4-10 | linear | 0.5000 | tau | 295 | 0.0035 | -0.0000 | 0.0002 | 0.0055 | 0.0140 | 0.0814 | 0.5000 |
| new | actual | 4-10 | linear | 0.8000 | tau | 295 | 0.0029 | -0.0000 | 0.0002 | 0.0051 | 0.0131 | 0.0881 | 0.5000 |
| new | actual | 4-10 | concave | 0.0000 | tau | 295 | 0.0043 | 0.0000 | 0.0006 | 0.0052 | 0.0151 | 0.0000 | 0.6599 |
| new | actual | 4-10 | concave | 0.5000 | tau | 295 | 0.0030 | 0.0000 | 0.0005 | 0.0040 | 0.0110 | 0.0034 | 0.6599 |
| new | actual | 4-10 | concave | 0.8000 | tau | 295 | 0.0023 | 0.0000 | 0.0002 | 0.0035 | 0.0098 | 0.0169 | 0.6599 |
| new | actual | 4-10 | convex | 0.0000 | tau | 295 | 0.0043 | -0.0001 | 0.0002 | 0.0071 | 0.0187 | 0.0000 | 0.3391 |
| new | actual | 4-10 | convex | 0.5000 | tau | 295 | 0.0037 | -0.0000 | 0.0003 | 0.0069 | 0.0163 | 0.0102 | 0.3391 |
| new | actual | 4-10 | convex | 0.8000 | tau | 295 | 0.0033 | -0.0000 | 0.0003 | 0.0061 | 0.0151 | 0.0203 | 0.3391 |
| new | actual | 4-10 | top3_stress | 0.0000 | tau | 295 | 0.0022 | -0.0001 | 0.0000 | 0.0059 | 0.0127 | 0.0000 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.5000 | tau | 295 | 0.0020 | -0.0001 | 0.0000 | 0.0055 | 0.0120 | 0.0169 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.8000 | tau | 295 | 0.0019 | -0.0001 | 0.0000 | 0.0054 | 0.0119 | 0.0169 | 0.1000 |
| new | actual | 11-16 | - | 0.0000 | M | 243 | 0.0079 | -0.0000 | 0.0000 | 0.0000 | 0.0255 |  |  |
| new | actual | 11-16 | linear | 0.0000 | tau | 243 | 0.0268 | 0.0004 | 0.0206 | 0.0393 | 0.0545 | 0.0000 | 0.5000 |
| new | actual | 11-16 | linear | 0.5000 | tau | 243 | 0.0249 | 0.0004 | 0.0187 | 0.0375 | 0.0489 | 0.0000 | 0.5000 |
| new | actual | 11-16 | linear | 0.8000 | tau | 243 | 0.0237 | 0.0004 | 0.0175 | 0.0368 | 0.0469 | 0.0041 | 0.5000 |
| new | actual | 11-16 | concave | 0.0000 | tau | 243 | 0.0205 | 0.0003 | 0.0162 | 0.0289 | 0.0434 | 0.0000 | 0.6599 |
| new | actual | 11-16 | concave | 0.5000 | tau | 243 | 0.0179 | 0.0003 | 0.0143 | 0.0268 | 0.0359 | 0.0000 | 0.6599 |
| new | actual | 11-16 | concave | 0.8000 | tau | 243 | 0.0163 | 0.0003 | 0.0119 | 0.0255 | 0.0334 | 0.0000 | 0.6599 |
| new | actual | 11-16 | convex | 0.0000 | tau | 243 | 0.0305 | 0.0005 | 0.0258 | 0.0439 | 0.0600 | 0.0000 | 0.3391 |
| new | actual | 11-16 | convex | 0.5000 | tau | 243 | 0.0292 | 0.0004 | 0.0226 | 0.0431 | 0.0586 | 0.0041 | 0.3391 |
| new | actual | 11-16 | convex | 0.8000 | tau | 243 | 0.0284 | 0.0004 | 0.0212 | 0.0430 | 0.0552 | 0.0082 | 0.3391 |
| new | actual | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0164 | 0.0003 | 0.0131 | 0.0240 | 0.0339 | 0.0000 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0160 | 0.0003 | 0.0120 | 0.0236 | 0.0315 | 0.0041 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0157 | 0.0003 | 0.0118 | 0.0231 | 0.0315 | 0.0082 | 0.1000 |
| new | actual | 17-30 | - | 0.0000 | M | 586 | 0.0080 | -0.0000 | 0.0000 | 0.0000 | 0.0258 |  |  |
| new | actual | 17-30 | linear | 0.0000 | tau | 586 | 0.0207 | 0.0000 | 0.0145 | 0.0359 | 0.0496 | 0.0000 | 0.5000 |
| new | actual | 17-30 | linear | 0.5000 | tau | 586 | 0.0187 | 0.0000 | 0.0138 | 0.0336 | 0.0463 | 0.0000 | 0.5000 |
| new | actual | 17-30 | linear | 0.8000 | tau | 586 | 0.0175 | 0.0000 | 0.0122 | 0.0320 | 0.0446 | 0.0017 | 0.5000 |
| new | actual | 17-30 | concave | 0.0000 | tau | 586 | 0.0222 | 0.0000 | 0.0199 | 0.0359 | 0.0511 | 0.0000 | 0.6599 |
| new | actual | 17-30 | concave | 0.5000 | tau | 586 | 0.0196 | 0.0000 | 0.0181 | 0.0349 | 0.0436 | 0.0000 | 0.6599 |
| new | actual | 17-30 | concave | 0.8000 | tau | 586 | 0.0180 | 0.0000 | 0.0142 | 0.0332 | 0.0411 | 0.0000 | 0.6599 |
| new | actual | 17-30 | convex | 0.0000 | tau | 586 | 0.0147 | 0.0000 | 0.0046 | 0.0234 | 0.0436 | 0.0000 | 0.3391 |
| new | actual | 17-30 | convex | 0.5000 | tau | 586 | 0.0134 | 0.0000 | 0.0043 | 0.0220 | 0.0388 | 0.0017 | 0.3391 |
| new | actual | 17-30 | convex | 0.8000 | tau | 586 | 0.0126 | 0.0000 | 0.0039 | 0.0206 | 0.0346 | 0.0068 | 0.3391 |
| new | actual | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0036 | 0.0000 | 0.0000 | 0.0024 | 0.0128 | 0.0000 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0032 | 0.0000 | 0.0000 | 0.0025 | 0.0109 | 0.1416 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0030 | 0.0000 | 0.0000 | 0.0024 | 0.0107 | 0.1399 | 0.1000 |
| new | own | all | - | 0.0000 | M | 1252 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | all | linear | 0.0000 | tau | 1252 | 0.0230 | 0.0002 | 0.0158 | 0.0388 | 0.0537 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.5000 | tau | 1252 | 0.0230 | 0.0002 | 0.0158 | 0.0388 | 0.0537 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.8000 | tau | 1252 | 0.0230 | 0.0002 | 0.0158 | 0.0388 | 0.0537 | 0.0000 | 0.5000 |
| new | own | all | concave | 0.0000 | tau | 1252 | 0.0204 | 0.0002 | 0.0202 | 0.0342 | 0.0442 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.5000 | tau | 1252 | 0.0204 | 0.0002 | 0.0202 | 0.0342 | 0.0442 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.8000 | tau | 1252 | 0.0204 | 0.0002 | 0.0202 | 0.0342 | 0.0442 | 0.0000 | 0.6599 |
| new | own | all | convex | 0.0000 | tau | 1252 | 0.0206 | 0.0001 | 0.0094 | 0.0334 | 0.0570 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.5000 | tau | 1252 | 0.0206 | 0.0001 | 0.0094 | 0.0334 | 0.0570 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.8000 | tau | 1252 | 0.0206 | 0.0001 | 0.0094 | 0.0334 | 0.0570 | 0.0000 | 0.3391 |
| new | own | all | top3_stress | 0.0000 | tau | 1252 | 0.0071 | 0.0000 | 0.0005 | 0.0115 | 0.0248 | 0.0000 | 0.1000 |
| new | own | all | top3_stress | 0.5000 | tau | 1252 | 0.0071 | 0.0000 | 0.0005 | 0.0115 | 0.0248 | 0.0942 | 0.1000 |
| new | own | all | top3_stress | 0.8000 | tau | 1252 | 0.0071 | 0.0000 | 0.0005 | 0.0115 | 0.0248 | 0.0935 | 0.1000 |
| new | own | 1-3 | - | 0.0000 | M | 128 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 1-3 | linear | 0.0000 | tau | 128 | -0.0016 | -0.0027 | -0.0007 | -0.0000 | 0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.5000 | tau | 128 | -0.0016 | -0.0027 | -0.0007 | -0.0000 | 0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.8000 | tau | 128 | -0.0016 | -0.0027 | -0.0007 | -0.0000 | 0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | concave | 0.0000 | tau | 128 | -0.0008 | -0.0013 | -0.0003 | -0.0000 | 0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.5000 | tau | 128 | -0.0008 | -0.0013 | -0.0003 | -0.0000 | 0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.8000 | tau | 128 | -0.0008 | -0.0013 | -0.0003 | -0.0000 | 0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | convex | 0.0000 | tau | 128 | -0.0029 | -0.0051 | -0.0012 | -0.0000 | 0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.5000 | tau | 128 | -0.0029 | -0.0051 | -0.0012 | -0.0000 | 0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.8000 | tau | 128 | -0.0029 | -0.0051 | -0.0012 | -0.0000 | 0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | top3_stress | 0.0000 | tau | 128 | -0.0053 | -0.0092 | -0.0022 | -0.0000 | 0.0000 | 0.0000 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.5000 | tau | 128 | -0.0053 | -0.0092 | -0.0022 | -0.0000 | 0.0000 | 0.0469 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.8000 | tau | 128 | -0.0053 | -0.0092 | -0.0022 | -0.0000 | 0.0000 | 0.0469 | 0.1000 |
| new | own | 4-10 | - | 0.0000 | M | 295 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 4-10 | linear | 0.0000 | tau | 295 | 0.0036 | -0.0000 | 0.0002 | 0.0053 | 0.0108 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.5000 | tau | 295 | 0.0036 | -0.0000 | 0.0002 | 0.0053 | 0.0108 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.8000 | tau | 295 | 0.0036 | -0.0000 | 0.0002 | 0.0053 | 0.0108 | 0.0000 | 0.5000 |
| new | own | 4-10 | concave | 0.0000 | tau | 295 | 0.0023 | 0.0000 | 0.0002 | 0.0032 | 0.0066 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.5000 | tau | 295 | 0.0023 | 0.0000 | 0.0002 | 0.0032 | 0.0066 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.8000 | tau | 295 | 0.0023 | 0.0000 | 0.0002 | 0.0032 | 0.0066 | 0.0000 | 0.6599 |
| new | own | 4-10 | convex | 0.0000 | tau | 295 | 0.0046 | -0.0000 | 0.0003 | 0.0076 | 0.0151 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.5000 | tau | 295 | 0.0046 | -0.0000 | 0.0003 | 0.0076 | 0.0151 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.8000 | tau | 295 | 0.0046 | -0.0000 | 0.0003 | 0.0076 | 0.0151 | 0.0000 | 0.3391 |
| new | own | 4-10 | top3_stress | 0.0000 | tau | 295 | 0.0027 | -0.0000 | 0.0000 | 0.0072 | 0.0129 | 0.0000 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.5000 | tau | 295 | 0.0027 | -0.0000 | 0.0000 | 0.0072 | 0.0129 | 0.0305 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.8000 | tau | 295 | 0.0027 | -0.0000 | 0.0000 | 0.0072 | 0.0129 | 0.0305 | 0.1000 |
| new | own | 11-16 | - | 0.0000 | M | 243 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 11-16 | linear | 0.0000 | tau | 243 | 0.0343 | 0.0129 | 0.0333 | 0.0457 | 0.0674 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.5000 | tau | 243 | 0.0343 | 0.0129 | 0.0333 | 0.0457 | 0.0674 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.8000 | tau | 243 | 0.0343 | 0.0129 | 0.0333 | 0.0457 | 0.0674 | 0.0000 | 0.5000 |
| new | own | 11-16 | concave | 0.0000 | tau | 243 | 0.0224 | 0.0078 | 0.0213 | 0.0308 | 0.0439 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.5000 | tau | 243 | 0.0224 | 0.0078 | 0.0213 | 0.0308 | 0.0439 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.8000 | tau | 243 | 0.0224 | 0.0078 | 0.0213 | 0.0308 | 0.0439 | 0.0000 | 0.6599 |
| new | own | 11-16 | convex | 0.0000 | tau | 243 | 0.0420 | 0.0164 | 0.0398 | 0.0551 | 0.0813 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.5000 | tau | 243 | 0.0420 | 0.0164 | 0.0398 | 0.0551 | 0.0813 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.8000 | tau | 243 | 0.0420 | 0.0164 | 0.0398 | 0.0551 | 0.0813 | 0.0000 | 0.3391 |
| new | own | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0222 | 0.0102 | 0.0189 | 0.0276 | 0.0453 | 0.0000 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0222 | 0.0102 | 0.0189 | 0.0276 | 0.0453 | 0.0123 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0222 | 0.0102 | 0.0189 | 0.0276 | 0.0453 | 0.0123 | 0.1000 |
| new | own | 17-30 | - | 0.0000 | M | 586 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 17-30 | linear | 0.0000 | tau | 586 | 0.0335 | 0.0159 | 0.0300 | 0.0446 | 0.0630 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.5000 | tau | 586 | 0.0335 | 0.0159 | 0.0300 | 0.0446 | 0.0630 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.8000 | tau | 586 | 0.0335 | 0.0159 | 0.0300 | 0.0446 | 0.0630 | 0.0000 | 0.5000 |
| new | own | 17-30 | concave | 0.0000 | tau | 586 | 0.0332 | 0.0240 | 0.0324 | 0.0398 | 0.0525 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.5000 | tau | 586 | 0.0332 | 0.0240 | 0.0324 | 0.0398 | 0.0525 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.8000 | tau | 586 | 0.0332 | 0.0240 | 0.0324 | 0.0398 | 0.0525 | 0.0000 | 0.6599 |
| new | own | 17-30 | convex | 0.0000 | tau | 586 | 0.0248 | 0.0043 | 0.0157 | 0.0367 | 0.0609 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.5000 | tau | 586 | 0.0248 | 0.0043 | 0.0157 | 0.0367 | 0.0609 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.8000 | tau | 586 | 0.0248 | 0.0043 | 0.0157 | 0.0367 | 0.0609 | 0.0000 | 0.3391 |
| new | own | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0058 | 0.0000 | 0.0002 | 0.0070 | 0.0205 | 0.0000 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0058 | 0.0000 | 0.0002 | 0.0070 | 0.0205 | 0.1706 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0058 | 0.0000 | 0.0002 | 0.0070 | 0.0205 | 0.1689 | 0.1000 |
| delta | actual | all | - | 0.0000 | M | 1252 | 0.0002 | -0.0000 | 0.0000 | 0.0000 | 0.0052 |  |  |
| delta | actual | all | linear | 0.0000 | tau | 1252 | -0.0014 | -0.0068 | 0.0000 | 0.0011 | 0.0114 | 0.0000 | 0.5000 |
| delta | actual | all | linear | 0.5000 | tau | 1252 | -0.0014 | -0.0068 | 0.0000 | 0.0010 | 0.0105 | 0.0088 | 0.5000 |
| delta | actual | all | linear | 0.8000 | tau | 1252 | -0.0015 | -0.0069 | 0.0000 | 0.0010 | 0.0098 | 0.0112 | 0.5000 |
| delta | actual | all | concave | 0.0000 | tau | 1252 | -0.0007 | -0.0041 | 0.0000 | 0.0011 | 0.0091 | 0.0000 | 0.6599 |
| delta | actual | all | concave | 0.5000 | tau | 1252 | -0.0008 | -0.0040 | 0.0000 | 0.0007 | 0.0071 | 0.0216 | 0.6599 |
| delta | actual | all | concave | 0.8000 | tau | 1252 | -0.0008 | -0.0039 | 0.0000 | 0.0006 | 0.0065 | 0.0375 | 0.6599 |
| delta | actual | all | convex | 0.0000 | tau | 1252 | -0.0022 | -0.0101 | 0.0000 | 0.0015 | 0.0141 | 0.0000 | 0.3391 |
| delta | actual | all | convex | 0.5000 | tau | 1252 | -0.0022 | -0.0104 | 0.0000 | 0.0014 | 0.0138 | 0.0048 | 0.3391 |
| delta | actual | all | convex | 0.8000 | tau | 1252 | -0.0022 | -0.0098 | 0.0000 | 0.0013 | 0.0133 | 0.0056 | 0.3391 |
| delta | actual | all | top3_stress | 0.0000 | tau | 1252 | -0.0018 | -0.0066 | 0.0000 | 0.0011 | 0.0121 | 0.0000 | 0.1000 |
| delta | actual | all | top3_stress | 0.5000 | tau | 1252 | -0.0018 | -0.0063 | 0.0000 | 0.0013 | 0.0117 | 0.0335 | 0.1000 |
| delta | actual | all | top3_stress | 0.8000 | tau | 1252 | -0.0018 | -0.0062 | 0.0000 | 0.0013 | 0.0116 | 0.0335 | 0.1000 |
| delta | actual | 1-3 | - | 0.0000 | M | 128 | -0.0003 | -0.0000 | -0.0000 | 0.0000 | 0.0029 |  |  |
| delta | actual | 1-3 | linear | 0.0000 | tau | 128 | -0.0055 | -0.0079 | -0.0024 | -0.0014 | -0.0003 | 0.0000 | 0.5000 |
| delta | actual | 1-3 | linear | 0.5000 | tau | 128 | -0.0055 | -0.0079 | -0.0026 | -0.0015 | -0.0005 | 0.0312 | 0.5000 |
| delta | actual | 1-3 | linear | 0.8000 | tau | 128 | -0.0054 | -0.0079 | -0.0028 | -0.0017 | -0.0007 | 0.0391 | 0.5000 |
| delta | actual | 1-3 | concave | 0.0000 | tau | 128 | -0.0032 | -0.0044 | -0.0013 | -0.0004 | 0.0013 | 0.0000 | 0.6599 |
| delta | actual | 1-3 | concave | 0.5000 | tau | 128 | -0.0031 | -0.0044 | -0.0013 | -0.0006 | 0.0000 | 0.0625 | 0.6599 |
| delta | actual | 1-3 | concave | 0.8000 | tau | 128 | -0.0030 | -0.0041 | -0.0014 | -0.0008 | -0.0003 | 0.1172 | 0.6599 |
| delta | actual | 1-3 | convex | 0.0000 | tau | 128 | -0.0090 | -0.0139 | -0.0045 | -0.0028 | -0.0011 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | convex | 0.5000 | tau | 128 | -0.0090 | -0.0126 | -0.0046 | -0.0029 | -0.0010 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | convex | 0.8000 | tau | 128 | -0.0090 | -0.0122 | -0.0048 | -0.0029 | -0.0010 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | top3_stress | 0.0000 | tau | 128 | -0.0098 | -0.0155 | -0.0033 | -0.0004 | -0.0000 | 0.0000 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.5000 | tau | 128 | -0.0097 | -0.0160 | -0.0033 | -0.0004 | -0.0000 | 0.0078 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.8000 | tau | 128 | -0.0097 | -0.0162 | -0.0032 | -0.0004 | -0.0000 | 0.0078 | 0.1000 |
| delta | actual | 4-10 | - | 0.0000 | M | 295 | -0.0035 | -0.0003 | -0.0000 | 0.0000 | 0.0030 |  |  |
| delta | actual | 4-10 | linear | 0.0000 | tau | 295 | -0.0129 | -0.0205 | -0.0114 | -0.0048 | 0.0000 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | linear | 0.5000 | tau | 295 | -0.0120 | -0.0182 | -0.0108 | -0.0057 | 0.0000 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | linear | 0.8000 | tau | 295 | -0.0115 | -0.0172 | -0.0102 | -0.0059 | 0.0000 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | concave | 0.0000 | tau | 295 | -0.0089 | -0.0132 | -0.0065 | -0.0024 | 0.0000 | 0.0000 | 0.6599 |
| delta | actual | 4-10 | concave | 0.5000 | tau | 295 | -0.0077 | -0.0123 | -0.0062 | -0.0025 | 0.0000 | 0.0373 | 0.6599 |
| delta | actual | 4-10 | concave | 0.8000 | tau | 295 | -0.0070 | -0.0111 | -0.0061 | -0.0030 | 0.0000 | 0.0542 | 0.6599 |
| delta | actual | 4-10 | convex | 0.0000 | tau | 295 | -0.0178 | -0.0262 | -0.0172 | -0.0095 | 0.0000 | 0.0000 | 0.3391 |
| delta | actual | 4-10 | convex | 0.5000 | tau | 295 | -0.0172 | -0.0252 | -0.0164 | -0.0094 | 0.0000 | 0.0136 | 0.3391 |
| delta | actual | 4-10 | convex | 0.8000 | tau | 295 | -0.0169 | -0.0244 | -0.0152 | -0.0093 | 0.0000 | 0.0136 | 0.3391 |
| delta | actual | 4-10 | top3_stress | 0.0000 | tau | 295 | -0.0155 | -0.0211 | -0.0145 | -0.0079 | 0.0000 | 0.0000 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.5000 | tau | 295 | -0.0153 | -0.0210 | -0.0142 | -0.0078 | 0.0000 | 0.0034 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.8000 | tau | 295 | -0.0152 | -0.0211 | -0.0142 | -0.0078 | 0.0000 | 0.0034 | 0.1000 |
| delta | actual | 11-16 | - | 0.0000 | M | 243 | -0.0019 | -0.0000 | 0.0000 | 0.0000 | 0.0008 |  |  |
| delta | actual | 11-16 | linear | 0.0000 | tau | 243 | -0.0004 | -0.0100 | 0.0000 | 0.0072 | 0.0202 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | linear | 0.5000 | tau | 243 | 0.0001 | -0.0093 | 0.0000 | 0.0065 | 0.0175 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | linear | 0.8000 | tau | 243 | 0.0004 | -0.0088 | 0.0000 | 0.0061 | 0.0150 | 0.0041 | 0.5000 |
| delta | actual | 11-16 | concave | 0.0000 | tau | 243 | -0.0013 | -0.0072 | 0.0000 | 0.0041 | 0.0134 | 0.0000 | 0.6599 |
| delta | actual | 11-16 | concave | 0.5000 | tau | 243 | -0.0007 | -0.0066 | 0.0000 | 0.0040 | 0.0118 | 0.0041 | 0.6599 |
| delta | actual | 11-16 | concave | 0.8000 | tau | 243 | -0.0003 | -0.0063 | 0.0000 | 0.0035 | 0.0110 | 0.0041 | 0.6599 |
| delta | actual | 11-16 | convex | 0.0000 | tau | 243 | 0.0019 | -0.0100 | 0.0000 | 0.0102 | 0.0236 | 0.0000 | 0.3391 |
| delta | actual | 11-16 | convex | 0.5000 | tau | 243 | 0.0023 | -0.0096 | 0.0000 | 0.0102 | 0.0223 | 0.0082 | 0.3391 |
| delta | actual | 11-16 | convex | 0.8000 | tau | 243 | 0.0025 | -0.0092 | 0.0000 | 0.0102 | 0.0223 | 0.0123 | 0.3391 |
| delta | actual | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0076 | 0.0000 | 0.0038 | 0.0135 | 0.0215 | 0.0000 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0077 | 0.0000 | 0.0041 | 0.0135 | 0.0214 | 0.0329 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0077 | 0.0000 | 0.0046 | 0.0135 | 0.0206 | 0.0329 | 0.1000 |
| delta | actual | 17-30 | - | 0.0000 | M | 586 | 0.0030 | 0.0000 | 0.0000 | 0.0000 | 0.0100 |  |  |
| delta | actual | 17-30 | linear | 0.0000 | tau | 586 | 0.0049 | 0.0000 | 0.0000 | 0.0042 | 0.0170 | 0.0000 | 0.5000 |
| delta | actual | 17-30 | linear | 0.5000 | tau | 586 | 0.0041 | 0.0000 | 0.0000 | 0.0040 | 0.0139 | 0.0119 | 0.5000 |
| delta | actual | 17-30 | linear | 0.8000 | tau | 586 | 0.0037 | 0.0000 | 0.0000 | 0.0039 | 0.0127 | 0.0137 | 0.5000 |
| delta | actual | 17-30 | concave | 0.0000 | tau | 586 | 0.0042 | 0.0000 | 0.0000 | 0.0029 | 0.0153 | 0.0000 | 0.6599 |
| delta | actual | 17-30 | concave | 0.5000 | tau | 586 | 0.0032 | 0.0000 | 0.0000 | 0.0025 | 0.0111 | 0.0119 | 0.6599 |
| delta | actual | 17-30 | concave | 0.8000 | tau | 586 | 0.0026 | 0.0000 | 0.0000 | 0.0025 | 0.0089 | 0.0256 | 0.6599 |
| delta | actual | 17-30 | convex | 0.0000 | tau | 586 | 0.0055 | 0.0000 | 0.0000 | 0.0055 | 0.0187 | 0.0000 | 0.3391 |
| delta | actual | 17-30 | convex | 0.5000 | tau | 586 | 0.0050 | 0.0000 | 0.0000 | 0.0053 | 0.0171 | 0.0000 | 0.3391 |
| delta | actual | 17-30 | convex | 0.8000 | tau | 586 | 0.0047 | 0.0000 | 0.0000 | 0.0053 | 0.0157 | 0.0000 | 0.3391 |
| delta | actual | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0030 | 0.0000 | 0.0000 | 0.0022 | 0.0108 | 0.0000 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0029 | 0.0000 | 0.0000 | 0.0023 | 0.0102 | 0.0546 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0028 | 0.0000 | 0.0000 | 0.0023 | 0.0097 | 0.0546 | 0.1000 |
| delta | own | all | - | 0.0000 | M | 1252 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | all | linear | 0.0000 | tau | 1252 | -0.0004 | -0.0074 | 0.0000 | 0.0039 | 0.0142 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.5000 | tau | 1252 | -0.0004 | -0.0074 | 0.0000 | 0.0039 | 0.0142 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.8000 | tau | 1252 | -0.0004 | -0.0074 | 0.0000 | 0.0039 | 0.0142 | 0.0000 | 0.5000 |
| delta | own | all | concave | 0.0000 | tau | 1252 | -0.0002 | -0.0043 | -0.0000 | 0.0021 | 0.0085 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.5000 | tau | 1252 | -0.0002 | -0.0043 | -0.0000 | 0.0021 | 0.0085 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.8000 | tau | 1252 | -0.0002 | -0.0043 | -0.0000 | 0.0021 | 0.0085 | 0.0000 | 0.6599 |
| delta | own | all | convex | 0.0000 | tau | 1252 | -0.0006 | -0.0113 | 0.0000 | 0.0065 | 0.0210 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.5000 | tau | 1252 | -0.0006 | -0.0113 | 0.0000 | 0.0065 | 0.0210 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.8000 | tau | 1252 | -0.0006 | -0.0113 | 0.0000 | 0.0065 | 0.0210 | 0.0000 | 0.3391 |
| delta | own | all | top3_stress | 0.0000 | tau | 1252 | -0.0004 | -0.0080 | 0.0000 | 0.0050 | 0.0172 | 0.0000 | 0.1000 |
| delta | own | all | top3_stress | 0.5000 | tau | 1252 | -0.0004 | -0.0080 | 0.0000 | 0.0050 | 0.0172 | 0.0128 | 0.1000 |
| delta | own | all | top3_stress | 0.8000 | tau | 1252 | -0.0004 | -0.0080 | 0.0000 | 0.0050 | 0.0172 | 0.0128 | 0.1000 |
| delta | own | 1-3 | - | 0.0000 | M | 128 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 1-3 | linear | 0.0000 | tau | 128 | -0.0048 | -0.0063 | -0.0030 | -0.0019 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.5000 | tau | 128 | -0.0048 | -0.0063 | -0.0030 | -0.0019 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.8000 | tau | 128 | -0.0048 | -0.0063 | -0.0030 | -0.0019 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | concave | 0.0000 | tau | 128 | -0.0026 | -0.0033 | -0.0016 | -0.0010 | -0.0007 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.5000 | tau | 128 | -0.0026 | -0.0033 | -0.0016 | -0.0010 | -0.0007 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.8000 | tau | 128 | -0.0026 | -0.0033 | -0.0016 | -0.0010 | -0.0007 | 0.0000 | 0.6599 |
| delta | own | 1-3 | convex | 0.0000 | tau | 128 | -0.0084 | -0.0110 | -0.0051 | -0.0033 | -0.0024 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.5000 | tau | 128 | -0.0084 | -0.0110 | -0.0051 | -0.0033 | -0.0024 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.8000 | tau | 128 | -0.0084 | -0.0110 | -0.0051 | -0.0033 | -0.0024 | 0.0000 | 0.3391 |
| delta | own | 1-3 | top3_stress | 0.0000 | tau | 128 | -0.0096 | -0.0155 | -0.0031 | -0.0004 | -0.0000 | 0.0000 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.5000 | tau | 128 | -0.0096 | -0.0155 | -0.0031 | -0.0004 | -0.0000 | 0.0000 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.8000 | tau | 128 | -0.0096 | -0.0155 | -0.0031 | -0.0004 | -0.0000 | 0.0000 | 0.1000 |
| delta | own | 4-10 | - | 0.0000 | M | 295 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 4-10 | linear | 0.0000 | tau | 295 | -0.0121 | -0.0168 | -0.0107 | -0.0070 | -0.0041 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.5000 | tau | 295 | -0.0121 | -0.0168 | -0.0107 | -0.0070 | -0.0041 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.8000 | tau | 295 | -0.0121 | -0.0168 | -0.0107 | -0.0070 | -0.0041 | 0.0000 | 0.5000 |
| delta | own | 4-10 | concave | 0.0000 | tau | 295 | -0.0069 | -0.0099 | -0.0059 | -0.0040 | -0.0023 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.5000 | tau | 295 | -0.0069 | -0.0099 | -0.0059 | -0.0040 | -0.0023 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.8000 | tau | 295 | -0.0069 | -0.0099 | -0.0059 | -0.0040 | -0.0023 | 0.0000 | 0.6599 |
| delta | own | 4-10 | convex | 0.0000 | tau | 295 | -0.0186 | -0.0253 | -0.0172 | -0.0112 | -0.0070 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.5000 | tau | 295 | -0.0186 | -0.0253 | -0.0172 | -0.0112 | -0.0070 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.8000 | tau | 295 | -0.0186 | -0.0253 | -0.0172 | -0.0112 | -0.0070 | 0.0000 | 0.3391 |
| delta | own | 4-10 | top3_stress | 0.0000 | tau | 295 | -0.0164 | -0.0211 | -0.0158 | -0.0099 | -0.0042 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.5000 | tau | 295 | -0.0164 | -0.0211 | -0.0158 | -0.0099 | -0.0042 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.8000 | tau | 295 | -0.0164 | -0.0211 | -0.0158 | -0.0099 | -0.0042 | 0.0000 | 0.1000 |
| delta | own | 11-16 | - | 0.0000 | M | 243 | 0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 11-16 | linear | 0.0000 | tau | 243 | 0.0022 | -0.0103 | 0.0026 | 0.0107 | 0.0198 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.5000 | tau | 243 | 0.0022 | -0.0103 | 0.0026 | 0.0107 | 0.0198 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.8000 | tau | 243 | 0.0022 | -0.0103 | 0.0026 | 0.0107 | 0.0198 | 0.0000 | 0.5000 |
| delta | own | 11-16 | concave | 0.0000 | tau | 243 | 0.0008 | -0.0066 | 0.0012 | 0.0060 | 0.0113 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.5000 | tau | 243 | 0.0008 | -0.0066 | 0.0012 | 0.0060 | 0.0113 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.8000 | tau | 243 | 0.0008 | -0.0066 | 0.0012 | 0.0060 | 0.0113 | 0.0000 | 0.6599 |
| delta | own | 11-16 | convex | 0.0000 | tau | 243 | 0.0054 | -0.0115 | 0.0059 | 0.0177 | 0.0309 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.5000 | tau | 243 | 0.0054 | -0.0115 | 0.0059 | 0.0177 | 0.0309 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.8000 | tau | 243 | 0.0054 | -0.0115 | 0.0059 | 0.0177 | 0.0309 | 0.0000 | 0.3391 |
| delta | own | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0112 | -0.0002 | 0.0096 | 0.0180 | 0.0287 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0112 | -0.0002 | 0.0096 | 0.0180 | 0.0287 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0112 | -0.0002 | 0.0096 | 0.0180 | 0.0287 | 0.0000 | 0.1000 |
| delta | own | 17-30 | - | 0.0000 | M | 586 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 17-30 | linear | 0.0000 | tau | 586 | 0.0054 | 0.0000 | 0.0001 | 0.0078 | 0.0176 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.5000 | tau | 586 | 0.0054 | 0.0000 | 0.0001 | 0.0078 | 0.0176 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.8000 | tau | 586 | 0.0054 | 0.0000 | 0.0001 | 0.0078 | 0.0176 | 0.0000 | 0.5000 |
| delta | own | 17-30 | concave | 0.0000 | tau | 586 | 0.0033 | 0.0000 | 0.0000 | 0.0048 | 0.0107 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.5000 | tau | 586 | 0.0033 | 0.0000 | 0.0000 | 0.0048 | 0.0107 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.8000 | tau | 586 | 0.0033 | 0.0000 | 0.0000 | 0.0048 | 0.0107 | 0.0000 | 0.6599 |
| delta | own | 17-30 | convex | 0.0000 | tau | 586 | 0.0076 | 0.0000 | 0.0003 | 0.0108 | 0.0247 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.5000 | tau | 586 | 0.0076 | 0.0000 | 0.0003 | 0.0108 | 0.0247 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.8000 | tau | 586 | 0.0076 | 0.0000 | 0.0003 | 0.0108 | 0.0247 | 0.0000 | 0.3391 |
| delta | own | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0049 | 0.0000 | 0.0002 | 0.0063 | 0.0167 | 0.0000 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0049 | 0.0000 | 0.0002 | 0.0063 | 0.0167 | 0.0273 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0049 | 0.0000 | 0.0002 | 0.0063 | 0.0167 | 0.0273 | 0.1000 |

## T5_attr_seeding

| rule | portfolio | seed_group | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| old | actual | <0.01 | B | dominance_positive | 0.7057 | 0.5896 | 0.8000 | 384 |
| old | actual | <0.01 | B | reversal | 0.0469 | 0.0115 | 0.0816 | 384 |
| old | actual | <0.01 | B | negligible | 0.1901 | 0.1019 | 0.2984 | 384 |
| old | actual | <0.01 | B | unresolved | 0.0573 | 0.0195 | 0.1197 | 384 |
| old | actual | 0.01-0.05 | B | dominance_positive | 0.6974 | 0.4706 | 0.9219 | 76 |
| old | actual | 0.01-0.05 | B | reversal | 0.0789 | 0.0000 | 0.2031 | 76 |
| old | actual | 0.01-0.05 | B | negligible | 0.2237 | 0.0417 | 0.4167 | 76 |
| old | actual | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 76 |
| old | actual | >=0.05 | B | dominance_positive | 0.7184 | 0.5933 | 0.8172 | 792 |
| old | actual | >=0.05 | B | reversal | 0.0265 | 0.0061 | 0.0618 | 792 |
| old | actual | >=0.05 | B | negligible | 0.2424 | 0.1624 | 0.3388 | 792 |
| old | actual | >=0.05 | B | unresolved | 0.0126 | 0.0000 | 0.0345 | 792 |
| old | own | <0.01 | B | dominance_positive | 0.8984 | 0.8053 | 0.9824 | 384 |
| old | own | <0.01 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 384 |
| old | own | <0.01 | B | negligible | 0.1016 | 0.0176 | 0.1947 | 384 |
| old | own | <0.01 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 384 |
| old | own | 0.01-0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 76 |
| old | own | 0.01-0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 76 |
| old | own | 0.01-0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 76 |
| old | own | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 76 |
| old | own | >=0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 792 |
| old | own | >=0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 792 |
| old | own | >=0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 792 |
| old | own | >=0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 792 |
| new | actual | <0.01 | B | dominance_positive | 0.1328 | 0.0669 | 0.2171 | 384 |
| new | actual | <0.01 | B | reversal | 0.3255 | 0.1882 | 0.4639 | 384 |
| new | actual | <0.01 | B | negligible | 0.4688 | 0.3354 | 0.6026 | 384 |
| new | actual | <0.01 | B | unresolved | 0.0729 | 0.0241 | 0.1560 | 384 |
| new | actual | 0.01-0.05 | B | dominance_positive | 0.5921 | 0.3571 | 0.8551 | 76 |
| new | actual | 0.01-0.05 | B | reversal | 0.0658 | 0.0000 | 0.2000 | 76 |
| new | actual | 0.01-0.05 | B | negligible | 0.3421 | 0.0941 | 0.5443 | 76 |
| new | actual | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 76 |
| new | actual | >=0.05 | B | dominance_positive | 0.7348 | 0.6300 | 0.8106 | 792 |
| new | actual | >=0.05 | B | reversal | 0.0303 | 0.0051 | 0.0614 | 792 |
| new | actual | >=0.05 | B | negligible | 0.2260 | 0.1535 | 0.3177 | 792 |
| new | actual | >=0.05 | B | unresolved | 0.0088 | 0.0011 | 0.0212 | 792 |
| new | own | <0.01 | B | dominance_positive | 0.1641 | 0.0857 | 0.2515 | 384 |
| new | own | <0.01 | B | reversal | 0.3151 | 0.1694 | 0.4724 | 384 |
| new | own | <0.01 | B | negligible | 0.5026 | 0.3746 | 0.6379 | 384 |
| new | own | <0.01 | B | unresolved | 0.0182 | 0.0000 | 0.0420 | 384 |
| new | own | 0.01-0.05 | B | dominance_positive | 0.8816 | 0.7679 | 0.9804 | 76 |
| new | own | 0.01-0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 76 |
| new | own | 0.01-0.05 | B | negligible | 0.1184 | 0.0196 | 0.2321 | 76 |
| new | own | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 76 |
| new | own | >=0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 792 |
| new | own | >=0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 792 |
| new | own | >=0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 792 |
| new | own | >=0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 792 |

## T5_attr_ledger_features

| rule | feature | value | n | reversal_share | lo99 | hi99 |
|---|---|---|---|---|---|---|
| old | holds_conditional_other | True | 529 | 0.0851 | 0.0377 | 0.1396 |
| old | holds_conditional_other | False | 723 | 0.0000 | 0.0000 | 0.0000 |
| old | holds_opponent_pick | True | 43 | 0.4651 | 0.2400 | 0.6970 |
| old | holds_opponent_pick | False | 1209 | 0.0207 | 0.0056 | 0.0422 |
| old | holds_pooled_pick | True | 379 | 0.0633 | 0.0030 | 0.1706 |
| old | holds_pooled_pick | False | 873 | 0.0241 | 0.0069 | 0.0435 |
| old | self_restricted | True | 103 | 0.0388 | 0.0000 | 0.1200 |
| old | self_restricted | False | 1149 | 0.0357 | 0.0148 | 0.0614 |
| old | opp_restricted | True | 103 | 0.0097 | 0.0000 | 0.0649 |
| old | opp_restricted | False | 1149 | 0.0383 | 0.0156 | 0.0696 |
| old | holds_conditional_other_state | True | 472 | 0.0932 | 0.0416 | 0.1615 |
| old | holds_conditional_other_state | False | 780 | 0.0013 | 0.0000 | 0.0075 |
| old | holds_opponent_pick_state | True | 39 | 0.5128 | 0.2593 | 0.7436 |
| old | holds_opponent_pick_state | False | 1213 | 0.0206 | 0.0056 | 0.0420 |
| new | holds_conditional_other | True | 529 | 0.1739 | 0.0864 | 0.2475 |
| new | holds_conditional_other | False | 723 | 0.0858 | 0.0353 | 0.1436 |
| new | holds_opponent_pick | True | 43 | 0.4884 | 0.2449 | 0.7778 |
| new | holds_opponent_pick | False | 1209 | 0.1100 | 0.0526 | 0.1468 |
| new | holds_pooled_pick | True | 379 | 0.1372 | 0.0392 | 0.2472 |
| new | holds_pooled_pick | False | 873 | 0.1168 | 0.0593 | 0.1777 |
| new | self_restricted | True | 103 | 0.1553 | 0.0090 | 0.3153 |
| new | self_restricted | False | 1149 | 0.1201 | 0.0558 | 0.1651 |
| new | opp_restricted | True | 103 | 0.0874 | 0.0000 | 0.1979 |
| new | opp_restricted | False | 1149 | 0.1262 | 0.0634 | 0.1662 |
| new | holds_conditional_other_state | True | 500 | 0.1640 | 0.0825 | 0.2274 |
| new | holds_conditional_other_state | False | 752 | 0.0957 | 0.0387 | 0.1530 |
| new | holds_opponent_pick_state | True | 40 | 0.5000 | 0.2542 | 0.7667 |
| new | holds_opponent_pick_state | False | 1212 | 0.1106 | 0.0530 | 0.1479 |

## T5_6_transitions

| portfolio | old | new | count |
|---|---|---|---|
| actual | dominance_positive | dominance_positive | 642 |
| actual | dominance_positive | negligible | 119 |
| actual | dominance_positive | reversal | 112 |
| actual | dominance_positive | unresolved | 20 |
| actual | negligible | dominance_positive | 23 |
| actual | negligible | negligible | 257 |
| actual | negligible | reversal | 1 |
| actual | negligible | unresolved | 1 |
| actual | reversal | dominance_positive | 3 |
| actual | reversal | negligible | 5 |
| actual | reversal | reversal | 35 |
| actual | reversal | unresolved | 2 |
| actual | unresolved | dominance_positive | 10 |
| actual | unresolved | negligible | 4 |
| actual | unresolved | reversal | 6 |
| actual | unresolved | unresolved | 12 |
| own | dominance_positive | dominance_positive | 922 |
| own | dominance_positive | negligible | 163 |
| own | dominance_positive | reversal | 121 |
| own | dominance_positive | unresolved | 7 |
| own | negligible | negligible | 39 |

## T5_headline_reversal_diff

| contrast | portfolio | verdict | share_a | share_b | diff | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| new_minus_old | actual | verdict_B | 0.1230 | 0.0359 | 0.0871 | 0.0350 | 0.1258 | 1252 |
| new_minus_old | actual | verdict_B_pm | 0.1038 | 0.0264 | 0.0775 | 0.0366 | 0.1102 | 1252 |
| new_minus_old | own | verdict_B | 0.0966 | 0.0000 | 0.0966 | 0.0469 | 0.1361 | 1252 |
| new_minus_old | own | verdict_B_pm | 0.0911 | 0.0000 | 0.0911 | 0.0436 | 0.1300 | 1252 |
| actual_minus_own | old | verdict_B | 0.0359 | 0.0000 | 0.0359 | 0.0146 | 0.0637 | 1252 |
| actual_minus_own | new | verdict_B | 0.1230 | 0.0966 | 0.0264 | 0.0065 | 0.0484 | 1252 |

## T5_4_typology

| rule | curve | type | share | lo99 | hi99 | n | tp_dominated_share | n_tp_defined |
|---|---|---|---|---|---|---|---|---|
| old | linear | both_lose | 0.4633 | 0.2929 | 0.6417 | 290 | 0.3000 | 290 |
| old | linear | both_win | 0.0016 | 0.0000 | 0.0097 | 1 | 0.0000 | 1 |
| old | linear | normal | 0.3882 | 0.2979 | 0.4615 | 243 | 0.7490 | 243 |
| old | linear | opposed | 0.0160 | 0.0016 | 0.0374 | 10 | 0.9000 | 10 |
| old | linear | one_sided_win | 0.0160 | 0.0000 | 0.0383 | 10 | 0.8000 | 10 |
| old | linear | no_own_stake | 0.1150 | 0.0375 | 0.2184 | 72 | 1.0000 | 61 |
| old | concave | both_lose | 0.4137 | 0.2579 | 0.5881 | 259 | 0.3398 | 259 |
| old | concave | both_win | 0.0016 | 0.0000 | 0.0097 | 1 | 0.0000 | 1 |
| old | concave | normal | 0.4153 | 0.3283 | 0.4943 | 260 | 0.7143 | 259 |
| old | concave | opposed | 0.0176 | 0.0047 | 0.0346 | 11 | 0.8182 | 11 |
| old | concave | one_sided_win | 0.0144 | 0.0000 | 0.0365 | 9 | 0.7778 | 9 |
| old | concave | no_own_stake | 0.1374 | 0.0493 | 0.2459 | 86 | 1.0000 | 71 |
| old | convex | both_lose | 0.4569 | 0.3211 | 0.5845 | 286 | 0.2133 | 286 |
| old | convex | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| old | convex | normal | 0.4153 | 0.3462 | 0.4769 | 260 | 0.6409 | 259 |
| old | convex | opposed | 0.0096 | 0.0000 | 0.0241 | 6 | 0.8333 | 6 |
| old | convex | one_sided_win | 0.0128 | 0.0000 | 0.0353 | 8 | 0.6250 | 8 |
| old | convex | no_own_stake | 0.1054 | 0.0435 | 0.1875 | 66 | 1.0000 | 49 |
| old | top3_stress | both_lose | 0.1805 | 0.1269 | 0.2540 | 113 | 0.0088 | 113 |
| old | top3_stress | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| old | top3_stress | normal | 0.4521 | 0.3904 | 0.5312 | 283 | 0.1321 | 280 |
| old | top3_stress | opposed | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| old | top3_stress | one_sided_win | 0.0048 | 0.0000 | 0.0178 | 3 | 0.3333 | 3 |
| old | top3_stress | no_own_stake | 0.3626 | 0.2848 | 0.4329 | 227 | 0.9744 | 39 |
| new | linear | both_lose | 0.2780 | 0.1618 | 0.3861 | 174 | 0.2644 | 174 |
| new | linear | both_win | 0.0048 | 0.0000 | 0.0182 | 3 | 0.3333 | 3 |
| new | linear | normal | 0.3978 | 0.3344 | 0.4703 | 249 | 0.6129 | 248 |
| new | linear | opposed | 0.0735 | 0.0239 | 0.1305 | 46 | 0.4130 | 46 |
| new | linear | one_sided_win | 0.0415 | 0.0065 | 0.0958 | 26 | 0.7692 | 26 |
| new | linear | no_own_stake | 0.2045 | 0.0986 | 0.3222 | 128 | 1.0000 | 80 |
| new | concave | both_lose | 0.2907 | 0.1733 | 0.3926 | 182 | 0.3187 | 182 |
| new | concave | both_win | 0.0016 | 0.0000 | 0.0097 | 1 | 0.0000 | 1 |
| new | concave | normal | 0.4185 | 0.3496 | 0.4880 | 262 | 0.6450 | 262 |
| new | concave | opposed | 0.0431 | 0.0097 | 0.0848 | 27 | 0.5926 | 27 |
| new | concave | one_sided_win | 0.0319 | 0.0036 | 0.0745 | 20 | 0.7000 | 20 |
| new | concave | no_own_stake | 0.2141 | 0.1122 | 0.3389 | 134 | 1.0000 | 86 |
| new | convex | both_lose | 0.2412 | 0.1409 | 0.3529 | 151 | 0.2252 | 151 |
| new | convex | both_win | 0.0048 | 0.0000 | 0.0181 | 3 | 0.0000 | 3 |
| new | convex | normal | 0.3930 | 0.3217 | 0.4734 | 246 | 0.5246 | 244 |
| new | convex | opposed | 0.0783 | 0.0222 | 0.1416 | 49 | 0.3061 | 49 |
| new | convex | one_sided_win | 0.0527 | 0.0138 | 0.1019 | 33 | 0.5455 | 33 |
| new | convex | no_own_stake | 0.2300 | 0.1340 | 0.3423 | 144 | 1.0000 | 73 |
| new | top3_stress | both_lose | 0.1278 | 0.0708 | 0.1897 | 80 | 0.0375 | 80 |
| new | top3_stress | both_win | 0.0064 | 0.0000 | 0.0216 | 4 | 0.0000 | 4 |
| new | top3_stress | normal | 0.3403 | 0.2624 | 0.4416 | 213 | 0.2404 | 208 |
| new | top3_stress | opposed | 0.0559 | 0.0204 | 0.0921 | 35 | 0.0286 | 35 |
| new | top3_stress | one_sided_win | 0.1102 | 0.0449 | 0.1701 | 69 | 0.3077 | 65 |
| new | top3_stress | no_own_stake | 0.3594 | 0.2736 | 0.4541 | 225 | 1.0000 | 62 |

## T5_5_stakes_distribution

| rule | curve | measure | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| old | linear | tp_share | 615 | 0.5701 | 0.4137 | 0.5327 | 0.7632 | 1.0000 |
| old | linear | tp_share_raw | 620 | 0.6215 | 0.4989 | 0.5745 | 0.7840 | 0.9442 |
| old | linear | hhi | 615 | 0.3090 | 0.2116 | 0.2763 | 0.3615 | 0.4982 |
| old | linear | n_material | 626 | 6.4058 | 4.0000 | 7.0000 | 9.0000 | 10.0000 |
| old | linear | mean_abs_third | 626 | 0.0017 | 0.0008 | 0.0015 | 0.0023 | 0.0033 |
| old | linear | mean_abs_third_raw | 626 | 0.0020 | 0.0012 | 0.0018 | 0.0027 | 0.0036 |
| old | concave | tp_share | 610 | 0.5964 | 0.4383 | 0.5598 | 0.8188 | 1.0000 |
| old | concave | tp_share_raw | 619 | 0.6453 | 0.5006 | 0.6068 | 0.8247 | 0.9575 |
| old | concave | hhi | 610 | 0.3138 | 0.2121 | 0.2806 | 0.3723 | 0.5000 |
| old | concave | n_material | 626 | 5.8594 | 4.0000 | 6.0000 | 8.0000 | 10.0000 |
| old | concave | mean_abs_third | 626 | 0.0018 | 0.0008 | 0.0016 | 0.0024 | 0.0035 |
| old | concave | mean_abs_third_raw | 626 | 0.0021 | 0.0011 | 0.0019 | 0.0028 | 0.0038 |
| old | convex | tp_share | 608 | 0.5098 | 0.3617 | 0.4881 | 0.6872 | 0.9319 |
| old | convex | tp_share_raw | 618 | 0.5979 | 0.4897 | 0.5476 | 0.7377 | 0.9259 |
| old | convex | hhi | 608 | 0.3616 | 0.2414 | 0.3165 | 0.4112 | 0.5247 |
| old | convex | n_material | 626 | 5.3914 | 3.0000 | 5.0000 | 7.0000 | 9.0000 |
| old | convex | mean_abs_third | 626 | 0.0013 | 0.0005 | 0.0011 | 0.0018 | 0.0026 |
| old | convex | mean_abs_third_raw | 626 | 0.0016 | 0.0009 | 0.0015 | 0.0022 | 0.0030 |
| old | top3_stress | tp_share | 435 | 0.3776 | 0.1927 | 0.4108 | 0.4773 | 0.7859 |
| old | top3_stress | tp_share_raw | 484 | 0.5302 | 0.4828 | 0.5011 | 0.5225 | 0.8490 |
| old | top3_stress | hhi | 435 | 0.5279 | 0.3581 | 0.4437 | 0.5813 | 1.0000 |
| old | top3_stress | n_material | 626 | 2.2061 | 0.0000 | 2.0000 | 4.0000 | 5.0000 |
| old | top3_stress | mean_abs_third | 626 | 0.0003 | 0.0000 | 0.0001 | 0.0005 | 0.0009 |
| old | top3_stress | mean_abs_third_raw | 626 | 0.0005 | 0.0001 | 0.0004 | 0.0007 | 0.0011 |
| new | linear | tp_share | 577 | 0.5894 | 0.4363 | 0.5260 | 0.7744 | 1.0000 |
| new | linear | tp_share_raw | 596 | 0.6380 | 0.5019 | 0.5900 | 0.8043 | 0.9795 |
| new | linear | hhi | 577 | 0.3184 | 0.2249 | 0.2977 | 0.3750 | 0.5000 |
| new | linear | n_material | 626 | 5.6518 | 3.0000 | 6.0000 | 8.0000 | 10.0000 |
| new | linear | mean_abs_third | 626 | 0.0017 | 0.0006 | 0.0013 | 0.0023 | 0.0036 |
| new | linear | mean_abs_third_raw | 626 | 0.0019 | 0.0009 | 0.0016 | 0.0026 | 0.0040 |
| new | concave | tp_share | 578 | 0.6110 | 0.4578 | 0.5543 | 0.8048 | 1.0000 |
| new | concave | tp_share_raw | 597 | 0.6510 | 0.5069 | 0.6040 | 0.8108 | 0.9812 |
| new | concave | hhi | 578 | 0.3117 | 0.2185 | 0.2912 | 0.3745 | 0.4669 |
| new | concave | n_material | 626 | 5.6230 | 3.0000 | 6.0000 | 8.0000 | 10.0000 |
| new | concave | mean_abs_third | 626 | 0.0018 | 0.0007 | 0.0015 | 0.0025 | 0.0036 |
| new | concave | mean_abs_third_raw | 626 | 0.0020 | 0.0011 | 0.0017 | 0.0027 | 0.0038 |
| new | convex | tp_share | 553 | 0.5418 | 0.3918 | 0.4946 | 0.7141 | 1.0000 |
| new | convex | tp_share_raw | 585 | 0.6183 | 0.5000 | 0.5523 | 0.7515 | 0.9643 |
| new | convex | hhi | 553 | 0.3881 | 0.2578 | 0.3370 | 0.4450 | 0.5792 |
| new | convex | n_material | 626 | 4.4904 | 2.0000 | 4.0000 | 7.0000 | 8.0000 |
| new | convex | mean_abs_third | 626 | 0.0014 | 0.0003 | 0.0008 | 0.0019 | 0.0033 |
| new | convex | mean_abs_third_raw | 626 | 0.0016 | 0.0005 | 0.0012 | 0.0022 | 0.0036 |
| new | top3_stress | tp_share | 454 | 0.4628 | 0.3236 | 0.4545 | 0.5443 | 1.0000 |
| new | top3_stress | tp_share_raw | 498 | 0.5805 | 0.4963 | 0.5047 | 0.6385 | 0.9761 |
| new | top3_stress | hhi | 454 | 0.4824 | 0.3399 | 0.4150 | 0.5133 | 1.0000 |
| new | top3_stress | n_material | 626 | 2.4153 | 0.0000 | 2.0000 | 4.0000 | 5.0000 |
| new | top3_stress | mean_abs_third | 626 | 0.0005 | 0.0000 | 0.0002 | 0.0007 | 0.0012 |
| new | top3_stress | mean_abs_third_raw | 626 | 0.0006 | 0.0001 | 0.0004 | 0.0009 | 0.0014 |
| new_minus_old | linear | tp_share | 577 | 0.0138 | -0.0303 | 0.0001 | 0.0749 | 0.1630 |
| new_minus_old | linear | hhi | 577 | 0.0241 | -0.0259 | 0.0032 | 0.0664 | 0.1562 |
| new_minus_old | linear | mean_abs_third | 626 | -0.0000 | -0.0004 | 0.0000 | 0.0004 | 0.0010 |
| new_minus_old | concave | tp_share | 576 | 0.0111 | -0.0338 | 0.0000 | 0.0652 | 0.1764 |
| new_minus_old | concave | hhi | 576 | 0.0121 | -0.0406 | 0.0000 | 0.0472 | 0.1309 |
| new_minus_old | concave | mean_abs_third | 626 | -0.0001 | -0.0003 | 0.0000 | 0.0003 | 0.0009 |
| new_minus_old | convex | tp_share | 553 | 0.0218 | -0.0506 | 0.0042 | 0.1038 | 0.2308 |
| new_minus_old | convex | hhi | 553 | 0.0396 | -0.0466 | 0.0051 | 0.0937 | 0.2051 |
| new_minus_old | convex | mean_abs_third | 626 | 0.0001 | -0.0005 | 0.0000 | 0.0005 | 0.0014 |
| new_minus_old | top3_stress | tp_share | 359 | 0.1155 | -0.0106 | 0.0760 | 0.3257 | 0.4705 |
| new_minus_old | top3_stress | hhi | 359 | -0.1050 | -0.3024 | -0.0460 | 0.0771 | 0.2462 |
| new_minus_old | top3_stress | mean_abs_third | 626 | 0.0002 | -0.0002 | 0.0000 | 0.0005 | 0.0010 |

## H2

| curve | sample | n_games | mean_diff_new_minus_old | lo99 | hi99 | registered | supported |
|---|---|---|---|---|---|---|---|
| linear | registered | 520 | 0.0000 | -0.0002 | 0.0002 | True | False |
| linear | state_conditional | 480 | 0.0000 | -0.0002 | 0.0002 | False | False |
| concave | registered | 520 | -0.0000 | -0.0003 | 0.0002 | False | False |
| concave | state_conditional | 480 | -0.0000 | -0.0003 | 0.0002 | False | False |
| convex | registered | 520 | 0.0001 | -0.0001 | 0.0003 | False | False |
| convex | state_conditional | 480 | 0.0001 | -0.0001 | 0.0004 | False | False |
| top3_stress | registered | 520 | 0.0002 | 0.0001 | 0.0004 | False | True |
| top3_stress | state_conditional | 480 | 0.0002 | 0.0001 | 0.0004 | False | True |

## F5_2_network_edges

10440 rows in `F5_2_network_edges.csv`.

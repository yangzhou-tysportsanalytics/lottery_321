# Registered analysis output

tag `defer`; exclude_imprecise=False; states=100

## T5_0_diagnostics

| states | games | stopped_2000 | stopped_8000 | stopped_32000 | missed_target | n_worlds_match | max_halfwidth_linear | max_halfwidth_linear_rules_only | max_halfwidth_delta_linear | p95_halfwidth_linear | max_q_total_dev | max_per_slot_dev | per_slot_noise_scale | max_own_slot_dev | max_zero_sum_dev |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 100 | 789 | 1 | 8 | 45 | 46 | 2000 | 0.0078 | 0.0078 | 0.0066 | 0.0051 | 0.0000 | 0.0116 | 0.0112 | 0.0000 | 0.0041 |

## T5_0b_zero_sum_by_curve

| curve | rule | max_zero_sum_dev | mean_zero_sum_dev | n_games |
|---|---|---|---|---|
| linear | old | 0.0006 | 0.0001 | 789 |
| linear | new | 0.0008 | 0.0001 | 789 |
| concave | old | 0.0003 | 0.0000 | 789 |
| concave | new | 0.0005 | 0.0001 | 789 |
| convex | old | 0.0009 | 0.0001 | 789 |
| convex | new | 0.0011 | 0.0001 | 789 |
| top3_stress | old | 0.0041 | 0.0003 | 789 |
| top3_stress | new | 0.0018 | 0.0002 | 789 |

## T5_0c_verdict_by_look

| rule | portfolio | stopped_at | verdict_B | verdict_B_pm | count |
|---|---|---|---|---|---|
| delta | actual | 2000 | reversal | reversal | 2 |
| delta | actual | 32000 | dominance_positive | dominance_positive | 52 |
| delta | actual | 32000 | dominance_positive | unresolved | 48 |
| delta | actual | 32000 | negligible | dominance_positive | 1 |
| delta | actual | 32000 | negligible | negligible | 178 |
| delta | actual | 32000 | negligible | unresolved | 17 |
| delta | actual | 32000 | reversal | reversal | 308 |
| delta | actual | 32000 | reversal | unresolved | 46 |
| delta | actual | 32000 | unresolved | unresolved | 28 |
| delta | actual | 8000 | dominance_positive | dominance_positive | 2 |
| delta | actual | 8000 | dominance_positive | unresolved | 1 |
| delta | actual | 8000 | negligible | negligible | 24 |
| delta | actual | 8000 | negligible | unresolved | 4 |
| delta | actual | 8000 | reversal | reversal | 25 |
| delta | actual | 8000 | reversal | unresolved | 3 |
| delta | actual | 8000 | unresolved | unresolved | 7 |
| delta | actual | missed | dominance_positive | dominance_positive | 76 |
| delta | actual | missed | dominance_positive | unresolved | 34 |
| delta | actual | missed | negligible | dominance_positive | 3 |
| delta | actual | missed | negligible | negligible | 193 |
| delta | actual | missed | negligible | unresolved | 15 |
| delta | actual | missed | reversal | reversal | 429 |
| delta | actual | missed | reversal | unresolved | 43 |
| delta | actual | missed | unresolved | unresolved | 39 |
| delta | own | 2000 | reversal | reversal | 2 |
| delta | own | 32000 | dominance_positive | dominance_positive | 2 |
| delta | own | 32000 | dominance_positive | unresolved | 50 |
| delta | own | 32000 | negligible | negligible | 104 |
| delta | own | 32000 | negligible | unresolved | 23 |
| delta | own | 32000 | reversal | reversal | 369 |
| delta | own | 32000 | reversal | unresolved | 85 |
| delta | own | 32000 | unresolved | unresolved | 45 |
| delta | own | 8000 | dominance_positive | dominance_positive | 1 |
| delta | own | 8000 | dominance_positive | unresolved | 1 |
| delta | own | 8000 | negligible | negligible | 13 |
| delta | own | 8000 | negligible | unresolved | 6 |
| delta | own | 8000 | reversal | reversal | 32 |
| delta | own | 8000 | reversal | unresolved | 4 |
| delta | own | 8000 | unresolved | unresolved | 9 |
| delta | own | missed | dominance_positive | dominance_positive | 5 |
| delta | own | missed | dominance_positive | unresolved | 33 |
| delta | own | missed | negligible | negligible | 139 |
| delta | own | missed | negligible | unresolved | 19 |
| delta | own | missed | reversal | reversal | 526 |
| delta | own | missed | reversal | unresolved | 63 |
| delta | own | missed | unresolved | unresolved | 47 |
| new | actual | 2000 | reversal | reversal | 2 |
| new | actual | 32000 | dominance_positive | dominance_positive | 369 |
| new | actual | 32000 | dominance_positive | unresolved | 14 |
| new | actual | 32000 | negligible | dominance_positive | 12 |
| new | actual | 32000 | negligible | negligible | 140 |
| new | actual | 32000 | negligible | unresolved | 15 |
| new | actual | 32000 | reversal | reversal | 79 |
| new | actual | 32000 | reversal | unresolved | 29 |
| new | actual | 32000 | unresolved | unresolved | 20 |
| new | actual | 8000 | dominance_positive | dominance_positive | 38 |
| new | actual | 8000 | dominance_positive | unresolved | 1 |
| new | actual | 8000 | negligible | dominance_positive | 1 |
| new | actual | 8000 | negligible | negligible | 17 |
| new | actual | 8000 | negligible | unresolved | 1 |
| new | actual | 8000 | reversal | reversal | 4 |
| new | actual | 8000 | reversal | unresolved | 1 |
| new | actual | 8000 | unresolved | unresolved | 3 |
| new | actual | missed | dominance_positive | dominance_positive | 410 |
| new | actual | missed | dominance_positive | unresolved | 35 |
| new | actual | missed | negligible | dominance_positive | 8 |
| new | actual | missed | negligible | negligible | 193 |
| new | actual | missed | negligible | unresolved | 28 |
| new | actual | missed | reversal | reversal | 113 |
| new | actual | missed | reversal | unresolved | 21 |
| new | actual | missed | unresolved | unresolved | 24 |
| new | own | 2000 | reversal | reversal | 2 |
| new | own | 32000 | dominance_positive | dominance_positive | 488 |
| new | own | 32000 | dominance_positive | unresolved | 13 |
| new | own | 32000 | negligible | dominance_positive | 11 |
| new | own | 32000 | negligible | negligible | 68 |
| new | own | 32000 | negligible | unresolved | 3 |
| new | own | 32000 | reversal | reversal | 73 |
| new | own | 32000 | reversal | unresolved | 11 |
| new | own | 32000 | unresolved | unresolved | 11 |
| new | own | 8000 | dominance_positive | dominance_positive | 49 |
| new | own | 8000 | negligible | dominance_positive | 1 |
| new | own | 8000 | negligible | negligible | 11 |
| new | own | 8000 | reversal | reversal | 4 |
| new | own | 8000 | reversal | unresolved | 1 |
| new | own | missed | dominance_positive | dominance_positive | 555 |
| new | own | missed | dominance_positive | unresolved | 10 |
| new | own | missed | negligible | dominance_positive | 16 |
| new | own | missed | negligible | negligible | 158 |
| new | own | missed | negligible | unresolved | 4 |
| new | own | missed | reversal | reversal | 73 |
| new | own | missed | reversal | unresolved | 12 |
| new | own | missed | unresolved | unresolved | 4 |
| old | actual | 2000 | dominance_positive | dominance_positive | 2 |
| old | actual | 32000 | dominance_positive | dominance_positive | 465 |
| old | actual | 32000 | dominance_positive | unresolved | 40 |
| old | actual | 32000 | negligible | dominance_positive | 2 |
| old | actual | 32000 | negligible | negligible | 120 |
| old | actual | 32000 | negligible | unresolved | 3 |
| old | actual | 32000 | reversal | reversal | 18 |
| old | actual | 32000 | reversal | unresolved | 14 |
| old | actual | 32000 | unresolved | unresolved | 16 |
| old | actual | 8000 | dominance_positive | dominance_positive | 44 |
| old | actual | 8000 | dominance_positive | unresolved | 2 |
| old | actual | 8000 | negligible | negligible | 14 |
| old | actual | 8000 | reversal | unresolved | 1 |
| old | actual | 8000 | unresolved | unresolved | 5 |
| old | actual | missed | dominance_positive | dominance_positive | 543 |
| old | actual | missed | dominance_positive | unresolved | 62 |
| old | actual | missed | negligible | dominance_positive | 7 |
| old | actual | missed | negligible | negligible | 134 |
| old | actual | missed | negligible | unresolved | 5 |
| old | actual | missed | reversal | reversal | 44 |
| old | actual | missed | reversal | unresolved | 11 |
| old | actual | missed | unresolved | unresolved | 26 |
| old | own | 2000 | dominance_positive | dominance_positive | 2 |
| old | own | 32000 | dominance_positive | dominance_positive | 645 |
| old | own | 32000 | dominance_positive | unresolved | 14 |
| old | own | 32000 | negligible | negligible | 17 |
| old | own | 32000 | negligible | unresolved | 2 |
| old | own | 8000 | dominance_positive | dominance_positive | 60 |
| old | own | 8000 | dominance_positive | unresolved | 2 |
| old | own | 8000 | negligible | negligible | 3 |
| old | own | 8000 | unresolved | unresolved | 1 |
| old | own | missed | dominance_positive | dominance_positive | 787 |
| old | own | missed | dominance_positive | unresolved | 16 |
| old | own | missed | negligible | dominance_positive | 1 |
| old | own | missed | negligible | negligible | 24 |
| old | own | missed | negligible | unresolved | 3 |
| old | own | missed | unresolved | unresolved | 1 |

## T5_0d_band_width

| rule | portfolio | measure | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| old | actual | band_ratio | 1578 | 1.5248 | 0.3621 | 1.4816 | 2.5312 | 2.9881 |
| old | actual | band_ratio_pm | 1578 | 5.8239 | 1.4432 | 5.7277 | 10.0137 | 11.5830 |
| old | own | band_ratio | 1578 | 1.9890 | 0.7017 | 2.3329 | 2.7384 | 3.1215 |
| old | own | band_ratio_pm | 1578 | 7.6148 | 2.6166 | 9.2388 | 10.8310 | 12.1822 |
| new | actual | band_ratio | 1578 | 1.2243 | 0.1458 | 0.6638 | 2.3899 | 2.8620 |
| new | actual | band_ratio_pm | 1578 | 4.6723 | 0.5537 | 2.5315 | 9.5128 | 11.2343 |
| new | own | band_ratio | 1578 | 1.5939 | 0.2243 | 2.0410 | 2.6506 | 3.0209 |
| new | own | band_ratio_pm | 1578 | 6.1106 | 0.8894 | 8.1415 | 10.5317 | 11.7851 |
| delta | actual | band_ratio | 1578 | 1.0385 | 0.1574 | 0.6855 | 1.6641 | 2.5035 |
| delta | actual | band_ratio_pm | 1578 | 4.0167 | 0.5909 | 2.6788 | 6.5022 | 9.7140 |
| delta | own | band_ratio | 1578 | 1.3112 | 0.4330 | 0.9834 | 2.1502 | 2.8656 |
| delta | own | band_ratio_pm | 1578 | 5.0566 | 1.7099 | 3.7681 | 8.4076 | 11.0961 |

## T5_1_verdicts

| rule | portfolio | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|
| old | actual | B | dominance_positive | 0.7338 | 0.7027 | 0.7600 | 1578 |
| old | actual | B | reversal | 0.0558 | 0.0288 | 0.0830 | 1578 |
| old | actual | B | negligible | 0.1806 | 0.1410 | 0.2284 | 1578 |
| old | actual | B | unresolved | 0.0298 | 0.0200 | 0.0405 | 1578 |
| old | actual | C | dominance_positive | 0.7338 | 0.7027 | 0.7600 | 1578 |
| old | actual | C | reversal | 0.0558 | 0.0288 | 0.0830 | 1578 |
| old | actual | C | negligible | 0.1806 | 0.1410 | 0.2284 | 1578 |
| old | actual | C | unresolved | 0.0298 | 0.0200 | 0.0405 | 1578 |
| old | actual | B_pm | dominance_positive | 0.6736 | 0.6464 | 0.7012 | 1578 |
| old | actual | B_pm | reversal | 0.0393 | 0.0166 | 0.0625 | 1578 |
| old | actual | B_pm | negligible | 0.1698 | 0.1242 | 0.2249 | 1578 |
| old | actual | B_pm | unresolved | 0.1172 | 0.0817 | 0.1523 | 1578 |
| old | actual | C_pm | dominance_positive | 0.6736 | 0.6464 | 0.7012 | 1578 |
| old | actual | C_pm | reversal | 0.0393 | 0.0166 | 0.0625 | 1578 |
| old | actual | C_pm | negligible | 0.1698 | 0.1242 | 0.2249 | 1578 |
| old | actual | C_pm | unresolved | 0.1172 | 0.0817 | 0.1523 | 1578 |
| old | own | B | dominance_positive | 0.9670 | 0.9468 | 0.9841 | 1578 |
| old | own | B | reversal | 0.0000 | 0.0000 | 0.0000 | 1578 |
| old | own | B | negligible | 0.0317 | 0.0149 | 0.0531 | 1578 |
| old | own | B | unresolved | 0.0013 | 0.0000 | 0.0051 | 1578 |
| old | own | C | dominance_positive | 0.9670 | 0.9468 | 0.9841 | 1578 |
| old | own | C | reversal | 0.0000 | 0.0000 | 0.0000 | 1578 |
| old | own | C | negligible | 0.0317 | 0.0149 | 0.0531 | 1578 |
| old | own | C | unresolved | 0.0013 | 0.0000 | 0.0051 | 1578 |
| old | own | B_pm | dominance_positive | 0.9474 | 0.9274 | 0.9644 | 1578 |
| old | own | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 1578 |
| old | own | B_pm | negligible | 0.0279 | 0.0118 | 0.0497 | 1578 |
| old | own | B_pm | unresolved | 0.0247 | 0.0124 | 0.0373 | 1578 |
| old | own | C_pm | dominance_positive | 0.9474 | 0.9274 | 0.9644 | 1578 |
| old | own | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 1578 |
| old | own | C_pm | negligible | 0.0279 | 0.0118 | 0.0497 | 1578 |
| old | own | C_pm | unresolved | 0.0247 | 0.0124 | 0.0373 | 1578 |
| new | actual | B | dominance_positive | 0.5494 | 0.5205 | 0.5785 | 1578 |
| new | actual | B | reversal | 0.1578 | 0.1391 | 0.1749 | 1578 |
| new | actual | B | negligible | 0.2630 | 0.2279 | 0.3014 | 1578 |
| new | actual | B | unresolved | 0.0298 | 0.0129 | 0.0477 | 1578 |
| new | actual | C | dominance_positive | 0.5494 | 0.5205 | 0.5785 | 1578 |
| new | actual | C | reversal | 0.1578 | 0.1391 | 0.1749 | 1578 |
| new | actual | C | negligible | 0.2630 | 0.2279 | 0.3014 | 1578 |
| new | actual | C | unresolved | 0.0298 | 0.0129 | 0.0477 | 1578 |
| new | actual | B_pm | dominance_positive | 0.5311 | 0.4897 | 0.5819 | 1578 |
| new | actual | B_pm | reversal | 0.1255 | 0.1029 | 0.1448 | 1578 |
| new | actual | B_pm | negligible | 0.2218 | 0.1742 | 0.2766 | 1578 |
| new | actual | B_pm | unresolved | 0.1217 | 0.0670 | 0.1800 | 1578 |
| new | actual | C_pm | dominance_positive | 0.5311 | 0.4897 | 0.5819 | 1578 |
| new | actual | C_pm | reversal | 0.1255 | 0.1029 | 0.1448 | 1578 |
| new | actual | C_pm | negligible | 0.2218 | 0.1742 | 0.2766 | 1578 |
| new | actual | C_pm | unresolved | 0.1217 | 0.0670 | 0.1800 | 1578 |
| new | own | B | dominance_positive | 0.7066 | 0.6682 | 0.7436 | 1578 |
| new | own | B | reversal | 0.1115 | 0.0800 | 0.1452 | 1578 |
| new | own | B | negligible | 0.1724 | 0.1154 | 0.2239 | 1578 |
| new | own | B | unresolved | 0.0095 | 0.0038 | 0.0164 | 1578 |
| new | own | C | dominance_positive | 0.7066 | 0.6682 | 0.7436 | 1578 |
| new | own | C | reversal | 0.1115 | 0.0800 | 0.1452 | 1578 |
| new | own | C | negligible | 0.1724 | 0.1154 | 0.2239 | 1578 |
| new | own | C | unresolved | 0.0095 | 0.0038 | 0.0164 | 1578 |
| new | own | B_pm | dominance_positive | 0.7098 | 0.6688 | 0.7513 | 1578 |
| new | own | B_pm | reversal | 0.0963 | 0.0706 | 0.1245 | 1578 |
| new | own | B_pm | negligible | 0.1502 | 0.0925 | 0.2026 | 1578 |
| new | own | B_pm | unresolved | 0.0437 | 0.0305 | 0.0591 | 1578 |
| new | own | C_pm | dominance_positive | 0.7098 | 0.6688 | 0.7513 | 1578 |
| new | own | C_pm | reversal | 0.0963 | 0.0706 | 0.1245 | 1578 |
| new | own | C_pm | negligible | 0.1502 | 0.0925 | 0.2026 | 1578 |
| new | own | C_pm | unresolved | 0.0437 | 0.0305 | 0.0591 | 1578 |
| delta | actual | B | dominance_positive | 0.1350 | 0.1123 | 0.1574 | 1578 |
| delta | actual | B | reversal | 0.5425 | 0.4902 | 0.5930 | 1578 |
| delta | actual | B | negligible | 0.2757 | 0.2235 | 0.3429 | 1578 |
| delta | actual | B | unresolved | 0.0469 | 0.0332 | 0.0622 | 1578 |
| delta | actual | C | dominance_positive | 0.1350 | 0.1123 | 0.1574 | 1578 |
| delta | actual | C | reversal | 0.5425 | 0.4902 | 0.5930 | 1578 |
| delta | actual | C | negligible | 0.2757 | 0.2235 | 0.3429 | 1578 |
| delta | actual | C | unresolved | 0.0469 | 0.0332 | 0.0622 | 1578 |
| delta | actual | B_pm | dominance_positive | 0.0849 | 0.0533 | 0.1154 | 1578 |
| delta | actual | B_pm | reversal | 0.4842 | 0.4387 | 0.5251 | 1578 |
| delta | actual | B_pm | negligible | 0.2503 | 0.1951 | 0.3195 | 1578 |
| delta | actual | B_pm | unresolved | 0.1806 | 0.1534 | 0.2103 | 1578 |
| delta | actual | C_pm | dominance_positive | 0.0849 | 0.0533 | 0.1154 | 1578 |
| delta | actual | C_pm | reversal | 0.4842 | 0.4387 | 0.5251 | 1578 |
| delta | actual | C_pm | negligible | 0.2503 | 0.1951 | 0.3195 | 1578 |
| delta | actual | C_pm | unresolved | 0.1806 | 0.1534 | 0.2103 | 1578 |
| delta | own | B | dominance_positive | 0.0583 | 0.0335 | 0.0867 | 1578 |
| delta | own | B | reversal | 0.6850 | 0.6373 | 0.7302 | 1578 |
| delta | own | B | negligible | 0.1926 | 0.1704 | 0.2239 | 1578 |
| delta | own | B | unresolved | 0.0640 | 0.0442 | 0.0875 | 1578 |
| delta | own | C | dominance_positive | 0.0583 | 0.0335 | 0.0867 | 1578 |
| delta | own | C | reversal | 0.6850 | 0.6373 | 0.7302 | 1578 |
| delta | own | C | negligible | 0.1926 | 0.1704 | 0.2239 | 1578 |
| delta | own | C | unresolved | 0.0640 | 0.0442 | 0.0875 | 1578 |
| delta | own | B_pm | dominance_positive | 0.0051 | 0.0007 | 0.0110 | 1578 |
| delta | own | B_pm | reversal | 0.5887 | 0.5227 | 0.6495 | 1578 |
| delta | own | B_pm | negligible | 0.1622 | 0.1400 | 0.1985 | 1578 |
| delta | own | B_pm | unresolved | 0.2440 | 0.1919 | 0.3113 | 1578 |
| delta | own | C_pm | dominance_positive | 0.0051 | 0.0007 | 0.0110 | 1578 |
| delta | own | C_pm | reversal | 0.5887 | 0.5227 | 0.6495 | 1578 |
| delta | own | C_pm | negligible | 0.1622 | 0.1400 | 0.1985 | 1578 |
| delta | own | C_pm | unresolved | 0.2440 | 0.1919 | 0.3113 | 1578 |

## T5_2_verdicts_by_band

| rule | portfolio | band | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| old | actual | 1-3 | B | dominance_positive | 0.8187 | 0.7468 | 0.8874 | 160 |
| old | actual | 1-3 | B | reversal | 0.0375 | 0.0000 | 0.1007 | 160 |
| old | actual | 1-3 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 160 |
| old | actual | 1-3 | B | unresolved | 0.1437 | 0.0797 | 0.2162 | 160 |
| old | actual | 1-3 | C | dominance_positive | 0.8187 | 0.7468 | 0.8874 | 160 |
| old | actual | 1-3 | C | reversal | 0.0375 | 0.0000 | 0.1007 | 160 |
| old | actual | 1-3 | C | negligible | 0.0000 | 0.0000 | 0.0000 | 160 |
| old | actual | 1-3 | C | unresolved | 0.1437 | 0.0797 | 0.2162 | 160 |
| old | actual | 1-3 | B_pm | dominance_positive | 0.6438 | 0.5783 | 0.7067 | 160 |
| old | actual | 1-3 | B_pm | reversal | 0.0312 | 0.0000 | 0.0838 | 160 |
| old | actual | 1-3 | B_pm | negligible | 0.0000 | 0.0000 | 0.0000 | 160 |
| old | actual | 1-3 | B_pm | unresolved | 0.3250 | 0.2581 | 0.3902 | 160 |
| old | actual | 1-3 | C_pm | dominance_positive | 0.6438 | 0.5783 | 0.7067 | 160 |
| old | actual | 1-3 | C_pm | reversal | 0.0312 | 0.0000 | 0.0838 | 160 |
| old | actual | 1-3 | C_pm | negligible | 0.0000 | 0.0000 | 0.0000 | 160 |
| old | actual | 1-3 | C_pm | unresolved | 0.3250 | 0.2581 | 0.3902 | 160 |
| old | actual | 4-10 | B | dominance_positive | 0.7875 | 0.7259 | 0.8571 | 367 |
| old | actual | 4-10 | B | reversal | 0.0708 | 0.0299 | 0.1200 | 367 |
| old | actual | 4-10 | B | negligible | 0.1117 | 0.0398 | 0.1765 | 367 |
| old | actual | 4-10 | B | unresolved | 0.0300 | 0.0105 | 0.0543 | 367 |
| old | actual | 4-10 | C | dominance_positive | 0.7875 | 0.7259 | 0.8571 | 367 |
| old | actual | 4-10 | C | reversal | 0.0708 | 0.0299 | 0.1200 | 367 |
| old | actual | 4-10 | C | negligible | 0.1117 | 0.0398 | 0.1765 | 367 |
| old | actual | 4-10 | C | unresolved | 0.0300 | 0.0105 | 0.0543 | 367 |
| old | actual | 4-10 | B_pm | dominance_positive | 0.6567 | 0.5395 | 0.7843 | 367 |
| old | actual | 4-10 | B_pm | reversal | 0.0463 | 0.0171 | 0.0811 | 367 |
| old | actual | 4-10 | B_pm | negligible | 0.1117 | 0.0398 | 0.1765 | 367 |
| old | actual | 4-10 | B_pm | unresolved | 0.1853 | 0.1108 | 0.2623 | 367 |
| old | actual | 4-10 | C_pm | dominance_positive | 0.6567 | 0.5395 | 0.7843 | 367 |
| old | actual | 4-10 | C_pm | reversal | 0.0463 | 0.0171 | 0.0811 | 367 |
| old | actual | 4-10 | C_pm | negligible | 0.1117 | 0.0398 | 0.1765 | 367 |
| old | actual | 4-10 | C_pm | unresolved | 0.1853 | 0.1108 | 0.2623 | 367 |
| old | actual | 11-16 | B | dominance_positive | 0.6901 | 0.5151 | 0.8495 | 313 |
| old | actual | 11-16 | B | reversal | 0.0735 | 0.0000 | 0.1656 | 313 |
| old | actual | 11-16 | B | negligible | 0.2268 | 0.0224 | 0.4664 | 313 |
| old | actual | 11-16 | B | unresolved | 0.0096 | 0.0000 | 0.0282 | 313 |
| old | actual | 11-16 | C | dominance_positive | 0.6901 | 0.5151 | 0.8495 | 313 |
| old | actual | 11-16 | C | reversal | 0.0735 | 0.0000 | 0.1656 | 313 |
| old | actual | 11-16 | C | negligible | 0.2268 | 0.0224 | 0.4664 | 313 |
| old | actual | 11-16 | C | unresolved | 0.0096 | 0.0000 | 0.0282 | 313 |
| old | actual | 11-16 | B_pm | dominance_positive | 0.6613 | 0.5082 | 0.7963 | 313 |
| old | actual | 11-16 | B_pm | reversal | 0.0703 | 0.0000 | 0.1656 | 313 |
| old | actual | 11-16 | B_pm | negligible | 0.2109 | 0.0094 | 0.4551 | 313 |
| old | actual | 11-16 | B_pm | unresolved | 0.0575 | 0.0192 | 0.1029 | 313 |
| old | actual | 11-16 | C_pm | dominance_positive | 0.6613 | 0.5082 | 0.7963 | 313 |
| old | actual | 11-16 | C_pm | reversal | 0.0703 | 0.0000 | 0.1656 | 313 |
| old | actual | 11-16 | C_pm | negligible | 0.2109 | 0.0094 | 0.4551 | 313 |
| old | actual | 11-16 | C_pm | unresolved | 0.0575 | 0.0192 | 0.1029 | 313 |
| old | actual | 17-30 | B | dominance_positive | 0.7073 | 0.6589 | 0.7555 | 738 |
| old | actual | 17-30 | B | reversal | 0.0447 | 0.0164 | 0.0740 | 738 |
| old | actual | 17-30 | B | negligible | 0.2344 | 0.2012 | 0.2668 | 738 |
| old | actual | 17-30 | B | unresolved | 0.0136 | 0.0027 | 0.0291 | 738 |
| old | actual | 17-30 | C | dominance_positive | 0.7073 | 0.6589 | 0.7555 | 738 |
| old | actual | 17-30 | C | reversal | 0.0447 | 0.0164 | 0.0740 | 738 |
| old | actual | 17-30 | C | negligible | 0.2344 | 0.2012 | 0.2668 | 738 |
| old | actual | 17-30 | C | unresolved | 0.0136 | 0.0027 | 0.0291 | 738 |
| old | actual | 17-30 | B_pm | dominance_positive | 0.6938 | 0.6574 | 0.7364 | 738 |
| old | actual | 17-30 | B_pm | reversal | 0.0244 | 0.0102 | 0.0405 | 738 |
| old | actual | 17-30 | B_pm | negligible | 0.2182 | 0.1777 | 0.2575 | 738 |
| old | actual | 17-30 | B_pm | unresolved | 0.0637 | 0.0287 | 0.0987 | 738 |
| old | actual | 17-30 | C_pm | dominance_positive | 0.6938 | 0.6574 | 0.7364 | 738 |
| old | actual | 17-30 | C_pm | reversal | 0.0244 | 0.0102 | 0.0405 | 738 |
| old | actual | 17-30 | C_pm | negligible | 0.2182 | 0.1777 | 0.2575 | 738 |
| old | actual | 17-30 | C_pm | unresolved | 0.0637 | 0.0287 | 0.0987 | 738 |
| old | own | 1-3 | B | dominance_positive | 0.9938 | 0.9689 | 1.0000 | 160 |
| old | own | 1-3 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 160 |
| old | own | 1-3 | B | negligible | 0.0063 | 0.0000 | 0.0311 | 160 |
| old | own | 1-3 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 160 |
| old | own | 1-3 | C | dominance_positive | 0.9938 | 0.9689 | 1.0000 | 160 |
| old | own | 1-3 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 160 |
| old | own | 1-3 | C | negligible | 0.0063 | 0.0000 | 0.0311 | 160 |
| old | own | 1-3 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 160 |
| old | own | 1-3 | B_pm | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 160 |
| old | own | 1-3 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 160 |
| old | own | 1-3 | B_pm | negligible | 0.0000 | 0.0000 | 0.0000 | 160 |
| old | own | 1-3 | B_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 160 |
| old | own | 1-3 | C_pm | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 160 |
| old | own | 1-3 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 160 |
| old | own | 1-3 | C_pm | negligible | 0.0000 | 0.0000 | 0.0000 | 160 |
| old | own | 1-3 | C_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 160 |
| old | own | 4-10 | B | dominance_positive | 0.9782 | 0.9419 | 1.0000 | 367 |
| old | own | 4-10 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 367 |
| old | own | 4-10 | B | negligible | 0.0163 | 0.0000 | 0.0529 | 367 |
| old | own | 4-10 | B | unresolved | 0.0054 | 0.0000 | 0.0221 | 367 |
| old | own | 4-10 | C | dominance_positive | 0.9782 | 0.9419 | 1.0000 | 367 |
| old | own | 4-10 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 367 |
| old | own | 4-10 | C | negligible | 0.0163 | 0.0000 | 0.0529 | 367 |
| old | own | 4-10 | C | unresolved | 0.0054 | 0.0000 | 0.0221 | 367 |
| old | own | 4-10 | B_pm | dominance_positive | 0.9428 | 0.8956 | 0.9871 | 367 |
| old | own | 4-10 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 367 |
| old | own | 4-10 | B_pm | negligible | 0.0163 | 0.0000 | 0.0529 | 367 |
| old | own | 4-10 | B_pm | unresolved | 0.0409 | 0.0052 | 0.0847 | 367 |
| old | own | 4-10 | C_pm | dominance_positive | 0.9428 | 0.8956 | 0.9871 | 367 |
| old | own | 4-10 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 367 |
| old | own | 4-10 | C_pm | negligible | 0.0163 | 0.0000 | 0.0529 | 367 |
| old | own | 4-10 | C_pm | unresolved | 0.0409 | 0.0052 | 0.0847 | 367 |
| old | own | 11-16 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 313 |
| old | own | 11-16 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 313 |
| old | own | 11-16 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 313 |
| old | own | 11-16 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 313 |
| old | own | 11-16 | C | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 313 |
| old | own | 11-16 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 313 |
| old | own | 11-16 | C | negligible | 0.0000 | 0.0000 | 0.0000 | 313 |
| old | own | 11-16 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 313 |
| old | own | 11-16 | B_pm | dominance_positive | 0.9585 | 0.9301 | 0.9833 | 313 |
| old | own | 11-16 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 313 |
| old | own | 11-16 | B_pm | negligible | 0.0000 | 0.0000 | 0.0000 | 313 |
| old | own | 11-16 | B_pm | unresolved | 0.0415 | 0.0167 | 0.0699 | 313 |
| old | own | 11-16 | C_pm | dominance_positive | 0.9585 | 0.9301 | 0.9833 | 313 |
| old | own | 11-16 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 313 |
| old | own | 11-16 | C_pm | negligible | 0.0000 | 0.0000 | 0.0000 | 313 |
| old | own | 11-16 | C_pm | unresolved | 0.0415 | 0.0167 | 0.0699 | 313 |
| old | own | 17-30 | B | dominance_positive | 0.9417 | 0.9050 | 0.9728 | 738 |
| old | own | 17-30 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 738 |
| old | own | 17-30 | B | negligible | 0.0583 | 0.0272 | 0.0950 | 738 |
| old | own | 17-30 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 738 |
| old | own | 17-30 | C | dominance_positive | 0.9417 | 0.9050 | 0.9728 | 738 |
| old | own | 17-30 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 738 |
| old | own | 17-30 | C | negligible | 0.0583 | 0.0272 | 0.0950 | 738 |
| old | own | 17-30 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 738 |
| old | own | 17-30 | B_pm | dominance_positive | 0.9336 | 0.8975 | 0.9654 | 738 |
| old | own | 17-30 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 738 |
| old | own | 17-30 | B_pm | negligible | 0.0515 | 0.0229 | 0.0864 | 738 |
| old | own | 17-30 | B_pm | unresolved | 0.0149 | 0.0050 | 0.0274 | 738 |
| old | own | 17-30 | C_pm | dominance_positive | 0.9336 | 0.8975 | 0.9654 | 738 |
| old | own | 17-30 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 738 |
| old | own | 17-30 | C_pm | negligible | 0.0515 | 0.0229 | 0.0864 | 738 |
| old | own | 17-30 | C_pm | unresolved | 0.0149 | 0.0050 | 0.0274 | 738 |
| new | actual | 1-3 | B | dominance_positive | 0.1250 | 0.0061 | 0.2791 | 160 |
| new | actual | 1-3 | B | reversal | 0.5813 | 0.3248 | 0.8654 | 160 |
| new | actual | 1-3 | B | negligible | 0.1562 | 0.0392 | 0.2989 | 160 |
| new | actual | 1-3 | B | unresolved | 0.1375 | 0.0485 | 0.2454 | 160 |
| new | actual | 1-3 | C | dominance_positive | 0.1250 | 0.0061 | 0.2791 | 160 |
| new | actual | 1-3 | C | reversal | 0.5813 | 0.3248 | 0.8654 | 160 |
| new | actual | 1-3 | C | negligible | 0.1562 | 0.0392 | 0.2989 | 160 |
| new | actual | 1-3 | C | unresolved | 0.1375 | 0.0485 | 0.2454 | 160 |
| new | actual | 1-3 | B_pm | dominance_positive | 0.0813 | 0.0000 | 0.1977 | 160 |
| new | actual | 1-3 | B_pm | reversal | 0.4562 | 0.3052 | 0.6309 | 160 |
| new | actual | 1-3 | B_pm | negligible | 0.1062 | 0.0196 | 0.2216 | 160 |
| new | actual | 1-3 | B_pm | unresolved | 0.3563 | 0.2805 | 0.4371 | 160 |
| new | actual | 1-3 | C_pm | dominance_positive | 0.0813 | 0.0000 | 0.1977 | 160 |
| new | actual | 1-3 | C_pm | reversal | 0.4562 | 0.3052 | 0.6309 | 160 |
| new | actual | 1-3 | C_pm | negligible | 0.1062 | 0.0196 | 0.2216 | 160 |
| new | actual | 1-3 | C_pm | unresolved | 0.3563 | 0.2805 | 0.4371 | 160 |
| new | actual | 4-10 | B | dominance_positive | 0.3188 | 0.1847 | 0.4721 | 367 |
| new | actual | 4-10 | B | reversal | 0.2507 | 0.2041 | 0.2950 | 367 |
| new | actual | 4-10 | B | negligible | 0.3951 | 0.2472 | 0.5144 | 367 |
| new | actual | 4-10 | B | unresolved | 0.0354 | 0.0114 | 0.0636 | 367 |
| new | actual | 4-10 | C | dominance_positive | 0.3188 | 0.1847 | 0.4721 | 367 |
| new | actual | 4-10 | C | reversal | 0.2507 | 0.2041 | 0.2950 | 367 |
| new | actual | 4-10 | C | negligible | 0.3951 | 0.2472 | 0.5144 | 367 |
| new | actual | 4-10 | C | unresolved | 0.0354 | 0.0114 | 0.0636 | 367 |
| new | actual | 4-10 | B_pm | dominance_positive | 0.2970 | 0.1135 | 0.5205 | 367 |
| new | actual | 4-10 | B_pm | reversal | 0.2125 | 0.1714 | 0.2540 | 367 |
| new | actual | 4-10 | B_pm | negligible | 0.2861 | 0.1816 | 0.3639 | 367 |
| new | actual | 4-10 | B_pm | unresolved | 0.2044 | 0.0564 | 0.3599 | 367 |
| new | actual | 4-10 | C_pm | dominance_positive | 0.2970 | 0.1135 | 0.5205 | 367 |
| new | actual | 4-10 | C_pm | reversal | 0.2125 | 0.1714 | 0.2540 | 367 |
| new | actual | 4-10 | C_pm | negligible | 0.2861 | 0.1816 | 0.3639 | 367 |
| new | actual | 4-10 | C_pm | unresolved | 0.2044 | 0.0564 | 0.3599 | 367 |
| new | actual | 11-16 | B | dominance_positive | 0.5847 | 0.4114 | 0.7416 | 313 |
| new | actual | 11-16 | B | reversal | 0.0799 | 0.0064 | 0.1656 | 313 |
| new | actual | 11-16 | B | negligible | 0.3323 | 0.1154 | 0.5699 | 313 |
| new | actual | 11-16 | B | unresolved | 0.0032 | 0.0000 | 0.0164 | 313 |
| new | actual | 11-16 | C | dominance_positive | 0.5847 | 0.4114 | 0.7416 | 313 |
| new | actual | 11-16 | C | reversal | 0.0799 | 0.0064 | 0.1656 | 313 |
| new | actual | 11-16 | C | negligible | 0.3323 | 0.1154 | 0.5699 | 313 |
| new | actual | 11-16 | C | unresolved | 0.0032 | 0.0000 | 0.0164 | 313 |
| new | actual | 11-16 | B_pm | dominance_positive | 0.5655 | 0.4093 | 0.7048 | 313 |
| new | actual | 11-16 | B_pm | reversal | 0.0735 | 0.0000 | 0.1656 | 313 |
| new | actual | 11-16 | B_pm | negligible | 0.3163 | 0.1084 | 0.5455 | 313 |
| new | actual | 11-16 | B_pm | unresolved | 0.0447 | 0.0164 | 0.0767 | 313 |
| new | actual | 11-16 | C_pm | dominance_positive | 0.5655 | 0.4093 | 0.7048 | 313 |
| new | actual | 11-16 | C_pm | reversal | 0.0735 | 0.0000 | 0.1656 | 313 |
| new | actual | 11-16 | C_pm | negligible | 0.3163 | 0.1084 | 0.5455 | 313 |
| new | actual | 11-16 | C_pm | unresolved | 0.0447 | 0.0164 | 0.0767 | 313 |
| new | actual | 17-30 | B | dominance_positive | 0.7412 | 0.6963 | 0.7934 | 738 |
| new | actual | 17-30 | B | reversal | 0.0528 | 0.0188 | 0.0877 | 738 |
| new | actual | 17-30 | B | negligible | 0.1911 | 0.1606 | 0.2249 | 738 |
| new | actual | 17-30 | B | unresolved | 0.0149 | 0.0026 | 0.0310 | 738 |
| new | actual | 17-30 | C | dominance_positive | 0.7412 | 0.6963 | 0.7934 | 738 |
| new | actual | 17-30 | C | reversal | 0.0528 | 0.0188 | 0.0877 | 738 |
| new | actual | 17-30 | C | negligible | 0.1911 | 0.1606 | 0.2249 | 738 |
| new | actual | 17-30 | C | unresolved | 0.0149 | 0.0026 | 0.0310 | 738 |
| new | actual | 17-30 | B_pm | dominance_positive | 0.7304 | 0.6822 | 0.7892 | 738 |
| new | actual | 17-30 | B_pm | reversal | 0.0325 | 0.0094 | 0.0574 | 738 |
| new | actual | 17-30 | B_pm | negligible | 0.1748 | 0.1417 | 0.2130 | 738 |
| new | actual | 17-30 | B_pm | unresolved | 0.0623 | 0.0212 | 0.1068 | 738 |
| new | actual | 17-30 | C_pm | dominance_positive | 0.7304 | 0.6822 | 0.7892 | 738 |
| new | actual | 17-30 | C_pm | reversal | 0.0325 | 0.0094 | 0.0574 | 738 |
| new | actual | 17-30 | C_pm | negligible | 0.1748 | 0.1417 | 0.2130 | 738 |
| new | actual | 17-30 | C_pm | unresolved | 0.0623 | 0.0212 | 0.1068 | 738 |
| new | own | 1-3 | B | dominance_positive | 0.0938 | 0.0000 | 0.2303 | 160 |
| new | own | 1-3 | B | reversal | 0.6250 | 0.3512 | 0.9155 | 160 |
| new | own | 1-3 | B | negligible | 0.2313 | 0.0541 | 0.4218 | 160 |
| new | own | 1-3 | B | unresolved | 0.0500 | 0.0057 | 0.1132 | 160 |
| new | own | 1-3 | C | dominance_positive | 0.0938 | 0.0000 | 0.2303 | 160 |
| new | own | 1-3 | C | reversal | 0.6250 | 0.3512 | 0.9155 | 160 |
| new | own | 1-3 | C | negligible | 0.2313 | 0.0541 | 0.4218 | 160 |
| new | own | 1-3 | C | unresolved | 0.0500 | 0.0057 | 0.1132 | 160 |
| new | own | 1-3 | B_pm | dominance_positive | 0.1000 | 0.0060 | 0.2264 | 160 |
| new | own | 1-3 | B_pm | reversal | 0.5563 | 0.3395 | 0.7947 | 160 |
| new | own | 1-3 | B_pm | negligible | 0.1812 | 0.0446 | 0.3430 | 160 |
| new | own | 1-3 | B_pm | unresolved | 0.1625 | 0.0926 | 0.2434 | 160 |
| new | own | 1-3 | C_pm | dominance_positive | 0.1000 | 0.0060 | 0.2264 | 160 |
| new | own | 1-3 | C_pm | reversal | 0.5563 | 0.3395 | 0.7947 | 160 |
| new | own | 1-3 | C_pm | negligible | 0.1812 | 0.0446 | 0.3430 | 160 |
| new | own | 1-3 | C_pm | unresolved | 0.1625 | 0.0926 | 0.2434 | 160 |
| new | own | 4-10 | B | dominance_positive | 0.3460 | 0.1827 | 0.5240 | 367 |
| new | own | 4-10 | B | reversal | 0.2044 | 0.1574 | 0.2539 | 367 |
| new | own | 4-10 | B | negligible | 0.4305 | 0.2551 | 0.5852 | 367 |
| new | own | 4-10 | B | unresolved | 0.0191 | 0.0027 | 0.0421 | 367 |
| new | own | 4-10 | C | dominance_positive | 0.3460 | 0.1827 | 0.5240 | 367 |
| new | own | 4-10 | C | reversal | 0.2044 | 0.1574 | 0.2539 | 367 |
| new | own | 4-10 | C | negligible | 0.4305 | 0.2551 | 0.5852 | 367 |
| new | own | 4-10 | C | unresolved | 0.0191 | 0.0027 | 0.0421 | 367 |
| new | own | 4-10 | B_pm | dominance_positive | 0.3733 | 0.1881 | 0.5820 | 367 |
| new | own | 4-10 | B_pm | reversal | 0.1689 | 0.1345 | 0.2082 | 367 |
| new | own | 4-10 | B_pm | negligible | 0.3815 | 0.1864 | 0.5468 | 367 |
| new | own | 4-10 | B_pm | unresolved | 0.0763 | 0.0393 | 0.1155 | 367 |
| new | own | 4-10 | C_pm | dominance_positive | 0.3733 | 0.1881 | 0.5820 | 367 |
| new | own | 4-10 | C_pm | reversal | 0.1689 | 0.1345 | 0.2082 | 367 |
| new | own | 4-10 | C_pm | negligible | 0.3815 | 0.1864 | 0.5468 | 367 |
| new | own | 4-10 | C_pm | unresolved | 0.0763 | 0.0393 | 0.1155 | 367 |
| new | own | 11-16 | B | dominance_positive | 0.8882 | 0.8307 | 0.9375 | 313 |
| new | own | 11-16 | B | reversal | 0.0032 | 0.0000 | 0.0175 | 313 |
| new | own | 11-16 | B | negligible | 0.1086 | 0.0605 | 0.1635 | 313 |
| new | own | 11-16 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 313 |
| new | own | 11-16 | C | dominance_positive | 0.8882 | 0.8307 | 0.9375 | 313 |
| new | own | 11-16 | C | reversal | 0.0032 | 0.0000 | 0.0175 | 313 |
| new | own | 11-16 | C | negligible | 0.1086 | 0.0605 | 0.1635 | 313 |
| new | own | 11-16 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 313 |
| new | own | 11-16 | B_pm | dominance_positive | 0.8882 | 0.8243 | 0.9459 | 313 |
| new | own | 11-16 | B_pm | reversal | 0.0032 | 0.0000 | 0.0175 | 313 |
| new | own | 11-16 | B_pm | negligible | 0.0958 | 0.0484 | 0.1518 | 313 |
| new | own | 11-16 | B_pm | unresolved | 0.0128 | 0.0000 | 0.0446 | 313 |
| new | own | 11-16 | C_pm | dominance_positive | 0.8882 | 0.8243 | 0.9459 | 313 |
| new | own | 11-16 | C_pm | reversal | 0.0032 | 0.0000 | 0.0175 | 313 |
| new | own | 11-16 | C_pm | negligible | 0.0958 | 0.0484 | 0.1518 | 313 |
| new | own | 11-16 | C_pm | unresolved | 0.0128 | 0.0000 | 0.0446 | 313 |
| new | own | 17-30 | B | dominance_positive | 0.9417 | 0.9050 | 0.9728 | 738 |
| new | own | 17-30 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 738 |
| new | own | 17-30 | B | negligible | 0.0583 | 0.0272 | 0.0950 | 738 |
| new | own | 17-30 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 738 |
| new | own | 17-30 | C | dominance_positive | 0.9417 | 0.9050 | 0.9728 | 738 |
| new | own | 17-30 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 738 |
| new | own | 17-30 | C | negligible | 0.0583 | 0.0272 | 0.0950 | 738 |
| new | own | 17-30 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 738 |
| new | own | 17-30 | B_pm | dominance_positive | 0.9336 | 0.8975 | 0.9654 | 738 |
| new | own | 17-30 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 738 |
| new | own | 17-30 | B_pm | negligible | 0.0515 | 0.0229 | 0.0864 | 738 |
| new | own | 17-30 | B_pm | unresolved | 0.0149 | 0.0050 | 0.0274 | 738 |
| new | own | 17-30 | C_pm | dominance_positive | 0.9336 | 0.8975 | 0.9654 | 738 |
| new | own | 17-30 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 738 |
| new | own | 17-30 | C_pm | negligible | 0.0515 | 0.0229 | 0.0864 | 738 |
| new | own | 17-30 | C_pm | unresolved | 0.0149 | 0.0050 | 0.0274 | 738 |

## T5_3_reversal_slot

| rule | portfolio | jstar | count | count_argmin_chat | count_precision_matched | n_reversals | n_reversals_pm |
|---|---|---|---|---|---|---|---|
| old | actual | 1 | 0 | 0 | 0 | 88 | 62 |
| old | actual | 2 | 0 | 0 | 0 | 88 | 62 |
| old | actual | 3 | 0 | 0 | 0 | 88 | 62 |
| old | actual | 4 | 0 | 0 | 0 | 88 | 62 |
| old | actual | 5 | 0 | 0 | 0 | 88 | 62 |
| old | actual | 6 | 0 | 0 | 0 | 88 | 62 |
| old | actual | 7 | 0 | 0 | 0 | 88 | 62 |
| old | actual | 8 | 0 | 0 | 0 | 88 | 62 |
| old | actual | 9 | 2 | 2 | 2 | 88 | 62 |
| old | actual | 10 | 8 | 8 | 4 | 88 | 62 |
| old | actual | 11 | 2 | 2 | 3 | 88 | 62 |
| old | actual | 12 | 1 | 1 | 1 | 88 | 62 |
| old | actual | 13 | 3 | 3 | 3 | 88 | 62 |
| old | actual | 14 | 1 | 1 | 0 | 88 | 62 |
| old | actual | 15 | 2 | 2 | 1 | 88 | 62 |
| old | actual | 16 | 2 | 3 | 4 | 88 | 62 |
| old | actual | 17 | 4 | 4 | 2 | 88 | 62 |
| old | actual | 18 | 4 | 4 | 1 | 88 | 62 |
| old | actual | 19 | 0 | 0 | 1 | 88 | 62 |
| old | actual | 20 | 4 | 4 | 4 | 88 | 62 |
| old | actual | 21 | 1 | 1 | 2 | 88 | 62 |
| old | actual | 22 | 1 | 1 | 0 | 88 | 62 |
| old | actual | 23 | 2 | 2 | 1 | 88 | 62 |
| old | actual | 24 | 6 | 6 | 8 | 88 | 62 |
| old | actual | 25 | 12 | 12 | 10 | 88 | 62 |
| old | actual | 26 | 8 | 8 | 8 | 88 | 62 |
| old | actual | 27 | 17 | 16 | 5 | 88 | 62 |
| old | actual | 28 | 1 | 2 | 0 | 88 | 62 |
| old | actual | 29 | 6 | 6 | 2 | 88 | 62 |
| old | actual | 30 | 1 | 0 | 0 | 88 | 62 |
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
| new | actual | 1 | 0 | 0 | 0 | 249 | 198 |
| new | actual | 2 | 0 | 0 | 0 | 249 | 198 |
| new | actual | 3 | 0 | 0 | 0 | 249 | 198 |
| new | actual | 4 | 0 | 0 | 0 | 249 | 198 |
| new | actual | 5 | 4 | 4 | 2 | 249 | 198 |
| new | actual | 6 | 0 | 0 | 0 | 249 | 198 |
| new | actual | 7 | 1 | 1 | 0 | 249 | 198 |
| new | actual | 8 | 4 | 3 | 1 | 249 | 198 |
| new | actual | 9 | 154 | 155 | 128 | 249 | 198 |
| new | actual | 10 | 1 | 1 | 2 | 249 | 198 |
| new | actual | 11 | 2 | 2 | 1 | 249 | 198 |
| new | actual | 12 | 0 | 0 | 0 | 249 | 198 |
| new | actual | 13 | 0 | 0 | 0 | 249 | 198 |
| new | actual | 14 | 0 | 0 | 0 | 249 | 198 |
| new | actual | 15 | 2 | 2 | 2 | 249 | 198 |
| new | actual | 16 | 1 | 1 | 1 | 249 | 198 |
| new | actual | 17 | 3 | 3 | 2 | 249 | 198 |
| new | actual | 18 | 3 | 3 | 3 | 249 | 198 |
| new | actual | 19 | 2 | 2 | 2 | 249 | 198 |
| new | actual | 20 | 6 | 6 | 4 | 249 | 198 |
| new | actual | 21 | 1 | 1 | 1 | 249 | 198 |
| new | actual | 22 | 2 | 2 | 2 | 249 | 198 |
| new | actual | 23 | 1 | 1 | 1 | 249 | 198 |
| new | actual | 24 | 7 | 7 | 7 | 249 | 198 |
| new | actual | 25 | 12 | 12 | 13 | 249 | 198 |
| new | actual | 26 | 9 | 9 | 11 | 249 | 198 |
| new | actual | 27 | 19 | 19 | 7 | 249 | 198 |
| new | actual | 28 | 4 | 4 | 1 | 249 | 198 |
| new | actual | 29 | 9 | 9 | 5 | 249 | 198 |
| new | actual | 30 | 2 | 2 | 2 | 249 | 198 |
| new | own | 1 | 0 | 0 | 0 | 176 | 152 |
| new | own | 2 | 0 | 0 | 0 | 176 | 152 |
| new | own | 3 | 0 | 0 | 0 | 176 | 152 |
| new | own | 4 | 0 | 0 | 0 | 176 | 152 |
| new | own | 5 | 2 | 2 | 2 | 176 | 152 |
| new | own | 6 | 0 | 0 | 0 | 176 | 152 |
| new | own | 7 | 0 | 0 | 0 | 176 | 152 |
| new | own | 8 | 0 | 0 | 0 | 176 | 152 |
| new | own | 9 | 174 | 174 | 150 | 176 | 152 |
| new | own | 10 | 0 | 0 | 0 | 176 | 152 |
| new | own | 11 | 0 | 0 | 0 | 176 | 152 |
| new | own | 12 | 0 | 0 | 0 | 176 | 152 |
| new | own | 13 | 0 | 0 | 0 | 176 | 152 |
| new | own | 14 | 0 | 0 | 0 | 176 | 152 |
| new | own | 15 | 0 | 0 | 0 | 176 | 152 |
| new | own | 16 | 0 | 0 | 0 | 176 | 152 |
| new | own | 17 | 0 | 0 | 0 | 176 | 152 |
| new | own | 18 | 0 | 0 | 0 | 176 | 152 |
| new | own | 19 | 0 | 0 | 0 | 176 | 152 |
| new | own | 20 | 0 | 0 | 0 | 176 | 152 |
| new | own | 21 | 0 | 0 | 0 | 176 | 152 |
| new | own | 22 | 0 | 0 | 0 | 176 | 152 |
| new | own | 23 | 0 | 0 | 0 | 176 | 152 |
| new | own | 24 | 0 | 0 | 0 | 176 | 152 |
| new | own | 25 | 0 | 0 | 0 | 176 | 152 |
| new | own | 26 | 0 | 0 | 0 | 176 | 152 |
| new | own | 27 | 0 | 0 | 0 | 176 | 152 |
| new | own | 28 | 0 | 0 | 0 | 176 | 152 |
| new | own | 29 | 0 | 0 | 0 | 176 | 152 |
| new | own | 30 | 0 | 0 | 0 | 176 | 152 |

## F5_1_profiles

720 rows in `F5_1_profiles.csv`.

## T5_curves_and_T5_6_delta

| rule | portfolio | band | curve | n | mean | q25 | median | q75 | q90 | share_sig_pos | pos_lo99 | pos_hi99 | share_sig_neg | neg_lo99 | neg_hi99 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| old | actual | all | linear | 1578 | 0.0171 | 0.0020 | 0.0112 | 0.0304 | 0.0418 | 0.7079 | 0.6806 | 0.7420 | 0.0330 | 0.0142 | 0.0511 |
| old | actual | all | concave | 1578 | 0.0163 | 0.0012 | 0.0099 | 0.0303 | 0.0416 | 0.6451 | 0.6208 | 0.6769 | 0.0342 | 0.0168 | 0.0516 |
| old | actual | all | convex | 1578 | 0.0137 | 0.0022 | 0.0089 | 0.0225 | 0.0343 | 0.7250 | 0.6980 | 0.7559 | 0.0292 | 0.0107 | 0.0474 |
| old | actual | all | top3_stress | 1578 | 0.0048 | 0.0000 | 0.0008 | 0.0071 | 0.0162 | 0.3828 | 0.3608 | 0.4052 | 0.0025 | 0.0000 | 0.0075 |
| old | actual | 1-3 | linear | 160 | 0.0027 | 0.0018 | 0.0026 | 0.0045 | 0.0054 | 0.4562 | 0.2075 | 0.7351 | 0.0250 | 0.0000 | 0.0702 |
| old | actual | 1-3 | concave | 160 | 0.0013 | 0.0010 | 0.0015 | 0.0024 | 0.0030 | 0.1375 | 0.0578 | 0.2434 | 0.0250 | 0.0000 | 0.0702 |
| old | actual | 1-3 | convex | 160 | 0.0048 | 0.0031 | 0.0044 | 0.0069 | 0.0088 | 0.8000 | 0.6105 | 0.9712 | 0.0187 | 0.0000 | 0.0533 |
| old | actual | 1-3 | top3_stress | 160 | 0.0037 | 0.0004 | 0.0021 | 0.0056 | 0.0087 | 0.3750 | 0.2683 | 0.5105 | 0.0063 | 0.0000 | 0.0340 |
| old | actual | 4-10 | linear | 367 | 0.0111 | 0.0035 | 0.0072 | 0.0204 | 0.0293 | 0.8011 | 0.7202 | 0.8928 | 0.0354 | 0.0050 | 0.0818 |
| old | actual | 4-10 | concave | 367 | 0.0080 | 0.0018 | 0.0042 | 0.0143 | 0.0265 | 0.6512 | 0.5245 | 0.8049 | 0.0436 | 0.0051 | 0.0934 |
| old | actual | 4-10 | convex | 367 | 0.0149 | 0.0057 | 0.0114 | 0.0234 | 0.0368 | 0.8501 | 0.7826 | 0.9209 | 0.0191 | 0.0000 | 0.0476 |
| old | actual | 4-10 | top3_stress | 367 | 0.0134 | 0.0073 | 0.0128 | 0.0199 | 0.0259 | 0.8583 | 0.7602 | 0.9515 | 0.0054 | 0.0000 | 0.0243 |
| old | actual | 11-16 | linear | 313 | 0.0143 | 0.0000 | 0.0124 | 0.0248 | 0.0366 | 0.6965 | 0.5228 | 0.8528 | 0.0703 | 0.0000 | 0.1656 |
| old | actual | 11-16 | concave | 313 | 0.0091 | 0.0000 | 0.0094 | 0.0161 | 0.0279 | 0.6933 | 0.5228 | 0.8462 | 0.0735 | 0.0000 | 0.1656 |
| old | actual | 11-16 | convex | 313 | 0.0165 | 0.0000 | 0.0139 | 0.0284 | 0.0351 | 0.7029 | 0.5336 | 0.8528 | 0.0703 | 0.0000 | 0.1656 |
| old | actual | 11-16 | top3_stress | 313 | 0.0057 | 0.0000 | 0.0045 | 0.0077 | 0.0155 | 0.6134 | 0.5208 | 0.7029 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 17-30 | linear | 738 | 0.0244 | 0.0009 | 0.0240 | 0.0384 | 0.0488 | 0.7209 | 0.6806 | 0.7660 | 0.0176 | 0.0056 | 0.0322 |
| old | actual | 17-30 | concave | 738 | 0.0268 | 0.0018 | 0.0295 | 0.0378 | 0.0567 | 0.7317 | 0.6892 | 0.7768 | 0.0149 | 0.0041 | 0.0288 |
| old | actual | 17-30 | convex | 738 | 0.0139 | 0.0008 | 0.0095 | 0.0223 | 0.0338 | 0.6558 | 0.6008 | 0.7125 | 0.0190 | 0.0071 | 0.0323 |
| old | actual | 17-30 | top3_stress | 738 | 0.0005 | 0.0000 | 0.0000 | 0.0004 | 0.0017 | 0.0501 | 0.0084 | 0.0994 | 0.0014 | 0.0000 | 0.0066 |
| old | own | all | linear | 1578 | 0.0235 | 0.0072 | 0.0222 | 0.0354 | 0.0446 | 0.8701 | 0.8304 | 0.9121 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | concave | 1578 | 0.0210 | 0.0041 | 0.0177 | 0.0331 | 0.0426 | 0.8048 | 0.7669 | 0.8453 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | convex | 1578 | 0.0193 | 0.0065 | 0.0179 | 0.0290 | 0.0377 | 0.8853 | 0.8352 | 0.9316 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | top3_stress | 1578 | 0.0058 | 0.0000 | 0.0022 | 0.0084 | 0.0186 | 0.4582 | 0.4342 | 0.4846 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | linear | 160 | 0.0030 | 0.0019 | 0.0026 | 0.0040 | 0.0052 | 0.3750 | 0.1706 | 0.6268 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | concave | 160 | 0.0016 | 0.0010 | 0.0014 | 0.0022 | 0.0028 | 0.0938 | 0.0321 | 0.1882 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | convex | 160 | 0.0050 | 0.0032 | 0.0043 | 0.0068 | 0.0088 | 0.7750 | 0.5537 | 0.9712 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | top3_stress | 160 | 0.0037 | 0.0004 | 0.0017 | 0.0057 | 0.0087 | 0.3688 | 0.2397 | 0.5302 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | linear | 367 | 0.0117 | 0.0050 | 0.0079 | 0.0188 | 0.0257 | 0.8801 | 0.7728 | 0.9816 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | concave | 367 | 0.0068 | 0.0028 | 0.0045 | 0.0109 | 0.0153 | 0.7248 | 0.5817 | 0.8795 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | convex | 367 | 0.0176 | 0.0082 | 0.0124 | 0.0281 | 0.0375 | 0.9482 | 0.8831 | 0.9897 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | top3_stress | 367 | 0.0152 | 0.0090 | 0.0143 | 0.0211 | 0.0263 | 0.9455 | 0.8764 | 0.9896 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | linear | 313 | 0.0259 | 0.0174 | 0.0246 | 0.0325 | 0.0401 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | concave | 313 | 0.0179 | 0.0115 | 0.0160 | 0.0235 | 0.0299 | 0.9840 | 0.9551 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | convex | 313 | 0.0286 | 0.0200 | 0.0283 | 0.0344 | 0.0419 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | top3_stress | 313 | 0.0080 | 0.0038 | 0.0057 | 0.0092 | 0.0187 | 0.8243 | 0.7500 | 0.8904 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | linear | 738 | 0.0327 | 0.0212 | 0.0341 | 0.0421 | 0.0506 | 0.9173 | 0.8912 | 0.9403 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | concave | 738 | 0.0336 | 0.0277 | 0.0335 | 0.0402 | 0.0543 | 0.9228 | 0.8940 | 0.9481 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | convex | 738 | 0.0194 | 0.0057 | 0.0189 | 0.0273 | 0.0378 | 0.8293 | 0.7825 | 0.8760 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | top3_stress | 738 | 0.0007 | 0.0000 | 0.0000 | 0.0007 | 0.0025 | 0.0799 | 0.0125 | 0.1564 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | all | linear | 1578 | 0.0173 | 0.0000 | 0.0065 | 0.0338 | 0.0481 | 0.5507 | 0.5242 | 0.5819 | 0.0437 | 0.0315 | 0.0553 |
| new | actual | all | concave | 1578 | 0.0170 | 0.0000 | 0.0069 | 0.0320 | 0.0475 | 0.5754 | 0.5432 | 0.6044 | 0.0336 | 0.0127 | 0.0538 |
| new | actual | all | convex | 1578 | 0.0131 | 0.0000 | 0.0029 | 0.0216 | 0.0408 | 0.5038 | 0.4690 | 0.5437 | 0.0817 | 0.0655 | 0.1004 |
| new | actual | all | top3_stress | 1578 | 0.0032 | 0.0000 | 0.0000 | 0.0050 | 0.0144 | 0.3067 | 0.2538 | 0.3553 | 0.0970 | 0.0702 | 0.1280 |
| new | actual | 1-3 | linear | 160 | -0.0006 | -0.0014 | 0.0000 | 0.0007 | 0.0022 | 0.1000 | 0.0000 | 0.2294 | 0.1375 | 0.0053 | 0.3309 |
| new | actual | 1-3 | concave | 160 | 0.0007 | -0.0007 | 0.0000 | 0.0016 | 0.0054 | 0.2000 | 0.0000 | 0.4309 | 0.0312 | 0.0000 | 0.0736 |
| new | actual | 1-3 | convex | 160 | -0.0025 | -0.0035 | -0.0014 | 0.0000 | 0.0005 | 0.0563 | 0.0000 | 0.1429 | 0.3438 | 0.1404 | 0.5901 |
| new | actual | 1-3 | top3_stress | 160 | -0.0052 | -0.0079 | -0.0032 | 0.0000 | 0.0000 | 0.0312 | 0.0000 | 0.0843 | 0.5625 | 0.3311 | 0.8250 |
| new | actual | 4-10 | linear | 367 | 0.0021 | 0.0000 | 0.0006 | 0.0033 | 0.0090 | 0.2807 | 0.1324 | 0.4525 | 0.0436 | 0.0180 | 0.0746 |
| new | actual | 4-10 | concave | 367 | 0.0025 | 0.0000 | 0.0006 | 0.0049 | 0.0091 | 0.3488 | 0.2015 | 0.5095 | 0.0463 | 0.0223 | 0.0760 |
| new | actual | 4-10 | convex | 367 | 0.0016 | -0.0005 | 0.0000 | 0.0019 | 0.0104 | 0.2343 | 0.0860 | 0.4134 | 0.1199 | 0.0799 | 0.1622 |
| new | actual | 4-10 | top3_stress | 367 | -0.0000 | -0.0011 | 0.0000 | 0.0015 | 0.0092 | 0.2044 | 0.0615 | 0.3861 | 0.1689 | 0.1320 | 0.2084 |
| new | actual | 11-16 | linear | 313 | 0.0149 | 0.0000 | 0.0104 | 0.0288 | 0.0418 | 0.5719 | 0.4082 | 0.7252 | 0.0703 | 0.0000 | 0.1656 |
| new | actual | 11-16 | concave | 313 | 0.0092 | 0.0000 | 0.0068 | 0.0227 | 0.0333 | 0.5559 | 0.3946 | 0.7093 | 0.0703 | 0.0000 | 0.1656 |
| new | actual | 11-16 | convex | 313 | 0.0183 | 0.0000 | 0.0115 | 0.0323 | 0.0449 | 0.5719 | 0.4082 | 0.7252 | 0.0703 | 0.0000 | 0.1656 |
| new | actual | 11-16 | top3_stress | 313 | 0.0102 | 0.0000 | 0.0078 | 0.0158 | 0.0241 | 0.5687 | 0.4082 | 0.7191 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 17-30 | linear | 738 | 0.0297 | 0.0068 | 0.0291 | 0.0439 | 0.0582 | 0.7737 | 0.7339 | 0.8207 | 0.0122 | 0.0015 | 0.0260 |
| new | actual | 17-30 | concave | 738 | 0.0310 | 0.0083 | 0.0315 | 0.0424 | 0.0617 | 0.7778 | 0.7404 | 0.8209 | 0.0122 | 0.0015 | 0.0260 |
| new | actual | 17-30 | convex | 738 | 0.0201 | 0.0020 | 0.0134 | 0.0317 | 0.0488 | 0.7060 | 0.6575 | 0.7637 | 0.0108 | 0.0000 | 0.0260 |
| new | actual | 17-30 | top3_stress | 738 | 0.0036 | 0.0000 | 0.0002 | 0.0041 | 0.0119 | 0.3062 | 0.2070 | 0.3989 | 0.0014 | 0.0000 | 0.0066 |
| new | own | all | linear | 1578 | 0.0232 | 0.0001 | 0.0167 | 0.0402 | 0.0546 | 0.6553 | 0.6114 | 0.7046 | 0.0374 | 0.0215 | 0.0569 |
| new | own | all | concave | 1578 | 0.0208 | 0.0001 | 0.0193 | 0.0354 | 0.0473 | 0.6420 | 0.5958 | 0.6936 | 0.0089 | 0.0033 | 0.0149 |
| new | own | all | convex | 1578 | 0.0189 | 0.0000 | 0.0102 | 0.0309 | 0.0516 | 0.6204 | 0.5608 | 0.6854 | 0.0672 | 0.0475 | 0.0888 |
| new | own | all | top3_stress | 1578 | 0.0052 | 0.0000 | 0.0004 | 0.0095 | 0.0202 | 0.3916 | 0.3375 | 0.4386 | 0.0925 | 0.0706 | 0.1166 |
| new | own | 1-3 | linear | 160 | -0.0015 | -0.0023 | -0.0009 | -0.0001 | 0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.1812 | 0.0861 | 0.3072 |
| new | own | 1-3 | concave | 160 | -0.0008 | -0.0011 | -0.0004 | -0.0001 | 0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.0312 | 0.0000 | 0.0702 |
| new | own | 1-3 | convex | 160 | -0.0029 | -0.0044 | -0.0016 | -0.0002 | 0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.3625 | 0.2267 | 0.5350 |
| new | own | 1-3 | top3_stress | 160 | -0.0052 | -0.0077 | -0.0030 | -0.0004 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.5250 | 0.3395 | 0.7329 |
| new | own | 4-10 | linear | 367 | 0.0015 | -0.0003 | 0.0001 | 0.0032 | 0.0084 | 0.2534 | 0.0992 | 0.4266 | 0.0817 | 0.0492 | 0.1143 |
| new | own | 4-10 | concave | 367 | 0.0010 | -0.0001 | 0.0000 | 0.0019 | 0.0050 | 0.2153 | 0.0620 | 0.3971 | 0.0245 | 0.0063 | 0.0448 |
| new | own | 4-10 | convex | 367 | 0.0019 | -0.0005 | 0.0001 | 0.0046 | 0.0120 | 0.2752 | 0.1250 | 0.4489 | 0.1308 | 0.0973 | 0.1624 |
| new | own | 4-10 | top3_stress | 367 | 0.0007 | -0.0010 | 0.0000 | 0.0042 | 0.0111 | 0.2698 | 0.1250 | 0.4335 | 0.1689 | 0.1345 | 0.2082 |
| new | own | 11-16 | linear | 313 | 0.0273 | 0.0082 | 0.0236 | 0.0404 | 0.0551 | 0.8435 | 0.7866 | 0.8952 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | concave | 313 | 0.0183 | 0.0049 | 0.0152 | 0.0279 | 0.0361 | 0.8083 | 0.7530 | 0.8642 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | convex | 313 | 0.0323 | 0.0103 | 0.0288 | 0.0444 | 0.0635 | 0.8498 | 0.7891 | 0.9035 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | top3_stress | 313 | 0.0154 | 0.0054 | 0.0130 | 0.0211 | 0.0303 | 0.8147 | 0.7601 | 0.8675 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | linear | 738 | 0.0375 | 0.0213 | 0.0375 | 0.0476 | 0.0624 | 0.9173 | 0.8912 | 0.9403 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | concave | 738 | 0.0364 | 0.0292 | 0.0351 | 0.0451 | 0.0574 | 0.9228 | 0.8940 | 0.9481 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | convex | 738 | 0.0264 | 0.0059 | 0.0202 | 0.0362 | 0.0602 | 0.8293 | 0.7825 | 0.8760 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | top3_stress | 738 | 0.0053 | 0.0000 | 0.0004 | 0.0057 | 0.0190 | 0.3577 | 0.2153 | 0.4859 | 0.0000 | 0.0000 | 0.0000 |
| delta | actual | all | linear | 1578 | 0.0002 | -0.0038 | 0.0000 | 0.0031 | 0.0116 | 0.2687 | 0.2067 | 0.3262 | 0.2858 | 0.2229 | 0.3529 |
| delta | actual | all | concave | 1578 | 0.0007 | -0.0019 | 0.0000 | 0.0026 | 0.0104 | 0.2541 | 0.1880 | 0.3115 | 0.2224 | 0.1714 | 0.2806 |
| delta | actual | all | convex | 1578 | -0.0006 | -0.0070 | 0.0000 | 0.0041 | 0.0140 | 0.2826 | 0.2232 | 0.3360 | 0.3384 | 0.3083 | 0.3718 |
| delta | actual | all | top3_stress | 1578 | -0.0017 | -0.0067 | 0.0000 | 0.0017 | 0.0102 | 0.2351 | 0.1554 | 0.3145 | 0.3042 | 0.2520 | 0.3615 |
| delta | actual | 1-3 | linear | 160 | -0.0032 | -0.0052 | -0.0022 | -0.0011 | -0.0004 | 0.0375 | 0.0000 | 0.0976 | 0.4500 | 0.0449 | 0.9080 |
| delta | actual | 1-3 | concave | 160 | -0.0006 | -0.0025 | -0.0009 | 0.0007 | 0.0031 | 0.1313 | 0.0000 | 0.3114 | 0.2437 | 0.0000 | 0.5960 |
| delta | actual | 1-3 | convex | 160 | -0.0073 | -0.0102 | -0.0054 | -0.0027 | -0.0017 | 0.0187 | 0.0000 | 0.0542 | 0.7562 | 0.5155 | 0.9781 |
| delta | actual | 1-3 | top3_stress | 160 | -0.0088 | -0.0137 | -0.0050 | -0.0006 | -0.0000 | 0.0125 | 0.0000 | 0.0516 | 0.5625 | 0.3248 | 0.8289 |
| delta | actual | 4-10 | linear | 367 | -0.0089 | -0.0157 | -0.0068 | -0.0026 | 0.0000 | 0.0381 | 0.0000 | 0.0951 | 0.7330 | 0.6260 | 0.8492 |
| delta | actual | 4-10 | concave | 367 | -0.0056 | -0.0102 | -0.0039 | 0.0000 | 0.0024 | 0.0926 | 0.0510 | 0.1445 | 0.5640 | 0.4592 | 0.6855 |
| delta | actual | 4-10 | convex | 367 | -0.0133 | -0.0199 | -0.0124 | -0.0062 | 0.0000 | 0.0245 | 0.0000 | 0.0674 | 0.8447 | 0.7870 | 0.9044 |
| delta | actual | 4-10 | top3_stress | 367 | -0.0134 | -0.0179 | -0.0128 | -0.0073 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.8610 | 0.7663 | 0.9515 |
| delta | actual | 11-16 | linear | 313 | 0.0006 | -0.0043 | 0.0000 | 0.0071 | 0.0168 | 0.4026 | 0.2012 | 0.6045 | 0.3003 | 0.2375 | 0.3689 |
| delta | actual | 11-16 | concave | 313 | 0.0001 | -0.0032 | 0.0000 | 0.0057 | 0.0154 | 0.3323 | 0.1753 | 0.4957 | 0.2684 | 0.2126 | 0.3247 |
| delta | actual | 11-16 | convex | 313 | 0.0018 | -0.0037 | 0.0000 | 0.0092 | 0.0204 | 0.4313 | 0.2437 | 0.6215 | 0.2971 | 0.2251 | 0.3707 |
| delta | actual | 11-16 | top3_stress | 313 | 0.0045 | -0.0000 | 0.0000 | 0.0104 | 0.0185 | 0.4824 | 0.3063 | 0.6581 | 0.2141 | 0.1696 | 0.2594 |
| delta | actual | 17-30 | linear | 738 | 0.0053 | 0.0000 | 0.0002 | 0.0065 | 0.0162 | 0.3767 | 0.3049 | 0.4360 | 0.0217 | 0.0028 | 0.0437 |
| delta | actual | 17-30 | concave | 738 | 0.0043 | 0.0000 | 0.0001 | 0.0040 | 0.0151 | 0.3279 | 0.2631 | 0.3755 | 0.0285 | 0.0097 | 0.0461 |
| delta | actual | 17-30 | convex | 738 | 0.0062 | 0.0000 | 0.0004 | 0.0081 | 0.0180 | 0.4051 | 0.3362 | 0.4617 | 0.0136 | 0.0000 | 0.0318 |
| delta | actual | 17-30 | top3_stress | 738 | 0.0031 | 0.0000 | 0.0001 | 0.0037 | 0.0104 | 0.2954 | 0.1923 | 0.3948 | 0.0095 | 0.0000 | 0.0263 |
| delta | own | all | linear | 1578 | -0.0003 | -0.0062 | 0.0000 | 0.0033 | 0.0126 | 0.2731 | 0.2073 | 0.3341 | 0.3631 | 0.3043 | 0.4270 |
| delta | own | all | concave | 1578 | -0.0002 | -0.0036 | -0.0000 | 0.0016 | 0.0075 | 0.2186 | 0.1761 | 0.2586 | 0.2953 | 0.2350 | 0.3604 |
| delta | own | all | convex | 1578 | -0.0004 | -0.0098 | 0.0000 | 0.0055 | 0.0185 | 0.3010 | 0.2385 | 0.3571 | 0.3853 | 0.3331 | 0.4373 |
| delta | own | all | top3_stress | 1578 | -0.0007 | -0.0082 | 0.0000 | 0.0043 | 0.0158 | 0.2921 | 0.2013 | 0.3786 | 0.3384 | 0.2785 | 0.4018 |
| delta | own | 1-3 | linear | 160 | -0.0045 | -0.0062 | -0.0035 | -0.0018 | -0.0014 | 0.0000 | 0.0000 | 0.0000 | 0.5875 | 0.3419 | 0.8589 |
| delta | own | 1-3 | concave | 160 | -0.0024 | -0.0032 | -0.0018 | -0.0010 | -0.0007 | 0.0000 | 0.0000 | 0.0000 | 0.3000 | 0.1543 | 0.4932 |
| delta | own | 1-3 | convex | 160 | -0.0079 | -0.0110 | -0.0060 | -0.0032 | -0.0024 | 0.0000 | 0.0000 | 0.0000 | 0.8125 | 0.6226 | 0.9800 |
| delta | own | 1-3 | top3_stress | 160 | -0.0089 | -0.0134 | -0.0045 | -0.0009 | -0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.6062 | 0.3512 | 0.8839 |
| delta | own | 4-10 | linear | 367 | -0.0101 | -0.0142 | -0.0085 | -0.0057 | -0.0032 | 0.0000 | 0.0000 | 0.0000 | 0.9128 | 0.8329 | 0.9816 |
| delta | own | 4-10 | concave | 367 | -0.0058 | -0.0080 | -0.0047 | -0.0032 | -0.0017 | 0.0000 | 0.0000 | 0.0000 | 0.7847 | 0.6533 | 0.9252 |
| delta | own | 4-10 | convex | 367 | -0.0156 | -0.0219 | -0.0137 | -0.0093 | -0.0053 | 0.0000 | 0.0000 | 0.0000 | 0.9482 | 0.8831 | 0.9897 |
| delta | own | 4-10 | top3_stress | 367 | -0.0145 | -0.0184 | -0.0133 | -0.0089 | -0.0052 | 0.0000 | 0.0000 | 0.0000 | 0.9482 | 0.8831 | 0.9897 |
| delta | own | 11-16 | linear | 313 | 0.0013 | -0.0086 | 0.0012 | 0.0095 | 0.0180 | 0.4888 | 0.3437 | 0.6289 | 0.4313 | 0.3062 | 0.5578 |
| delta | own | 11-16 | concave | 313 | 0.0004 | -0.0053 | 0.0002 | 0.0053 | 0.0098 | 0.3770 | 0.3060 | 0.4519 | 0.3866 | 0.2610 | 0.5119 |
| delta | own | 11-16 | convex | 313 | 0.0037 | -0.0100 | 0.0043 | 0.0161 | 0.0287 | 0.5367 | 0.3958 | 0.6744 | 0.3994 | 0.2727 | 0.5247 |
| delta | own | 11-16 | top3_stress | 313 | 0.0074 | -0.0036 | 0.0078 | 0.0164 | 0.0236 | 0.6613 | 0.5317 | 0.7874 | 0.2652 | 0.1698 | 0.3636 |
| delta | own | 17-30 | linear | 738 | 0.0048 | 0.0000 | 0.0004 | 0.0066 | 0.0164 | 0.3767 | 0.2835 | 0.4557 | 0.0122 | 0.0013 | 0.0263 |
| delta | own | 17-30 | concave | 738 | 0.0028 | 0.0000 | 0.0002 | 0.0040 | 0.0096 | 0.3076 | 0.2271 | 0.3762 | 0.0122 | 0.0013 | 0.0263 |
| delta | own | 17-30 | convex | 738 | 0.0070 | 0.0000 | 0.0008 | 0.0093 | 0.0242 | 0.4160 | 0.3310 | 0.4848 | 0.0068 | 0.0000 | 0.0185 |
| delta | own | 17-30 | top3_stress | 738 | 0.0046 | 0.0000 | 0.0004 | 0.0050 | 0.0165 | 0.3442 | 0.1975 | 0.4786 | 0.0081 | 0.0000 | 0.0263 |

## H1

| n_team_games | share_neg_new | share_neg_old | diff_new_minus_old | diff_lo99 | diff_hi99 | n_new_reversals | crossing_share | crossing_lo99 | crossing_hi99 | supported |
|---|---|---|---|---|---|---|---|---|---|---|
| 214 | 0.2710 | 0.0000 | 0.2710 | 0.1636 | 0.3961 | 156 | 1.0000 | 1.0000 | 1.0000 | True |

## T5_attr_portfolio_effect

| rule | band | n | mean | q25 | median | q75 | q90 | share_nonzero |
|---|---|---|---|---|---|---|---|---|
| old | all | 1578 | -0.0063 | -0.0083 | 0.0000 | 0.0000 | 0.0012 | 0.3758 |
| old | 1-3 | 160 | -0.0003 | 0.0000 | 0.0000 | 0.0000 | 0.0002 | 0.0437 |
| old | 4-10 | 367 | -0.0006 | -0.0000 | 0.0000 | 0.0013 | 0.0093 | 0.3787 |
| old | 11-16 | 313 | -0.0116 | -0.0238 | -0.0000 | 0.0000 | 0.0001 | 0.4824 |
| old | 17-30 | 738 | -0.0083 | -0.0138 | 0.0000 | 0.0000 | 0.0000 | 0.4011 |
| new | all | 1578 | -0.0059 | -0.0048 | 0.0000 | 0.0000 | 0.0035 | 0.3828 |
| new | 1-3 | 160 | 0.0010 | 0.0000 | 0.0000 | 0.0014 | 0.0052 | 0.2188 |
| new | 4-10 | 367 | 0.0006 | -0.0000 | 0.0000 | 0.0025 | 0.0065 | 0.3243 |
| new | 11-16 | 313 | -0.0124 | -0.0114 | 0.0000 | 0.0000 | 0.0005 | 0.4185 |
| new | 17-30 | 738 | -0.0078 | -0.0136 | 0.0000 | 0.0000 | 0.0000 | 0.4322 |
| delta | all | 1578 | 0.0005 | -0.0000 | 0.0000 | 0.0008 | 0.0079 | 0.3035 |
| delta | 1-3 | 160 | 0.0013 | 0.0000 | 0.0000 | 0.0015 | 0.0047 | 0.2062 |
| delta | 4-10 | 367 | 0.0012 | -0.0002 | 0.0000 | 0.0034 | 0.0101 | 0.4142 |
| delta | 11-16 | 313 | -0.0007 | -0.0000 | 0.0000 | 0.0032 | 0.0152 | 0.4313 |
| delta | 17-30 | 738 | 0.0005 | 0.0000 | 0.0000 | 0.0001 | 0.0059 | 0.2154 |

## T5_7_rollover

| rule | portfolio | band | curve | rho | measure | n | mean | q25 | median | q75 | q90 | share_sign_flip | vbar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| old | actual | all | - | 0.0000 | M | 1578 | 0.0032 | -0.0000 | 0.0000 | 0.0000 | 0.0130 |  |  |
| old | actual | all | linear | 0.0000 | tau | 1578 | 0.0171 | 0.0020 | 0.0112 | 0.0304 | 0.0418 | 0.0000 | 0.5000 |
| old | actual | all | linear | 0.5000 | tau | 1578 | 0.0163 | 0.0019 | 0.0104 | 0.0286 | 0.0407 | 0.0063 | 0.5000 |
| old | actual | all | linear | 0.8000 | tau | 1578 | 0.0158 | 0.0021 | 0.0098 | 0.0267 | 0.0400 | 0.0234 | 0.5000 |
| old | actual | all | concave | 0.0000 | tau | 1578 | 0.0163 | 0.0012 | 0.0099 | 0.0303 | 0.0416 | 0.0000 | 0.6599 |
| old | actual | all | concave | 0.5000 | tau | 1578 | 0.0153 | 0.0012 | 0.0087 | 0.0286 | 0.0398 | 0.0108 | 0.6599 |
| old | actual | all | concave | 0.8000 | tau | 1578 | 0.0146 | 0.0011 | 0.0072 | 0.0278 | 0.0381 | 0.0184 | 0.6599 |
| old | actual | all | convex | 0.0000 | tau | 1578 | 0.0137 | 0.0022 | 0.0089 | 0.0225 | 0.0343 | 0.0000 | 0.3391 |
| old | actual | all | convex | 0.5000 | tau | 1578 | 0.0132 | 0.0024 | 0.0087 | 0.0211 | 0.0335 | 0.0165 | 0.3391 |
| old | actual | all | convex | 0.8000 | tau | 1578 | 0.0129 | 0.0022 | 0.0084 | 0.0206 | 0.0331 | 0.0196 | 0.3391 |
| old | actual | all | top3_stress | 0.0000 | tau | 1578 | 0.0048 | 0.0000 | 0.0008 | 0.0071 | 0.0162 | 0.0000 | 0.1000 |
| old | actual | all | top3_stress | 0.5000 | tau | 1578 | 0.0047 | 0.0000 | 0.0006 | 0.0071 | 0.0158 | 0.1483 | 0.1000 |
| old | actual | all | top3_stress | 0.8000 | tau | 1578 | 0.0046 | 0.0000 | 0.0007 | 0.0073 | 0.0159 | 0.1496 | 0.1000 |
| old | actual | 1-3 | - | 0.0000 | M | 160 | -0.0002 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | actual | 1-3 | linear | 0.0000 | tau | 160 | 0.0027 | 0.0018 | 0.0026 | 0.0045 | 0.0054 | 0.0000 | 0.5000 |
| old | actual | 1-3 | linear | 0.5000 | tau | 160 | 0.0027 | 0.0019 | 0.0026 | 0.0045 | 0.0054 | 0.0000 | 0.5000 |
| old | actual | 1-3 | linear | 0.8000 | tau | 160 | 0.0027 | 0.0019 | 0.0026 | 0.0045 | 0.0054 | 0.0000 | 0.5000 |
| old | actual | 1-3 | concave | 0.0000 | tau | 160 | 0.0013 | 0.0010 | 0.0015 | 0.0024 | 0.0030 | 0.0000 | 0.6599 |
| old | actual | 1-3 | concave | 0.5000 | tau | 160 | 0.0014 | 0.0010 | 0.0015 | 0.0024 | 0.0030 | 0.0125 | 0.6599 |
| old | actual | 1-3 | concave | 0.8000 | tau | 160 | 0.0014 | 0.0010 | 0.0015 | 0.0024 | 0.0030 | 0.0187 | 0.6599 |
| old | actual | 1-3 | convex | 0.0000 | tau | 160 | 0.0048 | 0.0031 | 0.0044 | 0.0069 | 0.0088 | 0.0000 | 0.3391 |
| old | actual | 1-3 | convex | 0.5000 | tau | 160 | 0.0048 | 0.0031 | 0.0045 | 0.0069 | 0.0088 | 0.0000 | 0.3391 |
| old | actual | 1-3 | convex | 0.8000 | tau | 160 | 0.0048 | 0.0031 | 0.0045 | 0.0069 | 0.0088 | 0.0063 | 0.3391 |
| old | actual | 1-3 | top3_stress | 0.0000 | tau | 160 | 0.0037 | 0.0004 | 0.0021 | 0.0056 | 0.0087 | 0.0000 | 0.1000 |
| old | actual | 1-3 | top3_stress | 0.5000 | tau | 160 | 0.0037 | 0.0004 | 0.0021 | 0.0056 | 0.0087 | 0.0000 | 0.1000 |
| old | actual | 1-3 | top3_stress | 0.8000 | tau | 160 | 0.0037 | 0.0004 | 0.0021 | 0.0056 | 0.0088 | 0.0000 | 0.1000 |
| old | actual | 4-10 | - | 0.0000 | M | 367 | 0.0036 | -0.0000 | 0.0000 | 0.0001 | 0.0233 |  |  |
| old | actual | 4-10 | linear | 0.0000 | tau | 367 | 0.0111 | 0.0035 | 0.0072 | 0.0204 | 0.0293 | 0.0000 | 0.5000 |
| old | actual | 4-10 | linear | 0.5000 | tau | 367 | 0.0102 | 0.0035 | 0.0072 | 0.0186 | 0.0258 | 0.0082 | 0.5000 |
| old | actual | 4-10 | linear | 0.8000 | tau | 367 | 0.0096 | 0.0035 | 0.0072 | 0.0150 | 0.0253 | 0.0163 | 0.5000 |
| old | actual | 4-10 | concave | 0.0000 | tau | 367 | 0.0080 | 0.0018 | 0.0042 | 0.0143 | 0.0265 | 0.0000 | 0.6599 |
| old | actual | 4-10 | concave | 0.5000 | tau | 367 | 0.0068 | 0.0019 | 0.0041 | 0.0126 | 0.0187 | 0.0218 | 0.6599 |
| old | actual | 4-10 | concave | 0.8000 | tau | 367 | 0.0061 | 0.0019 | 0.0041 | 0.0117 | 0.0161 | 0.0327 | 0.6599 |
| old | actual | 4-10 | convex | 0.0000 | tau | 367 | 0.0149 | 0.0057 | 0.0114 | 0.0234 | 0.0368 | 0.0000 | 0.3391 |
| old | actual | 4-10 | convex | 0.5000 | tau | 367 | 0.0143 | 0.0058 | 0.0114 | 0.0208 | 0.0361 | 0.0027 | 0.3391 |
| old | actual | 4-10 | convex | 0.8000 | tau | 367 | 0.0139 | 0.0059 | 0.0110 | 0.0191 | 0.0344 | 0.0027 | 0.3391 |
| old | actual | 4-10 | top3_stress | 0.0000 | tau | 367 | 0.0134 | 0.0073 | 0.0128 | 0.0199 | 0.0259 | 0.0000 | 0.1000 |
| old | actual | 4-10 | top3_stress | 0.5000 | tau | 367 | 0.0132 | 0.0073 | 0.0124 | 0.0196 | 0.0256 | 0.0054 | 0.1000 |
| old | actual | 4-10 | top3_stress | 0.8000 | tau | 367 | 0.0131 | 0.0073 | 0.0122 | 0.0195 | 0.0254 | 0.0054 | 0.1000 |
| old | actual | 11-16 | - | 0.0000 | M | 313 | -0.0021 | -0.0000 | 0.0000 | 0.0027 | 0.0091 |  |  |
| old | actual | 11-16 | linear | 0.0000 | tau | 313 | 0.0143 | 0.0000 | 0.0124 | 0.0248 | 0.0366 | 0.0000 | 0.5000 |
| old | actual | 11-16 | linear | 0.5000 | tau | 313 | 0.0148 | 0.0000 | 0.0104 | 0.0244 | 0.0366 | 0.0032 | 0.5000 |
| old | actual | 11-16 | linear | 0.8000 | tau | 313 | 0.0151 | 0.0024 | 0.0115 | 0.0241 | 0.0366 | 0.0735 | 0.5000 |
| old | actual | 11-16 | concave | 0.0000 | tau | 313 | 0.0091 | 0.0000 | 0.0094 | 0.0161 | 0.0279 | 0.0000 | 0.6599 |
| old | actual | 11-16 | concave | 0.5000 | tau | 313 | 0.0098 | 0.0000 | 0.0080 | 0.0161 | 0.0273 | 0.0032 | 0.6599 |
| old | actual | 11-16 | concave | 0.8000 | tau | 313 | 0.0102 | 0.0000 | 0.0064 | 0.0158 | 0.0273 | 0.0128 | 0.6599 |
| old | actual | 11-16 | convex | 0.0000 | tau | 313 | 0.0165 | 0.0000 | 0.0139 | 0.0284 | 0.0351 | 0.0000 | 0.3391 |
| old | actual | 11-16 | convex | 0.5000 | tau | 313 | 0.0169 | 0.0032 | 0.0140 | 0.0282 | 0.0351 | 0.0703 | 0.3391 |
| old | actual | 11-16 | convex | 0.8000 | tau | 313 | 0.0171 | 0.0029 | 0.0170 | 0.0283 | 0.0351 | 0.0703 | 0.3391 |
| old | actual | 11-16 | top3_stress | 0.0000 | tau | 313 | 0.0057 | 0.0000 | 0.0045 | 0.0077 | 0.0155 | 0.0000 | 0.1000 |
| old | actual | 11-16 | top3_stress | 0.5000 | tau | 313 | 0.0058 | 0.0017 | 0.0046 | 0.0076 | 0.0132 | 0.1022 | 0.1000 |
| old | actual | 11-16 | top3_stress | 0.8000 | tau | 313 | 0.0059 | 0.0017 | 0.0049 | 0.0079 | 0.0131 | 0.1054 | 0.1000 |
| old | actual | 17-30 | - | 0.0000 | M | 738 | 0.0059 | -0.0000 | 0.0000 | 0.0000 | 0.0160 |  |  |
| old | actual | 17-30 | linear | 0.0000 | tau | 738 | 0.0244 | 0.0009 | 0.0240 | 0.0384 | 0.0488 | 0.0000 | 0.5000 |
| old | actual | 17-30 | linear | 0.5000 | tau | 738 | 0.0230 | 0.0011 | 0.0218 | 0.0373 | 0.0466 | 0.0081 | 0.5000 |
| old | actual | 17-30 | linear | 0.8000 | tau | 738 | 0.0221 | 0.0009 | 0.0205 | 0.0369 | 0.0460 | 0.0108 | 0.5000 |
| old | actual | 17-30 | concave | 0.0000 | tau | 738 | 0.0268 | 0.0018 | 0.0295 | 0.0378 | 0.0567 | 0.0000 | 0.6599 |
| old | actual | 17-30 | concave | 0.5000 | tau | 738 | 0.0248 | 0.0014 | 0.0283 | 0.0365 | 0.0513 | 0.0081 | 0.6599 |
| old | actual | 17-30 | concave | 0.8000 | tau | 738 | 0.0236 | 0.0011 | 0.0274 | 0.0356 | 0.0482 | 0.0136 | 0.6599 |
| old | actual | 17-30 | convex | 0.0000 | tau | 738 | 0.0139 | 0.0008 | 0.0095 | 0.0223 | 0.0338 | 0.0000 | 0.3391 |
| old | actual | 17-30 | convex | 0.5000 | tau | 738 | 0.0129 | 0.0008 | 0.0083 | 0.0210 | 0.0309 | 0.0041 | 0.3391 |
| old | actual | 17-30 | convex | 0.8000 | tau | 738 | 0.0123 | 0.0006 | 0.0064 | 0.0206 | 0.0306 | 0.0095 | 0.3391 |
| old | actual | 17-30 | top3_stress | 0.0000 | tau | 738 | 0.0005 | 0.0000 | 0.0000 | 0.0004 | 0.0017 | 0.0000 | 0.1000 |
| old | actual | 17-30 | top3_stress | 0.5000 | tau | 738 | 0.0002 | 0.0000 | 0.0000 | 0.0002 | 0.0011 | 0.2710 | 0.1000 |
| old | actual | 17-30 | top3_stress | 0.8000 | tau | 738 | 0.0000 | 0.0000 | 0.0000 | 0.0002 | 0.0012 | 0.2724 | 0.1000 |
| old | own | all | - | 0.0000 | M | 1578 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | all | linear | 0.0000 | tau | 1578 | 0.0235 | 0.0072 | 0.0222 | 0.0354 | 0.0446 | 0.0000 | 0.5000 |
| old | own | all | linear | 0.5000 | tau | 1578 | 0.0235 | 0.0072 | 0.0222 | 0.0354 | 0.0446 | 0.0000 | 0.5000 |
| old | own | all | linear | 0.8000 | tau | 1578 | 0.0235 | 0.0072 | 0.0222 | 0.0354 | 0.0446 | 0.0000 | 0.5000 |
| old | own | all | concave | 0.0000 | tau | 1578 | 0.0210 | 0.0041 | 0.0177 | 0.0331 | 0.0426 | 0.0000 | 0.6599 |
| old | own | all | concave | 0.5000 | tau | 1578 | 0.0210 | 0.0041 | 0.0177 | 0.0331 | 0.0426 | 0.0000 | 0.6599 |
| old | own | all | concave | 0.8000 | tau | 1578 | 0.0210 | 0.0041 | 0.0177 | 0.0331 | 0.0426 | 0.0000 | 0.6599 |
| old | own | all | convex | 0.0000 | tau | 1578 | 0.0193 | 0.0065 | 0.0179 | 0.0290 | 0.0377 | 0.0000 | 0.3391 |
| old | own | all | convex | 0.5000 | tau | 1578 | 0.0193 | 0.0065 | 0.0179 | 0.0290 | 0.0377 | 0.0000 | 0.3391 |
| old | own | all | convex | 0.8000 | tau | 1578 | 0.0193 | 0.0065 | 0.0179 | 0.0290 | 0.0377 | 0.0000 | 0.3391 |
| old | own | all | top3_stress | 0.0000 | tau | 1578 | 0.0058 | 0.0000 | 0.0022 | 0.0084 | 0.0186 | 0.0000 | 0.1000 |
| old | own | all | top3_stress | 0.5000 | tau | 1578 | 0.0058 | 0.0000 | 0.0022 | 0.0084 | 0.0186 | 0.0570 | 0.1000 |
| old | own | all | top3_stress | 0.8000 | tau | 1578 | 0.0058 | 0.0000 | 0.0022 | 0.0084 | 0.0186 | 0.0570 | 0.1000 |
| old | own | 1-3 | - | 0.0000 | M | 160 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 1-3 | linear | 0.0000 | tau | 160 | 0.0030 | 0.0019 | 0.0026 | 0.0040 | 0.0052 | 0.0000 | 0.5000 |
| old | own | 1-3 | linear | 0.5000 | tau | 160 | 0.0030 | 0.0019 | 0.0026 | 0.0040 | 0.0052 | 0.0000 | 0.5000 |
| old | own | 1-3 | linear | 0.8000 | tau | 160 | 0.0030 | 0.0019 | 0.0026 | 0.0040 | 0.0052 | 0.0000 | 0.5000 |
| old | own | 1-3 | concave | 0.0000 | tau | 160 | 0.0016 | 0.0010 | 0.0014 | 0.0022 | 0.0028 | 0.0000 | 0.6599 |
| old | own | 1-3 | concave | 0.5000 | tau | 160 | 0.0016 | 0.0010 | 0.0014 | 0.0022 | 0.0028 | 0.0000 | 0.6599 |
| old | own | 1-3 | concave | 0.8000 | tau | 160 | 0.0016 | 0.0010 | 0.0014 | 0.0022 | 0.0028 | 0.0000 | 0.6599 |
| old | own | 1-3 | convex | 0.0000 | tau | 160 | 0.0050 | 0.0032 | 0.0043 | 0.0068 | 0.0088 | 0.0000 | 0.3391 |
| old | own | 1-3 | convex | 0.5000 | tau | 160 | 0.0050 | 0.0032 | 0.0043 | 0.0068 | 0.0088 | 0.0000 | 0.3391 |
| old | own | 1-3 | convex | 0.8000 | tau | 160 | 0.0050 | 0.0032 | 0.0043 | 0.0068 | 0.0088 | 0.0000 | 0.3391 |
| old | own | 1-3 | top3_stress | 0.0000 | tau | 160 | 0.0037 | 0.0004 | 0.0017 | 0.0057 | 0.0087 | 0.0000 | 0.1000 |
| old | own | 1-3 | top3_stress | 0.5000 | tau | 160 | 0.0037 | 0.0004 | 0.0017 | 0.0057 | 0.0087 | 0.0000 | 0.1000 |
| old | own | 1-3 | top3_stress | 0.8000 | tau | 160 | 0.0037 | 0.0004 | 0.0017 | 0.0057 | 0.0087 | 0.0000 | 0.1000 |
| old | own | 4-10 | - | 0.0000 | M | 367 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 4-10 | linear | 0.0000 | tau | 367 | 0.0117 | 0.0050 | 0.0079 | 0.0188 | 0.0257 | 0.0000 | 0.5000 |
| old | own | 4-10 | linear | 0.5000 | tau | 367 | 0.0117 | 0.0050 | 0.0079 | 0.0188 | 0.0257 | 0.0000 | 0.5000 |
| old | own | 4-10 | linear | 0.8000 | tau | 367 | 0.0117 | 0.0050 | 0.0079 | 0.0188 | 0.0257 | 0.0000 | 0.5000 |
| old | own | 4-10 | concave | 0.0000 | tau | 367 | 0.0068 | 0.0028 | 0.0045 | 0.0109 | 0.0153 | 0.0000 | 0.6599 |
| old | own | 4-10 | concave | 0.5000 | tau | 367 | 0.0068 | 0.0028 | 0.0045 | 0.0109 | 0.0153 | 0.0000 | 0.6599 |
| old | own | 4-10 | concave | 0.8000 | tau | 367 | 0.0068 | 0.0028 | 0.0045 | 0.0109 | 0.0153 | 0.0000 | 0.6599 |
| old | own | 4-10 | convex | 0.0000 | tau | 367 | 0.0176 | 0.0082 | 0.0124 | 0.0281 | 0.0375 | 0.0000 | 0.3391 |
| old | own | 4-10 | convex | 0.5000 | tau | 367 | 0.0176 | 0.0082 | 0.0124 | 0.0281 | 0.0375 | 0.0000 | 0.3391 |
| old | own | 4-10 | convex | 0.8000 | tau | 367 | 0.0176 | 0.0082 | 0.0124 | 0.0281 | 0.0375 | 0.0000 | 0.3391 |
| old | own | 4-10 | top3_stress | 0.0000 | tau | 367 | 0.0152 | 0.0090 | 0.0143 | 0.0211 | 0.0263 | 0.0000 | 0.1000 |
| old | own | 4-10 | top3_stress | 0.5000 | tau | 367 | 0.0152 | 0.0090 | 0.0143 | 0.0211 | 0.0263 | 0.0000 | 0.1000 |
| old | own | 4-10 | top3_stress | 0.8000 | tau | 367 | 0.0152 | 0.0090 | 0.0143 | 0.0211 | 0.0263 | 0.0000 | 0.1000 |
| old | own | 11-16 | - | 0.0000 | M | 313 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 11-16 | linear | 0.0000 | tau | 313 | 0.0259 | 0.0174 | 0.0246 | 0.0325 | 0.0401 | 0.0000 | 0.5000 |
| old | own | 11-16 | linear | 0.5000 | tau | 313 | 0.0259 | 0.0174 | 0.0246 | 0.0325 | 0.0401 | 0.0000 | 0.5000 |
| old | own | 11-16 | linear | 0.8000 | tau | 313 | 0.0259 | 0.0174 | 0.0246 | 0.0325 | 0.0401 | 0.0000 | 0.5000 |
| old | own | 11-16 | concave | 0.0000 | tau | 313 | 0.0179 | 0.0115 | 0.0160 | 0.0235 | 0.0299 | 0.0000 | 0.6599 |
| old | own | 11-16 | concave | 0.5000 | tau | 313 | 0.0179 | 0.0115 | 0.0160 | 0.0235 | 0.0299 | 0.0000 | 0.6599 |
| old | own | 11-16 | concave | 0.8000 | tau | 313 | 0.0179 | 0.0115 | 0.0160 | 0.0235 | 0.0299 | 0.0000 | 0.6599 |
| old | own | 11-16 | convex | 0.0000 | tau | 313 | 0.0286 | 0.0200 | 0.0283 | 0.0344 | 0.0419 | 0.0000 | 0.3391 |
| old | own | 11-16 | convex | 0.5000 | tau | 313 | 0.0286 | 0.0200 | 0.0283 | 0.0344 | 0.0419 | 0.0000 | 0.3391 |
| old | own | 11-16 | convex | 0.8000 | tau | 313 | 0.0286 | 0.0200 | 0.0283 | 0.0344 | 0.0419 | 0.0000 | 0.3391 |
| old | own | 11-16 | top3_stress | 0.0000 | tau | 313 | 0.0080 | 0.0038 | 0.0057 | 0.0092 | 0.0187 | 0.0000 | 0.1000 |
| old | own | 11-16 | top3_stress | 0.5000 | tau | 313 | 0.0080 | 0.0038 | 0.0057 | 0.0092 | 0.0187 | 0.0000 | 0.1000 |
| old | own | 11-16 | top3_stress | 0.8000 | tau | 313 | 0.0080 | 0.0038 | 0.0057 | 0.0092 | 0.0187 | 0.0000 | 0.1000 |
| old | own | 17-30 | - | 0.0000 | M | 738 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 17-30 | linear | 0.0000 | tau | 738 | 0.0327 | 0.0212 | 0.0341 | 0.0421 | 0.0506 | 0.0000 | 0.5000 |
| old | own | 17-30 | linear | 0.5000 | tau | 738 | 0.0327 | 0.0212 | 0.0341 | 0.0421 | 0.0506 | 0.0000 | 0.5000 |
| old | own | 17-30 | linear | 0.8000 | tau | 738 | 0.0327 | 0.0212 | 0.0341 | 0.0421 | 0.0506 | 0.0000 | 0.5000 |
| old | own | 17-30 | concave | 0.0000 | tau | 738 | 0.0336 | 0.0277 | 0.0335 | 0.0402 | 0.0543 | 0.0000 | 0.6599 |
| old | own | 17-30 | concave | 0.5000 | tau | 738 | 0.0336 | 0.0277 | 0.0335 | 0.0402 | 0.0543 | 0.0000 | 0.6599 |
| old | own | 17-30 | concave | 0.8000 | tau | 738 | 0.0336 | 0.0277 | 0.0335 | 0.0402 | 0.0543 | 0.0000 | 0.6599 |
| old | own | 17-30 | convex | 0.0000 | tau | 738 | 0.0194 | 0.0057 | 0.0189 | 0.0273 | 0.0378 | 0.0000 | 0.3391 |
| old | own | 17-30 | convex | 0.5000 | tau | 738 | 0.0194 | 0.0057 | 0.0189 | 0.0273 | 0.0378 | 0.0000 | 0.3391 |
| old | own | 17-30 | convex | 0.8000 | tau | 738 | 0.0194 | 0.0057 | 0.0189 | 0.0273 | 0.0378 | 0.0000 | 0.3391 |
| old | own | 17-30 | top3_stress | 0.0000 | tau | 738 | 0.0007 | 0.0000 | 0.0000 | 0.0007 | 0.0025 | 0.0000 | 0.1000 |
| old | own | 17-30 | top3_stress | 0.5000 | tau | 738 | 0.0007 | 0.0000 | 0.0000 | 0.0007 | 0.0025 | 0.1220 | 0.1000 |
| old | own | 17-30 | top3_stress | 0.8000 | tau | 738 | 0.0007 | 0.0000 | 0.0000 | 0.0007 | 0.0025 | 0.1220 | 0.1000 |
| new | actual | all | - | 0.0000 | M | 1578 | 0.0045 | -0.0000 | 0.0000 | 0.0008 | 0.0154 |  |  |
| new | actual | all | linear | 0.0000 | tau | 1578 | 0.0173 | 0.0000 | 0.0065 | 0.0338 | 0.0481 | 0.0000 | 0.5000 |
| new | actual | all | linear | 0.5000 | tau | 1578 | 0.0162 | 0.0000 | 0.0054 | 0.0321 | 0.0456 | 0.0627 | 0.5000 |
| new | actual | all | linear | 0.8000 | tau | 1578 | 0.0155 | 0.0000 | 0.0054 | 0.0297 | 0.0441 | 0.0856 | 0.5000 |
| new | actual | all | concave | 0.0000 | tau | 1578 | 0.0170 | 0.0000 | 0.0069 | 0.0320 | 0.0475 | 0.0000 | 0.6599 |
| new | actual | all | concave | 0.5000 | tau | 1578 | 0.0155 | 0.0000 | 0.0047 | 0.0314 | 0.0432 | 0.0044 | 0.6599 |
| new | actual | all | concave | 0.8000 | tau | 1578 | 0.0146 | 0.0000 | 0.0038 | 0.0302 | 0.0406 | 0.0177 | 0.6599 |
| new | actual | all | convex | 0.0000 | tau | 1578 | 0.0131 | 0.0000 | 0.0029 | 0.0216 | 0.0408 | 0.0000 | 0.3391 |
| new | actual | all | convex | 0.5000 | tau | 1578 | 0.0124 | 0.0000 | 0.0033 | 0.0207 | 0.0385 | 0.0222 | 0.3391 |
| new | actual | all | convex | 0.8000 | tau | 1578 | 0.0119 | 0.0000 | 0.0034 | 0.0200 | 0.0372 | 0.0285 | 0.3391 |
| new | actual | all | top3_stress | 0.0000 | tau | 1578 | 0.0032 | 0.0000 | 0.0000 | 0.0050 | 0.0144 | 0.0000 | 0.1000 |
| new | actual | all | top3_stress | 0.5000 | tau | 1578 | 0.0030 | 0.0000 | 0.0001 | 0.0054 | 0.0137 | 0.0843 | 0.1000 |
| new | actual | all | top3_stress | 0.8000 | tau | 1578 | 0.0028 | 0.0000 | 0.0001 | 0.0054 | 0.0133 | 0.0849 | 0.1000 |
| new | actual | 1-3 | - | 0.0000 | M | 160 | 0.0023 | -0.0000 | 0.0000 | 0.0019 | 0.0084 |  |  |
| new | actual | 1-3 | linear | 0.0000 | tau | 160 | -0.0006 | -0.0014 | 0.0000 | 0.0007 | 0.0022 | 0.0000 | 0.5000 |
| new | actual | 1-3 | linear | 0.5000 | tau | 160 | -0.0011 | -0.0016 | -0.0005 | 0.0001 | 0.0005 | 0.1562 | 0.5000 |
| new | actual | 1-3 | linear | 0.8000 | tau | 160 | -0.0015 | -0.0020 | -0.0008 | 0.0000 | 0.0002 | 0.1688 | 0.5000 |
| new | actual | 1-3 | concave | 0.0000 | tau | 160 | 0.0007 | -0.0007 | 0.0000 | 0.0016 | 0.0054 | 0.0000 | 0.6599 |
| new | actual | 1-3 | concave | 0.5000 | tau | 160 | -0.0000 | -0.0007 | 0.0000 | 0.0008 | 0.0024 | 0.0000 | 0.6599 |
| new | actual | 1-3 | concave | 0.8000 | tau | 160 | -0.0005 | -0.0007 | -0.0000 | 0.0001 | 0.0005 | 0.0375 | 0.6599 |
| new | actual | 1-3 | convex | 0.0000 | tau | 160 | -0.0025 | -0.0035 | -0.0014 | 0.0000 | 0.0005 | 0.0000 | 0.3391 |
| new | actual | 1-3 | convex | 0.5000 | tau | 160 | -0.0029 | -0.0042 | -0.0017 | 0.0000 | 0.0001 | 0.0312 | 0.3391 |
| new | actual | 1-3 | convex | 0.8000 | tau | 160 | -0.0031 | -0.0047 | -0.0017 | 0.0000 | 0.0001 | 0.0625 | 0.3391 |
| new | actual | 1-3 | top3_stress | 0.0000 | tau | 160 | -0.0052 | -0.0079 | -0.0032 | 0.0000 | 0.0000 | 0.0000 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.5000 | tau | 160 | -0.0053 | -0.0080 | -0.0032 | -0.0000 | 0.0000 | 0.0437 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.8000 | tau | 160 | -0.0053 | -0.0080 | -0.0032 | -0.0000 | 0.0000 | 0.0437 | 0.1000 |
| new | actual | 4-10 | - | 0.0000 | M | 367 | 0.0026 | -0.0000 | 0.0000 | 0.0042 | 0.0129 |  |  |
| new | actual | 4-10 | linear | 0.0000 | tau | 367 | 0.0021 | 0.0000 | 0.0006 | 0.0033 | 0.0090 | 0.0000 | 0.5000 |
| new | actual | 4-10 | linear | 0.5000 | tau | 367 | 0.0015 | -0.0001 | 0.0000 | 0.0025 | 0.0079 | 0.1962 | 0.5000 |
| new | actual | 4-10 | linear | 0.8000 | tau | 367 | 0.0011 | -0.0002 | 0.0000 | 0.0027 | 0.0078 | 0.2207 | 0.5000 |
| new | actual | 4-10 | concave | 0.0000 | tau | 367 | 0.0025 | 0.0000 | 0.0006 | 0.0049 | 0.0091 | 0.0000 | 0.6599 |
| new | actual | 4-10 | concave | 0.5000 | tau | 367 | 0.0016 | 0.0000 | 0.0004 | 0.0031 | 0.0062 | 0.0191 | 0.6599 |
| new | actual | 4-10 | concave | 0.8000 | tau | 367 | 0.0011 | 0.0000 | 0.0001 | 0.0019 | 0.0054 | 0.0545 | 0.6599 |
| new | actual | 4-10 | convex | 0.0000 | tau | 367 | 0.0016 | -0.0005 | 0.0000 | 0.0019 | 0.0104 | 0.0000 | 0.3391 |
| new | actual | 4-10 | convex | 0.5000 | tau | 367 | 0.0011 | -0.0006 | 0.0000 | 0.0024 | 0.0099 | 0.0027 | 0.3391 |
| new | actual | 4-10 | convex | 0.8000 | tau | 367 | 0.0009 | -0.0006 | 0.0000 | 0.0023 | 0.0099 | 0.0136 | 0.3391 |
| new | actual | 4-10 | top3_stress | 0.0000 | tau | 367 | -0.0000 | -0.0011 | 0.0000 | 0.0015 | 0.0092 | 0.0000 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.5000 | tau | 367 | -0.0002 | -0.0011 | 0.0000 | 0.0015 | 0.0089 | 0.0327 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.8000 | tau | 367 | -0.0003 | -0.0011 | 0.0000 | 0.0016 | 0.0089 | 0.0354 | 0.1000 |
| new | actual | 11-16 | - | 0.0000 | M | 313 | -0.0022 | -0.0000 | 0.0000 | 0.0004 | 0.0196 |  |  |
| new | actual | 11-16 | linear | 0.0000 | tau | 313 | 0.0149 | 0.0000 | 0.0104 | 0.0288 | 0.0418 | 0.0000 | 0.5000 |
| new | actual | 11-16 | linear | 0.5000 | tau | 313 | 0.0154 | 0.0000 | 0.0088 | 0.0263 | 0.0417 | 0.0000 | 0.5000 |
| new | actual | 11-16 | linear | 0.8000 | tau | 313 | 0.0158 | 0.0000 | 0.0090 | 0.0238 | 0.0411 | 0.0703 | 0.5000 |
| new | actual | 11-16 | concave | 0.0000 | tau | 313 | 0.0092 | 0.0000 | 0.0068 | 0.0227 | 0.0333 | 0.0000 | 0.6599 |
| new | actual | 11-16 | concave | 0.5000 | tau | 313 | 0.0099 | 0.0000 | 0.0063 | 0.0188 | 0.0301 | 0.0000 | 0.6599 |
| new | actual | 11-16 | concave | 0.8000 | tau | 313 | 0.0104 | 0.0000 | 0.0057 | 0.0172 | 0.0295 | 0.0000 | 0.6599 |
| new | actual | 11-16 | convex | 0.0000 | tau | 313 | 0.0183 | 0.0000 | 0.0115 | 0.0323 | 0.0449 | 0.0000 | 0.3391 |
| new | actual | 11-16 | convex | 0.5000 | tau | 313 | 0.0187 | 0.0000 | 0.0110 | 0.0304 | 0.0447 | 0.0703 | 0.3391 |
| new | actual | 11-16 | convex | 0.8000 | tau | 313 | 0.0189 | 0.0000 | 0.0131 | 0.0300 | 0.0440 | 0.0703 | 0.3391 |
| new | actual | 11-16 | top3_stress | 0.0000 | tau | 313 | 0.0102 | 0.0000 | 0.0078 | 0.0158 | 0.0241 | 0.0000 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.5000 | tau | 313 | 0.0103 | 0.0000 | 0.0079 | 0.0153 | 0.0230 | 0.0703 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.8000 | tau | 313 | 0.0104 | 0.0000 | 0.0091 | 0.0151 | 0.0230 | 0.0703 | 0.1000 |
| new | actual | 17-30 | - | 0.0000 | M | 738 | 0.0087 | -0.0000 | 0.0000 | 0.0000 | 0.0512 |  |  |
| new | actual | 17-30 | linear | 0.0000 | tau | 738 | 0.0297 | 0.0068 | 0.0291 | 0.0439 | 0.0582 | 0.0000 | 0.5000 |
| new | actual | 17-30 | linear | 0.5000 | tau | 738 | 0.0275 | 0.0058 | 0.0267 | 0.0420 | 0.0524 | 0.0027 | 0.5000 |
| new | actual | 17-30 | linear | 0.8000 | tau | 738 | 0.0262 | 0.0051 | 0.0248 | 0.0409 | 0.0505 | 0.0068 | 0.5000 |
| new | actual | 17-30 | concave | 0.0000 | tau | 738 | 0.0310 | 0.0083 | 0.0315 | 0.0424 | 0.0617 | 0.0000 | 0.6599 |
| new | actual | 17-30 | concave | 0.5000 | tau | 738 | 0.0282 | 0.0057 | 0.0312 | 0.0397 | 0.0551 | 0.0000 | 0.6599 |
| new | actual | 17-30 | concave | 0.8000 | tau | 738 | 0.0264 | 0.0044 | 0.0299 | 0.0377 | 0.0513 | 0.0027 | 0.6599 |
| new | actual | 17-30 | convex | 0.0000 | tau | 738 | 0.0201 | 0.0020 | 0.0134 | 0.0317 | 0.0488 | 0.0000 | 0.3391 |
| new | actual | 17-30 | convex | 0.5000 | tau | 738 | 0.0186 | 0.0020 | 0.0128 | 0.0302 | 0.0433 | 0.0095 | 0.3391 |
| new | actual | 17-30 | convex | 0.8000 | tau | 738 | 0.0177 | 0.0020 | 0.0119 | 0.0285 | 0.0418 | 0.0108 | 0.3391 |
| new | actual | 17-30 | top3_stress | 0.0000 | tau | 738 | 0.0036 | 0.0000 | 0.0002 | 0.0041 | 0.0119 | 0.0000 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.5000 | tau | 738 | 0.0032 | 0.0000 | 0.0002 | 0.0041 | 0.0112 | 0.1247 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.8000 | tau | 738 | 0.0029 | 0.0000 | 0.0002 | 0.0040 | 0.0107 | 0.1247 | 0.1000 |
| new | own | all | - | 0.0000 | M | 1578 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | all | linear | 0.0000 | tau | 1578 | 0.0232 | 0.0001 | 0.0167 | 0.0402 | 0.0546 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.5000 | tau | 1578 | 0.0232 | 0.0001 | 0.0167 | 0.0402 | 0.0546 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.8000 | tau | 1578 | 0.0232 | 0.0001 | 0.0167 | 0.0402 | 0.0546 | 0.0000 | 0.5000 |
| new | own | all | concave | 0.0000 | tau | 1578 | 0.0208 | 0.0001 | 0.0193 | 0.0354 | 0.0473 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.5000 | tau | 1578 | 0.0208 | 0.0001 | 0.0193 | 0.0354 | 0.0473 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.8000 | tau | 1578 | 0.0208 | 0.0001 | 0.0193 | 0.0354 | 0.0473 | 0.0000 | 0.6599 |
| new | own | all | convex | 0.0000 | tau | 1578 | 0.0189 | 0.0000 | 0.0102 | 0.0309 | 0.0516 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.5000 | tau | 1578 | 0.0189 | 0.0000 | 0.0102 | 0.0309 | 0.0516 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.8000 | tau | 1578 | 0.0189 | 0.0000 | 0.0102 | 0.0309 | 0.0516 | 0.0000 | 0.3391 |
| new | own | all | top3_stress | 0.0000 | tau | 1578 | 0.0052 | 0.0000 | 0.0004 | 0.0095 | 0.0202 | 0.0000 | 0.1000 |
| new | own | all | top3_stress | 0.5000 | tau | 1578 | 0.0052 | 0.0000 | 0.0004 | 0.0095 | 0.0202 | 0.0748 | 0.1000 |
| new | own | all | top3_stress | 0.8000 | tau | 1578 | 0.0052 | 0.0000 | 0.0004 | 0.0095 | 0.0202 | 0.0748 | 0.1000 |
| new | own | 1-3 | - | 0.0000 | M | 160 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 1-3 | linear | 0.0000 | tau | 160 | -0.0015 | -0.0023 | -0.0009 | -0.0001 | 0.0001 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.5000 | tau | 160 | -0.0015 | -0.0023 | -0.0009 | -0.0001 | 0.0001 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.8000 | tau | 160 | -0.0015 | -0.0023 | -0.0009 | -0.0001 | 0.0001 | 0.0000 | 0.5000 |
| new | own | 1-3 | concave | 0.0000 | tau | 160 | -0.0008 | -0.0011 | -0.0004 | -0.0001 | 0.0001 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.5000 | tau | 160 | -0.0008 | -0.0011 | -0.0004 | -0.0001 | 0.0001 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.8000 | tau | 160 | -0.0008 | -0.0011 | -0.0004 | -0.0001 | 0.0001 | 0.0000 | 0.6599 |
| new | own | 1-3 | convex | 0.0000 | tau | 160 | -0.0029 | -0.0044 | -0.0016 | -0.0002 | 0.0001 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.5000 | tau | 160 | -0.0029 | -0.0044 | -0.0016 | -0.0002 | 0.0001 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.8000 | tau | 160 | -0.0029 | -0.0044 | -0.0016 | -0.0002 | 0.0001 | 0.0000 | 0.3391 |
| new | own | 1-3 | top3_stress | 0.0000 | tau | 160 | -0.0052 | -0.0077 | -0.0030 | -0.0004 | 0.0000 | 0.0000 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.5000 | tau | 160 | -0.0052 | -0.0077 | -0.0030 | -0.0004 | 0.0000 | 0.0437 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.8000 | tau | 160 | -0.0052 | -0.0077 | -0.0030 | -0.0004 | 0.0000 | 0.0437 | 0.1000 |
| new | own | 4-10 | - | 0.0000 | M | 367 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 4-10 | linear | 0.0000 | tau | 367 | 0.0015 | -0.0003 | 0.0001 | 0.0032 | 0.0084 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.5000 | tau | 367 | 0.0015 | -0.0003 | 0.0001 | 0.0032 | 0.0084 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.8000 | tau | 367 | 0.0015 | -0.0003 | 0.0001 | 0.0032 | 0.0084 | 0.0000 | 0.5000 |
| new | own | 4-10 | concave | 0.0000 | tau | 367 | 0.0010 | -0.0001 | 0.0000 | 0.0019 | 0.0050 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.5000 | tau | 367 | 0.0010 | -0.0001 | 0.0000 | 0.0019 | 0.0050 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.8000 | tau | 367 | 0.0010 | -0.0001 | 0.0000 | 0.0019 | 0.0050 | 0.0000 | 0.6599 |
| new | own | 4-10 | convex | 0.0000 | tau | 367 | 0.0019 | -0.0005 | 0.0001 | 0.0046 | 0.0120 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.5000 | tau | 367 | 0.0019 | -0.0005 | 0.0001 | 0.0046 | 0.0120 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.8000 | tau | 367 | 0.0019 | -0.0005 | 0.0001 | 0.0046 | 0.0120 | 0.0000 | 0.3391 |
| new | own | 4-10 | top3_stress | 0.0000 | tau | 367 | 0.0007 | -0.0010 | 0.0000 | 0.0042 | 0.0111 | 0.0000 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.5000 | tau | 367 | 0.0007 | -0.0010 | 0.0000 | 0.0042 | 0.0111 | 0.0109 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.8000 | tau | 367 | 0.0007 | -0.0010 | 0.0000 | 0.0042 | 0.0111 | 0.0109 | 0.1000 |
| new | own | 11-16 | - | 0.0000 | M | 313 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 11-16 | linear | 0.0000 | tau | 313 | 0.0273 | 0.0082 | 0.0236 | 0.0404 | 0.0551 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.5000 | tau | 313 | 0.0273 | 0.0082 | 0.0236 | 0.0404 | 0.0551 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.8000 | tau | 313 | 0.0273 | 0.0082 | 0.0236 | 0.0404 | 0.0551 | 0.0000 | 0.5000 |
| new | own | 11-16 | concave | 0.0000 | tau | 313 | 0.0183 | 0.0049 | 0.0152 | 0.0279 | 0.0361 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.5000 | tau | 313 | 0.0183 | 0.0049 | 0.0152 | 0.0279 | 0.0361 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.8000 | tau | 313 | 0.0183 | 0.0049 | 0.0152 | 0.0279 | 0.0361 | 0.0000 | 0.6599 |
| new | own | 11-16 | convex | 0.0000 | tau | 313 | 0.0323 | 0.0103 | 0.0288 | 0.0444 | 0.0635 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.5000 | tau | 313 | 0.0323 | 0.0103 | 0.0288 | 0.0444 | 0.0635 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.8000 | tau | 313 | 0.0323 | 0.0103 | 0.0288 | 0.0444 | 0.0635 | 0.0000 | 0.3391 |
| new | own | 11-16 | top3_stress | 0.0000 | tau | 313 | 0.0154 | 0.0054 | 0.0130 | 0.0211 | 0.0303 | 0.0000 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.5000 | tau | 313 | 0.0154 | 0.0054 | 0.0130 | 0.0211 | 0.0303 | 0.0351 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.8000 | tau | 313 | 0.0154 | 0.0054 | 0.0130 | 0.0211 | 0.0303 | 0.0351 | 0.1000 |
| new | own | 17-30 | - | 0.0000 | M | 738 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 17-30 | linear | 0.0000 | tau | 738 | 0.0375 | 0.0213 | 0.0375 | 0.0476 | 0.0624 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.5000 | tau | 738 | 0.0375 | 0.0213 | 0.0375 | 0.0476 | 0.0624 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.8000 | tau | 738 | 0.0375 | 0.0213 | 0.0375 | 0.0476 | 0.0624 | 0.0000 | 0.5000 |
| new | own | 17-30 | concave | 0.0000 | tau | 738 | 0.0364 | 0.0292 | 0.0351 | 0.0451 | 0.0574 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.5000 | tau | 738 | 0.0364 | 0.0292 | 0.0351 | 0.0451 | 0.0574 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.8000 | tau | 738 | 0.0364 | 0.0292 | 0.0351 | 0.0451 | 0.0574 | 0.0000 | 0.6599 |
| new | own | 17-30 | convex | 0.0000 | tau | 738 | 0.0264 | 0.0059 | 0.0202 | 0.0362 | 0.0602 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.5000 | tau | 738 | 0.0264 | 0.0059 | 0.0202 | 0.0362 | 0.0602 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.8000 | tau | 738 | 0.0264 | 0.0059 | 0.0202 | 0.0362 | 0.0602 | 0.0000 | 0.3391 |
| new | own | 17-30 | top3_stress | 0.0000 | tau | 738 | 0.0053 | 0.0000 | 0.0004 | 0.0057 | 0.0190 | 0.0000 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.5000 | tau | 738 | 0.0053 | 0.0000 | 0.0004 | 0.0057 | 0.0190 | 0.1301 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.8000 | tau | 738 | 0.0053 | 0.0000 | 0.0004 | 0.0057 | 0.0190 | 0.1301 | 0.1000 |
| delta | actual | all | - | 0.0000 | M | 1578 | 0.0013 | -0.0000 | 0.0000 | 0.0002 | 0.0107 |  |  |
| delta | actual | all | linear | 0.0000 | tau | 1578 | 0.0002 | -0.0038 | 0.0000 | 0.0031 | 0.0116 | 0.0000 | 0.5000 |
| delta | actual | all | linear | 0.5000 | tau | 1578 | -0.0002 | -0.0044 | 0.0000 | 0.0027 | 0.0106 | 0.0133 | 0.5000 |
| delta | actual | all | linear | 0.8000 | tau | 1578 | -0.0004 | -0.0045 | 0.0000 | 0.0025 | 0.0101 | 0.0222 | 0.5000 |
| delta | actual | all | concave | 0.0000 | tau | 1578 | 0.0007 | -0.0019 | 0.0000 | 0.0026 | 0.0104 | 0.0000 | 0.6599 |
| delta | actual | all | concave | 0.5000 | tau | 1578 | 0.0002 | -0.0020 | 0.0000 | 0.0017 | 0.0073 | 0.0456 | 0.6599 |
| delta | actual | all | concave | 0.8000 | tau | 1578 | -0.0000 | -0.0024 | 0.0000 | 0.0015 | 0.0065 | 0.0735 | 0.6599 |
| delta | actual | all | convex | 0.0000 | tau | 1578 | -0.0006 | -0.0070 | 0.0000 | 0.0041 | 0.0140 | 0.0000 | 0.3391 |
| delta | actual | all | convex | 0.5000 | tau | 1578 | -0.0008 | -0.0069 | 0.0000 | 0.0040 | 0.0137 | 0.0095 | 0.3391 |
| delta | actual | all | convex | 0.8000 | tau | 1578 | -0.0009 | -0.0068 | 0.0000 | 0.0037 | 0.0134 | 0.0165 | 0.3391 |
| delta | actual | all | top3_stress | 0.0000 | tau | 1578 | -0.0017 | -0.0067 | 0.0000 | 0.0017 | 0.0102 | 0.0000 | 0.1000 |
| delta | actual | all | top3_stress | 0.5000 | tau | 1578 | -0.0017 | -0.0066 | 0.0000 | 0.0016 | 0.0100 | 0.0361 | 0.1000 |
| delta | actual | all | top3_stress | 0.8000 | tau | 1578 | -0.0018 | -0.0065 | 0.0000 | 0.0016 | 0.0099 | 0.0380 | 0.1000 |
| delta | actual | 1-3 | - | 0.0000 | M | 160 | 0.0025 | -0.0000 | 0.0000 | 0.0019 | 0.0096 |  |  |
| delta | actual | 1-3 | linear | 0.0000 | tau | 160 | -0.0032 | -0.0052 | -0.0022 | -0.0011 | -0.0004 | 0.0000 | 0.5000 |
| delta | actual | 1-3 | linear | 0.5000 | tau | 160 | -0.0039 | -0.0058 | -0.0030 | -0.0014 | -0.0007 | 0.0312 | 0.5000 |
| delta | actual | 1-3 | linear | 0.8000 | tau | 160 | -0.0042 | -0.0059 | -0.0032 | -0.0016 | -0.0010 | 0.0500 | 0.5000 |
| delta | actual | 1-3 | concave | 0.0000 | tau | 160 | -0.0006 | -0.0025 | -0.0009 | 0.0007 | 0.0031 | 0.0000 | 0.6599 |
| delta | actual | 1-3 | concave | 0.5000 | tau | 160 | -0.0014 | -0.0025 | -0.0010 | -0.0002 | 0.0011 | 0.1250 | 0.6599 |
| delta | actual | 1-3 | concave | 0.8000 | tau | 160 | -0.0019 | -0.0030 | -0.0015 | -0.0007 | -0.0003 | 0.2250 | 0.6599 |
| delta | actual | 1-3 | convex | 0.0000 | tau | 160 | -0.0073 | -0.0102 | -0.0054 | -0.0027 | -0.0017 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | convex | 0.5000 | tau | 160 | -0.0077 | -0.0108 | -0.0057 | -0.0030 | -0.0019 | 0.0125 | 0.3391 |
| delta | actual | 1-3 | convex | 0.8000 | tau | 160 | -0.0079 | -0.0110 | -0.0060 | -0.0031 | -0.0019 | 0.0125 | 0.3391 |
| delta | actual | 1-3 | top3_stress | 0.0000 | tau | 160 | -0.0088 | -0.0137 | -0.0050 | -0.0006 | -0.0000 | 0.0000 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.5000 | tau | 160 | -0.0089 | -0.0139 | -0.0052 | -0.0006 | -0.0000 | 0.0000 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.8000 | tau | 160 | -0.0090 | -0.0140 | -0.0053 | -0.0006 | -0.0000 | 0.0063 | 0.1000 |
| delta | actual | 4-10 | - | 0.0000 | M | 367 | -0.0011 | -0.0003 | 0.0000 | 0.0010 | 0.0097 |  |  |
| delta | actual | 4-10 | linear | 0.0000 | tau | 367 | -0.0089 | -0.0157 | -0.0068 | -0.0026 | 0.0000 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | linear | 0.5000 | tau | 367 | -0.0087 | -0.0137 | -0.0072 | -0.0036 | 0.0000 | 0.0054 | 0.5000 |
| delta | actual | 4-10 | linear | 0.8000 | tau | 367 | -0.0085 | -0.0130 | -0.0077 | -0.0038 | 0.0000 | 0.0082 | 0.5000 |
| delta | actual | 4-10 | concave | 0.0000 | tau | 367 | -0.0056 | -0.0102 | -0.0039 | 0.0000 | 0.0024 | 0.0000 | 0.6599 |
| delta | actual | 4-10 | concave | 0.5000 | tau | 367 | -0.0052 | -0.0096 | -0.0038 | -0.0009 | 0.0000 | 0.1035 | 0.6599 |
| delta | actual | 4-10 | concave | 0.8000 | tau | 367 | -0.0050 | -0.0084 | -0.0039 | -0.0019 | 0.0000 | 0.1335 | 0.6599 |
| delta | actual | 4-10 | convex | 0.0000 | tau | 367 | -0.0133 | -0.0199 | -0.0124 | -0.0062 | 0.0000 | 0.0000 | 0.3391 |
| delta | actual | 4-10 | convex | 0.5000 | tau | 367 | -0.0131 | -0.0189 | -0.0123 | -0.0063 | 0.0000 | 0.0109 | 0.3391 |
| delta | actual | 4-10 | convex | 0.8000 | tau | 367 | -0.0130 | -0.0184 | -0.0119 | -0.0062 | 0.0000 | 0.0163 | 0.3391 |
| delta | actual | 4-10 | top3_stress | 0.0000 | tau | 367 | -0.0134 | -0.0179 | -0.0128 | -0.0073 | 0.0000 | 0.0000 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.5000 | tau | 367 | -0.0133 | -0.0180 | -0.0122 | -0.0073 | 0.0000 | 0.0054 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.8000 | tau | 367 | -0.0133 | -0.0179 | -0.0121 | -0.0072 | 0.0000 | 0.0054 | 0.1000 |
| delta | actual | 11-16 | - | 0.0000 | M | 313 | -0.0001 | -0.0000 | 0.0000 | 0.0004 | 0.0132 |  |  |
| delta | actual | 11-16 | linear | 0.0000 | tau | 313 | 0.0006 | -0.0043 | 0.0000 | 0.0071 | 0.0168 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | linear | 0.5000 | tau | 313 | 0.0006 | -0.0042 | 0.0000 | 0.0061 | 0.0148 | 0.0288 | 0.5000 |
| delta | actual | 11-16 | linear | 0.8000 | tau | 313 | 0.0006 | -0.0041 | 0.0000 | 0.0056 | 0.0132 | 0.0447 | 0.5000 |
| delta | actual | 11-16 | concave | 0.0000 | tau | 313 | 0.0001 | -0.0032 | 0.0000 | 0.0057 | 0.0154 | 0.0000 | 0.6599 |
| delta | actual | 11-16 | concave | 0.5000 | tau | 313 | 0.0001 | -0.0029 | 0.0000 | 0.0043 | 0.0114 | 0.0256 | 0.6599 |
| delta | actual | 11-16 | concave | 0.8000 | tau | 313 | 0.0002 | -0.0028 | 0.0000 | 0.0035 | 0.0086 | 0.0607 | 0.6599 |
| delta | actual | 11-16 | convex | 0.0000 | tau | 313 | 0.0018 | -0.0037 | 0.0000 | 0.0092 | 0.0204 | 0.0000 | 0.3391 |
| delta | actual | 11-16 | convex | 0.5000 | tau | 313 | 0.0018 | -0.0041 | 0.0000 | 0.0086 | 0.0188 | 0.0128 | 0.3391 |
| delta | actual | 11-16 | convex | 0.8000 | tau | 313 | 0.0018 | -0.0041 | 0.0000 | 0.0084 | 0.0178 | 0.0160 | 0.3391 |
| delta | actual | 11-16 | top3_stress | 0.0000 | tau | 313 | 0.0045 | -0.0000 | 0.0000 | 0.0104 | 0.0185 | 0.0000 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.5000 | tau | 313 | 0.0045 | -0.0005 | 0.0000 | 0.0103 | 0.0180 | 0.0160 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.8000 | tau | 313 | 0.0045 | -0.0006 | 0.0000 | 0.0103 | 0.0175 | 0.0192 | 0.1000 |
| delta | actual | 17-30 | - | 0.0000 | M | 738 | 0.0028 | -0.0000 | 0.0000 | 0.0000 | 0.0110 |  |  |
| delta | actual | 17-30 | linear | 0.0000 | tau | 738 | 0.0053 | 0.0000 | 0.0002 | 0.0065 | 0.0162 | 0.0000 | 0.5000 |
| delta | actual | 17-30 | linear | 0.5000 | tau | 738 | 0.0046 | 0.0000 | 0.0003 | 0.0063 | 0.0140 | 0.0068 | 0.5000 |
| delta | actual | 17-30 | linear | 0.8000 | tau | 738 | 0.0041 | 0.0000 | 0.0002 | 0.0055 | 0.0128 | 0.0136 | 0.5000 |
| delta | actual | 17-30 | concave | 0.0000 | tau | 738 | 0.0043 | 0.0000 | 0.0001 | 0.0040 | 0.0151 | 0.0000 | 0.6599 |
| delta | actual | 17-30 | concave | 0.5000 | tau | 738 | 0.0034 | 0.0000 | 0.0001 | 0.0039 | 0.0109 | 0.0081 | 0.6599 |
| delta | actual | 17-30 | concave | 0.8000 | tau | 738 | 0.0028 | 0.0000 | 0.0001 | 0.0036 | 0.0090 | 0.0163 | 0.6599 |
| delta | actual | 17-30 | convex | 0.0000 | tau | 738 | 0.0062 | 0.0000 | 0.0004 | 0.0081 | 0.0180 | 0.0000 | 0.3391 |
| delta | actual | 17-30 | convex | 0.5000 | tau | 738 | 0.0057 | 0.0000 | 0.0004 | 0.0077 | 0.0173 | 0.0068 | 0.3391 |
| delta | actual | 17-30 | convex | 0.8000 | tau | 738 | 0.0054 | 0.0000 | 0.0004 | 0.0074 | 0.0170 | 0.0176 | 0.3391 |
| delta | actual | 17-30 | top3_stress | 0.0000 | tau | 738 | 0.0031 | 0.0000 | 0.0001 | 0.0037 | 0.0104 | 0.0000 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.5000 | tau | 738 | 0.0029 | 0.0000 | 0.0002 | 0.0037 | 0.0100 | 0.0678 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.8000 | tau | 738 | 0.0029 | 0.0000 | 0.0002 | 0.0037 | 0.0097 | 0.0691 | 0.1000 |
| delta | own | all | - | 0.0000 | M | 1578 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | all | linear | 0.0000 | tau | 1578 | -0.0003 | -0.0062 | 0.0000 | 0.0033 | 0.0126 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.5000 | tau | 1578 | -0.0003 | -0.0062 | 0.0000 | 0.0033 | 0.0126 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.8000 | tau | 1578 | -0.0003 | -0.0062 | 0.0000 | 0.0033 | 0.0126 | 0.0000 | 0.5000 |
| delta | own | all | concave | 0.0000 | tau | 1578 | -0.0002 | -0.0036 | -0.0000 | 0.0016 | 0.0075 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.5000 | tau | 1578 | -0.0002 | -0.0036 | -0.0000 | 0.0016 | 0.0075 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.8000 | tau | 1578 | -0.0002 | -0.0036 | -0.0000 | 0.0016 | 0.0075 | 0.0000 | 0.6599 |
| delta | own | all | convex | 0.0000 | tau | 1578 | -0.0004 | -0.0098 | 0.0000 | 0.0055 | 0.0185 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.5000 | tau | 1578 | -0.0004 | -0.0098 | 0.0000 | 0.0055 | 0.0185 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.8000 | tau | 1578 | -0.0004 | -0.0098 | 0.0000 | 0.0055 | 0.0185 | 0.0000 | 0.3391 |
| delta | own | all | top3_stress | 0.0000 | tau | 1578 | -0.0007 | -0.0082 | 0.0000 | 0.0043 | 0.0158 | 0.0000 | 0.1000 |
| delta | own | all | top3_stress | 0.5000 | tau | 1578 | -0.0007 | -0.0082 | 0.0000 | 0.0043 | 0.0158 | 0.0139 | 0.1000 |
| delta | own | all | top3_stress | 0.8000 | tau | 1578 | -0.0007 | -0.0082 | 0.0000 | 0.0043 | 0.0158 | 0.0139 | 0.1000 |
| delta | own | 1-3 | - | 0.0000 | M | 160 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 1-3 | linear | 0.0000 | tau | 160 | -0.0045 | -0.0062 | -0.0035 | -0.0018 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.5000 | tau | 160 | -0.0045 | -0.0062 | -0.0035 | -0.0018 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.8000 | tau | 160 | -0.0045 | -0.0062 | -0.0035 | -0.0018 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | concave | 0.0000 | tau | 160 | -0.0024 | -0.0032 | -0.0018 | -0.0010 | -0.0007 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.5000 | tau | 160 | -0.0024 | -0.0032 | -0.0018 | -0.0010 | -0.0007 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.8000 | tau | 160 | -0.0024 | -0.0032 | -0.0018 | -0.0010 | -0.0007 | 0.0000 | 0.6599 |
| delta | own | 1-3 | convex | 0.0000 | tau | 160 | -0.0079 | -0.0110 | -0.0060 | -0.0032 | -0.0024 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.5000 | tau | 160 | -0.0079 | -0.0110 | -0.0060 | -0.0032 | -0.0024 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.8000 | tau | 160 | -0.0079 | -0.0110 | -0.0060 | -0.0032 | -0.0024 | 0.0000 | 0.3391 |
| delta | own | 1-3 | top3_stress | 0.0000 | tau | 160 | -0.0089 | -0.0134 | -0.0045 | -0.0009 | -0.0001 | 0.0000 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.5000 | tau | 160 | -0.0089 | -0.0134 | -0.0045 | -0.0009 | -0.0001 | 0.0000 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.8000 | tau | 160 | -0.0089 | -0.0134 | -0.0045 | -0.0009 | -0.0001 | 0.0000 | 0.1000 |
| delta | own | 4-10 | - | 0.0000 | M | 367 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 4-10 | linear | 0.0000 | tau | 367 | -0.0101 | -0.0142 | -0.0085 | -0.0057 | -0.0032 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.5000 | tau | 367 | -0.0101 | -0.0142 | -0.0085 | -0.0057 | -0.0032 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.8000 | tau | 367 | -0.0101 | -0.0142 | -0.0085 | -0.0057 | -0.0032 | 0.0000 | 0.5000 |
| delta | own | 4-10 | concave | 0.0000 | tau | 367 | -0.0058 | -0.0080 | -0.0047 | -0.0032 | -0.0017 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.5000 | tau | 367 | -0.0058 | -0.0080 | -0.0047 | -0.0032 | -0.0017 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.8000 | tau | 367 | -0.0058 | -0.0080 | -0.0047 | -0.0032 | -0.0017 | 0.0000 | 0.6599 |
| delta | own | 4-10 | convex | 0.0000 | tau | 367 | -0.0156 | -0.0219 | -0.0137 | -0.0093 | -0.0053 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.5000 | tau | 367 | -0.0156 | -0.0219 | -0.0137 | -0.0093 | -0.0053 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.8000 | tau | 367 | -0.0156 | -0.0219 | -0.0137 | -0.0093 | -0.0053 | 0.0000 | 0.3391 |
| delta | own | 4-10 | top3_stress | 0.0000 | tau | 367 | -0.0145 | -0.0184 | -0.0133 | -0.0089 | -0.0052 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.5000 | tau | 367 | -0.0145 | -0.0184 | -0.0133 | -0.0089 | -0.0052 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.8000 | tau | 367 | -0.0145 | -0.0184 | -0.0133 | -0.0089 | -0.0052 | 0.0000 | 0.1000 |
| delta | own | 11-16 | - | 0.0000 | M | 313 | 0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 11-16 | linear | 0.0000 | tau | 313 | 0.0013 | -0.0086 | 0.0012 | 0.0095 | 0.0180 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.5000 | tau | 313 | 0.0013 | -0.0086 | 0.0012 | 0.0095 | 0.0180 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.8000 | tau | 313 | 0.0013 | -0.0086 | 0.0012 | 0.0095 | 0.0180 | 0.0000 | 0.5000 |
| delta | own | 11-16 | concave | 0.0000 | tau | 313 | 0.0004 | -0.0053 | 0.0002 | 0.0053 | 0.0098 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.5000 | tau | 313 | 0.0004 | -0.0053 | 0.0002 | 0.0053 | 0.0098 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.8000 | tau | 313 | 0.0004 | -0.0053 | 0.0002 | 0.0053 | 0.0098 | 0.0000 | 0.6599 |
| delta | own | 11-16 | convex | 0.0000 | tau | 313 | 0.0037 | -0.0100 | 0.0043 | 0.0161 | 0.0287 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.5000 | tau | 313 | 0.0037 | -0.0100 | 0.0043 | 0.0161 | 0.0287 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.8000 | tau | 313 | 0.0037 | -0.0100 | 0.0043 | 0.0161 | 0.0287 | 0.0000 | 0.3391 |
| delta | own | 11-16 | top3_stress | 0.0000 | tau | 313 | 0.0074 | -0.0036 | 0.0078 | 0.0164 | 0.0236 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.5000 | tau | 313 | 0.0074 | -0.0036 | 0.0078 | 0.0164 | 0.0236 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.8000 | tau | 313 | 0.0074 | -0.0036 | 0.0078 | 0.0164 | 0.0236 | 0.0000 | 0.1000 |
| delta | own | 17-30 | - | 0.0000 | M | 738 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 17-30 | linear | 0.0000 | tau | 738 | 0.0048 | 0.0000 | 0.0004 | 0.0066 | 0.0164 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.5000 | tau | 738 | 0.0048 | 0.0000 | 0.0004 | 0.0066 | 0.0164 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.8000 | tau | 738 | 0.0048 | 0.0000 | 0.0004 | 0.0066 | 0.0164 | 0.0000 | 0.5000 |
| delta | own | 17-30 | concave | 0.0000 | tau | 738 | 0.0028 | 0.0000 | 0.0002 | 0.0040 | 0.0096 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.5000 | tau | 738 | 0.0028 | 0.0000 | 0.0002 | 0.0040 | 0.0096 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.8000 | tau | 738 | 0.0028 | 0.0000 | 0.0002 | 0.0040 | 0.0096 | 0.0000 | 0.6599 |
| delta | own | 17-30 | convex | 0.0000 | tau | 738 | 0.0070 | 0.0000 | 0.0008 | 0.0093 | 0.0242 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.5000 | tau | 738 | 0.0070 | 0.0000 | 0.0008 | 0.0093 | 0.0242 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.8000 | tau | 738 | 0.0070 | 0.0000 | 0.0008 | 0.0093 | 0.0242 | 0.0000 | 0.3391 |
| delta | own | 17-30 | top3_stress | 0.0000 | tau | 738 | 0.0046 | 0.0000 | 0.0004 | 0.0050 | 0.0165 | 0.0000 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.5000 | tau | 738 | 0.0046 | 0.0000 | 0.0004 | 0.0050 | 0.0165 | 0.0298 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.8000 | tau | 738 | 0.0046 | 0.0000 | 0.0004 | 0.0050 | 0.0165 | 0.0298 | 0.1000 |

## T5_attr_seeding

| rule | portfolio | seed_group | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| old | actual | <0.01 | B | dominance_positive | 0.7500 | 0.6595 | 0.8261 | 496 |
| old | actual | <0.01 | B | reversal | 0.0464 | 0.0235 | 0.0725 | 496 |
| old | actual | <0.01 | B | negligible | 0.1472 | 0.0803 | 0.2320 | 496 |
| old | actual | <0.01 | B | unresolved | 0.0565 | 0.0344 | 0.0801 | 496 |
| old | actual | 0.01-0.05 | B | dominance_positive | 0.6932 | 0.5233 | 0.8250 | 88 |
| old | actual | 0.01-0.05 | B | reversal | 0.0227 | 0.0000 | 0.1039 | 88 |
| old | actual | 0.01-0.05 | B | negligible | 0.2614 | 0.1395 | 0.3896 | 88 |
| old | actual | 0.01-0.05 | B | unresolved | 0.0227 | 0.0000 | 0.1026 | 88 |
| old | actual | >=0.05 | B | dominance_positive | 0.7294 | 0.7001 | 0.7592 | 994 |
| old | actual | >=0.05 | B | reversal | 0.0634 | 0.0245 | 0.1038 | 994 |
| old | actual | >=0.05 | B | negligible | 0.1901 | 0.1551 | 0.2287 | 994 |
| old | actual | >=0.05 | B | unresolved | 0.0171 | 0.0068 | 0.0294 | 994 |
| old | own | <0.01 | B | dominance_positive | 0.8952 | 0.8326 | 0.9500 | 496 |
| old | own | <0.01 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 496 |
| old | own | <0.01 | B | negligible | 0.1008 | 0.0467 | 0.1674 | 496 |
| old | own | <0.01 | B | unresolved | 0.0040 | 0.0000 | 0.0151 | 496 |
| old | own | 0.01-0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 88 |
| old | own | 0.01-0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 88 |
| old | own | 0.01-0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 88 |
| old | own | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 88 |
| old | own | >=0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 994 |
| old | own | >=0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 994 |
| old | own | >=0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 994 |
| old | own | >=0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 994 |
| new | actual | <0.01 | B | dominance_positive | 0.1431 | 0.0332 | 0.2510 | 496 |
| new | actual | <0.01 | B | reversal | 0.3609 | 0.2527 | 0.5154 | 496 |
| new | actual | <0.01 | B | negligible | 0.4254 | 0.3566 | 0.4881 | 496 |
| new | actual | <0.01 | B | unresolved | 0.0706 | 0.0330 | 0.1098 | 496 |
| new | actual | 0.01-0.05 | B | dominance_positive | 0.4318 | 0.2659 | 0.5803 | 88 |
| new | actual | 0.01-0.05 | B | reversal | 0.0227 | 0.0000 | 0.1039 | 88 |
| new | actual | 0.01-0.05 | B | negligible | 0.5341 | 0.4043 | 0.6667 | 88 |
| new | actual | 0.01-0.05 | B | unresolved | 0.0114 | 0.0000 | 0.0606 | 88 |
| new | actual | >=0.05 | B | dominance_positive | 0.7626 | 0.7294 | 0.8002 | 994 |
| new | actual | >=0.05 | B | reversal | 0.0684 | 0.0241 | 0.1148 | 994 |
| new | actual | >=0.05 | B | negligible | 0.1579 | 0.1224 | 0.1984 | 994 |
| new | actual | >=0.05 | B | unresolved | 0.0111 | 0.0019 | 0.0234 | 994 |
| new | own | <0.01 | B | dominance_positive | 0.1069 | 0.0577 | 0.1594 | 496 |
| new | own | <0.01 | B | reversal | 0.3548 | 0.2420 | 0.5156 | 496 |
| new | own | <0.01 | B | negligible | 0.5081 | 0.3683 | 0.6140 | 496 |
| new | own | <0.01 | B | unresolved | 0.0302 | 0.0122 | 0.0508 | 496 |
| new | own | 0.01-0.05 | B | dominance_positive | 0.7727 | 0.6374 | 0.8933 | 88 |
| new | own | 0.01-0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 88 |
| new | own | 0.01-0.05 | B | negligible | 0.2273 | 0.1067 | 0.3626 | 88 |
| new | own | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 88 |
| new | own | >=0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 994 |
| new | own | >=0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 994 |
| new | own | >=0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 994 |
| new | own | >=0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 994 |

## T5_attr_ledger_features

| rule | feature | value | n | reversal_share | lo99 | hi99 |
|---|---|---|---|---|---|---|
| old | holds_conditional_other | True | 628 | 0.0955 | 0.0700 | 0.1212 |
| old | holds_conditional_other | False | 950 | 0.0295 | 0.0010 | 0.0657 |
| old | holds_opponent_pick | True | 48 | 0.4375 | 0.2678 | 0.6250 |
| old | holds_opponent_pick | False | 1530 | 0.0438 | 0.0174 | 0.0702 |
| old | holds_pooled_pick | True | 350 | 0.0657 | 0.0000 | 0.1054 |
| old | holds_pooled_pick | False | 1228 | 0.0529 | 0.0306 | 0.0811 |
| old | self_restricted | True | 134 | 0.0299 | 0.0000 | 0.0844 |
| old | self_restricted | False | 1444 | 0.0582 | 0.0309 | 0.0860 |
| old | opp_restricted | True | 134 | 0.0672 | 0.0000 | 0.1364 |
| old | opp_restricted | False | 1444 | 0.0547 | 0.0299 | 0.0815 |
| old | holds_conditional_other_state | True | 575 | 0.1026 | 0.0749 | 0.1304 |
| old | holds_conditional_other_state | False | 1003 | 0.0289 | 0.0019 | 0.0622 |
| old | holds_opponent_pick_state | True | 43 | 0.4884 | 0.3023 | 0.6774 |
| old | holds_opponent_pick_state | False | 1535 | 0.0436 | 0.0173 | 0.0700 |
| new | holds_conditional_other | True | 628 | 0.2325 | 0.1930 | 0.2813 |
| new | holds_conditional_other | False | 950 | 0.1084 | 0.0881 | 0.1281 |
| new | holds_opponent_pick | True | 48 | 0.4583 | 0.2326 | 0.7333 |
| new | holds_opponent_pick | False | 1530 | 0.1484 | 0.1265 | 0.1669 |
| new | holds_pooled_pick | True | 350 | 0.1343 | 0.0820 | 0.2866 |
| new | holds_pooled_pick | False | 1228 | 0.1645 | 0.1323 | 0.1996 |
| new | self_restricted | True | 134 | 0.3731 | 0.2839 | 0.5333 |
| new | self_restricted | False | 1444 | 0.1378 | 0.1148 | 0.1580 |
| new | opp_restricted | True | 134 | 0.1493 | 0.0751 | 0.2816 |
| new | opp_restricted | False | 1444 | 0.1586 | 0.1367 | 0.1787 |
| new | holds_conditional_other_state | True | 602 | 0.2010 | 0.1435 | 0.2435 |
| new | holds_conditional_other_state | False | 976 | 0.1311 | 0.1036 | 0.1603 |
| new | holds_opponent_pick_state | True | 45 | 0.4667 | 0.2500 | 0.7143 |
| new | holds_opponent_pick_state | False | 1533 | 0.1487 | 0.1273 | 0.1669 |

## T5_6_transitions

| portfolio | old | new | count |
|---|---|---|---|
| actual | dominance_positive | dominance_positive | 809 |
| actual | dominance_positive | negligible | 163 |
| actual | dominance_positive | reversal | 162 |
| actual | dominance_positive | unresolved | 24 |
| actual | negligible | dominance_positive | 41 |
| actual | negligible | negligible | 243 |
| actual | negligible | unresolved | 1 |
| actual | reversal | dominance_positive | 5 |
| actual | reversal | negligible | 1 |
| actual | reversal | reversal | 79 |
| actual | reversal | unresolved | 3 |
| actual | unresolved | dominance_positive | 12 |
| actual | unresolved | negligible | 8 |
| actual | unresolved | reversal | 8 |
| actual | unresolved | unresolved | 19 |
| own | dominance_positive | dominance_positive | 1115 |
| own | dominance_positive | negligible | 220 |
| own | dominance_positive | reversal | 176 |
| own | dominance_positive | unresolved | 15 |
| own | negligible | negligible | 50 |
| own | unresolved | negligible | 2 |

## T5_headline_reversal_diff

| contrast | portfolio | verdict | share_a | share_b | diff | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| new_minus_old | actual | verdict_B | 0.1578 | 0.0558 | 0.1020 | 0.0744 | 0.1340 | 1578 |
| new_minus_old | actual | verdict_B_pm | 0.1255 | 0.0393 | 0.0862 | 0.0692 | 0.1043 | 1578 |
| new_minus_old | own | verdict_B | 0.1115 | 0.0000 | 0.1115 | 0.0800 | 0.1452 | 1578 |
| new_minus_old | own | verdict_B_pm | 0.0963 | 0.0000 | 0.0963 | 0.0706 | 0.1245 | 1578 |
| actual_minus_own | old | verdict_B | 0.0558 | 0.0000 | 0.0558 | 0.0288 | 0.0830 | 1578 |
| actual_minus_own | new | verdict_B | 0.1578 | 0.1115 | 0.0463 | 0.0136 | 0.0785 | 1578 |

## T5_4_typology

| rule | curve | type | share | lo99 | hi99 | n | tp_dominated_share | n_tp_defined |
|---|---|---|---|---|---|---|---|---|
| old | linear | both_lose | 0.5082 | 0.4639 | 0.5618 | 401 | 0.3616 | 401 |
| old | linear | both_win | 0.0013 | 0.0000 | 0.0062 | 1 | 1.0000 | 1 |
| old | linear | normal | 0.3612 | 0.3214 | 0.4000 | 285 | 0.7113 | 284 |
| old | linear | opposed | 0.0380 | 0.0134 | 0.0668 | 30 | 0.8667 | 30 |
| old | linear | one_sided_win | 0.0253 | 0.0087 | 0.0444 | 20 | 0.9000 | 20 |
| old | linear | no_own_stake | 0.0659 | 0.0461 | 0.0871 | 52 | 1.0000 | 41 |
| old | concave | both_lose | 0.4233 | 0.3808 | 0.4698 | 334 | 0.4102 | 334 |
| old | concave | both_win | 0.0013 | 0.0000 | 0.0062 | 1 | 1.0000 | 1 |
| old | concave | normal | 0.4030 | 0.3632 | 0.4476 | 318 | 0.6203 | 316 |
| old | concave | opposed | 0.0406 | 0.0181 | 0.0666 | 32 | 0.8125 | 32 |
| old | concave | one_sided_win | 0.0253 | 0.0086 | 0.0443 | 20 | 0.9000 | 20 |
| old | concave | no_own_stake | 0.1065 | 0.0814 | 0.1374 | 84 | 1.0000 | 62 |
| old | convex | both_lose | 0.5285 | 0.4813 | 0.5802 | 417 | 0.2998 | 417 |
| old | convex | both_win | 0.0013 | 0.0000 | 0.0062 | 1 | 1.0000 | 1 |
| old | convex | normal | 0.3536 | 0.3142 | 0.3920 | 279 | 0.6223 | 278 |
| old | convex | opposed | 0.0393 | 0.0107 | 0.0713 | 31 | 0.8065 | 31 |
| old | convex | one_sided_win | 0.0165 | 0.0041 | 0.0304 | 13 | 0.8462 | 13 |
| old | convex | no_own_stake | 0.0608 | 0.0387 | 0.0885 | 48 | 1.0000 | 37 |
| old | top3_stress | both_lose | 0.1521 | 0.1221 | 0.1882 | 120 | 0.0000 | 120 |
| old | top3_stress | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| old | top3_stress | normal | 0.4613 | 0.3934 | 0.5164 | 364 | 0.1219 | 361 |
| old | top3_stress | opposed | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| old | top3_stress | one_sided_win | 0.0051 | 0.0000 | 0.0150 | 4 | 0.6667 | 3 |
| old | top3_stress | no_own_stake | 0.3815 | 0.3434 | 0.4239 | 301 | 0.9851 | 67 |
| new | linear | both_lose | 0.3093 | 0.2724 | 0.3510 | 244 | 0.3074 | 244 |
| new | linear | both_win | 0.0038 | 0.0000 | 0.0108 | 3 | 0.6667 | 3 |
| new | linear | normal | 0.4297 | 0.3846 | 0.4750 | 339 | 0.5148 | 338 |
| new | linear | opposed | 0.0532 | 0.0345 | 0.0739 | 42 | 0.7381 | 42 |
| new | linear | one_sided_win | 0.0266 | 0.0136 | 0.0412 | 21 | 0.8571 | 21 |
| new | linear | no_own_stake | 0.1774 | 0.1444 | 0.2111 | 140 | 1.0000 | 68 |
| new | concave | both_lose | 0.3422 | 0.2986 | 0.3839 | 270 | 0.3667 | 270 |
| new | concave | both_win | 0.0025 | 0.0000 | 0.0100 | 2 | 1.0000 | 2 |
| new | concave | normal | 0.4259 | 0.3721 | 0.4814 | 336 | 0.6036 | 333 |
| new | concave | opposed | 0.0406 | 0.0153 | 0.0678 | 32 | 0.8125 | 32 |
| new | concave | one_sided_win | 0.0215 | 0.0056 | 0.0425 | 17 | 0.8824 | 17 |
| new | concave | no_own_stake | 0.1673 | 0.1310 | 0.2043 | 132 | 1.0000 | 66 |
| new | convex | both_lose | 0.2636 | 0.2198 | 0.3109 | 208 | 0.2452 | 208 |
| new | convex | both_win | 0.0076 | 0.0000 | 0.0185 | 6 | 0.1667 | 6 |
| new | convex | normal | 0.4005 | 0.3572 | 0.4437 | 316 | 0.4589 | 316 |
| new | convex | opposed | 0.0798 | 0.0559 | 0.1038 | 63 | 0.5079 | 63 |
| new | convex | one_sided_win | 0.0684 | 0.0468 | 0.0912 | 54 | 0.6346 | 52 |
| new | convex | no_own_stake | 0.1800 | 0.1351 | 0.2189 | 142 | 1.0000 | 50 |
| new | top3_stress | both_lose | 0.1052 | 0.0648 | 0.1537 | 83 | 0.0000 | 83 |
| new | top3_stress | both_win | 0.0063 | 0.0000 | 0.0185 | 5 | 0.0000 | 5 |
| new | top3_stress | normal | 0.3523 | 0.3096 | 0.3972 | 278 | 0.1728 | 272 |
| new | top3_stress | opposed | 0.0507 | 0.0304 | 0.0734 | 40 | 0.0500 | 40 |
| new | top3_stress | one_sided_win | 0.1305 | 0.0818 | 0.1818 | 103 | 0.3021 | 96 |
| new | top3_stress | no_own_stake | 0.3549 | 0.3111 | 0.3982 | 280 | 1.0000 | 79 |

## T5_5_stakes_distribution

| rule | curve | measure | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| old | linear | tp_share | 777 | 0.5496 | 0.4013 | 0.5338 | 0.7231 | 0.9004 |
| old | linear | tp_share_raw | 785 | 0.6047 | 0.4936 | 0.5843 | 0.7432 | 0.9078 |
| old | linear | hhi | 777 | 0.3017 | 0.2075 | 0.2717 | 0.3621 | 0.4871 |
| old | linear | n_material | 789 | 6.6451 | 4.0000 | 7.0000 | 9.0000 | 11.0000 |
| old | linear | mean_abs_third | 789 | 0.0020 | 0.0008 | 0.0015 | 0.0026 | 0.0037 |
| old | linear | mean_abs_third_raw | 789 | 0.0023 | 0.0012 | 0.0019 | 0.0030 | 0.0041 |
| old | concave | tp_share | 765 | 0.5777 | 0.4295 | 0.5660 | 0.7724 | 0.9451 |
| old | concave | tp_share_raw | 782 | 0.6240 | 0.4985 | 0.6096 | 0.7811 | 0.9248 |
| old | concave | hhi | 765 | 0.3112 | 0.2089 | 0.2793 | 0.3761 | 0.5000 |
| old | concave | n_material | 789 | 6.2129 | 4.0000 | 6.0000 | 8.0000 | 10.0000 |
| old | concave | mean_abs_third | 789 | 0.0022 | 0.0008 | 0.0017 | 0.0028 | 0.0043 |
| old | concave | mean_abs_third_raw | 789 | 0.0025 | 0.0012 | 0.0020 | 0.0032 | 0.0047 |
| old | convex | tp_share | 777 | 0.4854 | 0.3115 | 0.4899 | 0.6651 | 0.8595 |
| old | convex | tp_share_raw | 786 | 0.5892 | 0.4865 | 0.5563 | 0.7211 | 0.8884 |
| old | convex | hhi | 777 | 0.3648 | 0.2351 | 0.3178 | 0.4401 | 0.5337 |
| old | convex | n_material | 789 | 5.1407 | 3.0000 | 5.0000 | 7.0000 | 9.0000 |
| old | convex | mean_abs_third | 789 | 0.0013 | 0.0004 | 0.0010 | 0.0018 | 0.0026 |
| old | convex | mean_abs_third_raw | 789 | 0.0017 | 0.0008 | 0.0014 | 0.0022 | 0.0029 |
| old | top3_stress | tp_share | 551 | 0.3972 | 0.2194 | 0.4176 | 0.4911 | 1.0000 |
| old | top3_stress | tp_share_raw | 637 | 0.5438 | 0.4860 | 0.5022 | 0.5289 | 0.9625 |
| old | top3_stress | hhi | 551 | 0.5579 | 0.3759 | 0.5001 | 0.5923 | 1.0000 |
| old | top3_stress | n_material | 789 | 1.8821 | 0.0000 | 2.0000 | 3.0000 | 4.0000 |
| old | top3_stress | mean_abs_third | 789 | 0.0002 | 0.0000 | 0.0001 | 0.0004 | 0.0007 |
| old | top3_stress | mean_abs_third_raw | 789 | 0.0004 | 0.0001 | 0.0003 | 0.0006 | 0.0009 |
| new | linear | tp_share | 716 | 0.5572 | 0.4168 | 0.5047 | 0.7029 | 0.9835 |
| new | linear | tp_share_raw | 752 | 0.6087 | 0.5000 | 0.5686 | 0.7360 | 0.9073 |
| new | linear | hhi | 716 | 0.3178 | 0.2233 | 0.2995 | 0.3767 | 0.4649 |
| new | linear | n_material | 789 | 5.9899 | 3.0000 | 6.0000 | 8.0000 | 11.0000 |
| new | linear | mean_abs_third | 789 | 0.0017 | 0.0005 | 0.0012 | 0.0023 | 0.0038 |
| new | linear | mean_abs_third_raw | 789 | 0.0020 | 0.0008 | 0.0016 | 0.0026 | 0.0041 |
| new | concave | tp_share | 720 | 0.5683 | 0.4401 | 0.5313 | 0.7150 | 0.9383 |
| new | concave | tp_share_raw | 756 | 0.6172 | 0.5013 | 0.5904 | 0.7418 | 0.9067 |
| new | concave | hhi | 720 | 0.3028 | 0.2060 | 0.2828 | 0.3711 | 0.4867 |
| new | concave | n_material | 789 | 6.0735 | 4.0000 | 6.0000 | 9.0000 | 11.0000 |
| new | concave | mean_abs_third | 789 | 0.0019 | 0.0006 | 0.0013 | 0.0024 | 0.0042 |
| new | concave | mean_abs_third_raw | 789 | 0.0022 | 0.0010 | 0.0017 | 0.0027 | 0.0046 |
| new | convex | tp_share | 695 | 0.4862 | 0.3398 | 0.4796 | 0.6571 | 0.8926 |
| new | convex | tp_share_raw | 752 | 0.5965 | 0.5000 | 0.5467 | 0.7023 | 0.9075 |
| new | convex | hhi | 695 | 0.4054 | 0.2671 | 0.3477 | 0.4696 | 0.6816 |
| new | convex | n_material | 789 | 4.4499 | 2.0000 | 4.0000 | 6.0000 | 9.0000 |
| new | convex | mean_abs_third | 789 | 0.0012 | 0.0002 | 0.0007 | 0.0017 | 0.0032 |
| new | convex | mean_abs_third_raw | 789 | 0.0016 | 0.0005 | 0.0012 | 0.0020 | 0.0035 |
| new | top3_stress | tp_share | 575 | 0.4446 | 0.2867 | 0.4372 | 0.5277 | 1.0000 |
| new | top3_stress | tp_share_raw | 638 | 0.5826 | 0.4954 | 0.5048 | 0.6177 | 0.9812 |
| new | top3_stress | hhi | 575 | 0.5058 | 0.3562 | 0.4391 | 0.5267 | 1.0000 |
| new | top3_stress | n_material | 789 | 2.2129 | 0.0000 | 2.0000 | 3.0000 | 5.0000 |
| new | top3_stress | mean_abs_third | 789 | 0.0004 | 0.0000 | 0.0002 | 0.0006 | 0.0012 |
| new | top3_stress | mean_abs_third_raw | 789 | 0.0006 | 0.0001 | 0.0004 | 0.0008 | 0.0014 |
| new_minus_old | linear | tp_share | 716 | -0.0005 | -0.0538 | 0.0000 | 0.0560 | 0.1313 |
| new_minus_old | linear | hhi | 716 | 0.0317 | -0.0228 | 0.0052 | 0.0634 | 0.1519 |
| new_minus_old | linear | mean_abs_third | 789 | -0.0002 | -0.0006 | 0.0000 | 0.0003 | 0.0009 |
| new_minus_old | concave | tp_share | 715 | -0.0145 | -0.0709 | 0.0000 | 0.0403 | 0.1057 |
| new_minus_old | concave | hhi | 715 | 0.0039 | -0.0391 | -0.0002 | 0.0352 | 0.1211 |
| new_minus_old | concave | mean_abs_third | 789 | -0.0003 | -0.0005 | 0.0000 | 0.0003 | 0.0009 |
| new_minus_old | convex | tp_share | 695 | -0.0087 | -0.0809 | 0.0000 | 0.0968 | 0.1855 |
| new_minus_old | convex | hhi | 695 | 0.0564 | -0.0535 | 0.0034 | 0.1077 | 0.2591 |
| new_minus_old | convex | mean_abs_third | 789 | -0.0000 | -0.0005 | 0.0000 | 0.0004 | 0.0012 |
| new_minus_old | top3_stress | tp_share | 445 | 0.0933 | -0.0434 | 0.0459 | 0.2868 | 0.4645 |
| new_minus_old | top3_stress | hhi | 445 | -0.1205 | -0.4697 | -0.0407 | 0.0955 | 0.2468 |
| new_minus_old | top3_stress | mean_abs_third | 789 | 0.0002 | -0.0002 | 0.0000 | 0.0004 | 0.0010 |

## H2

| curve | sample | n_games | mean_diff_new_minus_old | lo99 | hi99 | registered | supported |
|---|---|---|---|---|---|---|---|
| linear | registered | 647 | -0.0002 | -0.0006 | 0.0000 | True | False |
| linear | state_conditional | 581 | -0.0003 | -0.0006 | 0.0000 | False | False |
| concave | registered | 647 | -0.0003 | -0.0007 | 0.0000 | False | False |
| concave | state_conditional | 581 | -0.0003 | -0.0007 | -0.0000 | False | False |
| convex | registered | 647 | -0.0000 | -0.0004 | 0.0003 | False | False |
| convex | state_conditional | 581 | -0.0000 | -0.0004 | 0.0003 | False | False |
| top3_stress | registered | 647 | 0.0002 | 0.0000 | 0.0004 | False | True |
| top3_stress | state_conditional | 581 | 0.0003 | 0.0000 | 0.0004 | False | True |

## F5_2_network_edges

3480 rows in `F5_2_network_edges.csv`.

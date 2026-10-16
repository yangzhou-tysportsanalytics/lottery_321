# Registered analysis output

tag `dta2`; exclude_imprecise=False; states=81

## T5_0_diagnostics

| states | games | stopped_2000 | stopped_8000 | stopped_32000 | missed_target | n_worlds_match | max_halfwidth_linear | max_halfwidth_linear_rules_only | max_halfwidth_delta_linear | p95_halfwidth_linear | max_q_total_dev | max_per_slot_dev | per_slot_noise_scale | max_own_slot_dev | max_zero_sum_dev |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 81 | 626 | 2 | 3 | 38 | 38 | 2000 | 0.0064 | 0.0063 | 0.0064 | 0.0049 | 0.0000 | 0.0066 | 0.0112 | 0.0000 | 0.0032 |

## T5_0b_zero_sum_by_curve

| curve | rule | max_zero_sum_dev | mean_zero_sum_dev | n_games |
|---|---|---|---|---|
| linear | old | 0.0009 | 0.0001 | 626 |
| linear | new | 0.0014 | 0.0001 | 626 |
| concave | old | 0.0005 | 0.0000 | 626 |
| concave | new | 0.0008 | 0.0001 | 626 |
| convex | old | 0.0016 | 0.0001 | 626 |
| convex | new | 0.0022 | 0.0002 | 626 |
| top3_stress | old | 0.0032 | 0.0004 | 626 |
| top3_stress | new | 0.0028 | 0.0003 | 626 |

## T5_0c_verdict_by_look

| rule | portfolio | stopped_at | verdict_B | verdict_B_pm | count |
|---|---|---|---|---|---|
| delta | actual | 2000 | dominance_positive | dominance_positive | 1 |
| delta | actual | 2000 | negligible | negligible | 3 |
| delta | actual | 2000 | reversal | reversal | 5 |
| delta | actual | 2000 | unresolved | unresolved | 1 |
| delta | actual | 32000 | dominance_positive | dominance_positive | 41 |
| delta | actual | 32000 | dominance_positive | unresolved | 23 |
| delta | actual | 32000 | negligible | dominance_positive | 1 |
| delta | actual | 32000 | negligible | negligible | 159 |
| delta | actual | 32000 | negligible | unresolved | 12 |
| delta | actual | 32000 | reversal | reversal | 267 |
| delta | actual | 32000 | reversal | unresolved | 44 |
| delta | actual | 32000 | unresolved | unresolved | 15 |
| delta | actual | 8000 | dominance_positive | unresolved | 1 |
| delta | actual | 8000 | negligible | negligible | 8 |
| delta | actual | 8000 | negligible | unresolved | 2 |
| delta | actual | 8000 | reversal | reversal | 14 |
| delta | actual | 8000 | unresolved | unresolved | 1 |
| delta | actual | missed | dominance_positive | dominance_positive | 58 |
| delta | actual | missed | dominance_positive | unresolved | 33 |
| delta | actual | missed | negligible | negligible | 194 |
| delta | actual | missed | negligible | unresolved | 5 |
| delta | actual | missed | reversal | reversal | 309 |
| delta | actual | missed | reversal | unresolved | 38 |
| delta | actual | missed | unresolved | unresolved | 17 |
| delta | own | 2000 | negligible | negligible | 1 |
| delta | own | 2000 | reversal | reversal | 8 |
| delta | own | 2000 | unresolved | unresolved | 1 |
| delta | own | 32000 | dominance_positive | dominance_positive | 1 |
| delta | own | 32000 | dominance_positive | unresolved | 36 |
| delta | own | 32000 | negligible | negligible | 96 |
| delta | own | 32000 | negligible | unresolved | 18 |
| delta | own | 32000 | reversal | reversal | 310 |
| delta | own | 32000 | reversal | unresolved | 70 |
| delta | own | 32000 | unresolved | unresolved | 31 |
| delta | own | 8000 | dominance_positive | unresolved | 1 |
| delta | own | 8000 | negligible | negligible | 7 |
| delta | own | 8000 | negligible | unresolved | 1 |
| delta | own | 8000 | reversal | reversal | 15 |
| delta | own | 8000 | unresolved | unresolved | 2 |
| delta | own | missed | dominance_positive | dominance_positive | 5 |
| delta | own | missed | dominance_positive | unresolved | 37 |
| delta | own | missed | negligible | negligible | 134 |
| delta | own | missed | negligible | unresolved | 13 |
| delta | own | missed | reversal | reversal | 371 |
| delta | own | missed | reversal | unresolved | 61 |
| delta | own | missed | unresolved | unresolved | 33 |
| new | actual | 2000 | dominance_positive | dominance_positive | 3 |
| new | actual | 2000 | negligible | negligible | 3 |
| new | actual | 2000 | reversal | reversal | 3 |
| new | actual | 2000 | unresolved | unresolved | 1 |
| new | actual | 32000 | dominance_positive | dominance_positive | 304 |
| new | actual | 32000 | dominance_positive | unresolved | 15 |
| new | actual | 32000 | negligible | dominance_positive | 5 |
| new | actual | 32000 | negligible | negligible | 131 |
| new | actual | 32000 | negligible | unresolved | 11 |
| new | actual | 32000 | reversal | reversal | 63 |
| new | actual | 32000 | reversal | unresolved | 15 |
| new | actual | 32000 | unresolved | unresolved | 18 |
| new | actual | 8000 | dominance_positive | dominance_positive | 16 |
| new | actual | 8000 | negligible | negligible | 4 |
| new | actual | 8000 | reversal | reversal | 5 |
| new | actual | 8000 | unresolved | unresolved | 1 |
| new | actual | missed | dominance_positive | dominance_positive | 326 |
| new | actual | missed | dominance_positive | unresolved | 17 |
| new | actual | missed | negligible | dominance_positive | 6 |
| new | actual | missed | negligible | negligible | 201 |
| new | actual | missed | negligible | unresolved | 13 |
| new | actual | missed | reversal | reversal | 64 |
| new | actual | missed | reversal | unresolved | 12 |
| new | actual | missed | unresolved | unresolved | 15 |
| new | own | 2000 | dominance_positive | dominance_positive | 7 |
| new | own | 2000 | reversal | reversal | 2 |
| new | own | 2000 | unresolved | unresolved | 1 |
| new | own | 32000 | dominance_positive | dominance_positive | 420 |
| new | own | 32000 | dominance_positive | unresolved | 6 |
| new | own | 32000 | negligible | dominance_positive | 6 |
| new | own | 32000 | negligible | negligible | 55 |
| new | own | 32000 | negligible | unresolved | 4 |
| new | own | 32000 | reversal | reversal | 62 |
| new | own | 32000 | reversal | unresolved | 7 |
| new | own | 32000 | unresolved | unresolved | 2 |
| new | own | 8000 | dominance_positive | dominance_positive | 19 |
| new | own | 8000 | negligible | negligible | 2 |
| new | own | 8000 | reversal | reversal | 5 |
| new | own | missed | dominance_positive | dominance_positive | 466 |
| new | own | missed | dominance_positive | unresolved | 10 |
| new | own | missed | negligible | dominance_positive | 7 |
| new | own | missed | negligible | negligible | 115 |
| new | own | missed | negligible | unresolved | 2 |
| new | own | missed | reversal | reversal | 50 |
| new | own | missed | reversal | unresolved | 4 |
| old | actual | 2000 | dominance_positive | dominance_positive | 5 |
| old | actual | 2000 | negligible | negligible | 3 |
| old | actual | 2000 | reversal | reversal | 1 |
| old | actual | 2000 | unresolved | unresolved | 1 |
| old | actual | 32000 | dominance_positive | dominance_positive | 392 |
| old | actual | 32000 | dominance_positive | unresolved | 24 |
| old | actual | 32000 | negligible | negligible | 109 |
| old | actual | 32000 | negligible | unresolved | 6 |
| old | actual | 32000 | reversal | reversal | 15 |
| old | actual | 32000 | reversal | unresolved | 4 |
| old | actual | 32000 | unresolved | unresolved | 12 |
| old | actual | 8000 | dominance_positive | dominance_positive | 20 |
| old | actual | 8000 | dominance_positive | unresolved | 3 |
| old | actual | 8000 | negligible | negligible | 3 |
| old | actual | missed | dominance_positive | dominance_positive | 424 |
| old | actual | missed | dominance_positive | unresolved | 30 |
| old | actual | missed | negligible | dominance_positive | 6 |
| old | actual | missed | negligible | negligible | 149 |
| old | actual | missed | negligible | unresolved | 5 |
| old | actual | missed | reversal | reversal | 18 |
| old | actual | missed | reversal | unresolved | 10 |
| old | actual | missed | unresolved | unresolved | 12 |
| old | own | 2000 | dominance_positive | dominance_positive | 10 |
| old | own | 32000 | dominance_positive | dominance_positive | 547 |
| old | own | 32000 | dominance_positive | unresolved | 3 |
| old | own | 32000 | negligible | negligible | 10 |
| old | own | 32000 | negligible | unresolved | 2 |
| old | own | 8000 | dominance_positive | dominance_positive | 26 |
| old | own | missed | dominance_positive | dominance_positive | 620 |
| old | own | missed | dominance_positive | unresolved | 9 |
| old | own | missed | negligible | negligible | 24 |
| old | own | missed | negligible | unresolved | 1 |

## T5_0d_band_width

| rule | portfolio | measure | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| old | actual | band_ratio | 1252 | 1.3801 | 0.2483 | 1.2404 | 2.4219 | 2.8677 |
| old | actual | band_ratio_pm | 1252 | 5.3387 | 0.9867 | 4.8874 | 9.5823 | 11.1408 |
| old | own | band_ratio | 1252 | 2.0121 | 0.9539 | 2.3254 | 2.7009 | 3.0828 |
| old | own | band_ratio_pm | 1252 | 7.7404 | 3.6242 | 9.2383 | 10.7146 | 12.1025 |
| new | actual | band_ratio | 1252 | 1.0651 | 0.0757 | 0.6252 | 2.1599 | 2.6530 |
| new | actual | band_ratio_pm | 1252 | 4.1110 | 0.3021 | 2.3912 | 8.2365 | 10.5291 |
| new | own | band_ratio | 1252 | 1.6063 | 0.2754 | 1.9912 | 2.5862 | 2.8955 |
| new | own | band_ratio_pm | 1252 | 6.1628 | 1.0869 | 7.8146 | 10.2538 | 11.3798 |
| delta | actual | band_ratio | 1252 | 1.0562 | 0.0473 | 0.7312 | 1.7744 | 2.5838 |
| delta | actual | band_ratio_pm | 1252 | 4.0922 | 0.1894 | 2.8018 | 6.9490 | 10.1770 |
| delta | own | band_ratio | 1252 | 1.3685 | 0.4238 | 1.1179 | 2.3099 | 2.8675 |
| delta | own | band_ratio_pm | 1252 | 5.2787 | 1.6497 | 4.2228 | 9.1373 | 11.3755 |

## T5_1_verdicts

| rule | portfolio | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|
| old | actual | B | dominance_positive | 0.7173 | 0.6169 | 0.8050 | 1252 |
| old | actual | B | reversal | 0.0383 | 0.0165 | 0.0632 | 1252 |
| old | actual | B | negligible | 0.2244 | 0.1520 | 0.3070 | 1252 |
| old | actual | B | unresolved | 0.0200 | 0.0091 | 0.0336 | 1252 |
| old | actual | C | dominance_positive | 0.7173 | 0.6169 | 0.8050 | 1252 |
| old | actual | C | reversal | 0.0383 | 0.0165 | 0.0632 | 1252 |
| old | actual | C | negligible | 0.2244 | 0.1520 | 0.3070 | 1252 |
| old | actual | C | unresolved | 0.0200 | 0.0091 | 0.0336 | 1252 |
| old | actual | B_pm | dominance_positive | 0.6765 | 0.5754 | 0.7617 | 1252 |
| old | actual | B_pm | reversal | 0.0272 | 0.0103 | 0.0498 | 1252 |
| old | actual | B_pm | negligible | 0.2109 | 0.1443 | 0.2914 | 1252 |
| old | actual | B_pm | unresolved | 0.0855 | 0.0574 | 0.1129 | 1252 |
| old | actual | C_pm | dominance_positive | 0.6765 | 0.5754 | 0.7617 | 1252 |
| old | actual | C_pm | reversal | 0.0272 | 0.0103 | 0.0498 | 1252 |
| old | actual | C_pm | negligible | 0.2109 | 0.1443 | 0.2914 | 1252 |
| old | actual | C_pm | unresolved | 0.0855 | 0.0574 | 0.1129 | 1252 |
| old | own | B | dominance_positive | 0.9704 | 0.9275 | 0.9962 | 1252 |
| old | own | B | reversal | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | B | negligible | 0.0296 | 0.0038 | 0.0725 | 1252 |
| old | own | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | C | dominance_positive | 0.9704 | 0.9275 | 0.9962 | 1252 |
| old | own | C | reversal | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | C | negligible | 0.0296 | 0.0038 | 0.0725 | 1252 |
| old | own | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | B_pm | dominance_positive | 0.9609 | 0.9109 | 0.9889 | 1252 |
| old | own | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | B_pm | negligible | 0.0272 | 0.0034 | 0.0684 | 1252 |
| old | own | B_pm | unresolved | 0.0120 | 0.0009 | 0.0264 | 1252 |
| old | own | C_pm | dominance_positive | 0.9609 | 0.9109 | 0.9889 | 1252 |
| old | own | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | C_pm | negligible | 0.0272 | 0.0034 | 0.0684 | 1252 |
| old | own | C_pm | unresolved | 0.0120 | 0.0009 | 0.0264 | 1252 |
| new | actual | B | dominance_positive | 0.5439 | 0.4401 | 0.6364 | 1252 |
| new | actual | B | reversal | 0.1294 | 0.0662 | 0.1693 | 1252 |
| new | actual | B | negligible | 0.2987 | 0.2050 | 0.4011 | 1252 |
| new | actual | B | unresolved | 0.0280 | 0.0137 | 0.0489 | 1252 |
| new | actual | C | dominance_positive | 0.5439 | 0.4401 | 0.6364 | 1252 |
| new | actual | C | reversal | 0.1286 | 0.0661 | 0.1688 | 1252 |
| new | actual | C | negligible | 0.2987 | 0.2050 | 0.4011 | 1252 |
| new | actual | C | unresolved | 0.0288 | 0.0141 | 0.0495 | 1252 |
| new | actual | B_pm | dominance_positive | 0.5272 | 0.4256 | 0.6199 | 1252 |
| new | actual | B_pm | reversal | 0.1078 | 0.0552 | 0.1411 | 1252 |
| new | actual | B_pm | negligible | 0.2708 | 0.1868 | 0.3709 | 1252 |
| new | actual | B_pm | unresolved | 0.0942 | 0.0489 | 0.1580 | 1252 |
| new | actual | C_pm | dominance_positive | 0.5280 | 0.4256 | 0.6218 | 1252 |
| new | actual | C_pm | reversal | 0.1078 | 0.0552 | 0.1411 | 1252 |
| new | actual | C_pm | negligible | 0.2708 | 0.1868 | 0.3709 | 1252 |
| new | actual | C_pm | unresolved | 0.0935 | 0.0479 | 0.1577 | 1252 |
| new | own | B | dominance_positive | 0.7412 | 0.6667 | 0.8197 | 1252 |
| new | own | B | reversal | 0.1038 | 0.0506 | 0.1441 | 1252 |
| new | own | B | negligible | 0.1526 | 0.0868 | 0.2243 | 1252 |
| new | own | B | unresolved | 0.0024 | 0.0000 | 0.0074 | 1252 |
| new | own | C | dominance_positive | 0.7412 | 0.6667 | 0.8197 | 1252 |
| new | own | C | reversal | 0.1038 | 0.0506 | 0.1441 | 1252 |
| new | own | C | negligible | 0.1526 | 0.0868 | 0.2243 | 1252 |
| new | own | C | unresolved | 0.0024 | 0.0000 | 0.0074 | 1252 |
| new | own | B_pm | dominance_positive | 0.7388 | 0.6645 | 0.8208 | 1252 |
| new | own | B_pm | reversal | 0.0950 | 0.0461 | 0.1344 | 1252 |
| new | own | B_pm | negligible | 0.1374 | 0.0764 | 0.2070 | 1252 |
| new | own | B_pm | unresolved | 0.0288 | 0.0101 | 0.0495 | 1252 |
| new | own | C_pm | dominance_positive | 0.7388 | 0.6645 | 0.8208 | 1252 |
| new | own | C_pm | reversal | 0.0950 | 0.0461 | 0.1344 | 1252 |
| new | own | C_pm | negligible | 0.1374 | 0.0764 | 0.2070 | 1252 |
| new | own | C_pm | unresolved | 0.0288 | 0.0101 | 0.0495 | 1252 |
| delta | actual | B | dominance_positive | 0.1254 | 0.0777 | 0.1696 | 1252 |
| delta | actual | B | reversal | 0.5407 | 0.4841 | 0.5933 | 1252 |
| delta | actual | B | negligible | 0.3067 | 0.2522 | 0.3696 | 1252 |
| delta | actual | B | unresolved | 0.0272 | 0.0149 | 0.0436 | 1252 |
| delta | actual | C | dominance_positive | 0.1254 | 0.0777 | 0.1696 | 1252 |
| delta | actual | C | reversal | 0.5407 | 0.4841 | 0.5933 | 1252 |
| delta | actual | C | negligible | 0.3067 | 0.2522 | 0.3696 | 1252 |
| delta | actual | C | unresolved | 0.0272 | 0.0149 | 0.0436 | 1252 |
| delta | actual | B_pm | dominance_positive | 0.0807 | 0.0431 | 0.1179 | 1252 |
| delta | actual | B_pm | reversal | 0.4752 | 0.4237 | 0.5243 | 1252 |
| delta | actual | B_pm | negligible | 0.2907 | 0.2374 | 0.3425 | 1252 |
| delta | actual | B_pm | unresolved | 0.1534 | 0.1165 | 0.2007 | 1252 |
| delta | actual | C_pm | dominance_positive | 0.0807 | 0.0431 | 0.1179 | 1252 |
| delta | actual | C_pm | reversal | 0.4752 | 0.4237 | 0.5243 | 1252 |
| delta | actual | C_pm | negligible | 0.2907 | 0.2374 | 0.3425 | 1252 |
| delta | actual | C_pm | unresolved | 0.1534 | 0.1165 | 0.2007 | 1252 |
| delta | own | B | dominance_positive | 0.0639 | 0.0454 | 0.0835 | 1252 |
| delta | own | B | reversal | 0.6669 | 0.6237 | 0.7226 | 1252 |
| delta | own | B | negligible | 0.2157 | 0.1650 | 0.2630 | 1252 |
| delta | own | B | unresolved | 0.0535 | 0.0353 | 0.0757 | 1252 |
| delta | own | C | dominance_positive | 0.0639 | 0.0454 | 0.0835 | 1252 |
| delta | own | C | reversal | 0.6669 | 0.6237 | 0.7226 | 1252 |
| delta | own | C | negligible | 0.2157 | 0.1650 | 0.2630 | 1252 |
| delta | own | C | unresolved | 0.0535 | 0.0353 | 0.0757 | 1252 |
| delta | own | B_pm | dominance_positive | 0.0048 | 0.0000 | 0.0155 | 1252 |
| delta | own | B_pm | reversal | 0.5623 | 0.5098 | 0.6157 | 1252 |
| delta | own | B_pm | negligible | 0.1901 | 0.1358 | 0.2394 | 1252 |
| delta | own | B_pm | unresolved | 0.2428 | 0.1951 | 0.2964 | 1252 |
| delta | own | C_pm | dominance_positive | 0.0048 | 0.0000 | 0.0155 | 1252 |
| delta | own | C_pm | reversal | 0.5623 | 0.5098 | 0.6157 | 1252 |
| delta | own | C_pm | negligible | 0.1901 | 0.1358 | 0.2394 | 1252 |
| delta | own | C_pm | unresolved | 0.2428 | 0.1951 | 0.2964 | 1252 |

## T5_2_verdicts_by_band

| rule | portfolio | band | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| old | actual | 1-3 | B | dominance_positive | 0.7812 | 0.6400 | 0.9070 | 128 |
| old | actual | 1-3 | B | reversal | 0.0391 | 0.0000 | 0.1129 | 128 |
| old | actual | 1-3 | B | negligible | 0.0703 | 0.0000 | 0.1862 | 128 |
| old | actual | 1-3 | B | unresolved | 0.1094 | 0.0238 | 0.2101 | 128 |
| old | actual | 1-3 | C | dominance_positive | 0.7812 | 0.6400 | 0.9070 | 128 |
| old | actual | 1-3 | C | reversal | 0.0391 | 0.0000 | 0.1129 | 128 |
| old | actual | 1-3 | C | negligible | 0.0703 | 0.0000 | 0.1862 | 128 |
| old | actual | 1-3 | C | unresolved | 0.1094 | 0.0238 | 0.2101 | 128 |
| old | actual | 1-3 | B_pm | dominance_positive | 0.6328 | 0.3636 | 0.8548 | 128 |
| old | actual | 1-3 | B_pm | reversal | 0.0312 | 0.0000 | 0.0887 | 128 |
| old | actual | 1-3 | B_pm | negligible | 0.0703 | 0.0000 | 0.1862 | 128 |
| old | actual | 1-3 | B_pm | unresolved | 0.2656 | 0.0753 | 0.4526 | 128 |
| old | actual | 1-3 | C_pm | dominance_positive | 0.6328 | 0.3636 | 0.8548 | 128 |
| old | actual | 1-3 | C_pm | reversal | 0.0312 | 0.0000 | 0.0887 | 128 |
| old | actual | 1-3 | C_pm | negligible | 0.0703 | 0.0000 | 0.1862 | 128 |
| old | actual | 1-3 | C_pm | unresolved | 0.2656 | 0.0753 | 0.4526 | 128 |
| old | actual | 4-10 | B | dominance_positive | 0.8441 | 0.7245 | 0.9470 | 295 |
| old | actual | 4-10 | B | reversal | 0.0508 | 0.0075 | 0.1082 | 295 |
| old | actual | 4-10 | B | negligible | 0.0915 | 0.0231 | 0.1782 | 295 |
| old | actual | 4-10 | B | unresolved | 0.0136 | 0.0000 | 0.0462 | 295 |
| old | actual | 4-10 | C | dominance_positive | 0.8441 | 0.7245 | 0.9470 | 295 |
| old | actual | 4-10 | C | reversal | 0.0508 | 0.0075 | 0.1082 | 295 |
| old | actual | 4-10 | C | negligible | 0.0915 | 0.0231 | 0.1782 | 295 |
| old | actual | 4-10 | C | unresolved | 0.0136 | 0.0000 | 0.0462 | 295 |
| old | actual | 4-10 | B_pm | dominance_positive | 0.7932 | 0.6580 | 0.9170 | 295 |
| old | actual | 4-10 | B_pm | reversal | 0.0339 | 0.0065 | 0.0691 | 295 |
| old | actual | 4-10 | B_pm | negligible | 0.0915 | 0.0231 | 0.1782 | 295 |
| old | actual | 4-10 | B_pm | unresolved | 0.0814 | 0.0169 | 0.1512 | 295 |
| old | actual | 4-10 | C_pm | dominance_positive | 0.7932 | 0.6580 | 0.9170 | 295 |
| old | actual | 4-10 | C_pm | reversal | 0.0339 | 0.0065 | 0.0691 | 295 |
| old | actual | 4-10 | C_pm | negligible | 0.0915 | 0.0231 | 0.1782 | 295 |
| old | actual | 4-10 | C_pm | unresolved | 0.0814 | 0.0169 | 0.1512 | 295 |
| old | actual | 11-16 | B | dominance_positive | 0.7942 | 0.6402 | 0.9016 | 243 |
| old | actual | 11-16 | B | reversal | 0.0206 | 0.0000 | 0.0588 | 243 |
| old | actual | 11-16 | B | negligible | 0.1770 | 0.0827 | 0.3198 | 243 |
| old | actual | 11-16 | B | unresolved | 0.0082 | 0.0000 | 0.0394 | 243 |
| old | actual | 11-16 | C | dominance_positive | 0.7942 | 0.6402 | 0.9016 | 243 |
| old | actual | 11-16 | C | reversal | 0.0206 | 0.0000 | 0.0588 | 243 |
| old | actual | 11-16 | C | negligible | 0.1770 | 0.0827 | 0.3198 | 243 |
| old | actual | 11-16 | C | unresolved | 0.0082 | 0.0000 | 0.0394 | 243 |
| old | actual | 11-16 | B_pm | dominance_positive | 0.7572 | 0.6147 | 0.8809 | 243 |
| old | actual | 11-16 | B_pm | reversal | 0.0165 | 0.0000 | 0.0518 | 243 |
| old | actual | 11-16 | B_pm | negligible | 0.1605 | 0.0775 | 0.2811 | 243 |
| old | actual | 11-16 | B_pm | unresolved | 0.0658 | 0.0076 | 0.1558 | 243 |
| old | actual | 11-16 | C_pm | dominance_positive | 0.7572 | 0.6147 | 0.8809 | 243 |
| old | actual | 11-16 | C_pm | reversal | 0.0165 | 0.0000 | 0.0518 | 243 |
| old | actual | 11-16 | C_pm | negligible | 0.1605 | 0.0775 | 0.2811 | 243 |
| old | actual | 11-16 | C_pm | unresolved | 0.0658 | 0.0076 | 0.1558 | 243 |
| old | actual | 17-30 | B | dominance_positive | 0.6075 | 0.3980 | 0.7743 | 586 |
| old | actual | 17-30 | B | reversal | 0.0392 | 0.0036 | 0.0926 | 586 |
| old | actual | 17-30 | B | negligible | 0.3447 | 0.2106 | 0.5145 | 586 |
| old | actual | 17-30 | B | unresolved | 0.0085 | 0.0000 | 0.0262 | 586 |
| old | actual | 17-30 | C | dominance_positive | 0.6075 | 0.3980 | 0.7743 | 586 |
| old | actual | 17-30 | C | reversal | 0.0392 | 0.0036 | 0.0926 | 586 |
| old | actual | 17-30 | C | negligible | 0.3447 | 0.2106 | 0.5145 | 586 |
| old | actual | 17-30 | C | unresolved | 0.0085 | 0.0000 | 0.0262 | 586 |
| old | actual | 17-30 | B_pm | dominance_positive | 0.5939 | 0.3780 | 0.7749 | 586 |
| old | actual | 17-30 | B_pm | reversal | 0.0273 | 0.0000 | 0.0737 | 586 |
| old | actual | 17-30 | B_pm | negligible | 0.3225 | 0.1892 | 0.4886 | 586 |
| old | actual | 17-30 | B_pm | unresolved | 0.0563 | 0.0129 | 0.1060 | 586 |
| old | actual | 17-30 | C_pm | dominance_positive | 0.5939 | 0.3780 | 0.7749 | 586 |
| old | actual | 17-30 | C_pm | reversal | 0.0273 | 0.0000 | 0.0737 | 586 |
| old | actual | 17-30 | C_pm | negligible | 0.3225 | 0.1892 | 0.4886 | 586 |
| old | actual | 17-30 | C_pm | unresolved | 0.0563 | 0.0129 | 0.1060 | 586 |
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
| old | own | 11-16 | B_pm | dominance_positive | 0.9671 | 0.9053 | 1.0000 | 243 |
| old | own | 11-16 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| old | own | 11-16 | B_pm | negligible | 0.0082 | 0.0000 | 0.0294 | 243 |
| old | own | 11-16 | B_pm | unresolved | 0.0247 | 0.0000 | 0.0717 | 243 |
| old | own | 11-16 | C_pm | dominance_positive | 0.9671 | 0.9053 | 1.0000 | 243 |
| old | own | 11-16 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| old | own | 11-16 | C_pm | negligible | 0.0082 | 0.0000 | 0.0294 | 243 |
| old | own | 11-16 | C_pm | unresolved | 0.0247 | 0.0000 | 0.0717 | 243 |
| old | own | 17-30 | B | dominance_positive | 0.9676 | 0.9147 | 1.0000 | 586 |
| old | own | 17-30 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | B | negligible | 0.0324 | 0.0000 | 0.0853 | 586 |
| old | own | 17-30 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | C | dominance_positive | 0.9676 | 0.9147 | 1.0000 | 586 |
| old | own | 17-30 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | C | negligible | 0.0324 | 0.0000 | 0.0853 | 586 |
| old | own | 17-30 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | B_pm | dominance_positive | 0.9608 | 0.9061 | 0.9982 | 586 |
| old | own | 17-30 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | B_pm | negligible | 0.0273 | 0.0000 | 0.0725 | 586 |
| old | own | 17-30 | B_pm | unresolved | 0.0119 | 0.0000 | 0.0280 | 586 |
| old | own | 17-30 | C_pm | dominance_positive | 0.9608 | 0.9061 | 0.9982 | 586 |
| old | own | 17-30 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | C_pm | negligible | 0.0273 | 0.0000 | 0.0725 | 586 |
| old | own | 17-30 | C_pm | unresolved | 0.0119 | 0.0000 | 0.0280 | 586 |
| new | actual | 1-3 | B | dominance_positive | 0.0781 | 0.0179 | 0.1533 | 128 |
| new | actual | 1-3 | B | reversal | 0.5547 | 0.2710 | 0.8029 | 128 |
| new | actual | 1-3 | B | negligible | 0.2500 | 0.0756 | 0.4841 | 128 |
| new | actual | 1-3 | B | unresolved | 0.1172 | 0.0263 | 0.2202 | 128 |
| new | actual | 1-3 | C | dominance_positive | 0.0781 | 0.0179 | 0.1533 | 128 |
| new | actual | 1-3 | C | reversal | 0.5547 | 0.2710 | 0.8029 | 128 |
| new | actual | 1-3 | C | negligible | 0.2500 | 0.0756 | 0.4841 | 128 |
| new | actual | 1-3 | C | unresolved | 0.1172 | 0.0263 | 0.2202 | 128 |
| new | actual | 1-3 | B_pm | dominance_positive | 0.0547 | 0.0071 | 0.1308 | 128 |
| new | actual | 1-3 | B_pm | reversal | 0.4609 | 0.2143 | 0.6723 | 128 |
| new | actual | 1-3 | B_pm | negligible | 0.2031 | 0.0397 | 0.4127 | 128 |
| new | actual | 1-3 | B_pm | unresolved | 0.2812 | 0.1278 | 0.4375 | 128 |
| new | actual | 1-3 | C_pm | dominance_positive | 0.0547 | 0.0071 | 0.1308 | 128 |
| new | actual | 1-3 | C_pm | reversal | 0.4609 | 0.2143 | 0.6723 | 128 |
| new | actual | 1-3 | C_pm | negligible | 0.2031 | 0.0397 | 0.4127 | 128 |
| new | actual | 1-3 | C_pm | unresolved | 0.2812 | 0.1278 | 0.4375 | 128 |
| new | actual | 4-10 | B | dominance_positive | 0.4237 | 0.2103 | 0.6626 | 295 |
| new | actual | 4-10 | B | reversal | 0.2102 | 0.1128 | 0.2815 | 295 |
| new | actual | 4-10 | B | negligible | 0.3220 | 0.1577 | 0.4777 | 295 |
| new | actual | 4-10 | B | unresolved | 0.0441 | 0.0000 | 0.1446 | 295 |
| new | actual | 4-10 | C | dominance_positive | 0.4237 | 0.2103 | 0.6626 | 295 |
| new | actual | 4-10 | C | reversal | 0.2102 | 0.1128 | 0.2815 | 295 |
| new | actual | 4-10 | C | negligible | 0.3220 | 0.1577 | 0.4777 | 295 |
| new | actual | 4-10 | C | unresolved | 0.0441 | 0.0000 | 0.1446 | 295 |
| new | actual | 4-10 | B_pm | dominance_positive | 0.3966 | 0.1474 | 0.6462 | 295 |
| new | actual | 4-10 | B_pm | reversal | 0.1797 | 0.0880 | 0.2569 | 295 |
| new | actual | 4-10 | B_pm | negligible | 0.2746 | 0.1429 | 0.3959 | 295 |
| new | actual | 4-10 | B_pm | unresolved | 0.1492 | 0.0219 | 0.3426 | 295 |
| new | actual | 4-10 | C_pm | dominance_positive | 0.3966 | 0.1474 | 0.6462 | 295 |
| new | actual | 4-10 | C_pm | reversal | 0.1797 | 0.0880 | 0.2569 | 295 |
| new | actual | 4-10 | C_pm | negligible | 0.2746 | 0.1429 | 0.3959 | 295 |
| new | actual | 4-10 | C_pm | unresolved | 0.1492 | 0.0219 | 0.3426 | 295 |
| new | actual | 11-16 | B | dominance_positive | 0.7284 | 0.5556 | 0.8734 | 243 |
| new | actual | 11-16 | B | reversal | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | actual | 11-16 | B | negligible | 0.2593 | 0.1213 | 0.4304 | 243 |
| new | actual | 11-16 | B | unresolved | 0.0082 | 0.0000 | 0.0357 | 243 |
| new | actual | 11-16 | C | dominance_positive | 0.7284 | 0.5556 | 0.8734 | 243 |
| new | actual | 11-16 | C | reversal | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | actual | 11-16 | C | negligible | 0.2593 | 0.1213 | 0.4304 | 243 |
| new | actual | 11-16 | C | unresolved | 0.0082 | 0.0000 | 0.0357 | 243 |
| new | actual | 11-16 | B_pm | dominance_positive | 0.7202 | 0.5556 | 0.8640 | 243 |
| new | actual | 11-16 | B_pm | reversal | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | actual | 11-16 | B_pm | negligible | 0.2387 | 0.1155 | 0.3891 | 243 |
| new | actual | 11-16 | B_pm | unresolved | 0.0370 | 0.0039 | 0.0860 | 243 |
| new | actual | 11-16 | C_pm | dominance_positive | 0.7202 | 0.5556 | 0.8640 | 243 |
| new | actual | 11-16 | C_pm | reversal | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | actual | 11-16 | C_pm | negligible | 0.2387 | 0.1155 | 0.3891 | 243 |
| new | actual | 11-16 | C_pm | unresolved | 0.0370 | 0.0039 | 0.0860 | 243 |
| new | actual | 17-30 | B | dominance_positive | 0.6297 | 0.4574 | 0.7909 | 586 |
| new | actual | 17-30 | B | reversal | 0.0478 | 0.0056 | 0.0935 | 586 |
| new | actual | 17-30 | B | negligible | 0.3140 | 0.1794 | 0.4717 | 586 |
| new | actual | 17-30 | B | unresolved | 0.0085 | 0.0000 | 0.0216 | 586 |
| new | actual | 17-30 | C | dominance_positive | 0.6297 | 0.4574 | 0.7909 | 586 |
| new | actual | 17-30 | C | reversal | 0.0461 | 0.0056 | 0.0903 | 586 |
| new | actual | 17-30 | C | negligible | 0.3140 | 0.1794 | 0.4717 | 586 |
| new | actual | 17-30 | C | unresolved | 0.0102 | 0.0000 | 0.0245 | 586 |
| new | actual | 17-30 | B_pm | dominance_positive | 0.6160 | 0.4459 | 0.7719 | 586 |
| new | actual | 17-30 | B_pm | reversal | 0.0375 | 0.0000 | 0.0841 | 586 |
| new | actual | 17-30 | B_pm | negligible | 0.2969 | 0.1735 | 0.4499 | 586 |
| new | actual | 17-30 | B_pm | unresolved | 0.0495 | 0.0123 | 0.0968 | 586 |
| new | actual | 17-30 | C_pm | dominance_positive | 0.6177 | 0.4459 | 0.7730 | 586 |
| new | actual | 17-30 | C_pm | reversal | 0.0375 | 0.0000 | 0.0841 | 586 |
| new | actual | 17-30 | C_pm | negligible | 0.2969 | 0.1735 | 0.4499 | 586 |
| new | actual | 17-30 | C_pm | unresolved | 0.0478 | 0.0097 | 0.0964 | 586 |
| new | own | 1-3 | B | dominance_positive | 0.0625 | 0.0000 | 0.1575 | 128 |
| new | own | 1-3 | B | reversal | 0.5703 | 0.2800 | 0.8235 | 128 |
| new | own | 1-3 | B | negligible | 0.3516 | 0.1062 | 0.6731 | 128 |
| new | own | 1-3 | B | unresolved | 0.0156 | 0.0000 | 0.0636 | 128 |
| new | own | 1-3 | C | dominance_positive | 0.0625 | 0.0000 | 0.1575 | 128 |
| new | own | 1-3 | C | reversal | 0.5703 | 0.2800 | 0.8235 | 128 |
| new | own | 1-3 | C | negligible | 0.3516 | 0.1062 | 0.6731 | 128 |
| new | own | 1-3 | C | unresolved | 0.0156 | 0.0000 | 0.0636 | 128 |
| new | own | 1-3 | B_pm | dominance_positive | 0.0469 | 0.0000 | 0.1224 | 128 |
| new | own | 1-3 | B_pm | reversal | 0.5156 | 0.2400 | 0.7838 | 128 |
| new | own | 1-3 | B_pm | negligible | 0.2891 | 0.0789 | 0.5824 | 128 |
| new | own | 1-3 | B_pm | unresolved | 0.1484 | 0.0291 | 0.2800 | 128 |
| new | own | 1-3 | C_pm | dominance_positive | 0.0469 | 0.0000 | 0.1224 | 128 |
| new | own | 1-3 | C_pm | reversal | 0.5156 | 0.2400 | 0.7838 | 128 |
| new | own | 1-3 | C_pm | negligible | 0.2891 | 0.0789 | 0.5824 | 128 |
| new | own | 1-3 | C_pm | unresolved | 0.1484 | 0.0291 | 0.2800 | 128 |
| new | own | 4-10 | B | dominance_positive | 0.4339 | 0.2078 | 0.6502 | 295 |
| new | own | 4-10 | B | reversal | 0.1932 | 0.0976 | 0.2734 | 295 |
| new | own | 4-10 | B | negligible | 0.3695 | 0.1896 | 0.5548 | 295 |
| new | own | 4-10 | B | unresolved | 0.0034 | 0.0000 | 0.0196 | 295 |
| new | own | 4-10 | C | dominance_positive | 0.4339 | 0.2078 | 0.6502 | 295 |
| new | own | 4-10 | C | reversal | 0.1932 | 0.0976 | 0.2734 | 295 |
| new | own | 4-10 | C | negligible | 0.3695 | 0.1896 | 0.5548 | 295 |
| new | own | 4-10 | C | unresolved | 0.0034 | 0.0000 | 0.0196 | 295 |
| new | own | 4-10 | B_pm | dominance_positive | 0.4441 | 0.2186 | 0.6525 | 295 |
| new | own | 4-10 | B_pm | reversal | 0.1797 | 0.0906 | 0.2509 | 295 |
| new | own | 4-10 | B_pm | negligible | 0.3458 | 0.1788 | 0.5319 | 295 |
| new | own | 4-10 | B_pm | unresolved | 0.0305 | 0.0039 | 0.0625 | 295 |
| new | own | 4-10 | C_pm | dominance_positive | 0.4441 | 0.2186 | 0.6525 | 295 |
| new | own | 4-10 | C_pm | reversal | 0.1797 | 0.0906 | 0.2509 | 295 |
| new | own | 4-10 | C_pm | negligible | 0.3458 | 0.1788 | 0.5319 | 295 |
| new | own | 4-10 | C_pm | unresolved | 0.0305 | 0.0039 | 0.0625 | 295 |
| new | own | 11-16 | B | dominance_positive | 0.9259 | 0.8042 | 1.0000 | 243 |
| new | own | 11-16 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | B | negligible | 0.0741 | 0.0000 | 0.1958 | 243 |
| new | own | 11-16 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | C | dominance_positive | 0.9259 | 0.8042 | 1.0000 | 243 |
| new | own | 11-16 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | C | negligible | 0.0741 | 0.0000 | 0.1958 | 243 |
| new | own | 11-16 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | B_pm | dominance_positive | 0.9259 | 0.8073 | 1.0000 | 243 |
| new | own | 11-16 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | B_pm | negligible | 0.0700 | 0.0000 | 0.1855 | 243 |
| new | own | 11-16 | B_pm | unresolved | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | own | 11-16 | C_pm | dominance_positive | 0.9259 | 0.8073 | 1.0000 | 243 |
| new | own | 11-16 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | C_pm | negligible | 0.0700 | 0.0000 | 0.1855 | 243 |
| new | own | 11-16 | C_pm | unresolved | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | own | 17-30 | B | dominance_positive | 0.9676 | 0.9147 | 1.0000 | 586 |
| new | own | 17-30 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | B | negligible | 0.0324 | 0.0000 | 0.0853 | 586 |
| new | own | 17-30 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | C | dominance_positive | 0.9676 | 0.9147 | 1.0000 | 586 |
| new | own | 17-30 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | C | negligible | 0.0324 | 0.0000 | 0.0853 | 586 |
| new | own | 17-30 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | B_pm | dominance_positive | 0.9608 | 0.9061 | 0.9982 | 586 |
| new | own | 17-30 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | B_pm | negligible | 0.0273 | 0.0000 | 0.0725 | 586 |
| new | own | 17-30 | B_pm | unresolved | 0.0119 | 0.0000 | 0.0280 | 586 |
| new | own | 17-30 | C_pm | dominance_positive | 0.9608 | 0.9061 | 0.9982 | 586 |
| new | own | 17-30 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | C_pm | negligible | 0.0273 | 0.0000 | 0.0725 | 586 |
| new | own | 17-30 | C_pm | unresolved | 0.0119 | 0.0000 | 0.0280 | 586 |

## T5_3_reversal_slot

| rule | portfolio | jstar | count | count_argmin_chat | count_precision_matched | n_reversals | n_reversals_pm |
|---|---|---|---|---|---|---|---|
| old | actual | 1 | 0 | 0 | 0 | 48 | 34 |
| old | actual | 2 | 0 | 0 | 0 | 48 | 34 |
| old | actual | 3 | 0 | 0 | 0 | 48 | 34 |
| old | actual | 4 | 0 | 0 | 0 | 48 | 34 |
| old | actual | 5 | 1 | 1 | 1 | 48 | 34 |
| old | actual | 6 | 0 | 0 | 0 | 48 | 34 |
| old | actual | 7 | 1 | 1 | 1 | 48 | 34 |
| old | actual | 8 | 0 | 0 | 0 | 48 | 34 |
| old | actual | 9 | 2 | 2 | 2 | 48 | 34 |
| old | actual | 10 | 2 | 2 | 0 | 48 | 34 |
| old | actual | 11 | 0 | 0 | 0 | 48 | 34 |
| old | actual | 12 | 0 | 0 | 1 | 48 | 34 |
| old | actual | 13 | 2 | 2 | 1 | 48 | 34 |
| old | actual | 14 | 2 | 3 | 1 | 48 | 34 |
| old | actual | 15 | 3 | 3 | 2 | 48 | 34 |
| old | actual | 16 | 3 | 4 | 3 | 48 | 34 |
| old | actual | 17 | 4 | 4 | 2 | 48 | 34 |
| old | actual | 18 | 4 | 3 | 1 | 48 | 34 |
| old | actual | 19 | 5 | 5 | 6 | 48 | 34 |
| old | actual | 20 | 4 | 4 | 3 | 48 | 34 |
| old | actual | 21 | 2 | 2 | 1 | 48 | 34 |
| old | actual | 22 | 1 | 1 | 1 | 48 | 34 |
| old | actual | 23 | 2 | 2 | 2 | 48 | 34 |
| old | actual | 24 | 2 | 2 | 1 | 48 | 34 |
| old | actual | 25 | 2 | 2 | 1 | 48 | 34 |
| old | actual | 26 | 2 | 2 | 2 | 48 | 34 |
| old | actual | 27 | 1 | 1 | 1 | 48 | 34 |
| old | actual | 28 | 0 | 0 | 0 | 48 | 34 |
| old | actual | 29 | 2 | 2 | 1 | 48 | 34 |
| old | actual | 30 | 1 | 0 | 0 | 48 | 34 |
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
| new | actual | 1 | 0 | 0 | 0 | 162 | 135 |
| new | actual | 2 | 0 | 0 | 0 | 162 | 135 |
| new | actual | 3 | 2 | 2 | 1 | 162 | 135 |
| new | actual | 4 | 3 | 3 | 2 | 162 | 135 |
| new | actual | 5 | 0 | 0 | 0 | 162 | 135 |
| new | actual | 6 | 0 | 0 | 0 | 162 | 135 |
| new | actual | 7 | 3 | 4 | 3 | 162 | 135 |
| new | actual | 8 | 13 | 10 | 9 | 162 | 135 |
| new | actual | 9 | 99 | 101 | 85 | 162 | 135 |
| new | actual | 10 | 0 | 0 | 0 | 162 | 135 |
| new | actual | 11 | 0 | 0 | 0 | 162 | 135 |
| new | actual | 12 | 0 | 0 | 0 | 162 | 135 |
| new | actual | 13 | 0 | 0 | 0 | 162 | 135 |
| new | actual | 14 | 0 | 0 | 0 | 162 | 135 |
| new | actual | 15 | 2 | 2 | 2 | 162 | 135 |
| new | actual | 16 | 1 | 1 | 1 | 162 | 135 |
| new | actual | 17 | 2 | 2 | 2 | 162 | 135 |
| new | actual | 18 | 2 | 2 | 2 | 162 | 135 |
| new | actual | 19 | 6 | 6 | 6 | 162 | 135 |
| new | actual | 20 | 4 | 4 | 3 | 162 | 135 |
| new | actual | 21 | 2 | 2 | 1 | 162 | 135 |
| new | actual | 22 | 1 | 1 | 1 | 162 | 135 |
| new | actual | 23 | 4 | 4 | 4 | 162 | 135 |
| new | actual | 24 | 2 | 2 | 1 | 162 | 135 |
| new | actual | 25 | 2 | 2 | 3 | 162 | 135 |
| new | actual | 26 | 3 | 3 | 2 | 162 | 135 |
| new | actual | 27 | 3 | 3 | 2 | 162 | 135 |
| new | actual | 28 | 0 | 0 | 0 | 162 | 135 |
| new | actual | 29 | 3 | 3 | 2 | 162 | 135 |
| new | actual | 30 | 5 | 5 | 3 | 162 | 135 |
| new | own | 1 | 0 | 0 | 0 | 130 | 119 |
| new | own | 2 | 0 | 0 | 0 | 130 | 119 |
| new | own | 3 | 0 | 0 | 0 | 130 | 119 |
| new | own | 4 | 0 | 0 | 0 | 130 | 119 |
| new | own | 5 | 0 | 0 | 0 | 130 | 119 |
| new | own | 6 | 0 | 0 | 0 | 130 | 119 |
| new | own | 7 | 0 | 0 | 0 | 130 | 119 |
| new | own | 8 | 0 | 0 | 0 | 130 | 119 |
| new | own | 9 | 130 | 130 | 119 | 130 | 119 |
| new | own | 10 | 0 | 0 | 0 | 130 | 119 |
| new | own | 11 | 0 | 0 | 0 | 130 | 119 |
| new | own | 12 | 0 | 0 | 0 | 130 | 119 |
| new | own | 13 | 0 | 0 | 0 | 130 | 119 |
| new | own | 14 | 0 | 0 | 0 | 130 | 119 |
| new | own | 15 | 0 | 0 | 0 | 130 | 119 |
| new | own | 16 | 0 | 0 | 0 | 130 | 119 |
| new | own | 17 | 0 | 0 | 0 | 130 | 119 |
| new | own | 18 | 0 | 0 | 0 | 130 | 119 |
| new | own | 19 | 0 | 0 | 0 | 130 | 119 |
| new | own | 20 | 0 | 0 | 0 | 130 | 119 |
| new | own | 21 | 0 | 0 | 0 | 130 | 119 |
| new | own | 22 | 0 | 0 | 0 | 130 | 119 |
| new | own | 23 | 0 | 0 | 0 | 130 | 119 |
| new | own | 24 | 0 | 0 | 0 | 130 | 119 |
| new | own | 25 | 0 | 0 | 0 | 130 | 119 |
| new | own | 26 | 0 | 0 | 0 | 130 | 119 |
| new | own | 27 | 0 | 0 | 0 | 130 | 119 |
| new | own | 28 | 0 | 0 | 0 | 130 | 119 |
| new | own | 29 | 0 | 0 | 0 | 130 | 119 |
| new | own | 30 | 0 | 0 | 0 | 130 | 119 |

## F5_1_profiles

720 rows in `F5_1_profiles.csv`.

## T5_curves_and_T5_6_delta

| rule | portfolio | band | curve | n | mean | q25 | median | q75 | q90 | share_sig_pos | pos_lo99 | pos_hi99 | share_sig_neg | neg_lo99 | neg_hi99 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| old | actual | all | linear | 1252 | 0.0175 | 0.0007 | 0.0102 | 0.0296 | 0.0420 | 0.6693 | 0.5332 | 0.8003 | 0.0176 | 0.0026 | 0.0368 |
| old | actual | all | concave | 1252 | 0.0163 | 0.0006 | 0.0088 | 0.0279 | 0.0389 | 0.6342 | 0.4911 | 0.7736 | 0.0184 | 0.0042 | 0.0368 |
| old | actual | all | convex | 1252 | 0.0160 | 0.0005 | 0.0090 | 0.0277 | 0.0409 | 0.6749 | 0.5659 | 0.7691 | 0.0120 | 0.0009 | 0.0262 |
| old | actual | all | top3_stress | 1252 | 0.0068 | 0.0000 | 0.0009 | 0.0110 | 0.0229 | 0.4145 | 0.3592 | 0.4872 | 0.0016 | 0.0000 | 0.0066 |
| old | actual | 1-3 | linear | 128 | 0.0029 | 0.0018 | 0.0027 | 0.0053 | 0.0076 | 0.4531 | 0.1964 | 0.6970 | 0.0156 | 0.0000 | 0.0580 |
| old | actual | 1-3 | concave | 128 | 0.0015 | 0.0010 | 0.0015 | 0.0029 | 0.0044 | 0.2891 | 0.0935 | 0.5310 | 0.0234 | 0.0000 | 0.0682 |
| old | actual | 1-3 | convex | 128 | 0.0051 | 0.0030 | 0.0042 | 0.0074 | 0.0109 | 0.7656 | 0.6418 | 0.8800 | 0.0156 | 0.0000 | 0.0580 |
| old | actual | 1-3 | top3_stress | 128 | 0.0043 | 0.0003 | 0.0013 | 0.0055 | 0.0121 | 0.3672 | 0.1587 | 0.6053 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 4-10 | linear | 295 | 0.0179 | 0.0055 | 0.0140 | 0.0265 | 0.0376 | 0.8475 | 0.7209 | 0.9561 | 0.0271 | 0.0000 | 0.0736 |
| old | actual | 4-10 | concave | 295 | 0.0137 | 0.0032 | 0.0089 | 0.0178 | 0.0346 | 0.7627 | 0.5793 | 0.9371 | 0.0305 | 0.0000 | 0.0836 |
| old | actual | 4-10 | convex | 295 | 0.0229 | 0.0090 | 0.0195 | 0.0361 | 0.0458 | 0.8746 | 0.7635 | 0.9654 | 0.0102 | 0.0000 | 0.0308 |
| old | actual | 4-10 | top3_stress | 295 | 0.0183 | 0.0096 | 0.0168 | 0.0276 | 0.0338 | 0.8712 | 0.7689 | 0.9599 | 0.0034 | 0.0000 | 0.0193 |
| old | actual | 11-16 | linear | 243 | 0.0280 | 0.0079 | 0.0267 | 0.0374 | 0.0523 | 0.8107 | 0.6548 | 0.9153 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 11-16 | concave | 243 | 0.0225 | 0.0064 | 0.0183 | 0.0280 | 0.0399 | 0.8066 | 0.6535 | 0.9109 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 11-16 | convex | 243 | 0.0294 | 0.0080 | 0.0299 | 0.0414 | 0.0602 | 0.7984 | 0.6429 | 0.9098 | 0.0041 | 0.0000 | 0.0262 |
| old | actual | 11-16 | top3_stress | 243 | 0.0091 | 0.0020 | 0.0065 | 0.0144 | 0.0211 | 0.7160 | 0.5826 | 0.8523 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 17-30 | linear | 586 | 0.0162 | 0.0000 | 0.0074 | 0.0298 | 0.0415 | 0.5683 | 0.3345 | 0.7542 | 0.0205 | 0.0000 | 0.0566 |
| old | actual | 17-30 | concave | 586 | 0.0184 | 0.0000 | 0.0117 | 0.0323 | 0.0425 | 0.5734 | 0.3387 | 0.7605 | 0.0188 | 0.0000 | 0.0564 |
| old | actual | 17-30 | convex | 586 | 0.0094 | 0.0000 | 0.0029 | 0.0158 | 0.0287 | 0.5034 | 0.3153 | 0.6520 | 0.0154 | 0.0000 | 0.0401 |
| old | actual | 17-30 | top3_stress | 586 | 0.0006 | 0.0000 | 0.0000 | 0.0003 | 0.0018 | 0.0700 | 0.0315 | 0.1139 | 0.0017 | 0.0000 | 0.0105 |
| old | own | all | linear | 1252 | 0.0240 | 0.0082 | 0.0238 | 0.0352 | 0.0457 | 0.8802 | 0.8086 | 0.9419 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | concave | 1252 | 0.0211 | 0.0061 | 0.0210 | 0.0318 | 0.0396 | 0.8490 | 0.7703 | 0.9268 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | convex | 1252 | 0.0218 | 0.0062 | 0.0188 | 0.0329 | 0.0442 | 0.8642 | 0.8119 | 0.9081 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | top3_stress | 1252 | 0.0077 | 0.0000 | 0.0026 | 0.0129 | 0.0238 | 0.4872 | 0.4264 | 0.5477 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | linear | 128 | 0.0033 | 0.0018 | 0.0024 | 0.0040 | 0.0061 | 0.3438 | 0.0984 | 0.6350 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | concave | 128 | 0.0018 | 0.0010 | 0.0013 | 0.0022 | 0.0033 | 0.1953 | 0.0164 | 0.4407 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | convex | 128 | 0.0055 | 0.0031 | 0.0041 | 0.0068 | 0.0103 | 0.7812 | 0.5929 | 0.9298 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | top3_stress | 128 | 0.0044 | 0.0002 | 0.0013 | 0.0057 | 0.0129 | 0.3750 | 0.1587 | 0.6271 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | linear | 295 | 0.0162 | 0.0071 | 0.0124 | 0.0246 | 0.0321 | 0.9220 | 0.8201 | 0.9898 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | concave | 295 | 0.0095 | 0.0039 | 0.0069 | 0.0144 | 0.0191 | 0.8339 | 0.6794 | 0.9732 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | convex | 295 | 0.0239 | 0.0114 | 0.0191 | 0.0363 | 0.0458 | 0.9492 | 0.8557 | 0.9965 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | top3_stress | 295 | 0.0196 | 0.0112 | 0.0179 | 0.0276 | 0.0336 | 0.9525 | 0.8669 | 0.9966 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | linear | 243 | 0.0329 | 0.0223 | 0.0306 | 0.0399 | 0.0550 | 0.9918 | 0.9706 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | concave | 243 | 0.0222 | 0.0146 | 0.0207 | 0.0277 | 0.0370 | 0.9794 | 0.9388 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | convex | 243 | 0.0377 | 0.0267 | 0.0343 | 0.0445 | 0.0660 | 0.9918 | 0.9706 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | top3_stress | 243 | 0.0113 | 0.0053 | 0.0084 | 0.0163 | 0.0226 | 0.9095 | 0.7653 | 0.9920 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | linear | 586 | 0.0288 | 0.0172 | 0.0290 | 0.0386 | 0.0482 | 0.9300 | 0.8617 | 0.9916 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | concave | 586 | 0.0307 | 0.0240 | 0.0309 | 0.0373 | 0.0448 | 0.9454 | 0.8912 | 0.9944 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | convex | 586 | 0.0176 | 0.0046 | 0.0148 | 0.0277 | 0.0368 | 0.7867 | 0.7155 | 0.8584 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | top3_stress | 586 | 0.0009 | 0.0000 | 0.0000 | 0.0008 | 0.0029 | 0.1024 | 0.0412 | 0.1843 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | all | linear | 1252 | 0.0159 | 0.0000 | 0.0038 | 0.0291 | 0.0452 | 0.5152 | 0.3833 | 0.6352 | 0.0647 | 0.0203 | 0.1116 |
| new | actual | all | concave | 1252 | 0.0154 | 0.0000 | 0.0039 | 0.0290 | 0.0410 | 0.5272 | 0.4005 | 0.6323 | 0.0407 | 0.0142 | 0.0687 |
| new | actual | all | convex | 1252 | 0.0135 | 0.0000 | 0.0019 | 0.0217 | 0.0432 | 0.4824 | 0.3683 | 0.6006 | 0.0767 | 0.0315 | 0.1186 |
| new | actual | all | top3_stress | 1252 | 0.0048 | 0.0000 | 0.0000 | 0.0071 | 0.0211 | 0.3283 | 0.2427 | 0.4220 | 0.0974 | 0.0455 | 0.1390 |
| new | actual | 1-3 | linear | 128 | -0.0029 | -0.0032 | -0.0003 | 0.0002 | 0.0018 | 0.0781 | 0.0081 | 0.1605 | 0.2969 | 0.0556 | 0.5825 |
| new | actual | 1-3 | concave | 128 | -0.0018 | -0.0017 | -0.0002 | 0.0002 | 0.0038 | 0.1406 | 0.0000 | 0.3421 | 0.1641 | 0.0348 | 0.3115 |
| new | actual | 1-3 | convex | 128 | -0.0042 | -0.0062 | -0.0012 | -0.0001 | 0.0006 | 0.0781 | 0.0081 | 0.1630 | 0.3828 | 0.1695 | 0.6159 |
| new | actual | 1-3 | top3_stress | 128 | -0.0059 | -0.0101 | -0.0029 | -0.0002 | 0.0000 | 0.0156 | 0.0000 | 0.0630 | 0.5391 | 0.2478 | 0.8000 |
| new | actual | 4-10 | linear | 295 | 0.0046 | 0.0000 | 0.0007 | 0.0068 | 0.0167 | 0.3458 | 0.1490 | 0.5512 | 0.1119 | 0.0439 | 0.1941 |
| new | actual | 4-10 | concave | 295 | 0.0045 | 0.0000 | 0.0007 | 0.0055 | 0.0151 | 0.3797 | 0.2097 | 0.5577 | 0.0678 | 0.0197 | 0.1434 |
| new | actual | 4-10 | convex | 295 | 0.0045 | -0.0002 | 0.0003 | 0.0075 | 0.0191 | 0.3492 | 0.1579 | 0.5724 | 0.1458 | 0.0560 | 0.2255 |
| new | actual | 4-10 | top3_stress | 295 | 0.0023 | -0.0001 | 0.0000 | 0.0066 | 0.0134 | 0.3288 | 0.1349 | 0.5526 | 0.1695 | 0.0732 | 0.2475 |
| new | actual | 11-16 | linear | 243 | 0.0270 | 0.0004 | 0.0222 | 0.0402 | 0.0555 | 0.7202 | 0.5420 | 0.8696 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 11-16 | concave | 243 | 0.0207 | 0.0003 | 0.0166 | 0.0294 | 0.0428 | 0.6955 | 0.5045 | 0.8577 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 11-16 | convex | 243 | 0.0305 | 0.0004 | 0.0266 | 0.0437 | 0.0619 | 0.7078 | 0.5153 | 0.8609 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 11-16 | top3_stress | 243 | 0.0164 | 0.0003 | 0.0138 | 0.0234 | 0.0336 | 0.6831 | 0.4961 | 0.8389 | 0.0041 | 0.0000 | 0.0260 |
| new | actual | 17-30 | linear | 586 | 0.0210 | 0.0000 | 0.0151 | 0.0360 | 0.0506 | 0.6109 | 0.4007 | 0.7858 | 0.0171 | 0.0000 | 0.0549 |
| new | actual | 17-30 | concave | 586 | 0.0226 | 0.0000 | 0.0208 | 0.0362 | 0.0520 | 0.6160 | 0.4105 | 0.7848 | 0.0171 | 0.0000 | 0.0549 |
| new | actual | 17-30 | convex | 586 | 0.0149 | 0.0000 | 0.0049 | 0.0237 | 0.0431 | 0.5444 | 0.3706 | 0.6841 | 0.0068 | 0.0000 | 0.0285 |
| new | actual | 17-30 | top3_stress | 586 | 0.0036 | 0.0000 | 0.0000 | 0.0027 | 0.0133 | 0.2491 | 0.1667 | 0.3658 | 0.0034 | 0.0000 | 0.0140 |
| new | own | all | linear | 1252 | 0.0233 | 0.0003 | 0.0166 | 0.0397 | 0.0543 | 0.6909 | 0.6147 | 0.7827 | 0.0447 | 0.0155 | 0.0747 |
| new | own | all | concave | 1252 | 0.0207 | 0.0002 | 0.0207 | 0.0347 | 0.0444 | 0.6781 | 0.6043 | 0.7734 | 0.0064 | 0.0000 | 0.0194 |
| new | own | all | convex | 1252 | 0.0207 | 0.0001 | 0.0101 | 0.0343 | 0.0567 | 0.6326 | 0.5626 | 0.7110 | 0.0679 | 0.0293 | 0.0988 |
| new | own | all | top3_stress | 1252 | 0.0072 | 0.0000 | 0.0006 | 0.0122 | 0.0245 | 0.4257 | 0.3361 | 0.5234 | 0.0903 | 0.0416 | 0.1308 |
| new | own | 1-3 | linear | 128 | -0.0016 | -0.0028 | -0.0008 | -0.0001 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.2500 | 0.0522 | 0.5039 |
| new | own | 1-3 | concave | 128 | -0.0008 | -0.0014 | -0.0004 | -0.0001 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0391 | 0.0000 | 0.1267 |
| new | own | 1-3 | convex | 128 | -0.0031 | -0.0052 | -0.0015 | -0.0002 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.3594 | 0.1583 | 0.5798 |
| new | own | 1-3 | top3_stress | 128 | -0.0057 | -0.0097 | -0.0026 | -0.0002 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.5000 | 0.2358 | 0.7652 |
| new | own | 4-10 | linear | 295 | 0.0037 | -0.0000 | 0.0003 | 0.0059 | 0.0125 | 0.3390 | 0.1569 | 0.5415 | 0.0814 | 0.0278 | 0.1342 |
| new | own | 4-10 | concave | 295 | 0.0023 | -0.0000 | 0.0002 | 0.0036 | 0.0074 | 0.2847 | 0.0989 | 0.5074 | 0.0102 | 0.0000 | 0.0343 |
| new | own | 4-10 | convex | 295 | 0.0047 | -0.0000 | 0.0004 | 0.0084 | 0.0177 | 0.3729 | 0.1739 | 0.5840 | 0.1322 | 0.0560 | 0.1954 |
| new | own | 4-10 | top3_stress | 295 | 0.0028 | -0.0000 | 0.0001 | 0.0073 | 0.0139 | 0.3559 | 0.1691 | 0.5520 | 0.1661 | 0.0725 | 0.2444 |
| new | own | 11-16 | linear | 243 | 0.0344 | 0.0131 | 0.0334 | 0.0465 | 0.0650 | 0.9053 | 0.7640 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | concave | 243 | 0.0226 | 0.0083 | 0.0218 | 0.0314 | 0.0440 | 0.8683 | 0.7248 | 0.9751 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | convex | 243 | 0.0421 | 0.0171 | 0.0396 | 0.0549 | 0.0800 | 0.9095 | 0.7714 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | top3_stress | 243 | 0.0224 | 0.0112 | 0.0191 | 0.0284 | 0.0455 | 0.8765 | 0.7471 | 0.9727 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | linear | 586 | 0.0341 | 0.0165 | 0.0312 | 0.0452 | 0.0625 | 0.9300 | 0.8617 | 0.9916 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | concave | 586 | 0.0339 | 0.0251 | 0.0333 | 0.0410 | 0.0523 | 0.9454 | 0.8912 | 0.9944 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | convex | 586 | 0.0251 | 0.0046 | 0.0161 | 0.0374 | 0.0600 | 0.7867 | 0.7155 | 0.8584 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | top3_stress | 586 | 0.0059 | 0.0000 | 0.0002 | 0.0071 | 0.0205 | 0.3669 | 0.2633 | 0.4833 | 0.0000 | 0.0000 | 0.0000 |
| delta | actual | all | linear | 1252 | -0.0016 | -0.0069 | 0.0000 | 0.0011 | 0.0109 | 0.2228 | 0.1709 | 0.2930 | 0.3307 | 0.2473 | 0.4035 |
| delta | actual | all | concave | 1252 | -0.0009 | -0.0043 | 0.0000 | 0.0012 | 0.0088 | 0.2005 | 0.1536 | 0.2608 | 0.2995 | 0.2104 | 0.3966 |
| delta | actual | all | convex | 1252 | -0.0025 | -0.0109 | 0.0000 | 0.0016 | 0.0138 | 0.2380 | 0.1864 | 0.3021 | 0.3650 | 0.3191 | 0.4077 |
| delta | actual | all | top3_stress | 1252 | -0.0020 | -0.0069 | 0.0000 | 0.0011 | 0.0119 | 0.2188 | 0.1603 | 0.2890 | 0.2915 | 0.2357 | 0.3468 |
| delta | actual | 1-3 | linear | 128 | -0.0058 | -0.0079 | -0.0026 | -0.0014 | -0.0005 | 0.0234 | 0.0000 | 0.0813 | 0.4766 | 0.1393 | 0.7656 |
| delta | actual | 1-3 | concave | 128 | -0.0033 | -0.0047 | -0.0015 | -0.0004 | 0.0014 | 0.0391 | 0.0000 | 0.1301 | 0.3516 | 0.0574 | 0.6504 |
| delta | actual | 1-3 | convex | 128 | -0.0093 | -0.0145 | -0.0049 | -0.0030 | -0.0014 | 0.0078 | 0.0000 | 0.0473 | 0.7969 | 0.6587 | 0.9179 |
| delta | actual | 1-3 | top3_stress | 128 | -0.0103 | -0.0164 | -0.0039 | -0.0005 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.5312 | 0.2389 | 0.8000 |
| delta | actual | 4-10 | linear | 295 | -0.0133 | -0.0204 | -0.0118 | -0.0053 | 0.0000 | 0.0237 | 0.0000 | 0.0709 | 0.8102 | 0.6551 | 0.9446 |
| delta | actual | 4-10 | concave | 295 | -0.0091 | -0.0134 | -0.0068 | -0.0026 | 0.0000 | 0.0508 | 0.0000 | 0.1359 | 0.7424 | 0.5633 | 0.9290 |
| delta | actual | 4-10 | convex | 295 | -0.0184 | -0.0271 | -0.0176 | -0.0101 | 0.0000 | 0.0169 | 0.0000 | 0.0498 | 0.8576 | 0.7516 | 0.9512 |
| delta | actual | 4-10 | top3_stress | 295 | -0.0160 | -0.0215 | -0.0155 | -0.0089 | 0.0000 | 0.0136 | 0.0000 | 0.0568 | 0.8508 | 0.7413 | 0.9498 |
| delta | actual | 11-16 | linear | 243 | -0.0010 | -0.0106 | 0.0000 | 0.0068 | 0.0189 | 0.3745 | 0.2358 | 0.5085 | 0.3909 | 0.2036 | 0.5447 |
| delta | actual | 11-16 | concave | 243 | -0.0018 | -0.0075 | 0.0000 | 0.0038 | 0.0125 | 0.2963 | 0.1745 | 0.4103 | 0.3663 | 0.1516 | 0.5353 |
| delta | actual | 11-16 | convex | 243 | 0.0011 | -0.0107 | 0.0000 | 0.0108 | 0.0223 | 0.4156 | 0.2906 | 0.5430 | 0.3580 | 0.1927 | 0.4921 |
| delta | actual | 11-16 | top3_stress | 243 | 0.0073 | 0.0000 | 0.0036 | 0.0132 | 0.0212 | 0.5309 | 0.3865 | 0.6654 | 0.1646 | 0.0724 | 0.2540 |
| delta | actual | 17-30 | linear | 586 | 0.0049 | 0.0000 | 0.0000 | 0.0041 | 0.0174 | 0.3038 | 0.2112 | 0.4223 | 0.0324 | 0.0035 | 0.0703 |
| delta | actual | 17-30 | concave | 586 | 0.0042 | 0.0000 | 0.0000 | 0.0030 | 0.0150 | 0.2713 | 0.1936 | 0.3613 | 0.0375 | 0.0036 | 0.0775 |
| delta | actual | 17-30 | convex | 586 | 0.0055 | 0.0000 | 0.0000 | 0.0058 | 0.0190 | 0.3259 | 0.2306 | 0.4466 | 0.0256 | 0.0033 | 0.0570 |
| delta | actual | 17-30 | top3_stress | 586 | 0.0030 | 0.0000 | 0.0000 | 0.0025 | 0.0109 | 0.2406 | 0.1646 | 0.3515 | 0.0102 | 0.0000 | 0.0267 |
| delta | own | all | linear | 1252 | -0.0007 | -0.0078 | 0.0000 | 0.0037 | 0.0140 | 0.2859 | 0.2378 | 0.3336 | 0.3730 | 0.3274 | 0.4153 |
| delta | own | all | concave | 1252 | -0.0004 | -0.0045 | 0.0000 | 0.0021 | 0.0081 | 0.2372 | 0.1994 | 0.2720 | 0.3211 | 0.2663 | 0.3780 |
| delta | own | all | convex | 1252 | -0.0010 | -0.0118 | 0.0000 | 0.0063 | 0.0202 | 0.3091 | 0.2643 | 0.3518 | 0.3970 | 0.3554 | 0.4339 |
| delta | own | all | top3_stress | 1252 | -0.0005 | -0.0084 | 0.0000 | 0.0054 | 0.0172 | 0.3051 | 0.2314 | 0.3730 | 0.3107 | 0.2463 | 0.3639 |
| delta | own | 1-3 | linear | 128 | -0.0049 | -0.0066 | -0.0033 | -0.0020 | -0.0015 | 0.0000 | 0.0000 | 0.0000 | 0.5391 | 0.2479 | 0.8080 |
| delta | own | 1-3 | concave | 128 | -0.0026 | -0.0034 | -0.0018 | -0.0011 | -0.0008 | 0.0000 | 0.0000 | 0.0000 | 0.2734 | 0.0702 | 0.5221 |
| delta | own | 1-3 | convex | 128 | -0.0086 | -0.0116 | -0.0057 | -0.0035 | -0.0025 | 0.0000 | 0.0000 | 0.0000 | 0.8438 | 0.6807 | 0.9655 |
| delta | own | 1-3 | top3_stress | 128 | -0.0101 | -0.0167 | -0.0039 | -0.0005 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.5469 | 0.2524 | 0.8130 |
| delta | own | 4-10 | linear | 295 | -0.0125 | -0.0175 | -0.0109 | -0.0074 | -0.0044 | 0.0000 | 0.0000 | 0.0000 | 0.9356 | 0.8393 | 0.9914 |
| delta | own | 4-10 | concave | 295 | -0.0072 | -0.0102 | -0.0060 | -0.0042 | -0.0024 | 0.0000 | 0.0000 | 0.0000 | 0.8780 | 0.7492 | 0.9786 |
| delta | own | 4-10 | convex | 295 | -0.0192 | -0.0261 | -0.0176 | -0.0118 | -0.0075 | 0.0000 | 0.0000 | 0.0000 | 0.9424 | 0.8423 | 0.9926 |
| delta | own | 4-10 | top3_stress | 295 | -0.0168 | -0.0217 | -0.0164 | -0.0103 | -0.0047 | 0.0136 | 0.0000 | 0.0470 | 0.9220 | 0.7932 | 0.9908 |
| delta | own | 11-16 | linear | 243 | 0.0015 | -0.0104 | 0.0025 | 0.0094 | 0.0188 | 0.5144 | 0.3622 | 0.7198 | 0.4115 | 0.2277 | 0.5377 |
| delta | own | 11-16 | concave | 243 | 0.0004 | -0.0070 | 0.0010 | 0.0052 | 0.0107 | 0.4033 | 0.2766 | 0.5333 | 0.3786 | 0.1681 | 0.5236 |
| delta | own | 11-16 | convex | 243 | 0.0044 | -0.0116 | 0.0051 | 0.0162 | 0.0290 | 0.5638 | 0.4292 | 0.7583 | 0.3951 | 0.2180 | 0.5238 |
| delta | own | 11-16 | top3_stress | 243 | 0.0111 | 0.0000 | 0.0097 | 0.0179 | 0.0279 | 0.6955 | 0.5433 | 0.8469 | 0.1811 | 0.0632 | 0.3108 |
| delta | own | 17-30 | linear | 586 | 0.0053 | 0.0000 | 0.0002 | 0.0082 | 0.0175 | 0.3976 | 0.3240 | 0.4798 | 0.0375 | 0.0032 | 0.0932 |
| delta | own | 17-30 | concave | 586 | 0.0032 | 0.0000 | 0.0001 | 0.0051 | 0.0101 | 0.3396 | 0.2649 | 0.4195 | 0.0273 | 0.0034 | 0.0612 |
| delta | own | 17-30 | convex | 586 | 0.0075 | 0.0000 | 0.0004 | 0.0107 | 0.0240 | 0.4266 | 0.3508 | 0.5089 | 0.0256 | 0.0020 | 0.0619 |
| delta | own | 17-30 | top3_stress | 586 | 0.0049 | 0.0000 | 0.0002 | 0.0064 | 0.0171 | 0.3567 | 0.2540 | 0.4715 | 0.0051 | 0.0000 | 0.0181 |

## H1

| n_team_games | share_neg_new | share_neg_old | diff_new_minus_old | diff_lo99 | diff_hi99 | n_new_reversals | crossing_share | crossing_lo99 | crossing_hi99 | supported |
|---|---|---|---|---|---|---|---|---|---|---|
| 163 | 0.3252 | 0.0000 | 0.3252 | 0.1180 | 0.5528 | 110 | 1.0000 | 1.0000 | 1.0000 | True |

## T5_attr_portfolio_effect

| rule | band | n | mean | q25 | median | q75 | q90 | share_nonzero |
|---|---|---|---|---|---|---|---|---|
| old | all | 1252 | -0.0065 | -0.0132 | 0.0000 | 0.0000 | 0.0020 | 0.4241 |
| old | 1-3 | 128 | -0.0004 | -0.0000 | 0.0000 | 0.0000 | 0.0016 | 0.0859 |
| old | 4-10 | 295 | 0.0017 | -0.0000 | 0.0000 | 0.0022 | 0.0135 | 0.3661 |
| old | 11-16 | 243 | -0.0050 | -0.0157 | 0.0000 | 0.0000 | 0.0015 | 0.4239 |
| old | 17-30 | 586 | -0.0126 | -0.0252 | -0.0036 | 0.0000 | 0.0000 | 0.5273 |
| new | all | 1252 | -0.0075 | -0.0098 | 0.0000 | 0.0000 | 0.0032 | 0.4321 |
| new | 1-3 | 128 | -0.0012 | -0.0001 | 0.0000 | 0.0005 | 0.0037 | 0.2266 |
| new | 4-10 | 295 | 0.0009 | 0.0000 | 0.0000 | 0.0015 | 0.0063 | 0.2983 |
| new | 11-16 | 243 | -0.0075 | -0.0087 | 0.0000 | 0.0000 | 0.0044 | 0.3951 |
| new | 17-30 | 586 | -0.0131 | -0.0220 | -0.0036 | 0.0000 | 0.0000 | 0.5597 |
| delta | all | 1252 | -0.0010 | -0.0002 | 0.0000 | 0.0001 | 0.0052 | 0.3043 |
| delta | 1-3 | 128 | -0.0008 | -0.0001 | 0.0000 | 0.0004 | 0.0029 | 0.1797 |
| delta | 4-10 | 295 | -0.0008 | -0.0005 | 0.0000 | 0.0001 | 0.0063 | 0.3492 |
| delta | 11-16 | 243 | -0.0025 | -0.0019 | 0.0000 | 0.0000 | 0.0072 | 0.3704 |
| delta | 17-30 | 586 | -0.0005 | -0.0000 | 0.0000 | 0.0000 | 0.0050 | 0.2816 |

## T5_7_rollover

| rule | portfolio | band | curve | rho | measure | n | mean | q25 | median | q75 | q90 | share_sign_flip | vbar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| old | actual | all | - | 0.0000 | M | 1252 | 0.0061 | -0.0000 | 0.0000 | 0.0000 | 0.0143 |  |  |
| old | actual | all | linear | 0.0000 | tau | 1252 | 0.0175 | 0.0007 | 0.0102 | 0.0296 | 0.0420 | 0.0000 | 0.5000 |
| old | actual | all | linear | 0.5000 | tau | 1252 | 0.0160 | 0.0007 | 0.0097 | 0.0278 | 0.0401 | 0.0016 | 0.5000 |
| old | actual | all | linear | 0.8000 | tau | 1252 | 0.0151 | 0.0006 | 0.0088 | 0.0266 | 0.0391 | 0.0040 | 0.5000 |
| old | actual | all | concave | 0.0000 | tau | 1252 | 0.0163 | 0.0006 | 0.0088 | 0.0279 | 0.0389 | 0.0000 | 0.6599 |
| old | actual | all | concave | 0.5000 | tau | 1252 | 0.0143 | 0.0006 | 0.0077 | 0.0253 | 0.0364 | 0.0072 | 0.6599 |
| old | actual | all | concave | 0.8000 | tau | 1252 | 0.0131 | 0.0006 | 0.0069 | 0.0231 | 0.0354 | 0.0104 | 0.6599 |
| old | actual | all | convex | 0.0000 | tau | 1252 | 0.0160 | 0.0005 | 0.0090 | 0.0277 | 0.0409 | 0.0000 | 0.3391 |
| old | actual | all | convex | 0.5000 | tau | 1252 | 0.0150 | 0.0004 | 0.0081 | 0.0263 | 0.0397 | 0.0024 | 0.3391 |
| old | actual | all | convex | 0.8000 | tau | 1252 | 0.0144 | 0.0003 | 0.0076 | 0.0251 | 0.0385 | 0.0064 | 0.3391 |
| old | actual | all | top3_stress | 0.0000 | tau | 1252 | 0.0068 | 0.0000 | 0.0009 | 0.0110 | 0.0229 | 0.0000 | 0.1000 |
| old | actual | all | top3_stress | 0.5000 | tau | 1252 | 0.0065 | 0.0000 | 0.0005 | 0.0105 | 0.0222 | 0.1118 | 0.1000 |
| old | actual | all | top3_stress | 0.8000 | tau | 1252 | 0.0063 | 0.0000 | 0.0005 | 0.0104 | 0.0220 | 0.1166 | 0.1000 |
| old | actual | 1-3 | - | 0.0000 | M | 128 | -0.0001 | -0.0000 | 0.0000 | 0.0000 | 0.0001 |  |  |
| old | actual | 1-3 | linear | 0.0000 | tau | 128 | 0.0029 | 0.0018 | 0.0027 | 0.0053 | 0.0076 | 0.0000 | 0.5000 |
| old | actual | 1-3 | linear | 0.5000 | tau | 128 | 0.0029 | 0.0018 | 0.0027 | 0.0053 | 0.0076 | 0.0000 | 0.5000 |
| old | actual | 1-3 | linear | 0.8000 | tau | 128 | 0.0029 | 0.0018 | 0.0027 | 0.0053 | 0.0076 | 0.0000 | 0.5000 |
| old | actual | 1-3 | concave | 0.0000 | tau | 128 | 0.0015 | 0.0010 | 0.0015 | 0.0029 | 0.0044 | 0.0000 | 0.6599 |
| old | actual | 1-3 | concave | 0.5000 | tau | 128 | 0.0015 | 0.0010 | 0.0015 | 0.0029 | 0.0043 | 0.0156 | 0.6599 |
| old | actual | 1-3 | concave | 0.8000 | tau | 128 | 0.0016 | 0.0010 | 0.0015 | 0.0029 | 0.0045 | 0.0234 | 0.6599 |
| old | actual | 1-3 | convex | 0.0000 | tau | 128 | 0.0051 | 0.0030 | 0.0042 | 0.0074 | 0.0109 | 0.0000 | 0.3391 |
| old | actual | 1-3 | convex | 0.5000 | tau | 128 | 0.0051 | 0.0030 | 0.0043 | 0.0076 | 0.0104 | 0.0000 | 0.3391 |
| old | actual | 1-3 | convex | 0.8000 | tau | 128 | 0.0051 | 0.0030 | 0.0043 | 0.0076 | 0.0110 | 0.0000 | 0.3391 |
| old | actual | 1-3 | top3_stress | 0.0000 | tau | 128 | 0.0043 | 0.0003 | 0.0013 | 0.0055 | 0.0121 | 0.0000 | 0.1000 |
| old | actual | 1-3 | top3_stress | 0.5000 | tau | 128 | 0.0043 | 0.0003 | 0.0013 | 0.0055 | 0.0121 | 0.0156 | 0.1000 |
| old | actual | 1-3 | top3_stress | 0.8000 | tau | 128 | 0.0043 | 0.0003 | 0.0013 | 0.0055 | 0.0121 | 0.0156 | 0.1000 |
| old | actual | 4-10 | - | 0.0000 | M | 295 | 0.0076 | -0.0000 | 0.0000 | 0.0012 | 0.0347 |  |  |
| old | actual | 4-10 | linear | 0.0000 | tau | 295 | 0.0179 | 0.0055 | 0.0140 | 0.0265 | 0.0376 | 0.0000 | 0.5000 |
| old | actual | 4-10 | linear | 0.5000 | tau | 295 | 0.0160 | 0.0056 | 0.0132 | 0.0250 | 0.0331 | 0.0034 | 0.5000 |
| old | actual | 4-10 | linear | 0.8000 | tau | 295 | 0.0148 | 0.0056 | 0.0124 | 0.0236 | 0.0310 | 0.0102 | 0.5000 |
| old | actual | 4-10 | concave | 0.0000 | tau | 295 | 0.0137 | 0.0032 | 0.0089 | 0.0178 | 0.0346 | 0.0000 | 0.6599 |
| old | actual | 4-10 | concave | 0.5000 | tau | 295 | 0.0111 | 0.0030 | 0.0082 | 0.0166 | 0.0258 | 0.0169 | 0.6599 |
| old | actual | 4-10 | concave | 0.8000 | tau | 295 | 0.0096 | 0.0030 | 0.0075 | 0.0153 | 0.0208 | 0.0271 | 0.6599 |
| old | actual | 4-10 | convex | 0.0000 | tau | 295 | 0.0229 | 0.0090 | 0.0195 | 0.0361 | 0.0458 | 0.0000 | 0.3391 |
| old | actual | 4-10 | convex | 0.5000 | tau | 295 | 0.0216 | 0.0090 | 0.0182 | 0.0340 | 0.0438 | 0.0034 | 0.3391 |
| old | actual | 4-10 | convex | 0.8000 | tau | 295 | 0.0208 | 0.0090 | 0.0166 | 0.0319 | 0.0425 | 0.0068 | 0.3391 |
| old | actual | 4-10 | top3_stress | 0.0000 | tau | 295 | 0.0183 | 0.0096 | 0.0168 | 0.0276 | 0.0338 | 0.0000 | 0.1000 |
| old | actual | 4-10 | top3_stress | 0.5000 | tau | 295 | 0.0179 | 0.0094 | 0.0165 | 0.0269 | 0.0329 | 0.0034 | 0.1000 |
| old | actual | 4-10 | top3_stress | 0.8000 | tau | 295 | 0.0177 | 0.0093 | 0.0163 | 0.0268 | 0.0324 | 0.0034 | 0.1000 |
| old | actual | 11-16 | - | 0.0000 | M | 243 | 0.0102 | -0.0000 | 0.0000 | 0.0002 | 0.0174 |  |  |
| old | actual | 11-16 | linear | 0.0000 | tau | 243 | 0.0280 | 0.0079 | 0.0267 | 0.0374 | 0.0523 | 0.0000 | 0.5000 |
| old | actual | 11-16 | linear | 0.5000 | tau | 243 | 0.0254 | 0.0062 | 0.0258 | 0.0359 | 0.0509 | 0.0000 | 0.5000 |
| old | actual | 11-16 | linear | 0.8000 | tau | 243 | 0.0239 | 0.0049 | 0.0252 | 0.0359 | 0.0470 | 0.0000 | 0.5000 |
| old | actual | 11-16 | concave | 0.0000 | tau | 243 | 0.0225 | 0.0064 | 0.0183 | 0.0280 | 0.0399 | 0.0000 | 0.6599 |
| old | actual | 11-16 | concave | 0.5000 | tau | 243 | 0.0191 | 0.0056 | 0.0180 | 0.0262 | 0.0358 | 0.0041 | 0.6599 |
| old | actual | 11-16 | concave | 0.8000 | tau | 243 | 0.0171 | 0.0040 | 0.0163 | 0.0253 | 0.0337 | 0.0041 | 0.6599 |
| old | actual | 11-16 | convex | 0.0000 | tau | 243 | 0.0294 | 0.0080 | 0.0299 | 0.0414 | 0.0602 | 0.0000 | 0.3391 |
| old | actual | 11-16 | convex | 0.5000 | tau | 243 | 0.0276 | 0.0062 | 0.0283 | 0.0403 | 0.0562 | 0.0082 | 0.3391 |
| old | actual | 11-16 | convex | 0.8000 | tau | 243 | 0.0266 | 0.0055 | 0.0282 | 0.0384 | 0.0548 | 0.0123 | 0.3391 |
| old | actual | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0091 | 0.0020 | 0.0065 | 0.0144 | 0.0211 | 0.0000 | 0.1000 |
| old | actual | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0086 | 0.0014 | 0.0061 | 0.0139 | 0.0211 | 0.0412 | 0.1000 |
| old | actual | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0083 | 0.0007 | 0.0060 | 0.0137 | 0.0210 | 0.0576 | 0.1000 |
| old | actual | 17-30 | - | 0.0000 | M | 586 | 0.0050 | -0.0000 | 0.0000 | 0.0000 | 0.0051 |  |  |
| old | actual | 17-30 | linear | 0.0000 | tau | 586 | 0.0162 | 0.0000 | 0.0074 | 0.0298 | 0.0415 | 0.0000 | 0.5000 |
| old | actual | 17-30 | linear | 0.5000 | tau | 586 | 0.0149 | 0.0000 | 0.0059 | 0.0285 | 0.0404 | 0.0017 | 0.5000 |
| old | actual | 17-30 | linear | 0.8000 | tau | 586 | 0.0142 | 0.0000 | 0.0045 | 0.0276 | 0.0402 | 0.0034 | 0.5000 |
| old | actual | 17-30 | concave | 0.0000 | tau | 586 | 0.0184 | 0.0000 | 0.0117 | 0.0323 | 0.0425 | 0.0000 | 0.6599 |
| old | actual | 17-30 | concave | 0.5000 | tau | 586 | 0.0167 | 0.0000 | 0.0091 | 0.0315 | 0.0397 | 0.0017 | 0.6599 |
| old | actual | 17-30 | concave | 0.8000 | tau | 586 | 0.0157 | 0.0000 | 0.0073 | 0.0308 | 0.0392 | 0.0017 | 0.6599 |
| old | actual | 17-30 | convex | 0.0000 | tau | 586 | 0.0094 | 0.0000 | 0.0029 | 0.0158 | 0.0287 | 0.0000 | 0.3391 |
| old | actual | 17-30 | convex | 0.5000 | tau | 586 | 0.0086 | 0.0000 | 0.0025 | 0.0141 | 0.0279 | 0.0000 | 0.3391 |
| old | actual | 17-30 | convex | 0.8000 | tau | 586 | 0.0081 | 0.0000 | 0.0018 | 0.0128 | 0.0277 | 0.0051 | 0.3391 |
| old | actual | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0006 | 0.0000 | 0.0000 | 0.0003 | 0.0018 | 0.0000 | 0.1000 |
| old | actual | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0003 | 0.0000 | 0.0000 | 0.0001 | 0.0012 | 0.2167 | 0.1000 |
| old | actual | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0002 | 0.0000 | 0.0000 | 0.0001 | 0.0013 | 0.2201 | 0.1000 |
| old | own | all | - | 0.0000 | M | 1252 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | all | linear | 0.0000 | tau | 1252 | 0.0240 | 0.0082 | 0.0238 | 0.0352 | 0.0457 | 0.0000 | 0.5000 |
| old | own | all | linear | 0.5000 | tau | 1252 | 0.0240 | 0.0082 | 0.0238 | 0.0352 | 0.0457 | 0.0000 | 0.5000 |
| old | own | all | linear | 0.8000 | tau | 1252 | 0.0240 | 0.0082 | 0.0238 | 0.0352 | 0.0457 | 0.0000 | 0.5000 |
| old | own | all | concave | 0.0000 | tau | 1252 | 0.0211 | 0.0061 | 0.0210 | 0.0318 | 0.0396 | 0.0000 | 0.6599 |
| old | own | all | concave | 0.5000 | tau | 1252 | 0.0211 | 0.0061 | 0.0210 | 0.0318 | 0.0396 | 0.0000 | 0.6599 |
| old | own | all | concave | 0.8000 | tau | 1252 | 0.0211 | 0.0061 | 0.0210 | 0.0318 | 0.0396 | 0.0000 | 0.6599 |
| old | own | all | convex | 0.0000 | tau | 1252 | 0.0218 | 0.0062 | 0.0188 | 0.0329 | 0.0442 | 0.0000 | 0.3391 |
| old | own | all | convex | 0.5000 | tau | 1252 | 0.0218 | 0.0062 | 0.0188 | 0.0329 | 0.0442 | 0.0000 | 0.3391 |
| old | own | all | convex | 0.8000 | tau | 1252 | 0.0218 | 0.0062 | 0.0188 | 0.0329 | 0.0442 | 0.0000 | 0.3391 |
| old | own | all | top3_stress | 0.0000 | tau | 1252 | 0.0077 | 0.0000 | 0.0026 | 0.0129 | 0.0238 | 0.0000 | 0.1000 |
| old | own | all | top3_stress | 0.5000 | tau | 1252 | 0.0077 | 0.0000 | 0.0026 | 0.0129 | 0.0238 | 0.0799 | 0.1000 |
| old | own | all | top3_stress | 0.8000 | tau | 1252 | 0.0077 | 0.0000 | 0.0026 | 0.0129 | 0.0238 | 0.0807 | 0.1000 |
| old | own | 1-3 | - | 0.0000 | M | 128 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 1-3 | linear | 0.0000 | tau | 128 | 0.0033 | 0.0018 | 0.0024 | 0.0040 | 0.0061 | 0.0000 | 0.5000 |
| old | own | 1-3 | linear | 0.5000 | tau | 128 | 0.0033 | 0.0018 | 0.0024 | 0.0040 | 0.0061 | 0.0000 | 0.5000 |
| old | own | 1-3 | linear | 0.8000 | tau | 128 | 0.0033 | 0.0018 | 0.0024 | 0.0040 | 0.0061 | 0.0000 | 0.5000 |
| old | own | 1-3 | concave | 0.0000 | tau | 128 | 0.0018 | 0.0010 | 0.0013 | 0.0022 | 0.0033 | 0.0000 | 0.6599 |
| old | own | 1-3 | concave | 0.5000 | tau | 128 | 0.0018 | 0.0010 | 0.0013 | 0.0022 | 0.0033 | 0.0000 | 0.6599 |
| old | own | 1-3 | concave | 0.8000 | tau | 128 | 0.0018 | 0.0010 | 0.0013 | 0.0022 | 0.0033 | 0.0000 | 0.6599 |
| old | own | 1-3 | convex | 0.0000 | tau | 128 | 0.0055 | 0.0031 | 0.0041 | 0.0068 | 0.0103 | 0.0000 | 0.3391 |
| old | own | 1-3 | convex | 0.5000 | tau | 128 | 0.0055 | 0.0031 | 0.0041 | 0.0068 | 0.0103 | 0.0000 | 0.3391 |
| old | own | 1-3 | convex | 0.8000 | tau | 128 | 0.0055 | 0.0031 | 0.0041 | 0.0068 | 0.0103 | 0.0000 | 0.3391 |
| old | own | 1-3 | top3_stress | 0.0000 | tau | 128 | 0.0044 | 0.0002 | 0.0013 | 0.0057 | 0.0129 | 0.0000 | 0.1000 |
| old | own | 1-3 | top3_stress | 0.5000 | tau | 128 | 0.0044 | 0.0002 | 0.0013 | 0.0057 | 0.0129 | 0.0078 | 0.1000 |
| old | own | 1-3 | top3_stress | 0.8000 | tau | 128 | 0.0044 | 0.0002 | 0.0013 | 0.0057 | 0.0129 | 0.0078 | 0.1000 |
| old | own | 4-10 | - | 0.0000 | M | 295 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 4-10 | linear | 0.0000 | tau | 295 | 0.0162 | 0.0071 | 0.0124 | 0.0246 | 0.0321 | 0.0000 | 0.5000 |
| old | own | 4-10 | linear | 0.5000 | tau | 295 | 0.0162 | 0.0071 | 0.0124 | 0.0246 | 0.0321 | 0.0000 | 0.5000 |
| old | own | 4-10 | linear | 0.8000 | tau | 295 | 0.0162 | 0.0071 | 0.0124 | 0.0246 | 0.0321 | 0.0000 | 0.5000 |
| old | own | 4-10 | concave | 0.0000 | tau | 295 | 0.0095 | 0.0039 | 0.0069 | 0.0144 | 0.0191 | 0.0000 | 0.6599 |
| old | own | 4-10 | concave | 0.5000 | tau | 295 | 0.0095 | 0.0039 | 0.0069 | 0.0144 | 0.0191 | 0.0000 | 0.6599 |
| old | own | 4-10 | concave | 0.8000 | tau | 295 | 0.0095 | 0.0039 | 0.0069 | 0.0144 | 0.0191 | 0.0000 | 0.6599 |
| old | own | 4-10 | convex | 0.0000 | tau | 295 | 0.0239 | 0.0114 | 0.0191 | 0.0363 | 0.0458 | 0.0000 | 0.3391 |
| old | own | 4-10 | convex | 0.5000 | tau | 295 | 0.0239 | 0.0114 | 0.0191 | 0.0363 | 0.0458 | 0.0000 | 0.3391 |
| old | own | 4-10 | convex | 0.8000 | tau | 295 | 0.0239 | 0.0114 | 0.0191 | 0.0363 | 0.0458 | 0.0000 | 0.3391 |
| old | own | 4-10 | top3_stress | 0.0000 | tau | 295 | 0.0196 | 0.0112 | 0.0179 | 0.0276 | 0.0336 | 0.0000 | 0.1000 |
| old | own | 4-10 | top3_stress | 0.5000 | tau | 295 | 0.0196 | 0.0112 | 0.0179 | 0.0276 | 0.0336 | 0.0000 | 0.1000 |
| old | own | 4-10 | top3_stress | 0.8000 | tau | 295 | 0.0196 | 0.0112 | 0.0179 | 0.0276 | 0.0336 | 0.0000 | 0.1000 |
| old | own | 11-16 | - | 0.0000 | M | 243 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 11-16 | linear | 0.0000 | tau | 243 | 0.0329 | 0.0223 | 0.0306 | 0.0399 | 0.0550 | 0.0000 | 0.5000 |
| old | own | 11-16 | linear | 0.5000 | tau | 243 | 0.0329 | 0.0223 | 0.0306 | 0.0399 | 0.0550 | 0.0000 | 0.5000 |
| old | own | 11-16 | linear | 0.8000 | tau | 243 | 0.0329 | 0.0223 | 0.0306 | 0.0399 | 0.0550 | 0.0000 | 0.5000 |
| old | own | 11-16 | concave | 0.0000 | tau | 243 | 0.0222 | 0.0146 | 0.0207 | 0.0277 | 0.0370 | 0.0000 | 0.6599 |
| old | own | 11-16 | concave | 0.5000 | tau | 243 | 0.0222 | 0.0146 | 0.0207 | 0.0277 | 0.0370 | 0.0000 | 0.6599 |
| old | own | 11-16 | concave | 0.8000 | tau | 243 | 0.0222 | 0.0146 | 0.0207 | 0.0277 | 0.0370 | 0.0000 | 0.6599 |
| old | own | 11-16 | convex | 0.0000 | tau | 243 | 0.0377 | 0.0267 | 0.0343 | 0.0445 | 0.0660 | 0.0000 | 0.3391 |
| old | own | 11-16 | convex | 0.5000 | tau | 243 | 0.0377 | 0.0267 | 0.0343 | 0.0445 | 0.0660 | 0.0000 | 0.3391 |
| old | own | 11-16 | convex | 0.8000 | tau | 243 | 0.0377 | 0.0267 | 0.0343 | 0.0445 | 0.0660 | 0.0000 | 0.3391 |
| old | own | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0113 | 0.0053 | 0.0084 | 0.0163 | 0.0226 | 0.0000 | 0.1000 |
| old | own | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0113 | 0.0053 | 0.0084 | 0.0163 | 0.0226 | 0.0000 | 0.1000 |
| old | own | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0113 | 0.0053 | 0.0084 | 0.0163 | 0.0226 | 0.0000 | 0.1000 |
| old | own | 17-30 | - | 0.0000 | M | 586 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 17-30 | linear | 0.0000 | tau | 586 | 0.0288 | 0.0172 | 0.0290 | 0.0386 | 0.0482 | 0.0000 | 0.5000 |
| old | own | 17-30 | linear | 0.5000 | tau | 586 | 0.0288 | 0.0172 | 0.0290 | 0.0386 | 0.0482 | 0.0000 | 0.5000 |
| old | own | 17-30 | linear | 0.8000 | tau | 586 | 0.0288 | 0.0172 | 0.0290 | 0.0386 | 0.0482 | 0.0000 | 0.5000 |
| old | own | 17-30 | concave | 0.0000 | tau | 586 | 0.0307 | 0.0240 | 0.0309 | 0.0373 | 0.0448 | 0.0000 | 0.6599 |
| old | own | 17-30 | concave | 0.5000 | tau | 586 | 0.0307 | 0.0240 | 0.0309 | 0.0373 | 0.0448 | 0.0000 | 0.6599 |
| old | own | 17-30 | concave | 0.8000 | tau | 586 | 0.0307 | 0.0240 | 0.0309 | 0.0373 | 0.0448 | 0.0000 | 0.6599 |
| old | own | 17-30 | convex | 0.0000 | tau | 586 | 0.0176 | 0.0046 | 0.0148 | 0.0277 | 0.0368 | 0.0000 | 0.3391 |
| old | own | 17-30 | convex | 0.5000 | tau | 586 | 0.0176 | 0.0046 | 0.0148 | 0.0277 | 0.0368 | 0.0000 | 0.3391 |
| old | own | 17-30 | convex | 0.8000 | tau | 586 | 0.0176 | 0.0046 | 0.0148 | 0.0277 | 0.0368 | 0.0000 | 0.3391 |
| old | own | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0009 | 0.0000 | 0.0000 | 0.0008 | 0.0029 | 0.0000 | 0.1000 |
| old | own | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0009 | 0.0000 | 0.0000 | 0.0008 | 0.0029 | 0.1689 | 0.1000 |
| old | own | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0009 | 0.0000 | 0.0000 | 0.0008 | 0.0029 | 0.1706 | 0.1000 |
| new | actual | all | - | 0.0000 | M | 1252 | 0.0062 | -0.0000 | 0.0000 | 0.0000 | 0.0156 |  |  |
| new | actual | all | linear | 0.0000 | tau | 1252 | 0.0159 | 0.0000 | 0.0038 | 0.0291 | 0.0452 | 0.0000 | 0.5000 |
| new | actual | all | linear | 0.5000 | tau | 1252 | 0.0143 | 0.0000 | 0.0035 | 0.0271 | 0.0438 | 0.0312 | 0.5000 |
| new | actual | all | linear | 0.8000 | tau | 1252 | 0.0134 | 0.0000 | 0.0031 | 0.0254 | 0.0420 | 0.0335 | 0.5000 |
| new | actual | all | concave | 0.0000 | tau | 1252 | 0.0154 | 0.0000 | 0.0039 | 0.0290 | 0.0410 | 0.0000 | 0.6599 |
| new | actual | all | concave | 0.5000 | tau | 1252 | 0.0134 | 0.0000 | 0.0029 | 0.0265 | 0.0387 | 0.0032 | 0.6599 |
| new | actual | all | concave | 0.8000 | tau | 1252 | 0.0122 | 0.0000 | 0.0024 | 0.0241 | 0.0367 | 0.0112 | 0.6599 |
| new | actual | all | convex | 0.0000 | tau | 1252 | 0.0135 | 0.0000 | 0.0019 | 0.0217 | 0.0432 | 0.0000 | 0.3391 |
| new | actual | all | convex | 0.5000 | tau | 1252 | 0.0125 | 0.0000 | 0.0019 | 0.0209 | 0.0411 | 0.0056 | 0.3391 |
| new | actual | all | convex | 0.8000 | tau | 1252 | 0.0118 | 0.0000 | 0.0018 | 0.0194 | 0.0400 | 0.0112 | 0.3391 |
| new | actual | all | top3_stress | 0.0000 | tau | 1252 | 0.0048 | 0.0000 | 0.0000 | 0.0071 | 0.0211 | 0.0000 | 0.1000 |
| new | actual | all | top3_stress | 0.5000 | tau | 1252 | 0.0045 | 0.0000 | 0.0000 | 0.0067 | 0.0199 | 0.0687 | 0.1000 |
| new | actual | all | top3_stress | 0.8000 | tau | 1252 | 0.0043 | 0.0000 | 0.0000 | 0.0062 | 0.0191 | 0.0687 | 0.1000 |
| new | actual | 1-3 | - | 0.0000 | M | 128 | -0.0005 | -0.0000 | 0.0000 | 0.0000 | 0.0034 |  |  |
| new | actual | 1-3 | linear | 0.0000 | tau | 128 | -0.0029 | -0.0032 | -0.0003 | 0.0002 | 0.0018 | 0.0000 | 0.5000 |
| new | actual | 1-3 | linear | 0.5000 | tau | 128 | -0.0027 | -0.0031 | -0.0006 | -0.0000 | 0.0008 | 0.1094 | 0.5000 |
| new | actual | 1-3 | linear | 0.8000 | tau | 128 | -0.0027 | -0.0033 | -0.0007 | -0.0000 | 0.0005 | 0.1172 | 0.5000 |
| new | actual | 1-3 | concave | 0.0000 | tau | 128 | -0.0018 | -0.0017 | -0.0002 | 0.0002 | 0.0038 | 0.0000 | 0.6599 |
| new | actual | 1-3 | concave | 0.5000 | tau | 128 | -0.0017 | -0.0017 | -0.0001 | 0.0003 | 0.0019 | 0.0156 | 0.6599 |
| new | actual | 1-3 | concave | 0.8000 | tau | 128 | -0.0016 | -0.0016 | -0.0002 | 0.0000 | 0.0010 | 0.0703 | 0.6599 |
| new | actual | 1-3 | convex | 0.0000 | tau | 128 | -0.0042 | -0.0062 | -0.0012 | -0.0001 | 0.0006 | 0.0000 | 0.3391 |
| new | actual | 1-3 | convex | 0.5000 | tau | 128 | -0.0041 | -0.0062 | -0.0014 | -0.0001 | 0.0003 | 0.0156 | 0.3391 |
| new | actual | 1-3 | convex | 0.8000 | tau | 128 | -0.0041 | -0.0061 | -0.0015 | -0.0001 | 0.0001 | 0.0391 | 0.3391 |
| new | actual | 1-3 | top3_stress | 0.0000 | tau | 128 | -0.0059 | -0.0101 | -0.0029 | -0.0002 | 0.0000 | 0.0000 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.5000 | tau | 128 | -0.0059 | -0.0101 | -0.0030 | -0.0001 | 0.0000 | 0.0859 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.8000 | tau | 128 | -0.0059 | -0.0102 | -0.0030 | -0.0001 | 0.0000 | 0.0859 | 0.1000 |
| new | actual | 4-10 | - | 0.0000 | M | 295 | 0.0041 | -0.0000 | 0.0000 | 0.0020 | 0.0156 |  |  |
| new | actual | 4-10 | linear | 0.0000 | tau | 295 | 0.0046 | 0.0000 | 0.0007 | 0.0068 | 0.0167 | 0.0000 | 0.5000 |
| new | actual | 4-10 | linear | 0.5000 | tau | 295 | 0.0036 | -0.0001 | 0.0003 | 0.0059 | 0.0147 | 0.0847 | 0.5000 |
| new | actual | 4-10 | linear | 0.8000 | tau | 295 | 0.0030 | -0.0001 | 0.0003 | 0.0055 | 0.0135 | 0.0881 | 0.5000 |
| new | actual | 4-10 | concave | 0.0000 | tau | 295 | 0.0045 | 0.0000 | 0.0007 | 0.0055 | 0.0151 | 0.0000 | 0.6599 |
| new | actual | 4-10 | concave | 0.5000 | tau | 295 | 0.0032 | 0.0000 | 0.0005 | 0.0043 | 0.0113 | 0.0068 | 0.6599 |
| new | actual | 4-10 | concave | 0.8000 | tau | 295 | 0.0024 | 0.0000 | 0.0003 | 0.0038 | 0.0104 | 0.0169 | 0.6599 |
| new | actual | 4-10 | convex | 0.0000 | tau | 295 | 0.0045 | -0.0002 | 0.0003 | 0.0075 | 0.0191 | 0.0000 | 0.3391 |
| new | actual | 4-10 | convex | 0.5000 | tau | 295 | 0.0038 | -0.0002 | 0.0003 | 0.0070 | 0.0176 | 0.0136 | 0.3391 |
| new | actual | 4-10 | convex | 0.8000 | tau | 295 | 0.0034 | -0.0001 | 0.0003 | 0.0069 | 0.0166 | 0.0169 | 0.3391 |
| new | actual | 4-10 | top3_stress | 0.0000 | tau | 295 | 0.0023 | -0.0001 | 0.0000 | 0.0066 | 0.0134 | 0.0000 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.5000 | tau | 295 | 0.0021 | -0.0001 | 0.0000 | 0.0063 | 0.0128 | 0.0169 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.8000 | tau | 295 | 0.0020 | -0.0001 | 0.0000 | 0.0062 | 0.0125 | 0.0169 | 0.1000 |
| new | actual | 11-16 | - | 0.0000 | M | 243 | 0.0081 | -0.0000 | 0.0000 | 0.0000 | 0.0308 |  |  |
| new | actual | 11-16 | linear | 0.0000 | tau | 243 | 0.0270 | 0.0004 | 0.0222 | 0.0402 | 0.0555 | 0.0000 | 0.5000 |
| new | actual | 11-16 | linear | 0.5000 | tau | 243 | 0.0249 | 0.0004 | 0.0189 | 0.0381 | 0.0480 | 0.0000 | 0.5000 |
| new | actual | 11-16 | linear | 0.8000 | tau | 243 | 0.0237 | 0.0004 | 0.0175 | 0.0366 | 0.0472 | 0.0000 | 0.5000 |
| new | actual | 11-16 | concave | 0.0000 | tau | 243 | 0.0207 | 0.0003 | 0.0166 | 0.0294 | 0.0428 | 0.0000 | 0.6599 |
| new | actual | 11-16 | concave | 0.5000 | tau | 243 | 0.0180 | 0.0003 | 0.0151 | 0.0275 | 0.0375 | 0.0000 | 0.6599 |
| new | actual | 11-16 | concave | 0.8000 | tau | 243 | 0.0164 | 0.0003 | 0.0121 | 0.0259 | 0.0322 | 0.0000 | 0.6599 |
| new | actual | 11-16 | convex | 0.0000 | tau | 243 | 0.0305 | 0.0004 | 0.0266 | 0.0437 | 0.0619 | 0.0000 | 0.3391 |
| new | actual | 11-16 | convex | 0.5000 | tau | 243 | 0.0291 | 0.0004 | 0.0242 | 0.0424 | 0.0573 | 0.0000 | 0.3391 |
| new | actual | 11-16 | convex | 0.8000 | tau | 243 | 0.0283 | 0.0004 | 0.0219 | 0.0422 | 0.0549 | 0.0000 | 0.3391 |
| new | actual | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0164 | 0.0003 | 0.0138 | 0.0234 | 0.0336 | 0.0000 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0160 | 0.0003 | 0.0125 | 0.0229 | 0.0317 | 0.0000 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0158 | 0.0003 | 0.0123 | 0.0228 | 0.0317 | 0.0000 | 0.1000 |
| new | actual | 17-30 | - | 0.0000 | M | 586 | 0.0080 | -0.0000 | 0.0000 | 0.0000 | 0.0253 |  |  |
| new | actual | 17-30 | linear | 0.0000 | tau | 586 | 0.0210 | 0.0000 | 0.0151 | 0.0360 | 0.0506 | 0.0000 | 0.5000 |
| new | actual | 17-30 | linear | 0.5000 | tau | 586 | 0.0190 | 0.0000 | 0.0142 | 0.0342 | 0.0464 | 0.0000 | 0.5000 |
| new | actual | 17-30 | linear | 0.8000 | tau | 586 | 0.0178 | 0.0000 | 0.0123 | 0.0323 | 0.0447 | 0.0017 | 0.5000 |
| new | actual | 17-30 | concave | 0.0000 | tau | 586 | 0.0226 | 0.0000 | 0.0208 | 0.0362 | 0.0520 | 0.0000 | 0.6599 |
| new | actual | 17-30 | concave | 0.5000 | tau | 586 | 0.0199 | 0.0000 | 0.0191 | 0.0354 | 0.0440 | 0.0000 | 0.6599 |
| new | actual | 17-30 | concave | 0.8000 | tau | 586 | 0.0183 | 0.0000 | 0.0153 | 0.0338 | 0.0412 | 0.0000 | 0.6599 |
| new | actual | 17-30 | convex | 0.0000 | tau | 586 | 0.0149 | 0.0000 | 0.0049 | 0.0237 | 0.0431 | 0.0000 | 0.3391 |
| new | actual | 17-30 | convex | 0.5000 | tau | 586 | 0.0135 | 0.0000 | 0.0046 | 0.0219 | 0.0387 | 0.0017 | 0.3391 |
| new | actual | 17-30 | convex | 0.8000 | tau | 586 | 0.0127 | 0.0000 | 0.0046 | 0.0210 | 0.0346 | 0.0068 | 0.3391 |
| new | actual | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0036 | 0.0000 | 0.0000 | 0.0027 | 0.0133 | 0.0000 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0032 | 0.0000 | 0.0000 | 0.0027 | 0.0114 | 0.1195 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0030 | 0.0000 | 0.0000 | 0.0025 | 0.0108 | 0.1195 | 0.1000 |
| new | own | all | - | 0.0000 | M | 1252 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | all | linear | 0.0000 | tau | 1252 | 0.0233 | 0.0003 | 0.0166 | 0.0397 | 0.0543 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.5000 | tau | 1252 | 0.0233 | 0.0003 | 0.0166 | 0.0397 | 0.0543 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.8000 | tau | 1252 | 0.0233 | 0.0003 | 0.0166 | 0.0397 | 0.0543 | 0.0000 | 0.5000 |
| new | own | all | concave | 0.0000 | tau | 1252 | 0.0207 | 0.0002 | 0.0207 | 0.0347 | 0.0444 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.5000 | tau | 1252 | 0.0207 | 0.0002 | 0.0207 | 0.0347 | 0.0444 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.8000 | tau | 1252 | 0.0207 | 0.0002 | 0.0207 | 0.0347 | 0.0444 | 0.0000 | 0.6599 |
| new | own | all | convex | 0.0000 | tau | 1252 | 0.0207 | 0.0001 | 0.0101 | 0.0343 | 0.0567 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.5000 | tau | 1252 | 0.0207 | 0.0001 | 0.0101 | 0.0343 | 0.0567 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.8000 | tau | 1252 | 0.0207 | 0.0001 | 0.0101 | 0.0343 | 0.0567 | 0.0000 | 0.3391 |
| new | own | all | top3_stress | 0.0000 | tau | 1252 | 0.0072 | 0.0000 | 0.0006 | 0.0122 | 0.0245 | 0.0000 | 0.1000 |
| new | own | all | top3_stress | 0.5000 | tau | 1252 | 0.0072 | 0.0000 | 0.0006 | 0.0122 | 0.0245 | 0.1118 | 0.1000 |
| new | own | all | top3_stress | 0.8000 | tau | 1252 | 0.0072 | 0.0000 | 0.0006 | 0.0122 | 0.0245 | 0.1126 | 0.1000 |
| new | own | 1-3 | - | 0.0000 | M | 128 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 1-3 | linear | 0.0000 | tau | 128 | -0.0016 | -0.0028 | -0.0008 | -0.0001 | -0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.5000 | tau | 128 | -0.0016 | -0.0028 | -0.0008 | -0.0001 | -0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.8000 | tau | 128 | -0.0016 | -0.0028 | -0.0008 | -0.0001 | -0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | concave | 0.0000 | tau | 128 | -0.0008 | -0.0014 | -0.0004 | -0.0001 | -0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.5000 | tau | 128 | -0.0008 | -0.0014 | -0.0004 | -0.0001 | -0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.8000 | tau | 128 | -0.0008 | -0.0014 | -0.0004 | -0.0001 | -0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | convex | 0.0000 | tau | 128 | -0.0031 | -0.0052 | -0.0015 | -0.0002 | -0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.5000 | tau | 128 | -0.0031 | -0.0052 | -0.0015 | -0.0002 | -0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.8000 | tau | 128 | -0.0031 | -0.0052 | -0.0015 | -0.0002 | -0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | top3_stress | 0.0000 | tau | 128 | -0.0057 | -0.0097 | -0.0026 | -0.0002 | 0.0000 | 0.0000 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.5000 | tau | 128 | -0.0057 | -0.0097 | -0.0026 | -0.0002 | 0.0000 | 0.1016 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.8000 | tau | 128 | -0.0057 | -0.0097 | -0.0026 | -0.0002 | 0.0000 | 0.1016 | 0.1000 |
| new | own | 4-10 | - | 0.0000 | M | 295 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 4-10 | linear | 0.0000 | tau | 295 | 0.0037 | -0.0000 | 0.0003 | 0.0059 | 0.0125 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.5000 | tau | 295 | 0.0037 | -0.0000 | 0.0003 | 0.0059 | 0.0125 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.8000 | tau | 295 | 0.0037 | -0.0000 | 0.0003 | 0.0059 | 0.0125 | 0.0000 | 0.5000 |
| new | own | 4-10 | concave | 0.0000 | tau | 295 | 0.0023 | -0.0000 | 0.0002 | 0.0036 | 0.0074 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.5000 | tau | 295 | 0.0023 | -0.0000 | 0.0002 | 0.0036 | 0.0074 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.8000 | tau | 295 | 0.0023 | -0.0000 | 0.0002 | 0.0036 | 0.0074 | 0.0000 | 0.6599 |
| new | own | 4-10 | convex | 0.0000 | tau | 295 | 0.0047 | -0.0000 | 0.0004 | 0.0084 | 0.0177 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.5000 | tau | 295 | 0.0047 | -0.0000 | 0.0004 | 0.0084 | 0.0177 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.8000 | tau | 295 | 0.0047 | -0.0000 | 0.0004 | 0.0084 | 0.0177 | 0.0000 | 0.3391 |
| new | own | 4-10 | top3_stress | 0.0000 | tau | 295 | 0.0028 | -0.0000 | 0.0001 | 0.0073 | 0.0139 | 0.0000 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.5000 | tau | 295 | 0.0028 | -0.0000 | 0.0001 | 0.0073 | 0.0139 | 0.0475 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.8000 | tau | 295 | 0.0028 | -0.0000 | 0.0001 | 0.0073 | 0.0139 | 0.0475 | 0.1000 |
| new | own | 11-16 | - | 0.0000 | M | 243 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 11-16 | linear | 0.0000 | tau | 243 | 0.0344 | 0.0131 | 0.0334 | 0.0465 | 0.0650 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.5000 | tau | 243 | 0.0344 | 0.0131 | 0.0334 | 0.0465 | 0.0650 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.8000 | tau | 243 | 0.0344 | 0.0131 | 0.0334 | 0.0465 | 0.0650 | 0.0000 | 0.5000 |
| new | own | 11-16 | concave | 0.0000 | tau | 243 | 0.0226 | 0.0083 | 0.0218 | 0.0314 | 0.0440 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.5000 | tau | 243 | 0.0226 | 0.0083 | 0.0218 | 0.0314 | 0.0440 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.8000 | tau | 243 | 0.0226 | 0.0083 | 0.0218 | 0.0314 | 0.0440 | 0.0000 | 0.6599 |
| new | own | 11-16 | convex | 0.0000 | tau | 243 | 0.0421 | 0.0171 | 0.0396 | 0.0549 | 0.0800 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.5000 | tau | 243 | 0.0421 | 0.0171 | 0.0396 | 0.0549 | 0.0800 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.8000 | tau | 243 | 0.0421 | 0.0171 | 0.0396 | 0.0549 | 0.0800 | 0.0000 | 0.3391 |
| new | own | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0224 | 0.0112 | 0.0191 | 0.0284 | 0.0455 | 0.0000 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0224 | 0.0112 | 0.0191 | 0.0284 | 0.0455 | 0.0123 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0224 | 0.0112 | 0.0191 | 0.0284 | 0.0455 | 0.0123 | 0.1000 |
| new | own | 17-30 | - | 0.0000 | M | 586 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 17-30 | linear | 0.0000 | tau | 586 | 0.0341 | 0.0165 | 0.0312 | 0.0452 | 0.0625 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.5000 | tau | 586 | 0.0341 | 0.0165 | 0.0312 | 0.0452 | 0.0625 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.8000 | tau | 586 | 0.0341 | 0.0165 | 0.0312 | 0.0452 | 0.0625 | 0.0000 | 0.5000 |
| new | own | 17-30 | concave | 0.0000 | tau | 586 | 0.0339 | 0.0251 | 0.0333 | 0.0410 | 0.0523 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.5000 | tau | 586 | 0.0339 | 0.0251 | 0.0333 | 0.0410 | 0.0523 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.8000 | tau | 586 | 0.0339 | 0.0251 | 0.0333 | 0.0410 | 0.0523 | 0.0000 | 0.6599 |
| new | own | 17-30 | convex | 0.0000 | tau | 586 | 0.0251 | 0.0046 | 0.0161 | 0.0374 | 0.0600 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.5000 | tau | 586 | 0.0251 | 0.0046 | 0.0161 | 0.0374 | 0.0600 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.8000 | tau | 586 | 0.0251 | 0.0046 | 0.0161 | 0.0374 | 0.0600 | 0.0000 | 0.3391 |
| new | own | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0059 | 0.0000 | 0.0002 | 0.0071 | 0.0205 | 0.0000 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0059 | 0.0000 | 0.0002 | 0.0071 | 0.0205 | 0.1877 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0059 | 0.0000 | 0.0002 | 0.0071 | 0.0205 | 0.1894 | 0.1000 |
| delta | actual | all | - | 0.0000 | M | 1252 | 0.0001 | -0.0000 | 0.0000 | 0.0000 | 0.0065 |  |  |
| delta | actual | all | linear | 0.0000 | tau | 1252 | -0.0016 | -0.0069 | 0.0000 | 0.0011 | 0.0109 | 0.0000 | 0.5000 |
| delta | actual | all | linear | 0.5000 | tau | 1252 | -0.0017 | -0.0070 | 0.0000 | 0.0011 | 0.0104 | 0.0064 | 0.5000 |
| delta | actual | all | linear | 0.8000 | tau | 1252 | -0.0017 | -0.0071 | 0.0000 | 0.0010 | 0.0094 | 0.0088 | 0.5000 |
| delta | actual | all | concave | 0.0000 | tau | 1252 | -0.0009 | -0.0043 | 0.0000 | 0.0012 | 0.0088 | 0.0000 | 0.6599 |
| delta | actual | all | concave | 0.5000 | tau | 1252 | -0.0009 | -0.0041 | 0.0000 | 0.0008 | 0.0072 | 0.0240 | 0.6599 |
| delta | actual | all | concave | 0.8000 | tau | 1252 | -0.0010 | -0.0041 | 0.0000 | 0.0006 | 0.0063 | 0.0407 | 0.6599 |
| delta | actual | all | convex | 0.0000 | tau | 1252 | -0.0025 | -0.0109 | 0.0000 | 0.0016 | 0.0138 | 0.0000 | 0.3391 |
| delta | actual | all | convex | 0.5000 | tau | 1252 | -0.0025 | -0.0110 | 0.0000 | 0.0015 | 0.0131 | 0.0048 | 0.3391 |
| delta | actual | all | convex | 0.8000 | tau | 1252 | -0.0025 | -0.0107 | 0.0000 | 0.0013 | 0.0127 | 0.0072 | 0.3391 |
| delta | actual | all | top3_stress | 0.0000 | tau | 1252 | -0.0020 | -0.0069 | 0.0000 | 0.0011 | 0.0119 | 0.0000 | 0.1000 |
| delta | actual | all | top3_stress | 0.5000 | tau | 1252 | -0.0020 | -0.0067 | 0.0000 | 0.0013 | 0.0115 | 0.0391 | 0.1000 |
| delta | actual | all | top3_stress | 0.8000 | tau | 1252 | -0.0020 | -0.0067 | 0.0000 | 0.0013 | 0.0116 | 0.0399 | 0.1000 |
| delta | actual | 1-3 | - | 0.0000 | M | 128 | -0.0004 | -0.0000 | -0.0000 | 0.0000 | 0.0034 |  |  |
| delta | actual | 1-3 | linear | 0.0000 | tau | 128 | -0.0058 | -0.0079 | -0.0026 | -0.0014 | -0.0005 | 0.0000 | 0.5000 |
| delta | actual | 1-3 | linear | 0.5000 | tau | 128 | -0.0057 | -0.0083 | -0.0028 | -0.0016 | -0.0008 | 0.0234 | 0.5000 |
| delta | actual | 1-3 | linear | 0.8000 | tau | 128 | -0.0056 | -0.0083 | -0.0030 | -0.0018 | -0.0008 | 0.0312 | 0.5000 |
| delta | actual | 1-3 | concave | 0.0000 | tau | 128 | -0.0033 | -0.0047 | -0.0015 | -0.0004 | 0.0014 | 0.0000 | 0.6599 |
| delta | actual | 1-3 | concave | 0.5000 | tau | 128 | -0.0032 | -0.0044 | -0.0015 | -0.0006 | -0.0000 | 0.0781 | 0.6599 |
| delta | actual | 1-3 | concave | 0.8000 | tau | 128 | -0.0031 | -0.0044 | -0.0015 | -0.0008 | -0.0004 | 0.1406 | 0.6599 |
| delta | actual | 1-3 | convex | 0.0000 | tau | 128 | -0.0093 | -0.0145 | -0.0049 | -0.0030 | -0.0014 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | convex | 0.5000 | tau | 128 | -0.0093 | -0.0132 | -0.0051 | -0.0031 | -0.0014 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | convex | 0.8000 | tau | 128 | -0.0092 | -0.0123 | -0.0052 | -0.0031 | -0.0014 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | top3_stress | 0.0000 | tau | 128 | -0.0103 | -0.0164 | -0.0039 | -0.0005 | -0.0000 | 0.0000 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.5000 | tau | 128 | -0.0102 | -0.0164 | -0.0042 | -0.0005 | -0.0000 | 0.0078 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.8000 | tau | 128 | -0.0102 | -0.0165 | -0.0042 | -0.0005 | -0.0000 | 0.0078 | 0.1000 |
| delta | actual | 4-10 | - | 0.0000 | M | 295 | -0.0036 | -0.0006 | 0.0000 | 0.0000 | 0.0033 |  |  |
| delta | actual | 4-10 | linear | 0.0000 | tau | 295 | -0.0133 | -0.0204 | -0.0118 | -0.0053 | 0.0000 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | linear | 0.5000 | tau | 295 | -0.0124 | -0.0189 | -0.0112 | -0.0060 | 0.0000 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | linear | 0.8000 | tau | 295 | -0.0118 | -0.0175 | -0.0108 | -0.0062 | 0.0000 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | concave | 0.0000 | tau | 295 | -0.0091 | -0.0134 | -0.0068 | -0.0026 | 0.0000 | 0.0000 | 0.6599 |
| delta | actual | 4-10 | concave | 0.5000 | tau | 295 | -0.0080 | -0.0126 | -0.0067 | -0.0027 | 0.0000 | 0.0441 | 0.6599 |
| delta | actual | 4-10 | concave | 0.8000 | tau | 295 | -0.0073 | -0.0115 | -0.0065 | -0.0032 | 0.0000 | 0.0644 | 0.6599 |
| delta | actual | 4-10 | convex | 0.0000 | tau | 295 | -0.0184 | -0.0271 | -0.0176 | -0.0101 | 0.0000 | 0.0000 | 0.3391 |
| delta | actual | 4-10 | convex | 0.5000 | tau | 295 | -0.0178 | -0.0265 | -0.0174 | -0.0102 | 0.0000 | 0.0102 | 0.3391 |
| delta | actual | 4-10 | convex | 0.8000 | tau | 295 | -0.0174 | -0.0258 | -0.0158 | -0.0100 | -0.0000 | 0.0169 | 0.3391 |
| delta | actual | 4-10 | top3_stress | 0.0000 | tau | 295 | -0.0160 | -0.0215 | -0.0155 | -0.0089 | 0.0000 | 0.0000 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.5000 | tau | 295 | -0.0158 | -0.0215 | -0.0150 | -0.0087 | 0.0000 | 0.0034 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.8000 | tau | 295 | -0.0157 | -0.0216 | -0.0150 | -0.0085 | 0.0000 | 0.0068 | 0.1000 |
| delta | actual | 11-16 | - | 0.0000 | M | 243 | -0.0021 | -0.0000 | 0.0000 | 0.0000 | 0.0008 |  |  |
| delta | actual | 11-16 | linear | 0.0000 | tau | 243 | -0.0010 | -0.0106 | 0.0000 | 0.0068 | 0.0189 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | linear | 0.5000 | tau | 243 | -0.0005 | -0.0098 | 0.0000 | 0.0065 | 0.0165 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | linear | 0.8000 | tau | 243 | -0.0002 | -0.0088 | 0.0000 | 0.0061 | 0.0141 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | concave | 0.0000 | tau | 243 | -0.0018 | -0.0075 | 0.0000 | 0.0038 | 0.0125 | 0.0000 | 0.6599 |
| delta | actual | 11-16 | concave | 0.5000 | tau | 243 | -0.0011 | -0.0072 | 0.0000 | 0.0038 | 0.0110 | 0.0041 | 0.6599 |
| delta | actual | 11-16 | concave | 0.8000 | tau | 243 | -0.0007 | -0.0065 | 0.0000 | 0.0035 | 0.0104 | 0.0082 | 0.6599 |
| delta | actual | 11-16 | convex | 0.0000 | tau | 243 | 0.0011 | -0.0107 | 0.0000 | 0.0108 | 0.0223 | 0.0000 | 0.3391 |
| delta | actual | 11-16 | convex | 0.5000 | tau | 243 | 0.0015 | -0.0095 | 0.0000 | 0.0106 | 0.0199 | 0.0082 | 0.3391 |
| delta | actual | 11-16 | convex | 0.8000 | tau | 243 | 0.0017 | -0.0091 | 0.0000 | 0.0104 | 0.0198 | 0.0123 | 0.3391 |
| delta | actual | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0073 | 0.0000 | 0.0036 | 0.0132 | 0.0212 | 0.0000 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0074 | 0.0000 | 0.0039 | 0.0132 | 0.0217 | 0.0412 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0075 | 0.0000 | 0.0043 | 0.0133 | 0.0211 | 0.0412 | 0.1000 |
| delta | actual | 17-30 | - | 0.0000 | M | 586 | 0.0030 | 0.0000 | 0.0000 | 0.0000 | 0.0110 |  |  |
| delta | actual | 17-30 | linear | 0.0000 | tau | 586 | 0.0049 | 0.0000 | 0.0000 | 0.0041 | 0.0174 | 0.0000 | 0.5000 |
| delta | actual | 17-30 | linear | 0.5000 | tau | 586 | 0.0041 | 0.0000 | 0.0000 | 0.0041 | 0.0141 | 0.0085 | 0.5000 |
| delta | actual | 17-30 | linear | 0.8000 | tau | 586 | 0.0036 | 0.0000 | 0.0000 | 0.0040 | 0.0131 | 0.0119 | 0.5000 |
| delta | actual | 17-30 | concave | 0.0000 | tau | 586 | 0.0042 | 0.0000 | 0.0000 | 0.0030 | 0.0150 | 0.0000 | 0.6599 |
| delta | actual | 17-30 | concave | 0.5000 | tau | 586 | 0.0032 | 0.0000 | 0.0000 | 0.0027 | 0.0113 | 0.0102 | 0.6599 |
| delta | actual | 17-30 | concave | 0.8000 | tau | 586 | 0.0026 | 0.0000 | 0.0000 | 0.0026 | 0.0090 | 0.0205 | 0.6599 |
| delta | actual | 17-30 | convex | 0.0000 | tau | 586 | 0.0055 | 0.0000 | 0.0000 | 0.0058 | 0.0190 | 0.0000 | 0.3391 |
| delta | actual | 17-30 | convex | 0.5000 | tau | 586 | 0.0049 | 0.0000 | 0.0000 | 0.0055 | 0.0174 | 0.0017 | 0.3391 |
| delta | actual | 17-30 | convex | 0.8000 | tau | 586 | 0.0046 | 0.0000 | 0.0000 | 0.0055 | 0.0161 | 0.0017 | 0.3391 |
| delta | actual | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0030 | 0.0000 | 0.0000 | 0.0025 | 0.0109 | 0.0000 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0029 | 0.0000 | 0.0000 | 0.0025 | 0.0105 | 0.0631 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0028 | 0.0000 | 0.0000 | 0.0026 | 0.0104 | 0.0631 | 0.1000 |
| delta | own | all | - | 0.0000 | M | 1252 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | all | linear | 0.0000 | tau | 1252 | -0.0007 | -0.0078 | 0.0000 | 0.0037 | 0.0140 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.5000 | tau | 1252 | -0.0007 | -0.0078 | 0.0000 | 0.0037 | 0.0140 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.8000 | tau | 1252 | -0.0007 | -0.0078 | 0.0000 | 0.0037 | 0.0140 | 0.0000 | 0.5000 |
| delta | own | all | concave | 0.0000 | tau | 1252 | -0.0004 | -0.0045 | 0.0000 | 0.0021 | 0.0081 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.5000 | tau | 1252 | -0.0004 | -0.0045 | 0.0000 | 0.0021 | 0.0081 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.8000 | tau | 1252 | -0.0004 | -0.0045 | 0.0000 | 0.0021 | 0.0081 | 0.0000 | 0.6599 |
| delta | own | all | convex | 0.0000 | tau | 1252 | -0.0010 | -0.0118 | 0.0000 | 0.0063 | 0.0202 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.5000 | tau | 1252 | -0.0010 | -0.0118 | 0.0000 | 0.0063 | 0.0202 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.8000 | tau | 1252 | -0.0010 | -0.0118 | 0.0000 | 0.0063 | 0.0202 | 0.0000 | 0.3391 |
| delta | own | all | top3_stress | 0.0000 | tau | 1252 | -0.0005 | -0.0084 | 0.0000 | 0.0054 | 0.0172 | 0.0000 | 0.1000 |
| delta | own | all | top3_stress | 0.5000 | tau | 1252 | -0.0005 | -0.0084 | 0.0000 | 0.0054 | 0.0172 | 0.0160 | 0.1000 |
| delta | own | all | top3_stress | 0.8000 | tau | 1252 | -0.0005 | -0.0084 | 0.0000 | 0.0054 | 0.0172 | 0.0160 | 0.1000 |
| delta | own | 1-3 | - | 0.0000 | M | 128 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 1-3 | linear | 0.0000 | tau | 128 | -0.0049 | -0.0066 | -0.0033 | -0.0020 | -0.0015 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.5000 | tau | 128 | -0.0049 | -0.0066 | -0.0033 | -0.0020 | -0.0015 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.8000 | tau | 128 | -0.0049 | -0.0066 | -0.0033 | -0.0020 | -0.0015 | 0.0000 | 0.5000 |
| delta | own | 1-3 | concave | 0.0000 | tau | 128 | -0.0026 | -0.0034 | -0.0018 | -0.0011 | -0.0008 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.5000 | tau | 128 | -0.0026 | -0.0034 | -0.0018 | -0.0011 | -0.0008 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.8000 | tau | 128 | -0.0026 | -0.0034 | -0.0018 | -0.0011 | -0.0008 | 0.0000 | 0.6599 |
| delta | own | 1-3 | convex | 0.0000 | tau | 128 | -0.0086 | -0.0116 | -0.0057 | -0.0035 | -0.0025 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.5000 | tau | 128 | -0.0086 | -0.0116 | -0.0057 | -0.0035 | -0.0025 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.8000 | tau | 128 | -0.0086 | -0.0116 | -0.0057 | -0.0035 | -0.0025 | 0.0000 | 0.3391 |
| delta | own | 1-3 | top3_stress | 0.0000 | tau | 128 | -0.0101 | -0.0167 | -0.0039 | -0.0005 | -0.0000 | 0.0000 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.5000 | tau | 128 | -0.0101 | -0.0167 | -0.0039 | -0.0005 | -0.0000 | 0.0000 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.8000 | tau | 128 | -0.0101 | -0.0167 | -0.0039 | -0.0005 | -0.0000 | 0.0000 | 0.1000 |
| delta | own | 4-10 | - | 0.0000 | M | 295 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 4-10 | linear | 0.0000 | tau | 295 | -0.0125 | -0.0175 | -0.0109 | -0.0074 | -0.0044 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.5000 | tau | 295 | -0.0125 | -0.0175 | -0.0109 | -0.0074 | -0.0044 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.8000 | tau | 295 | -0.0125 | -0.0175 | -0.0109 | -0.0074 | -0.0044 | 0.0000 | 0.5000 |
| delta | own | 4-10 | concave | 0.0000 | tau | 295 | -0.0072 | -0.0102 | -0.0060 | -0.0042 | -0.0024 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.5000 | tau | 295 | -0.0072 | -0.0102 | -0.0060 | -0.0042 | -0.0024 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.8000 | tau | 295 | -0.0072 | -0.0102 | -0.0060 | -0.0042 | -0.0024 | 0.0000 | 0.6599 |
| delta | own | 4-10 | convex | 0.0000 | tau | 295 | -0.0192 | -0.0261 | -0.0176 | -0.0118 | -0.0075 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.5000 | tau | 295 | -0.0192 | -0.0261 | -0.0176 | -0.0118 | -0.0075 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.8000 | tau | 295 | -0.0192 | -0.0261 | -0.0176 | -0.0118 | -0.0075 | 0.0000 | 0.3391 |
| delta | own | 4-10 | top3_stress | 0.0000 | tau | 295 | -0.0168 | -0.0217 | -0.0164 | -0.0103 | -0.0047 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.5000 | tau | 295 | -0.0168 | -0.0217 | -0.0164 | -0.0103 | -0.0047 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.8000 | tau | 295 | -0.0168 | -0.0217 | -0.0164 | -0.0103 | -0.0047 | 0.0000 | 0.1000 |
| delta | own | 11-16 | - | 0.0000 | M | 243 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 11-16 | linear | 0.0000 | tau | 243 | 0.0015 | -0.0104 | 0.0025 | 0.0094 | 0.0188 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.5000 | tau | 243 | 0.0015 | -0.0104 | 0.0025 | 0.0094 | 0.0188 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.8000 | tau | 243 | 0.0015 | -0.0104 | 0.0025 | 0.0094 | 0.0188 | 0.0000 | 0.5000 |
| delta | own | 11-16 | concave | 0.0000 | tau | 243 | 0.0004 | -0.0070 | 0.0010 | 0.0052 | 0.0107 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.5000 | tau | 243 | 0.0004 | -0.0070 | 0.0010 | 0.0052 | 0.0107 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.8000 | tau | 243 | 0.0004 | -0.0070 | 0.0010 | 0.0052 | 0.0107 | 0.0000 | 0.6599 |
| delta | own | 11-16 | convex | 0.0000 | tau | 243 | 0.0044 | -0.0116 | 0.0051 | 0.0162 | 0.0290 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.5000 | tau | 243 | 0.0044 | -0.0116 | 0.0051 | 0.0162 | 0.0290 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.8000 | tau | 243 | 0.0044 | -0.0116 | 0.0051 | 0.0162 | 0.0290 | 0.0000 | 0.3391 |
| delta | own | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0111 | 0.0000 | 0.0097 | 0.0179 | 0.0279 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0111 | 0.0000 | 0.0097 | 0.0179 | 0.0279 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0111 | 0.0000 | 0.0097 | 0.0179 | 0.0279 | 0.0000 | 0.1000 |
| delta | own | 17-30 | - | 0.0000 | M | 586 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 17-30 | linear | 0.0000 | tau | 586 | 0.0053 | 0.0000 | 0.0002 | 0.0082 | 0.0175 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.5000 | tau | 586 | 0.0053 | 0.0000 | 0.0002 | 0.0082 | 0.0175 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.8000 | tau | 586 | 0.0053 | 0.0000 | 0.0002 | 0.0082 | 0.0175 | 0.0000 | 0.5000 |
| delta | own | 17-30 | concave | 0.0000 | tau | 586 | 0.0032 | 0.0000 | 0.0001 | 0.0051 | 0.0101 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.5000 | tau | 586 | 0.0032 | 0.0000 | 0.0001 | 0.0051 | 0.0101 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.8000 | tau | 586 | 0.0032 | 0.0000 | 0.0001 | 0.0051 | 0.0101 | 0.0000 | 0.6599 |
| delta | own | 17-30 | convex | 0.0000 | tau | 586 | 0.0075 | 0.0000 | 0.0004 | 0.0107 | 0.0240 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.5000 | tau | 586 | 0.0075 | 0.0000 | 0.0004 | 0.0107 | 0.0240 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.8000 | tau | 586 | 0.0075 | 0.0000 | 0.0004 | 0.0107 | 0.0240 | 0.0000 | 0.3391 |
| delta | own | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0049 | 0.0000 | 0.0002 | 0.0064 | 0.0171 | 0.0000 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0049 | 0.0000 | 0.0002 | 0.0064 | 0.0171 | 0.0341 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0049 | 0.0000 | 0.0002 | 0.0064 | 0.0171 | 0.0341 | 0.1000 |

## T5_attr_seeding

| rule | portfolio | seed_group | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| old | actual | <0.01 | B | dominance_positive | 0.7182 | 0.5937 | 0.8190 | 369 |
| old | actual | <0.01 | B | reversal | 0.0515 | 0.0133 | 0.0843 | 369 |
| old | actual | <0.01 | B | negligible | 0.1816 | 0.0833 | 0.2958 | 369 |
| old | actual | <0.01 | B | unresolved | 0.0488 | 0.0205 | 0.0885 | 369 |
| old | actual | 0.01-0.05 | B | dominance_positive | 0.7215 | 0.5362 | 0.9265 | 79 |
| old | actual | 0.01-0.05 | B | reversal | 0.0506 | 0.0000 | 0.1477 | 79 |
| old | actual | 0.01-0.05 | B | negligible | 0.2278 | 0.0597 | 0.3810 | 79 |
| old | actual | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | actual | >=0.05 | B | dominance_positive | 0.7164 | 0.5889 | 0.8190 | 804 |
| old | actual | >=0.05 | B | reversal | 0.0311 | 0.0077 | 0.0663 | 804 |
| old | actual | >=0.05 | B | negligible | 0.2438 | 0.1603 | 0.3444 | 804 |
| old | actual | >=0.05 | B | unresolved | 0.0087 | 0.0000 | 0.0276 | 804 |
| old | own | <0.01 | B | dominance_positive | 0.8997 | 0.7988 | 0.9863 | 369 |
| old | own | <0.01 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 369 |
| old | own | <0.01 | B | negligible | 0.1003 | 0.0137 | 0.2012 | 369 |
| old | own | <0.01 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 369 |
| old | own | 0.01-0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 79 |
| old | own | 0.01-0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | own | 0.01-0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | own | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | own | >=0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 804 |
| old | own | >=0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 804 |
| old | own | >=0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 804 |
| old | own | >=0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 804 |
| new | actual | <0.01 | B | dominance_positive | 0.1165 | 0.0513 | 0.1858 | 369 |
| new | actual | <0.01 | B | reversal | 0.3550 | 0.2105 | 0.4984 | 369 |
| new | actual | <0.01 | B | negligible | 0.4472 | 0.3050 | 0.6000 | 369 |
| new | actual | <0.01 | B | unresolved | 0.0813 | 0.0307 | 0.1559 | 369 |
| new | actual | 0.01-0.05 | B | dominance_positive | 0.6076 | 0.4091 | 0.8696 | 79 |
| new | actual | 0.01-0.05 | B | reversal | 0.0380 | 0.0000 | 0.1447 | 79 |
| new | actual | 0.01-0.05 | B | negligible | 0.3544 | 0.0897 | 0.5618 | 79 |
| new | actual | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | actual | >=0.05 | B | dominance_positive | 0.7338 | 0.6294 | 0.8109 | 804 |
| new | actual | >=0.05 | B | reversal | 0.0348 | 0.0095 | 0.0631 | 804 |
| new | actual | >=0.05 | B | negligible | 0.2251 | 0.1516 | 0.3173 | 804 |
| new | actual | >=0.05 | B | unresolved | 0.0062 | 0.0000 | 0.0151 | 804 |
| new | own | <0.01 | B | dominance_positive | 0.1545 | 0.0827 | 0.2339 | 369 |
| new | own | <0.01 | B | reversal | 0.3523 | 0.1946 | 0.5107 | 369 |
| new | own | <0.01 | B | negligible | 0.4851 | 0.3484 | 0.6364 | 369 |
| new | own | <0.01 | B | unresolved | 0.0081 | 0.0000 | 0.0264 | 369 |
| new | own | 0.01-0.05 | B | dominance_positive | 0.8481 | 0.6349 | 1.0000 | 79 |
| new | own | 0.01-0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | own | 0.01-0.05 | B | negligible | 0.1519 | 0.0000 | 0.3651 | 79 |
| new | own | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | own | >=0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 804 |
| new | own | >=0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 804 |
| new | own | >=0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 804 |
| new | own | >=0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 804 |

## T5_attr_ledger_features

| rule | feature | value | n | reversal_share | lo99 | hi99 |
|---|---|---|---|---|---|---|
| old | holds_conditional_other | True | 529 | 0.0907 | 0.0429 | 0.1390 |
| old | holds_conditional_other | False | 723 | 0.0000 | 0.0000 | 0.0000 |
| old | holds_opponent_pick | True | 43 | 0.4651 | 0.2400 | 0.6970 |
| old | holds_opponent_pick | False | 1209 | 0.0232 | 0.0081 | 0.0419 |
| old | holds_pooled_pick | True | 379 | 0.0660 | 0.0030 | 0.1706 |
| old | holds_pooled_pick | False | 873 | 0.0263 | 0.0060 | 0.0486 |
| old | self_restricted | True | 103 | 0.0388 | 0.0000 | 0.1074 |
| old | self_restricted | False | 1149 | 0.0383 | 0.0162 | 0.0632 |
| old | opp_restricted | True | 103 | 0.0291 | 0.0000 | 0.0938 |
| old | opp_restricted | False | 1149 | 0.0392 | 0.0162 | 0.0678 |
| old | holds_conditional_other_state | True | 472 | 0.0996 | 0.0471 | 0.1592 |
| old | holds_conditional_other_state | False | 780 | 0.0013 | 0.0000 | 0.0075 |
| old | holds_opponent_pick_state | True | 39 | 0.5128 | 0.2593 | 0.7436 |
| old | holds_opponent_pick_state | False | 1213 | 0.0231 | 0.0081 | 0.0417 |
| new | holds_conditional_other | True | 529 | 0.1796 | 0.0880 | 0.2505 |
| new | holds_conditional_other | False | 723 | 0.0927 | 0.0398 | 0.1545 |
| new | holds_opponent_pick | True | 43 | 0.4884 | 0.2449 | 0.7778 |
| new | holds_opponent_pick | False | 1209 | 0.1166 | 0.0559 | 0.1565 |
| new | holds_pooled_pick | True | 379 | 0.1372 | 0.0297 | 0.2422 |
| new | holds_pooled_pick | False | 873 | 0.1260 | 0.0639 | 0.1912 |
| new | self_restricted | True | 103 | 0.1845 | 0.0090 | 0.3805 |
| new | self_restricted | False | 1149 | 0.1245 | 0.0571 | 0.1751 |
| new | opp_restricted | True | 103 | 0.0874 | 0.0000 | 0.1979 |
| new | opp_restricted | False | 1149 | 0.1332 | 0.0671 | 0.1768 |
| new | holds_conditional_other_state | True | 500 | 0.1700 | 0.0865 | 0.2311 |
| new | holds_conditional_other_state | False | 752 | 0.1024 | 0.0433 | 0.1628 |
| new | holds_opponent_pick_state | True | 40 | 0.5000 | 0.2542 | 0.7667 |
| new | holds_opponent_pick_state | False | 1212 | 0.1172 | 0.0562 | 0.1575 |

## T5_6_transitions

| portfolio | old | new | count |
|---|---|---|---|
| actual | dominance_positive | dominance_positive | 644 |
| actual | dominance_positive | negligible | 116 |
| actual | dominance_positive | reversal | 117 |
| actual | dominance_positive | unresolved | 21 |
| actual | negligible | dominance_positive | 27 |
| actual | negligible | negligible | 250 |
| actual | negligible | reversal | 3 |
| actual | negligible | unresolved | 1 |
| actual | reversal | dominance_positive | 4 |
| actual | reversal | negligible | 4 |
| actual | reversal | reversal | 38 |
| actual | reversal | unresolved | 2 |
| actual | unresolved | dominance_positive | 6 |
| actual | unresolved | negligible | 4 |
| actual | unresolved | reversal | 4 |
| actual | unresolved | unresolved | 11 |
| own | dominance_positive | dominance_positive | 928 |
| own | dominance_positive | negligible | 154 |
| own | dominance_positive | reversal | 130 |
| own | dominance_positive | unresolved | 3 |
| own | negligible | negligible | 37 |

## T5_headline_reversal_diff

| contrast | portfolio | verdict | share_a | share_b | diff | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| new_minus_old | actual | verdict_B | 0.1294 | 0.0383 | 0.0911 | 0.0392 | 0.1312 | 1252 |
| new_minus_old | actual | verdict_B_pm | 0.1078 | 0.0272 | 0.0807 | 0.0381 | 0.1102 | 1252 |
| new_minus_old | own | verdict_B | 0.1038 | 0.0000 | 0.1038 | 0.0506 | 0.1441 | 1252 |
| new_minus_old | own | verdict_B_pm | 0.0950 | 0.0000 | 0.0950 | 0.0461 | 0.1344 | 1252 |
| actual_minus_own | old | verdict_B | 0.0383 | 0.0000 | 0.0383 | 0.0165 | 0.0632 | 1252 |
| actual_minus_own | new | verdict_B | 0.1294 | 0.1038 | 0.0256 | 0.0062 | 0.0477 | 1252 |

## T5_4_typology

| rule | curve | type | share | lo99 | hi99 | n | tp_dominated_share | n_tp_defined |
|---|---|---|---|---|---|---|---|---|
| old | linear | both_lose | 0.4649 | 0.2982 | 0.6457 | 291 | 0.2818 | 291 |
| old | linear | both_win | 0.0016 | 0.0000 | 0.0097 | 1 | 0.0000 | 1 |
| old | linear | normal | 0.3914 | 0.2968 | 0.4663 | 245 | 0.7510 | 245 |
| old | linear | opposed | 0.0176 | 0.0016 | 0.0408 | 11 | 0.9091 | 11 |
| old | linear | one_sided_win | 0.0144 | 0.0000 | 0.0344 | 9 | 0.7778 | 9 |
| old | linear | no_own_stake | 0.1102 | 0.0347 | 0.2083 | 69 | 1.0000 | 59 |
| old | concave | both_lose | 0.4185 | 0.2574 | 0.6014 | 262 | 0.3282 | 262 |
| old | concave | both_win | 0.0016 | 0.0000 | 0.0097 | 1 | 0.0000 | 1 |
| old | concave | normal | 0.4121 | 0.3176 | 0.4983 | 258 | 0.7237 | 257 |
| old | concave | opposed | 0.0192 | 0.0048 | 0.0386 | 12 | 0.7500 | 12 |
| old | concave | one_sided_win | 0.0144 | 0.0000 | 0.0365 | 9 | 0.7778 | 9 |
| old | concave | no_own_stake | 0.1342 | 0.0479 | 0.2456 | 84 | 1.0000 | 70 |
| old | convex | both_lose | 0.4665 | 0.3379 | 0.5917 | 292 | 0.2295 | 292 |
| old | convex | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| old | convex | normal | 0.4058 | 0.3403 | 0.4654 | 254 | 0.6482 | 253 |
| old | convex | opposed | 0.0112 | 0.0000 | 0.0281 | 7 | 0.8571 | 7 |
| old | convex | one_sided_win | 0.0128 | 0.0000 | 0.0353 | 8 | 0.6250 | 8 |
| old | convex | no_own_stake | 0.1038 | 0.0434 | 0.1872 | 65 | 1.0000 | 48 |
| old | top3_stress | both_lose | 0.1885 | 0.1321 | 0.2666 | 118 | 0.0085 | 118 |
| old | top3_stress | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| old | top3_stress | normal | 0.4521 | 0.3870 | 0.5351 | 283 | 0.1321 | 280 |
| old | top3_stress | opposed | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| old | top3_stress | one_sided_win | 0.0032 | 0.0000 | 0.0132 | 2 | 0.5000 | 2 |
| old | top3_stress | no_own_stake | 0.3562 | 0.2710 | 0.4299 | 223 | 1.0000 | 40 |
| new | linear | both_lose | 0.2780 | 0.1627 | 0.3860 | 174 | 0.2644 | 174 |
| new | linear | both_win | 0.0048 | 0.0000 | 0.0182 | 3 | 0.3333 | 3 |
| new | linear | normal | 0.3946 | 0.3307 | 0.4708 | 247 | 0.6073 | 247 |
| new | linear | opposed | 0.0799 | 0.0239 | 0.1458 | 50 | 0.4800 | 50 |
| new | linear | one_sided_win | 0.0399 | 0.0065 | 0.0901 | 25 | 0.7600 | 25 |
| new | linear | no_own_stake | 0.2029 | 0.0978 | 0.3216 | 127 | 1.0000 | 80 |
| new | concave | both_lose | 0.2939 | 0.1796 | 0.3922 | 184 | 0.3261 | 184 |
| new | concave | both_win | 0.0016 | 0.0000 | 0.0097 | 1 | 0.0000 | 1 |
| new | concave | normal | 0.4201 | 0.3494 | 0.4864 | 263 | 0.6743 | 261 |
| new | concave | opposed | 0.0463 | 0.0145 | 0.0864 | 29 | 0.5862 | 29 |
| new | concave | one_sided_win | 0.0319 | 0.0036 | 0.0745 | 20 | 0.7500 | 20 |
| new | concave | no_own_stake | 0.2061 | 0.1083 | 0.3291 | 129 | 1.0000 | 85 |
| new | convex | both_lose | 0.2460 | 0.1424 | 0.3604 | 154 | 0.2143 | 154 |
| new | convex | both_win | 0.0048 | 0.0000 | 0.0181 | 3 | 0.0000 | 3 |
| new | convex | normal | 0.3866 | 0.3116 | 0.4666 | 242 | 0.5248 | 242 |
| new | convex | opposed | 0.0863 | 0.0229 | 0.1611 | 54 | 0.2778 | 54 |
| new | convex | one_sided_win | 0.0575 | 0.0190 | 0.1007 | 36 | 0.6111 | 36 |
| new | convex | no_own_stake | 0.2188 | 0.1216 | 0.3246 | 137 | 1.0000 | 68 |
| new | top3_stress | both_lose | 0.1294 | 0.0731 | 0.1908 | 81 | 0.0247 | 81 |
| new | top3_stress | both_win | 0.0064 | 0.0000 | 0.0216 | 4 | 0.0000 | 4 |
| new | top3_stress | normal | 0.3339 | 0.2537 | 0.4405 | 209 | 0.2244 | 205 |
| new | top3_stress | opposed | 0.0639 | 0.0211 | 0.1109 | 40 | 0.0500 | 40 |
| new | top3_stress | one_sided_win | 0.1182 | 0.0484 | 0.1829 | 74 | 0.2535 | 71 |
| new | top3_stress | no_own_stake | 0.3482 | 0.2638 | 0.4409 | 218 | 1.0000 | 62 |

## T5_5_stakes_distribution

| rule | curve | measure | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| old | linear | tp_share | 616 | 0.5675 | 0.4085 | 0.5300 | 0.7592 | 1.0000 |
| old | linear | tp_share_raw | 620 | 0.6194 | 0.4945 | 0.5805 | 0.7795 | 0.9442 |
| old | linear | hhi | 616 | 0.3084 | 0.2141 | 0.2787 | 0.3628 | 0.4945 |
| old | linear | n_material | 626 | 6.4712 | 4.0000 | 7.0000 | 9.0000 | 10.0000 |
| old | linear | mean_abs_third | 626 | 0.0017 | 0.0008 | 0.0015 | 0.0023 | 0.0034 |
| old | linear | mean_abs_third_raw | 626 | 0.0021 | 0.0012 | 0.0018 | 0.0027 | 0.0036 |
| old | concave | tp_share | 611 | 0.5920 | 0.4288 | 0.5569 | 0.8074 | 1.0000 |
| old | concave | tp_share_raw | 619 | 0.6441 | 0.5002 | 0.6096 | 0.8200 | 0.9567 |
| old | concave | hhi | 611 | 0.3139 | 0.2131 | 0.2797 | 0.3753 | 0.5000 |
| old | concave | n_material | 626 | 5.9281 | 4.0000 | 6.0000 | 8.0000 | 10.0000 |
| old | concave | mean_abs_third | 626 | 0.0018 | 0.0008 | 0.0016 | 0.0025 | 0.0035 |
| old | concave | mean_abs_third_raw | 626 | 0.0022 | 0.0012 | 0.0019 | 0.0028 | 0.0038 |
| old | convex | tp_share | 608 | 0.5072 | 0.3608 | 0.4887 | 0.6805 | 0.9261 |
| old | convex | tp_share_raw | 618 | 0.5958 | 0.4869 | 0.5464 | 0.7368 | 0.9235 |
| old | convex | hhi | 608 | 0.3627 | 0.2425 | 0.3151 | 0.4103 | 0.5277 |
| old | convex | n_material | 626 | 5.4649 | 3.0000 | 5.0000 | 8.0000 | 9.0000 |
| old | convex | mean_abs_third | 626 | 0.0013 | 0.0005 | 0.0011 | 0.0018 | 0.0027 |
| old | convex | mean_abs_third_raw | 626 | 0.0016 | 0.0009 | 0.0015 | 0.0022 | 0.0030 |
| old | top3_stress | tp_share | 440 | 0.3779 | 0.1761 | 0.4036 | 0.4765 | 0.7989 |
| old | top3_stress | tp_share_raw | 490 | 0.5317 | 0.4831 | 0.5014 | 0.5254 | 0.8586 |
| old | top3_stress | hhi | 440 | 0.5289 | 0.3582 | 0.4519 | 0.5713 | 1.0000 |
| old | top3_stress | n_material | 626 | 2.2636 | 0.0000 | 2.0000 | 4.0000 | 5.0000 |
| old | top3_stress | mean_abs_third | 626 | 0.0003 | 0.0000 | 0.0002 | 0.0005 | 0.0009 |
| old | top3_stress | mean_abs_third_raw | 626 | 0.0005 | 0.0001 | 0.0004 | 0.0007 | 0.0011 |
| new | linear | tp_share | 579 | 0.5897 | 0.4400 | 0.5226 | 0.7784 | 1.0000 |
| new | linear | tp_share_raw | 597 | 0.6358 | 0.5017 | 0.5825 | 0.8003 | 0.9764 |
| new | linear | hhi | 579 | 0.3145 | 0.2223 | 0.2981 | 0.3691 | 0.4961 |
| new | linear | n_material | 626 | 5.7891 | 3.0000 | 6.0000 | 8.0000 | 10.0000 |
| new | linear | mean_abs_third | 626 | 0.0017 | 0.0006 | 0.0013 | 0.0023 | 0.0037 |
| new | linear | mean_abs_third_raw | 626 | 0.0020 | 0.0009 | 0.0016 | 0.0026 | 0.0040 |
| new | concave | tp_share | 580 | 0.6100 | 0.4540 | 0.5544 | 0.8183 | 1.0000 |
| new | concave | tp_share_raw | 601 | 0.6507 | 0.5055 | 0.6066 | 0.8104 | 0.9823 |
| new | concave | hhi | 580 | 0.3092 | 0.2113 | 0.2903 | 0.3708 | 0.4699 |
| new | concave | n_material | 626 | 5.7412 | 4.0000 | 6.0000 | 8.0000 | 10.0000 |
| new | concave | mean_abs_third | 626 | 0.0018 | 0.0008 | 0.0015 | 0.0025 | 0.0036 |
| new | concave | mean_abs_third_raw | 626 | 0.0020 | 0.0011 | 0.0017 | 0.0028 | 0.0038 |
| new | convex | tp_share | 557 | 0.5373 | 0.3888 | 0.4933 | 0.7079 | 1.0000 |
| new | convex | tp_share_raw | 586 | 0.6159 | 0.5000 | 0.5513 | 0.7518 | 0.9634 |
| new | convex | hhi | 557 | 0.3846 | 0.2607 | 0.3304 | 0.4372 | 0.5681 |
| new | convex | n_material | 626 | 4.5958 | 2.0000 | 5.0000 | 7.0000 | 8.0000 |
| new | convex | mean_abs_third | 626 | 0.0014 | 0.0003 | 0.0009 | 0.0019 | 0.0033 |
| new | convex | mean_abs_third_raw | 626 | 0.0016 | 0.0005 | 0.0012 | 0.0022 | 0.0036 |
| new | top3_stress | tp_share | 463 | 0.4486 | 0.2782 | 0.4447 | 0.5239 | 1.0000 |
| new | top3_stress | tp_share_raw | 503 | 0.5811 | 0.4957 | 0.5043 | 0.6628 | 0.9794 |
| new | top3_stress | hhi | 463 | 0.4937 | 0.3381 | 0.4243 | 0.5196 | 1.0000 |
| new | top3_stress | n_material | 626 | 2.4345 | 0.0000 | 2.0000 | 4.0000 | 5.0000 |
| new | top3_stress | mean_abs_third | 626 | 0.0005 | 0.0000 | 0.0002 | 0.0007 | 0.0012 |
| new | top3_stress | mean_abs_third_raw | 626 | 0.0006 | 0.0001 | 0.0004 | 0.0009 | 0.0014 |
| new_minus_old | linear | tp_share | 579 | 0.0178 | -0.0268 | 0.0001 | 0.0765 | 0.1668 |
| new_minus_old | linear | hhi | 579 | 0.0187 | -0.0332 | 0.0015 | 0.0610 | 0.1452 |
| new_minus_old | linear | mean_abs_third | 626 | -0.0000 | -0.0004 | 0.0000 | 0.0004 | 0.0011 |
| new_minus_old | concave | tp_share | 578 | 0.0131 | -0.0285 | 0.0000 | 0.0707 | 0.1664 |
| new_minus_old | concave | hhi | 578 | 0.0077 | -0.0401 | 0.0000 | 0.0433 | 0.1194 |
| new_minus_old | concave | mean_abs_third | 626 | -0.0001 | -0.0003 | 0.0000 | 0.0004 | 0.0009 |
| new_minus_old | convex | tp_share | 557 | 0.0203 | -0.0523 | 0.0051 | 0.1013 | 0.2222 |
| new_minus_old | convex | hhi | 557 | 0.0349 | -0.0527 | 0.0025 | 0.0839 | 0.1956 |
| new_minus_old | convex | mean_abs_third | 626 | 0.0001 | -0.0005 | 0.0000 | 0.0005 | 0.0014 |
| new_minus_old | top3_stress | tp_share | 370 | 0.1071 | -0.0211 | 0.0588 | 0.2965 | 0.4721 |
| new_minus_old | top3_stress | hhi | 370 | -0.1010 | -0.3054 | -0.0469 | 0.0653 | 0.2490 |
| new_minus_old | top3_stress | mean_abs_third | 626 | 0.0002 | -0.0002 | 0.0000 | 0.0005 | 0.0010 |

## H2

| curve | sample | n_games | mean_diff_new_minus_old | lo99 | hi99 | registered | supported |
|---|---|---|---|---|---|---|---|
| linear | registered | 520 | -0.0000 | -0.0002 | 0.0002 | True | False |
| linear | state_conditional | 480 | 0.0000 | -0.0002 | 0.0002 | False | False |
| concave | registered | 520 | -0.0000 | -0.0003 | 0.0002 | False | False |
| concave | state_conditional | 480 | -0.0000 | -0.0003 | 0.0002 | False | False |
| convex | registered | 520 | 0.0001 | -0.0001 | 0.0003 | False | False |
| convex | state_conditional | 480 | 0.0001 | -0.0001 | 0.0003 | False | False |
| top3_stress | registered | 520 | 0.0002 | 0.0001 | 0.0004 | False | True |
| top3_stress | state_conditional | 480 | 0.0002 | 0.0001 | 0.0004 | False | True |

## F5_2_network_edges

10440 rows in `F5_2_network_edges.csv`.

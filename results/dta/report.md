# Registered analysis output

tag `dta`; exclude_imprecise=False; states=81

## T5_0_diagnostics

| states | games | stopped_2000 | stopped_8000 | stopped_32000 | missed_target | n_worlds_match | max_halfwidth_linear | max_halfwidth_linear_rules_only | max_halfwidth_delta_linear | p95_halfwidth_linear | max_q_total_dev | max_per_slot_dev | per_slot_noise_scale | max_own_slot_dev | max_zero_sum_dev |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 81 | 626 | 2 | 3 | 37 | 39 | 2000 | 0.0065 | 0.0063 | 0.0065 | 0.0049 | 0.0000 | 0.0066 | 0.0112 | 0.0000 | 0.0034 |

## T5_0b_zero_sum_by_curve

| curve | rule | max_zero_sum_dev | mean_zero_sum_dev | n_games |
|---|---|---|---|---|
| linear | old | 0.0009 | 0.0001 | 626 |
| linear | new | 0.0014 | 0.0001 | 626 |
| concave | old | 0.0005 | 0.0000 | 626 |
| concave | new | 0.0008 | 0.0001 | 626 |
| convex | old | 0.0016 | 0.0001 | 626 |
| convex | new | 0.0021 | 0.0002 | 626 |
| top3_stress | old | 0.0032 | 0.0004 | 626 |
| top3_stress | new | 0.0034 | 0.0003 | 626 |

## T5_0c_verdict_by_look

| rule | portfolio | stopped_at | verdict_B | verdict_B_pm | count |
|---|---|---|---|---|---|
| delta | actual | 2000 | dominance_positive | dominance_positive | 1 |
| delta | actual | 2000 | negligible | negligible | 3 |
| delta | actual | 2000 | reversal | reversal | 5 |
| delta | actual | 2000 | unresolved | unresolved | 1 |
| delta | actual | 32000 | dominance_positive | dominance_positive | 39 |
| delta | actual | 32000 | dominance_positive | unresolved | 22 |
| delta | actual | 32000 | negligible | dominance_positive | 1 |
| delta | actual | 32000 | negligible | negligible | 157 |
| delta | actual | 32000 | negligible | unresolved | 11 |
| delta | actual | 32000 | reversal | reversal | 264 |
| delta | actual | 32000 | reversal | unresolved | 44 |
| delta | actual | 32000 | unresolved | unresolved | 14 |
| delta | actual | 8000 | dominance_positive | unresolved | 1 |
| delta | actual | 8000 | negligible | negligible | 8 |
| delta | actual | 8000 | negligible | unresolved | 2 |
| delta | actual | 8000 | reversal | reversal | 14 |
| delta | actual | 8000 | unresolved | unresolved | 1 |
| delta | actual | missed | dominance_positive | dominance_positive | 60 |
| delta | actual | missed | dominance_positive | unresolved | 34 |
| delta | actual | missed | negligible | negligible | 196 |
| delta | actual | missed | negligible | unresolved | 6 |
| delta | actual | missed | reversal | reversal | 313 |
| delta | actual | missed | reversal | unresolved | 38 |
| delta | actual | missed | unresolved | unresolved | 17 |
| delta | own | 2000 | negligible | negligible | 1 |
| delta | own | 2000 | reversal | reversal | 8 |
| delta | own | 2000 | unresolved | unresolved | 1 |
| delta | own | 32000 | dominance_positive | dominance_positive | 1 |
| delta | own | 32000 | dominance_positive | unresolved | 35 |
| delta | own | 32000 | negligible | negligible | 94 |
| delta | own | 32000 | negligible | unresolved | 17 |
| delta | own | 32000 | reversal | reversal | 308 |
| delta | own | 32000 | reversal | unresolved | 66 |
| delta | own | 32000 | unresolved | unresolved | 31 |
| delta | own | 8000 | dominance_positive | unresolved | 1 |
| delta | own | 8000 | negligible | negligible | 7 |
| delta | own | 8000 | negligible | unresolved | 1 |
| delta | own | 8000 | reversal | reversal | 15 |
| delta | own | 8000 | unresolved | unresolved | 2 |
| delta | own | missed | dominance_positive | dominance_positive | 5 |
| delta | own | missed | dominance_positive | unresolved | 38 |
| delta | own | missed | negligible | negligible | 136 |
| delta | own | missed | negligible | unresolved | 14 |
| delta | own | missed | reversal | reversal | 374 |
| delta | own | missed | reversal | unresolved | 65 |
| delta | own | missed | unresolved | unresolved | 32 |
| new | actual | 2000 | dominance_positive | dominance_positive | 3 |
| new | actual | 2000 | negligible | negligible | 3 |
| new | actual | 2000 | reversal | reversal | 3 |
| new | actual | 2000 | unresolved | unresolved | 1 |
| new | actual | 32000 | dominance_positive | dominance_positive | 298 |
| new | actual | 32000 | dominance_positive | unresolved | 14 |
| new | actual | 32000 | negligible | dominance_positive | 5 |
| new | actual | 32000 | negligible | negligible | 129 |
| new | actual | 32000 | negligible | unresolved | 10 |
| new | actual | 32000 | reversal | reversal | 63 |
| new | actual | 32000 | reversal | unresolved | 15 |
| new | actual | 32000 | unresolved | unresolved | 18 |
| new | actual | 8000 | dominance_positive | dominance_positive | 16 |
| new | actual | 8000 | negligible | negligible | 4 |
| new | actual | 8000 | reversal | reversal | 5 |
| new | actual | 8000 | unresolved | unresolved | 1 |
| new | actual | missed | dominance_positive | dominance_positive | 334 |
| new | actual | missed | dominance_positive | unresolved | 15 |
| new | actual | missed | negligible | dominance_positive | 2 |
| new | actual | missed | negligible | negligible | 203 |
| new | actual | missed | negligible | unresolved | 17 |
| new | actual | missed | reversal | reversal | 63 |
| new | actual | missed | reversal | unresolved | 14 |
| new | actual | missed | unresolved | unresolved | 16 |
| new | own | 2000 | dominance_positive | dominance_positive | 7 |
| new | own | 2000 | reversal | reversal | 2 |
| new | own | 2000 | unresolved | unresolved | 1 |
| new | own | 32000 | dominance_positive | dominance_positive | 413 |
| new | own | 32000 | dominance_positive | unresolved | 5 |
| new | own | 32000 | negligible | dominance_positive | 4 |
| new | own | 32000 | negligible | negligible | 53 |
| new | own | 32000 | negligible | unresolved | 6 |
| new | own | 32000 | reversal | reversal | 62 |
| new | own | 32000 | reversal | unresolved | 7 |
| new | own | 32000 | unresolved | unresolved | 2 |
| new | own | 8000 | dominance_positive | dominance_positive | 19 |
| new | own | 8000 | negligible | negligible | 2 |
| new | own | 8000 | reversal | reversal | 5 |
| new | own | missed | dominance_positive | dominance_positive | 475 |
| new | own | missed | dominance_positive | unresolved | 5 |
| new | own | missed | negligible | dominance_positive | 5 |
| new | own | missed | negligible | negligible | 117 |
| new | own | missed | negligible | unresolved | 4 |
| new | own | missed | reversal | reversal | 50 |
| new | own | missed | reversal | unresolved | 5 |
| new | own | missed | unresolved | unresolved | 3 |
| old | actual | 2000 | dominance_positive | dominance_positive | 5 |
| old | actual | 2000 | negligible | negligible | 3 |
| old | actual | 2000 | reversal | reversal | 1 |
| old | actual | 2000 | unresolved | unresolved | 1 |
| old | actual | 32000 | dominance_positive | dominance_positive | 385 |
| old | actual | 32000 | dominance_positive | unresolved | 24 |
| old | actual | 32000 | negligible | negligible | 108 |
| old | actual | 32000 | negligible | unresolved | 6 |
| old | actual | 32000 | reversal | reversal | 15 |
| old | actual | 32000 | reversal | unresolved | 3 |
| old | actual | 32000 | unresolved | unresolved | 11 |
| old | actual | 8000 | dominance_positive | dominance_positive | 20 |
| old | actual | 8000 | dominance_positive | unresolved | 3 |
| old | actual | 8000 | negligible | negligible | 3 |
| old | actual | missed | dominance_positive | dominance_positive | 431 |
| old | actual | missed | dominance_positive | unresolved | 30 |
| old | actual | missed | negligible | dominance_positive | 6 |
| old | actual | missed | negligible | negligible | 150 |
| old | actual | missed | negligible | unresolved | 5 |
| old | actual | missed | reversal | reversal | 18 |
| old | actual | missed | reversal | unresolved | 11 |
| old | actual | missed | unresolved | unresolved | 13 |
| old | own | 2000 | dominance_positive | dominance_positive | 10 |
| old | own | 32000 | dominance_positive | dominance_positive | 538 |
| old | own | 32000 | dominance_positive | unresolved | 3 |
| old | own | 32000 | negligible | negligible | 9 |
| old | own | 32000 | negligible | unresolved | 2 |
| old | own | 8000 | dominance_positive | dominance_positive | 26 |
| old | own | missed | dominance_positive | dominance_positive | 629 |
| old | own | missed | dominance_positive | unresolved | 9 |
| old | own | missed | negligible | negligible | 25 |
| old | own | missed | negligible | unresolved | 1 |

## T5_0d_band_width

| rule | portfolio | measure | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| old | actual | band_ratio | 1252 | 1.3801 | 0.2483 | 1.2404 | 2.4219 | 2.8677 |
| old | actual | band_ratio_pm | 1252 | 5.3387 | 0.9867 | 4.8874 | 9.5823 | 11.1408 |
| old | own | band_ratio | 1252 | 2.0121 | 0.9539 | 2.3254 | 2.7009 | 3.0828 |
| old | own | band_ratio_pm | 1252 | 7.7404 | 3.6242 | 9.2383 | 10.7146 | 12.1025 |
| new | actual | band_ratio | 1252 | 1.0662 | 0.0728 | 0.6242 | 2.1606 | 2.6552 |
| new | actual | band_ratio_pm | 1252 | 4.1149 | 0.2862 | 2.4134 | 8.2286 | 10.5326 |
| new | own | band_ratio | 1252 | 1.6062 | 0.2740 | 1.9774 | 2.5856 | 2.8992 |
| new | own | band_ratio_pm | 1252 | 6.1622 | 1.0732 | 7.8260 | 10.2602 | 11.3782 |
| delta | actual | band_ratio | 1252 | 1.0582 | 0.0497 | 0.7327 | 1.7911 | 2.5809 |
| delta | actual | band_ratio_pm | 1252 | 4.0992 | 0.1986 | 2.8203 | 6.9892 | 10.1858 |
| delta | own | band_ratio | 1252 | 1.3706 | 0.4329 | 1.1171 | 2.3135 | 2.8658 |
| delta | own | band_ratio_pm | 1252 | 5.2859 | 1.7104 | 4.2212 | 9.1444 | 11.3633 |

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
| new | actual | B | dominance_positive | 0.5431 | 0.4412 | 0.6335 | 1252 |
| new | actual | B | reversal | 0.1302 | 0.0664 | 0.1694 | 1252 |
| new | actual | B | negligible | 0.2979 | 0.2044 | 0.4002 | 1252 |
| new | actual | B | unresolved | 0.0288 | 0.0139 | 0.0497 | 1252 |
| new | actual | C | dominance_positive | 0.5431 | 0.4412 | 0.6335 | 1252 |
| new | actual | C | reversal | 0.1294 | 0.0664 | 0.1690 | 1252 |
| new | actual | C | negligible | 0.2979 | 0.2044 | 0.4002 | 1252 |
| new | actual | C | unresolved | 0.0296 | 0.0146 | 0.0502 | 1252 |
| new | actual | B_pm | dominance_positive | 0.5256 | 0.4251 | 0.6179 | 1252 |
| new | actual | B_pm | reversal | 0.1070 | 0.0551 | 0.1404 | 1252 |
| new | actual | B_pm | negligible | 0.2708 | 0.1903 | 0.3675 | 1252 |
| new | actual | B_pm | unresolved | 0.0966 | 0.0532 | 0.1586 | 1252 |
| new | actual | C_pm | dominance_positive | 0.5264 | 0.4254 | 0.6201 | 1252 |
| new | actual | C_pm | reversal | 0.1070 | 0.0551 | 0.1404 | 1252 |
| new | actual | C_pm | negligible | 0.2708 | 0.1903 | 0.3675 | 1252 |
| new | actual | C_pm | unresolved | 0.0958 | 0.0521 | 0.1586 | 1252 |
| new | own | B | dominance_positive | 0.7380 | 0.6667 | 0.8157 | 1252 |
| new | own | B | reversal | 0.1046 | 0.0506 | 0.1450 | 1252 |
| new | own | B | negligible | 0.1526 | 0.0887 | 0.2216 | 1252 |
| new | own | B | unresolved | 0.0048 | 0.0000 | 0.0131 | 1252 |
| new | own | C | dominance_positive | 0.7380 | 0.6667 | 0.8157 | 1252 |
| new | own | C | reversal | 0.1046 | 0.0506 | 0.1450 | 1252 |
| new | own | C | negligible | 0.1526 | 0.0887 | 0.2216 | 1252 |
| new | own | C | unresolved | 0.0048 | 0.0000 | 0.0131 | 1252 |
| new | own | B_pm | dominance_positive | 0.7372 | 0.6651 | 0.8165 | 1252 |
| new | own | B_pm | reversal | 0.0950 | 0.0461 | 0.1344 | 1252 |
| new | own | B_pm | negligible | 0.1374 | 0.0791 | 0.2057 | 1252 |
| new | own | B_pm | unresolved | 0.0304 | 0.0126 | 0.0519 | 1252 |
| new | own | C_pm | dominance_positive | 0.7372 | 0.6651 | 0.8165 | 1252 |
| new | own | C_pm | reversal | 0.0950 | 0.0461 | 0.1344 | 1252 |
| new | own | C_pm | negligible | 0.1374 | 0.0791 | 0.2057 | 1252 |
| new | own | C_pm | unresolved | 0.0304 | 0.0126 | 0.0519 | 1252 |
| delta | actual | B | dominance_positive | 0.1254 | 0.0777 | 0.1696 | 1252 |
| delta | actual | B | reversal | 0.5415 | 0.4841 | 0.5962 | 1252 |
| delta | actual | B | negligible | 0.3067 | 0.2522 | 0.3696 | 1252 |
| delta | actual | B | unresolved | 0.0264 | 0.0142 | 0.0426 | 1252 |
| delta | actual | C | dominance_positive | 0.1254 | 0.0777 | 0.1696 | 1252 |
| delta | actual | C | reversal | 0.5415 | 0.4841 | 0.5962 | 1252 |
| delta | actual | C | negligible | 0.3067 | 0.2522 | 0.3696 | 1252 |
| delta | actual | C | unresolved | 0.0264 | 0.0142 | 0.0426 | 1252 |
| delta | actual | B_pm | dominance_positive | 0.0807 | 0.0431 | 0.1179 | 1252 |
| delta | actual | B_pm | reversal | 0.4760 | 0.4246 | 0.5243 | 1252 |
| delta | actual | B_pm | negligible | 0.2907 | 0.2374 | 0.3425 | 1252 |
| delta | actual | B_pm | unresolved | 0.1526 | 0.1148 | 0.2003 | 1252 |
| delta | actual | C_pm | dominance_positive | 0.0807 | 0.0431 | 0.1179 | 1252 |
| delta | actual | C_pm | reversal | 0.4760 | 0.4246 | 0.5243 | 1252 |
| delta | actual | C_pm | negligible | 0.2907 | 0.2374 | 0.3425 | 1252 |
| delta | actual | C_pm | unresolved | 0.1526 | 0.1148 | 0.2003 | 1252 |
| delta | own | B | dominance_positive | 0.0639 | 0.0454 | 0.0835 | 1252 |
| delta | own | B | reversal | 0.6677 | 0.6237 | 0.7265 | 1252 |
| delta | own | B | negligible | 0.2157 | 0.1650 | 0.2630 | 1252 |
| delta | own | B | unresolved | 0.0527 | 0.0348 | 0.0751 | 1252 |
| delta | own | C | dominance_positive | 0.0639 | 0.0454 | 0.0835 | 1252 |
| delta | own | C | reversal | 0.6677 | 0.6237 | 0.7265 | 1252 |
| delta | own | C | negligible | 0.2157 | 0.1650 | 0.2630 | 1252 |
| delta | own | C | unresolved | 0.0527 | 0.0348 | 0.0751 | 1252 |
| delta | own | B_pm | dominance_positive | 0.0048 | 0.0000 | 0.0155 | 1252 |
| delta | own | B_pm | reversal | 0.5631 | 0.5118 | 0.6157 | 1252 |
| delta | own | B_pm | negligible | 0.1901 | 0.1358 | 0.2394 | 1252 |
| delta | own | B_pm | unresolved | 0.2420 | 0.1948 | 0.2946 | 1252 |
| delta | own | C_pm | dominance_positive | 0.0048 | 0.0000 | 0.0155 | 1252 |
| delta | own | C_pm | reversal | 0.5631 | 0.5118 | 0.6157 | 1252 |
| delta | own | C_pm | negligible | 0.1901 | 0.1358 | 0.2394 | 1252 |
| delta | own | C_pm | unresolved | 0.2420 | 0.1948 | 0.2946 | 1252 |

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
| new | actual | 1-3 | B | dominance_positive | 0.0625 | 0.0087 | 0.1348 | 128 |
| new | actual | 1-3 | B | reversal | 0.5625 | 0.2783 | 0.8033 | 128 |
| new | actual | 1-3 | B | negligible | 0.2656 | 0.0796 | 0.5000 | 128 |
| new | actual | 1-3 | B | unresolved | 0.1094 | 0.0246 | 0.2110 | 128 |
| new | actual | 1-3 | C | dominance_positive | 0.0625 | 0.0087 | 0.1348 | 128 |
| new | actual | 1-3 | C | reversal | 0.5625 | 0.2783 | 0.8033 | 128 |
| new | actual | 1-3 | C | negligible | 0.2656 | 0.0796 | 0.5000 | 128 |
| new | actual | 1-3 | C | unresolved | 0.1094 | 0.0246 | 0.2110 | 128 |
| new | actual | 1-3 | B_pm | dominance_positive | 0.0391 | 0.0000 | 0.1045 | 128 |
| new | actual | 1-3 | B_pm | reversal | 0.4609 | 0.2143 | 0.6723 | 128 |
| new | actual | 1-3 | B_pm | negligible | 0.2109 | 0.0469 | 0.4144 | 128 |
| new | actual | 1-3 | B_pm | unresolved | 0.2891 | 0.1440 | 0.4478 | 128 |
| new | actual | 1-3 | C_pm | dominance_positive | 0.0391 | 0.0000 | 0.1045 | 128 |
| new | actual | 1-3 | C_pm | reversal | 0.4609 | 0.2143 | 0.6723 | 128 |
| new | actual | 1-3 | C_pm | negligible | 0.2109 | 0.0469 | 0.4144 | 128 |
| new | actual | 1-3 | C_pm | unresolved | 0.2891 | 0.1440 | 0.4478 | 128 |
| new | actual | 4-10 | B | dominance_positive | 0.4271 | 0.2044 | 0.6677 | 295 |
| new | actual | 4-10 | B | reversal | 0.2102 | 0.1128 | 0.2815 | 295 |
| new | actual | 4-10 | B | negligible | 0.3119 | 0.1522 | 0.4696 | 295 |
| new | actual | 4-10 | B | unresolved | 0.0508 | 0.0000 | 0.1489 | 295 |
| new | actual | 4-10 | C | dominance_positive | 0.4271 | 0.2044 | 0.6677 | 295 |
| new | actual | 4-10 | C | reversal | 0.2102 | 0.1128 | 0.2815 | 295 |
| new | actual | 4-10 | C | negligible | 0.3119 | 0.1522 | 0.4696 | 295 |
| new | actual | 4-10 | C | unresolved | 0.0508 | 0.0000 | 0.1489 | 295 |
| new | actual | 4-10 | B_pm | dominance_positive | 0.4000 | 0.1488 | 0.6466 | 295 |
| new | actual | 4-10 | B_pm | reversal | 0.1763 | 0.0866 | 0.2516 | 295 |
| new | actual | 4-10 | B_pm | negligible | 0.2712 | 0.1414 | 0.3936 | 295 |
| new | actual | 4-10 | B_pm | unresolved | 0.1525 | 0.0265 | 0.3466 | 295 |
| new | actual | 4-10 | C_pm | dominance_positive | 0.4000 | 0.1488 | 0.6466 | 295 |
| new | actual | 4-10 | C_pm | reversal | 0.1763 | 0.0866 | 0.2516 | 295 |
| new | actual | 4-10 | C_pm | negligible | 0.2712 | 0.1414 | 0.3936 | 295 |
| new | actual | 4-10 | C_pm | unresolved | 0.1525 | 0.0265 | 0.3466 | 295 |
| new | actual | 11-16 | B | dominance_positive | 0.7284 | 0.5556 | 0.8734 | 243 |
| new | actual | 11-16 | B | reversal | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | actual | 11-16 | B | negligible | 0.2593 | 0.1213 | 0.4304 | 243 |
| new | actual | 11-16 | B | unresolved | 0.0082 | 0.0000 | 0.0357 | 243 |
| new | actual | 11-16 | C | dominance_positive | 0.7284 | 0.5556 | 0.8734 | 243 |
| new | actual | 11-16 | C | reversal | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | actual | 11-16 | C | negligible | 0.2593 | 0.1213 | 0.4304 | 243 |
| new | actual | 11-16 | C | unresolved | 0.0082 | 0.0000 | 0.0357 | 243 |
| new | actual | 11-16 | B_pm | dominance_positive | 0.7160 | 0.5478 | 0.8633 | 243 |
| new | actual | 11-16 | B_pm | reversal | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | actual | 11-16 | B_pm | negligible | 0.2428 | 0.1169 | 0.3957 | 243 |
| new | actual | 11-16 | B_pm | unresolved | 0.0370 | 0.0039 | 0.0860 | 243 |
| new | actual | 11-16 | C_pm | dominance_positive | 0.7160 | 0.5478 | 0.8633 | 243 |
| new | actual | 11-16 | C_pm | reversal | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | actual | 11-16 | C_pm | negligible | 0.2428 | 0.1169 | 0.3957 | 243 |
| new | actual | 11-16 | C_pm | unresolved | 0.0370 | 0.0039 | 0.0860 | 243 |
| new | actual | 17-30 | B | dominance_positive | 0.6297 | 0.4574 | 0.7909 | 586 |
| new | actual | 17-30 | B | reversal | 0.0478 | 0.0056 | 0.0935 | 586 |
| new | actual | 17-30 | B | negligible | 0.3140 | 0.1794 | 0.4717 | 586 |
| new | actual | 17-30 | B | unresolved | 0.0085 | 0.0000 | 0.0216 | 586 |
| new | actual | 17-30 | C | dominance_positive | 0.6297 | 0.4574 | 0.7909 | 586 |
| new | actual | 17-30 | C | reversal | 0.0461 | 0.0056 | 0.0903 | 586 |
| new | actual | 17-30 | C | negligible | 0.3140 | 0.1794 | 0.4717 | 586 |
| new | actual | 17-30 | C | unresolved | 0.0102 | 0.0000 | 0.0245 | 586 |
| new | actual | 17-30 | B_pm | dominance_positive | 0.6160 | 0.4474 | 0.7719 | 586 |
| new | actual | 17-30 | B_pm | reversal | 0.0375 | 0.0000 | 0.0841 | 586 |
| new | actual | 17-30 | B_pm | negligible | 0.2952 | 0.1735 | 0.4469 | 586 |
| new | actual | 17-30 | B_pm | unresolved | 0.0512 | 0.0123 | 0.0986 | 586 |
| new | actual | 17-30 | C_pm | dominance_positive | 0.6177 | 0.4474 | 0.7730 | 586 |
| new | actual | 17-30 | C_pm | reversal | 0.0375 | 0.0000 | 0.0841 | 586 |
| new | actual | 17-30 | C_pm | negligible | 0.2952 | 0.1735 | 0.4469 | 586 |
| new | actual | 17-30 | C_pm | unresolved | 0.0495 | 0.0098 | 0.0982 | 586 |
| new | own | 1-3 | B | dominance_positive | 0.0234 | 0.0000 | 0.0873 | 128 |
| new | own | 1-3 | B | reversal | 0.5703 | 0.2800 | 0.8235 | 128 |
| new | own | 1-3 | B | negligible | 0.3750 | 0.1207 | 0.6893 | 128 |
| new | own | 1-3 | B | unresolved | 0.0312 | 0.0000 | 0.0909 | 128 |
| new | own | 1-3 | C | dominance_positive | 0.0234 | 0.0000 | 0.0873 | 128 |
| new | own | 1-3 | C | reversal | 0.5703 | 0.2800 | 0.8235 | 128 |
| new | own | 1-3 | C | negligible | 0.3750 | 0.1207 | 0.6893 | 128 |
| new | own | 1-3 | C | unresolved | 0.0312 | 0.0000 | 0.0909 | 128 |
| new | own | 1-3 | B_pm | dominance_positive | 0.0234 | 0.0000 | 0.0896 | 128 |
| new | own | 1-3 | B_pm | reversal | 0.5156 | 0.2400 | 0.7838 | 128 |
| new | own | 1-3 | B_pm | negligible | 0.3047 | 0.0880 | 0.5872 | 128 |
| new | own | 1-3 | B_pm | unresolved | 0.1562 | 0.0476 | 0.2824 | 128 |
| new | own | 1-3 | C_pm | dominance_positive | 0.0234 | 0.0000 | 0.0896 | 128 |
| new | own | 1-3 | C_pm | reversal | 0.5156 | 0.2400 | 0.7838 | 128 |
| new | own | 1-3 | C_pm | negligible | 0.3047 | 0.0880 | 0.5872 | 128 |
| new | own | 1-3 | C_pm | unresolved | 0.1562 | 0.0476 | 0.2824 | 128 |
| new | own | 4-10 | B | dominance_positive | 0.4373 | 0.2076 | 0.6550 | 295 |
| new | own | 4-10 | B | reversal | 0.1966 | 0.0993 | 0.2775 | 295 |
| new | own | 4-10 | B | negligible | 0.3593 | 0.1849 | 0.5439 | 295 |
| new | own | 4-10 | B | unresolved | 0.0068 | 0.0000 | 0.0263 | 295 |
| new | own | 4-10 | C | dominance_positive | 0.4373 | 0.2076 | 0.6550 | 295 |
| new | own | 4-10 | C | reversal | 0.1966 | 0.0993 | 0.2775 | 295 |
| new | own | 4-10 | C | negligible | 0.3593 | 0.1849 | 0.5439 | 295 |
| new | own | 4-10 | C | unresolved | 0.0068 | 0.0000 | 0.0263 | 295 |
| new | own | 4-10 | B_pm | dominance_positive | 0.4475 | 0.2207 | 0.6553 | 295 |
| new | own | 4-10 | B_pm | reversal | 0.1797 | 0.0906 | 0.2509 | 295 |
| new | own | 4-10 | B_pm | negligible | 0.3390 | 0.1732 | 0.5271 | 295 |
| new | own | 4-10 | B_pm | unresolved | 0.0339 | 0.0041 | 0.0722 | 295 |
| new | own | 4-10 | C_pm | dominance_positive | 0.4475 | 0.2207 | 0.6553 | 295 |
| new | own | 4-10 | C_pm | reversal | 0.1797 | 0.0906 | 0.2509 | 295 |
| new | own | 4-10 | C_pm | negligible | 0.3390 | 0.1732 | 0.5271 | 295 |
| new | own | 4-10 | C_pm | unresolved | 0.0339 | 0.0041 | 0.0722 | 295 |
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

| rule | portfolio | jstar | count | count_argmin_C_hat | count_precision_matched | n_reversals | n_reversals_pm |
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
| new | actual | 1 | 0 | 0 | 0 | 163 | 134 |
| new | actual | 2 | 0 | 0 | 0 | 163 | 134 |
| new | actual | 3 | 2 | 2 | 1 | 163 | 134 |
| new | actual | 4 | 4 | 4 | 2 | 163 | 134 |
| new | actual | 5 | 49 | 48 | 39 | 163 | 134 |
| new | actual | 6 | 0 | 0 | 0 | 163 | 134 |
| new | actual | 7 | 1 | 2 | 2 | 163 | 134 |
| new | actual | 8 | 35 | 35 | 30 | 163 | 134 |
| new | actual | 9 | 30 | 30 | 26 | 163 | 134 |
| new | actual | 10 | 0 | 0 | 0 | 163 | 134 |
| new | actual | 11 | 0 | 0 | 0 | 163 | 134 |
| new | actual | 12 | 0 | 0 | 0 | 163 | 134 |
| new | actual | 13 | 0 | 0 | 0 | 163 | 134 |
| new | actual | 14 | 0 | 0 | 0 | 163 | 134 |
| new | actual | 15 | 2 | 2 | 2 | 163 | 134 |
| new | actual | 16 | 1 | 1 | 1 | 163 | 134 |
| new | actual | 17 | 2 | 2 | 2 | 163 | 134 |
| new | actual | 18 | 2 | 2 | 1 | 163 | 134 |
| new | actual | 19 | 6 | 6 | 6 | 163 | 134 |
| new | actual | 20 | 4 | 4 | 3 | 163 | 134 |
| new | actual | 21 | 2 | 2 | 1 | 163 | 134 |
| new | actual | 22 | 1 | 1 | 1 | 163 | 134 |
| new | actual | 23 | 4 | 4 | 4 | 163 | 134 |
| new | actual | 24 | 2 | 2 | 1 | 163 | 134 |
| new | actual | 25 | 2 | 2 | 3 | 163 | 134 |
| new | actual | 26 | 3 | 3 | 2 | 163 | 134 |
| new | actual | 27 | 3 | 3 | 2 | 163 | 134 |
| new | actual | 28 | 0 | 0 | 0 | 163 | 134 |
| new | actual | 29 | 3 | 3 | 2 | 163 | 134 |
| new | actual | 30 | 5 | 5 | 3 | 163 | 134 |
| new | own | 1 | 0 | 0 | 0 | 131 | 119 |
| new | own | 2 | 0 | 0 | 0 | 131 | 119 |
| new | own | 3 | 0 | 0 | 0 | 131 | 119 |
| new | own | 4 | 0 | 0 | 0 | 131 | 119 |
| new | own | 5 | 56 | 56 | 52 | 131 | 119 |
| new | own | 6 | 0 | 0 | 0 | 131 | 119 |
| new | own | 7 | 0 | 0 | 0 | 131 | 119 |
| new | own | 8 | 38 | 38 | 34 | 131 | 119 |
| new | own | 9 | 37 | 37 | 33 | 131 | 119 |
| new | own | 10 | 0 | 0 | 0 | 131 | 119 |
| new | own | 11 | 0 | 0 | 0 | 131 | 119 |
| new | own | 12 | 0 | 0 | 0 | 131 | 119 |
| new | own | 13 | 0 | 0 | 0 | 131 | 119 |
| new | own | 14 | 0 | 0 | 0 | 131 | 119 |
| new | own | 15 | 0 | 0 | 0 | 131 | 119 |
| new | own | 16 | 0 | 0 | 0 | 131 | 119 |
| new | own | 17 | 0 | 0 | 0 | 131 | 119 |
| new | own | 18 | 0 | 0 | 0 | 131 | 119 |
| new | own | 19 | 0 | 0 | 0 | 131 | 119 |
| new | own | 20 | 0 | 0 | 0 | 131 | 119 |
| new | own | 21 | 0 | 0 | 0 | 131 | 119 |
| new | own | 22 | 0 | 0 | 0 | 131 | 119 |
| new | own | 23 | 0 | 0 | 0 | 131 | 119 |
| new | own | 24 | 0 | 0 | 0 | 131 | 119 |
| new | own | 25 | 0 | 0 | 0 | 131 | 119 |
| new | own | 26 | 0 | 0 | 0 | 131 | 119 |
| new | own | 27 | 0 | 0 | 0 | 131 | 119 |
| new | own | 28 | 0 | 0 | 0 | 131 | 119 |
| new | own | 29 | 0 | 0 | 0 | 131 | 119 |
| new | own | 30 | 0 | 0 | 0 | 131 | 119 |

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
| new | actual | all | linear | 1252 | 0.0159 | 0.0000 | 0.0038 | 0.0291 | 0.0453 | 0.5152 | 0.3857 | 0.6348 | 0.0639 | 0.0203 | 0.1091 |
| new | actual | all | concave | 1252 | 0.0155 | 0.0000 | 0.0042 | 0.0290 | 0.0414 | 0.5264 | 0.4005 | 0.6304 | 0.0423 | 0.0144 | 0.0708 |
| new | actual | all | convex | 1252 | 0.0135 | 0.0000 | 0.0019 | 0.0217 | 0.0433 | 0.4824 | 0.3707 | 0.5977 | 0.0799 | 0.0332 | 0.1220 |
| new | actual | all | top3_stress | 1252 | 0.0048 | 0.0000 | 0.0000 | 0.0072 | 0.0213 | 0.3283 | 0.2439 | 0.4205 | 0.0990 | 0.0463 | 0.1400 |
| new | actual | 1-3 | linear | 128 | -0.0028 | -0.0032 | -0.0003 | 0.0003 | 0.0019 | 0.0859 | 0.0087 | 0.1690 | 0.2891 | 0.0556 | 0.5625 |
| new | actual | 1-3 | concave | 128 | -0.0017 | -0.0017 | -0.0002 | 0.0003 | 0.0043 | 0.1406 | 0.0000 | 0.3421 | 0.1797 | 0.0348 | 0.3643 |
| new | actual | 1-3 | convex | 128 | -0.0043 | -0.0061 | -0.0012 | -0.0001 | 0.0005 | 0.0703 | 0.0080 | 0.1458 | 0.3750 | 0.1428 | 0.6296 |
| new | actual | 1-3 | top3_stress | 128 | -0.0064 | -0.0101 | -0.0033 | -0.0002 | 0.0000 | 0.0156 | 0.0000 | 0.0630 | 0.5469 | 0.2500 | 0.8033 |
| new | actual | 4-10 | linear | 295 | 0.0046 | 0.0000 | 0.0007 | 0.0068 | 0.0168 | 0.3458 | 0.1490 | 0.5512 | 0.1119 | 0.0439 | 0.1941 |
| new | actual | 4-10 | concave | 295 | 0.0045 | 0.0000 | 0.0007 | 0.0055 | 0.0155 | 0.3797 | 0.2097 | 0.5577 | 0.0678 | 0.0197 | 0.1434 |
| new | actual | 4-10 | convex | 295 | 0.0044 | -0.0002 | 0.0003 | 0.0076 | 0.0192 | 0.3492 | 0.1579 | 0.5724 | 0.1627 | 0.0688 | 0.2395 |
| new | actual | 4-10 | top3_stress | 295 | 0.0020 | -0.0002 | 0.0000 | 0.0066 | 0.0136 | 0.3254 | 0.1347 | 0.5455 | 0.1729 | 0.0763 | 0.2529 |
| new | actual | 11-16 | linear | 243 | 0.0270 | 0.0007 | 0.0223 | 0.0402 | 0.0555 | 0.7160 | 0.5413 | 0.8614 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 11-16 | concave | 243 | 0.0207 | 0.0004 | 0.0165 | 0.0294 | 0.0427 | 0.6914 | 0.5045 | 0.8528 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 11-16 | convex | 243 | 0.0305 | 0.0005 | 0.0268 | 0.0441 | 0.0621 | 0.7078 | 0.5153 | 0.8609 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 11-16 | top3_stress | 243 | 0.0167 | 0.0004 | 0.0138 | 0.0241 | 0.0339 | 0.6872 | 0.5020 | 0.8399 | 0.0041 | 0.0000 | 0.0260 |
| new | actual | 17-30 | linear | 586 | 0.0211 | 0.0000 | 0.0153 | 0.0366 | 0.0505 | 0.6109 | 0.4007 | 0.7858 | 0.0171 | 0.0000 | 0.0549 |
| new | actual | 17-30 | concave | 586 | 0.0226 | 0.0000 | 0.0209 | 0.0362 | 0.0520 | 0.6160 | 0.4105 | 0.7848 | 0.0171 | 0.0000 | 0.0549 |
| new | actual | 17-30 | convex | 586 | 0.0149 | 0.0000 | 0.0049 | 0.0239 | 0.0431 | 0.5461 | 0.3757 | 0.6841 | 0.0068 | 0.0000 | 0.0285 |
| new | actual | 17-30 | top3_stress | 586 | 0.0037 | 0.0000 | 0.0000 | 0.0027 | 0.0136 | 0.2491 | 0.1667 | 0.3658 | 0.0034 | 0.0000 | 0.0140 |
| new | own | all | linear | 1252 | 0.0233 | 0.0003 | 0.0167 | 0.0397 | 0.0543 | 0.6901 | 0.6144 | 0.7827 | 0.0455 | 0.0164 | 0.0741 |
| new | own | all | concave | 1252 | 0.0207 | 0.0002 | 0.0207 | 0.0347 | 0.0444 | 0.6773 | 0.6043 | 0.7718 | 0.0096 | 0.0000 | 0.0247 |
| new | own | all | convex | 1252 | 0.0207 | 0.0001 | 0.0101 | 0.0344 | 0.0568 | 0.6326 | 0.5626 | 0.7110 | 0.0671 | 0.0291 | 0.0986 |
| new | own | all | top3_stress | 1252 | 0.0072 | 0.0000 | 0.0006 | 0.0123 | 0.0249 | 0.4273 | 0.3371 | 0.5239 | 0.0927 | 0.0427 | 0.1329 |
| new | own | 1-3 | linear | 128 | -0.0017 | -0.0029 | -0.0008 | -0.0001 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.2500 | 0.0598 | 0.4718 |
| new | own | 1-3 | concave | 128 | -0.0009 | -0.0015 | -0.0004 | -0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0625 | 0.0000 | 0.1558 |
| new | own | 1-3 | convex | 128 | -0.0032 | -0.0053 | -0.0015 | -0.0002 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.3594 | 0.1583 | 0.5798 |
| new | own | 1-3 | top3_stress | 128 | -0.0061 | -0.0099 | -0.0029 | -0.0003 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.5156 | 0.2385 | 0.7769 |
| new | own | 4-10 | linear | 295 | 0.0037 | -0.0000 | 0.0003 | 0.0059 | 0.0125 | 0.3390 | 0.1569 | 0.5415 | 0.0847 | 0.0312 | 0.1347 |
| new | own | 4-10 | concave | 295 | 0.0023 | -0.0000 | 0.0002 | 0.0036 | 0.0075 | 0.2847 | 0.0989 | 0.5074 | 0.0136 | 0.0000 | 0.0451 |
| new | own | 4-10 | convex | 295 | 0.0047 | -0.0001 | 0.0004 | 0.0084 | 0.0178 | 0.3729 | 0.1739 | 0.5840 | 0.1288 | 0.0547 | 0.1933 |
| new | own | 4-10 | top3_stress | 295 | 0.0025 | -0.0000 | 0.0001 | 0.0077 | 0.0140 | 0.3525 | 0.1661 | 0.5519 | 0.1695 | 0.0752 | 0.2492 |
| new | own | 11-16 | linear | 243 | 0.0345 | 0.0131 | 0.0335 | 0.0465 | 0.0651 | 0.9012 | 0.7611 | 0.9953 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | concave | 243 | 0.0226 | 0.0084 | 0.0217 | 0.0313 | 0.0440 | 0.8642 | 0.7222 | 0.9719 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | convex | 243 | 0.0422 | 0.0172 | 0.0397 | 0.0549 | 0.0802 | 0.9095 | 0.7714 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | top3_stress | 243 | 0.0227 | 0.0115 | 0.0195 | 0.0285 | 0.0456 | 0.8807 | 0.7540 | 0.9769 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | linear | 586 | 0.0341 | 0.0166 | 0.0313 | 0.0451 | 0.0625 | 0.9300 | 0.8617 | 0.9916 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | concave | 586 | 0.0339 | 0.0251 | 0.0334 | 0.0409 | 0.0523 | 0.9454 | 0.8912 | 0.9944 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | convex | 586 | 0.0252 | 0.0046 | 0.0161 | 0.0377 | 0.0600 | 0.7867 | 0.7155 | 0.8584 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | top3_stress | 586 | 0.0060 | 0.0000 | 0.0002 | 0.0072 | 0.0208 | 0.3703 | 0.2659 | 0.4901 | 0.0000 | 0.0000 | 0.0000 |
| delta | actual | all | linear | 1252 | -0.0016 | -0.0069 | 0.0000 | 0.0011 | 0.0110 | 0.2228 | 0.1709 | 0.2930 | 0.3315 | 0.2517 | 0.4024 |
| delta | actual | all | concave | 1252 | -0.0009 | -0.0042 | 0.0000 | 0.0013 | 0.0089 | 0.2045 | 0.1575 | 0.2680 | 0.2995 | 0.2104 | 0.3987 |
| delta | actual | all | convex | 1252 | -0.0025 | -0.0108 | 0.0000 | 0.0016 | 0.0141 | 0.2372 | 0.1862 | 0.3020 | 0.3650 | 0.3191 | 0.4077 |
| delta | actual | all | top3_stress | 1252 | -0.0020 | -0.0070 | 0.0000 | 0.0012 | 0.0121 | 0.2228 | 0.1627 | 0.2943 | 0.2931 | 0.2348 | 0.3483 |
| delta | actual | 1-3 | linear | 128 | -0.0057 | -0.0078 | -0.0026 | -0.0013 | -0.0004 | 0.0234 | 0.0000 | 0.0813 | 0.4688 | 0.1346 | 0.7652 |
| delta | actual | 1-3 | concave | 128 | -0.0032 | -0.0046 | -0.0015 | -0.0004 | 0.0015 | 0.0625 | 0.0000 | 0.2117 | 0.3516 | 0.0547 | 0.6729 |
| delta | actual | 1-3 | convex | 128 | -0.0094 | -0.0146 | -0.0051 | -0.0030 | -0.0014 | 0.0000 | 0.0000 | 0.0000 | 0.7969 | 0.6587 | 0.9179 |
| delta | actual | 1-3 | top3_stress | 128 | -0.0107 | -0.0165 | -0.0045 | -0.0005 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.5547 | 0.2556 | 0.8080 |
| delta | actual | 4-10 | linear | 295 | -0.0133 | -0.0205 | -0.0119 | -0.0055 | 0.0000 | 0.0237 | 0.0000 | 0.0709 | 0.8169 | 0.6751 | 0.9451 |
| delta | actual | 4-10 | concave | 295 | -0.0091 | -0.0134 | -0.0069 | -0.0026 | 0.0000 | 0.0542 | 0.0000 | 0.1394 | 0.7424 | 0.5633 | 0.9290 |
| delta | actual | 4-10 | convex | 295 | -0.0185 | -0.0270 | -0.0176 | -0.0104 | 0.0000 | 0.0169 | 0.0000 | 0.0498 | 0.8576 | 0.7516 | 0.9512 |
| delta | actual | 4-10 | top3_stress | 295 | -0.0162 | -0.0224 | -0.0158 | -0.0090 | 0.0000 | 0.0169 | 0.0000 | 0.0742 | 0.8475 | 0.7326 | 0.9496 |
| delta | actual | 11-16 | linear | 243 | -0.0010 | -0.0106 | 0.0000 | 0.0069 | 0.0188 | 0.3745 | 0.2358 | 0.5085 | 0.3909 | 0.2036 | 0.5447 |
| delta | actual | 11-16 | concave | 243 | -0.0018 | -0.0075 | 0.0000 | 0.0038 | 0.0124 | 0.2963 | 0.1745 | 0.4103 | 0.3663 | 0.1516 | 0.5353 |
| delta | actual | 11-16 | convex | 243 | 0.0012 | -0.0107 | 0.0000 | 0.0108 | 0.0224 | 0.4156 | 0.2906 | 0.5430 | 0.3580 | 0.1927 | 0.4921 |
| delta | actual | 11-16 | top3_stress | 243 | 0.0076 | 0.0000 | 0.0038 | 0.0133 | 0.0217 | 0.5350 | 0.3934 | 0.6667 | 0.1646 | 0.0724 | 0.2540 |
| delta | actual | 17-30 | linear | 586 | 0.0049 | 0.0000 | 0.0000 | 0.0042 | 0.0177 | 0.3038 | 0.2112 | 0.4223 | 0.0324 | 0.0035 | 0.0703 |
| delta | actual | 17-30 | concave | 586 | 0.0042 | 0.0000 | 0.0000 | 0.0030 | 0.0158 | 0.2730 | 0.1966 | 0.3597 | 0.0375 | 0.0036 | 0.0775 |
| delta | actual | 17-30 | convex | 586 | 0.0055 | 0.0000 | 0.0000 | 0.0059 | 0.0192 | 0.3259 | 0.2306 | 0.4466 | 0.0256 | 0.0033 | 0.0570 |
| delta | actual | 17-30 | top3_stress | 586 | 0.0031 | 0.0000 | 0.0000 | 0.0025 | 0.0111 | 0.2457 | 0.1648 | 0.3633 | 0.0102 | 0.0000 | 0.0267 |
| delta | own | all | linear | 1252 | -0.0007 | -0.0078 | 0.0000 | 0.0038 | 0.0140 | 0.2851 | 0.2378 | 0.3309 | 0.3738 | 0.3275 | 0.4172 |
| delta | own | all | concave | 1252 | -0.0004 | -0.0045 | 0.0000 | 0.0021 | 0.0081 | 0.2372 | 0.1994 | 0.2720 | 0.3235 | 0.2728 | 0.3781 |
| delta | own | all | convex | 1252 | -0.0010 | -0.0120 | 0.0000 | 0.0063 | 0.0203 | 0.3091 | 0.2643 | 0.3518 | 0.3970 | 0.3554 | 0.4339 |
| delta | own | all | top3_stress | 1252 | -0.0006 | -0.0084 | 0.0000 | 0.0054 | 0.0176 | 0.3091 | 0.2326 | 0.3802 | 0.3131 | 0.2483 | 0.3648 |
| delta | own | 1-3 | linear | 128 | -0.0050 | -0.0068 | -0.0033 | -0.0021 | -0.0015 | 0.0000 | 0.0000 | 0.0000 | 0.5469 | 0.2520 | 0.8136 |
| delta | own | 1-3 | concave | 128 | -0.0027 | -0.0036 | -0.0018 | -0.0011 | -0.0008 | 0.0000 | 0.0000 | 0.0000 | 0.2891 | 0.0846 | 0.5271 |
| delta | own | 1-3 | convex | 128 | -0.0088 | -0.0118 | -0.0058 | -0.0035 | -0.0025 | 0.0000 | 0.0000 | 0.0000 | 0.8438 | 0.6807 | 0.9655 |
| delta | own | 1-3 | top3_stress | 128 | -0.0105 | -0.0164 | -0.0042 | -0.0005 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.5703 | 0.2830 | 0.8148 |
| delta | own | 4-10 | linear | 295 | -0.0125 | -0.0175 | -0.0110 | -0.0074 | -0.0046 | 0.0000 | 0.0000 | 0.0000 | 0.9356 | 0.8393 | 0.9914 |
| delta | own | 4-10 | concave | 295 | -0.0072 | -0.0103 | -0.0061 | -0.0041 | -0.0025 | 0.0000 | 0.0000 | 0.0000 | 0.8814 | 0.7509 | 0.9786 |
| delta | own | 4-10 | convex | 295 | -0.0192 | -0.0263 | -0.0177 | -0.0120 | -0.0076 | 0.0000 | 0.0000 | 0.0000 | 0.9424 | 0.8423 | 0.9926 |
| delta | own | 4-10 | top3_stress | 295 | -0.0171 | -0.0224 | -0.0164 | -0.0102 | -0.0046 | 0.0169 | 0.0000 | 0.0606 | 0.9220 | 0.7932 | 0.9908 |
| delta | own | 11-16 | linear | 243 | 0.0015 | -0.0103 | 0.0024 | 0.0095 | 0.0187 | 0.5144 | 0.3622 | 0.7198 | 0.4115 | 0.2277 | 0.5377 |
| delta | own | 11-16 | concave | 243 | 0.0004 | -0.0070 | 0.0010 | 0.0052 | 0.0107 | 0.4033 | 0.2766 | 0.5333 | 0.3786 | 0.1681 | 0.5236 |
| delta | own | 11-16 | convex | 243 | 0.0045 | -0.0115 | 0.0052 | 0.0162 | 0.0290 | 0.5638 | 0.4292 | 0.7583 | 0.3951 | 0.2180 | 0.5238 |
| delta | own | 11-16 | top3_stress | 243 | 0.0113 | 0.0001 | 0.0099 | 0.0181 | 0.0283 | 0.6996 | 0.5524 | 0.8469 | 0.1811 | 0.0632 | 0.3108 |
| delta | own | 17-30 | linear | 586 | 0.0053 | 0.0000 | 0.0002 | 0.0082 | 0.0175 | 0.3959 | 0.3214 | 0.4797 | 0.0375 | 0.0032 | 0.0932 |
| delta | own | 17-30 | concave | 586 | 0.0032 | 0.0000 | 0.0001 | 0.0051 | 0.0101 | 0.3396 | 0.2649 | 0.4195 | 0.0273 | 0.0034 | 0.0612 |
| delta | own | 17-30 | convex | 586 | 0.0075 | 0.0000 | 0.0004 | 0.0107 | 0.0241 | 0.4266 | 0.3508 | 0.5089 | 0.0256 | 0.0020 | 0.0619 |
| delta | own | 17-30 | top3_stress | 586 | 0.0050 | 0.0000 | 0.0002 | 0.0066 | 0.0174 | 0.3618 | 0.2551 | 0.4828 | 0.0051 | 0.0000 | 0.0181 |

## H1

| n_team_games | share_neg_new | share_neg_old | diff_new_minus_old | diff_lo99 | diff_hi99 | n_new_reversals | crossing_share | crossing_lo99 | crossing_hi99 | supported |
|---|---|---|---|---|---|---|---|---|---|---|
| 163 | 0.3313 | 0.0000 | 0.3313 | 0.1260 | 0.5475 | 111 | 1.0000 | 1.0000 | 1.0000 | True |

## T5_attr_portfolio_effect

| rule | band | n | mean | q25 | median | q75 | q90 | share_nonzero |
|---|---|---|---|---|---|---|---|---|
| old | all | 1252 | -0.0065 | -0.0132 | 0.0000 | 0.0000 | 0.0020 | 0.4241 |
| old | 1-3 | 128 | -0.0004 | -0.0000 | 0.0000 | 0.0000 | 0.0016 | 0.0859 |
| old | 4-10 | 295 | 0.0017 | -0.0000 | 0.0000 | 0.0022 | 0.0135 | 0.3661 |
| old | 11-16 | 243 | -0.0050 | -0.0157 | 0.0000 | 0.0000 | 0.0015 | 0.4239 |
| old | 17-30 | 586 | -0.0126 | -0.0252 | -0.0036 | 0.0000 | 0.0000 | 0.5273 |
| new | all | 1252 | -0.0074 | -0.0096 | 0.0000 | 0.0000 | 0.0033 | 0.4297 |
| new | 1-3 | 128 | -0.0011 | -0.0000 | 0.0000 | 0.0004 | 0.0045 | 0.2266 |
| new | 4-10 | 295 | 0.0009 | -0.0000 | 0.0000 | 0.0016 | 0.0063 | 0.2949 |
| new | 11-16 | 243 | -0.0075 | -0.0081 | 0.0000 | 0.0000 | 0.0041 | 0.3909 |
| new | 17-30 | 586 | -0.0130 | -0.0220 | -0.0036 | 0.0000 | 0.0000 | 0.5580 |
| delta | all | 1252 | -0.0009 | -0.0002 | 0.0000 | 0.0001 | 0.0055 | 0.3043 |
| delta | 1-3 | 128 | -0.0007 | -0.0001 | 0.0000 | 0.0004 | 0.0029 | 0.1719 |
| delta | 4-10 | 295 | -0.0007 | -0.0005 | 0.0000 | 0.0001 | 0.0063 | 0.3492 |
| delta | 11-16 | 243 | -0.0025 | -0.0019 | 0.0000 | 0.0000 | 0.0074 | 0.3704 |
| delta | 17-30 | 586 | -0.0004 | -0.0000 | 0.0000 | 0.0000 | 0.0052 | 0.2833 |

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
| new | actual | all | - | 0.0000 | M | 1252 | 0.0063 | -0.0000 | 0.0000 | 0.0000 | 0.0160 |  |  |
| new | actual | all | linear | 0.0000 | tau | 1252 | 0.0159 | 0.0000 | 0.0038 | 0.0291 | 0.0453 | 0.0000 | 0.5000 |
| new | actual | all | linear | 0.5000 | tau | 1252 | 0.0143 | 0.0000 | 0.0035 | 0.0273 | 0.0438 | 0.0312 | 0.5000 |
| new | actual | all | linear | 0.8000 | tau | 1252 | 0.0134 | 0.0000 | 0.0031 | 0.0254 | 0.0420 | 0.0343 | 0.5000 |
| new | actual | all | concave | 0.0000 | tau | 1252 | 0.0155 | 0.0000 | 0.0042 | 0.0290 | 0.0414 | 0.0000 | 0.6599 |
| new | actual | all | concave | 0.5000 | tau | 1252 | 0.0134 | 0.0000 | 0.0029 | 0.0266 | 0.0387 | 0.0032 | 0.6599 |
| new | actual | all | concave | 0.8000 | tau | 1252 | 0.0122 | 0.0000 | 0.0024 | 0.0241 | 0.0367 | 0.0160 | 0.6599 |
| new | actual | all | convex | 0.0000 | tau | 1252 | 0.0135 | 0.0000 | 0.0019 | 0.0217 | 0.0433 | 0.0000 | 0.3391 |
| new | actual | all | convex | 0.5000 | tau | 1252 | 0.0125 | 0.0000 | 0.0018 | 0.0209 | 0.0410 | 0.0064 | 0.3391 |
| new | actual | all | convex | 0.8000 | tau | 1252 | 0.0118 | 0.0000 | 0.0017 | 0.0195 | 0.0400 | 0.0136 | 0.3391 |
| new | actual | all | top3_stress | 0.0000 | tau | 1252 | 0.0048 | 0.0000 | 0.0000 | 0.0072 | 0.0213 | 0.0000 | 0.1000 |
| new | actual | all | top3_stress | 0.5000 | tau | 1252 | 0.0045 | 0.0000 | 0.0000 | 0.0067 | 0.0203 | 0.0735 | 0.1000 |
| new | actual | all | top3_stress | 0.8000 | tau | 1252 | 0.0043 | 0.0000 | 0.0000 | 0.0063 | 0.0196 | 0.0743 | 0.1000 |
| new | actual | 1-3 | - | 0.0000 | M | 128 | -0.0003 | -0.0000 | 0.0000 | 0.0000 | 0.0035 |  |  |
| new | actual | 1-3 | linear | 0.0000 | tau | 128 | -0.0028 | -0.0032 | -0.0003 | 0.0003 | 0.0019 | 0.0000 | 0.5000 |
| new | actual | 1-3 | linear | 0.5000 | tau | 128 | -0.0028 | -0.0030 | -0.0005 | -0.0000 | 0.0007 | 0.1094 | 0.5000 |
| new | actual | 1-3 | linear | 0.8000 | tau | 128 | -0.0027 | -0.0032 | -0.0007 | -0.0000 | 0.0005 | 0.1172 | 0.5000 |
| new | actual | 1-3 | concave | 0.0000 | tau | 128 | -0.0017 | -0.0017 | -0.0002 | 0.0003 | 0.0043 | 0.0000 | 0.6599 |
| new | actual | 1-3 | concave | 0.5000 | tau | 128 | -0.0016 | -0.0016 | -0.0001 | 0.0003 | 0.0021 | 0.0156 | 0.6599 |
| new | actual | 1-3 | concave | 0.8000 | tau | 128 | -0.0016 | -0.0015 | -0.0002 | 0.0001 | 0.0010 | 0.0391 | 0.6599 |
| new | actual | 1-3 | convex | 0.0000 | tau | 128 | -0.0043 | -0.0061 | -0.0012 | -0.0001 | 0.0005 | 0.0000 | 0.3391 |
| new | actual | 1-3 | convex | 0.5000 | tau | 128 | -0.0042 | -0.0062 | -0.0014 | -0.0001 | 0.0002 | 0.0312 | 0.3391 |
| new | actual | 1-3 | convex | 0.8000 | tau | 128 | -0.0042 | -0.0061 | -0.0016 | -0.0001 | 0.0001 | 0.0547 | 0.3391 |
| new | actual | 1-3 | top3_stress | 0.0000 | tau | 128 | -0.0064 | -0.0101 | -0.0033 | -0.0002 | 0.0000 | 0.0000 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.5000 | tau | 128 | -0.0064 | -0.0104 | -0.0033 | -0.0002 | 0.0000 | 0.0781 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.8000 | tau | 128 | -0.0064 | -0.0102 | -0.0032 | -0.0002 | 0.0000 | 0.0781 | 0.1000 |
| new | actual | 4-10 | - | 0.0000 | M | 295 | 0.0041 | -0.0000 | 0.0000 | 0.0020 | 0.0157 |  |  |
| new | actual | 4-10 | linear | 0.0000 | tau | 295 | 0.0046 | 0.0000 | 0.0007 | 0.0068 | 0.0168 | 0.0000 | 0.5000 |
| new | actual | 4-10 | linear | 0.5000 | tau | 295 | 0.0036 | -0.0001 | 0.0003 | 0.0059 | 0.0147 | 0.0847 | 0.5000 |
| new | actual | 4-10 | linear | 0.8000 | tau | 295 | 0.0030 | -0.0001 | 0.0002 | 0.0055 | 0.0136 | 0.0915 | 0.5000 |
| new | actual | 4-10 | concave | 0.0000 | tau | 295 | 0.0045 | 0.0000 | 0.0007 | 0.0055 | 0.0155 | 0.0000 | 0.6599 |
| new | actual | 4-10 | concave | 0.5000 | tau | 295 | 0.0032 | 0.0000 | 0.0005 | 0.0043 | 0.0113 | 0.0068 | 0.6599 |
| new | actual | 4-10 | concave | 0.8000 | tau | 295 | 0.0024 | -0.0000 | 0.0003 | 0.0038 | 0.0104 | 0.0508 | 0.6599 |
| new | actual | 4-10 | convex | 0.0000 | tau | 295 | 0.0044 | -0.0002 | 0.0003 | 0.0076 | 0.0192 | 0.0000 | 0.3391 |
| new | actual | 4-10 | convex | 0.5000 | tau | 295 | 0.0037 | -0.0002 | 0.0002 | 0.0071 | 0.0178 | 0.0102 | 0.3391 |
| new | actual | 4-10 | convex | 0.8000 | tau | 295 | 0.0033 | -0.0002 | 0.0003 | 0.0069 | 0.0167 | 0.0169 | 0.3391 |
| new | actual | 4-10 | top3_stress | 0.0000 | tau | 295 | 0.0020 | -0.0002 | 0.0000 | 0.0066 | 0.0136 | 0.0000 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.5000 | tau | 295 | 0.0018 | -0.0002 | 0.0000 | 0.0064 | 0.0129 | 0.0339 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.8000 | tau | 295 | 0.0017 | -0.0002 | 0.0000 | 0.0062 | 0.0126 | 0.0373 | 0.1000 |
| new | actual | 11-16 | - | 0.0000 | M | 243 | 0.0081 | -0.0000 | 0.0000 | 0.0000 | 0.0311 |  |  |
| new | actual | 11-16 | linear | 0.0000 | tau | 243 | 0.0270 | 0.0007 | 0.0223 | 0.0402 | 0.0555 | 0.0000 | 0.5000 |
| new | actual | 11-16 | linear | 0.5000 | tau | 243 | 0.0250 | 0.0006 | 0.0190 | 0.0381 | 0.0480 | 0.0000 | 0.5000 |
| new | actual | 11-16 | linear | 0.8000 | tau | 243 | 0.0237 | 0.0004 | 0.0178 | 0.0366 | 0.0472 | 0.0000 | 0.5000 |
| new | actual | 11-16 | concave | 0.0000 | tau | 243 | 0.0207 | 0.0004 | 0.0165 | 0.0294 | 0.0427 | 0.0000 | 0.6599 |
| new | actual | 11-16 | concave | 0.5000 | tau | 243 | 0.0180 | 0.0004 | 0.0152 | 0.0275 | 0.0375 | 0.0000 | 0.6599 |
| new | actual | 11-16 | concave | 0.8000 | tau | 243 | 0.0164 | 0.0004 | 0.0121 | 0.0259 | 0.0322 | 0.0000 | 0.6599 |
| new | actual | 11-16 | convex | 0.0000 | tau | 243 | 0.0305 | 0.0005 | 0.0268 | 0.0441 | 0.0621 | 0.0000 | 0.3391 |
| new | actual | 11-16 | convex | 0.5000 | tau | 243 | 0.0292 | 0.0004 | 0.0244 | 0.0426 | 0.0577 | 0.0000 | 0.3391 |
| new | actual | 11-16 | convex | 0.8000 | tau | 243 | 0.0284 | 0.0004 | 0.0220 | 0.0423 | 0.0550 | 0.0041 | 0.3391 |
| new | actual | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0167 | 0.0004 | 0.0138 | 0.0241 | 0.0339 | 0.0000 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0163 | 0.0004 | 0.0126 | 0.0232 | 0.0322 | 0.0165 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0160 | 0.0004 | 0.0125 | 0.0230 | 0.0322 | 0.0165 | 0.1000 |
| new | actual | 17-30 | - | 0.0000 | M | 586 | 0.0081 | -0.0000 | 0.0000 | 0.0000 | 0.0265 |  |  |
| new | actual | 17-30 | linear | 0.0000 | tau | 586 | 0.0211 | 0.0000 | 0.0153 | 0.0366 | 0.0505 | 0.0000 | 0.5000 |
| new | actual | 17-30 | linear | 0.5000 | tau | 586 | 0.0190 | 0.0000 | 0.0146 | 0.0342 | 0.0466 | 0.0000 | 0.5000 |
| new | actual | 17-30 | linear | 0.8000 | tau | 586 | 0.0178 | 0.0000 | 0.0123 | 0.0322 | 0.0446 | 0.0017 | 0.5000 |
| new | actual | 17-30 | concave | 0.0000 | tau | 586 | 0.0226 | 0.0000 | 0.0209 | 0.0362 | 0.0520 | 0.0000 | 0.6599 |
| new | actual | 17-30 | concave | 0.5000 | tau | 586 | 0.0199 | 0.0000 | 0.0192 | 0.0355 | 0.0440 | 0.0000 | 0.6599 |
| new | actual | 17-30 | concave | 0.8000 | tau | 586 | 0.0183 | 0.0000 | 0.0155 | 0.0337 | 0.0414 | 0.0000 | 0.6599 |
| new | actual | 17-30 | convex | 0.0000 | tau | 586 | 0.0149 | 0.0000 | 0.0049 | 0.0239 | 0.0431 | 0.0000 | 0.3391 |
| new | actual | 17-30 | convex | 0.5000 | tau | 586 | 0.0136 | 0.0000 | 0.0046 | 0.0220 | 0.0388 | 0.0017 | 0.3391 |
| new | actual | 17-30 | convex | 0.8000 | tau | 586 | 0.0127 | 0.0000 | 0.0046 | 0.0211 | 0.0349 | 0.0068 | 0.3391 |
| new | actual | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0037 | 0.0000 | 0.0000 | 0.0027 | 0.0136 | 0.0000 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0033 | 0.0000 | 0.0000 | 0.0027 | 0.0117 | 0.1160 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0031 | 0.0000 | 0.0000 | 0.0025 | 0.0111 | 0.1160 | 0.1000 |
| new | own | all | - | 0.0000 | M | 1252 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | all | linear | 0.0000 | tau | 1252 | 0.0233 | 0.0003 | 0.0167 | 0.0397 | 0.0543 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.5000 | tau | 1252 | 0.0233 | 0.0003 | 0.0167 | 0.0397 | 0.0543 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.8000 | tau | 1252 | 0.0233 | 0.0003 | 0.0167 | 0.0397 | 0.0543 | 0.0000 | 0.5000 |
| new | own | all | concave | 0.0000 | tau | 1252 | 0.0207 | 0.0002 | 0.0207 | 0.0347 | 0.0444 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.5000 | tau | 1252 | 0.0207 | 0.0002 | 0.0207 | 0.0347 | 0.0444 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.8000 | tau | 1252 | 0.0207 | 0.0002 | 0.0207 | 0.0347 | 0.0444 | 0.0000 | 0.6599 |
| new | own | all | convex | 0.0000 | tau | 1252 | 0.0207 | 0.0001 | 0.0101 | 0.0344 | 0.0568 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.5000 | tau | 1252 | 0.0207 | 0.0001 | 0.0101 | 0.0344 | 0.0568 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.8000 | tau | 1252 | 0.0207 | 0.0001 | 0.0101 | 0.0344 | 0.0568 | 0.0000 | 0.3391 |
| new | own | all | top3_stress | 0.0000 | tau | 1252 | 0.0072 | 0.0000 | 0.0006 | 0.0123 | 0.0249 | 0.0000 | 0.1000 |
| new | own | all | top3_stress | 0.5000 | tau | 1252 | 0.0072 | 0.0000 | 0.0006 | 0.0123 | 0.0249 | 0.1134 | 0.1000 |
| new | own | all | top3_stress | 0.8000 | tau | 1252 | 0.0072 | 0.0000 | 0.0006 | 0.0123 | 0.0249 | 0.1142 | 0.1000 |
| new | own | 1-3 | - | 0.0000 | M | 128 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 1-3 | linear | 0.0000 | tau | 128 | -0.0017 | -0.0029 | -0.0008 | -0.0001 | -0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.5000 | tau | 128 | -0.0017 | -0.0029 | -0.0008 | -0.0001 | -0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.8000 | tau | 128 | -0.0017 | -0.0029 | -0.0008 | -0.0001 | -0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | concave | 0.0000 | tau | 128 | -0.0009 | -0.0015 | -0.0004 | -0.0001 | 0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.5000 | tau | 128 | -0.0009 | -0.0015 | -0.0004 | -0.0001 | 0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.8000 | tau | 128 | -0.0009 | -0.0015 | -0.0004 | -0.0001 | 0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | convex | 0.0000 | tau | 128 | -0.0032 | -0.0053 | -0.0015 | -0.0002 | -0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.5000 | tau | 128 | -0.0032 | -0.0053 | -0.0015 | -0.0002 | -0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.8000 | tau | 128 | -0.0032 | -0.0053 | -0.0015 | -0.0002 | -0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | top3_stress | 0.0000 | tau | 128 | -0.0061 | -0.0099 | -0.0029 | -0.0003 | 0.0000 | 0.0000 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.5000 | tau | 128 | -0.0061 | -0.0099 | -0.0029 | -0.0003 | 0.0000 | 0.1016 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.8000 | tau | 128 | -0.0061 | -0.0099 | -0.0029 | -0.0003 | 0.0000 | 0.1016 | 0.1000 |
| new | own | 4-10 | - | 0.0000 | M | 295 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 4-10 | linear | 0.0000 | tau | 295 | 0.0037 | -0.0000 | 0.0003 | 0.0059 | 0.0125 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.5000 | tau | 295 | 0.0037 | -0.0000 | 0.0003 | 0.0059 | 0.0125 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.8000 | tau | 295 | 0.0037 | -0.0000 | 0.0003 | 0.0059 | 0.0125 | 0.0000 | 0.5000 |
| new | own | 4-10 | concave | 0.0000 | tau | 295 | 0.0023 | -0.0000 | 0.0002 | 0.0036 | 0.0075 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.5000 | tau | 295 | 0.0023 | -0.0000 | 0.0002 | 0.0036 | 0.0075 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.8000 | tau | 295 | 0.0023 | -0.0000 | 0.0002 | 0.0036 | 0.0075 | 0.0000 | 0.6599 |
| new | own | 4-10 | convex | 0.0000 | tau | 295 | 0.0047 | -0.0001 | 0.0004 | 0.0084 | 0.0178 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.5000 | tau | 295 | 0.0047 | -0.0001 | 0.0004 | 0.0084 | 0.0178 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.8000 | tau | 295 | 0.0047 | -0.0001 | 0.0004 | 0.0084 | 0.0178 | 0.0000 | 0.3391 |
| new | own | 4-10 | top3_stress | 0.0000 | tau | 295 | 0.0025 | -0.0000 | 0.0001 | 0.0077 | 0.0140 | 0.0000 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.5000 | tau | 295 | 0.0025 | -0.0000 | 0.0001 | 0.0077 | 0.0140 | 0.0475 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.8000 | tau | 295 | 0.0025 | -0.0000 | 0.0001 | 0.0077 | 0.0140 | 0.0475 | 0.1000 |
| new | own | 11-16 | - | 0.0000 | M | 243 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 11-16 | linear | 0.0000 | tau | 243 | 0.0345 | 0.0131 | 0.0335 | 0.0465 | 0.0651 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.5000 | tau | 243 | 0.0345 | 0.0131 | 0.0335 | 0.0465 | 0.0651 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.8000 | tau | 243 | 0.0345 | 0.0131 | 0.0335 | 0.0465 | 0.0651 | 0.0000 | 0.5000 |
| new | own | 11-16 | concave | 0.0000 | tau | 243 | 0.0226 | 0.0084 | 0.0217 | 0.0313 | 0.0440 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.5000 | tau | 243 | 0.0226 | 0.0084 | 0.0217 | 0.0313 | 0.0440 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.8000 | tau | 243 | 0.0226 | 0.0084 | 0.0217 | 0.0313 | 0.0440 | 0.0000 | 0.6599 |
| new | own | 11-16 | convex | 0.0000 | tau | 243 | 0.0422 | 0.0172 | 0.0397 | 0.0549 | 0.0802 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.5000 | tau | 243 | 0.0422 | 0.0172 | 0.0397 | 0.0549 | 0.0802 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.8000 | tau | 243 | 0.0422 | 0.0172 | 0.0397 | 0.0549 | 0.0802 | 0.0000 | 0.3391 |
| new | own | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0227 | 0.0115 | 0.0195 | 0.0285 | 0.0456 | 0.0000 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0227 | 0.0115 | 0.0195 | 0.0285 | 0.0456 | 0.0123 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0227 | 0.0115 | 0.0195 | 0.0285 | 0.0456 | 0.0123 | 0.1000 |
| new | own | 17-30 | - | 0.0000 | M | 586 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 17-30 | linear | 0.0000 | tau | 586 | 0.0341 | 0.0166 | 0.0313 | 0.0451 | 0.0625 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.5000 | tau | 586 | 0.0341 | 0.0166 | 0.0313 | 0.0451 | 0.0625 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.8000 | tau | 586 | 0.0341 | 0.0166 | 0.0313 | 0.0451 | 0.0625 | 0.0000 | 0.5000 |
| new | own | 17-30 | concave | 0.0000 | tau | 586 | 0.0339 | 0.0251 | 0.0334 | 0.0409 | 0.0523 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.5000 | tau | 586 | 0.0339 | 0.0251 | 0.0334 | 0.0409 | 0.0523 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.8000 | tau | 586 | 0.0339 | 0.0251 | 0.0334 | 0.0409 | 0.0523 | 0.0000 | 0.6599 |
| new | own | 17-30 | convex | 0.0000 | tau | 586 | 0.0252 | 0.0046 | 0.0161 | 0.0377 | 0.0600 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.5000 | tau | 586 | 0.0252 | 0.0046 | 0.0161 | 0.0377 | 0.0600 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.8000 | tau | 586 | 0.0252 | 0.0046 | 0.0161 | 0.0377 | 0.0600 | 0.0000 | 0.3391 |
| new | own | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0060 | 0.0000 | 0.0002 | 0.0072 | 0.0208 | 0.0000 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0060 | 0.0000 | 0.0002 | 0.0072 | 0.0208 | 0.1911 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0060 | 0.0000 | 0.0002 | 0.0072 | 0.0208 | 0.1928 | 0.1000 |
| delta | actual | all | - | 0.0000 | M | 1252 | 0.0002 | -0.0000 | 0.0000 | 0.0000 | 0.0066 |  |  |
| delta | actual | all | linear | 0.0000 | tau | 1252 | -0.0016 | -0.0069 | 0.0000 | 0.0011 | 0.0110 | 0.0000 | 0.5000 |
| delta | actual | all | linear | 0.5000 | tau | 1252 | -0.0017 | -0.0072 | 0.0000 | 0.0011 | 0.0104 | 0.0072 | 0.5000 |
| delta | actual | all | linear | 0.8000 | tau | 1252 | -0.0017 | -0.0072 | 0.0000 | 0.0010 | 0.0094 | 0.0120 | 0.5000 |
| delta | actual | all | concave | 0.0000 | tau | 1252 | -0.0009 | -0.0042 | 0.0000 | 0.0013 | 0.0089 | 0.0000 | 0.6599 |
| delta | actual | all | concave | 0.5000 | tau | 1252 | -0.0009 | -0.0041 | 0.0000 | 0.0008 | 0.0072 | 0.0232 | 0.6599 |
| delta | actual | all | concave | 0.8000 | tau | 1252 | -0.0009 | -0.0041 | 0.0000 | 0.0006 | 0.0063 | 0.0399 | 0.6599 |
| delta | actual | all | convex | 0.0000 | tau | 1252 | -0.0025 | -0.0108 | 0.0000 | 0.0016 | 0.0141 | 0.0000 | 0.3391 |
| delta | actual | all | convex | 0.5000 | tau | 1252 | -0.0025 | -0.0110 | 0.0000 | 0.0014 | 0.0131 | 0.0056 | 0.3391 |
| delta | actual | all | convex | 0.8000 | tau | 1252 | -0.0026 | -0.0108 | 0.0000 | 0.0013 | 0.0126 | 0.0088 | 0.3391 |
| delta | actual | all | top3_stress | 0.0000 | tau | 1252 | -0.0020 | -0.0070 | 0.0000 | 0.0012 | 0.0121 | 0.0000 | 0.1000 |
| delta | actual | all | top3_stress | 0.5000 | tau | 1252 | -0.0020 | -0.0067 | 0.0000 | 0.0013 | 0.0119 | 0.0383 | 0.1000 |
| delta | actual | all | top3_stress | 0.8000 | tau | 1252 | -0.0020 | -0.0067 | 0.0000 | 0.0014 | 0.0119 | 0.0391 | 0.1000 |
| delta | actual | 1-3 | - | 0.0000 | M | 128 | -0.0002 | -0.0000 | 0.0000 | 0.0000 | 0.0035 |  |  |
| delta | actual | 1-3 | linear | 0.0000 | tau | 128 | -0.0057 | -0.0078 | -0.0026 | -0.0013 | -0.0004 | 0.0000 | 0.5000 |
| delta | actual | 1-3 | linear | 0.5000 | tau | 128 | -0.0057 | -0.0083 | -0.0028 | -0.0017 | -0.0008 | 0.0391 | 0.5000 |
| delta | actual | 1-3 | linear | 0.8000 | tau | 128 | -0.0057 | -0.0083 | -0.0030 | -0.0018 | -0.0008 | 0.0391 | 0.5000 |
| delta | actual | 1-3 | concave | 0.0000 | tau | 128 | -0.0032 | -0.0046 | -0.0015 | -0.0004 | 0.0015 | 0.0000 | 0.6599 |
| delta | actual | 1-3 | concave | 0.5000 | tau | 128 | -0.0032 | -0.0044 | -0.0014 | -0.0005 | 0.0000 | 0.0781 | 0.6599 |
| delta | actual | 1-3 | concave | 0.8000 | tau | 128 | -0.0031 | -0.0043 | -0.0015 | -0.0008 | -0.0004 | 0.1484 | 0.6599 |
| delta | actual | 1-3 | convex | 0.0000 | tau | 128 | -0.0094 | -0.0146 | -0.0051 | -0.0030 | -0.0014 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | convex | 0.5000 | tau | 128 | -0.0094 | -0.0133 | -0.0051 | -0.0031 | -0.0014 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | convex | 0.8000 | tau | 128 | -0.0093 | -0.0129 | -0.0053 | -0.0032 | -0.0014 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | top3_stress | 0.0000 | tau | 128 | -0.0107 | -0.0165 | -0.0045 | -0.0005 | -0.0000 | 0.0000 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.5000 | tau | 128 | -0.0107 | -0.0165 | -0.0045 | -0.0005 | -0.0000 | 0.0078 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.8000 | tau | 128 | -0.0107 | -0.0166 | -0.0046 | -0.0005 | -0.0000 | 0.0078 | 0.1000 |
| delta | actual | 4-10 | - | 0.0000 | M | 295 | -0.0035 | -0.0006 | -0.0000 | 0.0000 | 0.0036 |  |  |
| delta | actual | 4-10 | linear | 0.0000 | tau | 295 | -0.0133 | -0.0205 | -0.0119 | -0.0055 | 0.0000 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | linear | 0.5000 | tau | 295 | -0.0124 | -0.0188 | -0.0114 | -0.0061 | 0.0000 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | linear | 0.8000 | tau | 295 | -0.0119 | -0.0175 | -0.0109 | -0.0063 | 0.0000 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | concave | 0.0000 | tau | 295 | -0.0091 | -0.0134 | -0.0069 | -0.0026 | 0.0000 | 0.0000 | 0.6599 |
| delta | actual | 4-10 | concave | 0.5000 | tau | 295 | -0.0080 | -0.0126 | -0.0067 | -0.0027 | 0.0000 | 0.0441 | 0.6599 |
| delta | actual | 4-10 | concave | 0.8000 | tau | 295 | -0.0073 | -0.0115 | -0.0065 | -0.0032 | 0.0000 | 0.0610 | 0.6599 |
| delta | actual | 4-10 | convex | 0.0000 | tau | 295 | -0.0185 | -0.0270 | -0.0176 | -0.0104 | 0.0000 | 0.0000 | 0.3391 |
| delta | actual | 4-10 | convex | 0.5000 | tau | 295 | -0.0179 | -0.0266 | -0.0173 | -0.0102 | 0.0000 | 0.0102 | 0.3391 |
| delta | actual | 4-10 | convex | 0.8000 | tau | 295 | -0.0175 | -0.0257 | -0.0157 | -0.0101 | -0.0000 | 0.0169 | 0.3391 |
| delta | actual | 4-10 | top3_stress | 0.0000 | tau | 295 | -0.0162 | -0.0224 | -0.0158 | -0.0090 | 0.0000 | 0.0000 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.5000 | tau | 295 | -0.0161 | -0.0222 | -0.0154 | -0.0087 | 0.0000 | 0.0034 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.8000 | tau | 295 | -0.0160 | -0.0222 | -0.0150 | -0.0085 | 0.0000 | 0.0068 | 0.1000 |
| delta | actual | 11-16 | - | 0.0000 | M | 243 | -0.0021 | -0.0000 | 0.0000 | 0.0000 | 0.0012 |  |  |
| delta | actual | 11-16 | linear | 0.0000 | tau | 243 | -0.0010 | -0.0106 | 0.0000 | 0.0069 | 0.0188 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | linear | 0.5000 | tau | 243 | -0.0005 | -0.0098 | 0.0000 | 0.0065 | 0.0168 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | linear | 0.8000 | tau | 243 | -0.0001 | -0.0088 | 0.0000 | 0.0061 | 0.0142 | 0.0123 | 0.5000 |
| delta | actual | 11-16 | concave | 0.0000 | tau | 243 | -0.0018 | -0.0075 | 0.0000 | 0.0038 | 0.0124 | 0.0000 | 0.6599 |
| delta | actual | 11-16 | concave | 0.5000 | tau | 243 | -0.0011 | -0.0071 | 0.0000 | 0.0038 | 0.0110 | 0.0041 | 0.6599 |
| delta | actual | 11-16 | concave | 0.8000 | tau | 243 | -0.0007 | -0.0065 | 0.0000 | 0.0035 | 0.0104 | 0.0082 | 0.6599 |
| delta | actual | 11-16 | convex | 0.0000 | tau | 243 | 0.0012 | -0.0107 | 0.0000 | 0.0108 | 0.0224 | 0.0000 | 0.3391 |
| delta | actual | 11-16 | convex | 0.5000 | tau | 243 | 0.0016 | -0.0096 | 0.0000 | 0.0106 | 0.0199 | 0.0123 | 0.3391 |
| delta | actual | 11-16 | convex | 0.8000 | tau | 243 | 0.0018 | -0.0091 | 0.0000 | 0.0104 | 0.0199 | 0.0165 | 0.3391 |
| delta | actual | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0076 | 0.0000 | 0.0038 | 0.0133 | 0.0217 | 0.0000 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0077 | 0.0000 | 0.0041 | 0.0133 | 0.0224 | 0.0329 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0078 | 0.0000 | 0.0044 | 0.0136 | 0.0216 | 0.0329 | 0.1000 |
| delta | actual | 17-30 | - | 0.0000 | M | 586 | 0.0031 | 0.0000 | 0.0000 | 0.0000 | 0.0118 |  |  |
| delta | actual | 17-30 | linear | 0.0000 | tau | 586 | 0.0049 | 0.0000 | 0.0000 | 0.0042 | 0.0177 | 0.0000 | 0.5000 |
| delta | actual | 17-30 | linear | 0.5000 | tau | 586 | 0.0041 | 0.0000 | 0.0000 | 0.0041 | 0.0143 | 0.0068 | 0.5000 |
| delta | actual | 17-30 | linear | 0.8000 | tau | 586 | 0.0037 | 0.0000 | 0.0000 | 0.0040 | 0.0131 | 0.0119 | 0.5000 |
| delta | actual | 17-30 | concave | 0.0000 | tau | 586 | 0.0042 | 0.0000 | 0.0000 | 0.0030 | 0.0158 | 0.0000 | 0.6599 |
| delta | actual | 17-30 | concave | 0.5000 | tau | 586 | 0.0032 | 0.0000 | 0.0000 | 0.0027 | 0.0113 | 0.0085 | 0.6599 |
| delta | actual | 17-30 | concave | 0.8000 | tau | 586 | 0.0026 | 0.0000 | 0.0000 | 0.0026 | 0.0091 | 0.0188 | 0.6599 |
| delta | actual | 17-30 | convex | 0.0000 | tau | 586 | 0.0055 | 0.0000 | 0.0000 | 0.0059 | 0.0192 | 0.0000 | 0.3391 |
| delta | actual | 17-30 | convex | 0.5000 | tau | 586 | 0.0050 | 0.0000 | 0.0000 | 0.0055 | 0.0175 | 0.0017 | 0.3391 |
| delta | actual | 17-30 | convex | 0.8000 | tau | 586 | 0.0047 | 0.0000 | 0.0000 | 0.0055 | 0.0161 | 0.0034 | 0.3391 |
| delta | actual | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0031 | 0.0000 | 0.0000 | 0.0025 | 0.0111 | 0.0000 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0029 | 0.0000 | 0.0000 | 0.0025 | 0.0107 | 0.0648 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0029 | 0.0000 | 0.0000 | 0.0026 | 0.0106 | 0.0648 | 0.1000 |
| delta | own | all | - | 0.0000 | M | 1252 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | all | linear | 0.0000 | tau | 1252 | -0.0007 | -0.0078 | 0.0000 | 0.0038 | 0.0140 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.5000 | tau | 1252 | -0.0007 | -0.0078 | 0.0000 | 0.0038 | 0.0140 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.8000 | tau | 1252 | -0.0007 | -0.0078 | 0.0000 | 0.0038 | 0.0140 | 0.0000 | 0.5000 |
| delta | own | all | concave | 0.0000 | tau | 1252 | -0.0004 | -0.0045 | 0.0000 | 0.0021 | 0.0081 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.5000 | tau | 1252 | -0.0004 | -0.0045 | 0.0000 | 0.0021 | 0.0081 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.8000 | tau | 1252 | -0.0004 | -0.0045 | 0.0000 | 0.0021 | 0.0081 | 0.0000 | 0.6599 |
| delta | own | all | convex | 0.0000 | tau | 1252 | -0.0010 | -0.0120 | 0.0000 | 0.0063 | 0.0203 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.5000 | tau | 1252 | -0.0010 | -0.0120 | 0.0000 | 0.0063 | 0.0203 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.8000 | tau | 1252 | -0.0010 | -0.0120 | 0.0000 | 0.0063 | 0.0203 | 0.0000 | 0.3391 |
| delta | own | all | top3_stress | 0.0000 | tau | 1252 | -0.0006 | -0.0084 | 0.0000 | 0.0054 | 0.0176 | 0.0000 | 0.1000 |
| delta | own | all | top3_stress | 0.5000 | tau | 1252 | -0.0006 | -0.0084 | 0.0000 | 0.0054 | 0.0176 | 0.0160 | 0.1000 |
| delta | own | all | top3_stress | 0.8000 | tau | 1252 | -0.0006 | -0.0084 | 0.0000 | 0.0054 | 0.0176 | 0.0160 | 0.1000 |
| delta | own | 1-3 | - | 0.0000 | M | 128 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 1-3 | linear | 0.0000 | tau | 128 | -0.0050 | -0.0068 | -0.0033 | -0.0021 | -0.0015 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.5000 | tau | 128 | -0.0050 | -0.0068 | -0.0033 | -0.0021 | -0.0015 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.8000 | tau | 128 | -0.0050 | -0.0068 | -0.0033 | -0.0021 | -0.0015 | 0.0000 | 0.5000 |
| delta | own | 1-3 | concave | 0.0000 | tau | 128 | -0.0027 | -0.0036 | -0.0018 | -0.0011 | -0.0008 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.5000 | tau | 128 | -0.0027 | -0.0036 | -0.0018 | -0.0011 | -0.0008 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.8000 | tau | 128 | -0.0027 | -0.0036 | -0.0018 | -0.0011 | -0.0008 | 0.0000 | 0.6599 |
| delta | own | 1-3 | convex | 0.0000 | tau | 128 | -0.0088 | -0.0118 | -0.0058 | -0.0035 | -0.0025 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.5000 | tau | 128 | -0.0088 | -0.0118 | -0.0058 | -0.0035 | -0.0025 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.8000 | tau | 128 | -0.0088 | -0.0118 | -0.0058 | -0.0035 | -0.0025 | 0.0000 | 0.3391 |
| delta | own | 1-3 | top3_stress | 0.0000 | tau | 128 | -0.0105 | -0.0164 | -0.0042 | -0.0005 | -0.0000 | 0.0000 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.5000 | tau | 128 | -0.0105 | -0.0164 | -0.0042 | -0.0005 | -0.0000 | 0.0000 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.8000 | tau | 128 | -0.0105 | -0.0164 | -0.0042 | -0.0005 | -0.0000 | 0.0000 | 0.1000 |
| delta | own | 4-10 | - | 0.0000 | M | 295 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 4-10 | linear | 0.0000 | tau | 295 | -0.0125 | -0.0175 | -0.0110 | -0.0074 | -0.0046 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.5000 | tau | 295 | -0.0125 | -0.0175 | -0.0110 | -0.0074 | -0.0046 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.8000 | tau | 295 | -0.0125 | -0.0175 | -0.0110 | -0.0074 | -0.0046 | 0.0000 | 0.5000 |
| delta | own | 4-10 | concave | 0.0000 | tau | 295 | -0.0072 | -0.0103 | -0.0061 | -0.0041 | -0.0025 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.5000 | tau | 295 | -0.0072 | -0.0103 | -0.0061 | -0.0041 | -0.0025 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.8000 | tau | 295 | -0.0072 | -0.0103 | -0.0061 | -0.0041 | -0.0025 | 0.0000 | 0.6599 |
| delta | own | 4-10 | convex | 0.0000 | tau | 295 | -0.0192 | -0.0263 | -0.0177 | -0.0120 | -0.0076 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.5000 | tau | 295 | -0.0192 | -0.0263 | -0.0177 | -0.0120 | -0.0076 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.8000 | tau | 295 | -0.0192 | -0.0263 | -0.0177 | -0.0120 | -0.0076 | 0.0000 | 0.3391 |
| delta | own | 4-10 | top3_stress | 0.0000 | tau | 295 | -0.0171 | -0.0224 | -0.0164 | -0.0102 | -0.0046 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.5000 | tau | 295 | -0.0171 | -0.0224 | -0.0164 | -0.0102 | -0.0046 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.8000 | tau | 295 | -0.0171 | -0.0224 | -0.0164 | -0.0102 | -0.0046 | 0.0000 | 0.1000 |
| delta | own | 11-16 | - | 0.0000 | M | 243 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 11-16 | linear | 0.0000 | tau | 243 | 0.0015 | -0.0103 | 0.0024 | 0.0095 | 0.0187 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.5000 | tau | 243 | 0.0015 | -0.0103 | 0.0024 | 0.0095 | 0.0187 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.8000 | tau | 243 | 0.0015 | -0.0103 | 0.0024 | 0.0095 | 0.0187 | 0.0000 | 0.5000 |
| delta | own | 11-16 | concave | 0.0000 | tau | 243 | 0.0004 | -0.0070 | 0.0010 | 0.0052 | 0.0107 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.5000 | tau | 243 | 0.0004 | -0.0070 | 0.0010 | 0.0052 | 0.0107 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.8000 | tau | 243 | 0.0004 | -0.0070 | 0.0010 | 0.0052 | 0.0107 | 0.0000 | 0.6599 |
| delta | own | 11-16 | convex | 0.0000 | tau | 243 | 0.0045 | -0.0115 | 0.0052 | 0.0162 | 0.0290 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.5000 | tau | 243 | 0.0045 | -0.0115 | 0.0052 | 0.0162 | 0.0290 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.8000 | tau | 243 | 0.0045 | -0.0115 | 0.0052 | 0.0162 | 0.0290 | 0.0000 | 0.3391 |
| delta | own | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0113 | 0.0001 | 0.0099 | 0.0181 | 0.0283 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0113 | 0.0001 | 0.0099 | 0.0181 | 0.0283 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0113 | 0.0001 | 0.0099 | 0.0181 | 0.0283 | 0.0000 | 0.1000 |
| delta | own | 17-30 | - | 0.0000 | M | 586 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 17-30 | linear | 0.0000 | tau | 586 | 0.0053 | 0.0000 | 0.0002 | 0.0082 | 0.0175 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.5000 | tau | 586 | 0.0053 | 0.0000 | 0.0002 | 0.0082 | 0.0175 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.8000 | tau | 586 | 0.0053 | 0.0000 | 0.0002 | 0.0082 | 0.0175 | 0.0000 | 0.5000 |
| delta | own | 17-30 | concave | 0.0000 | tau | 586 | 0.0032 | 0.0000 | 0.0001 | 0.0051 | 0.0101 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.5000 | tau | 586 | 0.0032 | 0.0000 | 0.0001 | 0.0051 | 0.0101 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.8000 | tau | 586 | 0.0032 | 0.0000 | 0.0001 | 0.0051 | 0.0101 | 0.0000 | 0.6599 |
| delta | own | 17-30 | convex | 0.0000 | tau | 586 | 0.0075 | 0.0000 | 0.0004 | 0.0107 | 0.0241 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.5000 | tau | 586 | 0.0075 | 0.0000 | 0.0004 | 0.0107 | 0.0241 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.8000 | tau | 586 | 0.0075 | 0.0000 | 0.0004 | 0.0107 | 0.0241 | 0.0000 | 0.3391 |
| delta | own | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0050 | 0.0000 | 0.0002 | 0.0066 | 0.0174 | 0.0000 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0050 | 0.0000 | 0.0002 | 0.0066 | 0.0174 | 0.0341 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0050 | 0.0000 | 0.0002 | 0.0066 | 0.0174 | 0.0341 | 0.1000 |

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
| new | actual | <0.01 | B | dominance_positive | 0.1138 | 0.0515 | 0.1771 | 369 |
| new | actual | <0.01 | B | reversal | 0.3577 | 0.2131 | 0.4986 | 369 |
| new | actual | <0.01 | B | negligible | 0.4444 | 0.3067 | 0.5965 | 369 |
| new | actual | <0.01 | B | unresolved | 0.0840 | 0.0314 | 0.1585 | 369 |
| new | actual | 0.01-0.05 | B | dominance_positive | 0.6076 | 0.4091 | 0.8696 | 79 |
| new | actual | 0.01-0.05 | B | reversal | 0.0380 | 0.0000 | 0.1447 | 79 |
| new | actual | 0.01-0.05 | B | negligible | 0.3544 | 0.0897 | 0.5618 | 79 |
| new | actual | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | actual | >=0.05 | B | dominance_positive | 0.7338 | 0.6294 | 0.8109 | 804 |
| new | actual | >=0.05 | B | reversal | 0.0348 | 0.0095 | 0.0631 | 804 |
| new | actual | >=0.05 | B | negligible | 0.2251 | 0.1516 | 0.3173 | 804 |
| new | actual | >=0.05 | B | unresolved | 0.0062 | 0.0000 | 0.0151 | 804 |
| new | own | <0.01 | B | dominance_positive | 0.1436 | 0.0665 | 0.2330 | 369 |
| new | own | <0.01 | B | reversal | 0.3550 | 0.1959 | 0.5119 | 369 |
| new | own | <0.01 | B | negligible | 0.4851 | 0.3556 | 0.6355 | 369 |
| new | own | <0.01 | B | unresolved | 0.0163 | 0.0000 | 0.0446 | 369 |
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
| new | holds_conditional_other | True | 529 | 0.1815 | 0.0892 | 0.2514 |
| new | holds_conditional_other | False | 723 | 0.0927 | 0.0398 | 0.1545 |
| new | holds_opponent_pick | True | 43 | 0.4884 | 0.2449 | 0.7778 |
| new | holds_opponent_pick | False | 1209 | 0.1175 | 0.0562 | 0.1570 |
| new | holds_pooled_pick | True | 379 | 0.1398 | 0.0355 | 0.2422 |
| new | holds_pooled_pick | False | 873 | 0.1260 | 0.0639 | 0.1912 |
| new | self_restricted | True | 103 | 0.1845 | 0.0090 | 0.3805 |
| new | self_restricted | False | 1149 | 0.1253 | 0.0580 | 0.1751 |
| new | opp_restricted | True | 103 | 0.0874 | 0.0000 | 0.1979 |
| new | opp_restricted | False | 1149 | 0.1340 | 0.0681 | 0.1771 |
| new | holds_conditional_other_state | True | 500 | 0.1720 | 0.0870 | 0.2332 |
| new | holds_conditional_other_state | False | 752 | 0.1024 | 0.0433 | 0.1628 |
| new | holds_opponent_pick_state | True | 40 | 0.5000 | 0.2542 | 0.7667 |
| new | holds_opponent_pick_state | False | 1212 | 0.1180 | 0.0571 | 0.1576 |

## T5_6_transitions

| portfolio | old | new | count |
|---|---|---|---|
| actual | dominance_positive | dominance_positive | 643 |
| actual | dominance_positive | negligible | 115 |
| actual | dominance_positive | reversal | 117 |
| actual | dominance_positive | unresolved | 23 |
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
| actual | unresolved | reversal | 5 |
| actual | unresolved | unresolved | 10 |
| own | dominance_positive | dominance_positive | 924 |
| own | dominance_positive | negligible | 154 |
| own | dominance_positive | reversal | 131 |
| own | dominance_positive | unresolved | 6 |
| own | negligible | negligible | 37 |

## T5_headline_reversal_diff

| contrast | portfolio | verdict | share_a | share_b | diff | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| new_minus_old | actual | verdict_B | 0.1302 | 0.0383 | 0.0919 | 0.0400 | 0.1316 | 1252 |
| new_minus_old | actual | verdict_B_pm | 0.1070 | 0.0272 | 0.0799 | 0.0376 | 0.1094 | 1252 |
| new_minus_old | own | verdict_B | 0.1046 | 0.0000 | 0.1046 | 0.0506 | 0.1450 | 1252 |
| new_minus_old | own | verdict_B_pm | 0.0950 | 0.0000 | 0.0950 | 0.0461 | 0.1344 | 1252 |
| actual_minus_own | old | verdict_B | 0.0383 | 0.0000 | 0.0383 | 0.0165 | 0.0632 | 1252 |
| actual_minus_own | new | verdict_B | 0.1302 | 0.1046 | 0.0256 | 0.0062 | 0.0477 | 1252 |

## T5_4_typology

| rule | curve | type | share | lo99 | hi99 | n | tp_dominated_share |
|---|---|---|---|---|---|---|---|
| old | linear | both_lose | 0.4649 | 0.2982 | 0.6457 | 291 | 0.2818 |
| old | linear | both_win | 0.0016 | 0.0000 | 0.0097 | 1 | 0.0000 |
| old | linear | normal | 0.3914 | 0.2968 | 0.4663 | 245 | 0.7510 |
| old | linear | opposed | 0.0176 | 0.0016 | 0.0408 | 11 | 0.9091 |
| old | linear | one_sided_win | 0.0144 | 0.0000 | 0.0344 | 9 | 0.7778 |
| old | linear | no_own_stake | 0.1102 | 0.0347 | 0.2083 | 69 | 1.0000 |
| old | concave | both_lose | 0.4185 | 0.2574 | 0.6014 | 262 | 0.3282 |
| old | concave | both_win | 0.0016 | 0.0000 | 0.0097 | 1 | 0.0000 |
| old | concave | normal | 0.4121 | 0.3176 | 0.4983 | 258 | 0.7237 |
| old | concave | opposed | 0.0192 | 0.0048 | 0.0386 | 12 | 0.7500 |
| old | concave | one_sided_win | 0.0144 | 0.0000 | 0.0365 | 9 | 0.7778 |
| old | concave | no_own_stake | 0.1342 | 0.0479 | 0.2456 | 84 | 1.0000 |
| old | convex | both_lose | 0.4665 | 0.3379 | 0.5917 | 292 | 0.2295 |
| old | convex | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan |
| old | convex | normal | 0.4058 | 0.3403 | 0.4654 | 254 | 0.6482 |
| old | convex | opposed | 0.0112 | 0.0000 | 0.0281 | 7 | 0.8571 |
| old | convex | one_sided_win | 0.0128 | 0.0000 | 0.0353 | 8 | 0.6250 |
| old | convex | no_own_stake | 0.1038 | 0.0434 | 0.1872 | 65 | 1.0000 |
| old | top3_stress | both_lose | 0.1885 | 0.1321 | 0.2666 | 118 | 0.0085 |
| old | top3_stress | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan |
| old | top3_stress | normal | 0.4521 | 0.3870 | 0.5351 | 283 | 0.1321 |
| old | top3_stress | opposed | 0.0000 | 0.0000 | 0.0000 | 0 | nan |
| old | top3_stress | one_sided_win | 0.0032 | 0.0000 | 0.0132 | 2 | 0.5000 |
| old | top3_stress | no_own_stake | 0.3562 | 0.2710 | 0.4299 | 223 | 1.0000 |
| new | linear | both_lose | 0.2780 | 0.1646 | 0.3858 | 174 | 0.2644 |
| new | linear | both_win | 0.0048 | 0.0000 | 0.0182 | 3 | 0.3333 |
| new | linear | normal | 0.3962 | 0.3291 | 0.4738 | 248 | 0.6129 |
| new | linear | opposed | 0.0783 | 0.0239 | 0.1425 | 49 | 0.4490 |
| new | linear | one_sided_win | 0.0399 | 0.0065 | 0.0901 | 25 | 0.7600 |
| new | linear | no_own_stake | 0.2029 | 0.0978 | 0.3216 | 127 | 1.0000 |
| new | concave | both_lose | 0.2939 | 0.1796 | 0.3922 | 184 | 0.3261 |
| new | concave | both_win | 0.0016 | 0.0000 | 0.0097 | 1 | 0.0000 |
| new | concave | normal | 0.4153 | 0.3473 | 0.4811 | 260 | 0.6667 |
| new | concave | opposed | 0.0495 | 0.0145 | 0.0944 | 31 | 0.5806 |
| new | concave | one_sided_win | 0.0319 | 0.0036 | 0.0745 | 20 | 0.7500 |
| new | concave | no_own_stake | 0.2077 | 0.1127 | 0.3291 | 130 | 1.0000 |
| new | convex | both_lose | 0.2460 | 0.1445 | 0.3558 | 154 | 0.2208 |
| new | convex | both_win | 0.0048 | 0.0000 | 0.0181 | 3 | 0.0000 |
| new | convex | normal | 0.3786 | 0.3036 | 0.4600 | 237 | 0.5424 |
| new | convex | opposed | 0.0942 | 0.0258 | 0.1721 | 59 | 0.2373 |
| new | convex | one_sided_win | 0.0559 | 0.0166 | 0.1012 | 35 | 0.6286 |
| new | convex | no_own_stake | 0.2204 | 0.1244 | 0.3196 | 138 | 1.0000 |
| new | top3_stress | both_lose | 0.1294 | 0.0731 | 0.1908 | 81 | 0.0247 |
| new | top3_stress | both_win | 0.0064 | 0.0000 | 0.0216 | 4 | 0.0000 |
| new | top3_stress | normal | 0.3323 | 0.2544 | 0.4384 | 208 | 0.2427 |
| new | top3_stress | opposed | 0.0655 | 0.0226 | 0.1113 | 41 | 0.0732 |
| new | top3_stress | one_sided_win | 0.1198 | 0.0497 | 0.1830 | 75 | 0.2877 |
| new | top3_stress | no_own_stake | 0.3466 | 0.2669 | 0.4356 | 217 | 1.0000 |

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
| new | linear | tp_share | 582 | 0.5916 | 0.4400 | 0.5235 | 0.7802 | 1.0000 |
| new | linear | tp_share_raw | 598 | 0.6366 | 0.5016 | 0.5854 | 0.8028 | 0.9758 |
| new | linear | hhi | 582 | 0.3176 | 0.2223 | 0.2977 | 0.3694 | 0.5000 |
| new | linear | n_material | 626 | 5.7955 | 3.0000 | 6.0000 | 8.0000 | 10.0000 |
| new | linear | mean_abs_third | 626 | 0.0017 | 0.0006 | 0.0013 | 0.0023 | 0.0037 |
| new | linear | mean_abs_third_raw | 626 | 0.0020 | 0.0009 | 0.0016 | 0.0026 | 0.0040 |
| new | concave | tp_share | 580 | 0.6101 | 0.4541 | 0.5575 | 0.8192 | 1.0000 |
| new | concave | tp_share_raw | 602 | 0.6514 | 0.5062 | 0.6072 | 0.8122 | 0.9820 |
| new | concave | hhi | 580 | 0.3089 | 0.2113 | 0.2904 | 0.3691 | 0.4693 |
| new | concave | n_material | 626 | 5.7476 | 4.0000 | 6.0000 | 8.0000 | 10.0000 |
| new | concave | mean_abs_third | 626 | 0.0018 | 0.0007 | 0.0015 | 0.0025 | 0.0036 |
| new | concave | mean_abs_third_raw | 626 | 0.0020 | 0.0011 | 0.0017 | 0.0028 | 0.0038 |
| new | convex | tp_share | 556 | 0.5416 | 0.3930 | 0.4966 | 0.7038 | 1.0000 |
| new | convex | tp_share_raw | 587 | 0.6167 | 0.5000 | 0.5522 | 0.7539 | 0.9597 |
| new | convex | hhi | 556 | 0.3817 | 0.2567 | 0.3263 | 0.4295 | 0.5639 |
| new | convex | n_material | 626 | 4.6278 | 2.0000 | 5.0000 | 7.0000 | 8.0000 |
| new | convex | mean_abs_third | 626 | 0.0014 | 0.0003 | 0.0009 | 0.0019 | 0.0033 |
| new | convex | mean_abs_third_raw | 626 | 0.0016 | 0.0006 | 0.0012 | 0.0022 | 0.0036 |
| new | top3_stress | tp_share | 466 | 0.4516 | 0.2928 | 0.4449 | 0.5405 | 1.0000 |
| new | top3_stress | tp_share_raw | 505 | 0.5835 | 0.4953 | 0.5047 | 0.6710 | 0.9783 |
| new | top3_stress | hhi | 466 | 0.4869 | 0.3364 | 0.4196 | 0.5173 | 1.0000 |
| new | top3_stress | n_material | 626 | 2.4872 | 0.0000 | 2.0000 | 4.0000 | 5.0000 |
| new | top3_stress | mean_abs_third | 626 | 0.0005 | 0.0000 | 0.0003 | 0.0007 | 0.0012 |
| new | top3_stress | mean_abs_third_raw | 626 | 0.0007 | 0.0001 | 0.0005 | 0.0010 | 0.0014 |
| new_minus_old | linear | tp_share | 582 | 0.0188 | -0.0268 | 0.0010 | 0.0800 | 0.1680 |
| new_minus_old | linear | hhi | 582 | 0.0215 | -0.0324 | 0.0013 | 0.0621 | 0.1463 |
| new_minus_old | linear | mean_abs_third | 626 | -0.0000 | -0.0004 | 0.0000 | 0.0004 | 0.0011 |
| new_minus_old | concave | tp_share | 578 | 0.0131 | -0.0272 | 0.0000 | 0.0712 | 0.1660 |
| new_minus_old | concave | hhi | 578 | 0.0074 | -0.0406 | 0.0000 | 0.0421 | 0.1198 |
| new_minus_old | concave | mean_abs_third | 626 | -0.0001 | -0.0003 | 0.0000 | 0.0004 | 0.0009 |
| new_minus_old | convex | tp_share | 556 | 0.0243 | -0.0501 | 0.0076 | 0.1044 | 0.2274 |
| new_minus_old | convex | hhi | 556 | 0.0321 | -0.0526 | 0.0007 | 0.0816 | 0.1912 |
| new_minus_old | convex | mean_abs_third | 626 | 0.0001 | -0.0005 | 0.0000 | 0.0005 | 0.0014 |
| new_minus_old | top3_stress | tp_share | 372 | 0.1075 | -0.0271 | 0.0661 | 0.2979 | 0.4679 |
| new_minus_old | top3_stress | hhi | 372 | -0.1026 | -0.3087 | -0.0494 | 0.0653 | 0.2497 |
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

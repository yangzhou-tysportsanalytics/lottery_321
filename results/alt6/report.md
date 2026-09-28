# Registered analysis output

tag `alt6`; exclude_imprecise=False; states=25

## T5_0_diagnostics

| states | games | stopped_2000 | stopped_8000 | stopped_32000 | missed_target | n_worlds_match | max_halfwidth_linear | max_halfwidth_linear_rules_only | max_halfwidth_delta_linear | p95_halfwidth_linear | max_q_total_dev | max_per_slot_dev | per_slot_noise_scale | max_own_slot_dev | max_zero_sum_dev |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 25 | 193 | 0 | 2 | 9 | 14 | 8000 | 0.0043 | 0.0043 | 0.0042 | 0.0041 | 0.0000 | 0.0091 | 0.0056 | 0.0000 | 0.0024 |

## T5_0b_zero_sum_by_curve

| curve | rule | max_zero_sum_dev | mean_zero_sum_dev | n_games |
|---|---|---|---|---|
| linear | old | 0.0006 | 0.0001 | 193 |
| linear | new | 0.0008 | 0.0001 | 193 |
| concave | old | 0.0003 | 0.0001 | 193 |
| concave | new | 0.0004 | 0.0001 | 193 |
| convex | old | 0.0009 | 0.0002 | 193 |
| convex | new | 0.0011 | 0.0002 | 193 |
| top3_stress | old | 0.0024 | 0.0004 | 193 |
| top3_stress | new | 0.0018 | 0.0002 | 193 |

## T5_0c_verdict_by_look

| rule | portfolio | stopped_at | verdict_B | verdict_B_pm | count |
|---|---|---|---|---|---|
| delta | actual | 32000 | dominance_positive | dominance_positive | 19 |
| delta | actual | 32000 | dominance_positive | unresolved | 1 |
| delta | actual | 32000 | negligible | negligible | 34 |
| delta | actual | 32000 | negligible | unresolved | 1 |
| delta | actual | 32000 | reversal | reversal | 62 |
| delta | actual | 32000 | reversal | unresolved | 5 |
| delta | actual | 32000 | unresolved | unresolved | 4 |
| delta | actual | 8000 | dominance_positive | dominance_positive | 2 |
| delta | actual | 8000 | negligible | negligible | 8 |
| delta | actual | 8000 | reversal | reversal | 6 |
| delta | actual | 8000 | unresolved | unresolved | 2 |
| delta | actual | missed | dominance_positive | dominance_positive | 38 |
| delta | actual | missed | dominance_positive | unresolved | 6 |
| delta | actual | missed | negligible | negligible | 59 |
| delta | actual | missed | negligible | unresolved | 2 |
| delta | actual | missed | reversal | reversal | 130 |
| delta | actual | missed | reversal | unresolved | 2 |
| delta | actual | missed | unresolved | unresolved | 5 |
| delta | own | 32000 | dominance_positive | dominance_positive | 4 |
| delta | own | 32000 | dominance_positive | unresolved | 2 |
| delta | own | 32000 | negligible | dominance_positive | 2 |
| delta | own | 32000 | negligible | negligible | 23 |
| delta | own | 32000 | negligible | unresolved | 1 |
| delta | own | 32000 | reversal | reversal | 84 |
| delta | own | 32000 | reversal | unresolved | 4 |
| delta | own | 32000 | unresolved | unresolved | 6 |
| delta | own | 8000 | dominance_positive | dominance_positive | 1 |
| delta | own | 8000 | negligible | negligible | 5 |
| delta | own | 8000 | reversal | reversal | 10 |
| delta | own | 8000 | unresolved | unresolved | 2 |
| delta | own | missed | dominance_positive | dominance_positive | 5 |
| delta | own | missed | dominance_positive | unresolved | 7 |
| delta | own | missed | negligible | dominance_positive | 1 |
| delta | own | missed | negligible | negligible | 38 |
| delta | own | missed | negligible | unresolved | 2 |
| delta | own | missed | reversal | reversal | 162 |
| delta | own | missed | reversal | unresolved | 8 |
| delta | own | missed | unresolved | unresolved | 19 |
| new | actual | 32000 | dominance_positive | dominance_positive | 72 |
| new | actual | 32000 | dominance_positive | unresolved | 1 |
| new | actual | 32000 | negligible | dominance_positive | 1 |
| new | actual | 32000 | negligible | negligible | 26 |
| new | actual | 32000 | negligible | unresolved | 5 |
| new | actual | 32000 | reversal | reversal | 17 |
| new | actual | 32000 | reversal | unresolved | 1 |
| new | actual | 32000 | unresolved | unresolved | 3 |
| new | actual | 8000 | dominance_positive | dominance_positive | 14 |
| new | actual | 8000 | negligible | negligible | 4 |
| new | actual | missed | dominance_positive | dominance_positive | 140 |
| new | actual | missed | dominance_positive | unresolved | 4 |
| new | actual | missed | negligible | negligible | 54 |
| new | actual | missed | negligible | unresolved | 7 |
| new | actual | missed | reversal | reversal | 24 |
| new | actual | missed | reversal | unresolved | 3 |
| new | actual | missed | unresolved | unresolved | 10 |
| new | own | 32000 | dominance_positive | dominance_positive | 88 |
| new | own | 32000 | dominance_positive | unresolved | 1 |
| new | own | 32000 | negligible | dominance_positive | 1 |
| new | own | 32000 | negligible | negligible | 18 |
| new | own | 32000 | reversal | reversal | 16 |
| new | own | 32000 | unresolved | unresolved | 2 |
| new | own | 8000 | dominance_positive | dominance_positive | 18 |
| new | own | missed | dominance_positive | dominance_positive | 177 |
| new | own | missed | dominance_positive | unresolved | 2 |
| new | own | missed | negligible | dominance_positive | 4 |
| new | own | missed | negligible | negligible | 29 |
| new | own | missed | negligible | unresolved | 1 |
| new | own | missed | reversal | reversal | 24 |
| new | own | missed | reversal | unresolved | 3 |
| new | own | missed | unresolved | unresolved | 2 |
| old | actual | 32000 | dominance_positive | dominance_positive | 98 |
| old | actual | 32000 | dominance_positive | unresolved | 1 |
| old | actual | 32000 | negligible | negligible | 23 |
| old | actual | 32000 | reversal | reversal | 4 |
| old | actual | 8000 | dominance_positive | dominance_positive | 13 |
| old | actual | 8000 | negligible | negligible | 5 |
| old | actual | missed | dominance_positive | dominance_positive | 182 |
| old | actual | missed | dominance_positive | unresolved | 3 |
| old | actual | missed | negligible | dominance_positive | 3 |
| old | actual | missed | negligible | negligible | 40 |
| old | actual | missed | reversal | reversal | 4 |
| old | actual | missed | unresolved | unresolved | 10 |
| old | own | 32000 | dominance_positive | dominance_positive | 124 |
| old | own | 32000 | negligible | negligible | 2 |
| old | own | 8000 | dominance_positive | dominance_positive | 18 |
| old | own | missed | dominance_positive | dominance_positive | 240 |
| old | own | missed | negligible | negligible | 2 |

## T5_0d_band_width

| rule | portfolio | measure | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| old | actual | band_ratio | 386 | 1.3067 | 0.1908 | 1.1413 | 2.3097 | 2.7072 |
| old | actual | band_ratio_pm | 386 | 2.4927 | 0.3815 | 2.2467 | 4.5631 | 5.3115 |
| old | own | band_ratio | 386 | 1.9136 | 0.7842 | 2.2580 | 2.6589 | 2.9942 |
| old | own | band_ratio_pm | 386 | 3.6362 | 1.4099 | 4.4843 | 5.2590 | 5.7556 |
| new | actual | band_ratio | 386 | 1.1257 | 0.1760 | 0.6311 | 2.2696 | 2.6504 |
| new | actual | band_ratio_pm | 386 | 2.1339 | 0.3484 | 1.2623 | 4.4561 | 5.2108 |
| new | own | band_ratio | 386 | 1.5816 | 0.2225 | 2.1346 | 2.5419 | 2.8104 |
| new | own | band_ratio_pm | 386 | 2.9927 | 0.4241 | 4.2313 | 5.0421 | 5.4643 |
| delta | actual | band_ratio | 386 | 0.9955 | 0.1882 | 0.5635 | 1.6646 | 2.4042 |
| delta | actual | band_ratio_pm | 386 | 1.9250 | 0.3730 | 1.0806 | 3.3000 | 4.6647 |
| delta | own | band_ratio | 386 | 1.3724 | 0.4289 | 1.0231 | 2.3777 | 2.8695 |
| delta | own | band_ratio_pm | 386 | 2.6306 | 0.8579 | 2.0363 | 4.6696 | 5.6097 |

## T5_1_verdicts

| rule | portfolio | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|
| old | actual | B | dominance_positive | 0.7694 | 0.7257 | 0.8146 | 386 |
| old | actual | B | reversal | 0.0207 | 0.0060 | 0.0352 | 386 |
| old | actual | B | negligible | 0.1839 | 0.1451 | 0.2216 | 386 |
| old | actual | B | unresolved | 0.0259 | 0.0087 | 0.0464 | 386 |
| old | actual | C | dominance_positive | 0.7694 | 0.7257 | 0.8146 | 386 |
| old | actual | C | reversal | 0.0207 | 0.0060 | 0.0352 | 386 |
| old | actual | C | negligible | 0.1839 | 0.1451 | 0.2216 | 386 |
| old | actual | C | unresolved | 0.0259 | 0.0087 | 0.0464 | 386 |
| old | actual | B_pm | dominance_positive | 0.7668 | 0.7228 | 0.8142 | 386 |
| old | actual | B_pm | reversal | 0.0207 | 0.0060 | 0.0352 | 386 |
| old | actual | B_pm | negligible | 0.1762 | 0.1381 | 0.2143 | 386 |
| old | actual | B_pm | unresolved | 0.0363 | 0.0156 | 0.0596 | 386 |
| old | actual | C_pm | dominance_positive | 0.7668 | 0.7228 | 0.8142 | 386 |
| old | actual | C_pm | reversal | 0.0207 | 0.0060 | 0.0352 | 386 |
| old | actual | C_pm | negligible | 0.1762 | 0.1381 | 0.2143 | 386 |
| old | actual | C_pm | unresolved | 0.0363 | 0.0156 | 0.0596 | 386 |
| old | own | B | dominance_positive | 0.9896 | 0.9751 | 1.0000 | 386 |
| old | own | B | reversal | 0.0000 | 0.0000 | 0.0000 | 386 |
| old | own | B | negligible | 0.0104 | 0.0000 | 0.0249 | 386 |
| old | own | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 386 |
| old | own | C | dominance_positive | 0.9896 | 0.9751 | 1.0000 | 386 |
| old | own | C | reversal | 0.0000 | 0.0000 | 0.0000 | 386 |
| old | own | C | negligible | 0.0104 | 0.0000 | 0.0249 | 386 |
| old | own | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 386 |
| old | own | B_pm | dominance_positive | 0.9896 | 0.9751 | 1.0000 | 386 |
| old | own | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 386 |
| old | own | B_pm | negligible | 0.0104 | 0.0000 | 0.0249 | 386 |
| old | own | B_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 386 |
| old | own | C_pm | dominance_positive | 0.9896 | 0.9751 | 1.0000 | 386 |
| old | own | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 386 |
| old | own | C_pm | negligible | 0.0104 | 0.0000 | 0.0249 | 386 |
| old | own | C_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 386 |
| new | actual | B | dominance_positive | 0.5984 | 0.5442 | 0.6541 | 386 |
| new | actual | B | reversal | 0.1166 | 0.0799 | 0.1503 | 386 |
| new | actual | B | negligible | 0.2513 | 0.2016 | 0.3059 | 386 |
| new | actual | B | unresolved | 0.0337 | 0.0149 | 0.0528 | 386 |
| new | actual | C | dominance_positive | 0.5984 | 0.5442 | 0.6541 | 386 |
| new | actual | C | reversal | 0.1166 | 0.0799 | 0.1503 | 386 |
| new | actual | C | negligible | 0.2513 | 0.2016 | 0.3059 | 386 |
| new | actual | C | unresolved | 0.0337 | 0.0149 | 0.0528 | 386 |
| new | actual | B_pm | dominance_positive | 0.5881 | 0.5343 | 0.6429 | 386 |
| new | actual | B_pm | reversal | 0.1062 | 0.0730 | 0.1359 | 386 |
| new | actual | B_pm | negligible | 0.2176 | 0.1736 | 0.2619 | 386 |
| new | actual | B_pm | unresolved | 0.0881 | 0.0612 | 0.1158 | 386 |
| new | actual | C_pm | dominance_positive | 0.5881 | 0.5343 | 0.6429 | 386 |
| new | actual | C_pm | reversal | 0.1062 | 0.0730 | 0.1359 | 386 |
| new | actual | C_pm | negligible | 0.2176 | 0.1736 | 0.2619 | 386 |
| new | actual | C_pm | unresolved | 0.0881 | 0.0612 | 0.1158 | 386 |
| new | own | B | dominance_positive | 0.7409 | 0.6779 | 0.8030 | 386 |
| new | own | B | reversal | 0.1114 | 0.0755 | 0.1440 | 386 |
| new | own | B | negligible | 0.1373 | 0.0829 | 0.1951 | 386 |
| new | own | B | unresolved | 0.0104 | 0.0000 | 0.0243 | 386 |
| new | own | C | dominance_positive | 0.7409 | 0.6779 | 0.8030 | 386 |
| new | own | C | reversal | 0.1114 | 0.0755 | 0.1440 | 386 |
| new | own | C | negligible | 0.1373 | 0.0829 | 0.1951 | 386 |
| new | own | C | unresolved | 0.0104 | 0.0000 | 0.0243 | 386 |
| new | own | B_pm | dominance_positive | 0.7461 | 0.6899 | 0.8060 | 386 |
| new | own | B_pm | reversal | 0.1036 | 0.0690 | 0.1359 | 386 |
| new | own | B_pm | negligible | 0.1218 | 0.0751 | 0.1706 | 386 |
| new | own | B_pm | unresolved | 0.0285 | 0.0106 | 0.0493 | 386 |
| new | own | C_pm | dominance_positive | 0.7461 | 0.6899 | 0.8060 | 386 |
| new | own | C_pm | reversal | 0.1036 | 0.0690 | 0.1359 | 386 |
| new | own | C_pm | negligible | 0.1218 | 0.0751 | 0.1706 | 386 |
| new | own | C_pm | unresolved | 0.0285 | 0.0106 | 0.0493 | 386 |
| delta | actual | B | dominance_positive | 0.1710 | 0.1265 | 0.2170 | 386 |
| delta | actual | B | reversal | 0.5311 | 0.4649 | 0.5924 | 386 |
| delta | actual | B | negligible | 0.2694 | 0.2324 | 0.3133 | 386 |
| delta | actual | B | unresolved | 0.0285 | 0.0095 | 0.0518 | 386 |
| delta | actual | C | dominance_positive | 0.1710 | 0.1265 | 0.2170 | 386 |
| delta | actual | C | reversal | 0.5311 | 0.4649 | 0.5924 | 386 |
| delta | actual | C | negligible | 0.2694 | 0.2324 | 0.3133 | 386 |
| delta | actual | C | unresolved | 0.0285 | 0.0095 | 0.0518 | 386 |
| delta | actual | B_pm | dominance_positive | 0.1528 | 0.1160 | 0.1900 | 386 |
| delta | actual | B_pm | reversal | 0.5130 | 0.4454 | 0.5744 | 386 |
| delta | actual | B_pm | negligible | 0.2617 | 0.2225 | 0.3082 | 386 |
| delta | actual | B_pm | unresolved | 0.0725 | 0.0479 | 0.0968 | 386 |
| delta | actual | C_pm | dominance_positive | 0.1528 | 0.1160 | 0.1900 | 386 |
| delta | actual | C_pm | reversal | 0.5130 | 0.4454 | 0.5744 | 386 |
| delta | actual | C_pm | negligible | 0.2617 | 0.2225 | 0.3082 | 386 |
| delta | actual | C_pm | unresolved | 0.0725 | 0.0479 | 0.0968 | 386 |
| delta | own | B | dominance_positive | 0.0492 | 0.0190 | 0.0856 | 386 |
| delta | own | B | reversal | 0.6943 | 0.6324 | 0.7524 | 386 |
| delta | own | B | negligible | 0.1865 | 0.1473 | 0.2310 | 386 |
| delta | own | B | unresolved | 0.0699 | 0.0364 | 0.1099 | 386 |
| delta | own | C | dominance_positive | 0.0492 | 0.0190 | 0.0856 | 386 |
| delta | own | C | reversal | 0.6943 | 0.6324 | 0.7524 | 386 |
| delta | own | C | negligible | 0.1865 | 0.1473 | 0.2310 | 386 |
| delta | own | C | unresolved | 0.0699 | 0.0364 | 0.1099 | 386 |
| delta | own | B_pm | dominance_positive | 0.0337 | 0.0153 | 0.0521 | 386 |
| delta | own | B_pm | reversal | 0.6632 | 0.6029 | 0.7219 | 386 |
| delta | own | B_pm | negligible | 0.1710 | 0.1377 | 0.2096 | 386 |
| delta | own | B_pm | unresolved | 0.1321 | 0.0878 | 0.1791 | 386 |
| delta | own | C_pm | dominance_positive | 0.0337 | 0.0153 | 0.0521 | 386 |
| delta | own | C_pm | reversal | 0.6632 | 0.6029 | 0.7219 | 386 |
| delta | own | C_pm | negligible | 0.1710 | 0.1377 | 0.2096 | 386 |
| delta | own | C_pm | unresolved | 0.1321 | 0.0878 | 0.1791 | 386 |

## T5_2_verdicts_by_band

| rule | portfolio | band | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| old | actual | 1-3 | B | dominance_positive | 0.7317 | 0.5833 | 0.8750 | 41 |
| old | actual | 1-3 | B | reversal | 0.0732 | 0.0000 | 0.1905 | 41 |
| old | actual | 1-3 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 41 |
| old | actual | 1-3 | B | unresolved | 0.1951 | 0.0645 | 0.3500 | 41 |
| old | actual | 1-3 | C | dominance_positive | 0.7317 | 0.5833 | 0.8750 | 41 |
| old | actual | 1-3 | C | reversal | 0.0732 | 0.0000 | 0.1905 | 41 |
| old | actual | 1-3 | C | negligible | 0.0000 | 0.0000 | 0.0000 | 41 |
| old | actual | 1-3 | C | unresolved | 0.1951 | 0.0645 | 0.3500 | 41 |
| old | actual | 1-3 | B_pm | dominance_positive | 0.6829 | 0.5484 | 0.8182 | 41 |
| old | actual | 1-3 | B_pm | reversal | 0.0732 | 0.0000 | 0.1905 | 41 |
| old | actual | 1-3 | B_pm | negligible | 0.0000 | 0.0000 | 0.0000 | 41 |
| old | actual | 1-3 | B_pm | unresolved | 0.2439 | 0.1071 | 0.3846 | 41 |
| old | actual | 1-3 | C_pm | dominance_positive | 0.6829 | 0.5484 | 0.8182 | 41 |
| old | actual | 1-3 | C_pm | reversal | 0.0732 | 0.0000 | 0.1905 | 41 |
| old | actual | 1-3 | C_pm | negligible | 0.0000 | 0.0000 | 0.0000 | 41 |
| old | actual | 1-3 | C_pm | unresolved | 0.2439 | 0.1071 | 0.3846 | 41 |
| old | actual | 4-10 | B | dominance_positive | 0.8132 | 0.7206 | 0.8941 | 91 |
| old | actual | 4-10 | B | reversal | 0.0220 | 0.0000 | 0.0676 | 91 |
| old | actual | 4-10 | B | negligible | 0.1429 | 0.0800 | 0.2073 | 91 |
| old | actual | 4-10 | B | unresolved | 0.0220 | 0.0000 | 0.0690 | 91 |
| old | actual | 4-10 | C | dominance_positive | 0.8132 | 0.7206 | 0.8941 | 91 |
| old | actual | 4-10 | C | reversal | 0.0220 | 0.0000 | 0.0676 | 91 |
| old | actual | 4-10 | C | negligible | 0.1429 | 0.0800 | 0.2073 | 91 |
| old | actual | 4-10 | C | unresolved | 0.0220 | 0.0000 | 0.0690 | 91 |
| old | actual | 4-10 | B_pm | dominance_positive | 0.8022 | 0.7027 | 0.8900 | 91 |
| old | actual | 4-10 | B_pm | reversal | 0.0220 | 0.0000 | 0.0676 | 91 |
| old | actual | 4-10 | B_pm | negligible | 0.1429 | 0.0800 | 0.2073 | 91 |
| old | actual | 4-10 | B_pm | unresolved | 0.0330 | 0.0000 | 0.0870 | 91 |
| old | actual | 4-10 | C_pm | dominance_positive | 0.8022 | 0.7027 | 0.8900 | 91 |
| old | actual | 4-10 | C_pm | reversal | 0.0220 | 0.0000 | 0.0676 | 91 |
| old | actual | 4-10 | C_pm | negligible | 0.1429 | 0.0800 | 0.2073 | 91 |
| old | actual | 4-10 | C_pm | unresolved | 0.0330 | 0.0000 | 0.0870 | 91 |
| old | actual | 11-16 | B | dominance_positive | 0.7595 | 0.6786 | 0.8361 | 79 |
| old | actual | 11-16 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | actual | 11-16 | B | negligible | 0.2405 | 0.1639 | 0.3214 | 79 |
| old | actual | 11-16 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | actual | 11-16 | C | dominance_positive | 0.7595 | 0.6786 | 0.8361 | 79 |
| old | actual | 11-16 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | actual | 11-16 | C | negligible | 0.2405 | 0.1639 | 0.3214 | 79 |
| old | actual | 11-16 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | actual | 11-16 | B_pm | dominance_positive | 0.7595 | 0.6786 | 0.8361 | 79 |
| old | actual | 11-16 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | actual | 11-16 | B_pm | negligible | 0.2278 | 0.1507 | 0.3067 | 79 |
| old | actual | 11-16 | B_pm | unresolved | 0.0127 | 0.0000 | 0.0571 | 79 |
| old | actual | 11-16 | C_pm | dominance_positive | 0.7595 | 0.6786 | 0.8361 | 79 |
| old | actual | 11-16 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | actual | 11-16 | C_pm | negligible | 0.2278 | 0.1507 | 0.3067 | 79 |
| old | actual | 11-16 | C_pm | unresolved | 0.0127 | 0.0000 | 0.0571 | 79 |
| old | actual | 17-30 | B | dominance_positive | 0.7600 | 0.6923 | 0.8229 | 175 |
| old | actual | 17-30 | B | reversal | 0.0171 | 0.0000 | 0.0429 | 175 |
| old | actual | 17-30 | B | negligible | 0.2229 | 0.1517 | 0.2973 | 175 |
| old | actual | 17-30 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 175 |
| old | actual | 17-30 | C | dominance_positive | 0.7600 | 0.6923 | 0.8229 | 175 |
| old | actual | 17-30 | C | reversal | 0.0171 | 0.0000 | 0.0429 | 175 |
| old | actual | 17-30 | C | negligible | 0.2229 | 0.1517 | 0.2973 | 175 |
| old | actual | 17-30 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 175 |
| old | actual | 17-30 | B_pm | dominance_positive | 0.7714 | 0.7011 | 0.8389 | 175 |
| old | actual | 17-30 | B_pm | reversal | 0.0171 | 0.0000 | 0.0429 | 175 |
| old | actual | 17-30 | B_pm | negligible | 0.2114 | 0.1379 | 0.2882 | 175 |
| old | actual | 17-30 | B_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 175 |
| old | actual | 17-30 | C_pm | dominance_positive | 0.7714 | 0.7011 | 0.8389 | 175 |
| old | actual | 17-30 | C_pm | reversal | 0.0171 | 0.0000 | 0.0429 | 175 |
| old | actual | 17-30 | C_pm | negligible | 0.2114 | 0.1379 | 0.2882 | 175 |
| old | actual | 17-30 | C_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 175 |
| old | own | 1-3 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 41 |
| old | own | 1-3 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 41 |
| old | own | 1-3 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 41 |
| old | own | 1-3 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 41 |
| old | own | 1-3 | C | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 41 |
| old | own | 1-3 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 41 |
| old | own | 1-3 | C | negligible | 0.0000 | 0.0000 | 0.0000 | 41 |
| old | own | 1-3 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 41 |
| old | own | 1-3 | B_pm | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 41 |
| old | own | 1-3 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 41 |
| old | own | 1-3 | B_pm | negligible | 0.0000 | 0.0000 | 0.0000 | 41 |
| old | own | 1-3 | B_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 41 |
| old | own | 1-3 | C_pm | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 41 |
| old | own | 1-3 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 41 |
| old | own | 1-3 | C_pm | negligible | 0.0000 | 0.0000 | 0.0000 | 41 |
| old | own | 1-3 | C_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 41 |
| old | own | 4-10 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 91 |
| old | own | 4-10 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 91 |
| old | own | 4-10 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 91 |
| old | own | 4-10 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 91 |
| old | own | 4-10 | C | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 91 |
| old | own | 4-10 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 91 |
| old | own | 4-10 | C | negligible | 0.0000 | 0.0000 | 0.0000 | 91 |
| old | own | 4-10 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 91 |
| old | own | 4-10 | B_pm | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 91 |
| old | own | 4-10 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 91 |
| old | own | 4-10 | B_pm | negligible | 0.0000 | 0.0000 | 0.0000 | 91 |
| old | own | 4-10 | B_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 91 |
| old | own | 4-10 | C_pm | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 91 |
| old | own | 4-10 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 91 |
| old | own | 4-10 | C_pm | negligible | 0.0000 | 0.0000 | 0.0000 | 91 |
| old | own | 4-10 | C_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 91 |
| old | own | 11-16 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 79 |
| old | own | 11-16 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | own | 11-16 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | own | 11-16 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | own | 11-16 | C | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 79 |
| old | own | 11-16 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | own | 11-16 | C | negligible | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | own | 11-16 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | own | 11-16 | B_pm | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 79 |
| old | own | 11-16 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | own | 11-16 | B_pm | negligible | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | own | 11-16 | B_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | own | 11-16 | C_pm | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 79 |
| old | own | 11-16 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | own | 11-16 | C_pm | negligible | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | own | 11-16 | C_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| old | own | 17-30 | B | dominance_positive | 0.9771 | 0.9441 | 1.0000 | 175 |
| old | own | 17-30 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 175 |
| old | own | 17-30 | B | negligible | 0.0229 | 0.0000 | 0.0559 | 175 |
| old | own | 17-30 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 175 |
| old | own | 17-30 | C | dominance_positive | 0.9771 | 0.9441 | 1.0000 | 175 |
| old | own | 17-30 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 175 |
| old | own | 17-30 | C | negligible | 0.0229 | 0.0000 | 0.0559 | 175 |
| old | own | 17-30 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 175 |
| old | own | 17-30 | B_pm | dominance_positive | 0.9771 | 0.9441 | 1.0000 | 175 |
| old | own | 17-30 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 175 |
| old | own | 17-30 | B_pm | negligible | 0.0229 | 0.0000 | 0.0559 | 175 |
| old | own | 17-30 | B_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 175 |
| old | own | 17-30 | C_pm | dominance_positive | 0.9771 | 0.9441 | 1.0000 | 175 |
| old | own | 17-30 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 175 |
| old | own | 17-30 | C_pm | negligible | 0.0229 | 0.0000 | 0.0559 | 175 |
| old | own | 17-30 | C_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 175 |
| new | actual | 1-3 | B | dominance_positive | 0.2683 | 0.1224 | 0.4324 | 41 |
| new | actual | 1-3 | B | reversal | 0.4390 | 0.3095 | 0.5610 | 41 |
| new | actual | 1-3 | B | negligible | 0.0976 | 0.0000 | 0.2143 | 41 |
| new | actual | 1-3 | B | unresolved | 0.1951 | 0.0625 | 0.3636 | 41 |
| new | actual | 1-3 | C | dominance_positive | 0.2683 | 0.1224 | 0.4324 | 41 |
| new | actual | 1-3 | C | reversal | 0.4390 | 0.3095 | 0.5610 | 41 |
| new | actual | 1-3 | C | negligible | 0.0976 | 0.0000 | 0.2143 | 41 |
| new | actual | 1-3 | C | unresolved | 0.1951 | 0.0625 | 0.3636 | 41 |
| new | actual | 1-3 | B_pm | dominance_positive | 0.2927 | 0.1463 | 0.4468 | 41 |
| new | actual | 1-3 | B_pm | reversal | 0.3902 | 0.2812 | 0.5116 | 41 |
| new | actual | 1-3 | B_pm | negligible | 0.0732 | 0.0000 | 0.1842 | 41 |
| new | actual | 1-3 | B_pm | unresolved | 0.2439 | 0.1053 | 0.3871 | 41 |
| new | actual | 1-3 | C_pm | dominance_positive | 0.2927 | 0.1463 | 0.4468 | 41 |
| new | actual | 1-3 | C_pm | reversal | 0.3902 | 0.2812 | 0.5116 | 41 |
| new | actual | 1-3 | C_pm | negligible | 0.0732 | 0.0000 | 0.1842 | 41 |
| new | actual | 1-3 | C_pm | unresolved | 0.2439 | 0.1053 | 0.3871 | 41 |
| new | actual | 4-10 | B | dominance_positive | 0.2198 | 0.1373 | 0.3030 | 91 |
| new | actual | 4-10 | B | reversal | 0.2637 | 0.1771 | 0.3535 | 91 |
| new | actual | 4-10 | B | negligible | 0.4835 | 0.3924 | 0.5780 | 91 |
| new | actual | 4-10 | B | unresolved | 0.0330 | 0.0000 | 0.0875 | 91 |
| new | actual | 4-10 | C | dominance_positive | 0.2198 | 0.1373 | 0.3030 | 91 |
| new | actual | 4-10 | C | reversal | 0.2637 | 0.1771 | 0.3535 | 91 |
| new | actual | 4-10 | C | negligible | 0.4835 | 0.3924 | 0.5780 | 91 |
| new | actual | 4-10 | C | unresolved | 0.0330 | 0.0000 | 0.0875 | 91 |
| new | actual | 4-10 | B_pm | dominance_positive | 0.1978 | 0.1158 | 0.2857 | 91 |
| new | actual | 4-10 | B_pm | reversal | 0.2418 | 0.1519 | 0.3372 | 91 |
| new | actual | 4-10 | B_pm | negligible | 0.3626 | 0.2571 | 0.4731 | 91 |
| new | actual | 4-10 | B_pm | unresolved | 0.1978 | 0.1161 | 0.2857 | 91 |
| new | actual | 4-10 | C_pm | dominance_positive | 0.1978 | 0.1158 | 0.2857 | 91 |
| new | actual | 4-10 | C_pm | reversal | 0.2418 | 0.1519 | 0.3372 | 91 |
| new | actual | 4-10 | C_pm | negligible | 0.3626 | 0.2571 | 0.4731 | 91 |
| new | actual | 4-10 | C_pm | unresolved | 0.1978 | 0.1161 | 0.2857 | 91 |
| new | actual | 11-16 | B | dominance_positive | 0.7595 | 0.6721 | 0.8387 | 79 |
| new | actual | 11-16 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | actual | 11-16 | B | negligible | 0.2405 | 0.1613 | 0.3279 | 79 |
| new | actual | 11-16 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | actual | 11-16 | C | dominance_positive | 0.7595 | 0.6721 | 0.8387 | 79 |
| new | actual | 11-16 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | actual | 11-16 | C | negligible | 0.2405 | 0.1613 | 0.3279 | 79 |
| new | actual | 11-16 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | actual | 11-16 | B_pm | dominance_positive | 0.7215 | 0.6250 | 0.8169 | 79 |
| new | actual | 11-16 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | actual | 11-16 | B_pm | negligible | 0.2278 | 0.1558 | 0.2973 | 79 |
| new | actual | 11-16 | B_pm | unresolved | 0.0506 | 0.0000 | 0.1154 | 79 |
| new | actual | 11-16 | C_pm | dominance_positive | 0.7215 | 0.6250 | 0.8169 | 79 |
| new | actual | 11-16 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | actual | 11-16 | C_pm | negligible | 0.2278 | 0.1558 | 0.2973 | 79 |
| new | actual | 11-16 | C_pm | unresolved | 0.0506 | 0.0000 | 0.1154 | 79 |
| new | actual | 17-30 | B | dominance_positive | 0.8000 | 0.7514 | 0.8482 | 175 |
| new | actual | 17-30 | B | reversal | 0.0171 | 0.0000 | 0.0441 | 175 |
| new | actual | 17-30 | B | negligible | 0.1714 | 0.1160 | 0.2291 | 175 |
| new | actual | 17-30 | B | unresolved | 0.0114 | 0.0000 | 0.0333 | 175 |
| new | actual | 17-30 | C | dominance_positive | 0.8000 | 0.7514 | 0.8482 | 175 |
| new | actual | 17-30 | C | reversal | 0.0171 | 0.0000 | 0.0441 | 175 |
| new | actual | 17-30 | C | negligible | 0.1714 | 0.1160 | 0.2291 | 175 |
| new | actual | 17-30 | C | unresolved | 0.0114 | 0.0000 | 0.0333 | 175 |
| new | actual | 17-30 | B_pm | dominance_positive | 0.8000 | 0.7514 | 0.8482 | 175 |
| new | actual | 17-30 | B_pm | reversal | 0.0171 | 0.0000 | 0.0441 | 175 |
| new | actual | 17-30 | B_pm | negligible | 0.1714 | 0.1160 | 0.2291 | 175 |
| new | actual | 17-30 | B_pm | unresolved | 0.0114 | 0.0000 | 0.0333 | 175 |
| new | actual | 17-30 | C_pm | dominance_positive | 0.8000 | 0.7514 | 0.8482 | 175 |
| new | actual | 17-30 | C_pm | reversal | 0.0171 | 0.0000 | 0.0441 | 175 |
| new | actual | 17-30 | C_pm | negligible | 0.1714 | 0.1160 | 0.2291 | 175 |
| new | actual | 17-30 | C_pm | unresolved | 0.0114 | 0.0000 | 0.0333 | 175 |
| new | own | 1-3 | B | dominance_positive | 0.2683 | 0.1250 | 0.4286 | 41 |
| new | own | 1-3 | B | reversal | 0.5122 | 0.3333 | 0.6667 | 41 |
| new | own | 1-3 | B | negligible | 0.1463 | 0.0270 | 0.2973 | 41 |
| new | own | 1-3 | B | unresolved | 0.0732 | 0.0000 | 0.1944 | 41 |
| new | own | 1-3 | C | dominance_positive | 0.2683 | 0.1250 | 0.4286 | 41 |
| new | own | 1-3 | C | reversal | 0.5122 | 0.3333 | 0.6667 | 41 |
| new | own | 1-3 | C | negligible | 0.1463 | 0.0270 | 0.2973 | 41 |
| new | own | 1-3 | C | unresolved | 0.0732 | 0.0000 | 0.1944 | 41 |
| new | own | 1-3 | B_pm | dominance_positive | 0.2683 | 0.1276 | 0.4375 | 41 |
| new | own | 1-3 | B_pm | reversal | 0.4878 | 0.3125 | 0.6471 | 41 |
| new | own | 1-3 | B_pm | negligible | 0.1220 | 0.0213 | 0.2728 | 41 |
| new | own | 1-3 | B_pm | unresolved | 0.1220 | 0.0222 | 0.2400 | 41 |
| new | own | 1-3 | C_pm | dominance_positive | 0.2683 | 0.1276 | 0.4375 | 41 |
| new | own | 1-3 | C_pm | reversal | 0.4878 | 0.3125 | 0.6471 | 41 |
| new | own | 1-3 | C_pm | negligible | 0.1220 | 0.0213 | 0.2728 | 41 |
| new | own | 1-3 | C_pm | unresolved | 0.1220 | 0.0222 | 0.2400 | 41 |
| new | own | 4-10 | B | dominance_positive | 0.3297 | 0.1959 | 0.4605 | 91 |
| new | own | 4-10 | B | reversal | 0.2418 | 0.1512 | 0.3380 | 91 |
| new | own | 4-10 | B | negligible | 0.4176 | 0.2740 | 0.5701 | 91 |
| new | own | 4-10 | B | unresolved | 0.0110 | 0.0000 | 0.0449 | 91 |
| new | own | 4-10 | C | dominance_positive | 0.3297 | 0.1959 | 0.4605 | 91 |
| new | own | 4-10 | C | reversal | 0.2418 | 0.1512 | 0.3380 | 91 |
| new | own | 4-10 | C | negligible | 0.4176 | 0.2740 | 0.5701 | 91 |
| new | own | 4-10 | C | unresolved | 0.0110 | 0.0000 | 0.0449 | 91 |
| new | own | 4-10 | B_pm | dominance_positive | 0.3297 | 0.1839 | 0.4691 | 91 |
| new | own | 4-10 | B_pm | reversal | 0.2198 | 0.1287 | 0.3196 | 91 |
| new | own | 4-10 | B_pm | negligible | 0.3846 | 0.2533 | 0.5192 | 91 |
| new | own | 4-10 | B_pm | unresolved | 0.0659 | 0.0122 | 0.1215 | 91 |
| new | own | 4-10 | C_pm | dominance_positive | 0.3297 | 0.1839 | 0.4691 | 91 |
| new | own | 4-10 | C_pm | reversal | 0.2198 | 0.1287 | 0.3196 | 91 |
| new | own | 4-10 | C_pm | negligible | 0.3846 | 0.2533 | 0.5192 | 91 |
| new | own | 4-10 | C_pm | unresolved | 0.0659 | 0.0122 | 0.1215 | 91 |
| new | own | 11-16 | B | dominance_positive | 0.9367 | 0.8611 | 0.9890 | 79 |
| new | own | 11-16 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | own | 11-16 | B | negligible | 0.0633 | 0.0110 | 0.1389 | 79 |
| new | own | 11-16 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | own | 11-16 | C | dominance_positive | 0.9367 | 0.8611 | 0.9890 | 79 |
| new | own | 11-16 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | own | 11-16 | C | negligible | 0.0633 | 0.0110 | 0.1389 | 79 |
| new | own | 11-16 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | own | 11-16 | B_pm | dominance_positive | 0.9620 | 0.9014 | 1.0000 | 79 |
| new | own | 11-16 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | own | 11-16 | B_pm | negligible | 0.0380 | 0.0000 | 0.0986 | 79 |
| new | own | 11-16 | B_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | own | 11-16 | C_pm | dominance_positive | 0.9620 | 0.9014 | 1.0000 | 79 |
| new | own | 11-16 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | own | 11-16 | C_pm | negligible | 0.0380 | 0.0000 | 0.0986 | 79 |
| new | own | 11-16 | C_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 79 |
| new | own | 17-30 | B | dominance_positive | 0.9771 | 0.9441 | 1.0000 | 175 |
| new | own | 17-30 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 175 |
| new | own | 17-30 | B | negligible | 0.0229 | 0.0000 | 0.0559 | 175 |
| new | own | 17-30 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 175 |
| new | own | 17-30 | C | dominance_positive | 0.9771 | 0.9441 | 1.0000 | 175 |
| new | own | 17-30 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 175 |
| new | own | 17-30 | C | negligible | 0.0229 | 0.0000 | 0.0559 | 175 |
| new | own | 17-30 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 175 |
| new | own | 17-30 | B_pm | dominance_positive | 0.9771 | 0.9441 | 1.0000 | 175 |
| new | own | 17-30 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 175 |
| new | own | 17-30 | B_pm | negligible | 0.0229 | 0.0000 | 0.0559 | 175 |
| new | own | 17-30 | B_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 175 |
| new | own | 17-30 | C_pm | dominance_positive | 0.9771 | 0.9441 | 1.0000 | 175 |
| new | own | 17-30 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 175 |
| new | own | 17-30 | C_pm | negligible | 0.0229 | 0.0000 | 0.0559 | 175 |
| new | own | 17-30 | C_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 175 |

## T5_3_reversal_slot

| rule | portfolio | jstar | count | count_argmin_C_hat | count_precision_matched | n_reversals | n_reversals_pm |
|---|---|---|---|---|---|---|---|
| old | actual | 1 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 2 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 3 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 4 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 5 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 6 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 7 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 8 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 9 | 1 | 1 | 1 | 8 | 8 |
| old | actual | 10 | 1 | 1 | 1 | 8 | 8 |
| old | actual | 11 | 1 | 1 | 1 | 8 | 8 |
| old | actual | 12 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 13 | 1 | 1 | 1 | 8 | 8 |
| old | actual | 14 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 15 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 16 | 0 | 1 | 0 | 8 | 8 |
| old | actual | 17 | 2 | 1 | 1 | 8 | 8 |
| old | actual | 18 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 19 | 0 | 0 | 1 | 8 | 8 |
| old | actual | 20 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 21 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 22 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 23 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 24 | 1 | 1 | 1 | 8 | 8 |
| old | actual | 25 | 1 | 1 | 1 | 8 | 8 |
| old | actual | 26 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 27 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 28 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 29 | 0 | 0 | 0 | 8 | 8 |
| old | actual | 30 | 0 | 0 | 0 | 8 | 8 |
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
| new | actual | 1 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 2 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 3 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 4 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 5 | 2 | 2 | 0 | 45 | 41 |
| new | actual | 6 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 7 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 8 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 9 | 36 | 36 | 34 | 45 | 41 |
| new | actual | 10 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 11 | 1 | 1 | 1 | 45 | 41 |
| new | actual | 12 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 13 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 14 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 15 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 16 | 1 | 1 | 1 | 45 | 41 |
| new | actual | 17 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 18 | 1 | 1 | 1 | 45 | 41 |
| new | actual | 19 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 20 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 21 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 22 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 23 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 24 | 1 | 1 | 1 | 45 | 41 |
| new | actual | 25 | 1 | 1 | 1 | 45 | 41 |
| new | actual | 26 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 27 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 28 | 0 | 0 | 0 | 45 | 41 |
| new | actual | 29 | 2 | 2 | 2 | 45 | 41 |
| new | actual | 30 | 0 | 0 | 0 | 45 | 41 |
| new | own | 1 | 0 | 0 | 0 | 43 | 40 |
| new | own | 2 | 0 | 0 | 0 | 43 | 40 |
| new | own | 3 | 0 | 0 | 0 | 43 | 40 |
| new | own | 4 | 0 | 0 | 0 | 43 | 40 |
| new | own | 5 | 0 | 0 | 0 | 43 | 40 |
| new | own | 6 | 0 | 0 | 0 | 43 | 40 |
| new | own | 7 | 0 | 0 | 0 | 43 | 40 |
| new | own | 8 | 0 | 0 | 0 | 43 | 40 |
| new | own | 9 | 43 | 43 | 40 | 43 | 40 |
| new | own | 10 | 0 | 0 | 0 | 43 | 40 |
| new | own | 11 | 0 | 0 | 0 | 43 | 40 |
| new | own | 12 | 0 | 0 | 0 | 43 | 40 |
| new | own | 13 | 0 | 0 | 0 | 43 | 40 |
| new | own | 14 | 0 | 0 | 0 | 43 | 40 |
| new | own | 15 | 0 | 0 | 0 | 43 | 40 |
| new | own | 16 | 0 | 0 | 0 | 43 | 40 |
| new | own | 17 | 0 | 0 | 0 | 43 | 40 |
| new | own | 18 | 0 | 0 | 0 | 43 | 40 |
| new | own | 19 | 0 | 0 | 0 | 43 | 40 |
| new | own | 20 | 0 | 0 | 0 | 43 | 40 |
| new | own | 21 | 0 | 0 | 0 | 43 | 40 |
| new | own | 22 | 0 | 0 | 0 | 43 | 40 |
| new | own | 23 | 0 | 0 | 0 | 43 | 40 |
| new | own | 24 | 0 | 0 | 0 | 43 | 40 |
| new | own | 25 | 0 | 0 | 0 | 43 | 40 |
| new | own | 26 | 0 | 0 | 0 | 43 | 40 |
| new | own | 27 | 0 | 0 | 0 | 43 | 40 |
| new | own | 28 | 0 | 0 | 0 | 43 | 40 |
| new | own | 29 | 0 | 0 | 0 | 43 | 40 |
| new | own | 30 | 0 | 0 | 0 | 43 | 40 |

## F5_1_profiles

720 rows in `F5_1_profiles.csv`.

## T5_curves_and_T5_6_delta

| rule | portfolio | band | curve | n | mean | q25 | median | q75 | q90 | share_sig_pos | pos_lo99 | pos_hi99 | share_sig_neg | neg_lo99 | neg_hi99 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| old | actual | all | linear | 386 | 0.0166 | 0.0021 | 0.0088 | 0.0258 | 0.0409 | 0.6762 | 0.6376 | 0.7090 | 0.0181 | 0.0051 | 0.0327 |
| old | actual | all | concave | 386 | 0.0166 | 0.0015 | 0.0081 | 0.0300 | 0.0361 | 0.6218 | 0.5833 | 0.6548 | 0.0130 | 0.0024 | 0.0265 |
| old | actual | all | convex | 386 | 0.0129 | 0.0024 | 0.0068 | 0.0228 | 0.0311 | 0.7176 | 0.6750 | 0.7574 | 0.0130 | 0.0025 | 0.0259 |
| old | actual | all | top3_stress | 386 | 0.0039 | 0.0000 | 0.0015 | 0.0067 | 0.0126 | 0.3756 | 0.3239 | 0.4239 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 1-3 | linear | 41 | 0.0014 | 0.0015 | 0.0021 | 0.0027 | 0.0036 | 0.2683 | 0.1053 | 0.4222 | 0.0732 | 0.0000 | 0.1905 |
| old | actual | 1-3 | concave | 41 | 0.0003 | 0.0008 | 0.0012 | 0.0017 | 0.0019 | 0.0732 | 0.0000 | 0.1750 | 0.0732 | 0.0000 | 0.1905 |
| old | actual | 1-3 | convex | 41 | 0.0034 | 0.0027 | 0.0035 | 0.0045 | 0.0057 | 0.7073 | 0.5556 | 0.8500 | 0.0488 | 0.0000 | 0.1538 |
| old | actual | 1-3 | top3_stress | 41 | 0.0024 | 0.0003 | 0.0008 | 0.0036 | 0.0069 | 0.2927 | 0.1500 | 0.4130 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 4-10 | linear | 91 | 0.0112 | 0.0029 | 0.0052 | 0.0199 | 0.0258 | 0.7473 | 0.6567 | 0.8333 | 0.0110 | 0.0000 | 0.0500 |
| old | actual | 4-10 | concave | 91 | 0.0101 | 0.0016 | 0.0030 | 0.0148 | 0.0272 | 0.5604 | 0.4681 | 0.6508 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 4-10 | convex | 91 | 0.0127 | 0.0049 | 0.0087 | 0.0198 | 0.0297 | 0.8462 | 0.7586 | 0.9176 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 4-10 | top3_stress | 91 | 0.0100 | 0.0072 | 0.0095 | 0.0137 | 0.0177 | 0.8571 | 0.7927 | 0.9200 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 11-16 | linear | 79 | 0.0210 | 0.0053 | 0.0101 | 0.0316 | 0.0393 | 0.7595 | 0.6786 | 0.8361 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 11-16 | concave | 79 | 0.0194 | 0.0054 | 0.0092 | 0.0233 | 0.0326 | 0.7595 | 0.6786 | 0.8361 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 11-16 | convex | 79 | 0.0187 | 0.0050 | 0.0130 | 0.0279 | 0.0318 | 0.7595 | 0.6786 | 0.8361 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 11-16 | top3_stress | 79 | 0.0050 | 0.0015 | 0.0045 | 0.0066 | 0.0117 | 0.5696 | 0.4750 | 0.6620 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 17-30 | linear | 175 | 0.0209 | 0.0017 | 0.0212 | 0.0371 | 0.0450 | 0.6971 | 0.6400 | 0.7517 | 0.0171 | 0.0000 | 0.0429 |
| old | actual | 17-30 | concave | 175 | 0.0226 | 0.0024 | 0.0287 | 0.0340 | 0.0400 | 0.7200 | 0.6550 | 0.7840 | 0.0114 | 0.0000 | 0.0333 |
| old | actual | 17-30 | convex | 175 | 0.0127 | 0.0013 | 0.0068 | 0.0265 | 0.0330 | 0.6343 | 0.5604 | 0.7048 | 0.0171 | 0.0000 | 0.0429 |
| old | actual | 17-30 | top3_stress | 175 | 0.0007 | 0.0000 | 0.0000 | 0.0012 | 0.0025 | 0.0571 | 0.0199 | 0.1011 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | linear | 386 | 0.0219 | 0.0069 | 0.0191 | 0.0364 | 0.0433 | 0.8549 | 0.8161 | 0.8938 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | concave | 386 | 0.0196 | 0.0039 | 0.0223 | 0.0320 | 0.0369 | 0.7953 | 0.7527 | 0.8392 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | convex | 386 | 0.0181 | 0.0055 | 0.0181 | 0.0293 | 0.0353 | 0.8964 | 0.8629 | 0.9269 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | top3_stress | 386 | 0.0049 | 0.0002 | 0.0025 | 0.0074 | 0.0143 | 0.4637 | 0.4046 | 0.5246 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | linear | 41 | 0.0023 | 0.0018 | 0.0021 | 0.0027 | 0.0034 | 0.2195 | 0.0714 | 0.3659 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | concave | 41 | 0.0013 | 0.0010 | 0.0011 | 0.0014 | 0.0018 | 0.0244 | 0.0000 | 0.0952 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | convex | 41 | 0.0039 | 0.0030 | 0.0035 | 0.0045 | 0.0057 | 0.7561 | 0.5897 | 0.8974 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | top3_stress | 41 | 0.0025 | 0.0005 | 0.0009 | 0.0032 | 0.0069 | 0.2683 | 0.1212 | 0.4048 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | linear | 91 | 0.0092 | 0.0039 | 0.0070 | 0.0144 | 0.0173 | 0.8681 | 0.7895 | 0.9457 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | concave | 91 | 0.0053 | 0.0021 | 0.0039 | 0.0082 | 0.0100 | 0.6703 | 0.5955 | 0.7500 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | convex | 91 | 0.0140 | 0.0065 | 0.0110 | 0.0214 | 0.0261 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | top3_stress | 91 | 0.0128 | 0.0086 | 0.0113 | 0.0173 | 0.0202 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | linear | 79 | 0.0268 | 0.0174 | 0.0285 | 0.0352 | 0.0381 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | concave | 79 | 0.0195 | 0.0107 | 0.0204 | 0.0264 | 0.0303 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | convex | 79 | 0.0270 | 0.0228 | 0.0283 | 0.0316 | 0.0343 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | top3_stress | 79 | 0.0057 | 0.0026 | 0.0054 | 0.0064 | 0.0100 | 0.7342 | 0.6462 | 0.8133 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | linear | 175 | 0.0310 | 0.0199 | 0.0349 | 0.0421 | 0.0478 | 0.9314 | 0.8910 | 0.9679 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | concave | 175 | 0.0314 | 0.0288 | 0.0330 | 0.0365 | 0.0406 | 0.9486 | 0.9080 | 0.9829 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | convex | 175 | 0.0194 | 0.0049 | 0.0201 | 0.0316 | 0.0388 | 0.8286 | 0.7673 | 0.8889 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | top3_stress | 175 | 0.0010 | 0.0000 | 0.0001 | 0.0017 | 0.0030 | 0.1086 | 0.0511 | 0.1734 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | all | linear | 386 | 0.0171 | 0.0001 | 0.0079 | 0.0329 | 0.0464 | 0.5440 | 0.4915 | 0.5930 | 0.0130 | 0.0024 | 0.0265 |
| new | actual | all | concave | 386 | 0.0171 | 0.0001 | 0.0070 | 0.0312 | 0.0387 | 0.5907 | 0.5421 | 0.6359 | 0.0130 | 0.0024 | 0.0265 |
| new | actual | all | convex | 386 | 0.0134 | 0.0000 | 0.0030 | 0.0270 | 0.0421 | 0.5078 | 0.4465 | 0.5674 | 0.0415 | 0.0166 | 0.0693 |
| new | actual | all | top3_stress | 386 | 0.0039 | 0.0000 | 0.0001 | 0.0084 | 0.0165 | 0.3497 | 0.2857 | 0.4129 | 0.0881 | 0.0559 | 0.1159 |
| new | actual | 1-3 | linear | 41 | 0.0010 | 0.0001 | 0.0006 | 0.0016 | 0.0042 | 0.1707 | 0.0513 | 0.2800 | 0.0488 | 0.0000 | 0.1538 |
| new | actual | 1-3 | concave | 41 | 0.0021 | 0.0001 | 0.0014 | 0.0045 | 0.0059 | 0.3659 | 0.2000 | 0.5208 | 0.0488 | 0.0000 | 0.1538 |
| new | actual | 1-3 | convex | 41 | -0.0006 | -0.0016 | 0.0000 | 0.0003 | 0.0028 | 0.1220 | 0.0233 | 0.2368 | 0.1707 | 0.0500 | 0.3000 |
| new | actual | 1-3 | top3_stress | 41 | -0.0031 | -0.0047 | -0.0011 | 0.0000 | 0.0000 | 0.0488 | 0.0000 | 0.1489 | 0.4634 | 0.2941 | 0.6123 |
| new | actual | 4-10 | linear | 91 | 0.0011 | 0.0000 | 0.0002 | 0.0011 | 0.0055 | 0.1538 | 0.0779 | 0.2283 | 0.0220 | 0.0000 | 0.0676 |
| new | actual | 4-10 | concave | 91 | 0.0015 | 0.0000 | 0.0006 | 0.0024 | 0.0053 | 0.2308 | 0.1562 | 0.3111 | 0.0220 | 0.0000 | 0.0676 |
| new | actual | 4-10 | convex | 91 | 0.0006 | -0.0006 | 0.0000 | 0.0003 | 0.0066 | 0.1429 | 0.0658 | 0.2237 | 0.0879 | 0.0303 | 0.1474 |
| new | actual | 4-10 | top3_stress | 91 | -0.0004 | -0.0018 | 0.0000 | 0.0004 | 0.0050 | 0.1429 | 0.0729 | 0.2222 | 0.1648 | 0.0843 | 0.2500 |
| new | actual | 11-16 | linear | 79 | 0.0173 | 0.0013 | 0.0146 | 0.0303 | 0.0398 | 0.7089 | 0.5976 | 0.8148 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 11-16 | concave | 79 | 0.0144 | 0.0011 | 0.0115 | 0.0262 | 0.0331 | 0.7089 | 0.5976 | 0.8148 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 11-16 | convex | 79 | 0.0174 | 0.0011 | 0.0147 | 0.0317 | 0.0376 | 0.7089 | 0.5976 | 0.8148 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 11-16 | top3_stress | 79 | 0.0092 | 0.0009 | 0.0091 | 0.0126 | 0.0220 | 0.6962 | 0.5854 | 0.8060 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 17-30 | linear | 175 | 0.0291 | 0.0091 | 0.0243 | 0.0451 | 0.0595 | 0.7600 | 0.7115 | 0.8114 | 0.0057 | 0.0000 | 0.0244 |
| new | actual | 17-30 | concave | 175 | 0.0300 | 0.0098 | 0.0310 | 0.0374 | 0.0616 | 0.7771 | 0.7238 | 0.8315 | 0.0057 | 0.0000 | 0.0244 |
| new | actual | 17-30 | convex | 175 | 0.0214 | 0.0015 | 0.0105 | 0.0400 | 0.0523 | 0.6971 | 0.6418 | 0.7557 | 0.0057 | 0.0000 | 0.0244 |
| new | actual | 17-30 | top3_stress | 175 | 0.0053 | 0.0000 | 0.0005 | 0.0090 | 0.0194 | 0.3714 | 0.2970 | 0.4508 | 0.0000 | 0.0000 | 0.0000 |
| new | own | all | linear | 386 | 0.0228 | 0.0002 | 0.0175 | 0.0414 | 0.0568 | 0.6554 | 0.5933 | 0.7175 | 0.0181 | 0.0025 | 0.0383 |
| new | own | all | concave | 386 | 0.0200 | 0.0001 | 0.0233 | 0.0343 | 0.0435 | 0.6399 | 0.5778 | 0.7037 | 0.0000 | 0.0000 | 0.0000 |
| new | own | all | convex | 386 | 0.0194 | 0.0001 | 0.0077 | 0.0369 | 0.0563 | 0.6192 | 0.5516 | 0.6841 | 0.0492 | 0.0185 | 0.0792 |
| new | own | all | top3_stress | 386 | 0.0059 | 0.0000 | 0.0008 | 0.0114 | 0.0218 | 0.4430 | 0.3829 | 0.5029 | 0.0907 | 0.0583 | 0.1182 |
| new | own | 1-3 | linear | 41 | -0.0010 | -0.0014 | -0.0005 | 0.0001 | 0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.0488 | 0.0000 | 0.1364 |
| new | own | 1-3 | concave | 41 | -0.0005 | -0.0007 | -0.0003 | 0.0000 | 0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 1-3 | convex | 41 | -0.0019 | -0.0026 | -0.0010 | 0.0000 | 0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.2439 | 0.0968 | 0.3800 |
| new | own | 1-3 | top3_stress | 41 | -0.0035 | -0.0047 | -0.0019 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.4878 | 0.3125 | 0.6471 |
| new | own | 4-10 | linear | 91 | 0.0010 | -0.0005 | 0.0001 | 0.0015 | 0.0055 | 0.2088 | 0.0991 | 0.3288 | 0.0549 | 0.0102 | 0.1111 |
| new | own | 4-10 | concave | 91 | 0.0006 | -0.0003 | 0.0000 | 0.0009 | 0.0033 | 0.1319 | 0.0430 | 0.2442 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 4-10 | convex | 91 | 0.0013 | -0.0009 | 0.0001 | 0.0022 | 0.0081 | 0.2418 | 0.1359 | 0.3494 | 0.0989 | 0.0341 | 0.1739 |
| new | own | 4-10 | top3_stress | 91 | 0.0005 | -0.0018 | 0.0000 | 0.0022 | 0.0082 | 0.2418 | 0.1359 | 0.3494 | 0.1648 | 0.0843 | 0.2500 |
| new | own | 11-16 | linear | 79 | 0.0287 | 0.0129 | 0.0335 | 0.0417 | 0.0459 | 0.8987 | 0.8226 | 0.9647 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | concave | 79 | 0.0201 | 0.0081 | 0.0227 | 0.0304 | 0.0340 | 0.8734 | 0.7949 | 0.9474 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | convex | 79 | 0.0316 | 0.0170 | 0.0363 | 0.0431 | 0.0536 | 0.9114 | 0.8354 | 0.9756 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | top3_stress | 79 | 0.0133 | 0.0080 | 0.0117 | 0.0206 | 0.0259 | 0.8608 | 0.7683 | 0.9437 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | linear | 175 | 0.0370 | 0.0199 | 0.0380 | 0.0525 | 0.0664 | 0.9314 | 0.8910 | 0.9679 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | concave | 175 | 0.0349 | 0.0296 | 0.0345 | 0.0429 | 0.0488 | 0.9486 | 0.9080 | 0.9829 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | convex | 175 | 0.0284 | 0.0049 | 0.0235 | 0.0479 | 0.0663 | 0.8286 | 0.7673 | 0.8889 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | top3_stress | 175 | 0.0076 | 0.0000 | 0.0015 | 0.0133 | 0.0240 | 0.4629 | 0.3976 | 0.5275 | 0.0000 | 0.0000 | 0.0000 |
| delta | actual | all | linear | 386 | 0.0005 | -0.0022 | 0.0000 | 0.0048 | 0.0139 | 0.3161 | 0.2638 | 0.3696 | 0.2073 | 0.1552 | 0.2542 |
| delta | actual | all | concave | 386 | 0.0005 | -0.0007 | 0.0000 | 0.0031 | 0.0139 | 0.2953 | 0.2486 | 0.3434 | 0.1762 | 0.1351 | 0.2167 |
| delta | actual | all | convex | 386 | 0.0004 | -0.0052 | 0.0000 | 0.0069 | 0.0168 | 0.3187 | 0.2698 | 0.3690 | 0.3161 | 0.2592 | 0.3706 |
| delta | actual | all | top3_stress | 386 | -0.0001 | -0.0056 | 0.0000 | 0.0052 | 0.0125 | 0.2902 | 0.2302 | 0.3495 | 0.2824 | 0.2304 | 0.3294 |
| delta | actual | 1-3 | linear | 41 | -0.0005 | -0.0019 | -0.0014 | -0.0006 | 0.0020 | 0.0976 | 0.0000 | 0.2051 | 0.0488 | 0.0000 | 0.1364 |
| delta | actual | 1-3 | concave | 41 | 0.0019 | -0.0007 | 0.0009 | 0.0029 | 0.0039 | 0.2927 | 0.1282 | 0.4600 | 0.0000 | 0.0000 | 0.0000 |
| delta | actual | 1-3 | convex | 41 | -0.0040 | -0.0051 | -0.0030 | -0.0021 | -0.0016 | 0.0244 | 0.0000 | 0.1026 | 0.5854 | 0.4091 | 0.7675 |
| delta | actual | 1-3 | top3_stress | 41 | -0.0055 | -0.0079 | -0.0028 | -0.0003 | -0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.4146 | 0.2683 | 0.5476 |
| delta | actual | 4-10 | linear | 91 | -0.0101 | -0.0171 | -0.0051 | -0.0024 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.6264 | 0.5326 | 0.7229 |
| delta | actual | 4-10 | concave | 91 | -0.0085 | -0.0171 | -0.0028 | 0.0000 | 0.0002 | 0.0549 | 0.0102 | 0.1111 | 0.5275 | 0.4524 | 0.6111 |
| delta | actual | 4-10 | convex | 91 | -0.0120 | -0.0176 | -0.0100 | -0.0056 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.8571 | 0.7927 | 0.9200 |
| delta | actual | 4-10 | top3_stress | 91 | -0.0104 | -0.0134 | -0.0102 | -0.0072 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.8571 | 0.7927 | 0.9200 |
| delta | actual | 11-16 | linear | 79 | -0.0036 | -0.0021 | 0.0030 | 0.0072 | 0.0182 | 0.5443 | 0.4176 | 0.6806 | 0.2532 | 0.1333 | 0.3625 |
| delta | actual | 11-16 | concave | 79 | -0.0050 | -0.0015 | 0.0012 | 0.0072 | 0.0186 | 0.3797 | 0.2658 | 0.5082 | 0.2152 | 0.1127 | 0.3140 |
| delta | actual | 11-16 | convex | 79 | -0.0012 | -0.0021 | 0.0065 | 0.0089 | 0.0181 | 0.5570 | 0.4384 | 0.6857 | 0.2532 | 0.1333 | 0.3625 |
| delta | actual | 11-16 | top3_stress | 79 | 0.0042 | 0.0000 | 0.0066 | 0.0094 | 0.0166 | 0.6076 | 0.4831 | 0.7333 | 0.1772 | 0.0870 | 0.2593 |
| delta | actual | 17-30 | linear | 175 | 0.0081 | 0.0000 | 0.0001 | 0.0075 | 0.0258 | 0.4286 | 0.3529 | 0.5098 | 0.0057 | 0.0000 | 0.0261 |
| delta | actual | 17-30 | concave | 175 | 0.0074 | 0.0000 | 0.0001 | 0.0052 | 0.0220 | 0.3829 | 0.3148 | 0.4571 | 0.0171 | 0.0000 | 0.0441 |
| delta | actual | 17-30 | convex | 175 | 0.0087 | 0.0000 | 0.0005 | 0.0104 | 0.0302 | 0.4457 | 0.3722 | 0.5253 | 0.0000 | 0.0000 | 0.0000 |
| delta | actual | 17-30 | top3_stress | 175 | 0.0046 | 0.0000 | 0.0004 | 0.0079 | 0.0174 | 0.3657 | 0.2830 | 0.4481 | 0.0000 | 0.0000 | 0.0000 |
| delta | own | all | linear | 386 | 0.0008 | -0.0052 | 0.0000 | 0.0048 | 0.0151 | 0.3368 | 0.2840 | 0.3901 | 0.3446 | 0.2861 | 0.4000 |
| delta | own | all | concave | 386 | 0.0004 | -0.0029 | 0.0000 | 0.0024 | 0.0088 | 0.2539 | 0.2028 | 0.3086 | 0.2539 | 0.1989 | 0.3060 |
| delta | own | all | convex | 386 | 0.0014 | -0.0076 | 0.0000 | 0.0083 | 0.0221 | 0.3472 | 0.2974 | 0.3995 | 0.3808 | 0.3208 | 0.4369 |
| delta | own | all | top3_stress | 386 | 0.0010 | -0.0081 | 0.0000 | 0.0080 | 0.0181 | 0.3627 | 0.3088 | 0.4162 | 0.3264 | 0.2642 | 0.3828 |
| delta | own | 1-3 | linear | 41 | -0.0033 | -0.0040 | -0.0028 | -0.0018 | -0.0014 | 0.0000 | 0.0000 | 0.0000 | 0.4634 | 0.2963 | 0.6098 |
| delta | own | 1-3 | concave | 41 | -0.0017 | -0.0022 | -0.0015 | -0.0009 | -0.0007 | 0.0000 | 0.0000 | 0.0000 | 0.1951 | 0.0690 | 0.3182 |
| delta | own | 1-3 | convex | 41 | -0.0058 | -0.0070 | -0.0048 | -0.0030 | -0.0024 | 0.0000 | 0.0000 | 0.0000 | 0.7805 | 0.6389 | 0.9167 |
| delta | own | 1-3 | top3_stress | 41 | -0.0060 | -0.0079 | -0.0029 | -0.0005 | -0.0003 | 0.0000 | 0.0000 | 0.0000 | 0.5122 | 0.3333 | 0.6667 |
| delta | own | 4-10 | linear | 91 | -0.0082 | -0.0112 | -0.0071 | -0.0052 | -0.0034 | 0.0000 | 0.0000 | 0.0000 | 0.9780 | 0.9342 | 1.0000 |
| delta | own | 4-10 | concave | 91 | -0.0046 | -0.0064 | -0.0039 | -0.0028 | -0.0019 | 0.0000 | 0.0000 | 0.0000 | 0.7473 | 0.6629 | 0.8356 |
| delta | own | 4-10 | convex | 91 | -0.0127 | -0.0172 | -0.0118 | -0.0079 | -0.0058 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 |
| delta | own | 4-10 | top3_stress | 91 | -0.0124 | -0.0147 | -0.0112 | -0.0091 | -0.0072 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 |
| delta | own | 11-16 | linear | 79 | 0.0019 | -0.0052 | 0.0033 | 0.0060 | 0.0119 | 0.6329 | 0.5050 | 0.7714 | 0.3165 | 0.1918 | 0.4231 |
| delta | own | 11-16 | concave | 79 | 0.0006 | -0.0032 | 0.0015 | 0.0033 | 0.0066 | 0.4177 | 0.2667 | 0.5694 | 0.2785 | 0.1688 | 0.3827 |
| delta | own | 11-16 | convex | 79 | 0.0045 | -0.0050 | 0.0070 | 0.0112 | 0.0188 | 0.6582 | 0.5584 | 0.7792 | 0.3038 | 0.1746 | 0.4186 |
| delta | own | 11-16 | top3_stress | 79 | 0.0076 | 0.0034 | 0.0077 | 0.0154 | 0.0199 | 0.7722 | 0.6628 | 0.8816 | 0.1772 | 0.0870 | 0.2593 |
| delta | own | 17-30 | linear | 175 | 0.0060 | 0.0000 | 0.0006 | 0.0109 | 0.0194 | 0.4571 | 0.3958 | 0.5235 | 0.0000 | 0.0000 | 0.0000 |
| delta | own | 17-30 | concave | 175 | 0.0035 | 0.0000 | 0.0004 | 0.0061 | 0.0110 | 0.3714 | 0.2934 | 0.4463 | 0.0000 | 0.0000 | 0.0000 |
| delta | own | 17-30 | convex | 175 | 0.0089 | 0.0000 | 0.0014 | 0.0165 | 0.0289 | 0.4686 | 0.4061 | 0.5361 | 0.0000 | 0.0000 | 0.0000 |
| delta | own | 17-30 | top3_stress | 175 | 0.0066 | 0.0000 | 0.0014 | 0.0112 | 0.0206 | 0.4514 | 0.3867 | 0.5185 | 0.0000 | 0.0000 | 0.0000 |

## H1

| n_team_games | share_neg_new | share_neg_old | diff_new_minus_old | diff_lo99 | diff_hi99 | n_new_reversals | crossing_share | crossing_lo99 | crossing_hi99 | supported |
|---|---|---|---|---|---|---|---|---|---|---|
| 57 | 0.1228 | 0.0000 | 0.1228 | 0.0167 | 0.2500 | 42 | 1.0000 | 1.0000 | 1.0000 | True |

## T5_attr_portfolio_effect

| rule | band | n | mean | q25 | median | q75 | q90 | share_nonzero |
|---|---|---|---|---|---|---|---|---|
| old | all | 386 | -0.0054 | -0.0132 | 0.0000 | 0.0000 | 0.0027 | 0.4430 |
| old | 1-3 | 41 | -0.0009 | -0.0000 | 0.0000 | 0.0000 | 0.0001 | 0.1220 |
| old | 4-10 | 91 | 0.0021 | -0.0000 | 0.0000 | 0.0028 | 0.0187 | 0.3956 |
| old | 11-16 | 79 | -0.0059 | -0.0282 | 0.0000 | 0.0000 | 0.0008 | 0.5570 |
| old | 17-30 | 175 | -0.0100 | -0.0175 | -0.0009 | 0.0000 | 0.0000 | 0.4914 |
| new | all | 386 | -0.0057 | -0.0087 | 0.0000 | 0.0001 | 0.0036 | 0.4482 |
| new | 1-3 | 41 | 0.0019 | 0.0000 | 0.0014 | 0.0042 | 0.0055 | 0.4146 |
| new | 4-10 | 91 | 0.0001 | -0.0002 | 0.0001 | 0.0016 | 0.0039 | 0.2527 |
| new | 11-16 | 79 | -0.0113 | -0.0230 | 0.0000 | 0.0000 | 0.0008 | 0.4684 |
| new | 17-30 | 175 | -0.0079 | -0.0156 | -0.0024 | 0.0000 | 0.0000 | 0.5486 |
| delta | all | 386 | -0.0003 | -0.0003 | 0.0000 | 0.0022 | 0.0103 | 0.4093 |
| delta | 1-3 | 41 | 0.0028 | 0.0000 | 0.0017 | 0.0041 | 0.0056 | 0.3902 |
| delta | 4-10 | 91 | -0.0020 | -0.0039 | 0.0002 | 0.0021 | 0.0082 | 0.5165 |
| delta | 11-16 | 79 | -0.0055 | -0.0032 | 0.0000 | 0.0039 | 0.0127 | 0.5443 |
| delta | 17-30 | 175 | 0.0021 | -0.0003 | 0.0000 | 0.0001 | 0.0075 | 0.2971 |

## T5_7_rollover

| rule | portfolio | band | curve | rho | measure | n | mean | q25 | median | q75 | q90 | share_sign_flip | vbar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| old | actual | all | - | 0.0000 | M | 386 | 0.0074 | -0.0000 | 0.0000 | 0.0001 | 0.0233 |  |  |
| old | actual | all | linear | 0.0000 | tau | 386 | 0.0166 | 0.0021 | 0.0088 | 0.0258 | 0.0409 | 0.0000 | 0.5000 |
| old | actual | all | linear | 0.5000 | tau | 386 | 0.0148 | 0.0019 | 0.0071 | 0.0244 | 0.0388 | 0.0026 | 0.5000 |
| old | actual | all | linear | 0.8000 | tau | 386 | 0.0136 | 0.0016 | 0.0071 | 0.0224 | 0.0380 | 0.0026 | 0.5000 |
| old | actual | all | concave | 0.0000 | tau | 386 | 0.0166 | 0.0015 | 0.0081 | 0.0300 | 0.0361 | 0.0000 | 0.6599 |
| old | actual | all | concave | 0.5000 | tau | 386 | 0.0142 | 0.0013 | 0.0061 | 0.0291 | 0.0349 | 0.0130 | 0.6599 |
| old | actual | all | concave | 0.8000 | tau | 386 | 0.0128 | 0.0012 | 0.0055 | 0.0274 | 0.0343 | 0.0155 | 0.6599 |
| old | actual | all | convex | 0.0000 | tau | 386 | 0.0129 | 0.0024 | 0.0068 | 0.0228 | 0.0311 | 0.0000 | 0.3391 |
| old | actual | all | convex | 0.5000 | tau | 386 | 0.0117 | 0.0023 | 0.0064 | 0.0195 | 0.0304 | 0.0026 | 0.3391 |
| old | actual | all | convex | 0.8000 | tau | 386 | 0.0109 | 0.0023 | 0.0058 | 0.0190 | 0.0303 | 0.0078 | 0.3391 |
| old | actual | all | top3_stress | 0.0000 | tau | 386 | 0.0039 | 0.0000 | 0.0015 | 0.0067 | 0.0126 | 0.0000 | 0.1000 |
| old | actual | all | top3_stress | 0.5000 | tau | 386 | 0.0036 | 0.0000 | 0.0011 | 0.0063 | 0.0110 | 0.0803 | 0.1000 |
| old | actual | all | top3_stress | 0.8000 | tau | 386 | 0.0034 | 0.0000 | 0.0011 | 0.0061 | 0.0105 | 0.0803 | 0.1000 |
| old | actual | 1-3 | - | 0.0000 | M | 41 | -0.0006 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | actual | 1-3 | linear | 0.0000 | tau | 41 | 0.0014 | 0.0015 | 0.0021 | 0.0027 | 0.0036 | 0.0000 | 0.5000 |
| old | actual | 1-3 | linear | 0.5000 | tau | 41 | 0.0016 | 0.0016 | 0.0021 | 0.0027 | 0.0036 | 0.0000 | 0.5000 |
| old | actual | 1-3 | linear | 0.8000 | tau | 41 | 0.0017 | 0.0016 | 0.0021 | 0.0027 | 0.0036 | 0.0000 | 0.5000 |
| old | actual | 1-3 | concave | 0.0000 | tau | 41 | 0.0003 | 0.0008 | 0.0012 | 0.0017 | 0.0019 | 0.0000 | 0.6599 |
| old | actual | 1-3 | concave | 0.5000 | tau | 41 | 0.0005 | 0.0008 | 0.0012 | 0.0017 | 0.0019 | 0.0244 | 0.6599 |
| old | actual | 1-3 | concave | 0.8000 | tau | 41 | 0.0006 | 0.0009 | 0.0012 | 0.0017 | 0.0020 | 0.0244 | 0.6599 |
| old | actual | 1-3 | convex | 0.0000 | tau | 41 | 0.0034 | 0.0027 | 0.0035 | 0.0045 | 0.0057 | 0.0000 | 0.3391 |
| old | actual | 1-3 | convex | 0.5000 | tau | 41 | 0.0035 | 0.0027 | 0.0035 | 0.0045 | 0.0057 | 0.0000 | 0.3391 |
| old | actual | 1-3 | convex | 0.8000 | tau | 41 | 0.0036 | 0.0027 | 0.0035 | 0.0045 | 0.0057 | 0.0244 | 0.3391 |
| old | actual | 1-3 | top3_stress | 0.0000 | tau | 41 | 0.0024 | 0.0003 | 0.0008 | 0.0036 | 0.0069 | 0.0000 | 0.1000 |
| old | actual | 1-3 | top3_stress | 0.5000 | tau | 41 | 0.0025 | 0.0003 | 0.0008 | 0.0036 | 0.0074 | 0.0000 | 0.1000 |
| old | actual | 1-3 | top3_stress | 0.8000 | tau | 41 | 0.0025 | 0.0003 | 0.0008 | 0.0036 | 0.0074 | 0.0000 | 0.1000 |
| old | actual | 4-10 | - | 0.0000 | M | 91 | 0.0083 | -0.0000 | 0.0000 | 0.0176 | 0.0290 |  |  |
| old | actual | 4-10 | linear | 0.0000 | tau | 91 | 0.0112 | 0.0029 | 0.0052 | 0.0199 | 0.0258 | 0.0000 | 0.5000 |
| old | actual | 4-10 | linear | 0.5000 | tau | 91 | 0.0092 | 0.0029 | 0.0055 | 0.0146 | 0.0213 | 0.0000 | 0.5000 |
| old | actual | 4-10 | linear | 0.8000 | tau | 91 | 0.0079 | 0.0029 | 0.0055 | 0.0134 | 0.0194 | 0.0000 | 0.5000 |
| old | actual | 4-10 | concave | 0.0000 | tau | 91 | 0.0101 | 0.0016 | 0.0030 | 0.0148 | 0.0272 | 0.0000 | 0.6599 |
| old | actual | 4-10 | concave | 0.5000 | tau | 91 | 0.0073 | 0.0016 | 0.0030 | 0.0130 | 0.0177 | 0.0110 | 0.6599 |
| old | actual | 4-10 | concave | 0.8000 | tau | 91 | 0.0057 | 0.0016 | 0.0030 | 0.0093 | 0.0129 | 0.0110 | 0.6599 |
| old | actual | 4-10 | convex | 0.0000 | tau | 91 | 0.0127 | 0.0049 | 0.0087 | 0.0198 | 0.0297 | 0.0000 | 0.3391 |
| old | actual | 4-10 | convex | 0.5000 | tau | 91 | 0.0112 | 0.0049 | 0.0087 | 0.0165 | 0.0254 | 0.0110 | 0.3391 |
| old | actual | 4-10 | convex | 0.8000 | tau | 91 | 0.0104 | 0.0049 | 0.0087 | 0.0148 | 0.0222 | 0.0110 | 0.3391 |
| old | actual | 4-10 | top3_stress | 0.0000 | tau | 91 | 0.0100 | 0.0072 | 0.0095 | 0.0137 | 0.0177 | 0.0000 | 0.1000 |
| old | actual | 4-10 | top3_stress | 0.5000 | tau | 91 | 0.0096 | 0.0072 | 0.0091 | 0.0129 | 0.0174 | 0.0000 | 0.1000 |
| old | actual | 4-10 | top3_stress | 0.8000 | tau | 91 | 0.0093 | 0.0071 | 0.0090 | 0.0123 | 0.0164 | 0.0000 | 0.1000 |
| old | actual | 11-16 | - | 0.0000 | M | 79 | 0.0129 | -0.0000 | 0.0000 | 0.0078 | 0.0111 |  |  |
| old | actual | 11-16 | linear | 0.0000 | tau | 79 | 0.0210 | 0.0053 | 0.0101 | 0.0316 | 0.0393 | 0.0000 | 0.5000 |
| old | actual | 11-16 | linear | 0.5000 | tau | 79 | 0.0177 | 0.0039 | 0.0098 | 0.0316 | 0.0393 | 0.0000 | 0.5000 |
| old | actual | 11-16 | linear | 0.8000 | tau | 79 | 0.0158 | 0.0031 | 0.0091 | 0.0316 | 0.0382 | 0.0000 | 0.5000 |
| old | actual | 11-16 | concave | 0.0000 | tau | 79 | 0.0194 | 0.0054 | 0.0092 | 0.0233 | 0.0326 | 0.0000 | 0.6599 |
| old | actual | 11-16 | concave | 0.5000 | tau | 79 | 0.0152 | 0.0036 | 0.0062 | 0.0233 | 0.0326 | 0.0000 | 0.6599 |
| old | actual | 11-16 | concave | 0.8000 | tau | 79 | 0.0126 | 0.0025 | 0.0061 | 0.0233 | 0.0326 | 0.0000 | 0.6599 |
| old | actual | 11-16 | convex | 0.0000 | tau | 79 | 0.0187 | 0.0050 | 0.0130 | 0.0279 | 0.0318 | 0.0000 | 0.3391 |
| old | actual | 11-16 | convex | 0.5000 | tau | 79 | 0.0165 | 0.0041 | 0.0123 | 0.0279 | 0.0318 | 0.0000 | 0.3391 |
| old | actual | 11-16 | convex | 0.8000 | tau | 79 | 0.0152 | 0.0035 | 0.0123 | 0.0279 | 0.0318 | 0.0000 | 0.3391 |
| old | actual | 11-16 | top3_stress | 0.0000 | tau | 79 | 0.0050 | 0.0015 | 0.0045 | 0.0066 | 0.0117 | 0.0000 | 0.1000 |
| old | actual | 11-16 | top3_stress | 0.5000 | tau | 79 | 0.0044 | 0.0015 | 0.0042 | 0.0063 | 0.0096 | 0.0000 | 0.1000 |
| old | actual | 11-16 | top3_stress | 0.8000 | tau | 79 | 0.0040 | 0.0015 | 0.0040 | 0.0060 | 0.0077 | 0.0000 | 0.1000 |
| old | actual | 17-30 | - | 0.0000 | M | 175 | 0.0063 | -0.0000 | 0.0000 | 0.0000 | 0.0051 |  |  |
| old | actual | 17-30 | linear | 0.0000 | tau | 175 | 0.0209 | 0.0017 | 0.0212 | 0.0371 | 0.0450 | 0.0000 | 0.5000 |
| old | actual | 17-30 | linear | 0.5000 | tau | 175 | 0.0194 | 0.0013 | 0.0197 | 0.0352 | 0.0426 | 0.0057 | 0.5000 |
| old | actual | 17-30 | linear | 0.8000 | tau | 175 | 0.0184 | 0.0011 | 0.0175 | 0.0346 | 0.0422 | 0.0057 | 0.5000 |
| old | actual | 17-30 | concave | 0.0000 | tau | 175 | 0.0226 | 0.0024 | 0.0287 | 0.0340 | 0.0400 | 0.0000 | 0.6599 |
| old | actual | 17-30 | concave | 0.5000 | tau | 175 | 0.0206 | 0.0017 | 0.0274 | 0.0333 | 0.0366 | 0.0171 | 0.6599 |
| old | actual | 17-30 | concave | 0.8000 | tau | 175 | 0.0193 | 0.0013 | 0.0237 | 0.0315 | 0.0361 | 0.0229 | 0.6599 |
| old | actual | 17-30 | convex | 0.0000 | tau | 175 | 0.0127 | 0.0013 | 0.0068 | 0.0265 | 0.0330 | 0.0000 | 0.3391 |
| old | actual | 17-30 | convex | 0.5000 | tau | 175 | 0.0116 | 0.0012 | 0.0060 | 0.0227 | 0.0316 | 0.0000 | 0.3391 |
| old | actual | 17-30 | convex | 0.8000 | tau | 175 | 0.0110 | 0.0011 | 0.0049 | 0.0226 | 0.0316 | 0.0057 | 0.3391 |
| old | actual | 17-30 | top3_stress | 0.0000 | tau | 175 | 0.0007 | 0.0000 | 0.0000 | 0.0012 | 0.0025 | 0.0000 | 0.1000 |
| old | actual | 17-30 | top3_stress | 0.5000 | tau | 175 | 0.0004 | 0.0000 | 0.0000 | 0.0005 | 0.0017 | 0.1771 | 0.1000 |
| old | actual | 17-30 | top3_stress | 0.8000 | tau | 175 | 0.0002 | 0.0000 | 0.0000 | 0.0005 | 0.0018 | 0.1771 | 0.1000 |
| old | own | all | - | 0.0000 | M | 386 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | all | linear | 0.0000 | tau | 386 | 0.0219 | 0.0069 | 0.0191 | 0.0364 | 0.0433 | 0.0000 | 0.5000 |
| old | own | all | linear | 0.5000 | tau | 386 | 0.0219 | 0.0069 | 0.0191 | 0.0364 | 0.0433 | 0.0000 | 0.5000 |
| old | own | all | linear | 0.8000 | tau | 386 | 0.0219 | 0.0069 | 0.0191 | 0.0364 | 0.0433 | 0.0000 | 0.5000 |
| old | own | all | concave | 0.0000 | tau | 386 | 0.0196 | 0.0039 | 0.0223 | 0.0320 | 0.0369 | 0.0000 | 0.6599 |
| old | own | all | concave | 0.5000 | tau | 386 | 0.0196 | 0.0039 | 0.0223 | 0.0320 | 0.0369 | 0.0000 | 0.6599 |
| old | own | all | concave | 0.8000 | tau | 386 | 0.0196 | 0.0039 | 0.0223 | 0.0320 | 0.0369 | 0.0000 | 0.6599 |
| old | own | all | convex | 0.0000 | tau | 386 | 0.0181 | 0.0055 | 0.0181 | 0.0293 | 0.0353 | 0.0000 | 0.3391 |
| old | own | all | convex | 0.5000 | tau | 386 | 0.0181 | 0.0055 | 0.0181 | 0.0293 | 0.0353 | 0.0000 | 0.3391 |
| old | own | all | convex | 0.8000 | tau | 386 | 0.0181 | 0.0055 | 0.0181 | 0.0293 | 0.0353 | 0.0000 | 0.3391 |
| old | own | all | top3_stress | 0.0000 | tau | 386 | 0.0049 | 0.0002 | 0.0025 | 0.0074 | 0.0143 | 0.0000 | 0.1000 |
| old | own | all | top3_stress | 0.5000 | tau | 386 | 0.0049 | 0.0002 | 0.0025 | 0.0074 | 0.0143 | 0.0440 | 0.1000 |
| old | own | all | top3_stress | 0.8000 | tau | 386 | 0.0049 | 0.0002 | 0.0025 | 0.0074 | 0.0143 | 0.0440 | 0.1000 |
| old | own | 1-3 | - | 0.0000 | M | 41 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 1-3 | linear | 0.0000 | tau | 41 | 0.0023 | 0.0018 | 0.0021 | 0.0027 | 0.0034 | 0.0000 | 0.5000 |
| old | own | 1-3 | linear | 0.5000 | tau | 41 | 0.0023 | 0.0018 | 0.0021 | 0.0027 | 0.0034 | 0.0000 | 0.5000 |
| old | own | 1-3 | linear | 0.8000 | tau | 41 | 0.0023 | 0.0018 | 0.0021 | 0.0027 | 0.0034 | 0.0000 | 0.5000 |
| old | own | 1-3 | concave | 0.0000 | tau | 41 | 0.0013 | 0.0010 | 0.0011 | 0.0014 | 0.0018 | 0.0000 | 0.6599 |
| old | own | 1-3 | concave | 0.5000 | tau | 41 | 0.0013 | 0.0010 | 0.0011 | 0.0014 | 0.0018 | 0.0000 | 0.6599 |
| old | own | 1-3 | concave | 0.8000 | tau | 41 | 0.0013 | 0.0010 | 0.0011 | 0.0014 | 0.0018 | 0.0000 | 0.6599 |
| old | own | 1-3 | convex | 0.0000 | tau | 41 | 0.0039 | 0.0030 | 0.0035 | 0.0045 | 0.0057 | 0.0000 | 0.3391 |
| old | own | 1-3 | convex | 0.5000 | tau | 41 | 0.0039 | 0.0030 | 0.0035 | 0.0045 | 0.0057 | 0.0000 | 0.3391 |
| old | own | 1-3 | convex | 0.8000 | tau | 41 | 0.0039 | 0.0030 | 0.0035 | 0.0045 | 0.0057 | 0.0000 | 0.3391 |
| old | own | 1-3 | top3_stress | 0.0000 | tau | 41 | 0.0025 | 0.0005 | 0.0009 | 0.0032 | 0.0069 | 0.0000 | 0.1000 |
| old | own | 1-3 | top3_stress | 0.5000 | tau | 41 | 0.0025 | 0.0005 | 0.0009 | 0.0032 | 0.0069 | 0.0000 | 0.1000 |
| old | own | 1-3 | top3_stress | 0.8000 | tau | 41 | 0.0025 | 0.0005 | 0.0009 | 0.0032 | 0.0069 | 0.0000 | 0.1000 |
| old | own | 4-10 | - | 0.0000 | M | 91 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 4-10 | linear | 0.0000 | tau | 91 | 0.0092 | 0.0039 | 0.0070 | 0.0144 | 0.0173 | 0.0000 | 0.5000 |
| old | own | 4-10 | linear | 0.5000 | tau | 91 | 0.0092 | 0.0039 | 0.0070 | 0.0144 | 0.0173 | 0.0000 | 0.5000 |
| old | own | 4-10 | linear | 0.8000 | tau | 91 | 0.0092 | 0.0039 | 0.0070 | 0.0144 | 0.0173 | 0.0000 | 0.5000 |
| old | own | 4-10 | concave | 0.0000 | tau | 91 | 0.0053 | 0.0021 | 0.0039 | 0.0082 | 0.0100 | 0.0000 | 0.6599 |
| old | own | 4-10 | concave | 0.5000 | tau | 91 | 0.0053 | 0.0021 | 0.0039 | 0.0082 | 0.0100 | 0.0000 | 0.6599 |
| old | own | 4-10 | concave | 0.8000 | tau | 91 | 0.0053 | 0.0021 | 0.0039 | 0.0082 | 0.0100 | 0.0000 | 0.6599 |
| old | own | 4-10 | convex | 0.0000 | tau | 91 | 0.0140 | 0.0065 | 0.0110 | 0.0214 | 0.0261 | 0.0000 | 0.3391 |
| old | own | 4-10 | convex | 0.5000 | tau | 91 | 0.0140 | 0.0065 | 0.0110 | 0.0214 | 0.0261 | 0.0000 | 0.3391 |
| old | own | 4-10 | convex | 0.8000 | tau | 91 | 0.0140 | 0.0065 | 0.0110 | 0.0214 | 0.0261 | 0.0000 | 0.3391 |
| old | own | 4-10 | top3_stress | 0.0000 | tau | 91 | 0.0128 | 0.0086 | 0.0113 | 0.0173 | 0.0202 | 0.0000 | 0.1000 |
| old | own | 4-10 | top3_stress | 0.5000 | tau | 91 | 0.0128 | 0.0086 | 0.0113 | 0.0173 | 0.0202 | 0.0000 | 0.1000 |
| old | own | 4-10 | top3_stress | 0.8000 | tau | 91 | 0.0128 | 0.0086 | 0.0113 | 0.0173 | 0.0202 | 0.0000 | 0.1000 |
| old | own | 11-16 | - | 0.0000 | M | 79 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 11-16 | linear | 0.0000 | tau | 79 | 0.0268 | 0.0174 | 0.0285 | 0.0352 | 0.0381 | 0.0000 | 0.5000 |
| old | own | 11-16 | linear | 0.5000 | tau | 79 | 0.0268 | 0.0174 | 0.0285 | 0.0352 | 0.0381 | 0.0000 | 0.5000 |
| old | own | 11-16 | linear | 0.8000 | tau | 79 | 0.0268 | 0.0174 | 0.0285 | 0.0352 | 0.0381 | 0.0000 | 0.5000 |
| old | own | 11-16 | concave | 0.0000 | tau | 79 | 0.0195 | 0.0107 | 0.0204 | 0.0264 | 0.0303 | 0.0000 | 0.6599 |
| old | own | 11-16 | concave | 0.5000 | tau | 79 | 0.0195 | 0.0107 | 0.0204 | 0.0264 | 0.0303 | 0.0000 | 0.6599 |
| old | own | 11-16 | concave | 0.8000 | tau | 79 | 0.0195 | 0.0107 | 0.0204 | 0.0264 | 0.0303 | 0.0000 | 0.6599 |
| old | own | 11-16 | convex | 0.0000 | tau | 79 | 0.0270 | 0.0228 | 0.0283 | 0.0316 | 0.0343 | 0.0000 | 0.3391 |
| old | own | 11-16 | convex | 0.5000 | tau | 79 | 0.0270 | 0.0228 | 0.0283 | 0.0316 | 0.0343 | 0.0000 | 0.3391 |
| old | own | 11-16 | convex | 0.8000 | tau | 79 | 0.0270 | 0.0228 | 0.0283 | 0.0316 | 0.0343 | 0.0000 | 0.3391 |
| old | own | 11-16 | top3_stress | 0.0000 | tau | 79 | 0.0057 | 0.0026 | 0.0054 | 0.0064 | 0.0100 | 0.0000 | 0.1000 |
| old | own | 11-16 | top3_stress | 0.5000 | tau | 79 | 0.0057 | 0.0026 | 0.0054 | 0.0064 | 0.0100 | 0.0000 | 0.1000 |
| old | own | 11-16 | top3_stress | 0.8000 | tau | 79 | 0.0057 | 0.0026 | 0.0054 | 0.0064 | 0.0100 | 0.0000 | 0.1000 |
| old | own | 17-30 | - | 0.0000 | M | 175 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 17-30 | linear | 0.0000 | tau | 175 | 0.0310 | 0.0199 | 0.0349 | 0.0421 | 0.0478 | 0.0000 | 0.5000 |
| old | own | 17-30 | linear | 0.5000 | tau | 175 | 0.0310 | 0.0199 | 0.0349 | 0.0421 | 0.0478 | 0.0000 | 0.5000 |
| old | own | 17-30 | linear | 0.8000 | tau | 175 | 0.0310 | 0.0199 | 0.0349 | 0.0421 | 0.0478 | 0.0000 | 0.5000 |
| old | own | 17-30 | concave | 0.0000 | tau | 175 | 0.0314 | 0.0288 | 0.0330 | 0.0365 | 0.0406 | 0.0000 | 0.6599 |
| old | own | 17-30 | concave | 0.5000 | tau | 175 | 0.0314 | 0.0288 | 0.0330 | 0.0365 | 0.0406 | 0.0000 | 0.6599 |
| old | own | 17-30 | concave | 0.8000 | tau | 175 | 0.0314 | 0.0288 | 0.0330 | 0.0365 | 0.0406 | 0.0000 | 0.6599 |
| old | own | 17-30 | convex | 0.0000 | tau | 175 | 0.0194 | 0.0049 | 0.0201 | 0.0316 | 0.0388 | 0.0000 | 0.3391 |
| old | own | 17-30 | convex | 0.5000 | tau | 175 | 0.0194 | 0.0049 | 0.0201 | 0.0316 | 0.0388 | 0.0000 | 0.3391 |
| old | own | 17-30 | convex | 0.8000 | tau | 175 | 0.0194 | 0.0049 | 0.0201 | 0.0316 | 0.0388 | 0.0000 | 0.3391 |
| old | own | 17-30 | top3_stress | 0.0000 | tau | 175 | 0.0010 | 0.0000 | 0.0001 | 0.0017 | 0.0030 | 0.0000 | 0.1000 |
| old | own | 17-30 | top3_stress | 0.5000 | tau | 175 | 0.0010 | 0.0000 | 0.0001 | 0.0017 | 0.0030 | 0.0971 | 0.1000 |
| old | own | 17-30 | top3_stress | 0.8000 | tau | 175 | 0.0010 | 0.0000 | 0.0001 | 0.0017 | 0.0030 | 0.0971 | 0.1000 |
| new | actual | all | - | 0.0000 | M | 386 | 0.0079 | 0.0000 | 0.0000 | 0.0027 | 0.0170 |  |  |
| new | actual | all | linear | 0.0000 | tau | 386 | 0.0171 | 0.0001 | 0.0079 | 0.0329 | 0.0464 | 0.0000 | 0.5000 |
| new | actual | all | linear | 0.5000 | tau | 386 | 0.0151 | 0.0000 | 0.0061 | 0.0287 | 0.0441 | 0.0984 | 0.5000 |
| new | actual | all | linear | 0.8000 | tau | 386 | 0.0139 | 0.0000 | 0.0050 | 0.0262 | 0.0424 | 0.1062 | 0.5000 |
| new | actual | all | concave | 0.0000 | tau | 386 | 0.0171 | 0.0001 | 0.0070 | 0.0312 | 0.0387 | 0.0000 | 0.6599 |
| new | actual | all | concave | 0.5000 | tau | 386 | 0.0145 | 0.0001 | 0.0055 | 0.0310 | 0.0374 | 0.0026 | 0.6599 |
| new | actual | all | concave | 0.8000 | tau | 386 | 0.0130 | 0.0000 | 0.0041 | 0.0296 | 0.0357 | 0.0259 | 0.6599 |
| new | actual | all | convex | 0.0000 | tau | 386 | 0.0134 | 0.0000 | 0.0030 | 0.0270 | 0.0421 | 0.0000 | 0.3391 |
| new | actual | all | convex | 0.5000 | tau | 386 | 0.0120 | 0.0000 | 0.0028 | 0.0238 | 0.0399 | 0.0130 | 0.3391 |
| new | actual | all | convex | 0.8000 | tau | 386 | 0.0112 | 0.0000 | 0.0028 | 0.0223 | 0.0379 | 0.0207 | 0.3391 |
| new | actual | all | top3_stress | 0.0000 | tau | 386 | 0.0039 | 0.0000 | 0.0001 | 0.0084 | 0.0165 | 0.0000 | 0.1000 |
| new | actual | all | top3_stress | 0.5000 | tau | 386 | 0.0035 | 0.0000 | 0.0001 | 0.0081 | 0.0146 | 0.0363 | 0.1000 |
| new | actual | all | top3_stress | 0.8000 | tau | 386 | 0.0032 | 0.0000 | 0.0001 | 0.0079 | 0.0132 | 0.0363 | 0.1000 |
| new | actual | 1-3 | - | 0.0000 | M | 41 | 0.0041 | 0.0000 | 0.0028 | 0.0077 | 0.0097 |  |  |
| new | actual | 1-3 | linear | 0.0000 | tau | 41 | 0.0010 | 0.0001 | 0.0006 | 0.0016 | 0.0042 | 0.0000 | 0.5000 |
| new | actual | 1-3 | linear | 0.5000 | tau | 41 | -0.0000 | -0.0005 | 0.0001 | 0.0004 | 0.0028 | 0.2927 | 0.5000 |
| new | actual | 1-3 | linear | 0.8000 | tau | 41 | -0.0007 | -0.0011 | 0.0001 | 0.0002 | 0.0022 | 0.2927 | 0.5000 |
| new | actual | 1-3 | concave | 0.0000 | tau | 41 | 0.0021 | 0.0001 | 0.0014 | 0.0045 | 0.0059 | 0.0000 | 0.6599 |
| new | actual | 1-3 | concave | 0.5000 | tau | 41 | 0.0008 | 0.0001 | 0.0006 | 0.0020 | 0.0029 | 0.0000 | 0.6599 |
| new | actual | 1-3 | concave | 0.8000 | tau | 41 | -0.0000 | 0.0000 | 0.0001 | 0.0003 | 0.0019 | 0.1220 | 0.6599 |
| new | actual | 1-3 | convex | 0.0000 | tau | 41 | -0.0006 | -0.0016 | 0.0000 | 0.0003 | 0.0028 | 0.0000 | 0.3391 |
| new | actual | 1-3 | convex | 0.5000 | tau | 41 | -0.0013 | -0.0023 | 0.0000 | 0.0001 | 0.0012 | 0.0976 | 0.3391 |
| new | actual | 1-3 | convex | 0.8000 | tau | 41 | -0.0017 | -0.0029 | -0.0004 | 0.0001 | 0.0002 | 0.1463 | 0.3391 |
| new | actual | 1-3 | top3_stress | 0.0000 | tau | 41 | -0.0031 | -0.0047 | -0.0011 | 0.0000 | 0.0000 | 0.0000 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.5000 | tau | 41 | -0.0033 | -0.0049 | -0.0012 | -0.0000 | 0.0000 | 0.0976 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.8000 | tau | 41 | -0.0034 | -0.0051 | -0.0013 | -0.0000 | 0.0000 | 0.0976 | 0.1000 |
| new | actual | 4-10 | - | 0.0000 | M | 91 | 0.0019 | 0.0000 | 0.0000 | 0.0020 | 0.0077 |  |  |
| new | actual | 4-10 | linear | 0.0000 | tau | 91 | 0.0011 | 0.0000 | 0.0002 | 0.0011 | 0.0055 | 0.0000 | 0.5000 |
| new | actual | 4-10 | linear | 0.5000 | tau | 91 | 0.0007 | -0.0002 | 0.0000 | 0.0004 | 0.0053 | 0.2857 | 0.5000 |
| new | actual | 4-10 | linear | 0.8000 | tau | 91 | 0.0004 | -0.0003 | 0.0000 | 0.0003 | 0.0050 | 0.3077 | 0.5000 |
| new | actual | 4-10 | concave | 0.0000 | tau | 91 | 0.0015 | 0.0000 | 0.0006 | 0.0024 | 0.0053 | 0.0000 | 0.6599 |
| new | actual | 4-10 | concave | 0.5000 | tau | 91 | 0.0009 | 0.0000 | 0.0003 | 0.0012 | 0.0041 | 0.0110 | 0.6599 |
| new | actual | 4-10 | concave | 0.8000 | tau | 91 | 0.0005 | 0.0000 | 0.0000 | 0.0003 | 0.0041 | 0.0549 | 0.6599 |
| new | actual | 4-10 | convex | 0.0000 | tau | 91 | 0.0006 | -0.0006 | 0.0000 | 0.0003 | 0.0066 | 0.0000 | 0.3391 |
| new | actual | 4-10 | convex | 0.5000 | tau | 91 | 0.0003 | -0.0007 | 0.0000 | 0.0003 | 0.0061 | 0.0000 | 0.3391 |
| new | actual | 4-10 | convex | 0.8000 | tau | 91 | 0.0001 | -0.0008 | 0.0000 | 0.0004 | 0.0053 | 0.0110 | 0.3391 |
| new | actual | 4-10 | top3_stress | 0.0000 | tau | 91 | -0.0004 | -0.0018 | 0.0000 | 0.0004 | 0.0050 | 0.0000 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.5000 | tau | 91 | -0.0005 | -0.0017 | 0.0000 | 0.0004 | 0.0045 | 0.0110 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.8000 | tau | 91 | -0.0005 | -0.0017 | 0.0000 | 0.0004 | 0.0043 | 0.0110 | 0.1000 |
| new | actual | 11-16 | - | 0.0000 | M | 79 | 0.0065 | 0.0000 | 0.0000 | 0.0113 | 0.0268 |  |  |
| new | actual | 11-16 | linear | 0.0000 | tau | 79 | 0.0173 | 0.0013 | 0.0146 | 0.0303 | 0.0398 | 0.0000 | 0.5000 |
| new | actual | 11-16 | linear | 0.5000 | tau | 79 | 0.0157 | 0.0009 | 0.0114 | 0.0255 | 0.0398 | 0.0000 | 0.5000 |
| new | actual | 11-16 | linear | 0.8000 | tau | 79 | 0.0147 | 0.0007 | 0.0108 | 0.0254 | 0.0398 | 0.0000 | 0.5000 |
| new | actual | 11-16 | concave | 0.0000 | tau | 79 | 0.0144 | 0.0011 | 0.0115 | 0.0262 | 0.0331 | 0.0000 | 0.6599 |
| new | actual | 11-16 | concave | 0.5000 | tau | 79 | 0.0123 | 0.0009 | 0.0093 | 0.0206 | 0.0305 | 0.0000 | 0.6599 |
| new | actual | 11-16 | concave | 0.8000 | tau | 79 | 0.0110 | 0.0006 | 0.0073 | 0.0167 | 0.0305 | 0.0000 | 0.6599 |
| new | actual | 11-16 | convex | 0.0000 | tau | 79 | 0.0174 | 0.0011 | 0.0147 | 0.0317 | 0.0376 | 0.0000 | 0.3391 |
| new | actual | 11-16 | convex | 0.5000 | tau | 79 | 0.0163 | 0.0008 | 0.0142 | 0.0301 | 0.0376 | 0.0000 | 0.3391 |
| new | actual | 11-16 | convex | 0.8000 | tau | 79 | 0.0157 | 0.0007 | 0.0137 | 0.0301 | 0.0376 | 0.0000 | 0.3391 |
| new | actual | 11-16 | top3_stress | 0.0000 | tau | 79 | 0.0092 | 0.0009 | 0.0091 | 0.0126 | 0.0220 | 0.0000 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.5000 | tau | 79 | 0.0089 | 0.0009 | 0.0091 | 0.0122 | 0.0206 | 0.0000 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.8000 | tau | 79 | 0.0087 | 0.0009 | 0.0091 | 0.0122 | 0.0197 | 0.0000 | 0.1000 |
| new | actual | 17-30 | - | 0.0000 | M | 175 | 0.0125 | -0.0000 | 0.0000 | 0.0000 | 0.0681 |  |  |
| new | actual | 17-30 | linear | 0.0000 | tau | 175 | 0.0291 | 0.0091 | 0.0243 | 0.0451 | 0.0595 | 0.0000 | 0.5000 |
| new | actual | 17-30 | linear | 0.5000 | tau | 175 | 0.0259 | 0.0072 | 0.0243 | 0.0430 | 0.0502 | 0.0000 | 0.5000 |
| new | actual | 17-30 | linear | 0.8000 | tau | 175 | 0.0241 | 0.0057 | 0.0239 | 0.0408 | 0.0464 | 0.0057 | 0.5000 |
| new | actual | 17-30 | concave | 0.0000 | tau | 175 | 0.0300 | 0.0098 | 0.0310 | 0.0374 | 0.0616 | 0.0000 | 0.6599 |
| new | actual | 17-30 | concave | 0.5000 | tau | 175 | 0.0259 | 0.0074 | 0.0311 | 0.0369 | 0.0434 | 0.0000 | 0.6599 |
| new | actual | 17-30 | concave | 0.8000 | tau | 175 | 0.0234 | 0.0052 | 0.0296 | 0.0347 | 0.0386 | 0.0000 | 0.6599 |
| new | actual | 17-30 | convex | 0.0000 | tau | 175 | 0.0214 | 0.0015 | 0.0105 | 0.0400 | 0.0523 | 0.0000 | 0.3391 |
| new | actual | 17-30 | convex | 0.5000 | tau | 175 | 0.0193 | 0.0015 | 0.0100 | 0.0365 | 0.0455 | 0.0057 | 0.3391 |
| new | actual | 17-30 | convex | 0.8000 | tau | 175 | 0.0180 | 0.0015 | 0.0094 | 0.0334 | 0.0421 | 0.0057 | 0.3391 |
| new | actual | 17-30 | top3_stress | 0.0000 | tau | 175 | 0.0053 | 0.0000 | 0.0005 | 0.0090 | 0.0194 | 0.0000 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.5000 | tau | 175 | 0.0047 | 0.0000 | 0.0005 | 0.0084 | 0.0160 | 0.0514 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.8000 | tau | 175 | 0.0043 | 0.0000 | 0.0005 | 0.0082 | 0.0140 | 0.0514 | 0.1000 |
| new | own | all | - | 0.0000 | M | 386 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | all | linear | 0.0000 | tau | 386 | 0.0228 | 0.0002 | 0.0175 | 0.0414 | 0.0568 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.5000 | tau | 386 | 0.0228 | 0.0002 | 0.0175 | 0.0414 | 0.0568 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.8000 | tau | 386 | 0.0228 | 0.0002 | 0.0175 | 0.0414 | 0.0568 | 0.0000 | 0.5000 |
| new | own | all | concave | 0.0000 | tau | 386 | 0.0200 | 0.0001 | 0.0233 | 0.0343 | 0.0435 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.5000 | tau | 386 | 0.0200 | 0.0001 | 0.0233 | 0.0343 | 0.0435 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.8000 | tau | 386 | 0.0200 | 0.0001 | 0.0233 | 0.0343 | 0.0435 | 0.0000 | 0.6599 |
| new | own | all | convex | 0.0000 | tau | 386 | 0.0194 | 0.0001 | 0.0077 | 0.0369 | 0.0563 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.5000 | tau | 386 | 0.0194 | 0.0001 | 0.0077 | 0.0369 | 0.0563 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.8000 | tau | 386 | 0.0194 | 0.0001 | 0.0077 | 0.0369 | 0.0563 | 0.0000 | 0.3391 |
| new | own | all | top3_stress | 0.0000 | tau | 386 | 0.0059 | 0.0000 | 0.0008 | 0.0114 | 0.0218 | 0.0000 | 0.1000 |
| new | own | all | top3_stress | 0.5000 | tau | 386 | 0.0059 | 0.0000 | 0.0008 | 0.0114 | 0.0218 | 0.0570 | 0.1000 |
| new | own | all | top3_stress | 0.8000 | tau | 386 | 0.0059 | 0.0000 | 0.0008 | 0.0114 | 0.0218 | 0.0570 | 0.1000 |
| new | own | 1-3 | - | 0.0000 | M | 41 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 1-3 | linear | 0.0000 | tau | 41 | -0.0010 | -0.0014 | -0.0005 | 0.0001 | 0.0001 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.5000 | tau | 41 | -0.0010 | -0.0014 | -0.0005 | 0.0001 | 0.0001 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.8000 | tau | 41 | -0.0010 | -0.0014 | -0.0005 | 0.0001 | 0.0001 | 0.0000 | 0.5000 |
| new | own | 1-3 | concave | 0.0000 | tau | 41 | -0.0005 | -0.0007 | -0.0003 | 0.0000 | 0.0001 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.5000 | tau | 41 | -0.0005 | -0.0007 | -0.0003 | 0.0000 | 0.0001 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.8000 | tau | 41 | -0.0005 | -0.0007 | -0.0003 | 0.0000 | 0.0001 | 0.0000 | 0.6599 |
| new | own | 1-3 | convex | 0.0000 | tau | 41 | -0.0019 | -0.0026 | -0.0010 | 0.0000 | 0.0001 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.5000 | tau | 41 | -0.0019 | -0.0026 | -0.0010 | 0.0000 | 0.0001 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.8000 | tau | 41 | -0.0019 | -0.0026 | -0.0010 | 0.0000 | 0.0001 | 0.0000 | 0.3391 |
| new | own | 1-3 | top3_stress | 0.0000 | tau | 41 | -0.0035 | -0.0047 | -0.0019 | 0.0000 | 0.0000 | 0.0000 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.5000 | tau | 41 | -0.0035 | -0.0047 | -0.0019 | -0.0000 | -0.0000 | 0.0976 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.8000 | tau | 41 | -0.0035 | -0.0047 | -0.0019 | -0.0000 | -0.0000 | 0.0976 | 0.1000 |
| new | own | 4-10 | - | 0.0000 | M | 91 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 4-10 | linear | 0.0000 | tau | 91 | 0.0010 | -0.0005 | 0.0001 | 0.0015 | 0.0055 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.5000 | tau | 91 | 0.0010 | -0.0005 | 0.0001 | 0.0015 | 0.0055 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.8000 | tau | 91 | 0.0010 | -0.0005 | 0.0001 | 0.0015 | 0.0055 | 0.0000 | 0.5000 |
| new | own | 4-10 | concave | 0.0000 | tau | 91 | 0.0006 | -0.0003 | 0.0000 | 0.0009 | 0.0033 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.5000 | tau | 91 | 0.0006 | -0.0003 | 0.0000 | 0.0009 | 0.0033 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.8000 | tau | 91 | 0.0006 | -0.0003 | 0.0000 | 0.0009 | 0.0033 | 0.0000 | 0.6599 |
| new | own | 4-10 | convex | 0.0000 | tau | 91 | 0.0013 | -0.0009 | 0.0001 | 0.0022 | 0.0081 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.5000 | tau | 91 | 0.0013 | -0.0009 | 0.0001 | 0.0022 | 0.0081 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.8000 | tau | 91 | 0.0013 | -0.0009 | 0.0001 | 0.0022 | 0.0081 | 0.0000 | 0.3391 |
| new | own | 4-10 | top3_stress | 0.0000 | tau | 91 | 0.0005 | -0.0018 | 0.0000 | 0.0022 | 0.0082 | 0.0000 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.5000 | tau | 91 | 0.0005 | -0.0018 | 0.0000 | 0.0022 | 0.0082 | 0.0330 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.8000 | tau | 91 | 0.0005 | -0.0018 | 0.0000 | 0.0022 | 0.0082 | 0.0330 | 0.1000 |
| new | own | 11-16 | - | 0.0000 | M | 79 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 11-16 | linear | 0.0000 | tau | 79 | 0.0287 | 0.0129 | 0.0335 | 0.0417 | 0.0459 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.5000 | tau | 79 | 0.0287 | 0.0129 | 0.0335 | 0.0417 | 0.0459 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.8000 | tau | 79 | 0.0287 | 0.0129 | 0.0335 | 0.0417 | 0.0459 | 0.0000 | 0.5000 |
| new | own | 11-16 | concave | 0.0000 | tau | 79 | 0.0201 | 0.0081 | 0.0227 | 0.0304 | 0.0340 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.5000 | tau | 79 | 0.0201 | 0.0081 | 0.0227 | 0.0304 | 0.0340 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.8000 | tau | 79 | 0.0201 | 0.0081 | 0.0227 | 0.0304 | 0.0340 | 0.0000 | 0.6599 |
| new | own | 11-16 | convex | 0.0000 | tau | 79 | 0.0316 | 0.0170 | 0.0363 | 0.0431 | 0.0536 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.5000 | tau | 79 | 0.0316 | 0.0170 | 0.0363 | 0.0431 | 0.0536 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.8000 | tau | 79 | 0.0316 | 0.0170 | 0.0363 | 0.0431 | 0.0536 | 0.0000 | 0.3391 |
| new | own | 11-16 | top3_stress | 0.0000 | tau | 79 | 0.0133 | 0.0080 | 0.0117 | 0.0206 | 0.0259 | 0.0000 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.5000 | tau | 79 | 0.0133 | 0.0080 | 0.0117 | 0.0206 | 0.0259 | 0.0380 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.8000 | tau | 79 | 0.0133 | 0.0080 | 0.0117 | 0.0206 | 0.0259 | 0.0380 | 0.1000 |
| new | own | 17-30 | - | 0.0000 | M | 175 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 17-30 | linear | 0.0000 | tau | 175 | 0.0370 | 0.0199 | 0.0380 | 0.0525 | 0.0664 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.5000 | tau | 175 | 0.0370 | 0.0199 | 0.0380 | 0.0525 | 0.0664 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.8000 | tau | 175 | 0.0370 | 0.0199 | 0.0380 | 0.0525 | 0.0664 | 0.0000 | 0.5000 |
| new | own | 17-30 | concave | 0.0000 | tau | 175 | 0.0349 | 0.0296 | 0.0345 | 0.0429 | 0.0488 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.5000 | tau | 175 | 0.0349 | 0.0296 | 0.0345 | 0.0429 | 0.0488 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.8000 | tau | 175 | 0.0349 | 0.0296 | 0.0345 | 0.0429 | 0.0488 | 0.0000 | 0.6599 |
| new | own | 17-30 | convex | 0.0000 | tau | 175 | 0.0284 | 0.0049 | 0.0235 | 0.0479 | 0.0663 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.5000 | tau | 175 | 0.0284 | 0.0049 | 0.0235 | 0.0479 | 0.0663 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.8000 | tau | 175 | 0.0284 | 0.0049 | 0.0235 | 0.0479 | 0.0663 | 0.0000 | 0.3391 |
| new | own | 17-30 | top3_stress | 0.0000 | tau | 175 | 0.0076 | 0.0000 | 0.0015 | 0.0133 | 0.0240 | 0.0000 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.5000 | tau | 175 | 0.0076 | 0.0000 | 0.0015 | 0.0133 | 0.0240 | 0.0686 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.8000 | tau | 175 | 0.0076 | 0.0000 | 0.0015 | 0.0133 | 0.0240 | 0.0686 | 0.1000 |
| delta | actual | all | - | 0.0000 | M | 386 | 0.0005 | -0.0000 | 0.0000 | 0.0019 | 0.0124 |  |  |
| delta | actual | all | linear | 0.0000 | tau | 386 | 0.0005 | -0.0022 | 0.0000 | 0.0048 | 0.0139 | 0.0000 | 0.5000 |
| delta | actual | all | linear | 0.5000 | tau | 386 | 0.0004 | -0.0029 | 0.0000 | 0.0047 | 0.0124 | 0.0181 | 0.5000 |
| delta | actual | all | linear | 0.8000 | tau | 386 | 0.0003 | -0.0031 | 0.0000 | 0.0042 | 0.0117 | 0.0285 | 0.5000 |
| delta | actual | all | concave | 0.0000 | tau | 386 | 0.0005 | -0.0007 | 0.0000 | 0.0031 | 0.0139 | 0.0000 | 0.6599 |
| delta | actual | all | concave | 0.5000 | tau | 386 | 0.0003 | -0.0010 | 0.0000 | 0.0027 | 0.0097 | 0.0570 | 0.6599 |
| delta | actual | all | concave | 0.8000 | tau | 386 | 0.0002 | -0.0015 | 0.0000 | 0.0025 | 0.0077 | 0.0777 | 0.6599 |
| delta | actual | all | convex | 0.0000 | tau | 386 | 0.0004 | -0.0052 | 0.0000 | 0.0069 | 0.0168 | 0.0000 | 0.3391 |
| delta | actual | all | convex | 0.5000 | tau | 386 | 0.0004 | -0.0056 | 0.0000 | 0.0066 | 0.0157 | 0.0078 | 0.3391 |
| delta | actual | all | convex | 0.8000 | tau | 386 | 0.0003 | -0.0059 | 0.0000 | 0.0064 | 0.0141 | 0.0104 | 0.3391 |
| delta | actual | all | top3_stress | 0.0000 | tau | 386 | -0.0001 | -0.0056 | 0.0000 | 0.0052 | 0.0125 | 0.0000 | 0.1000 |
| delta | actual | all | top3_stress | 0.5000 | tau | 386 | -0.0001 | -0.0053 | 0.0000 | 0.0052 | 0.0119 | 0.0052 | 0.1000 |
| delta | actual | all | top3_stress | 0.8000 | tau | 386 | -0.0001 | -0.0051 | 0.0000 | 0.0052 | 0.0116 | 0.0078 | 0.1000 |
| delta | actual | 1-3 | - | 0.0000 | M | 41 | 0.0047 | 0.0000 | 0.0033 | 0.0077 | 0.0101 |  |  |
| delta | actual | 1-3 | linear | 0.0000 | tau | 41 | -0.0005 | -0.0019 | -0.0014 | -0.0006 | 0.0020 | 0.0000 | 0.5000 |
| delta | actual | 1-3 | linear | 0.5000 | tau | 41 | -0.0017 | -0.0026 | -0.0016 | -0.0010 | 0.0005 | 0.0976 | 0.5000 |
| delta | actual | 1-3 | linear | 0.8000 | tau | 41 | -0.0024 | -0.0030 | -0.0018 | -0.0013 | -0.0010 | 0.1707 | 0.5000 |
| delta | actual | 1-3 | concave | 0.0000 | tau | 41 | 0.0019 | -0.0007 | 0.0009 | 0.0029 | 0.0039 | 0.0000 | 0.6599 |
| delta | actual | 1-3 | concave | 0.5000 | tau | 41 | 0.0003 | -0.0008 | -0.0002 | 0.0001 | 0.0017 | 0.2683 | 0.6599 |
| delta | actual | 1-3 | concave | 0.8000 | tau | 41 | -0.0006 | -0.0013 | -0.0008 | -0.0005 | 0.0006 | 0.4146 | 0.6599 |
| delta | actual | 1-3 | convex | 0.0000 | tau | 41 | -0.0040 | -0.0051 | -0.0030 | -0.0021 | -0.0016 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | convex | 0.5000 | tau | 41 | -0.0048 | -0.0056 | -0.0033 | -0.0027 | -0.0023 | 0.0488 | 0.3391 |
| delta | actual | 1-3 | convex | 0.8000 | tau | 41 | -0.0053 | -0.0062 | -0.0039 | -0.0027 | -0.0023 | 0.0488 | 0.3391 |
| delta | actual | 1-3 | top3_stress | 0.0000 | tau | 41 | -0.0055 | -0.0079 | -0.0028 | -0.0003 | -0.0001 | 0.0000 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.5000 | tau | 41 | -0.0057 | -0.0081 | -0.0030 | -0.0003 | -0.0001 | 0.0000 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.8000 | tau | 41 | -0.0059 | -0.0083 | -0.0031 | -0.0003 | -0.0001 | 0.0244 | 0.1000 |
| delta | actual | 4-10 | - | 0.0000 | M | 91 | -0.0064 | -0.0154 | 0.0000 | 0.0013 | 0.0043 |  |  |
| delta | actual | 4-10 | linear | 0.0000 | tau | 91 | -0.0101 | -0.0171 | -0.0051 | -0.0024 | 0.0000 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | linear | 0.5000 | tau | 91 | -0.0085 | -0.0133 | -0.0056 | -0.0031 | 0.0000 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | linear | 0.8000 | tau | 91 | -0.0075 | -0.0114 | -0.0060 | -0.0033 | 0.0000 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | concave | 0.0000 | tau | 91 | -0.0085 | -0.0171 | -0.0028 | 0.0000 | 0.0002 | 0.0000 | 0.6599 |
| delta | actual | 4-10 | concave | 0.5000 | tau | 91 | -0.0064 | -0.0112 | -0.0028 | -0.0009 | 0.0000 | 0.1209 | 0.6599 |
| delta | actual | 4-10 | concave | 0.8000 | tau | 91 | -0.0052 | -0.0082 | -0.0031 | -0.0016 | 0.0000 | 0.1209 | 0.6599 |
| delta | actual | 4-10 | convex | 0.0000 | tau | 91 | -0.0120 | -0.0176 | -0.0100 | -0.0056 | 0.0000 | 0.0000 | 0.3391 |
| delta | actual | 4-10 | convex | 0.5000 | tau | 91 | -0.0109 | -0.0165 | -0.0109 | -0.0058 | 0.0000 | 0.0000 | 0.3391 |
| delta | actual | 4-10 | convex | 0.8000 | tau | 91 | -0.0103 | -0.0144 | -0.0104 | -0.0060 | 0.0000 | 0.0000 | 0.3391 |
| delta | actual | 4-10 | top3_stress | 0.0000 | tau | 91 | -0.0104 | -0.0134 | -0.0102 | -0.0072 | 0.0000 | 0.0000 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.5000 | tau | 91 | -0.0100 | -0.0129 | -0.0099 | -0.0071 | 0.0000 | 0.0000 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.8000 | tau | 91 | -0.0099 | -0.0122 | -0.0095 | -0.0066 | 0.0000 | 0.0000 | 0.1000 |
| delta | actual | 11-16 | - | 0.0000 | M | 79 | -0.0064 | -0.0000 | 0.0000 | 0.0074 | 0.0191 |  |  |
| delta | actual | 11-16 | linear | 0.0000 | tau | 79 | -0.0036 | -0.0021 | 0.0030 | 0.0072 | 0.0182 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | linear | 0.5000 | tau | 79 | -0.0020 | -0.0021 | 0.0030 | 0.0060 | 0.0134 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | linear | 0.8000 | tau | 79 | -0.0011 | -0.0021 | 0.0030 | 0.0053 | 0.0117 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | concave | 0.0000 | tau | 79 | -0.0050 | -0.0015 | 0.0012 | 0.0072 | 0.0186 | 0.0000 | 0.6599 |
| delta | actual | 11-16 | concave | 0.5000 | tau | 79 | -0.0029 | -0.0015 | 0.0012 | 0.0049 | 0.0123 | 0.0000 | 0.6599 |
| delta | actual | 11-16 | concave | 0.8000 | tau | 79 | -0.0016 | -0.0014 | 0.0012 | 0.0035 | 0.0085 | 0.0000 | 0.6599 |
| delta | actual | 11-16 | convex | 0.0000 | tau | 79 | -0.0012 | -0.0021 | 0.0065 | 0.0089 | 0.0181 | 0.0000 | 0.3391 |
| delta | actual | 11-16 | convex | 0.5000 | tau | 79 | -0.0002 | -0.0021 | 0.0056 | 0.0084 | 0.0158 | 0.0000 | 0.3391 |
| delta | actual | 11-16 | convex | 0.8000 | tau | 79 | 0.0005 | -0.0021 | 0.0049 | 0.0082 | 0.0136 | 0.0000 | 0.3391 |
| delta | actual | 11-16 | top3_stress | 0.0000 | tau | 79 | 0.0042 | 0.0000 | 0.0066 | 0.0094 | 0.0166 | 0.0000 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.5000 | tau | 79 | 0.0045 | 0.0000 | 0.0062 | 0.0090 | 0.0156 | 0.0000 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.8000 | tau | 79 | 0.0047 | 0.0000 | 0.0060 | 0.0089 | 0.0149 | 0.0000 | 0.1000 |
| delta | actual | 17-30 | - | 0.0000 | M | 175 | 0.0062 | -0.0000 | 0.0000 | 0.0000 | 0.0139 |  |  |
| delta | actual | 17-30 | linear | 0.0000 | tau | 175 | 0.0081 | 0.0000 | 0.0001 | 0.0075 | 0.0258 | 0.0000 | 0.5000 |
| delta | actual | 17-30 | linear | 0.5000 | tau | 175 | 0.0065 | 0.0000 | 0.0002 | 0.0070 | 0.0222 | 0.0171 | 0.5000 |
| delta | actual | 17-30 | linear | 0.8000 | tau | 175 | 0.0056 | 0.0000 | 0.0002 | 0.0068 | 0.0200 | 0.0229 | 0.5000 |
| delta | actual | 17-30 | concave | 0.0000 | tau | 175 | 0.0074 | 0.0000 | 0.0001 | 0.0052 | 0.0220 | 0.0000 | 0.6599 |
| delta | actual | 17-30 | concave | 0.5000 | tau | 175 | 0.0053 | 0.0000 | 0.0000 | 0.0048 | 0.0170 | 0.0000 | 0.6599 |
| delta | actual | 17-30 | concave | 0.8000 | tau | 175 | 0.0041 | 0.0000 | 0.0001 | 0.0043 | 0.0137 | 0.0114 | 0.6599 |
| delta | actual | 17-30 | convex | 0.0000 | tau | 175 | 0.0087 | 0.0000 | 0.0005 | 0.0104 | 0.0302 | 0.0000 | 0.3391 |
| delta | actual | 17-30 | convex | 0.5000 | tau | 175 | 0.0077 | 0.0000 | 0.0005 | 0.0103 | 0.0274 | 0.0057 | 0.3391 |
| delta | actual | 17-30 | convex | 0.8000 | tau | 175 | 0.0070 | 0.0000 | 0.0005 | 0.0103 | 0.0257 | 0.0114 | 0.3391 |
| delta | actual | 17-30 | top3_stress | 0.0000 | tau | 175 | 0.0046 | 0.0000 | 0.0004 | 0.0079 | 0.0174 | 0.0000 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.5000 | tau | 175 | 0.0043 | 0.0000 | 0.0004 | 0.0079 | 0.0149 | 0.0114 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.8000 | tau | 175 | 0.0041 | 0.0000 | 0.0004 | 0.0079 | 0.0138 | 0.0114 | 0.1000 |
| delta | own | all | - | 0.0000 | M | 386 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | all | linear | 0.0000 | tau | 386 | 0.0008 | -0.0052 | 0.0000 | 0.0048 | 0.0151 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.5000 | tau | 386 | 0.0008 | -0.0052 | 0.0000 | 0.0048 | 0.0151 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.8000 | tau | 386 | 0.0008 | -0.0052 | 0.0000 | 0.0048 | 0.0151 | 0.0000 | 0.5000 |
| delta | own | all | concave | 0.0000 | tau | 386 | 0.0004 | -0.0029 | 0.0000 | 0.0024 | 0.0088 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.5000 | tau | 386 | 0.0004 | -0.0029 | 0.0000 | 0.0024 | 0.0088 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.8000 | tau | 386 | 0.0004 | -0.0029 | 0.0000 | 0.0024 | 0.0088 | 0.0000 | 0.6599 |
| delta | own | all | convex | 0.0000 | tau | 386 | 0.0014 | -0.0076 | 0.0000 | 0.0083 | 0.0221 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.5000 | tau | 386 | 0.0014 | -0.0076 | 0.0000 | 0.0083 | 0.0221 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.8000 | tau | 386 | 0.0014 | -0.0076 | 0.0000 | 0.0083 | 0.0221 | 0.0000 | 0.3391 |
| delta | own | all | top3_stress | 0.0000 | tau | 386 | 0.0010 | -0.0081 | 0.0000 | 0.0080 | 0.0181 | 0.0000 | 0.1000 |
| delta | own | all | top3_stress | 0.5000 | tau | 386 | 0.0010 | -0.0081 | 0.0000 | 0.0080 | 0.0181 | 0.0052 | 0.1000 |
| delta | own | all | top3_stress | 0.8000 | tau | 386 | 0.0010 | -0.0081 | 0.0000 | 0.0080 | 0.0181 | 0.0052 | 0.1000 |
| delta | own | 1-3 | - | 0.0000 | M | 41 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 1-3 | linear | 0.0000 | tau | 41 | -0.0033 | -0.0040 | -0.0028 | -0.0018 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.5000 | tau | 41 | -0.0033 | -0.0040 | -0.0028 | -0.0018 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.8000 | tau | 41 | -0.0033 | -0.0040 | -0.0028 | -0.0018 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | concave | 0.0000 | tau | 41 | -0.0017 | -0.0022 | -0.0015 | -0.0009 | -0.0007 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.5000 | tau | 41 | -0.0017 | -0.0022 | -0.0015 | -0.0009 | -0.0007 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.8000 | tau | 41 | -0.0017 | -0.0022 | -0.0015 | -0.0009 | -0.0007 | 0.0000 | 0.6599 |
| delta | own | 1-3 | convex | 0.0000 | tau | 41 | -0.0058 | -0.0070 | -0.0048 | -0.0030 | -0.0024 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.5000 | tau | 41 | -0.0058 | -0.0070 | -0.0048 | -0.0030 | -0.0024 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.8000 | tau | 41 | -0.0058 | -0.0070 | -0.0048 | -0.0030 | -0.0024 | 0.0000 | 0.3391 |
| delta | own | 1-3 | top3_stress | 0.0000 | tau | 41 | -0.0060 | -0.0079 | -0.0029 | -0.0005 | -0.0003 | 0.0000 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.5000 | tau | 41 | -0.0060 | -0.0079 | -0.0029 | -0.0005 | -0.0003 | 0.0000 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.8000 | tau | 41 | -0.0060 | -0.0079 | -0.0029 | -0.0005 | -0.0003 | 0.0000 | 0.1000 |
| delta | own | 4-10 | - | 0.0000 | M | 91 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 4-10 | linear | 0.0000 | tau | 91 | -0.0082 | -0.0112 | -0.0071 | -0.0052 | -0.0034 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.5000 | tau | 91 | -0.0082 | -0.0112 | -0.0071 | -0.0052 | -0.0034 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.8000 | tau | 91 | -0.0082 | -0.0112 | -0.0071 | -0.0052 | -0.0034 | 0.0000 | 0.5000 |
| delta | own | 4-10 | concave | 0.0000 | tau | 91 | -0.0046 | -0.0064 | -0.0039 | -0.0028 | -0.0019 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.5000 | tau | 91 | -0.0046 | -0.0064 | -0.0039 | -0.0028 | -0.0019 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.8000 | tau | 91 | -0.0046 | -0.0064 | -0.0039 | -0.0028 | -0.0019 | 0.0000 | 0.6599 |
| delta | own | 4-10 | convex | 0.0000 | tau | 91 | -0.0127 | -0.0172 | -0.0118 | -0.0079 | -0.0058 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.5000 | tau | 91 | -0.0127 | -0.0172 | -0.0118 | -0.0079 | -0.0058 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.8000 | tau | 91 | -0.0127 | -0.0172 | -0.0118 | -0.0079 | -0.0058 | 0.0000 | 0.3391 |
| delta | own | 4-10 | top3_stress | 0.0000 | tau | 91 | -0.0124 | -0.0147 | -0.0112 | -0.0091 | -0.0072 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.5000 | tau | 91 | -0.0124 | -0.0147 | -0.0112 | -0.0091 | -0.0072 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.8000 | tau | 91 | -0.0124 | -0.0147 | -0.0112 | -0.0091 | -0.0072 | 0.0000 | 0.1000 |
| delta | own | 11-16 | - | 0.0000 | M | 79 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 11-16 | linear | 0.0000 | tau | 79 | 0.0019 | -0.0052 | 0.0033 | 0.0060 | 0.0119 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.5000 | tau | 79 | 0.0019 | -0.0052 | 0.0033 | 0.0060 | 0.0119 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.8000 | tau | 79 | 0.0019 | -0.0052 | 0.0033 | 0.0060 | 0.0119 | 0.0000 | 0.5000 |
| delta | own | 11-16 | concave | 0.0000 | tau | 79 | 0.0006 | -0.0032 | 0.0015 | 0.0033 | 0.0066 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.5000 | tau | 79 | 0.0006 | -0.0032 | 0.0015 | 0.0033 | 0.0066 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.8000 | tau | 79 | 0.0006 | -0.0032 | 0.0015 | 0.0033 | 0.0066 | 0.0000 | 0.6599 |
| delta | own | 11-16 | convex | 0.0000 | tau | 79 | 0.0045 | -0.0050 | 0.0070 | 0.0112 | 0.0188 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.5000 | tau | 79 | 0.0045 | -0.0050 | 0.0070 | 0.0112 | 0.0188 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.8000 | tau | 79 | 0.0045 | -0.0050 | 0.0070 | 0.0112 | 0.0188 | 0.0000 | 0.3391 |
| delta | own | 11-16 | top3_stress | 0.0000 | tau | 79 | 0.0076 | 0.0034 | 0.0077 | 0.0154 | 0.0199 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.5000 | tau | 79 | 0.0076 | 0.0034 | 0.0077 | 0.0154 | 0.0199 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.8000 | tau | 79 | 0.0076 | 0.0034 | 0.0077 | 0.0154 | 0.0199 | 0.0000 | 0.1000 |
| delta | own | 17-30 | - | 0.0000 | M | 175 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 17-30 | linear | 0.0000 | tau | 175 | 0.0060 | 0.0000 | 0.0006 | 0.0109 | 0.0194 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.5000 | tau | 175 | 0.0060 | 0.0000 | 0.0006 | 0.0109 | 0.0194 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.8000 | tau | 175 | 0.0060 | 0.0000 | 0.0006 | 0.0109 | 0.0194 | 0.0000 | 0.5000 |
| delta | own | 17-30 | concave | 0.0000 | tau | 175 | 0.0035 | 0.0000 | 0.0004 | 0.0061 | 0.0110 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.5000 | tau | 175 | 0.0035 | 0.0000 | 0.0004 | 0.0061 | 0.0110 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.8000 | tau | 175 | 0.0035 | 0.0000 | 0.0004 | 0.0061 | 0.0110 | 0.0000 | 0.6599 |
| delta | own | 17-30 | convex | 0.0000 | tau | 175 | 0.0089 | 0.0000 | 0.0014 | 0.0165 | 0.0289 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.5000 | tau | 175 | 0.0089 | 0.0000 | 0.0014 | 0.0165 | 0.0289 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.8000 | tau | 175 | 0.0089 | 0.0000 | 0.0014 | 0.0165 | 0.0289 | 0.0000 | 0.3391 |
| delta | own | 17-30 | top3_stress | 0.0000 | tau | 175 | 0.0066 | 0.0000 | 0.0014 | 0.0112 | 0.0206 | 0.0000 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.5000 | tau | 175 | 0.0066 | 0.0000 | 0.0014 | 0.0112 | 0.0206 | 0.0114 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.8000 | tau | 175 | 0.0066 | 0.0000 | 0.0014 | 0.0112 | 0.0206 | 0.0114 | 0.1000 |

## T5_attr_seeding

| rule | portfolio | seed_group | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| old | actual | <0.01 | B | dominance_positive | 0.8362 | 0.7674 | 0.9115 | 116 |
| old | actual | <0.01 | B | reversal | 0.0345 | 0.0000 | 0.0746 | 116 |
| old | actual | <0.01 | B | negligible | 0.0517 | 0.0101 | 0.0952 | 116 |
| old | actual | <0.01 | B | unresolved | 0.0776 | 0.0280 | 0.1333 | 116 |
| old | actual | 0.01-0.05 | B | dominance_positive | 0.8182 | 0.5384 | 1.0000 | 22 |
| old | actual | 0.01-0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 22 |
| old | actual | 0.01-0.05 | B | negligible | 0.1364 | 0.0000 | 0.3750 | 22 |
| old | actual | 0.01-0.05 | B | unresolved | 0.0455 | 0.0000 | 0.2273 | 22 |
| old | actual | >=0.05 | B | dominance_positive | 0.7339 | 0.6864 | 0.7854 | 248 |
| old | actual | >=0.05 | B | reversal | 0.0161 | 0.0000 | 0.0370 | 248 |
| old | actual | >=0.05 | B | negligible | 0.2500 | 0.1966 | 0.2982 | 248 |
| old | actual | >=0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 248 |
| old | own | <0.01 | B | dominance_positive | 0.9655 | 0.9231 | 1.0000 | 116 |
| old | own | <0.01 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 116 |
| old | own | <0.01 | B | negligible | 0.0345 | 0.0000 | 0.0769 | 116 |
| old | own | <0.01 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 116 |
| old | own | 0.01-0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 22 |
| old | own | 0.01-0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 22 |
| old | own | 0.01-0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 22 |
| old | own | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 22 |
| old | own | >=0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 248 |
| old | own | >=0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 248 |
| old | own | >=0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 248 |
| old | own | >=0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 248 |
| new | actual | <0.01 | B | dominance_positive | 0.2414 | 0.1463 | 0.3448 | 116 |
| new | actual | <0.01 | B | reversal | 0.3534 | 0.2521 | 0.4455 | 116 |
| new | actual | <0.01 | B | negligible | 0.3103 | 0.1983 | 0.4220 | 116 |
| new | actual | <0.01 | B | unresolved | 0.0948 | 0.0388 | 0.1548 | 116 |
| new | actual | 0.01-0.05 | B | dominance_positive | 0.5455 | 0.3077 | 0.7273 | 22 |
| new | actual | 0.01-0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 22 |
| new | actual | 0.01-0.05 | B | negligible | 0.4545 | 0.2727 | 0.6923 | 22 |
| new | actual | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 22 |
| new | actual | >=0.05 | B | dominance_positive | 0.7702 | 0.7253 | 0.8141 | 248 |
| new | actual | >=0.05 | B | reversal | 0.0161 | 0.0000 | 0.0385 | 248 |
| new | actual | >=0.05 | B | negligible | 0.2056 | 0.1598 | 0.2529 | 248 |
| new | actual | >=0.05 | B | unresolved | 0.0081 | 0.0000 | 0.0237 | 248 |
| new | own | <0.01 | B | dominance_positive | 0.1983 | 0.1138 | 0.3000 | 116 |
| new | own | <0.01 | B | reversal | 0.3707 | 0.2613 | 0.4808 | 116 |
| new | own | <0.01 | B | negligible | 0.3966 | 0.2577 | 0.5221 | 116 |
| new | own | <0.01 | B | unresolved | 0.0345 | 0.0000 | 0.0813 | 116 |
| new | own | 0.01-0.05 | B | dominance_positive | 0.6818 | 0.3571 | 0.8929 | 22 |
| new | own | 0.01-0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 22 |
| new | own | 0.01-0.05 | B | negligible | 0.3182 | 0.1071 | 0.6429 | 22 |
| new | own | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 22 |
| new | own | >=0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 248 |
| new | own | >=0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 248 |
| new | own | >=0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 248 |
| new | own | >=0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 248 |

## T5_attr_ledger_features

| rule | feature | value | n | reversal_share | lo99 | hi99 |
|---|---|---|---|---|---|---|
| old | holds_conditional_other | True | 164 | 0.0488 | 0.0141 | 0.0829 |
| old | holds_conditional_other | False | 222 | 0.0000 | 0.0000 | 0.0000 |
| old | holds_opponent_pick | True | 15 | 0.4000 | 0.0908 | 0.7500 |
| old | holds_opponent_pick | False | 371 | 0.0054 | 0.0000 | 0.0159 |
| old | holds_pooled_pick | True | 124 | 0.0403 | 0.0078 | 0.0806 |
| old | holds_pooled_pick | False | 262 | 0.0115 | 0.0000 | 0.0302 |
| old | self_restricted | True | 40 | 0.0250 | 0.0000 | 0.1053 |
| old | self_restricted | False | 346 | 0.0202 | 0.0058 | 0.0358 |
| old | opp_restricted | True | 40 | 0.1000 | 0.0000 | 0.2093 |
| old | opp_restricted | False | 346 | 0.0116 | 0.0000 | 0.0271 |
| old | holds_conditional_other_state | True | 150 | 0.0533 | 0.0156 | 0.0898 |
| old | holds_conditional_other_state | False | 236 | 0.0000 | 0.0000 | 0.0000 |
| old | holds_opponent_pick_state | True | 13 | 0.4615 | 0.1000 | 0.8750 |
| old | holds_opponent_pick_state | False | 373 | 0.0054 | 0.0000 | 0.0157 |
| new | holds_conditional_other | True | 164 | 0.1890 | 0.1258 | 0.2474 |
| new | holds_conditional_other | False | 222 | 0.0631 | 0.0394 | 0.0846 |
| new | holds_opponent_pick | True | 15 | 0.2667 | 0.0000 | 0.5833 |
| new | holds_opponent_pick | False | 371 | 0.1105 | 0.0744 | 0.1439 |
| new | holds_pooled_pick | True | 124 | 0.0565 | 0.0093 | 0.1071 |
| new | holds_pooled_pick | False | 262 | 0.1450 | 0.1022 | 0.1832 |
| new | self_restricted | True | 40 | 0.3500 | 0.2500 | 0.4286 |
| new | self_restricted | False | 346 | 0.0896 | 0.0551 | 0.1217 |
| new | opp_restricted | True | 40 | 0.1000 | 0.0000 | 0.2188 |
| new | opp_restricted | False | 346 | 0.1185 | 0.0788 | 0.1545 |
| new | holds_conditional_other_state | True | 164 | 0.1890 | 0.1258 | 0.2474 |
| new | holds_conditional_other_state | False | 222 | 0.0631 | 0.0394 | 0.0846 |
| new | holds_opponent_pick_state | True | 13 | 0.3077 | 0.0000 | 0.6924 |
| new | holds_opponent_pick_state | False | 373 | 0.1099 | 0.0737 | 0.1432 |

## T5_6_transitions

| portfolio | old | new | count |
|---|---|---|---|
| actual | dominance_positive | dominance_positive | 214 |
| actual | dominance_positive | negligible | 40 |
| actual | dominance_positive | reversal | 38 |
| actual | dominance_positive | unresolved | 5 |
| actual | negligible | dominance_positive | 16 |
| actual | negligible | negligible | 55 |
| actual | reversal | reversal | 6 |
| actual | reversal | unresolved | 2 |
| actual | unresolved | dominance_positive | 1 |
| actual | unresolved | negligible | 2 |
| actual | unresolved | reversal | 1 |
| actual | unresolved | unresolved | 6 |
| own | dominance_positive | dominance_positive | 286 |
| own | dominance_positive | negligible | 49 |
| own | dominance_positive | reversal | 43 |
| own | dominance_positive | unresolved | 4 |
| own | negligible | negligible | 4 |

## T5_headline_reversal_diff

| contrast | portfolio | verdict | share_a | share_b | diff | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| new_minus_old | actual | verdict_B | 0.1166 | 0.0207 | 0.0959 | 0.0612 | 0.1279 | 386 |
| new_minus_old | actual | verdict_B_pm | 0.1062 | 0.0207 | 0.0855 | 0.0556 | 0.1142 | 386 |
| new_minus_old | own | verdict_B | 0.1114 | 0.0000 | 0.1114 | 0.0755 | 0.1440 | 386 |
| new_minus_old | own | verdict_B_pm | 0.1036 | 0.0000 | 0.1036 | 0.0690 | 0.1359 | 386 |
| actual_minus_own | old | verdict_B | 0.0207 | 0.0000 | 0.0207 | 0.0060 | 0.0352 | 386 |
| actual_minus_own | new | verdict_B | 0.1166 | 0.1114 | 0.0052 | -0.0107 | 0.0223 | 386 |

## T5_4_typology

| rule | curve | type | share | lo99 | hi99 | n | tp_dominated_share | n_tp_defined |
|---|---|---|---|---|---|---|---|---|
| old | linear | both_lose | 0.4611 | 0.3964 | 0.5156 | 89 | 0.3708 | 89 |
| old | linear | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| old | linear | normal | 0.4093 | 0.3416 | 0.4885 | 79 | 0.6329 | 79 |
| old | linear | opposed | 0.0207 | 0.0000 | 0.0455 | 4 | 1.0000 | 4 |
| old | linear | one_sided_win | 0.0155 | 0.0000 | 0.0410 | 3 | 0.6667 | 3 |
| old | linear | no_own_stake | 0.0933 | 0.0492 | 0.1381 | 18 | 1.0000 | 14 |
| old | concave | both_lose | 0.3679 | 0.2990 | 0.4335 | 71 | 0.3521 | 71 |
| old | concave | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| old | concave | normal | 0.4922 | 0.4032 | 0.5842 | 95 | 0.6596 | 94 |
| old | concave | opposed | 0.0155 | 0.0000 | 0.0387 | 3 | 1.0000 | 3 |
| old | concave | one_sided_win | 0.0104 | 0.0000 | 0.0315 | 2 | 0.5000 | 2 |
| old | concave | no_own_stake | 0.1140 | 0.0656 | 0.1632 | 22 | 1.0000 | 16 |
| old | convex | both_lose | 0.5078 | 0.4329 | 0.5686 | 98 | 0.3163 | 98 |
| old | convex | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| old | convex | normal | 0.3990 | 0.3333 | 0.4744 | 77 | 0.5455 | 77 |
| old | convex | opposed | 0.0207 | 0.0000 | 0.0455 | 4 | 0.2500 | 4 |
| old | convex | one_sided_win | 0.0052 | 0.0000 | 0.0221 | 1 | 0.0000 | 1 |
| old | convex | no_own_stake | 0.0674 | 0.0286 | 0.1059 | 13 | 1.0000 | 9 |
| old | top3_stress | both_lose | 0.1451 | 0.0989 | 0.1925 | 28 | 0.0000 | 28 |
| old | top3_stress | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| old | top3_stress | normal | 0.4611 | 0.3797 | 0.5388 | 89 | 0.1364 | 88 |
| old | top3_stress | opposed | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| old | top3_stress | one_sided_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| old | top3_stress | no_own_stake | 0.3938 | 0.3196 | 0.4719 | 76 | 1.0000 | 16 |
| new | linear | both_lose | 0.3161 | 0.2485 | 0.3874 | 61 | 0.2295 | 61 |
| new | linear | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| new | linear | normal | 0.4508 | 0.3582 | 0.5372 | 87 | 0.5057 | 87 |
| new | linear | opposed | 0.0052 | 0.0000 | 0.0238 | 1 | 1.0000 | 1 |
| new | linear | one_sided_win | 0.0207 | 0.0000 | 0.0442 | 4 | 0.7500 | 4 |
| new | linear | no_own_stake | 0.2073 | 0.1489 | 0.2747 | 40 | 1.0000 | 18 |
| new | concave | both_lose | 0.3782 | 0.3092 | 0.4410 | 73 | 0.2877 | 73 |
| new | concave | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| new | concave | normal | 0.4197 | 0.3422 | 0.5026 | 81 | 0.5750 | 80 |
| new | concave | opposed | 0.0052 | 0.0000 | 0.0238 | 1 | 1.0000 | 1 |
| new | concave | one_sided_win | 0.0207 | 0.0000 | 0.0442 | 4 | 0.7500 | 4 |
| new | concave | no_own_stake | 0.1762 | 0.1273 | 0.2313 | 34 | 1.0000 | 15 |
| new | convex | both_lose | 0.2746 | 0.2000 | 0.3548 | 53 | 0.2453 | 53 |
| new | convex | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| new | convex | normal | 0.4301 | 0.3318 | 0.5249 | 83 | 0.4819 | 83 |
| new | convex | opposed | 0.0363 | 0.0054 | 0.0730 | 7 | 0.4286 | 7 |
| new | convex | one_sided_win | 0.0466 | 0.0143 | 0.0843 | 9 | 0.4444 | 9 |
| new | convex | no_own_stake | 0.2124 | 0.1494 | 0.2765 | 41 | 1.0000 | 12 |
| new | top3_stress | both_lose | 0.1503 | 0.0950 | 0.2094 | 29 | 0.0000 | 29 |
| new | top3_stress | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan | 0 |
| new | top3_stress | normal | 0.3420 | 0.2458 | 0.4457 | 66 | 0.1667 | 66 |
| new | top3_stress | opposed | 0.0570 | 0.0167 | 0.1005 | 11 | 0.0000 | 11 |
| new | top3_stress | one_sided_win | 0.1192 | 0.0680 | 0.1727 | 23 | 0.3333 | 21 |
| new | top3_stress | no_own_stake | 0.3316 | 0.2603 | 0.4141 | 64 | 1.0000 | 22 |

## T5_5_stakes_distribution

| rule | curve | measure | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| old | linear | tp_share | 189 | 0.5627 | 0.4269 | 0.5308 | 0.7273 | 0.9104 |
| old | linear | tp_share_raw | 192 | 0.6167 | 0.4908 | 0.5964 | 0.7548 | 0.9126 |
| old | linear | hhi | 189 | 0.3068 | 0.2188 | 0.2789 | 0.3780 | 0.4418 |
| old | linear | n_material | 193 | 6.2539 | 4.0000 | 6.0000 | 9.0000 | 10.0000 |
| old | linear | mean_abs_third | 193 | 0.0015 | 0.0008 | 0.0014 | 0.0021 | 0.0029 |
| old | linear | mean_abs_third_raw | 193 | 0.0019 | 0.0012 | 0.0018 | 0.0026 | 0.0033 |
| old | concave | tp_share | 186 | 0.5909 | 0.4329 | 0.5507 | 0.7802 | 1.0000 |
| old | concave | tp_share_raw | 190 | 0.6319 | 0.4942 | 0.6016 | 0.7990 | 0.9216 |
| old | concave | hhi | 186 | 0.3039 | 0.2173 | 0.2847 | 0.3808 | 0.4444 |
| old | concave | n_material | 193 | 5.8238 | 4.0000 | 6.0000 | 8.0000 | 10.0000 |
| old | concave | mean_abs_third | 193 | 0.0016 | 0.0008 | 0.0014 | 0.0024 | 0.0030 |
| old | concave | mean_abs_third_raw | 193 | 0.0020 | 0.0011 | 0.0018 | 0.0027 | 0.0034 |
| old | convex | tp_share | 189 | 0.4958 | 0.3635 | 0.4705 | 0.6712 | 0.8849 |
| old | convex | tp_share_raw | 192 | 0.6050 | 0.4914 | 0.5721 | 0.7180 | 0.8922 |
| old | convex | hhi | 189 | 0.3713 | 0.2556 | 0.3346 | 0.4186 | 0.5140 |
| old | convex | n_material | 193 | 4.9430 | 3.0000 | 5.0000 | 6.0000 | 8.0000 |
| old | convex | mean_abs_third | 193 | 0.0011 | 0.0005 | 0.0009 | 0.0017 | 0.0022 |
| old | convex | mean_abs_third_raw | 193 | 0.0015 | 0.0009 | 0.0014 | 0.0021 | 0.0025 |
| old | top3_stress | tp_share | 132 | 0.3882 | 0.0000 | 0.4158 | 0.4746 | 1.0000 |
| old | top3_stress | tp_share_raw | 167 | 0.5445 | 0.4881 | 0.5040 | 0.5353 | 0.8433 |
| old | top3_stress | hhi | 132 | 0.5960 | 0.3841 | 0.5030 | 1.0000 | 1.0000 |
| old | top3_stress | n_material | 193 | 1.6632 | 0.0000 | 1.0000 | 3.0000 | 4.0000 |
| old | top3_stress | mean_abs_third | 193 | 0.0002 | 0.0000 | 0.0000 | 0.0003 | 0.0005 |
| old | top3_stress | mean_abs_third_raw | 193 | 0.0003 | 0.0001 | 0.0003 | 0.0005 | 0.0007 |
| new | linear | tp_share | 171 | 0.5470 | 0.3901 | 0.4821 | 0.6837 | 1.0000 |
| new | linear | tp_share_raw | 185 | 0.6138 | 0.4991 | 0.5857 | 0.7213 | 0.9379 |
| new | linear | hhi | 171 | 0.3203 | 0.2190 | 0.2902 | 0.3823 | 0.5000 |
| new | linear | n_material | 193 | 5.9067 | 3.0000 | 6.0000 | 9.0000 | 11.0000 |
| new | linear | mean_abs_third | 193 | 0.0014 | 0.0003 | 0.0011 | 0.0022 | 0.0032 |
| new | linear | mean_abs_third_raw | 193 | 0.0017 | 0.0006 | 0.0015 | 0.0026 | 0.0035 |
| new | concave | tp_share | 173 | 0.5469 | 0.4003 | 0.4984 | 0.6519 | 0.9539 |
| new | concave | tp_share_raw | 188 | 0.6110 | 0.5001 | 0.5881 | 0.7075 | 0.9436 |
| new | concave | hhi | 173 | 0.3026 | 0.2061 | 0.2708 | 0.3818 | 0.5002 |
| new | concave | n_material | 193 | 5.9223 | 3.0000 | 6.0000 | 8.0000 | 10.0000 |
| new | concave | mean_abs_third | 193 | 0.0014 | 0.0005 | 0.0012 | 0.0024 | 0.0031 |
| new | concave | mean_abs_third_raw | 193 | 0.0018 | 0.0008 | 0.0015 | 0.0028 | 0.0036 |
| new | convex | tp_share | 164 | 0.4931 | 0.3441 | 0.4675 | 0.6448 | 0.9472 |
| new | convex | tp_share_raw | 182 | 0.6110 | 0.5000 | 0.5545 | 0.7175 | 0.9228 |
| new | convex | hhi | 164 | 0.3986 | 0.2478 | 0.3377 | 0.4692 | 0.7346 |
| new | convex | n_material | 193 | 4.6632 | 2.0000 | 5.0000 | 7.0000 | 9.0000 |
| new | convex | mean_abs_third | 193 | 0.0012 | 0.0001 | 0.0007 | 0.0019 | 0.0030 |
| new | convex | mean_abs_third_raw | 193 | 0.0015 | 0.0004 | 0.0011 | 0.0022 | 0.0033 |
| new | top3_stress | tp_share | 149 | 0.4346 | 0.2248 | 0.4188 | 0.5344 | 1.0000 |
| new | top3_stress | tp_share_raw | 164 | 0.5919 | 0.4975 | 0.5079 | 0.6447 | 0.9654 |
| new | top3_stress | hhi | 149 | 0.5086 | 0.3221 | 0.4300 | 0.5668 | 1.0000 |
| new | top3_stress | n_material | 193 | 2.5440 | 1.0000 | 2.0000 | 4.0000 | 6.0000 |
| new | top3_stress | mean_abs_third | 193 | 0.0004 | 0.0000 | 0.0002 | 0.0006 | 0.0013 |
| new | top3_stress | mean_abs_third_raw | 193 | 0.0006 | 0.0002 | 0.0004 | 0.0008 | 0.0014 |
| new_minus_old | linear | tp_share | 171 | -0.0164 | -0.1209 | -0.0005 | 0.0541 | 0.1578 |
| new_minus_old | linear | hhi | 171 | 0.0189 | -0.0423 | 0.0010 | 0.0797 | 0.1621 |
| new_minus_old | linear | mean_abs_third | 193 | -0.0002 | -0.0007 | 0.0000 | 0.0004 | 0.0011 |
| new_minus_old | concave | tp_share | 172 | -0.0402 | -0.1424 | -0.0013 | 0.0438 | 0.1483 |
| new_minus_old | concave | hhi | 172 | 0.0062 | -0.0474 | -0.0046 | 0.0564 | 0.1464 |
| new_minus_old | concave | mean_abs_third | 193 | -0.0002 | -0.0007 | 0.0000 | 0.0004 | 0.0011 |
| new_minus_old | convex | tp_share | 164 | -0.0203 | -0.1348 | 0.0000 | 0.0863 | 0.1966 |
| new_minus_old | convex | hhi | 164 | 0.0434 | -0.0836 | -0.0002 | 0.0939 | 0.2783 |
| new_minus_old | convex | mean_abs_third | 193 | 0.0001 | -0.0006 | 0.0000 | 0.0006 | 0.0013 |
| new_minus_old | top3_stress | tp_share | 104 | 0.1246 | -0.0678 | 0.0819 | 0.3847 | 0.4854 |
| new_minus_old | top3_stress | hhi | 104 | -0.1633 | -0.5734 | -0.1043 | 0.0878 | 0.3047 |
| new_minus_old | top3_stress | mean_abs_third | 193 | 0.0002 | -0.0002 | 0.0000 | 0.0005 | 0.0010 |

## H2

| curve | sample | n_games | mean_diff_new_minus_old | lo99 | hi99 | registered | supported |
|---|---|---|---|---|---|---|---|
| linear | registered | 168 | -0.0002 | -0.0003 | 0.0000 | True | False |
| linear | state_conditional | 148 | -0.0002 | -0.0004 | 0.0000 | False | False |
| concave | registered | 168 | -0.0002 | -0.0004 | 0.0000 | False | False |
| concave | state_conditional | 148 | -0.0002 | -0.0004 | 0.0000 | False | False |
| convex | registered | 168 | 0.0001 | -0.0001 | 0.0002 | False | False |
| convex | state_conditional | 148 | 0.0001 | -0.0001 | 0.0003 | False | False |
| top3_stress | registered | 168 | 0.0002 | 0.0002 | 0.0003 | False | True |
| top3_stress | state_conditional | 148 | 0.0003 | 0.0002 | 0.0004 | False | True |

## F5_2_network_edges

1740 rows in `F5_2_network_edges.csv`.

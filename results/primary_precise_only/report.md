# Registered analysis output

tag `primary`; exclude_imprecise=True; states=163

## T5_0_diagnostics

| states | games | stopped_2000 | stopped_8000 | stopped_32000 | missed_target | n_worlds_match | max_halfwidth_linear | max_halfwidth_linear_rules_only | max_halfwidth_delta_linear | p95_halfwidth_linear | max_q_total_dev | max_per_slot_dev | per_slot_noise_scale | max_own_slot_dev | max_zero_sum_dev |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 163 | 1154 | 3 | 20 | 140 | 0 | 2000 | 0.0034 | 0.0034 | 0.0032 | 0.0031 | 0.0000 | 0.0116 | 0.0112 | 0.0000 | 0.0068 |

## T5_0b_zero_sum_by_curve

| curve | rule | max_zero_sum_dev | mean_zero_sum_dev | n_games |
|---|---|---|---|---|
| linear | old | 0.0012 | 0.0001 | 1154 |
| linear | new | 0.0017 | 0.0001 | 1154 |
| concave | old | 0.0007 | 0.0001 | 1154 |
| concave | new | 0.0010 | 0.0001 | 1154 |
| convex | old | 0.0020 | 0.0002 | 1154 |
| convex | new | 0.0025 | 0.0002 | 1154 |
| top3_stress | old | 0.0068 | 0.0004 | 1154 |
| top3_stress | new | 0.0053 | 0.0003 | 1154 |

## T5_0c_verdict_by_look

| rule | portfolio | stopped_at | verdict_B | verdict_B_pm | count |
|---|---|---|---|---|---|
| delta | actual | 2000 | dominance_positive | dominance_positive | 1 |
| delta | actual | 2000 | negligible | negligible | 3 |
| delta | actual | 2000 | reversal | reversal | 7 |
| delta | actual | 2000 | unresolved | unresolved | 1 |
| delta | actual | 32000 | dominance_positive | dominance_positive | 117 |
| delta | actual | 32000 | dominance_positive | unresolved | 111 |
| delta | actual | 32000 | negligible | dominance_positive | 1 |
| delta | actual | 32000 | negligible | negligible | 605 |
| delta | actual | 32000 | negligible | unresolved | 49 |
| delta | actual | 32000 | reversal | reversal | 993 |
| delta | actual | 32000 | reversal | unresolved | 142 |
| delta | actual | 32000 | unresolved | unresolved | 68 |
| delta | actual | 8000 | dominance_positive | dominance_positive | 5 |
| delta | actual | 8000 | dominance_positive | unresolved | 5 |
| delta | actual | 8000 | negligible | negligible | 74 |
| delta | actual | 8000 | negligible | unresolved | 8 |
| delta | actual | 8000 | reversal | reversal | 100 |
| delta | actual | 8000 | reversal | unresolved | 7 |
| delta | actual | 8000 | unresolved | unresolved | 11 |
| delta | own | 2000 | negligible | negligible | 1 |
| delta | own | 2000 | reversal | reversal | 10 |
| delta | own | 2000 | unresolved | unresolved | 1 |
| delta | own | 32000 | dominance_positive | dominance_positive | 4 |
| delta | own | 32000 | dominance_positive | unresolved | 137 |
| delta | own | 32000 | negligible | negligible | 358 |
| delta | own | 32000 | negligible | unresolved | 56 |
| delta | own | 32000 | reversal | reversal | 1158 |
| delta | own | 32000 | reversal | unresolved | 238 |
| delta | own | 32000 | unresolved | unresolved | 135 |
| delta | own | 8000 | dominance_positive | dominance_positive | 2 |
| delta | own | 8000 | dominance_positive | unresolved | 8 |
| delta | own | 8000 | negligible | negligible | 39 |
| delta | own | 8000 | negligible | unresolved | 10 |
| delta | own | 8000 | reversal | reversal | 116 |
| delta | own | 8000 | reversal | unresolved | 14 |
| delta | own | 8000 | unresolved | unresolved | 21 |
| new | actual | 2000 | dominance_positive | dominance_positive | 3 |
| new | actual | 2000 | negligible | negligible | 3 |
| new | actual | 2000 | reversal | reversal | 5 |
| new | actual | 2000 | unresolved | unresolved | 1 |
| new | actual | 32000 | dominance_positive | dominance_positive | 1131 |
| new | actual | 32000 | dominance_positive | unresolved | 60 |
| new | actual | 32000 | negligible | dominance_positive | 20 |
| new | actual | 32000 | negligible | negligible | 494 |
| new | actual | 32000 | negligible | unresolved | 36 |
| new | actual | 32000 | reversal | reversal | 231 |
| new | actual | 32000 | reversal | unresolved | 52 |
| new | actual | 32000 | unresolved | unresolved | 62 |
| new | actual | 8000 | dominance_positive | dominance_positive | 113 |
| new | actual | 8000 | dominance_positive | unresolved | 3 |
| new | actual | 8000 | negligible | dominance_positive | 2 |
| new | actual | 8000 | negligible | negligible | 55 |
| new | actual | 8000 | negligible | unresolved | 1 |
| new | actual | 8000 | reversal | reversal | 26 |
| new | actual | 8000 | reversal | unresolved | 3 |
| new | actual | 8000 | unresolved | unresolved | 7 |
| new | own | 2000 | dominance_positive | dominance_positive | 7 |
| new | own | 2000 | reversal | reversal | 5 |
| new | own | 32000 | dominance_positive | dominance_positive | 1567 |
| new | own | 32000 | dominance_positive | unresolved | 26 |
| new | own | 32000 | negligible | dominance_positive | 27 |
| new | own | 32000 | negligible | negligible | 201 |
| new | own | 32000 | negligible | unresolved | 4 |
| new | own | 32000 | reversal | reversal | 218 |
| new | own | 32000 | reversal | unresolved | 20 |
| new | own | 32000 | unresolved | unresolved | 23 |
| new | own | 8000 | dominance_positive | dominance_positive | 159 |
| new | own | 8000 | negligible | dominance_positive | 2 |
| new | own | 8000 | negligible | negligible | 21 |
| new | own | 8000 | reversal | reversal | 26 |
| new | own | 8000 | reversal | unresolved | 1 |
| new | own | 8000 | unresolved | unresolved | 1 |
| old | actual | 2000 | dominance_positive | dominance_positive | 7 |
| old | actual | 2000 | negligible | negligible | 3 |
| old | actual | 2000 | reversal | reversal | 1 |
| old | actual | 2000 | unresolved | unresolved | 1 |
| old | actual | 32000 | dominance_positive | dominance_positive | 1425 |
| old | actual | 32000 | dominance_positive | unresolved | 120 |
| old | actual | 32000 | negligible | dominance_positive | 4 |
| old | actual | 32000 | negligible | negligible | 427 |
| old | actual | 32000 | negligible | unresolved | 13 |
| old | actual | 32000 | reversal | reversal | 39 |
| old | actual | 32000 | reversal | unresolved | 23 |
| old | actual | 32000 | unresolved | unresolved | 35 |
| old | actual | 8000 | dominance_positive | dominance_positive | 144 |
| old | actual | 8000 | dominance_positive | unresolved | 11 |
| old | actual | 8000 | negligible | negligible | 47 |
| old | actual | 8000 | reversal | reversal | 3 |
| old | actual | 8000 | unresolved | unresolved | 5 |
| old | own | 2000 | dominance_positive | dominance_positive | 12 |
| old | own | 32000 | dominance_positive | dominance_positive | 2033 |
| old | own | 32000 | dominance_positive | unresolved | 23 |
| old | own | 32000 | negligible | dominance_positive | 1 |
| old | own | 32000 | negligible | negligible | 27 |
| old | own | 32000 | negligible | unresolved | 2 |
| old | own | 8000 | dominance_positive | dominance_positive | 204 |
| old | own | 8000 | dominance_positive | unresolved | 2 |
| old | own | 8000 | negligible | negligible | 3 |
| old | own | 8000 | unresolved | unresolved | 1 |

## T5_0d_band_width

| rule | portfolio | measure | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| old | actual | band_ratio | 2308 | 1.5033 | 0.2862 | 1.3634 | 2.4673 | 2.8847 |
| old | actual | band_ratio_pm | 2308 | 5.4616 | 1.1141 | 5.2911 | 9.6696 | 10.9553 |
| old | own | band_ratio | 2308 | 2.1213 | 1.1658 | 2.3201 | 2.6989 | 3.1519 |
| old | own | band_ratio_pm | 2308 | 7.6880 | 3.9744 | 9.0738 | 10.5047 | 11.6158 |
| new | actual | band_ratio | 2308 | 1.1944 | 0.1294 | 0.7257 | 2.2676 | 2.7042 |
| new | actual | band_ratio_pm | 2308 | 4.3374 | 0.4797 | 2.6889 | 8.8389 | 10.4720 |
| new | own | band_ratio | 2308 | 1.7044 | 0.3356 | 2.0475 | 2.5562 | 2.9463 |
| new | own | band_ratio_pm | 2308 | 6.1730 | 1.2861 | 7.9942 | 9.9979 | 11.1407 |
| delta | actual | band_ratio | 2308 | 1.0844 | 0.0652 | 0.7182 | 1.8147 | 2.6830 |
| delta | actual | band_ratio_pm | 2308 | 3.9824 | 0.2551 | 2.6880 | 6.8504 | 10.1201 |
| delta | own | band_ratio | 2308 | 1.3860 | 0.4609 | 1.0934 | 2.2674 | 2.8390 |
| delta | own | band_ratio_pm | 2308 | 5.0598 | 1.7975 | 3.8713 | 8.7160 | 10.7990 |

## T5_1_verdicts

| rule | portfolio | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|
| old | actual | B | dominance_positive | 0.7396 | 0.6085 | 0.8199 | 2308 |
| old | actual | B | reversal | 0.0286 | 0.0127 | 0.0680 | 2308 |
| old | actual | B | negligible | 0.2140 | 0.1472 | 0.3090 | 2308 |
| old | actual | B | unresolved | 0.0178 | 0.0085 | 0.0303 | 2308 |
| old | actual | C | dominance_positive | 0.7396 | 0.6085 | 0.8199 | 2308 |
| old | actual | C | reversal | 0.0286 | 0.0127 | 0.0680 | 2308 |
| old | actual | C | negligible | 0.2140 | 0.1472 | 0.3090 | 2308 |
| old | actual | C | unresolved | 0.0178 | 0.0085 | 0.0303 | 2308 |
| old | actual | B_pm | dominance_positive | 0.6846 | 0.5655 | 0.7636 | 2308 |
| old | actual | B_pm | reversal | 0.0186 | 0.0067 | 0.0439 | 2308 |
| old | actual | B_pm | negligible | 0.2067 | 0.1440 | 0.2983 | 2308 |
| old | actual | B_pm | unresolved | 0.0901 | 0.0690 | 0.1176 | 2308 |
| old | actual | C_pm | dominance_positive | 0.6846 | 0.5655 | 0.7636 | 2308 |
| old | actual | C_pm | reversal | 0.0186 | 0.0067 | 0.0439 | 2308 |
| old | actual | C_pm | negligible | 0.2067 | 0.1440 | 0.2983 | 2308 |
| old | actual | C_pm | unresolved | 0.0901 | 0.0690 | 0.1176 | 2308 |
| old | own | B | dominance_positive | 0.9853 | 0.9676 | 0.9981 | 2308 |
| old | own | B | reversal | 0.0000 | 0.0000 | 0.0000 | 2308 |
| old | own | B | negligible | 0.0143 | 0.0018 | 0.0316 | 2308 |
| old | own | B | unresolved | 0.0004 | 0.0000 | 0.0030 | 2308 |
| old | own | C | dominance_positive | 0.9853 | 0.9676 | 0.9981 | 2308 |
| old | own | C | reversal | 0.0000 | 0.0000 | 0.0000 | 2308 |
| old | own | C | negligible | 0.0143 | 0.0018 | 0.0316 | 2308 |
| old | own | C | unresolved | 0.0004 | 0.0000 | 0.0030 | 2308 |
| old | own | B_pm | dominance_positive | 0.9749 | 0.9465 | 0.9952 | 2308 |
| old | own | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 2308 |
| old | own | B_pm | negligible | 0.0130 | 0.0016 | 0.0284 | 2308 |
| old | own | B_pm | unresolved | 0.0121 | 0.0005 | 0.0297 | 2308 |
| old | own | C_pm | dominance_positive | 0.9749 | 0.9465 | 0.9952 | 2308 |
| old | own | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 2308 |
| old | own | C_pm | negligible | 0.0130 | 0.0016 | 0.0284 | 2308 |
| old | own | C_pm | unresolved | 0.0121 | 0.0005 | 0.0297 | 2308 |
| new | actual | B | dominance_positive | 0.5676 | 0.4467 | 0.6559 | 2308 |
| new | actual | B | reversal | 0.1373 | 0.0814 | 0.1770 | 2308 |
| new | actual | B | negligible | 0.2647 | 0.1784 | 0.3699 | 2308 |
| new | actual | B | unresolved | 0.0303 | 0.0178 | 0.0482 | 2308 |
| new | actual | C | dominance_positive | 0.5680 | 0.4467 | 0.6569 | 2308 |
| new | actual | C | reversal | 0.1373 | 0.0814 | 0.1770 | 2308 |
| new | actual | C | negligible | 0.2647 | 0.1784 | 0.3699 | 2308 |
| new | actual | C | unresolved | 0.0299 | 0.0175 | 0.0481 | 2308 |
| new | actual | B_pm | dominance_positive | 0.5498 | 0.4164 | 0.6359 | 2308 |
| new | actual | B_pm | reversal | 0.1135 | 0.0691 | 0.1482 | 2308 |
| new | actual | B_pm | negligible | 0.2392 | 0.1662 | 0.3449 | 2308 |
| new | actual | B_pm | unresolved | 0.0975 | 0.0661 | 0.1517 | 2308 |
| new | actual | C_pm | dominance_positive | 0.5507 | 0.4164 | 0.6383 | 2308 |
| new | actual | C_pm | reversal | 0.1131 | 0.0691 | 0.1480 | 2308 |
| new | actual | C_pm | negligible | 0.2392 | 0.1662 | 0.3449 | 2308 |
| new | actual | C_pm | unresolved | 0.0971 | 0.0654 | 0.1517 | 2308 |
| new | own | B | dominance_positive | 0.7621 | 0.6918 | 0.8207 | 2308 |
| new | own | B | reversal | 0.1170 | 0.0679 | 0.1522 | 2308 |
| new | own | B | negligible | 0.1105 | 0.0583 | 0.1731 | 2308 |
| new | own | B | unresolved | 0.0104 | 0.0044 | 0.0176 | 2308 |
| new | own | C | dominance_positive | 0.7621 | 0.6918 | 0.8207 | 2308 |
| new | own | C | reversal | 0.1170 | 0.0679 | 0.1522 | 2308 |
| new | own | C | negligible | 0.1105 | 0.0583 | 0.1731 | 2308 |
| new | own | C | unresolved | 0.0104 | 0.0044 | 0.0176 | 2308 |
| new | own | B_pm | dominance_positive | 0.7634 | 0.6939 | 0.8185 | 2308 |
| new | own | B_pm | reversal | 0.1079 | 0.0639 | 0.1427 | 2308 |
| new | own | B_pm | negligible | 0.0962 | 0.0482 | 0.1581 | 2308 |
| new | own | B_pm | unresolved | 0.0325 | 0.0161 | 0.0484 | 2308 |
| new | own | C_pm | dominance_positive | 0.7634 | 0.6939 | 0.8185 | 2308 |
| new | own | C_pm | reversal | 0.1079 | 0.0639 | 0.1427 | 2308 |
| new | own | C_pm | negligible | 0.0962 | 0.0482 | 0.1581 | 2308 |
| new | own | C_pm | unresolved | 0.0325 | 0.0161 | 0.0484 | 2308 |
| delta | actual | B | dominance_positive | 0.1036 | 0.0625 | 0.1465 | 2308 |
| delta | actual | B | reversal | 0.5412 | 0.4718 | 0.6101 | 2308 |
| delta | actual | B | negligible | 0.3206 | 0.2921 | 0.3625 | 2308 |
| delta | actual | B | unresolved | 0.0347 | 0.0217 | 0.0564 | 2308 |
| delta | actual | C | dominance_positive | 0.1036 | 0.0625 | 0.1465 | 2308 |
| delta | actual | C | reversal | 0.5412 | 0.4718 | 0.6101 | 2308 |
| delta | actual | C | negligible | 0.3206 | 0.2921 | 0.3625 | 2308 |
| delta | actual | C | unresolved | 0.0347 | 0.0217 | 0.0564 | 2308 |
| delta | actual | B_pm | dominance_positive | 0.0537 | 0.0296 | 0.0882 | 2308 |
| delta | actual | B_pm | reversal | 0.4766 | 0.4177 | 0.5330 | 2308 |
| delta | actual | B_pm | negligible | 0.2955 | 0.2724 | 0.3278 | 2308 |
| delta | actual | B_pm | unresolved | 0.1742 | 0.1306 | 0.2248 | 2308 |
| delta | actual | C_pm | dominance_positive | 0.0537 | 0.0296 | 0.0882 | 2308 |
| delta | actual | C_pm | reversal | 0.4766 | 0.4177 | 0.5330 | 2308 |
| delta | actual | C_pm | negligible | 0.2955 | 0.2724 | 0.3278 | 2308 |
| delta | actual | C_pm | unresolved | 0.1742 | 0.1306 | 0.2248 | 2308 |
| delta | own | B | dominance_positive | 0.0654 | 0.0422 | 0.0891 | 2308 |
| delta | own | B | reversal | 0.6655 | 0.6279 | 0.6956 | 2308 |
| delta | own | B | negligible | 0.2010 | 0.1699 | 0.2362 | 2308 |
| delta | own | B | unresolved | 0.0680 | 0.0510 | 0.0897 | 2308 |
| delta | own | C | dominance_positive | 0.0654 | 0.0422 | 0.0891 | 2308 |
| delta | own | C | reversal | 0.6655 | 0.6279 | 0.6956 | 2308 |
| delta | own | C | negligible | 0.2010 | 0.1699 | 0.2362 | 2308 |
| delta | own | C | unresolved | 0.0680 | 0.0510 | 0.0897 | 2308 |
| delta | own | B_pm | dominance_positive | 0.0026 | 0.0000 | 0.0072 | 2308 |
| delta | own | B_pm | reversal | 0.5563 | 0.4974 | 0.6064 | 2308 |
| delta | own | B_pm | negligible | 0.1724 | 0.1367 | 0.2128 | 2308 |
| delta | own | B_pm | unresolved | 0.2686 | 0.2225 | 0.3245 | 2308 |
| delta | own | C_pm | dominance_positive | 0.0026 | 0.0000 | 0.0072 | 2308 |
| delta | own | C_pm | reversal | 0.5563 | 0.4974 | 0.6064 | 2308 |
| delta | own | C_pm | negligible | 0.1724 | 0.1367 | 0.2128 | 2308 |
| delta | own | C_pm | unresolved | 0.2686 | 0.2225 | 0.3245 | 2308 |

## T5_2_verdicts_by_band

| rule | portfolio | band | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| old | actual | 1-3 | B | dominance_positive | 0.7763 | 0.6149 | 0.9240 | 228 |
| old | actual | 1-3 | B | reversal | 0.0482 | 0.0000 | 0.1107 | 228 |
| old | actual | 1-3 | B | negligible | 0.0833 | 0.0000 | 0.1973 | 228 |
| old | actual | 1-3 | B | unresolved | 0.0921 | 0.0161 | 0.1625 | 228 |
| old | actual | 1-3 | C | dominance_positive | 0.7763 | 0.6149 | 0.9240 | 228 |
| old | actual | 1-3 | C | reversal | 0.0482 | 0.0000 | 0.1107 | 228 |
| old | actual | 1-3 | C | negligible | 0.0833 | 0.0000 | 0.1973 | 228 |
| old | actual | 1-3 | C | unresolved | 0.0921 | 0.0161 | 0.1625 | 228 |
| old | actual | 1-3 | B_pm | dominance_positive | 0.5395 | 0.2725 | 0.8158 | 228 |
| old | actual | 1-3 | B_pm | reversal | 0.0351 | 0.0000 | 0.0862 | 228 |
| old | actual | 1-3 | B_pm | negligible | 0.0833 | 0.0000 | 0.1973 | 228 |
| old | actual | 1-3 | B_pm | unresolved | 0.3421 | 0.1382 | 0.4966 | 228 |
| old | actual | 1-3 | C_pm | dominance_positive | 0.5395 | 0.2725 | 0.8158 | 228 |
| old | actual | 1-3 | C_pm | reversal | 0.0351 | 0.0000 | 0.0862 | 228 |
| old | actual | 1-3 | C_pm | negligible | 0.0833 | 0.0000 | 0.1973 | 228 |
| old | actual | 1-3 | C_pm | unresolved | 0.3421 | 0.1382 | 0.4966 | 228 |
| old | actual | 4-10 | B | dominance_positive | 0.8989 | 0.8067 | 0.9699 | 564 |
| old | actual | 4-10 | B | reversal | 0.0266 | 0.0053 | 0.0609 | 564 |
| old | actual | 4-10 | B | negligible | 0.0603 | 0.0102 | 0.1438 | 564 |
| old | actual | 4-10 | B | unresolved | 0.0142 | 0.0000 | 0.0404 | 564 |
| old | actual | 4-10 | C | dominance_positive | 0.8989 | 0.8067 | 0.9699 | 564 |
| old | actual | 4-10 | C | reversal | 0.0266 | 0.0053 | 0.0609 | 564 |
| old | actual | 4-10 | C | negligible | 0.0603 | 0.0102 | 0.1438 | 564 |
| old | actual | 4-10 | C | unresolved | 0.0142 | 0.0000 | 0.0404 | 564 |
| old | actual | 4-10 | B_pm | dominance_positive | 0.8121 | 0.6646 | 0.9213 | 564 |
| old | actual | 4-10 | B_pm | reversal | 0.0124 | 0.0000 | 0.0296 | 564 |
| old | actual | 4-10 | B_pm | negligible | 0.0585 | 0.0095 | 0.1402 | 564 |
| old | actual | 4-10 | B_pm | unresolved | 0.1170 | 0.0526 | 0.1987 | 564 |
| old | actual | 4-10 | C_pm | dominance_positive | 0.8121 | 0.6646 | 0.9213 | 564 |
| old | actual | 4-10 | C_pm | reversal | 0.0124 | 0.0000 | 0.0296 | 564 |
| old | actual | 4-10 | C_pm | negligible | 0.0585 | 0.0095 | 0.1402 | 564 |
| old | actual | 4-10 | C_pm | unresolved | 0.1170 | 0.0526 | 0.1987 | 564 |
| old | actual | 11-16 | B | dominance_positive | 0.7631 | 0.5690 | 0.9183 | 439 |
| old | actual | 11-16 | B | reversal | 0.0296 | 0.0026 | 0.0949 | 439 |
| old | actual | 11-16 | B | negligible | 0.1913 | 0.0595 | 0.3535 | 439 |
| old | actual | 11-16 | B | unresolved | 0.0159 | 0.0000 | 0.0630 | 439 |
| old | actual | 11-16 | C | dominance_positive | 0.7631 | 0.5690 | 0.9183 | 439 |
| old | actual | 11-16 | C | reversal | 0.0296 | 0.0026 | 0.0949 | 439 |
| old | actual | 11-16 | C | negligible | 0.1913 | 0.0595 | 0.3535 | 439 |
| old | actual | 11-16 | C | unresolved | 0.0159 | 0.0000 | 0.0630 | 439 |
| old | actual | 11-16 | B_pm | dominance_positive | 0.7449 | 0.5452 | 0.9109 | 439 |
| old | actual | 11-16 | B_pm | reversal | 0.0182 | 0.0000 | 0.0526 | 439 |
| old | actual | 11-16 | B_pm | negligible | 0.1800 | 0.0576 | 0.3342 | 439 |
| old | actual | 11-16 | B_pm | unresolved | 0.0569 | 0.0085 | 0.1459 | 439 |
| old | actual | 11-16 | C_pm | dominance_positive | 0.7449 | 0.5452 | 0.9109 | 439 |
| old | actual | 11-16 | C_pm | reversal | 0.0182 | 0.0000 | 0.0526 | 439 |
| old | actual | 11-16 | C_pm | negligible | 0.1800 | 0.0576 | 0.3342 | 439 |
| old | actual | 11-16 | C_pm | unresolved | 0.0569 | 0.0085 | 0.1459 | 439 |
| old | actual | 17-30 | B | dominance_positive | 0.6388 | 0.3759 | 0.7670 | 1077 |
| old | actual | 17-30 | B | reversal | 0.0251 | 0.0024 | 0.0904 | 1077 |
| old | actual | 17-30 | B | negligible | 0.3315 | 0.2257 | 0.5318 | 1077 |
| old | actual | 17-30 | B | unresolved | 0.0046 | 0.0000 | 0.0155 | 1077 |
| old | actual | 17-30 | C | dominance_positive | 0.6388 | 0.3759 | 0.7670 | 1077 |
| old | actual | 17-30 | C | reversal | 0.0251 | 0.0024 | 0.0904 | 1077 |
| old | actual | 17-30 | C | negligible | 0.3315 | 0.2257 | 0.5318 | 1077 |
| old | actual | 17-30 | C | unresolved | 0.0046 | 0.0000 | 0.0155 | 1077 |
| old | actual | 17-30 | B_pm | dominance_positive | 0.6240 | 0.3464 | 0.7622 | 1077 |
| old | actual | 17-30 | B_pm | reversal | 0.0186 | 0.0011 | 0.0656 | 1077 |
| old | actual | 17-30 | B_pm | negligible | 0.3213 | 0.2186 | 0.5221 | 1077 |
| old | actual | 17-30 | B_pm | unresolved | 0.0362 | 0.0098 | 0.0839 | 1077 |
| old | actual | 17-30 | C_pm | dominance_positive | 0.6240 | 0.3464 | 0.7622 | 1077 |
| old | actual | 17-30 | C_pm | reversal | 0.0186 | 0.0011 | 0.0656 | 1077 |
| old | actual | 17-30 | C_pm | negligible | 0.3213 | 0.2186 | 0.5221 | 1077 |
| old | actual | 17-30 | C_pm | unresolved | 0.0362 | 0.0098 | 0.0839 | 1077 |
| old | own | 1-3 | B | dominance_positive | 0.9825 | 0.9405 | 1.0000 | 228 |
| old | own | 1-3 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 228 |
| old | own | 1-3 | B | negligible | 0.0175 | 0.0000 | 0.0595 | 228 |
| old | own | 1-3 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 228 |
| old | own | 1-3 | C | dominance_positive | 0.9825 | 0.9405 | 1.0000 | 228 |
| old | own | 1-3 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 228 |
| old | own | 1-3 | C | negligible | 0.0175 | 0.0000 | 0.0595 | 228 |
| old | own | 1-3 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 228 |
| old | own | 1-3 | B_pm | dominance_positive | 0.9825 | 0.9405 | 1.0000 | 228 |
| old | own | 1-3 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 228 |
| old | own | 1-3 | B_pm | negligible | 0.0175 | 0.0000 | 0.0595 | 228 |
| old | own | 1-3 | B_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 228 |
| old | own | 1-3 | C_pm | dominance_positive | 0.9825 | 0.9405 | 1.0000 | 228 |
| old | own | 1-3 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 228 |
| old | own | 1-3 | C_pm | negligible | 0.0175 | 0.0000 | 0.0595 | 228 |
| old | own | 1-3 | C_pm | unresolved | 0.0000 | 0.0000 | 0.0000 | 228 |
| old | own | 4-10 | B | dominance_positive | 0.9858 | 0.9472 | 1.0000 | 564 |
| old | own | 4-10 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 564 |
| old | own | 4-10 | B | negligible | 0.0124 | 0.0000 | 0.0513 | 564 |
| old | own | 4-10 | B | unresolved | 0.0018 | 0.0000 | 0.0121 | 564 |
| old | own | 4-10 | C | dominance_positive | 0.9858 | 0.9472 | 1.0000 | 564 |
| old | own | 4-10 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 564 |
| old | own | 4-10 | C | negligible | 0.0124 | 0.0000 | 0.0513 | 564 |
| old | own | 4-10 | C | unresolved | 0.0018 | 0.0000 | 0.0121 | 564 |
| old | own | 4-10 | B_pm | dominance_positive | 0.9734 | 0.9233 | 0.9986 | 564 |
| old | own | 4-10 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 564 |
| old | own | 4-10 | B_pm | negligible | 0.0106 | 0.0000 | 0.0421 | 564 |
| old | own | 4-10 | B_pm | unresolved | 0.0160 | 0.0000 | 0.0625 | 564 |
| old | own | 4-10 | C_pm | dominance_positive | 0.9734 | 0.9233 | 0.9986 | 564 |
| old | own | 4-10 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 564 |
| old | own | 4-10 | C_pm | negligible | 0.0106 | 0.0000 | 0.0421 | 564 |
| old | own | 4-10 | C_pm | unresolved | 0.0160 | 0.0000 | 0.0625 | 564 |
| old | own | 11-16 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 439 |
| old | own | 11-16 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 439 |
| old | own | 11-16 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 439 |
| old | own | 11-16 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 439 |
| old | own | 11-16 | C | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 439 |
| old | own | 11-16 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 439 |
| old | own | 11-16 | C | negligible | 0.0000 | 0.0000 | 0.0000 | 439 |
| old | own | 11-16 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 439 |
| old | own | 11-16 | B_pm | dominance_positive | 0.9818 | 0.9475 | 1.0000 | 439 |
| old | own | 11-16 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 439 |
| old | own | 11-16 | B_pm | negligible | 0.0000 | 0.0000 | 0.0000 | 439 |
| old | own | 11-16 | B_pm | unresolved | 0.0182 | 0.0000 | 0.0525 | 439 |
| old | own | 11-16 | C_pm | dominance_positive | 0.9818 | 0.9475 | 1.0000 | 439 |
| old | own | 11-16 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 439 |
| old | own | 11-16 | C_pm | negligible | 0.0000 | 0.0000 | 0.0000 | 439 |
| old | own | 11-16 | C_pm | unresolved | 0.0182 | 0.0000 | 0.0525 | 439 |
| old | own | 17-30 | B | dominance_positive | 0.9796 | 0.9409 | 1.0000 | 1077 |
| old | own | 17-30 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 1077 |
| old | own | 17-30 | B | negligible | 0.0204 | 0.0000 | 0.0591 | 1077 |
| old | own | 17-30 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 1077 |
| old | own | 17-30 | C | dominance_positive | 0.9796 | 0.9409 | 1.0000 | 1077 |
| old | own | 17-30 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 1077 |
| old | own | 17-30 | C | negligible | 0.0204 | 0.0000 | 0.0591 | 1077 |
| old | own | 17-30 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 1077 |
| old | own | 17-30 | B_pm | dominance_positive | 0.9712 | 0.9286 | 0.9990 | 1077 |
| old | own | 17-30 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 1077 |
| old | own | 17-30 | B_pm | negligible | 0.0186 | 0.0000 | 0.0527 | 1077 |
| old | own | 17-30 | B_pm | unresolved | 0.0102 | 0.0009 | 0.0235 | 1077 |
| old | own | 17-30 | C_pm | dominance_positive | 0.9712 | 0.9286 | 0.9990 | 1077 |
| old | own | 17-30 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 1077 |
| old | own | 17-30 | C_pm | negligible | 0.0186 | 0.0000 | 0.0527 | 1077 |
| old | own | 17-30 | C_pm | unresolved | 0.0102 | 0.0009 | 0.0235 | 1077 |
| new | actual | 1-3 | B | dominance_positive | 0.0702 | 0.0166 | 0.1771 | 228 |
| new | actual | 1-3 | B | reversal | 0.6096 | 0.3275 | 0.8235 | 228 |
| new | actual | 1-3 | B | negligible | 0.1930 | 0.0486 | 0.3851 | 228 |
| new | actual | 1-3 | B | unresolved | 0.1272 | 0.0652 | 0.2126 | 228 |
| new | actual | 1-3 | C | dominance_positive | 0.0702 | 0.0166 | 0.1771 | 228 |
| new | actual | 1-3 | C | reversal | 0.6096 | 0.3275 | 0.8235 | 228 |
| new | actual | 1-3 | C | negligible | 0.1930 | 0.0486 | 0.3851 | 228 |
| new | actual | 1-3 | C | unresolved | 0.1272 | 0.0652 | 0.2126 | 228 |
| new | actual | 1-3 | B_pm | dominance_positive | 0.0702 | 0.0070 | 0.2098 | 228 |
| new | actual | 1-3 | B_pm | reversal | 0.5088 | 0.2930 | 0.6683 | 228 |
| new | actual | 1-3 | B_pm | negligible | 0.1491 | 0.0338 | 0.3118 | 228 |
| new | actual | 1-3 | B_pm | unresolved | 0.2719 | 0.1850 | 0.3641 | 228 |
| new | actual | 1-3 | C_pm | dominance_positive | 0.0702 | 0.0070 | 0.2098 | 228 |
| new | actual | 1-3 | C_pm | reversal | 0.5088 | 0.2930 | 0.6683 | 228 |
| new | actual | 1-3 | C_pm | negligible | 0.1491 | 0.0338 | 0.3118 | 228 |
| new | actual | 1-3 | C_pm | unresolved | 0.2719 | 0.1850 | 0.3641 | 228 |
| new | actual | 4-10 | B | dominance_positive | 0.4716 | 0.2373 | 0.6464 | 564 |
| new | actual | 4-10 | B | reversal | 0.2199 | 0.1438 | 0.2833 | 564 |
| new | actual | 4-10 | B | negligible | 0.2571 | 0.1126 | 0.4438 | 564 |
| new | actual | 4-10 | B | unresolved | 0.0514 | 0.0132 | 0.1194 | 564 |
| new | actual | 4-10 | C | dominance_positive | 0.4716 | 0.2373 | 0.6464 | 564 |
| new | actual | 4-10 | C | reversal | 0.2199 | 0.1438 | 0.2833 | 564 |
| new | actual | 4-10 | C | negligible | 0.2571 | 0.1126 | 0.4438 | 564 |
| new | actual | 4-10 | C | unresolved | 0.0514 | 0.0132 | 0.1194 | 564 |
| new | actual | 4-10 | B_pm | dominance_positive | 0.4379 | 0.1767 | 0.6045 | 564 |
| new | actual | 4-10 | B_pm | reversal | 0.1844 | 0.1250 | 0.2324 | 564 |
| new | actual | 4-10 | B_pm | negligible | 0.2021 | 0.0939 | 0.3365 | 564 |
| new | actual | 4-10 | B_pm | unresolved | 0.1755 | 0.0699 | 0.3099 | 564 |
| new | actual | 4-10 | C_pm | dominance_positive | 0.4379 | 0.1767 | 0.6045 | 564 |
| new | actual | 4-10 | C_pm | reversal | 0.1844 | 0.1250 | 0.2324 | 564 |
| new | actual | 4-10 | C_pm | negligible | 0.2021 | 0.0939 | 0.3365 | 564 |
| new | actual | 4-10 | C_pm | unresolved | 0.1755 | 0.0699 | 0.3099 | 564 |
| new | actual | 11-16 | B | dominance_positive | 0.7403 | 0.5274 | 0.9146 | 439 |
| new | actual | 11-16 | B | reversal | 0.0159 | 0.0000 | 0.0500 | 439 |
| new | actual | 11-16 | B | negligible | 0.2323 | 0.0760 | 0.4296 | 439 |
| new | actual | 11-16 | B | unresolved | 0.0114 | 0.0000 | 0.0341 | 439 |
| new | actual | 11-16 | C | dominance_positive | 0.7403 | 0.5274 | 0.9146 | 439 |
| new | actual | 11-16 | C | reversal | 0.0159 | 0.0000 | 0.0500 | 439 |
| new | actual | 11-16 | C | negligible | 0.2323 | 0.0760 | 0.4296 | 439 |
| new | actual | 11-16 | C | unresolved | 0.0114 | 0.0000 | 0.0341 | 439 |
| new | actual | 11-16 | B_pm | dominance_positive | 0.7267 | 0.5082 | 0.9103 | 439 |
| new | actual | 11-16 | B_pm | reversal | 0.0091 | 0.0000 | 0.0377 | 439 |
| new | actual | 11-16 | B_pm | negligible | 0.2164 | 0.0744 | 0.3964 | 439 |
| new | actual | 11-16 | B_pm | unresolved | 0.0478 | 0.0088 | 0.1136 | 439 |
| new | actual | 11-16 | C_pm | dominance_positive | 0.7267 | 0.5082 | 0.9103 | 439 |
| new | actual | 11-16 | C_pm | reversal | 0.0091 | 0.0000 | 0.0377 | 439 |
| new | actual | 11-16 | C_pm | negligible | 0.2164 | 0.0744 | 0.3964 | 439 |
| new | actual | 11-16 | C_pm | unresolved | 0.0478 | 0.0088 | 0.1136 | 439 |
| new | actual | 17-30 | B | dominance_positive | 0.6527 | 0.4568 | 0.7556 | 1077 |
| new | actual | 17-30 | B | reversal | 0.0436 | 0.0068 | 0.0972 | 1077 |
| new | actual | 17-30 | B | negligible | 0.2971 | 0.2073 | 0.4601 | 1077 |
| new | actual | 17-30 | B | unresolved | 0.0065 | 0.0009 | 0.0145 | 1077 |
| new | actual | 17-30 | C | dominance_positive | 0.6537 | 0.4568 | 0.7574 | 1077 |
| new | actual | 17-30 | C | reversal | 0.0436 | 0.0068 | 0.0972 | 1077 |
| new | actual | 17-30 | C | negligible | 0.2971 | 0.2073 | 0.4601 | 1077 |
| new | actual | 17-30 | C | unresolved | 0.0056 | 0.0000 | 0.0141 | 1077 |
| new | actual | 17-30 | B_pm | dominance_positive | 0.6379 | 0.4315 | 0.7434 | 1077 |
| new | actual | 17-30 | B_pm | reversal | 0.0353 | 0.0042 | 0.0778 | 1077 |
| new | actual | 17-30 | B_pm | negligible | 0.2869 | 0.1971 | 0.4507 | 1077 |
| new | actual | 17-30 | B_pm | unresolved | 0.0399 | 0.0206 | 0.0775 | 1077 |
| new | actual | 17-30 | C_pm | dominance_positive | 0.6397 | 0.4315 | 0.7457 | 1077 |
| new | actual | 17-30 | C_pm | reversal | 0.0344 | 0.0042 | 0.0773 | 1077 |
| new | actual | 17-30 | C_pm | negligible | 0.2869 | 0.1971 | 0.4507 | 1077 |
| new | actual | 17-30 | C_pm | unresolved | 0.0390 | 0.0189 | 0.0774 | 1077 |
| new | own | 1-3 | B | dominance_positive | 0.0658 | 0.0046 | 0.1484 | 228 |
| new | own | 1-3 | B | reversal | 0.6535 | 0.3393 | 0.8859 | 228 |
| new | own | 1-3 | B | negligible | 0.2281 | 0.0643 | 0.4857 | 228 |
| new | own | 1-3 | B | unresolved | 0.0526 | 0.0157 | 0.1128 | 228 |
| new | own | 1-3 | C | dominance_positive | 0.0658 | 0.0046 | 0.1484 | 228 |
| new | own | 1-3 | C | reversal | 0.6535 | 0.3393 | 0.8859 | 228 |
| new | own | 1-3 | C | negligible | 0.2281 | 0.0643 | 0.4857 | 228 |
| new | own | 1-3 | C | unresolved | 0.0526 | 0.0157 | 0.1128 | 228 |
| new | own | 1-3 | B_pm | dominance_positive | 0.0789 | 0.0051 | 0.2071 | 228 |
| new | own | 1-3 | B_pm | reversal | 0.5965 | 0.3233 | 0.8030 | 228 |
| new | own | 1-3 | B_pm | negligible | 0.1711 | 0.0539 | 0.3988 | 228 |
| new | own | 1-3 | B_pm | unresolved | 0.1535 | 0.0765 | 0.2255 | 228 |
| new | own | 1-3 | C_pm | dominance_positive | 0.0789 | 0.0051 | 0.2071 | 228 |
| new | own | 1-3 | C_pm | reversal | 0.5965 | 0.3233 | 0.8030 | 228 |
| new | own | 1-3 | C_pm | negligible | 0.1711 | 0.0539 | 0.3988 | 228 |
| new | own | 1-3 | C_pm | unresolved | 0.1535 | 0.0765 | 0.2255 | 228 |
| new | own | 4-10 | B | dominance_positive | 0.4645 | 0.1954 | 0.6514 | 564 |
| new | own | 4-10 | B | reversal | 0.2145 | 0.1319 | 0.2917 | 564 |
| new | own | 4-10 | B | negligible | 0.2996 | 0.1192 | 0.5210 | 564 |
| new | own | 4-10 | B | unresolved | 0.0213 | 0.0046 | 0.0390 | 564 |
| new | own | 4-10 | C | dominance_positive | 0.4645 | 0.1954 | 0.6514 | 564 |
| new | own | 4-10 | C | reversal | 0.2145 | 0.1319 | 0.2917 | 564 |
| new | own | 4-10 | C | negligible | 0.2996 | 0.1192 | 0.5210 | 564 |
| new | own | 4-10 | C | unresolved | 0.0213 | 0.0046 | 0.0390 | 564 |
| new | own | 4-10 | B_pm | dominance_positive | 0.4823 | 0.2146 | 0.6535 | 564 |
| new | own | 4-10 | B_pm | reversal | 0.2004 | 0.1184 | 0.2778 | 564 |
| new | own | 4-10 | B_pm | negligible | 0.2713 | 0.1010 | 0.4990 | 564 |
| new | own | 4-10 | B_pm | unresolved | 0.0461 | 0.0111 | 0.0731 | 564 |
| new | own | 4-10 | C_pm | dominance_positive | 0.4823 | 0.2146 | 0.6535 | 564 |
| new | own | 4-10 | C_pm | reversal | 0.2004 | 0.1184 | 0.2778 | 564 |
| new | own | 4-10 | C_pm | negligible | 0.2713 | 0.1010 | 0.4990 | 564 |
| new | own | 4-10 | C_pm | unresolved | 0.0461 | 0.0111 | 0.0731 | 564 |
| new | own | 11-16 | B | dominance_positive | 0.9727 | 0.9180 | 1.0000 | 439 |
| new | own | 11-16 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 439 |
| new | own | 11-16 | B | negligible | 0.0273 | 0.0000 | 0.0820 | 439 |
| new | own | 11-16 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 439 |
| new | own | 11-16 | C | dominance_positive | 0.9727 | 0.9180 | 1.0000 | 439 |
| new | own | 11-16 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 439 |
| new | own | 11-16 | C | negligible | 0.0273 | 0.0000 | 0.0820 | 439 |
| new | own | 11-16 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 439 |
| new | own | 11-16 | B_pm | dominance_positive | 0.9681 | 0.9049 | 1.0000 | 439 |
| new | own | 11-16 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 439 |
| new | own | 11-16 | B_pm | negligible | 0.0228 | 0.0000 | 0.0664 | 439 |
| new | own | 11-16 | B_pm | unresolved | 0.0091 | 0.0000 | 0.0376 | 439 |
| new | own | 11-16 | C_pm | dominance_positive | 0.9681 | 0.9049 | 1.0000 | 439 |
| new | own | 11-16 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 439 |
| new | own | 11-16 | C_pm | negligible | 0.0228 | 0.0000 | 0.0664 | 439 |
| new | own | 11-16 | C_pm | unresolved | 0.0091 | 0.0000 | 0.0376 | 439 |
| new | own | 17-30 | B | dominance_positive | 0.9796 | 0.9409 | 1.0000 | 1077 |
| new | own | 17-30 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 1077 |
| new | own | 17-30 | B | negligible | 0.0204 | 0.0000 | 0.0591 | 1077 |
| new | own | 17-30 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 1077 |
| new | own | 17-30 | C | dominance_positive | 0.9796 | 0.9409 | 1.0000 | 1077 |
| new | own | 17-30 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 1077 |
| new | own | 17-30 | C | negligible | 0.0204 | 0.0000 | 0.0591 | 1077 |
| new | own | 17-30 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 1077 |
| new | own | 17-30 | B_pm | dominance_positive | 0.9721 | 0.9286 | 1.0000 | 1077 |
| new | own | 17-30 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 1077 |
| new | own | 17-30 | B_pm | negligible | 0.0186 | 0.0000 | 0.0527 | 1077 |
| new | own | 17-30 | B_pm | unresolved | 0.0093 | 0.0000 | 0.0234 | 1077 |
| new | own | 17-30 | C_pm | dominance_positive | 0.9721 | 0.9286 | 1.0000 | 1077 |
| new | own | 17-30 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 1077 |
| new | own | 17-30 | C_pm | negligible | 0.0186 | 0.0000 | 0.0527 | 1077 |
| new | own | 17-30 | C_pm | unresolved | 0.0093 | 0.0000 | 0.0234 | 1077 |

## T5_3_reversal_slot

| rule | portfolio | jstar | count | count_argmin_C_hat | count_precision_matched | n_reversals | n_reversals_pm |
|---|---|---|---|---|---|---|---|
| old | actual | 1 | 0 | 0 | 0 | 66 | 43 |
| old | actual | 2 | 0 | 0 | 0 | 66 | 43 |
| old | actual | 3 | 0 | 0 | 0 | 66 | 43 |
| old | actual | 4 | 1 | 1 | 0 | 66 | 43 |
| old | actual | 5 | 0 | 0 | 0 | 66 | 43 |
| old | actual | 6 | 1 | 1 | 1 | 66 | 43 |
| old | actual | 7 | 0 | 0 | 0 | 66 | 43 |
| old | actual | 8 | 0 | 0 | 0 | 66 | 43 |
| old | actual | 9 | 2 | 2 | 2 | 66 | 43 |
| old | actual | 10 | 3 | 3 | 0 | 66 | 43 |
| old | actual | 11 | 3 | 3 | 3 | 66 | 43 |
| old | actual | 12 | 0 | 0 | 0 | 66 | 43 |
| old | actual | 13 | 1 | 1 | 1 | 66 | 43 |
| old | actual | 14 | 2 | 3 | 1 | 66 | 43 |
| old | actual | 15 | 1 | 1 | 1 | 66 | 43 |
| old | actual | 16 | 6 | 6 | 4 | 66 | 43 |
| old | actual | 17 | 3 | 4 | 1 | 66 | 43 |
| old | actual | 18 | 5 | 5 | 4 | 66 | 43 |
| old | actual | 19 | 7 | 6 | 4 | 66 | 43 |
| old | actual | 20 | 5 | 5 | 4 | 66 | 43 |
| old | actual | 21 | 2 | 2 | 3 | 66 | 43 |
| old | actual | 22 | 5 | 5 | 1 | 66 | 43 |
| old | actual | 23 | 1 | 1 | 1 | 66 | 43 |
| old | actual | 24 | 1 | 1 | 1 | 66 | 43 |
| old | actual | 25 | 2 | 2 | 2 | 66 | 43 |
| old | actual | 26 | 1 | 2 | 1 | 66 | 43 |
| old | actual | 27 | 8 | 7 | 4 | 66 | 43 |
| old | actual | 28 | 1 | 1 | 2 | 66 | 43 |
| old | actual | 29 | 4 | 4 | 2 | 66 | 43 |
| old | actual | 30 | 1 | 0 | 0 | 66 | 43 |
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
| new | actual | 1 | 0 | 0 | 0 | 317 | 262 |
| new | actual | 2 | 0 | 0 | 0 | 317 | 262 |
| new | actual | 3 | 7 | 7 | 7 | 317 | 262 |
| new | actual | 4 | 7 | 5 | 5 | 317 | 262 |
| new | actual | 5 | 1 | 1 | 1 | 317 | 262 |
| new | actual | 6 | 1 | 3 | 1 | 317 | 262 |
| new | actual | 7 | 5 | 4 | 3 | 317 | 262 |
| new | actual | 8 | 30 | 29 | 14 | 317 | 262 |
| new | actual | 9 | 199 | 201 | 179 | 317 | 262 |
| new | actual | 10 | 0 | 0 | 0 | 317 | 262 |
| new | actual | 11 | 1 | 1 | 1 | 317 | 262 |
| new | actual | 12 | 1 | 1 | 1 | 317 | 262 |
| new | actual | 13 | 0 | 0 | 0 | 317 | 262 |
| new | actual | 14 | 0 | 0 | 0 | 317 | 262 |
| new | actual | 15 | 0 | 0 | 0 | 317 | 262 |
| new | actual | 16 | 0 | 0 | 0 | 317 | 262 |
| new | actual | 17 | 3 | 3 | 2 | 317 | 262 |
| new | actual | 18 | 5 | 5 | 3 | 317 | 262 |
| new | actual | 19 | 5 | 5 | 5 | 317 | 262 |
| new | actual | 20 | 6 | 6 | 4 | 317 | 262 |
| new | actual | 21 | 2 | 2 | 2 | 317 | 262 |
| new | actual | 22 | 2 | 2 | 1 | 317 | 262 |
| new | actual | 23 | 5 | 5 | 5 | 317 | 262 |
| new | actual | 24 | 5 | 5 | 4 | 317 | 262 |
| new | actual | 25 | 2 | 2 | 2 | 317 | 262 |
| new | actual | 26 | 1 | 2 | 2 | 317 | 262 |
| new | actual | 27 | 10 | 9 | 6 | 317 | 262 |
| new | actual | 28 | 4 | 4 | 3 | 317 | 262 |
| new | actual | 29 | 6 | 6 | 3 | 317 | 262 |
| new | actual | 30 | 9 | 9 | 8 | 317 | 262 |
| new | own | 1 | 0 | 0 | 0 | 270 | 249 |
| new | own | 2 | 0 | 0 | 0 | 270 | 249 |
| new | own | 3 | 0 | 0 | 0 | 270 | 249 |
| new | own | 4 | 0 | 0 | 0 | 270 | 249 |
| new | own | 5 | 0 | 0 | 0 | 270 | 249 |
| new | own | 6 | 0 | 0 | 0 | 270 | 249 |
| new | own | 7 | 0 | 0 | 0 | 270 | 249 |
| new | own | 8 | 0 | 0 | 0 | 270 | 249 |
| new | own | 9 | 270 | 270 | 249 | 270 | 249 |
| new | own | 10 | 0 | 0 | 0 | 270 | 249 |
| new | own | 11 | 0 | 0 | 0 | 270 | 249 |
| new | own | 12 | 0 | 0 | 0 | 270 | 249 |
| new | own | 13 | 0 | 0 | 0 | 270 | 249 |
| new | own | 14 | 0 | 0 | 0 | 270 | 249 |
| new | own | 15 | 0 | 0 | 0 | 270 | 249 |
| new | own | 16 | 0 | 0 | 0 | 270 | 249 |
| new | own | 17 | 0 | 0 | 0 | 270 | 249 |
| new | own | 18 | 0 | 0 | 0 | 270 | 249 |
| new | own | 19 | 0 | 0 | 0 | 270 | 249 |
| new | own | 20 | 0 | 0 | 0 | 270 | 249 |
| new | own | 21 | 0 | 0 | 0 | 270 | 249 |
| new | own | 22 | 0 | 0 | 0 | 270 | 249 |
| new | own | 23 | 0 | 0 | 0 | 270 | 249 |
| new | own | 24 | 0 | 0 | 0 | 270 | 249 |
| new | own | 25 | 0 | 0 | 0 | 270 | 249 |
| new | own | 26 | 0 | 0 | 0 | 270 | 249 |
| new | own | 27 | 0 | 0 | 0 | 270 | 249 |
| new | own | 28 | 0 | 0 | 0 | 270 | 249 |
| new | own | 29 | 0 | 0 | 0 | 270 | 249 |
| new | own | 30 | 0 | 0 | 0 | 270 | 249 |

## F5_1_profiles

720 rows in `F5_1_profiles.csv`.

## T5_curves_and_T5_6_delta

| rule | portfolio | band | curve | n | mean | q25 | median | q75 | q90 | share_sig_pos | pos_lo99 | pos_hi99 | share_sig_neg | neg_lo99 | neg_hi99 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| old | actual | all | linear | 2308 | 0.0166 | 0.0014 | 0.0140 | 0.0292 | 0.0384 | 0.7054 | 0.5516 | 0.8158 | 0.0117 | 0.0021 | 0.0328 |
| old | actual | all | concave | 2308 | 0.0151 | 0.0010 | 0.0113 | 0.0273 | 0.0357 | 0.6638 | 0.5050 | 0.7858 | 0.0143 | 0.0022 | 0.0412 |
| old | actual | all | convex | 2308 | 0.0155 | 0.0008 | 0.0096 | 0.0278 | 0.0397 | 0.6989 | 0.5675 | 0.7759 | 0.0091 | 0.0021 | 0.0213 |
| old | actual | all | top3_stress | 2308 | 0.0073 | 0.0000 | 0.0009 | 0.0126 | 0.0246 | 0.4298 | 0.3677 | 0.4976 | 0.0013 | 0.0000 | 0.0048 |
| old | actual | 1-3 | linear | 228 | 0.0036 | 0.0017 | 0.0029 | 0.0048 | 0.0071 | 0.5351 | 0.2102 | 0.7263 | 0.0263 | 0.0000 | 0.0679 |
| old | actual | 1-3 | concave | 228 | 0.0022 | 0.0011 | 0.0017 | 0.0026 | 0.0043 | 0.2544 | 0.0120 | 0.4804 | 0.0307 | 0.0000 | 0.0752 |
| old | actual | 1-3 | convex | 228 | 0.0058 | 0.0027 | 0.0045 | 0.0076 | 0.0119 | 0.7588 | 0.6117 | 0.9414 | 0.0219 | 0.0000 | 0.0591 |
| old | actual | 1-3 | top3_stress | 228 | 0.0056 | 0.0005 | 0.0028 | 0.0073 | 0.0135 | 0.4868 | 0.2442 | 0.6914 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 4-10 | linear | 564 | 0.0175 | 0.0069 | 0.0152 | 0.0264 | 0.0347 | 0.9025 | 0.7930 | 0.9737 | 0.0089 | 0.0000 | 0.0321 |
| old | actual | 4-10 | concave | 564 | 0.0126 | 0.0039 | 0.0093 | 0.0173 | 0.0292 | 0.8316 | 0.6552 | 0.9484 | 0.0089 | 0.0000 | 0.0357 |
| old | actual | 4-10 | convex | 564 | 0.0233 | 0.0113 | 0.0215 | 0.0360 | 0.0440 | 0.9273 | 0.8379 | 0.9856 | 0.0035 | 0.0000 | 0.0171 |
| old | actual | 4-10 | top3_stress | 564 | 0.0196 | 0.0120 | 0.0200 | 0.0275 | 0.0329 | 0.9149 | 0.8047 | 0.9863 | 0.0018 | 0.0000 | 0.0103 |
| old | actual | 11-16 | linear | 439 | 0.0227 | 0.0046 | 0.0259 | 0.0349 | 0.0424 | 0.7677 | 0.5748 | 0.9310 | 0.0068 | 0.0000 | 0.0341 |
| old | actual | 11-16 | concave | 439 | 0.0160 | 0.0052 | 0.0170 | 0.0246 | 0.0308 | 0.7677 | 0.5784 | 0.9256 | 0.0091 | 0.0000 | 0.0367 |
| old | actual | 11-16 | convex | 439 | 0.0258 | 0.0032 | 0.0298 | 0.0387 | 0.0509 | 0.7563 | 0.5492 | 0.9301 | 0.0046 | 0.0000 | 0.0205 |
| old | actual | 11-16 | top3_stress | 439 | 0.0088 | 0.0009 | 0.0064 | 0.0148 | 0.0211 | 0.6993 | 0.5058 | 0.8682 | 0.0023 | 0.0000 | 0.0167 |
| old | actual | 17-30 | linear | 1077 | 0.0164 | 0.0000 | 0.0151 | 0.0297 | 0.0389 | 0.6128 | 0.3243 | 0.7574 | 0.0121 | 0.0000 | 0.0481 |
| old | actual | 17-30 | concave | 1077 | 0.0187 | 0.0000 | 0.0221 | 0.0327 | 0.0405 | 0.6202 | 0.3380 | 0.7603 | 0.0158 | 0.0000 | 0.0677 |
| old | actual | 17-30 | convex | 1077 | 0.0093 | 0.0000 | 0.0044 | 0.0161 | 0.0277 | 0.5432 | 0.2799 | 0.6620 | 0.0111 | 0.0000 | 0.0359 |
| old | actual | 17-30 | top3_stress | 1077 | 0.0005 | 0.0000 | 0.0000 | 0.0002 | 0.0012 | 0.0539 | 0.0131 | 0.0924 | 0.0009 | 0.0000 | 0.0068 |
| old | own | all | linear | 2308 | 0.0232 | 0.0101 | 0.0239 | 0.0336 | 0.0409 | 0.9151 | 0.8569 | 0.9544 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | concave | 2308 | 0.0208 | 0.0079 | 0.0213 | 0.0311 | 0.0378 | 0.8713 | 0.7981 | 0.9238 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | convex | 2308 | 0.0209 | 0.0072 | 0.0189 | 0.0314 | 0.0416 | 0.8951 | 0.8446 | 0.9231 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | top3_stress | 2308 | 0.0081 | 0.0000 | 0.0027 | 0.0141 | 0.0254 | 0.4983 | 0.4503 | 0.5452 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | linear | 228 | 0.0037 | 0.0019 | 0.0028 | 0.0045 | 0.0071 | 0.4649 | 0.1872 | 0.6816 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | concave | 228 | 0.0020 | 0.0011 | 0.0015 | 0.0024 | 0.0039 | 0.1842 | 0.0000 | 0.3647 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | convex | 228 | 0.0063 | 0.0033 | 0.0047 | 0.0076 | 0.0119 | 0.8158 | 0.6495 | 0.9833 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | top3_stress | 228 | 0.0056 | 0.0005 | 0.0026 | 0.0071 | 0.0141 | 0.4868 | 0.2408 | 0.7220 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | linear | 564 | 0.0161 | 0.0072 | 0.0134 | 0.0242 | 0.0305 | 0.9486 | 0.8606 | 0.9948 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | concave | 564 | 0.0094 | 0.0040 | 0.0076 | 0.0142 | 0.0182 | 0.8777 | 0.7146 | 0.9771 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | convex | 564 | 0.0241 | 0.0117 | 0.0213 | 0.0356 | 0.0438 | 0.9787 | 0.9181 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | top3_stress | 564 | 0.0208 | 0.0131 | 0.0205 | 0.0277 | 0.0328 | 0.9770 | 0.9171 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | linear | 439 | 0.0313 | 0.0234 | 0.0303 | 0.0372 | 0.0482 | 0.9954 | 0.9821 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | concave | 439 | 0.0211 | 0.0151 | 0.0201 | 0.0261 | 0.0327 | 0.9909 | 0.9760 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | convex | 439 | 0.0359 | 0.0267 | 0.0343 | 0.0425 | 0.0576 | 0.9954 | 0.9821 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | top3_stress | 439 | 0.0113 | 0.0051 | 0.0084 | 0.0166 | 0.0231 | 0.9089 | 0.8323 | 0.9730 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | linear | 1077 | 0.0278 | 0.0195 | 0.0281 | 0.0371 | 0.0426 | 0.9601 | 0.9147 | 0.9977 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | concave | 1077 | 0.0306 | 0.0251 | 0.0307 | 0.0360 | 0.0432 | 0.9647 | 0.9197 | 0.9991 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | convex | 1077 | 0.0162 | 0.0050 | 0.0147 | 0.0249 | 0.0332 | 0.8273 | 0.7544 | 0.8733 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | top3_stress | 1077 | 0.0007 | 0.0000 | 0.0000 | 0.0006 | 0.0021 | 0.0826 | 0.0271 | 0.1412 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | all | linear | 2308 | 0.0142 | 0.0000 | 0.0047 | 0.0270 | 0.0419 | 0.5403 | 0.3779 | 0.6519 | 0.0602 | 0.0133 | 0.1084 |
| new | actual | all | concave | 2308 | 0.0137 | 0.0000 | 0.0049 | 0.0284 | 0.0374 | 0.5472 | 0.3987 | 0.6394 | 0.0360 | 0.0077 | 0.0696 |
| new | actual | all | convex | 2308 | 0.0119 | 0.0000 | 0.0029 | 0.0211 | 0.0402 | 0.5052 | 0.3571 | 0.6093 | 0.0858 | 0.0385 | 0.1235 |
| new | actual | all | top3_stress | 2308 | 0.0040 | 0.0000 | 0.0000 | 0.0071 | 0.0188 | 0.3397 | 0.2529 | 0.4154 | 0.1053 | 0.0590 | 0.1426 |
| new | actual | 1-3 | linear | 228 | -0.0024 | -0.0032 | -0.0010 | 0.0001 | 0.0014 | 0.0439 | 0.0000 | 0.0952 | 0.3246 | 0.0514 | 0.5292 |
| new | actual | 1-3 | concave | 228 | -0.0014 | -0.0017 | -0.0006 | 0.0001 | 0.0034 | 0.1140 | 0.0091 | 0.3086 | 0.1447 | 0.0114 | 0.2841 |
| new | actual | 1-3 | convex | 228 | -0.0039 | -0.0059 | -0.0023 | -0.0003 | 0.0001 | 0.0219 | 0.0000 | 0.0617 | 0.4605 | 0.1720 | 0.6329 |
| new | actual | 1-3 | top3_stress | 228 | -0.0062 | -0.0102 | -0.0041 | -0.0007 | 0.0000 | 0.0044 | 0.0000 | 0.0298 | 0.5877 | 0.2901 | 0.8058 |
| new | actual | 4-10 | linear | 564 | 0.0035 | 0.0000 | 0.0014 | 0.0066 | 0.0141 | 0.3954 | 0.1975 | 0.5423 | 0.0904 | 0.0105 | 0.2068 |
| new | actual | 4-10 | concave | 564 | 0.0031 | 0.0000 | 0.0013 | 0.0053 | 0.0110 | 0.3954 | 0.2306 | 0.5107 | 0.0603 | 0.0110 | 0.1345 |
| new | actual | 4-10 | convex | 564 | 0.0036 | -0.0001 | 0.0009 | 0.0081 | 0.0155 | 0.3989 | 0.1897 | 0.5657 | 0.1525 | 0.0677 | 0.2466 |
| new | actual | 4-10 | top3_stress | 564 | 0.0015 | -0.0003 | 0.0001 | 0.0066 | 0.0125 | 0.3617 | 0.1626 | 0.5073 | 0.1862 | 0.1099 | 0.2597 |
| new | actual | 11-16 | linear | 439 | 0.0230 | 0.0009 | 0.0216 | 0.0389 | 0.0469 | 0.7221 | 0.4986 | 0.9051 | 0.0068 | 0.0000 | 0.0267 |
| new | actual | 11-16 | concave | 439 | 0.0161 | 0.0006 | 0.0151 | 0.0270 | 0.0337 | 0.7107 | 0.4779 | 0.9030 | 0.0023 | 0.0000 | 0.0137 |
| new | actual | 11-16 | convex | 439 | 0.0274 | 0.0007 | 0.0261 | 0.0434 | 0.0549 | 0.7130 | 0.4718 | 0.9051 | 0.0046 | 0.0000 | 0.0200 |
| new | actual | 11-16 | top3_stress | 439 | 0.0152 | 0.0000 | 0.0156 | 0.0229 | 0.0304 | 0.7062 | 0.4677 | 0.8992 | 0.0046 | 0.0000 | 0.0274 |
| new | actual | 17-30 | linear | 1077 | 0.0198 | 0.0000 | 0.0192 | 0.0347 | 0.0450 | 0.6472 | 0.3904 | 0.7705 | 0.0102 | 0.0000 | 0.0474 |
| new | actual | 17-30 | concave | 1077 | 0.0214 | 0.0000 | 0.0246 | 0.0353 | 0.0453 | 0.6518 | 0.4008 | 0.7722 | 0.0139 | 0.0000 | 0.0632 |
| new | actual | 17-30 | convex | 1077 | 0.0133 | 0.0000 | 0.0051 | 0.0229 | 0.0379 | 0.5785 | 0.3555 | 0.6844 | 0.0046 | 0.0000 | 0.0200 |
| new | actual | 17-30 | top3_stress | 1077 | 0.0029 | 0.0000 | 0.0000 | 0.0025 | 0.0101 | 0.2498 | 0.1688 | 0.3291 | 0.0019 | 0.0000 | 0.0119 |
| new | own | all | linear | 2308 | 0.0215 | 0.0008 | 0.0186 | 0.0369 | 0.0492 | 0.7153 | 0.6507 | 0.7693 | 0.0516 | 0.0213 | 0.0789 |
| new | own | all | concave | 2308 | 0.0198 | 0.0007 | 0.0211 | 0.0333 | 0.0426 | 0.6967 | 0.6340 | 0.7468 | 0.0113 | 0.0006 | 0.0259 |
| new | own | all | convex | 2308 | 0.0182 | 0.0005 | 0.0101 | 0.0310 | 0.0507 | 0.6629 | 0.5781 | 0.7247 | 0.0836 | 0.0423 | 0.1192 |
| new | own | all | top3_stress | 2308 | 0.0059 | 0.0000 | 0.0008 | 0.0114 | 0.0217 | 0.4406 | 0.3760 | 0.5029 | 0.1018 | 0.0569 | 0.1402 |
| new | own | 1-3 | linear | 228 | -0.0019 | -0.0031 | -0.0012 | -0.0002 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.2719 | 0.0857 | 0.4380 |
| new | own | 1-3 | concave | 228 | -0.0009 | -0.0015 | -0.0006 | -0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0482 | 0.0000 | 0.1290 |
| new | own | 1-3 | convex | 228 | -0.0035 | -0.0059 | -0.0023 | -0.0004 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.4561 | 0.2222 | 0.6505 |
| new | own | 1-3 | top3_stress | 228 | -0.0063 | -0.0101 | -0.0041 | -0.0008 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.5614 | 0.2778 | 0.7772 |
| new | own | 4-10 | linear | 564 | 0.0030 | -0.0000 | 0.0005 | 0.0060 | 0.0102 | 0.3617 | 0.1564 | 0.5070 | 0.1011 | 0.0450 | 0.1586 |
| new | own | 4-10 | concave | 564 | 0.0019 | -0.0000 | 0.0003 | 0.0036 | 0.0063 | 0.2908 | 0.1104 | 0.4172 | 0.0266 | 0.0022 | 0.0565 |
| new | own | 4-10 | convex | 564 | 0.0039 | -0.0000 | 0.0007 | 0.0085 | 0.0145 | 0.3989 | 0.1722 | 0.5661 | 0.1578 | 0.0786 | 0.2349 |
| new | own | 4-10 | top3_stress | 564 | 0.0019 | -0.0002 | 0.0002 | 0.0077 | 0.0132 | 0.3723 | 0.1712 | 0.5095 | 0.1897 | 0.1117 | 0.2729 |
| new | own | 11-16 | linear | 439 | 0.0321 | 0.0148 | 0.0313 | 0.0444 | 0.0567 | 0.9431 | 0.8698 | 0.9926 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | concave | 439 | 0.0211 | 0.0092 | 0.0203 | 0.0301 | 0.0384 | 0.9226 | 0.8277 | 0.9869 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | convex | 439 | 0.0390 | 0.0197 | 0.0375 | 0.0519 | 0.0670 | 0.9453 | 0.8717 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | top3_stress | 439 | 0.0204 | 0.0127 | 0.0188 | 0.0245 | 0.0342 | 0.9317 | 0.8420 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | linear | 1077 | 0.0317 | 0.0195 | 0.0306 | 0.0420 | 0.0540 | 0.9591 | 0.9147 | 0.9960 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | concave | 1077 | 0.0329 | 0.0271 | 0.0328 | 0.0391 | 0.0463 | 0.9647 | 0.9197 | 0.9991 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | convex | 1077 | 0.0219 | 0.0050 | 0.0163 | 0.0333 | 0.0505 | 0.8264 | 0.7544 | 0.8711 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | top3_stress | 1077 | 0.0046 | 0.0000 | 0.0004 | 0.0060 | 0.0149 | 0.3695 | 0.2850 | 0.4438 | 0.0000 | 0.0000 | 0.0000 |
| delta | actual | all | linear | 2308 | -0.0024 | -0.0075 | 0.0000 | 0.0008 | 0.0086 | 0.2097 | 0.1422 | 0.2748 | 0.3388 | 0.2383 | 0.4038 |
| delta | actual | all | concave | 2308 | -0.0014 | -0.0045 | 0.0000 | 0.0008 | 0.0058 | 0.1885 | 0.1386 | 0.2500 | 0.3133 | 0.2034 | 0.3979 |
| delta | actual | all | convex | 2308 | -0.0036 | -0.0114 | 0.0000 | 0.0016 | 0.0117 | 0.2322 | 0.1609 | 0.2947 | 0.3614 | 0.3124 | 0.3979 |
| delta | actual | all | top3_stress | 2308 | -0.0033 | -0.0094 | 0.0000 | 0.0009 | 0.0102 | 0.2175 | 0.1566 | 0.2682 | 0.3115 | 0.2573 | 0.3457 |
| delta | actual | 1-3 | linear | 228 | -0.0059 | -0.0078 | -0.0033 | -0.0014 | -0.0008 | 0.0175 | 0.0000 | 0.0698 | 0.5482 | 0.1097 | 0.8100 |
| delta | actual | 1-3 | concave | 228 | -0.0035 | -0.0044 | -0.0021 | -0.0007 | 0.0008 | 0.0614 | 0.0000 | 0.2166 | 0.4298 | 0.0611 | 0.6410 |
| delta | actual | 1-3 | convex | 228 | -0.0096 | -0.0137 | -0.0068 | -0.0027 | -0.0012 | 0.0088 | 0.0000 | 0.0497 | 0.7544 | 0.6000 | 0.9372 |
| delta | actual | 1-3 | top3_stress | 228 | -0.0117 | -0.0174 | -0.0071 | -0.0012 | -0.0001 | 0.0044 | 0.0000 | 0.0298 | 0.6184 | 0.3030 | 0.8342 |
| delta | actual | 4-10 | linear | 564 | -0.0140 | -0.0204 | -0.0123 | -0.0068 | -0.0022 | 0.0142 | 0.0000 | 0.0505 | 0.8723 | 0.7188 | 0.9700 |
| delta | actual | 4-10 | concave | 564 | -0.0095 | -0.0127 | -0.0072 | -0.0037 | 0.0000 | 0.0337 | 0.0000 | 0.0905 | 0.8085 | 0.5955 | 0.9538 |
| delta | actual | 4-10 | convex | 564 | -0.0197 | -0.0273 | -0.0190 | -0.0113 | -0.0053 | 0.0089 | 0.0000 | 0.0323 | 0.9255 | 0.8461 | 0.9851 |
| delta | actual | 4-10 | top3_stress | 564 | -0.0181 | -0.0239 | -0.0169 | -0.0113 | -0.0037 | 0.0018 | 0.0000 | 0.0135 | 0.9096 | 0.7908 | 0.9811 |
| delta | actual | 11-16 | linear | 439 | 0.0003 | -0.0064 | 0.0000 | 0.0068 | 0.0137 | 0.3713 | 0.1770 | 0.5375 | 0.3121 | 0.1513 | 0.4404 |
| delta | actual | 11-16 | concave | 439 | 0.0001 | -0.0046 | 0.0000 | 0.0038 | 0.0089 | 0.3121 | 0.1336 | 0.4539 | 0.3121 | 0.1347 | 0.4435 |
| delta | actual | 11-16 | convex | 439 | 0.0015 | -0.0061 | 0.0000 | 0.0104 | 0.0192 | 0.4419 | 0.2685 | 0.5890 | 0.2870 | 0.1360 | 0.4027 |
| delta | actual | 11-16 | top3_stress | 439 | 0.0063 | 0.0000 | 0.0059 | 0.0132 | 0.0185 | 0.5467 | 0.3704 | 0.6911 | 0.1458 | 0.0493 | 0.2053 |
| delta | actual | 17-30 | linear | 1077 | 0.0034 | 0.0000 | 0.0000 | 0.0035 | 0.0106 | 0.2869 | 0.1874 | 0.3911 | 0.0260 | 0.0000 | 0.0585 |
| delta | actual | 17-30 | concave | 1077 | 0.0027 | 0.0000 | 0.0000 | 0.0023 | 0.0076 | 0.2461 | 0.1679 | 0.3340 | 0.0297 | 0.0040 | 0.0638 |
| delta | actual | 17-30 | convex | 1077 | 0.0040 | 0.0000 | 0.0000 | 0.0048 | 0.0131 | 0.3110 | 0.2035 | 0.4196 | 0.0130 | 0.0000 | 0.0332 |
| delta | actual | 17-30 | top3_stress | 1077 | 0.0024 | 0.0000 | 0.0000 | 0.0023 | 0.0085 | 0.2414 | 0.1636 | 0.3203 | 0.0009 | 0.0000 | 0.0074 |
| delta | own | all | linear | 2308 | -0.0018 | -0.0082 | -0.0000 | 0.0034 | 0.0113 | 0.2769 | 0.2268 | 0.3230 | 0.3865 | 0.3208 | 0.4354 |
| delta | own | all | concave | 2308 | -0.0010 | -0.0047 | -0.0000 | 0.0019 | 0.0067 | 0.2305 | 0.1857 | 0.2665 | 0.3419 | 0.2675 | 0.3855 |
| delta | own | all | convex | 2308 | -0.0027 | -0.0128 | 0.0000 | 0.0057 | 0.0169 | 0.3063 | 0.2582 | 0.3482 | 0.4029 | 0.3495 | 0.4425 |
| delta | own | all | top3_stress | 2308 | -0.0022 | -0.0107 | 0.0000 | 0.0049 | 0.0140 | 0.3020 | 0.2392 | 0.3536 | 0.3349 | 0.2807 | 0.3738 |
| delta | own | 1-3 | linear | 228 | -0.0056 | -0.0074 | -0.0042 | -0.0022 | -0.0014 | 0.0000 | 0.0000 | 0.0000 | 0.6096 | 0.3048 | 0.8450 |
| delta | own | 1-3 | concave | 228 | -0.0030 | -0.0039 | -0.0022 | -0.0012 | -0.0008 | 0.0000 | 0.0000 | 0.0000 | 0.3728 | 0.1500 | 0.5502 |
| delta | own | 1-3 | convex | 228 | -0.0098 | -0.0130 | -0.0072 | -0.0037 | -0.0025 | 0.0000 | 0.0000 | 0.0000 | 0.8640 | 0.6889 | 0.9802 |
| delta | own | 1-3 | top3_stress | 228 | -0.0119 | -0.0177 | -0.0068 | -0.0012 | -0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.6316 | 0.2984 | 0.8630 |
| delta | own | 4-10 | linear | 564 | -0.0131 | -0.0180 | -0.0118 | -0.0078 | -0.0056 | 0.0018 | 0.0000 | 0.0135 | 0.9645 | 0.8859 | 0.9969 |
| delta | own | 4-10 | concave | 564 | -0.0075 | -0.0103 | -0.0067 | -0.0045 | -0.0031 | 0.0018 | 0.0000 | 0.0135 | 0.9131 | 0.7816 | 0.9839 |
| delta | own | 4-10 | convex | 564 | -0.0203 | -0.0271 | -0.0190 | -0.0125 | -0.0090 | 0.0018 | 0.0000 | 0.0135 | 0.9787 | 0.9248 | 0.9984 |
| delta | own | 4-10 | top3_stress | 564 | -0.0189 | -0.0240 | -0.0174 | -0.0122 | -0.0077 | 0.0071 | 0.0000 | 0.0309 | 0.9699 | 0.9173 | 0.9930 |
| delta | own | 11-16 | linear | 439 | 0.0008 | -0.0098 | 0.0027 | 0.0101 | 0.0152 | 0.5148 | 0.3540 | 0.7134 | 0.3895 | 0.2083 | 0.5108 |
| delta | own | 11-16 | concave | 439 | 0.0000 | -0.0062 | 0.0010 | 0.0055 | 0.0089 | 0.4260 | 0.2812 | 0.5524 | 0.3645 | 0.1773 | 0.4732 |
| delta | own | 11-16 | convex | 439 | 0.0031 | -0.0119 | 0.0064 | 0.0162 | 0.0226 | 0.5831 | 0.4301 | 0.7774 | 0.3576 | 0.1738 | 0.4788 |
| delta | own | 11-16 | top3_stress | 439 | 0.0091 | 0.0006 | 0.0102 | 0.0167 | 0.0222 | 0.7039 | 0.5787 | 0.8717 | 0.1868 | 0.0659 | 0.2891 |
| delta | own | 17-30 | linear | 1077 | 0.0039 | 0.0000 | 0.0004 | 0.0064 | 0.0131 | 0.3825 | 0.3263 | 0.4320 | 0.0353 | 0.0019 | 0.0990 |
| delta | own | 17-30 | concave | 1077 | 0.0023 | 0.0000 | 0.0001 | 0.0039 | 0.0080 | 0.3194 | 0.2622 | 0.3669 | 0.0269 | 0.0019 | 0.0640 |
| delta | own | 17-30 | convex | 1077 | 0.0057 | 0.0000 | 0.0006 | 0.0090 | 0.0185 | 0.4178 | 0.3627 | 0.4651 | 0.0223 | 0.0009 | 0.0556 |
| delta | own | 17-30 | top3_stress | 1077 | 0.0039 | 0.0000 | 0.0004 | 0.0054 | 0.0120 | 0.3565 | 0.2667 | 0.4357 | 0.0000 | 0.0000 | 0.0000 |

## H1

| n_team_games | share_neg_new | share_neg_old | diff_new_minus_old | diff_lo99 | diff_hi99 | n_new_reversals | crossing_share | crossing_lo99 | crossing_hi99 | supported |
|---|---|---|---|---|---|---|---|---|---|---|
| 322 | 0.3540 | 0.0000 | 0.3540 | 0.1423 | 0.5288 | 234 | 1.0000 | 1.0000 | 1.0000 | True |

## T5_attr_portfolio_effect

| rule | band | n | mean | q25 | median | q75 | q90 | share_nonzero |
|---|---|---|---|---|---|---|---|---|
| old | all | 2308 | -0.0066 | -0.0108 | 0.0000 | 0.0000 | 0.0006 | 0.3696 |
| old | 1-3 | 228 | -0.0001 | -0.0000 | 0.0000 | 0.0000 | 0.0009 | 0.0658 |
| old | 4-10 | 564 | 0.0014 | 0.0000 | 0.0000 | 0.0009 | 0.0096 | 0.2890 |
| old | 11-16 | 439 | -0.0086 | -0.0186 | 0.0000 | 0.0000 | 0.0001 | 0.3986 |
| old | 17-30 | 1077 | -0.0113 | -0.0227 | -0.0008 | 0.0000 | 0.0000 | 0.4643 |
| new | all | 2308 | -0.0072 | -0.0087 | 0.0000 | 0.0000 | 0.0012 | 0.3817 |
| new | 1-3 | 228 | -0.0005 | -0.0002 | 0.0000 | 0.0003 | 0.0034 | 0.1974 |
| new | 4-10 | 564 | 0.0005 | 0.0000 | 0.0000 | 0.0008 | 0.0051 | 0.2535 |
| new | 11-16 | 439 | -0.0091 | -0.0103 | 0.0000 | 0.0000 | 0.0005 | 0.3781 |
| new | 17-30 | 1077 | -0.0119 | -0.0208 | -0.0013 | 0.0000 | 0.0000 | 0.4893 |
| delta | all | 2308 | -0.0006 | -0.0001 | 0.0000 | 0.0000 | 0.0035 | 0.2574 |
| delta | 1-3 | 228 | -0.0004 | -0.0001 | 0.0000 | 0.0005 | 0.0032 | 0.1842 |
| delta | 4-10 | 564 | -0.0009 | -0.0003 | 0.0000 | 0.0001 | 0.0047 | 0.2819 |
| delta | 11-16 | 439 | -0.0005 | -0.0004 | 0.0000 | 0.0000 | 0.0086 | 0.3349 |
| delta | 17-30 | 1077 | -0.0006 | -0.0000 | 0.0000 | 0.0000 | 0.0023 | 0.2284 |

## T5_7_rollover

| rule | portfolio | band | curve | rho | measure | n | mean | q25 | median | q75 | q90 | share_sign_flip | vbar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| old | actual | all | - | 0.0000 | M | 2308 | 0.0026 | -0.0000 | 0.0000 | 0.0000 | 0.0049 |  |  |
| old | actual | all | linear | 0.0000 | tau | 2308 | 0.0166 | 0.0014 | 0.0140 | 0.0292 | 0.0384 | 0.0000 | 0.5000 |
| old | actual | all | linear | 0.5000 | tau | 2308 | 0.0160 | 0.0013 | 0.0129 | 0.0280 | 0.0374 | 0.0013 | 0.5000 |
| old | actual | all | linear | 0.8000 | tau | 2308 | 0.0156 | 0.0012 | 0.0118 | 0.0273 | 0.0371 | 0.0026 | 0.5000 |
| old | actual | all | concave | 0.0000 | tau | 2308 | 0.0151 | 0.0010 | 0.0113 | 0.0273 | 0.0357 | 0.0000 | 0.6599 |
| old | actual | all | concave | 0.5000 | tau | 2308 | 0.0142 | 0.0010 | 0.0103 | 0.0256 | 0.0344 | 0.0061 | 0.6599 |
| old | actual | all | concave | 0.8000 | tau | 2308 | 0.0137 | 0.0009 | 0.0091 | 0.0245 | 0.0342 | 0.0078 | 0.6599 |
| old | actual | all | convex | 0.0000 | tau | 2308 | 0.0155 | 0.0008 | 0.0096 | 0.0278 | 0.0397 | 0.0000 | 0.3391 |
| old | actual | all | convex | 0.5000 | tau | 2308 | 0.0151 | 0.0007 | 0.0088 | 0.0270 | 0.0389 | 0.0017 | 0.3391 |
| old | actual | all | convex | 0.8000 | tau | 2308 | 0.0148 | 0.0006 | 0.0084 | 0.0263 | 0.0387 | 0.0043 | 0.3391 |
| old | actual | all | top3_stress | 0.0000 | tau | 2308 | 0.0073 | 0.0000 | 0.0009 | 0.0126 | 0.0246 | 0.0000 | 0.1000 |
| old | actual | all | top3_stress | 0.5000 | tau | 2308 | 0.0071 | 0.0000 | 0.0007 | 0.0125 | 0.0245 | 0.1018 | 0.1000 |
| old | actual | all | top3_stress | 0.8000 | tau | 2308 | 0.0070 | 0.0000 | 0.0007 | 0.0123 | 0.0241 | 0.1031 | 0.1000 |
| old | actual | 1-3 | - | 0.0000 | M | 228 | 0.0006 | -0.0000 | 0.0000 | 0.0000 | 0.0006 |  |  |
| old | actual | 1-3 | linear | 0.0000 | tau | 228 | 0.0036 | 0.0017 | 0.0029 | 0.0048 | 0.0071 | 0.0000 | 0.5000 |
| old | actual | 1-3 | linear | 0.5000 | tau | 228 | 0.0034 | 0.0018 | 0.0029 | 0.0048 | 0.0071 | 0.0044 | 0.5000 |
| old | actual | 1-3 | linear | 0.8000 | tau | 228 | 0.0033 | 0.0018 | 0.0029 | 0.0048 | 0.0071 | 0.0044 | 0.5000 |
| old | actual | 1-3 | concave | 0.0000 | tau | 228 | 0.0022 | 0.0011 | 0.0017 | 0.0026 | 0.0043 | 0.0000 | 0.6599 |
| old | actual | 1-3 | concave | 0.5000 | tau | 228 | 0.0020 | 0.0010 | 0.0017 | 0.0026 | 0.0043 | 0.0088 | 0.6599 |
| old | actual | 1-3 | concave | 0.8000 | tau | 228 | 0.0019 | 0.0010 | 0.0017 | 0.0026 | 0.0043 | 0.0175 | 0.6599 |
| old | actual | 1-3 | convex | 0.0000 | tau | 228 | 0.0058 | 0.0027 | 0.0045 | 0.0076 | 0.0119 | 0.0000 | 0.3391 |
| old | actual | 1-3 | convex | 0.5000 | tau | 228 | 0.0057 | 0.0027 | 0.0046 | 0.0076 | 0.0119 | 0.0000 | 0.3391 |
| old | actual | 1-3 | convex | 0.8000 | tau | 228 | 0.0056 | 0.0026 | 0.0046 | 0.0076 | 0.0119 | 0.0044 | 0.3391 |
| old | actual | 1-3 | top3_stress | 0.0000 | tau | 228 | 0.0056 | 0.0005 | 0.0028 | 0.0073 | 0.0135 | 0.0000 | 0.1000 |
| old | actual | 1-3 | top3_stress | 0.5000 | tau | 228 | 0.0055 | 0.0005 | 0.0028 | 0.0073 | 0.0135 | 0.0088 | 0.1000 |
| old | actual | 1-3 | top3_stress | 0.8000 | tau | 228 | 0.0055 | 0.0005 | 0.0028 | 0.0073 | 0.0135 | 0.0088 | 0.1000 |
| old | actual | 4-10 | - | 0.0000 | M | 564 | 0.0053 | -0.0000 | 0.0000 | 0.0001 | 0.0257 |  |  |
| old | actual | 4-10 | linear | 0.0000 | tau | 564 | 0.0175 | 0.0069 | 0.0152 | 0.0264 | 0.0347 | 0.0000 | 0.5000 |
| old | actual | 4-10 | linear | 0.5000 | tau | 564 | 0.0161 | 0.0069 | 0.0143 | 0.0250 | 0.0317 | 0.0000 | 0.5000 |
| old | actual | 4-10 | linear | 0.8000 | tau | 564 | 0.0153 | 0.0069 | 0.0137 | 0.0238 | 0.0304 | 0.0018 | 0.5000 |
| old | actual | 4-10 | concave | 0.0000 | tau | 564 | 0.0126 | 0.0039 | 0.0093 | 0.0173 | 0.0292 | 0.0000 | 0.6599 |
| old | actual | 4-10 | concave | 0.5000 | tau | 564 | 0.0108 | 0.0039 | 0.0090 | 0.0161 | 0.0224 | 0.0106 | 0.6599 |
| old | actual | 4-10 | concave | 0.8000 | tau | 564 | 0.0097 | 0.0039 | 0.0085 | 0.0151 | 0.0197 | 0.0124 | 0.6599 |
| old | actual | 4-10 | convex | 0.0000 | tau | 564 | 0.0233 | 0.0113 | 0.0215 | 0.0360 | 0.0440 | 0.0000 | 0.3391 |
| old | actual | 4-10 | convex | 0.5000 | tau | 564 | 0.0224 | 0.0112 | 0.0206 | 0.0335 | 0.0428 | 0.0018 | 0.3391 |
| old | actual | 4-10 | convex | 0.8000 | tau | 564 | 0.0218 | 0.0112 | 0.0198 | 0.0322 | 0.0424 | 0.0035 | 0.3391 |
| old | actual | 4-10 | top3_stress | 0.0000 | tau | 564 | 0.0196 | 0.0120 | 0.0200 | 0.0275 | 0.0329 | 0.0000 | 0.1000 |
| old | actual | 4-10 | top3_stress | 0.5000 | tau | 564 | 0.0193 | 0.0112 | 0.0196 | 0.0273 | 0.0328 | 0.0000 | 0.1000 |
| old | actual | 4-10 | top3_stress | 0.8000 | tau | 564 | 0.0192 | 0.0111 | 0.0195 | 0.0270 | 0.0328 | 0.0000 | 0.1000 |
| old | actual | 11-16 | - | 0.0000 | M | 439 | 0.0022 | -0.0000 | 0.0000 | 0.0000 | 0.0065 |  |  |
| old | actual | 11-16 | linear | 0.0000 | tau | 439 | 0.0227 | 0.0046 | 0.0259 | 0.0349 | 0.0424 | 0.0000 | 0.5000 |
| old | actual | 11-16 | linear | 0.5000 | tau | 439 | 0.0222 | 0.0038 | 0.0257 | 0.0345 | 0.0417 | 0.0023 | 0.5000 |
| old | actual | 11-16 | linear | 0.8000 | tau | 439 | 0.0218 | 0.0032 | 0.0249 | 0.0344 | 0.0417 | 0.0046 | 0.5000 |
| old | actual | 11-16 | concave | 0.0000 | tau | 439 | 0.0160 | 0.0052 | 0.0170 | 0.0246 | 0.0308 | 0.0000 | 0.6599 |
| old | actual | 11-16 | concave | 0.5000 | tau | 439 | 0.0153 | 0.0037 | 0.0167 | 0.0239 | 0.0291 | 0.0023 | 0.6599 |
| old | actual | 11-16 | concave | 0.8000 | tau | 439 | 0.0148 | 0.0028 | 0.0164 | 0.0233 | 0.0289 | 0.0046 | 0.6599 |
| old | actual | 11-16 | convex | 0.0000 | tau | 439 | 0.0258 | 0.0032 | 0.0298 | 0.0387 | 0.0509 | 0.0000 | 0.3391 |
| old | actual | 11-16 | convex | 0.5000 | tau | 439 | 0.0255 | 0.0026 | 0.0286 | 0.0385 | 0.0509 | 0.0046 | 0.3391 |
| old | actual | 11-16 | convex | 0.8000 | tau | 439 | 0.0252 | 0.0023 | 0.0284 | 0.0383 | 0.0509 | 0.0068 | 0.3391 |
| old | actual | 11-16 | top3_stress | 0.0000 | tau | 439 | 0.0088 | 0.0009 | 0.0064 | 0.0148 | 0.0211 | 0.0000 | 0.1000 |
| old | actual | 11-16 | top3_stress | 0.5000 | tau | 439 | 0.0087 | 0.0008 | 0.0063 | 0.0148 | 0.0211 | 0.0273 | 0.1000 |
| old | actual | 11-16 | top3_stress | 0.8000 | tau | 439 | 0.0087 | 0.0002 | 0.0063 | 0.0148 | 0.0211 | 0.0319 | 0.1000 |
| old | actual | 17-30 | - | 0.0000 | M | 1077 | 0.0018 | -0.0000 | 0.0000 | 0.0000 | 0.0001 |  |  |
| old | actual | 17-30 | linear | 0.0000 | tau | 1077 | 0.0164 | 0.0000 | 0.0151 | 0.0297 | 0.0389 | 0.0000 | 0.5000 |
| old | actual | 17-30 | linear | 0.5000 | tau | 1077 | 0.0160 | 0.0000 | 0.0132 | 0.0292 | 0.0388 | 0.0009 | 0.5000 |
| old | actual | 17-30 | linear | 0.8000 | tau | 1077 | 0.0157 | 0.0000 | 0.0108 | 0.0292 | 0.0388 | 0.0019 | 0.5000 |
| old | actual | 17-30 | concave | 0.0000 | tau | 1077 | 0.0187 | 0.0000 | 0.0221 | 0.0327 | 0.0405 | 0.0000 | 0.6599 |
| old | actual | 17-30 | concave | 0.5000 | tau | 1077 | 0.0181 | 0.0000 | 0.0205 | 0.0322 | 0.0398 | 0.0046 | 0.6599 |
| old | actual | 17-30 | concave | 0.8000 | tau | 1077 | 0.0178 | 0.0000 | 0.0192 | 0.0322 | 0.0398 | 0.0046 | 0.6599 |
| old | actual | 17-30 | convex | 0.0000 | tau | 1077 | 0.0093 | 0.0000 | 0.0044 | 0.0161 | 0.0277 | 0.0000 | 0.3391 |
| old | actual | 17-30 | convex | 0.5000 | tau | 1077 | 0.0090 | 0.0000 | 0.0039 | 0.0156 | 0.0277 | 0.0009 | 0.3391 |
| old | actual | 17-30 | convex | 0.8000 | tau | 1077 | 0.0088 | 0.0000 | 0.0030 | 0.0156 | 0.0277 | 0.0037 | 0.3391 |
| old | actual | 17-30 | top3_stress | 0.0000 | tau | 1077 | 0.0005 | 0.0000 | 0.0000 | 0.0002 | 0.0012 | 0.0000 | 0.1000 |
| old | actual | 17-30 | top3_stress | 0.5000 | tau | 1077 | 0.0004 | 0.0000 | 0.0000 | 0.0001 | 0.0011 | 0.2052 | 0.1000 |
| old | actual | 17-30 | top3_stress | 0.8000 | tau | 1077 | 0.0004 | 0.0000 | 0.0000 | 0.0001 | 0.0011 | 0.2061 | 0.1000 |
| old | own | all | - | 0.0000 | M | 2308 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | all | linear | 0.0000 | tau | 2308 | 0.0232 | 0.0101 | 0.0239 | 0.0336 | 0.0409 | 0.0000 | 0.5000 |
| old | own | all | linear | 0.5000 | tau | 2308 | 0.0232 | 0.0101 | 0.0239 | 0.0336 | 0.0409 | 0.0000 | 0.5000 |
| old | own | all | linear | 0.8000 | tau | 2308 | 0.0232 | 0.0101 | 0.0239 | 0.0336 | 0.0409 | 0.0000 | 0.5000 |
| old | own | all | concave | 0.0000 | tau | 2308 | 0.0208 | 0.0079 | 0.0213 | 0.0311 | 0.0378 | 0.0000 | 0.6599 |
| old | own | all | concave | 0.5000 | tau | 2308 | 0.0208 | 0.0079 | 0.0213 | 0.0311 | 0.0378 | 0.0000 | 0.6599 |
| old | own | all | concave | 0.8000 | tau | 2308 | 0.0208 | 0.0079 | 0.0213 | 0.0311 | 0.0378 | 0.0000 | 0.6599 |
| old | own | all | convex | 0.0000 | tau | 2308 | 0.0209 | 0.0072 | 0.0189 | 0.0314 | 0.0416 | 0.0000 | 0.3391 |
| old | own | all | convex | 0.5000 | tau | 2308 | 0.0209 | 0.0072 | 0.0189 | 0.0314 | 0.0416 | 0.0000 | 0.3391 |
| old | own | all | convex | 0.8000 | tau | 2308 | 0.0209 | 0.0072 | 0.0189 | 0.0314 | 0.0416 | 0.0000 | 0.3391 |
| old | own | all | top3_stress | 0.0000 | tau | 2308 | 0.0081 | 0.0000 | 0.0027 | 0.0141 | 0.0254 | 0.0000 | 0.1000 |
| old | own | all | top3_stress | 0.5000 | tau | 2308 | 0.0081 | 0.0000 | 0.0027 | 0.0141 | 0.0254 | 0.0702 | 0.1000 |
| old | own | all | top3_stress | 0.8000 | tau | 2308 | 0.0081 | 0.0000 | 0.0027 | 0.0141 | 0.0254 | 0.0702 | 0.1000 |
| old | own | 1-3 | - | 0.0000 | M | 228 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 1-3 | linear | 0.0000 | tau | 228 | 0.0037 | 0.0019 | 0.0028 | 0.0045 | 0.0071 | 0.0000 | 0.5000 |
| old | own | 1-3 | linear | 0.5000 | tau | 228 | 0.0037 | 0.0019 | 0.0028 | 0.0045 | 0.0071 | 0.0000 | 0.5000 |
| old | own | 1-3 | linear | 0.8000 | tau | 228 | 0.0037 | 0.0019 | 0.0028 | 0.0045 | 0.0071 | 0.0000 | 0.5000 |
| old | own | 1-3 | concave | 0.0000 | tau | 228 | 0.0020 | 0.0011 | 0.0015 | 0.0024 | 0.0039 | 0.0000 | 0.6599 |
| old | own | 1-3 | concave | 0.5000 | tau | 228 | 0.0020 | 0.0011 | 0.0015 | 0.0024 | 0.0039 | 0.0000 | 0.6599 |
| old | own | 1-3 | concave | 0.8000 | tau | 228 | 0.0020 | 0.0011 | 0.0015 | 0.0024 | 0.0039 | 0.0000 | 0.6599 |
| old | own | 1-3 | convex | 0.0000 | tau | 228 | 0.0063 | 0.0033 | 0.0047 | 0.0076 | 0.0119 | 0.0000 | 0.3391 |
| old | own | 1-3 | convex | 0.5000 | tau | 228 | 0.0063 | 0.0033 | 0.0047 | 0.0076 | 0.0119 | 0.0000 | 0.3391 |
| old | own | 1-3 | convex | 0.8000 | tau | 228 | 0.0063 | 0.0033 | 0.0047 | 0.0076 | 0.0119 | 0.0000 | 0.3391 |
| old | own | 1-3 | top3_stress | 0.0000 | tau | 228 | 0.0056 | 0.0005 | 0.0026 | 0.0071 | 0.0141 | 0.0000 | 0.1000 |
| old | own | 1-3 | top3_stress | 0.5000 | tau | 228 | 0.0056 | 0.0005 | 0.0026 | 0.0071 | 0.0141 | 0.0088 | 0.1000 |
| old | own | 1-3 | top3_stress | 0.8000 | tau | 228 | 0.0056 | 0.0005 | 0.0026 | 0.0071 | 0.0141 | 0.0088 | 0.1000 |
| old | own | 4-10 | - | 0.0000 | M | 564 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 4-10 | linear | 0.0000 | tau | 564 | 0.0161 | 0.0072 | 0.0134 | 0.0242 | 0.0305 | 0.0000 | 0.5000 |
| old | own | 4-10 | linear | 0.5000 | tau | 564 | 0.0161 | 0.0072 | 0.0134 | 0.0242 | 0.0305 | 0.0000 | 0.5000 |
| old | own | 4-10 | linear | 0.8000 | tau | 564 | 0.0161 | 0.0072 | 0.0134 | 0.0242 | 0.0305 | 0.0000 | 0.5000 |
| old | own | 4-10 | concave | 0.0000 | tau | 564 | 0.0094 | 0.0040 | 0.0076 | 0.0142 | 0.0182 | 0.0000 | 0.6599 |
| old | own | 4-10 | concave | 0.5000 | tau | 564 | 0.0094 | 0.0040 | 0.0076 | 0.0142 | 0.0182 | 0.0000 | 0.6599 |
| old | own | 4-10 | concave | 0.8000 | tau | 564 | 0.0094 | 0.0040 | 0.0076 | 0.0142 | 0.0182 | 0.0000 | 0.6599 |
| old | own | 4-10 | convex | 0.0000 | tau | 564 | 0.0241 | 0.0117 | 0.0213 | 0.0356 | 0.0438 | 0.0000 | 0.3391 |
| old | own | 4-10 | convex | 0.5000 | tau | 564 | 0.0241 | 0.0117 | 0.0213 | 0.0356 | 0.0438 | 0.0000 | 0.3391 |
| old | own | 4-10 | convex | 0.8000 | tau | 564 | 0.0241 | 0.0117 | 0.0213 | 0.0356 | 0.0438 | 0.0000 | 0.3391 |
| old | own | 4-10 | top3_stress | 0.0000 | tau | 564 | 0.0208 | 0.0131 | 0.0205 | 0.0277 | 0.0328 | 0.0000 | 0.1000 |
| old | own | 4-10 | top3_stress | 0.5000 | tau | 564 | 0.0208 | 0.0131 | 0.0205 | 0.0277 | 0.0328 | 0.0000 | 0.1000 |
| old | own | 4-10 | top3_stress | 0.8000 | tau | 564 | 0.0208 | 0.0131 | 0.0205 | 0.0277 | 0.0328 | 0.0000 | 0.1000 |
| old | own | 11-16 | - | 0.0000 | M | 439 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 11-16 | linear | 0.0000 | tau | 439 | 0.0313 | 0.0234 | 0.0303 | 0.0372 | 0.0482 | 0.0000 | 0.5000 |
| old | own | 11-16 | linear | 0.5000 | tau | 439 | 0.0313 | 0.0234 | 0.0303 | 0.0372 | 0.0482 | 0.0000 | 0.5000 |
| old | own | 11-16 | linear | 0.8000 | tau | 439 | 0.0313 | 0.0234 | 0.0303 | 0.0372 | 0.0482 | 0.0000 | 0.5000 |
| old | own | 11-16 | concave | 0.0000 | tau | 439 | 0.0211 | 0.0151 | 0.0201 | 0.0261 | 0.0327 | 0.0000 | 0.6599 |
| old | own | 11-16 | concave | 0.5000 | tau | 439 | 0.0211 | 0.0151 | 0.0201 | 0.0261 | 0.0327 | 0.0000 | 0.6599 |
| old | own | 11-16 | concave | 0.8000 | tau | 439 | 0.0211 | 0.0151 | 0.0201 | 0.0261 | 0.0327 | 0.0000 | 0.6599 |
| old | own | 11-16 | convex | 0.0000 | tau | 439 | 0.0359 | 0.0267 | 0.0343 | 0.0425 | 0.0576 | 0.0000 | 0.3391 |
| old | own | 11-16 | convex | 0.5000 | tau | 439 | 0.0359 | 0.0267 | 0.0343 | 0.0425 | 0.0576 | 0.0000 | 0.3391 |
| old | own | 11-16 | convex | 0.8000 | tau | 439 | 0.0359 | 0.0267 | 0.0343 | 0.0425 | 0.0576 | 0.0000 | 0.3391 |
| old | own | 11-16 | top3_stress | 0.0000 | tau | 439 | 0.0113 | 0.0051 | 0.0084 | 0.0166 | 0.0231 | 0.0000 | 0.1000 |
| old | own | 11-16 | top3_stress | 0.5000 | tau | 439 | 0.0113 | 0.0051 | 0.0084 | 0.0166 | 0.0231 | 0.0000 | 0.1000 |
| old | own | 11-16 | top3_stress | 0.8000 | tau | 439 | 0.0113 | 0.0051 | 0.0084 | 0.0166 | 0.0231 | 0.0000 | 0.1000 |
| old | own | 17-30 | - | 0.0000 | M | 1077 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 17-30 | linear | 0.0000 | tau | 1077 | 0.0278 | 0.0195 | 0.0281 | 0.0371 | 0.0426 | 0.0000 | 0.5000 |
| old | own | 17-30 | linear | 0.5000 | tau | 1077 | 0.0278 | 0.0195 | 0.0281 | 0.0371 | 0.0426 | 0.0000 | 0.5000 |
| old | own | 17-30 | linear | 0.8000 | tau | 1077 | 0.0278 | 0.0195 | 0.0281 | 0.0371 | 0.0426 | 0.0000 | 0.5000 |
| old | own | 17-30 | concave | 0.0000 | tau | 1077 | 0.0306 | 0.0251 | 0.0307 | 0.0360 | 0.0432 | 0.0000 | 0.6599 |
| old | own | 17-30 | concave | 0.5000 | tau | 1077 | 0.0306 | 0.0251 | 0.0307 | 0.0360 | 0.0432 | 0.0000 | 0.6599 |
| old | own | 17-30 | concave | 0.8000 | tau | 1077 | 0.0306 | 0.0251 | 0.0307 | 0.0360 | 0.0432 | 0.0000 | 0.6599 |
| old | own | 17-30 | convex | 0.0000 | tau | 1077 | 0.0162 | 0.0050 | 0.0147 | 0.0249 | 0.0332 | 0.0000 | 0.3391 |
| old | own | 17-30 | convex | 0.5000 | tau | 1077 | 0.0162 | 0.0050 | 0.0147 | 0.0249 | 0.0332 | 0.0000 | 0.3391 |
| old | own | 17-30 | convex | 0.8000 | tau | 1077 | 0.0162 | 0.0050 | 0.0147 | 0.0249 | 0.0332 | 0.0000 | 0.3391 |
| old | own | 17-30 | top3_stress | 0.0000 | tau | 1077 | 0.0007 | 0.0000 | 0.0000 | 0.0006 | 0.0021 | 0.0000 | 0.1000 |
| old | own | 17-30 | top3_stress | 0.5000 | tau | 1077 | 0.0007 | 0.0000 | 0.0000 | 0.0006 | 0.0021 | 0.1486 | 0.1000 |
| old | own | 17-30 | top3_stress | 0.8000 | tau | 1077 | 0.0007 | 0.0000 | 0.0000 | 0.0006 | 0.0021 | 0.1486 | 0.1000 |
| new | actual | all | - | 0.0000 | M | 2308 | 0.0026 | -0.0000 | 0.0000 | 0.0000 | 0.0068 |  |  |
| new | actual | all | linear | 0.0000 | tau | 2308 | 0.0142 | 0.0000 | 0.0047 | 0.0270 | 0.0419 | 0.0000 | 0.5000 |
| new | actual | all | linear | 0.5000 | tau | 2308 | 0.0136 | 0.0000 | 0.0046 | 0.0255 | 0.0410 | 0.0251 | 0.5000 |
| new | actual | all | linear | 0.8000 | tau | 2308 | 0.0132 | 0.0000 | 0.0043 | 0.0243 | 0.0407 | 0.0316 | 0.5000 |
| new | actual | all | concave | 0.0000 | tau | 2308 | 0.0137 | 0.0000 | 0.0049 | 0.0284 | 0.0374 | 0.0000 | 0.6599 |
| new | actual | all | concave | 0.5000 | tau | 2308 | 0.0128 | 0.0000 | 0.0039 | 0.0272 | 0.0361 | 0.0026 | 0.6599 |
| new | actual | all | concave | 0.8000 | tau | 2308 | 0.0123 | 0.0000 | 0.0035 | 0.0260 | 0.0356 | 0.0078 | 0.6599 |
| new | actual | all | convex | 0.0000 | tau | 2308 | 0.0119 | 0.0000 | 0.0029 | 0.0211 | 0.0402 | 0.0000 | 0.3391 |
| new | actual | all | convex | 0.5000 | tau | 2308 | 0.0115 | 0.0000 | 0.0029 | 0.0197 | 0.0392 | 0.0026 | 0.3391 |
| new | actual | all | convex | 0.8000 | tau | 2308 | 0.0112 | 0.0000 | 0.0028 | 0.0183 | 0.0384 | 0.0056 | 0.3391 |
| new | actual | all | top3_stress | 0.0000 | tau | 2308 | 0.0040 | 0.0000 | 0.0000 | 0.0071 | 0.0188 | 0.0000 | 0.1000 |
| new | actual | all | top3_stress | 0.5000 | tau | 2308 | 0.0039 | 0.0000 | 0.0000 | 0.0067 | 0.0183 | 0.0771 | 0.1000 |
| new | actual | all | top3_stress | 0.8000 | tau | 2308 | 0.0038 | 0.0000 | 0.0000 | 0.0063 | 0.0179 | 0.0776 | 0.1000 |
| new | actual | 1-3 | - | 0.0000 | M | 228 | -0.0001 | -0.0000 | -0.0000 | 0.0000 | 0.0041 |  |  |
| new | actual | 1-3 | linear | 0.0000 | tau | 228 | -0.0024 | -0.0032 | -0.0010 | 0.0001 | 0.0014 | 0.0000 | 0.5000 |
| new | actual | 1-3 | linear | 0.5000 | tau | 228 | -0.0023 | -0.0032 | -0.0010 | 0.0000 | 0.0005 | 0.0833 | 0.5000 |
| new | actual | 1-3 | linear | 0.8000 | tau | 228 | -0.0023 | -0.0032 | -0.0013 | -0.0000 | 0.0002 | 0.1140 | 0.5000 |
| new | actual | 1-3 | concave | 0.0000 | tau | 228 | -0.0014 | -0.0017 | -0.0006 | 0.0001 | 0.0034 | 0.0000 | 0.6599 |
| new | actual | 1-3 | concave | 0.5000 | tau | 228 | -0.0013 | -0.0016 | -0.0006 | 0.0001 | 0.0018 | 0.0175 | 0.6599 |
| new | actual | 1-3 | concave | 0.8000 | tau | 228 | -0.0013 | -0.0016 | -0.0005 | 0.0000 | 0.0005 | 0.0307 | 0.6599 |
| new | actual | 1-3 | convex | 0.0000 | tau | 228 | -0.0039 | -0.0059 | -0.0023 | -0.0003 | 0.0001 | 0.0000 | 0.3391 |
| new | actual | 1-3 | convex | 0.5000 | tau | 228 | -0.0038 | -0.0059 | -0.0023 | -0.0003 | 0.0001 | 0.0044 | 0.3391 |
| new | actual | 1-3 | convex | 0.8000 | tau | 228 | -0.0038 | -0.0060 | -0.0024 | -0.0003 | 0.0001 | 0.0263 | 0.3391 |
| new | actual | 1-3 | top3_stress | 0.0000 | tau | 228 | -0.0062 | -0.0102 | -0.0041 | -0.0007 | 0.0000 | 0.0000 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.5000 | tau | 228 | -0.0062 | -0.0102 | -0.0041 | -0.0007 | 0.0000 | 0.0702 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.8000 | tau | 228 | -0.0062 | -0.0102 | -0.0041 | -0.0007 | 0.0000 | 0.0702 | 0.1000 |
| new | actual | 4-10 | - | 0.0000 | M | 564 | 0.0019 | -0.0000 | 0.0000 | 0.0004 | 0.0095 |  |  |
| new | actual | 4-10 | linear | 0.0000 | tau | 564 | 0.0035 | 0.0000 | 0.0014 | 0.0066 | 0.0141 | 0.0000 | 0.5000 |
| new | actual | 4-10 | linear | 0.5000 | tau | 564 | 0.0030 | -0.0000 | 0.0007 | 0.0061 | 0.0121 | 0.0674 | 0.5000 |
| new | actual | 4-10 | linear | 0.8000 | tau | 564 | 0.0027 | -0.0000 | 0.0007 | 0.0057 | 0.0108 | 0.0798 | 0.5000 |
| new | actual | 4-10 | concave | 0.0000 | tau | 564 | 0.0031 | 0.0000 | 0.0013 | 0.0053 | 0.0110 | 0.0000 | 0.6599 |
| new | actual | 4-10 | concave | 0.5000 | tau | 564 | 0.0025 | 0.0000 | 0.0011 | 0.0043 | 0.0092 | 0.0035 | 0.6599 |
| new | actual | 4-10 | concave | 0.8000 | tau | 564 | 0.0021 | 0.0000 | 0.0005 | 0.0039 | 0.0078 | 0.0177 | 0.6599 |
| new | actual | 4-10 | convex | 0.0000 | tau | 564 | 0.0036 | -0.0001 | 0.0009 | 0.0081 | 0.0155 | 0.0000 | 0.3391 |
| new | actual | 4-10 | convex | 0.5000 | tau | 564 | 0.0033 | -0.0001 | 0.0009 | 0.0073 | 0.0145 | 0.0035 | 0.3391 |
| new | actual | 4-10 | convex | 0.8000 | tau | 564 | 0.0031 | -0.0001 | 0.0009 | 0.0072 | 0.0136 | 0.0053 | 0.3391 |
| new | actual | 4-10 | top3_stress | 0.0000 | tau | 564 | 0.0015 | -0.0003 | 0.0001 | 0.0066 | 0.0125 | 0.0000 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.5000 | tau | 564 | 0.0014 | -0.0003 | 0.0002 | 0.0064 | 0.0118 | 0.0266 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.8000 | tau | 564 | 0.0013 | -0.0003 | 0.0002 | 0.0063 | 0.0117 | 0.0266 | 0.1000 |
| new | actual | 11-16 | - | 0.0000 | M | 439 | 0.0029 | -0.0000 | 0.0000 | 0.0000 | 0.0053 |  |  |
| new | actual | 11-16 | linear | 0.0000 | tau | 439 | 0.0230 | 0.0009 | 0.0216 | 0.0389 | 0.0469 | 0.0000 | 0.5000 |
| new | actual | 11-16 | linear | 0.5000 | tau | 439 | 0.0223 | 0.0009 | 0.0204 | 0.0382 | 0.0465 | 0.0023 | 0.5000 |
| new | actual | 11-16 | linear | 0.8000 | tau | 439 | 0.0218 | 0.0009 | 0.0190 | 0.0374 | 0.0460 | 0.0023 | 0.5000 |
| new | actual | 11-16 | concave | 0.0000 | tau | 439 | 0.0161 | 0.0006 | 0.0151 | 0.0270 | 0.0337 | 0.0000 | 0.6599 |
| new | actual | 11-16 | concave | 0.5000 | tau | 439 | 0.0152 | 0.0006 | 0.0139 | 0.0256 | 0.0326 | 0.0000 | 0.6599 |
| new | actual | 11-16 | concave | 0.8000 | tau | 439 | 0.0146 | 0.0006 | 0.0128 | 0.0249 | 0.0318 | 0.0023 | 0.6599 |
| new | actual | 11-16 | convex | 0.0000 | tau | 439 | 0.0274 | 0.0007 | 0.0261 | 0.0434 | 0.0549 | 0.0000 | 0.3391 |
| new | actual | 11-16 | convex | 0.5000 | tau | 439 | 0.0269 | 0.0007 | 0.0254 | 0.0429 | 0.0545 | 0.0000 | 0.3391 |
| new | actual | 11-16 | convex | 0.8000 | tau | 439 | 0.0266 | 0.0007 | 0.0249 | 0.0424 | 0.0542 | 0.0000 | 0.3391 |
| new | actual | 11-16 | top3_stress | 0.0000 | tau | 439 | 0.0152 | 0.0000 | 0.0156 | 0.0229 | 0.0304 | 0.0000 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.5000 | tau | 439 | 0.0151 | 0.0000 | 0.0155 | 0.0224 | 0.0303 | 0.0068 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.8000 | tau | 439 | 0.0150 | 0.0001 | 0.0155 | 0.0222 | 0.0303 | 0.0091 | 0.1000 |
| new | actual | 17-30 | - | 0.0000 | M | 1077 | 0.0035 | -0.0000 | 0.0000 | 0.0000 | 0.0016 |  |  |
| new | actual | 17-30 | linear | 0.0000 | tau | 1077 | 0.0198 | 0.0000 | 0.0192 | 0.0347 | 0.0450 | 0.0000 | 0.5000 |
| new | actual | 17-30 | linear | 0.5000 | tau | 1077 | 0.0189 | 0.0000 | 0.0183 | 0.0326 | 0.0438 | 0.0000 | 0.5000 |
| new | actual | 17-30 | linear | 0.8000 | tau | 1077 | 0.0184 | 0.0000 | 0.0168 | 0.0317 | 0.0433 | 0.0009 | 0.5000 |
| new | actual | 17-30 | concave | 0.0000 | tau | 1077 | 0.0214 | 0.0000 | 0.0246 | 0.0353 | 0.0453 | 0.0000 | 0.6599 |
| new | actual | 17-30 | concave | 0.5000 | tau | 1077 | 0.0203 | 0.0000 | 0.0237 | 0.0345 | 0.0422 | 0.0000 | 0.6599 |
| new | actual | 17-30 | concave | 0.8000 | tau | 1077 | 0.0196 | 0.0000 | 0.0220 | 0.0340 | 0.0418 | 0.0000 | 0.6599 |
| new | actual | 17-30 | convex | 0.0000 | tau | 1077 | 0.0133 | 0.0000 | 0.0051 | 0.0229 | 0.0379 | 0.0000 | 0.3391 |
| new | actual | 17-30 | convex | 0.5000 | tau | 1077 | 0.0127 | 0.0000 | 0.0051 | 0.0217 | 0.0369 | 0.0028 | 0.3391 |
| new | actual | 17-30 | convex | 0.8000 | tau | 1077 | 0.0124 | 0.0000 | 0.0049 | 0.0202 | 0.0351 | 0.0037 | 0.3391 |
| new | actual | 17-30 | top3_stress | 0.0000 | tau | 1077 | 0.0029 | 0.0000 | 0.0000 | 0.0025 | 0.0101 | 0.0000 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.5000 | tau | 1077 | 0.0027 | 0.0000 | 0.0000 | 0.0025 | 0.0087 | 0.1337 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.8000 | tau | 1077 | 0.0026 | 0.0000 | 0.0000 | 0.0025 | 0.0082 | 0.1337 | 0.1000 |
| new | own | all | - | 0.0000 | M | 2308 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | all | linear | 0.0000 | tau | 2308 | 0.0215 | 0.0008 | 0.0186 | 0.0369 | 0.0492 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.5000 | tau | 2308 | 0.0215 | 0.0008 | 0.0186 | 0.0369 | 0.0492 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.8000 | tau | 2308 | 0.0215 | 0.0008 | 0.0186 | 0.0369 | 0.0492 | 0.0000 | 0.5000 |
| new | own | all | concave | 0.0000 | tau | 2308 | 0.0198 | 0.0007 | 0.0211 | 0.0333 | 0.0426 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.5000 | tau | 2308 | 0.0198 | 0.0007 | 0.0211 | 0.0333 | 0.0426 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.8000 | tau | 2308 | 0.0198 | 0.0007 | 0.0211 | 0.0333 | 0.0426 | 0.0000 | 0.6599 |
| new | own | all | convex | 0.0000 | tau | 2308 | 0.0182 | 0.0005 | 0.0101 | 0.0310 | 0.0507 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.5000 | tau | 2308 | 0.0182 | 0.0005 | 0.0101 | 0.0310 | 0.0507 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.8000 | tau | 2308 | 0.0182 | 0.0005 | 0.0101 | 0.0310 | 0.0507 | 0.0000 | 0.3391 |
| new | own | all | top3_stress | 0.0000 | tau | 2308 | 0.0059 | 0.0000 | 0.0008 | 0.0114 | 0.0217 | 0.0000 | 0.1000 |
| new | own | all | top3_stress | 0.5000 | tau | 2308 | 0.0059 | 0.0000 | 0.0008 | 0.0114 | 0.0217 | 0.0914 | 0.1000 |
| new | own | all | top3_stress | 0.8000 | tau | 2308 | 0.0059 | 0.0000 | 0.0008 | 0.0114 | 0.0217 | 0.0914 | 0.1000 |
| new | own | 1-3 | - | 0.0000 | M | 228 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 1-3 | linear | 0.0000 | tau | 228 | -0.0019 | -0.0031 | -0.0012 | -0.0002 | 0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.5000 | tau | 228 | -0.0019 | -0.0031 | -0.0012 | -0.0002 | 0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.8000 | tau | 228 | -0.0019 | -0.0031 | -0.0012 | -0.0002 | 0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | concave | 0.0000 | tau | 228 | -0.0009 | -0.0015 | -0.0006 | -0.0001 | 0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.5000 | tau | 228 | -0.0009 | -0.0015 | -0.0006 | -0.0001 | 0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.8000 | tau | 228 | -0.0009 | -0.0015 | -0.0006 | -0.0001 | 0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | convex | 0.0000 | tau | 228 | -0.0035 | -0.0059 | -0.0023 | -0.0004 | 0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.5000 | tau | 228 | -0.0035 | -0.0059 | -0.0023 | -0.0004 | 0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.8000 | tau | 228 | -0.0035 | -0.0059 | -0.0023 | -0.0004 | 0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | top3_stress | 0.0000 | tau | 228 | -0.0063 | -0.0101 | -0.0041 | -0.0008 | 0.0000 | 0.0000 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.5000 | tau | 228 | -0.0063 | -0.0101 | -0.0041 | -0.0008 | -0.0000 | 0.0439 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.8000 | tau | 228 | -0.0063 | -0.0101 | -0.0041 | -0.0008 | -0.0000 | 0.0439 | 0.1000 |
| new | own | 4-10 | - | 0.0000 | M | 564 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 4-10 | linear | 0.0000 | tau | 564 | 0.0030 | -0.0000 | 0.0005 | 0.0060 | 0.0102 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.5000 | tau | 564 | 0.0030 | -0.0000 | 0.0005 | 0.0060 | 0.0102 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.8000 | tau | 564 | 0.0030 | -0.0000 | 0.0005 | 0.0060 | 0.0102 | 0.0000 | 0.5000 |
| new | own | 4-10 | concave | 0.0000 | tau | 564 | 0.0019 | -0.0000 | 0.0003 | 0.0036 | 0.0063 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.5000 | tau | 564 | 0.0019 | -0.0000 | 0.0003 | 0.0036 | 0.0063 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.8000 | tau | 564 | 0.0019 | -0.0000 | 0.0003 | 0.0036 | 0.0063 | 0.0000 | 0.6599 |
| new | own | 4-10 | convex | 0.0000 | tau | 564 | 0.0039 | -0.0000 | 0.0007 | 0.0085 | 0.0145 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.5000 | tau | 564 | 0.0039 | -0.0000 | 0.0007 | 0.0085 | 0.0145 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.8000 | tau | 564 | 0.0039 | -0.0000 | 0.0007 | 0.0085 | 0.0145 | 0.0000 | 0.3391 |
| new | own | 4-10 | top3_stress | 0.0000 | tau | 564 | 0.0019 | -0.0002 | 0.0002 | 0.0077 | 0.0132 | 0.0000 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.5000 | tau | 564 | 0.0019 | -0.0002 | 0.0002 | 0.0077 | 0.0132 | 0.0461 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.8000 | tau | 564 | 0.0019 | -0.0002 | 0.0002 | 0.0077 | 0.0132 | 0.0461 | 0.1000 |
| new | own | 11-16 | - | 0.0000 | M | 439 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 11-16 | linear | 0.0000 | tau | 439 | 0.0321 | 0.0148 | 0.0313 | 0.0444 | 0.0567 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.5000 | tau | 439 | 0.0321 | 0.0148 | 0.0313 | 0.0444 | 0.0567 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.8000 | tau | 439 | 0.0321 | 0.0148 | 0.0313 | 0.0444 | 0.0567 | 0.0000 | 0.5000 |
| new | own | 11-16 | concave | 0.0000 | tau | 439 | 0.0211 | 0.0092 | 0.0203 | 0.0301 | 0.0384 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.5000 | tau | 439 | 0.0211 | 0.0092 | 0.0203 | 0.0301 | 0.0384 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.8000 | tau | 439 | 0.0211 | 0.0092 | 0.0203 | 0.0301 | 0.0384 | 0.0000 | 0.6599 |
| new | own | 11-16 | convex | 0.0000 | tau | 439 | 0.0390 | 0.0197 | 0.0375 | 0.0519 | 0.0670 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.5000 | tau | 439 | 0.0390 | 0.0197 | 0.0375 | 0.0519 | 0.0670 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.8000 | tau | 439 | 0.0390 | 0.0197 | 0.0375 | 0.0519 | 0.0670 | 0.0000 | 0.3391 |
| new | own | 11-16 | top3_stress | 0.0000 | tau | 439 | 0.0204 | 0.0127 | 0.0188 | 0.0245 | 0.0342 | 0.0000 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.5000 | tau | 439 | 0.0204 | 0.0127 | 0.0188 | 0.0245 | 0.0342 | 0.0091 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.8000 | tau | 439 | 0.0204 | 0.0127 | 0.0188 | 0.0245 | 0.0342 | 0.0091 | 0.1000 |
| new | own | 17-30 | - | 0.0000 | M | 1077 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 17-30 | linear | 0.0000 | tau | 1077 | 0.0317 | 0.0195 | 0.0306 | 0.0420 | 0.0540 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.5000 | tau | 1077 | 0.0317 | 0.0195 | 0.0306 | 0.0420 | 0.0540 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.8000 | tau | 1077 | 0.0317 | 0.0195 | 0.0306 | 0.0420 | 0.0540 | 0.0000 | 0.5000 |
| new | own | 17-30 | concave | 0.0000 | tau | 1077 | 0.0329 | 0.0271 | 0.0328 | 0.0391 | 0.0463 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.5000 | tau | 1077 | 0.0329 | 0.0271 | 0.0328 | 0.0391 | 0.0463 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.8000 | tau | 1077 | 0.0329 | 0.0271 | 0.0328 | 0.0391 | 0.0463 | 0.0000 | 0.6599 |
| new | own | 17-30 | convex | 0.0000 | tau | 1077 | 0.0219 | 0.0050 | 0.0163 | 0.0333 | 0.0505 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.5000 | tau | 1077 | 0.0219 | 0.0050 | 0.0163 | 0.0333 | 0.0505 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.8000 | tau | 1077 | 0.0219 | 0.0050 | 0.0163 | 0.0333 | 0.0505 | 0.0000 | 0.3391 |
| new | own | 17-30 | top3_stress | 0.0000 | tau | 1077 | 0.0046 | 0.0000 | 0.0004 | 0.0060 | 0.0149 | 0.0000 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.5000 | tau | 1077 | 0.0046 | 0.0000 | 0.0004 | 0.0060 | 0.0149 | 0.1588 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.8000 | tau | 1077 | 0.0046 | 0.0000 | 0.0004 | 0.0060 | 0.0149 | 0.1588 | 0.1000 |
| delta | actual | all | - | 0.0000 | M | 2308 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0013 |  |  |
| delta | actual | all | linear | 0.0000 | tau | 2308 | -0.0024 | -0.0075 | 0.0000 | 0.0008 | 0.0086 | 0.0000 | 0.5000 |
| delta | actual | all | linear | 0.5000 | tau | 2308 | -0.0024 | -0.0075 | 0.0000 | 0.0009 | 0.0082 | 0.0100 | 0.5000 |
| delta | actual | all | linear | 0.8000 | tau | 2308 | -0.0024 | -0.0074 | 0.0000 | 0.0009 | 0.0076 | 0.0143 | 0.5000 |
| delta | actual | all | concave | 0.0000 | tau | 2308 | -0.0014 | -0.0045 | 0.0000 | 0.0008 | 0.0058 | 0.0000 | 0.6599 |
| delta | actual | all | concave | 0.5000 | tau | 2308 | -0.0014 | -0.0043 | 0.0000 | 0.0005 | 0.0052 | 0.0234 | 0.6599 |
| delta | actual | all | concave | 0.8000 | tau | 2308 | -0.0014 | -0.0042 | 0.0000 | 0.0005 | 0.0049 | 0.0381 | 0.6599 |
| delta | actual | all | convex | 0.0000 | tau | 2308 | -0.0036 | -0.0114 | 0.0000 | 0.0016 | 0.0117 | 0.0000 | 0.3391 |
| delta | actual | all | convex | 0.5000 | tau | 2308 | -0.0036 | -0.0114 | 0.0000 | 0.0017 | 0.0112 | 0.0052 | 0.3391 |
| delta | actual | all | convex | 0.8000 | tau | 2308 | -0.0036 | -0.0114 | 0.0000 | 0.0018 | 0.0107 | 0.0078 | 0.3391 |
| delta | actual | all | top3_stress | 0.0000 | tau | 2308 | -0.0033 | -0.0094 | 0.0000 | 0.0009 | 0.0102 | 0.0000 | 0.1000 |
| delta | actual | all | top3_stress | 0.5000 | tau | 2308 | -0.0033 | -0.0093 | 0.0000 | 0.0009 | 0.0102 | 0.0412 | 0.1000 |
| delta | actual | all | top3_stress | 0.8000 | tau | 2308 | -0.0033 | -0.0090 | 0.0000 | 0.0009 | 0.0100 | 0.0420 | 0.1000 |
| delta | actual | 1-3 | - | 0.0000 | M | 228 | -0.0007 | -0.0000 | -0.0000 | 0.0000 | 0.0027 |  |  |
| delta | actual | 1-3 | linear | 0.0000 | tau | 228 | -0.0059 | -0.0078 | -0.0033 | -0.0014 | -0.0008 | 0.0000 | 0.5000 |
| delta | actual | 1-3 | linear | 0.5000 | tau | 228 | -0.0058 | -0.0077 | -0.0038 | -0.0015 | -0.0008 | 0.0219 | 0.5000 |
| delta | actual | 1-3 | linear | 0.8000 | tau | 228 | -0.0057 | -0.0078 | -0.0041 | -0.0016 | -0.0008 | 0.0263 | 0.5000 |
| delta | actual | 1-3 | concave | 0.0000 | tau | 228 | -0.0035 | -0.0044 | -0.0021 | -0.0007 | 0.0008 | 0.0000 | 0.6599 |
| delta | actual | 1-3 | concave | 0.5000 | tau | 228 | -0.0033 | -0.0041 | -0.0019 | -0.0007 | -0.0001 | 0.0570 | 0.6599 |
| delta | actual | 1-3 | concave | 0.8000 | tau | 228 | -0.0032 | -0.0041 | -0.0019 | -0.0009 | -0.0005 | 0.1184 | 0.6599 |
| delta | actual | 1-3 | convex | 0.0000 | tau | 228 | -0.0096 | -0.0137 | -0.0068 | -0.0027 | -0.0012 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | convex | 0.5000 | tau | 228 | -0.0095 | -0.0137 | -0.0070 | -0.0028 | -0.0013 | 0.0088 | 0.3391 |
| delta | actual | 1-3 | convex | 0.8000 | tau | 228 | -0.0094 | -0.0136 | -0.0070 | -0.0028 | -0.0013 | 0.0088 | 0.3391 |
| delta | actual | 1-3 | top3_stress | 0.0000 | tau | 228 | -0.0117 | -0.0174 | -0.0071 | -0.0012 | -0.0001 | 0.0000 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.5000 | tau | 228 | -0.0117 | -0.0177 | -0.0071 | -0.0012 | -0.0001 | 0.0132 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.8000 | tau | 228 | -0.0117 | -0.0177 | -0.0071 | -0.0012 | -0.0001 | 0.0132 | 0.1000 |
| delta | actual | 4-10 | - | 0.0000 | M | 564 | -0.0034 | -0.0002 | -0.0000 | 0.0000 | 0.0013 |  |  |
| delta | actual | 4-10 | linear | 0.0000 | tau | 564 | -0.0140 | -0.0204 | -0.0123 | -0.0068 | -0.0022 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | linear | 0.5000 | tau | 564 | -0.0131 | -0.0188 | -0.0122 | -0.0070 | -0.0032 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | linear | 0.8000 | tau | 564 | -0.0126 | -0.0182 | -0.0117 | -0.0071 | -0.0033 | 0.0018 | 0.5000 |
| delta | actual | 4-10 | concave | 0.0000 | tau | 564 | -0.0095 | -0.0127 | -0.0072 | -0.0037 | 0.0000 | 0.0000 | 0.6599 |
| delta | actual | 4-10 | concave | 0.5000 | tau | 564 | -0.0083 | -0.0124 | -0.0070 | -0.0037 | -0.0002 | 0.0496 | 0.6599 |
| delta | actual | 4-10 | concave | 0.8000 | tau | 564 | -0.0076 | -0.0114 | -0.0069 | -0.0037 | -0.0015 | 0.0585 | 0.6599 |
| delta | actual | 4-10 | convex | 0.0000 | tau | 564 | -0.0197 | -0.0273 | -0.0190 | -0.0113 | -0.0053 | 0.0000 | 0.3391 |
| delta | actual | 4-10 | convex | 0.5000 | tau | 564 | -0.0191 | -0.0270 | -0.0184 | -0.0113 | -0.0054 | 0.0035 | 0.3391 |
| delta | actual | 4-10 | convex | 0.8000 | tau | 564 | -0.0188 | -0.0266 | -0.0179 | -0.0112 | -0.0055 | 0.0071 | 0.3391 |
| delta | actual | 4-10 | top3_stress | 0.0000 | tau | 564 | -0.0181 | -0.0239 | -0.0169 | -0.0113 | -0.0037 | 0.0000 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.5000 | tau | 564 | -0.0179 | -0.0238 | -0.0167 | -0.0106 | -0.0036 | 0.0018 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.8000 | tau | 564 | -0.0178 | -0.0237 | -0.0166 | -0.0103 | -0.0036 | 0.0018 | 0.1000 |
| delta | actual | 11-16 | - | 0.0000 | M | 439 | 0.0007 | -0.0000 | 0.0000 | 0.0000 | 0.0002 |  |  |
| delta | actual | 11-16 | linear | 0.0000 | tau | 439 | 0.0003 | -0.0064 | 0.0000 | 0.0068 | 0.0137 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | linear | 0.5000 | tau | 439 | 0.0001 | -0.0062 | 0.0000 | 0.0065 | 0.0125 | 0.0023 | 0.5000 |
| delta | actual | 11-16 | linear | 0.8000 | tau | 439 | 0.0000 | -0.0055 | 0.0000 | 0.0062 | 0.0124 | 0.0091 | 0.5000 |
| delta | actual | 11-16 | concave | 0.0000 | tau | 439 | 0.0001 | -0.0046 | 0.0000 | 0.0038 | 0.0089 | 0.0000 | 0.6599 |
| delta | actual | 11-16 | concave | 0.5000 | tau | 439 | -0.0001 | -0.0045 | 0.0000 | 0.0037 | 0.0083 | 0.0068 | 0.6599 |
| delta | actual | 11-16 | concave | 0.8000 | tau | 439 | -0.0002 | -0.0043 | 0.0000 | 0.0035 | 0.0075 | 0.0068 | 0.6599 |
| delta | actual | 11-16 | convex | 0.0000 | tau | 439 | 0.0015 | -0.0061 | 0.0000 | 0.0104 | 0.0192 | 0.0000 | 0.3391 |
| delta | actual | 11-16 | convex | 0.5000 | tau | 439 | 0.0014 | -0.0061 | 0.0000 | 0.0102 | 0.0185 | 0.0091 | 0.3391 |
| delta | actual | 11-16 | convex | 0.8000 | tau | 439 | 0.0013 | -0.0056 | 0.0000 | 0.0100 | 0.0184 | 0.0137 | 0.3391 |
| delta | actual | 11-16 | top3_stress | 0.0000 | tau | 439 | 0.0063 | 0.0000 | 0.0059 | 0.0132 | 0.0185 | 0.0000 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.5000 | tau | 439 | 0.0063 | 0.0000 | 0.0059 | 0.0128 | 0.0182 | 0.0205 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.8000 | tau | 439 | 0.0063 | 0.0000 | 0.0060 | 0.0128 | 0.0182 | 0.0205 | 0.1000 |
| delta | actual | 17-30 | - | 0.0000 | M | 1077 | 0.0017 | -0.0000 | 0.0000 | 0.0000 | 0.0017 |  |  |
| delta | actual | 17-30 | linear | 0.0000 | tau | 1077 | 0.0034 | 0.0000 | 0.0000 | 0.0035 | 0.0106 | 0.0000 | 0.5000 |
| delta | actual | 17-30 | linear | 0.5000 | tau | 1077 | 0.0029 | 0.0000 | 0.0000 | 0.0033 | 0.0096 | 0.0158 | 0.5000 |
| delta | actual | 17-30 | linear | 0.8000 | tau | 1077 | 0.0027 | 0.0000 | 0.0000 | 0.0033 | 0.0091 | 0.0204 | 0.5000 |
| delta | actual | 17-30 | concave | 0.0000 | tau | 1077 | 0.0027 | 0.0000 | 0.0000 | 0.0023 | 0.0076 | 0.0000 | 0.6599 |
| delta | actual | 17-30 | concave | 0.5000 | tau | 1077 | 0.0022 | 0.0000 | 0.0000 | 0.0022 | 0.0066 | 0.0093 | 0.6599 |
| delta | actual | 17-30 | concave | 0.8000 | tau | 1077 | 0.0018 | 0.0000 | 0.0000 | 0.0020 | 0.0059 | 0.0232 | 0.6599 |
| delta | actual | 17-30 | convex | 0.0000 | tau | 1077 | 0.0040 | 0.0000 | 0.0000 | 0.0048 | 0.0131 | 0.0000 | 0.3391 |
| delta | actual | 17-30 | convex | 0.5000 | tau | 1077 | 0.0037 | 0.0000 | 0.0000 | 0.0046 | 0.0125 | 0.0037 | 0.3391 |
| delta | actual | 17-30 | convex | 0.8000 | tau | 1077 | 0.0035 | 0.0000 | 0.0000 | 0.0047 | 0.0121 | 0.0056 | 0.3391 |
| delta | actual | 17-30 | top3_stress | 0.0000 | tau | 1077 | 0.0024 | 0.0000 | 0.0000 | 0.0023 | 0.0085 | 0.0000 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.5000 | tau | 1077 | 0.0023 | 0.0000 | 0.0000 | 0.0023 | 0.0081 | 0.0761 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.8000 | tau | 1077 | 0.0022 | 0.0000 | 0.0000 | 0.0024 | 0.0078 | 0.0780 | 0.1000 |
| delta | own | all | - | 0.0000 | M | 2308 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | all | linear | 0.0000 | tau | 2308 | -0.0018 | -0.0082 | -0.0000 | 0.0034 | 0.0113 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.5000 | tau | 2308 | -0.0018 | -0.0082 | -0.0000 | 0.0034 | 0.0113 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.8000 | tau | 2308 | -0.0018 | -0.0082 | -0.0000 | 0.0034 | 0.0113 | 0.0000 | 0.5000 |
| delta | own | all | concave | 0.0000 | tau | 2308 | -0.0010 | -0.0047 | -0.0000 | 0.0019 | 0.0067 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.5000 | tau | 2308 | -0.0010 | -0.0047 | -0.0000 | 0.0019 | 0.0067 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.8000 | tau | 2308 | -0.0010 | -0.0047 | -0.0000 | 0.0019 | 0.0067 | 0.0000 | 0.6599 |
| delta | own | all | convex | 0.0000 | tau | 2308 | -0.0027 | -0.0128 | 0.0000 | 0.0057 | 0.0169 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.5000 | tau | 2308 | -0.0027 | -0.0128 | 0.0000 | 0.0057 | 0.0169 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.8000 | tau | 2308 | -0.0027 | -0.0128 | 0.0000 | 0.0057 | 0.0169 | 0.0000 | 0.3391 |
| delta | own | all | top3_stress | 0.0000 | tau | 2308 | -0.0022 | -0.0107 | 0.0000 | 0.0049 | 0.0140 | 0.0000 | 0.1000 |
| delta | own | all | top3_stress | 0.5000 | tau | 2308 | -0.0022 | -0.0107 | 0.0000 | 0.0049 | 0.0140 | 0.0191 | 0.1000 |
| delta | own | all | top3_stress | 0.8000 | tau | 2308 | -0.0022 | -0.0107 | 0.0000 | 0.0049 | 0.0140 | 0.0191 | 0.1000 |
| delta | own | 1-3 | - | 0.0000 | M | 228 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 1-3 | linear | 0.0000 | tau | 228 | -0.0056 | -0.0074 | -0.0042 | -0.0022 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.5000 | tau | 228 | -0.0056 | -0.0074 | -0.0042 | -0.0022 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.8000 | tau | 228 | -0.0056 | -0.0074 | -0.0042 | -0.0022 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | concave | 0.0000 | tau | 228 | -0.0030 | -0.0039 | -0.0022 | -0.0012 | -0.0008 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.5000 | tau | 228 | -0.0030 | -0.0039 | -0.0022 | -0.0012 | -0.0008 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.8000 | tau | 228 | -0.0030 | -0.0039 | -0.0022 | -0.0012 | -0.0008 | 0.0000 | 0.6599 |
| delta | own | 1-3 | convex | 0.0000 | tau | 228 | -0.0098 | -0.0130 | -0.0072 | -0.0037 | -0.0025 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.5000 | tau | 228 | -0.0098 | -0.0130 | -0.0072 | -0.0037 | -0.0025 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.8000 | tau | 228 | -0.0098 | -0.0130 | -0.0072 | -0.0037 | -0.0025 | 0.0000 | 0.3391 |
| delta | own | 1-3 | top3_stress | 0.0000 | tau | 228 | -0.0119 | -0.0177 | -0.0068 | -0.0012 | -0.0001 | 0.0000 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.5000 | tau | 228 | -0.0119 | -0.0177 | -0.0068 | -0.0012 | -0.0001 | 0.0044 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.8000 | tau | 228 | -0.0119 | -0.0177 | -0.0068 | -0.0012 | -0.0001 | 0.0044 | 0.1000 |
| delta | own | 4-10 | - | 0.0000 | M | 564 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 4-10 | linear | 0.0000 | tau | 564 | -0.0131 | -0.0180 | -0.0118 | -0.0078 | -0.0056 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.5000 | tau | 564 | -0.0131 | -0.0180 | -0.0118 | -0.0078 | -0.0056 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.8000 | tau | 564 | -0.0131 | -0.0180 | -0.0118 | -0.0078 | -0.0056 | 0.0000 | 0.5000 |
| delta | own | 4-10 | concave | 0.0000 | tau | 564 | -0.0075 | -0.0103 | -0.0067 | -0.0045 | -0.0031 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.5000 | tau | 564 | -0.0075 | -0.0103 | -0.0067 | -0.0045 | -0.0031 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.8000 | tau | 564 | -0.0075 | -0.0103 | -0.0067 | -0.0045 | -0.0031 | 0.0000 | 0.6599 |
| delta | own | 4-10 | convex | 0.0000 | tau | 564 | -0.0203 | -0.0271 | -0.0190 | -0.0125 | -0.0090 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.5000 | tau | 564 | -0.0203 | -0.0271 | -0.0190 | -0.0125 | -0.0090 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.8000 | tau | 564 | -0.0203 | -0.0271 | -0.0190 | -0.0125 | -0.0090 | 0.0000 | 0.3391 |
| delta | own | 4-10 | top3_stress | 0.0000 | tau | 564 | -0.0189 | -0.0240 | -0.0174 | -0.0122 | -0.0077 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.5000 | tau | 564 | -0.0189 | -0.0240 | -0.0174 | -0.0122 | -0.0077 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.8000 | tau | 564 | -0.0189 | -0.0240 | -0.0174 | -0.0122 | -0.0077 | 0.0000 | 0.1000 |
| delta | own | 11-16 | - | 0.0000 | M | 439 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 11-16 | linear | 0.0000 | tau | 439 | 0.0008 | -0.0098 | 0.0027 | 0.0101 | 0.0152 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.5000 | tau | 439 | 0.0008 | -0.0098 | 0.0027 | 0.0101 | 0.0152 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.8000 | tau | 439 | 0.0008 | -0.0098 | 0.0027 | 0.0101 | 0.0152 | 0.0000 | 0.5000 |
| delta | own | 11-16 | concave | 0.0000 | tau | 439 | 0.0000 | -0.0062 | 0.0010 | 0.0055 | 0.0089 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.5000 | tau | 439 | 0.0000 | -0.0062 | 0.0010 | 0.0055 | 0.0089 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.8000 | tau | 439 | 0.0000 | -0.0062 | 0.0010 | 0.0055 | 0.0089 | 0.0000 | 0.6599 |
| delta | own | 11-16 | convex | 0.0000 | tau | 439 | 0.0031 | -0.0119 | 0.0064 | 0.0162 | 0.0226 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.5000 | tau | 439 | 0.0031 | -0.0119 | 0.0064 | 0.0162 | 0.0226 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.8000 | tau | 439 | 0.0031 | -0.0119 | 0.0064 | 0.0162 | 0.0226 | 0.0000 | 0.3391 |
| delta | own | 11-16 | top3_stress | 0.0000 | tau | 439 | 0.0091 | 0.0006 | 0.0102 | 0.0167 | 0.0222 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.5000 | tau | 439 | 0.0091 | 0.0006 | 0.0102 | 0.0167 | 0.0222 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.8000 | tau | 439 | 0.0091 | 0.0006 | 0.0102 | 0.0167 | 0.0222 | 0.0000 | 0.1000 |
| delta | own | 17-30 | - | 0.0000 | M | 1077 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 17-30 | linear | 0.0000 | tau | 1077 | 0.0039 | 0.0000 | 0.0004 | 0.0064 | 0.0131 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.5000 | tau | 1077 | 0.0039 | 0.0000 | 0.0004 | 0.0064 | 0.0131 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.8000 | tau | 1077 | 0.0039 | 0.0000 | 0.0004 | 0.0064 | 0.0131 | 0.0000 | 0.5000 |
| delta | own | 17-30 | concave | 0.0000 | tau | 1077 | 0.0023 | 0.0000 | 0.0001 | 0.0039 | 0.0080 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.5000 | tau | 1077 | 0.0023 | 0.0000 | 0.0001 | 0.0039 | 0.0080 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.8000 | tau | 1077 | 0.0023 | 0.0000 | 0.0001 | 0.0039 | 0.0080 | 0.0000 | 0.6599 |
| delta | own | 17-30 | convex | 0.0000 | tau | 1077 | 0.0057 | 0.0000 | 0.0006 | 0.0090 | 0.0185 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.5000 | tau | 1077 | 0.0057 | 0.0000 | 0.0006 | 0.0090 | 0.0185 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.8000 | tau | 1077 | 0.0057 | 0.0000 | 0.0006 | 0.0090 | 0.0185 | 0.0000 | 0.3391 |
| delta | own | 17-30 | top3_stress | 0.0000 | tau | 1077 | 0.0039 | 0.0000 | 0.0004 | 0.0054 | 0.0120 | 0.0000 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.5000 | tau | 1077 | 0.0039 | 0.0000 | 0.0004 | 0.0054 | 0.0120 | 0.0399 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.8000 | tau | 1077 | 0.0039 | 0.0000 | 0.0004 | 0.0054 | 0.0120 | 0.0399 | 0.1000 |

## T5_attr_seeding

| rule | portfolio | seed_group | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| old | actual | <0.01 | B | dominance_positive | 0.7753 | 0.6892 | 0.8595 | 583 |
| old | actual | <0.01 | B | reversal | 0.0360 | 0.0110 | 0.0680 | 583 |
| old | actual | <0.01 | B | negligible | 0.1475 | 0.0890 | 0.2195 | 583 |
| old | actual | <0.01 | B | unresolved | 0.0412 | 0.0097 | 0.0759 | 583 |
| old | actual | 0.01-0.05 | B | dominance_positive | 0.7215 | 0.5241 | 0.9333 | 158 |
| old | actual | 0.01-0.05 | B | reversal | 0.0380 | 0.0000 | 0.1073 | 158 |
| old | actual | 0.01-0.05 | B | negligible | 0.2215 | 0.0556 | 0.3729 | 158 |
| old | actual | 0.01-0.05 | B | unresolved | 0.0190 | 0.0000 | 0.0690 | 158 |
| old | actual | >=0.05 | B | dominance_positive | 0.7281 | 0.5253 | 0.8311 | 1567 |
| old | actual | >=0.05 | B | reversal | 0.0249 | 0.0055 | 0.0771 | 1567 |
| old | actual | >=0.05 | B | negligible | 0.2380 | 0.1573 | 0.3831 | 1567 |
| old | actual | >=0.05 | B | unresolved | 0.0089 | 0.0000 | 0.0290 | 1567 |
| old | own | <0.01 | B | dominance_positive | 0.9417 | 0.8790 | 0.9933 | 583 |
| old | own | <0.01 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 583 |
| old | own | <0.01 | B | negligible | 0.0566 | 0.0063 | 0.1194 | 583 |
| old | own | <0.01 | B | unresolved | 0.0017 | 0.0000 | 0.0105 | 583 |
| old | own | 0.01-0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 158 |
| old | own | 0.01-0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 158 |
| old | own | 0.01-0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 158 |
| old | own | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 158 |
| old | own | >=0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 1567 |
| old | own | >=0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 1567 |
| old | own | >=0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 1567 |
| old | own | >=0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 1567 |
| new | actual | <0.01 | B | dominance_positive | 0.1012 | 0.0450 | 0.1890 | 583 |
| new | actual | <0.01 | B | reversal | 0.4425 | 0.2641 | 0.5798 | 583 |
| new | actual | <0.01 | B | negligible | 0.3671 | 0.2632 | 0.5184 | 583 |
| new | actual | <0.01 | B | unresolved | 0.0892 | 0.0498 | 0.1315 | 583 |
| new | actual | 0.01-0.05 | B | dominance_positive | 0.5696 | 0.3308 | 0.8000 | 158 |
| new | actual | 0.01-0.05 | B | reversal | 0.0190 | 0.0000 | 0.0800 | 158 |
| new | actual | 0.01-0.05 | B | negligible | 0.3671 | 0.0915 | 0.6183 | 158 |
| new | actual | 0.01-0.05 | B | unresolved | 0.0443 | 0.0000 | 0.1214 | 158 |
| new | actual | >=0.05 | B | dominance_positive | 0.7409 | 0.5859 | 0.8111 | 1567 |
| new | actual | >=0.05 | B | reversal | 0.0357 | 0.0097 | 0.0781 | 1567 |
| new | actual | >=0.05 | B | negligible | 0.2163 | 0.1497 | 0.3403 | 1567 |
| new | actual | >=0.05 | B | unresolved | 0.0070 | 0.0011 | 0.0140 | 1567 |
| new | own | <0.01 | B | dominance_positive | 0.1046 | 0.0478 | 0.1780 | 583 |
| new | own | <0.01 | B | reversal | 0.4597 | 0.2581 | 0.6053 | 583 |
| new | own | <0.01 | B | negligible | 0.3997 | 0.2719 | 0.5516 | 583 |
| new | own | <0.01 | B | unresolved | 0.0360 | 0.0149 | 0.0599 | 583 |
| new | own | 0.01-0.05 | B | dominance_positive | 0.8291 | 0.6812 | 0.9302 | 158 |
| new | own | 0.01-0.05 | B | reversal | 0.0127 | 0.0000 | 0.0719 | 158 |
| new | own | 0.01-0.05 | B | negligible | 0.1392 | 0.0211 | 0.3145 | 158 |
| new | own | 0.01-0.05 | B | unresolved | 0.0190 | 0.0000 | 0.0769 | 158 |
| new | own | >=0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 1567 |
| new | own | >=0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 1567 |
| new | own | >=0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 1567 |
| new | own | >=0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 1567 |

## T5_attr_ledger_features

| rule | feature | value | n | reversal_share | lo99 | hi99 |
|---|---|---|---|---|---|---|
| old | holds_conditional_other | True | 918 | 0.0708 | 0.0290 | 0.1537 |
| old | holds_conditional_other | False | 1390 | 0.0007 | 0.0000 | 0.0043 |
| old | holds_opponent_pick | True | 61 | 0.3770 | 0.1600 | 0.5952 |
| old | holds_opponent_pick | False | 2247 | 0.0191 | 0.0051 | 0.0551 |
| old | holds_pooled_pick | True | 673 | 0.0520 | 0.0069 | 0.1920 |
| old | holds_pooled_pick | False | 1635 | 0.0190 | 0.0078 | 0.0326 |
| old | self_restricted | True | 182 | 0.0549 | 0.0000 | 0.1630 |
| old | self_restricted | False | 2126 | 0.0263 | 0.0087 | 0.0625 |
| old | opp_restricted | True | 182 | 0.0330 | 0.0000 | 0.0897 |
| old | opp_restricted | False | 2126 | 0.0282 | 0.0119 | 0.0688 |
| old | holds_conditional_other_state | True | 831 | 0.0782 | 0.0306 | 0.1816 |
| old | holds_conditional_other_state | False | 1477 | 0.0007 | 0.0000 | 0.0040 |
| old | holds_opponent_pick_state | True | 53 | 0.4340 | 0.1818 | 0.6552 |
| old | holds_opponent_pick_state | False | 2255 | 0.0191 | 0.0051 | 0.0548 |
| new | holds_conditional_other | True | 918 | 0.1830 | 0.0986 | 0.2618 |
| new | holds_conditional_other | False | 1390 | 0.1072 | 0.0545 | 0.1621 |
| new | holds_opponent_pick | True | 61 | 0.4262 | 0.1860 | 0.6441 |
| new | holds_opponent_pick | False | 2247 | 0.1295 | 0.0769 | 0.1655 |
| new | holds_pooled_pick | True | 673 | 0.1664 | 0.0480 | 0.2939 |
| new | holds_pooled_pick | False | 1635 | 0.1254 | 0.0815 | 0.1975 |
| new | self_restricted | True | 182 | 0.2418 | 0.0406 | 0.4051 |
| new | self_restricted | False | 2126 | 0.1284 | 0.0656 | 0.1830 |
| new | opp_restricted | True | 182 | 0.1209 | 0.0494 | 0.2147 |
| new | opp_restricted | False | 2126 | 0.1388 | 0.0829 | 0.1773 |
| new | holds_conditional_other_state | True | 861 | 0.1754 | 0.0870 | 0.2570 |
| new | holds_conditional_other_state | False | 1447 | 0.1147 | 0.0595 | 0.1661 |
| new | holds_opponent_pick_state | True | 55 | 0.4545 | 0.1852 | 0.6667 |
| new | holds_opponent_pick_state | False | 2253 | 0.1296 | 0.0770 | 0.1657 |

## T5_6_transitions

| portfolio | old | new | count |
|---|---|---|---|
| actual | dominance_positive | dominance_positive | 1251 |
| actual | dominance_positive | negligible | 150 |
| actual | dominance_positive | reversal | 265 |
| actual | dominance_positive | unresolved | 41 |
| actual | negligible | dominance_positive | 40 |
| actual | negligible | negligible | 451 |
| actual | negligible | reversal | 1 |
| actual | negligible | unresolved | 2 |
| actual | reversal | dominance_positive | 8 |
| actual | reversal | negligible | 5 |
| actual | reversal | reversal | 47 |
| actual | reversal | unresolved | 6 |
| actual | unresolved | dominance_positive | 11 |
| actual | unresolved | negligible | 5 |
| actual | unresolved | reversal | 4 |
| actual | unresolved | unresolved | 21 |
| own | dominance_positive | dominance_positive | 1759 |
| own | dominance_positive | negligible | 221 |
| own | dominance_positive | reversal | 270 |
| own | dominance_positive | unresolved | 24 |
| own | negligible | negligible | 33 |
| own | unresolved | negligible | 1 |

## T5_headline_reversal_diff

| contrast | portfolio | verdict | share_a | share_b | diff | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| new_minus_old | actual | verdict_B | 0.1373 | 0.0286 | 0.1088 | 0.0544 | 0.1423 | 2308 |
| new_minus_old | actual | verdict_B_pm | 0.1135 | 0.0186 | 0.0949 | 0.0558 | 0.1224 | 2308 |
| new_minus_old | own | verdict_B | 0.1170 | 0.0000 | 0.1170 | 0.0679 | 0.1522 | 2308 |
| new_minus_old | own | verdict_B_pm | 0.1079 | 0.0000 | 0.1079 | 0.0639 | 0.1427 | 2308 |
| actual_minus_own | old | verdict_B | 0.0286 | 0.0000 | 0.0286 | 0.0127 | 0.0680 | 2308 |
| actual_minus_own | new | verdict_B | 0.1373 | 0.1170 | 0.0204 | 0.0027 | 0.0505 | 2308 |

## T5_4_typology

| rule | curve | type | share | lo99 | hi99 | n | tp_dominated_share |
|---|---|---|---|---|---|---|---|
| old | linear | both_lose | 0.5087 | 0.2961 | 0.6769 | 587 | 0.2181 |
| old | linear | both_win | 0.0009 | 0.0000 | 0.0070 | 1 | 0.0000 |
| old | linear | normal | 0.3847 | 0.2718 | 0.5194 | 444 | 0.7624 |
| old | linear | opposed | 0.0087 | 0.0000 | 0.0216 | 10 | 0.8000 |
| old | linear | one_sided_win | 0.0130 | 0.0017 | 0.0426 | 15 | 0.8000 |
| old | linear | no_own_stake | 0.0841 | 0.0366 | 0.1630 | 97 | 1.0000 |
| old | concave | both_lose | 0.4593 | 0.2656 | 0.6277 | 530 | 0.2585 |
| old | concave | both_win | 0.0017 | 0.0000 | 0.0087 | 2 | 0.0000 |
| old | concave | normal | 0.3977 | 0.3011 | 0.5152 | 459 | 0.7352 |
| old | concave | opposed | 0.0113 | 0.0000 | 0.0273 | 13 | 0.7692 |
| old | concave | one_sided_win | 0.0139 | 0.0000 | 0.0543 | 16 | 0.8750 |
| old | concave | no_own_stake | 0.1161 | 0.0476 | 0.2074 | 134 | 1.0000 |
| old | convex | both_lose | 0.4879 | 0.3154 | 0.5978 | 563 | 0.1616 |
| old | convex | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan |
| old | convex | normal | 0.4133 | 0.3446 | 0.5174 | 477 | 0.5882 |
| old | convex | opposed | 0.0087 | 0.0008 | 0.0208 | 10 | 0.6000 |
| old | convex | one_sided_win | 0.0095 | 0.0000 | 0.0324 | 11 | 0.6364 |
| old | convex | no_own_stake | 0.0806 | 0.0384 | 0.1570 | 93 | 1.0000 |
| old | top3_stress | both_lose | 0.1993 | 0.1323 | 0.2674 | 230 | 0.0087 |
| old | top3_stress | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan |
| old | top3_stress | normal | 0.4610 | 0.4123 | 0.5125 | 532 | 0.1094 |
| old | top3_stress | opposed | 0.0000 | 0.0000 | 0.0000 | 0 | nan |
| old | top3_stress | one_sided_win | 0.0026 | 0.0000 | 0.0096 | 3 | 0.6667 |
| old | top3_stress | no_own_stake | 0.3371 | 0.2647 | 0.4123 | 389 | 0.9875 |
| new | linear | both_lose | 0.3128 | 0.1721 | 0.4295 | 361 | 0.1773 |
| new | linear | both_win | 0.0078 | 0.0000 | 0.0203 | 9 | 0.2222 |
| new | linear | normal | 0.3995 | 0.3139 | 0.5076 | 461 | 0.5795 |
| new | linear | opposed | 0.0555 | 0.0063 | 0.1002 | 64 | 0.2857 |
| new | linear | one_sided_win | 0.0494 | 0.0105 | 0.1252 | 57 | 0.8182 |
| new | linear | no_own_stake | 0.1750 | 0.0857 | 0.3073 | 202 | 1.0000 |
| new | concave | both_lose | 0.3206 | 0.1848 | 0.4126 | 370 | 0.2514 |
| new | concave | both_win | 0.0061 | 0.0000 | 0.0163 | 7 | 0.0000 |
| new | concave | normal | 0.4255 | 0.3632 | 0.4925 | 491 | 0.6388 |
| new | concave | opposed | 0.0277 | 0.0056 | 0.0536 | 32 | 0.3438 |
| new | concave | one_sided_win | 0.0321 | 0.0058 | 0.0796 | 37 | 0.8378 |
| new | concave | no_own_stake | 0.1880 | 0.1030 | 0.3047 | 217 | 1.0000 |
| new | convex | both_lose | 0.2704 | 0.1514 | 0.3638 | 312 | 0.1667 |
| new | convex | both_win | 0.0104 | 0.0023 | 0.0209 | 12 | 0.0833 |
| new | convex | normal | 0.3925 | 0.3135 | 0.4831 | 453 | 0.4812 |
| new | convex | opposed | 0.0771 | 0.0245 | 0.1244 | 89 | 0.2584 |
| new | convex | one_sided_win | 0.0737 | 0.0288 | 0.1456 | 85 | 0.6265 |
| new | convex | no_own_stake | 0.1759 | 0.0880 | 0.2990 | 203 | 1.0000 |
| new | top3_stress | both_lose | 0.1265 | 0.0737 | 0.1774 | 146 | 0.0068 |
| new | top3_stress | both_win | 0.0121 | 0.0032 | 0.0230 | 14 | 0.0714 |
| new | top3_stress | normal | 0.3579 | 0.2679 | 0.4419 | 413 | 0.2138 |
| new | top3_stress | opposed | 0.0685 | 0.0296 | 0.1030 | 79 | 0.0253 |
| new | top3_stress | one_sided_win | 0.1179 | 0.0594 | 0.1849 | 136 | 0.2520 |
| new | top3_stress | no_own_stake | 0.3172 | 0.2458 | 0.4069 | 366 | 1.0000 |

## T5_5_stakes_distribution

| rule | curve | measure | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| old | linear | tp_share | 1143 | 0.5407 | 0.3693 | 0.5005 | 0.7419 | 0.9329 |
| old | linear | tp_share_raw | 1153 | 0.6047 | 0.4816 | 0.5545 | 0.7676 | 0.9325 |
| old | linear | hhi | 1143 | 0.3023 | 0.2114 | 0.2768 | 0.3695 | 0.4770 |
| old | linear | n_material | 1154 | 6.5295 | 4.2500 | 7.0000 | 9.0000 | 10.0000 |
| old | linear | mean_abs_third | 1154 | 0.0016 | 0.0007 | 0.0013 | 0.0021 | 0.0030 |
| old | linear | mean_abs_third_raw | 1154 | 0.0019 | 0.0012 | 0.0017 | 0.0025 | 0.0033 |
| old | concave | tp_share | 1133 | 0.5682 | 0.3944 | 0.5322 | 0.7879 | 1.0000 |
| old | concave | tp_share_raw | 1150 | 0.6296 | 0.4964 | 0.5886 | 0.8110 | 0.9513 |
| old | concave | hhi | 1133 | 0.3083 | 0.2131 | 0.2751 | 0.3744 | 0.5000 |
| old | concave | n_material | 1154 | 5.9870 | 4.0000 | 6.0000 | 8.0000 | 10.0000 |
| old | concave | mean_abs_third | 1154 | 0.0016 | 0.0007 | 0.0014 | 0.0022 | 0.0030 |
| old | concave | mean_abs_third_raw | 1154 | 0.0020 | 0.0011 | 0.0018 | 0.0026 | 0.0034 |
| old | convex | tp_share | 1141 | 0.4771 | 0.3007 | 0.4590 | 0.6581 | 0.9060 |
| old | convex | tp_share_raw | 1150 | 0.5832 | 0.4758 | 0.5259 | 0.7302 | 0.9160 |
| old | convex | hhi | 1141 | 0.3728 | 0.2487 | 0.3261 | 0.4309 | 0.5527 |
| old | convex | n_material | 1154 | 5.3761 | 3.0000 | 5.0000 | 7.0000 | 9.0000 |
| old | convex | mean_abs_third | 1154 | 0.0012 | 0.0004 | 0.0009 | 0.0016 | 0.0024 |
| old | convex | mean_abs_third_raw | 1154 | 0.0016 | 0.0008 | 0.0014 | 0.0020 | 0.0028 |
| old | top3_stress | tp_share | 843 | 0.3552 | 0.0933 | 0.3684 | 0.4703 | 0.8441 |
| old | top3_stress | tp_share_raw | 917 | 0.5258 | 0.4770 | 0.5007 | 0.5192 | 0.9028 |
| old | top3_stress | hhi | 843 | 0.5453 | 0.3577 | 0.4684 | 0.6052 | 1.0000 |
| old | top3_stress | n_material | 1154 | 2.3319 | 0.0000 | 2.0000 | 4.0000 | 5.0000 |
| old | top3_stress | mean_abs_third | 1154 | 0.0003 | 0.0000 | 0.0001 | 0.0005 | 0.0009 |
| old | top3_stress | mean_abs_third_raw | 1154 | 0.0005 | 0.0001 | 0.0004 | 0.0008 | 0.0011 |
| new | linear | tp_share | 1087 | 0.5742 | 0.4158 | 0.4970 | 0.7721 | 1.0000 |
| new | linear | tp_share_raw | 1118 | 0.6276 | 0.5001 | 0.5650 | 0.7848 | 0.9671 |
| new | linear | hhi | 1087 | 0.3193 | 0.2223 | 0.2932 | 0.3758 | 0.5001 |
| new | linear | n_material | 1154 | 5.8440 | 4.0000 | 6.0000 | 8.0000 | 10.0000 |
| new | linear | mean_abs_third | 1154 | 0.0015 | 0.0006 | 0.0012 | 0.0022 | 0.0032 |
| new | linear | mean_abs_third_raw | 1154 | 0.0018 | 0.0009 | 0.0016 | 0.0025 | 0.0034 |
| new | concave | tp_share | 1082 | 0.5929 | 0.4399 | 0.5325 | 0.7769 | 1.0000 |
| new | concave | tp_share_raw | 1118 | 0.6425 | 0.5021 | 0.5898 | 0.7920 | 0.9749 |
| new | concave | hhi | 1082 | 0.3056 | 0.2102 | 0.2762 | 0.3648 | 0.4625 |
| new | concave | n_material | 1154 | 5.8683 | 4.0000 | 6.0000 | 8.0000 | 10.0000 |
| new | concave | mean_abs_third | 1154 | 0.0015 | 0.0007 | 0.0014 | 0.0022 | 0.0031 |
| new | concave | mean_abs_third_raw | 1154 | 0.0018 | 0.0010 | 0.0017 | 0.0025 | 0.0034 |
| new | convex | tp_share | 1059 | 0.5117 | 0.3643 | 0.4725 | 0.6971 | 1.0000 |
| new | convex | tp_share_raw | 1111 | 0.6109 | 0.4986 | 0.5408 | 0.7532 | 0.9549 |
| new | convex | hhi | 1059 | 0.3937 | 0.2612 | 0.3357 | 0.4464 | 0.6002 |
| new | convex | n_material | 1154 | 4.5849 | 2.0000 | 5.0000 | 7.0000 | 8.0000 |
| new | convex | mean_abs_third | 1154 | 0.0012 | 0.0002 | 0.0009 | 0.0018 | 0.0029 |
| new | convex | mean_abs_third_raw | 1154 | 0.0015 | 0.0006 | 0.0012 | 0.0021 | 0.0032 |
| new | top3_stress | tp_share | 898 | 0.4469 | 0.2880 | 0.4316 | 0.5338 | 1.0000 |
| new | top3_stress | tp_share_raw | 983 | 0.5868 | 0.4950 | 0.5060 | 0.6357 | 0.9939 |
| new | top3_stress | hhi | 898 | 0.4912 | 0.3346 | 0.4247 | 0.5295 | 1.0000 |
| new | top3_stress | n_material | 1154 | 2.5399 | 1.0000 | 2.0000 | 4.0000 | 5.0000 |
| new | top3_stress | mean_abs_third | 1154 | 0.0004 | 0.0000 | 0.0003 | 0.0007 | 0.0012 |
| new | top3_stress | mean_abs_third_raw | 1154 | 0.0006 | 0.0002 | 0.0005 | 0.0009 | 0.0014 |
| new_minus_old | linear | tp_share | 1087 | 0.0260 | -0.0224 | 0.0099 | 0.0884 | 0.1753 |
| new_minus_old | linear | hhi | 1087 | 0.0263 | -0.0349 | 0.0013 | 0.0615 | 0.1530 |
| new_minus_old | linear | mean_abs_third | 1154 | -0.0001 | -0.0004 | 0.0000 | 0.0004 | 0.0009 |
| new_minus_old | concave | tp_share | 1077 | 0.0168 | -0.0237 | 0.0063 | 0.0728 | 0.1752 |
| new_minus_old | concave | hhi | 1077 | 0.0060 | -0.0434 | -0.0002 | 0.0419 | 0.1221 |
| new_minus_old | concave | mean_abs_third | 1154 | -0.0001 | -0.0002 | 0.0000 | 0.0004 | 0.0008 |
| new_minus_old | convex | tp_share | 1059 | 0.0290 | -0.0267 | 0.0204 | 0.1210 | 0.2308 |
| new_minus_old | convex | hhi | 1059 | 0.0292 | -0.0605 | 0.0000 | 0.0800 | 0.2052 |
| new_minus_old | convex | mean_abs_third | 1154 | 0.0000 | -0.0005 | 0.0000 | 0.0006 | 0.0012 |
| new_minus_old | top3_stress | tp_share | 731 | 0.1076 | -0.0164 | 0.0767 | 0.3073 | 0.4590 |
| new_minus_old | top3_stress | hhi | 731 | -0.1147 | -0.3215 | -0.0521 | 0.0733 | 0.2140 |
| new_minus_old | top3_stress | mean_abs_third | 1154 | 0.0001 | -0.0002 | 0.0000 | 0.0004 | 0.0009 |

## H2

| curve | sample | n_games | mean_diff_new_minus_old | lo99 | hi99 | registered | supported |
|---|---|---|---|---|---|---|---|
| linear | registered | 934 | -0.0001 | -0.0005 | 0.0002 | True | False |
| linear | state_conditional | 858 | -0.0001 | -0.0005 | 0.0002 | False | False |
| concave | registered | 934 | -0.0001 | -0.0005 | 0.0002 | False | False |
| concave | state_conditional | 858 | -0.0001 | -0.0006 | 0.0002 | False | False |
| convex | registered | 934 | 0.0001 | -0.0003 | 0.0003 | False | False |
| convex | state_conditional | 858 | 0.0001 | -0.0003 | 0.0003 | False | False |
| top3_stress | registered | 934 | 0.0002 | 0.0000 | 0.0003 | False | True |
| top3_stress | state_conditional | 858 | 0.0002 | 0.0001 | 0.0004 | False | True |

## F5_2_network_edges

10382 rows in `F5_2_network_edges.csv`.

# Registered analysis output

tag `latelink`; exclude_imprecise=False; states=81

## T5_0_diagnostics

| states | games | stopped_2000 | stopped_8000 | stopped_32000 | missed_target | n_worlds_match | max_halfwidth_linear | max_halfwidth_linear_rules_only | max_halfwidth_delta_linear | p95_halfwidth_linear | max_q_total_dev | max_per_slot_dev | per_slot_noise_scale | max_own_slot_dev | max_zero_sum_dev |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 81 | 626 | 1 | 4 | 38 | 38 | 2000 | 0.0064 | 0.0064 | 0.0061 | 0.0046 | 0.0000 | 0.0060 | 0.0112 | 0.0000 | 0.0037 |

## T5_0b_zero_sum_by_curve

| curve | rule | max_zero_sum_dev | mean_zero_sum_dev | n_games |
|---|---|---|---|---|
| linear | old | 0.0007 | 0.0001 | 626 |
| linear | new | 0.0011 | 0.0001 | 626 |
| concave | old | 0.0004 | 0.0000 | 626 |
| concave | new | 0.0007 | 0.0001 | 626 |
| convex | old | 0.0013 | 0.0001 | 626 |
| convex | new | 0.0017 | 0.0002 | 626 |
| top3_stress | old | 0.0037 | 0.0003 | 626 |
| top3_stress | new | 0.0031 | 0.0003 | 626 |

## T5_0c_verdict_by_look

| rule | portfolio | stopped_at | verdict_B | verdict_B_pm | count |
|---|---|---|---|---|---|
| delta | actual | 2000 | negligible | negligible | 1 |
| delta | actual | 2000 | reversal | reversal | 1 |
| delta | actual | 32000 | dominance_positive | dominance_positive | 36 |
| delta | actual | 32000 | dominance_positive | unresolved | 27 |
| delta | actual | 32000 | negligible | dominance_positive | 2 |
| delta | actual | 32000 | negligible | negligible | 155 |
| delta | actual | 32000 | negligible | unresolved | 15 |
| delta | actual | 32000 | reversal | reversal | 266 |
| delta | actual | 32000 | reversal | unresolved | 45 |
| delta | actual | 32000 | unresolved | unresolved | 16 |
| delta | actual | 8000 | dominance_positive | dominance_positive | 1 |
| delta | actual | 8000 | dominance_positive | unresolved | 1 |
| delta | actual | 8000 | negligible | negligible | 10 |
| delta | actual | 8000 | negligible | unresolved | 2 |
| delta | actual | 8000 | reversal | reversal | 18 |
| delta | actual | 8000 | unresolved | unresolved | 2 |
| delta | actual | missed | dominance_positive | dominance_positive | 57 |
| delta | actual | missed | dominance_positive | unresolved | 33 |
| delta | actual | missed | negligible | dominance_positive | 1 |
| delta | actual | missed | negligible | negligible | 193 |
| delta | actual | missed | negligible | unresolved | 7 |
| delta | actual | missed | reversal | reversal | 308 |
| delta | actual | missed | reversal | unresolved | 39 |
| delta | actual | missed | unresolved | unresolved | 16 |
| delta | own | 2000 | reversal | reversal | 1 |
| delta | own | 2000 | unresolved | unresolved | 1 |
| delta | own | 32000 | dominance_positive | dominance_positive | 1 |
| delta | own | 32000 | dominance_positive | unresolved | 34 |
| delta | own | 32000 | negligible | negligible | 93 |
| delta | own | 32000 | negligible | unresolved | 20 |
| delta | own | 32000 | reversal | reversal | 310 |
| delta | own | 32000 | reversal | unresolved | 70 |
| delta | own | 32000 | unresolved | unresolved | 34 |
| delta | own | 8000 | dominance_positive | unresolved | 1 |
| delta | own | 8000 | negligible | negligible | 8 |
| delta | own | 8000 | reversal | reversal | 22 |
| delta | own | 8000 | unresolved | unresolved | 3 |
| delta | own | missed | dominance_positive | dominance_positive | 5 |
| delta | own | missed | dominance_positive | unresolved | 36 |
| delta | own | missed | negligible | negligible | 132 |
| delta | own | missed | negligible | unresolved | 15 |
| delta | own | missed | reversal | reversal | 367 |
| delta | own | missed | reversal | unresolved | 64 |
| delta | own | missed | unresolved | unresolved | 35 |
| new | actual | 2000 | negligible | negligible | 1 |
| new | actual | 2000 | reversal | reversal | 1 |
| new | actual | 32000 | dominance_positive | dominance_positive | 305 |
| new | actual | 32000 | dominance_positive | unresolved | 16 |
| new | actual | 32000 | negligible | dominance_positive | 7 |
| new | actual | 32000 | negligible | negligible | 130 |
| new | actual | 32000 | negligible | unresolved | 8 |
| new | actual | 32000 | reversal | reversal | 63 |
| new | actual | 32000 | reversal | unresolved | 16 |
| new | actual | 32000 | unresolved | unresolved | 17 |
| new | actual | 8000 | dominance_positive | dominance_positive | 19 |
| new | actual | 8000 | negligible | negligible | 6 |
| new | actual | 8000 | reversal | reversal | 7 |
| new | actual | 8000 | reversal | unresolved | 1 |
| new | actual | 8000 | unresolved | unresolved | 1 |
| new | actual | missed | dominance_positive | dominance_positive | 332 |
| new | actual | missed | dominance_positive | unresolved | 16 |
| new | actual | missed | negligible | dominance_positive | 5 |
| new | actual | missed | negligible | negligible | 196 |
| new | actual | missed | negligible | unresolved | 15 |
| new | actual | missed | reversal | reversal | 63 |
| new | actual | missed | reversal | unresolved | 12 |
| new | actual | missed | unresolved | unresolved | 15 |
| new | own | 2000 | dominance_positive | dominance_positive | 1 |
| new | own | 2000 | reversal | reversal | 1 |
| new | own | 32000 | dominance_positive | dominance_positive | 420 |
| new | own | 32000 | dominance_positive | unresolved | 5 |
| new | own | 32000 | negligible | dominance_positive | 9 |
| new | own | 32000 | negligible | negligible | 51 |
| new | own | 32000 | negligible | unresolved | 2 |
| new | own | 32000 | reversal | reversal | 64 |
| new | own | 32000 | reversal | unresolved | 6 |
| new | own | 32000 | unresolved | unresolved | 5 |
| new | own | 8000 | dominance_positive | dominance_positive | 24 |
| new | own | 8000 | negligible | dominance_positive | 1 |
| new | own | 8000 | negligible | negligible | 2 |
| new | own | 8000 | reversal | reversal | 6 |
| new | own | 8000 | reversal | unresolved | 1 |
| new | own | missed | dominance_positive | dominance_positive | 473 |
| new | own | missed | dominance_positive | unresolved | 8 |
| new | own | missed | negligible | dominance_positive | 7 |
| new | own | missed | negligible | negligible | 109 |
| new | own | missed | negligible | unresolved | 3 |
| new | own | missed | reversal | reversal | 51 |
| new | own | missed | reversal | unresolved | 3 |
| old | actual | 2000 | dominance_positive | dominance_positive | 1 |
| old | actual | 2000 | negligible | negligible | 1 |
| old | actual | 32000 | dominance_positive | dominance_positive | 384 |
| old | actual | 32000 | dominance_positive | unresolved | 30 |
| old | actual | 32000 | negligible | dominance_positive | 1 |
| old | actual | 32000 | negligible | negligible | 108 |
| old | actual | 32000 | negligible | unresolved | 5 |
| old | actual | 32000 | reversal | reversal | 15 |
| old | actual | 32000 | reversal | unresolved | 4 |
| old | actual | 32000 | unresolved | unresolved | 15 |
| old | actual | 8000 | dominance_positive | dominance_positive | 25 |
| old | actual | 8000 | dominance_positive | unresolved | 2 |
| old | actual | 8000 | negligible | negligible | 5 |
| old | actual | 8000 | reversal | reversal | 1 |
| old | actual | 8000 | unresolved | unresolved | 1 |
| old | actual | missed | dominance_positive | dominance_positive | 424 |
| old | actual | missed | dominance_positive | unresolved | 34 |
| old | actual | missed | negligible | dominance_positive | 5 |
| old | actual | missed | negligible | negligible | 149 |
| old | actual | missed | negligible | unresolved | 5 |
| old | actual | missed | reversal | reversal | 18 |
| old | actual | missed | reversal | unresolved | 10 |
| old | actual | missed | unresolved | unresolved | 9 |
| old | own | 2000 | dominance_positive | dominance_positive | 2 |
| old | own | 32000 | dominance_positive | dominance_positive | 546 |
| old | own | 32000 | dominance_positive | unresolved | 4 |
| old | own | 32000 | negligible | negligible | 10 |
| old | own | 32000 | negligible | unresolved | 2 |
| old | own | 8000 | dominance_positive | dominance_positive | 34 |
| old | own | missed | dominance_positive | dominance_positive | 620 |
| old | own | missed | dominance_positive | unresolved | 9 |
| old | own | missed | negligible | negligible | 24 |
| old | own | missed | negligible | unresolved | 1 |

## T5_0d_band_width

| rule | portfolio | measure | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| old | actual | band_ratio | 1252 | 1.3769 | 0.2505 | 1.2332 | 2.4237 | 2.8427 |
| old | actual | band_ratio_pm | 1252 | 5.3541 | 1.0018 | 4.8438 | 9.5963 | 11.2329 |
| old | own | band_ratio | 1252 | 2.0000 | 1.0026 | 2.3063 | 2.7046 | 3.1298 |
| old | own | band_ratio_pm | 1252 | 7.7673 | 3.7420 | 9.1936 | 10.7462 | 12.2030 |
| new | actual | band_ratio | 1252 | 1.0596 | 0.0774 | 0.6306 | 2.1422 | 2.6761 |
| new | actual | band_ratio_pm | 1252 | 4.1210 | 0.3067 | 2.4251 | 8.4003 | 10.5505 |
| new | own | band_ratio | 1252 | 1.5980 | 0.2854 | 2.0071 | 2.5599 | 2.9048 |
| new | own | band_ratio_pm | 1252 | 6.1993 | 1.1295 | 7.9961 | 10.1552 | 11.4640 |
| delta | actual | band_ratio | 1252 | 1.0550 | 0.0462 | 0.7179 | 1.7494 | 2.6259 |
| delta | actual | band_ratio_pm | 1252 | 4.1144 | 0.1848 | 2.7588 | 6.9481 | 10.2711 |
| delta | own | band_ratio | 1252 | 1.3606 | 0.4333 | 1.1317 | 2.3093 | 2.9077 |
| delta | own | band_ratio_pm | 1252 | 5.3072 | 1.6883 | 4.3314 | 9.1373 | 11.5059 |

## T5_1_verdicts

| rule | portfolio | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|
| old | actual | B | dominance_positive | 0.7188 | 0.6240 | 0.8004 | 1252 |
| old | actual | B | reversal | 0.0383 | 0.0165 | 0.0632 | 1252 |
| old | actual | B | negligible | 0.2228 | 0.1520 | 0.3047 | 1252 |
| old | actual | B | unresolved | 0.0200 | 0.0090 | 0.0336 | 1252 |
| old | actual | C | dominance_positive | 0.7188 | 0.6240 | 0.8004 | 1252 |
| old | actual | C | reversal | 0.0383 | 0.0165 | 0.0632 | 1252 |
| old | actual | C | negligible | 0.2228 | 0.1520 | 0.3047 | 1252 |
| old | actual | C | unresolved | 0.0200 | 0.0090 | 0.0336 | 1252 |
| old | actual | B_pm | dominance_positive | 0.6709 | 0.5694 | 0.7556 | 1252 |
| old | actual | B_pm | reversal | 0.0272 | 0.0103 | 0.0498 | 1252 |
| old | actual | B_pm | negligible | 0.2101 | 0.1425 | 0.2914 | 1252 |
| old | actual | B_pm | unresolved | 0.0919 | 0.0647 | 0.1206 | 1252 |
| old | actual | C_pm | dominance_positive | 0.6717 | 0.5694 | 0.7569 | 1252 |
| old | actual | C_pm | reversal | 0.0272 | 0.0103 | 0.0498 | 1252 |
| old | actual | C_pm | negligible | 0.2101 | 0.1425 | 0.2914 | 1252 |
| old | actual | C_pm | unresolved | 0.0911 | 0.0647 | 0.1198 | 1252 |
| old | own | B | dominance_positive | 0.9704 | 0.9275 | 0.9962 | 1252 |
| old | own | B | reversal | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | B | negligible | 0.0296 | 0.0038 | 0.0725 | 1252 |
| old | own | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | C | dominance_positive | 0.9704 | 0.9275 | 0.9962 | 1252 |
| old | own | C | reversal | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | C | negligible | 0.0296 | 0.0038 | 0.0725 | 1252 |
| old | own | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | B_pm | dominance_positive | 0.9601 | 0.9102 | 0.9888 | 1252 |
| old | own | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | B_pm | negligible | 0.0272 | 0.0034 | 0.0684 | 1252 |
| old | own | B_pm | unresolved | 0.0128 | 0.0009 | 0.0280 | 1252 |
| old | own | C_pm | dominance_positive | 0.9609 | 0.9104 | 0.9889 | 1252 |
| old | own | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 1252 |
| old | own | C_pm | negligible | 0.0272 | 0.0034 | 0.0684 | 1252 |
| old | own | C_pm | unresolved | 0.0120 | 0.0009 | 0.0261 | 1252 |
| new | actual | B | dominance_positive | 0.5495 | 0.4417 | 0.6424 | 1252 |
| new | actual | B | reversal | 0.1302 | 0.0656 | 0.1729 | 1252 |
| new | actual | B | negligible | 0.2939 | 0.1998 | 0.3984 | 1252 |
| new | actual | B | unresolved | 0.0264 | 0.0100 | 0.0474 | 1252 |
| new | actual | C | dominance_positive | 0.5495 | 0.4417 | 0.6424 | 1252 |
| new | actual | C | reversal | 0.1286 | 0.0650 | 0.1714 | 1252 |
| new | actual | C | negligible | 0.2939 | 0.1998 | 0.3984 | 1252 |
| new | actual | C | unresolved | 0.0280 | 0.0114 | 0.0481 | 1252 |
| new | actual | B_pm | dominance_positive | 0.5335 | 0.4311 | 0.6244 | 1252 |
| new | actual | B_pm | reversal | 0.1070 | 0.0548 | 0.1402 | 1252 |
| new | actual | B_pm | negligible | 0.2660 | 0.1850 | 0.3632 | 1252 |
| new | actual | B_pm | unresolved | 0.0935 | 0.0516 | 0.1563 | 1252 |
| new | actual | C_pm | dominance_positive | 0.5351 | 0.4311 | 0.6274 | 1252 |
| new | actual | C_pm | reversal | 0.1070 | 0.0548 | 0.1402 | 1252 |
| new | actual | C_pm | negligible | 0.2660 | 0.1850 | 0.3632 | 1252 |
| new | actual | C_pm | unresolved | 0.0919 | 0.0503 | 0.1556 | 1252 |
| new | own | B | dominance_positive | 0.7436 | 0.6697 | 0.8186 | 1252 |
| new | own | B | reversal | 0.1054 | 0.0510 | 0.1457 | 1252 |
| new | own | B | negligible | 0.1470 | 0.0808 | 0.2198 | 1252 |
| new | own | B | unresolved | 0.0040 | 0.0000 | 0.0111 | 1252 |
| new | own | C | dominance_positive | 0.7436 | 0.6697 | 0.8186 | 1252 |
| new | own | C | reversal | 0.1054 | 0.0510 | 0.1457 | 1252 |
| new | own | C | negligible | 0.1470 | 0.0808 | 0.2198 | 1252 |
| new | own | C | unresolved | 0.0040 | 0.0000 | 0.0111 | 1252 |
| new | own | B_pm | dominance_positive | 0.7468 | 0.6717 | 0.8272 | 1252 |
| new | own | B_pm | reversal | 0.0974 | 0.0471 | 0.1356 | 1252 |
| new | own | B_pm | negligible | 0.1294 | 0.0687 | 0.2004 | 1252 |
| new | own | B_pm | unresolved | 0.0264 | 0.0103 | 0.0465 | 1252 |
| new | own | C_pm | dominance_positive | 0.7476 | 0.6720 | 0.8273 | 1252 |
| new | own | C_pm | reversal | 0.0974 | 0.0471 | 0.1356 | 1252 |
| new | own | C_pm | negligible | 0.1294 | 0.0687 | 0.2004 | 1252 |
| new | own | C_pm | unresolved | 0.0256 | 0.0102 | 0.0439 | 1252 |
| delta | actual | B | dominance_positive | 0.1238 | 0.0753 | 0.1693 | 1252 |
| delta | actual | B | reversal | 0.5407 | 0.4838 | 0.5943 | 1252 |
| delta | actual | B | negligible | 0.3083 | 0.2533 | 0.3714 | 1252 |
| delta | actual | B | unresolved | 0.0272 | 0.0145 | 0.0424 | 1252 |
| delta | actual | C | dominance_positive | 0.1238 | 0.0753 | 0.1693 | 1252 |
| delta | actual | C | reversal | 0.5407 | 0.4838 | 0.5943 | 1252 |
| delta | actual | C | negligible | 0.3083 | 0.2533 | 0.3714 | 1252 |
| delta | actual | C | unresolved | 0.0272 | 0.0145 | 0.0424 | 1252 |
| delta | actual | B_pm | dominance_positive | 0.0775 | 0.0419 | 0.1153 | 1252 |
| delta | actual | B_pm | reversal | 0.4736 | 0.4250 | 0.5176 | 1252 |
| delta | actual | B_pm | negligible | 0.2867 | 0.2347 | 0.3403 | 1252 |
| delta | actual | B_pm | unresolved | 0.1621 | 0.1222 | 0.2040 | 1252 |
| delta | actual | C_pm | dominance_positive | 0.0775 | 0.0419 | 0.1153 | 1252 |
| delta | actual | C_pm | reversal | 0.4736 | 0.4250 | 0.5176 | 1252 |
| delta | actual | C_pm | negligible | 0.2867 | 0.2347 | 0.3403 | 1252 |
| delta | actual | C_pm | unresolved | 0.1621 | 0.1222 | 0.2040 | 1252 |
| delta | own | B | dominance_positive | 0.0615 | 0.0424 | 0.0809 | 1252 |
| delta | own | B | reversal | 0.6661 | 0.6229 | 0.7213 | 1252 |
| delta | own | B | negligible | 0.2141 | 0.1646 | 0.2606 | 1252 |
| delta | own | B | unresolved | 0.0583 | 0.0385 | 0.0817 | 1252 |
| delta | own | C | dominance_positive | 0.0615 | 0.0424 | 0.0809 | 1252 |
| delta | own | C | reversal | 0.6661 | 0.6229 | 0.7213 | 1252 |
| delta | own | C | negligible | 0.2141 | 0.1646 | 0.2606 | 1252 |
| delta | own | C | unresolved | 0.0583 | 0.0385 | 0.0817 | 1252 |
| delta | own | B_pm | dominance_positive | 0.0048 | 0.0000 | 0.0155 | 1252 |
| delta | own | B_pm | reversal | 0.5591 | 0.5115 | 0.6127 | 1252 |
| delta | own | B_pm | negligible | 0.1861 | 0.1341 | 0.2350 | 1252 |
| delta | own | B_pm | unresolved | 0.2500 | 0.2043 | 0.2992 | 1252 |
| delta | own | C_pm | dominance_positive | 0.0048 | 0.0000 | 0.0155 | 1252 |
| delta | own | C_pm | reversal | 0.5591 | 0.5115 | 0.6127 | 1252 |
| delta | own | C_pm | negligible | 0.1861 | 0.1341 | 0.2350 | 1252 |
| delta | own | C_pm | unresolved | 0.2500 | 0.2043 | 0.2992 | 1252 |

## T5_2_verdicts_by_band

| rule | portfolio | band | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| old | actual | 1-3 | B | dominance_positive | 0.7734 | 0.5956 | 0.9149 | 128 |
| old | actual | 1-3 | B | reversal | 0.0391 | 0.0000 | 0.1129 | 128 |
| old | actual | 1-3 | B | negligible | 0.0703 | 0.0000 | 0.1862 | 128 |
| old | actual | 1-3 | B | unresolved | 0.1172 | 0.0160 | 0.2326 | 128 |
| old | actual | 1-3 | C | dominance_positive | 0.7734 | 0.5956 | 0.9149 | 128 |
| old | actual | 1-3 | C | reversal | 0.0391 | 0.0000 | 0.1129 | 128 |
| old | actual | 1-3 | C | negligible | 0.0703 | 0.0000 | 0.1862 | 128 |
| old | actual | 1-3 | C | unresolved | 0.1172 | 0.0160 | 0.2326 | 128 |
| old | actual | 1-3 | B_pm | dominance_positive | 0.6328 | 0.3642 | 0.8548 | 128 |
| old | actual | 1-3 | B_pm | reversal | 0.0312 | 0.0000 | 0.0887 | 128 |
| old | actual | 1-3 | B_pm | negligible | 0.0625 | 0.0000 | 0.1638 | 128 |
| old | actual | 1-3 | B_pm | unresolved | 0.2734 | 0.0753 | 0.4752 | 128 |
| old | actual | 1-3 | C_pm | dominance_positive | 0.6328 | 0.3642 | 0.8548 | 128 |
| old | actual | 1-3 | C_pm | reversal | 0.0312 | 0.0000 | 0.0887 | 128 |
| old | actual | 1-3 | C_pm | negligible | 0.0625 | 0.0000 | 0.1638 | 128 |
| old | actual | 1-3 | C_pm | unresolved | 0.2734 | 0.0753 | 0.4752 | 128 |
| old | actual | 4-10 | B | dominance_positive | 0.8441 | 0.7245 | 0.9470 | 295 |
| old | actual | 4-10 | B | reversal | 0.0508 | 0.0075 | 0.1082 | 295 |
| old | actual | 4-10 | B | negligible | 0.0915 | 0.0231 | 0.1782 | 295 |
| old | actual | 4-10 | B | unresolved | 0.0136 | 0.0000 | 0.0462 | 295 |
| old | actual | 4-10 | C | dominance_positive | 0.8441 | 0.7245 | 0.9470 | 295 |
| old | actual | 4-10 | C | reversal | 0.0508 | 0.0075 | 0.1082 | 295 |
| old | actual | 4-10 | C | negligible | 0.0915 | 0.0231 | 0.1782 | 295 |
| old | actual | 4-10 | C | unresolved | 0.0136 | 0.0000 | 0.0462 | 295 |
| old | actual | 4-10 | B_pm | dominance_positive | 0.7763 | 0.6397 | 0.9043 | 295 |
| old | actual | 4-10 | B_pm | reversal | 0.0339 | 0.0065 | 0.0691 | 295 |
| old | actual | 4-10 | B_pm | negligible | 0.0915 | 0.0231 | 0.1782 | 295 |
| old | actual | 4-10 | B_pm | unresolved | 0.0983 | 0.0269 | 0.1736 | 295 |
| old | actual | 4-10 | C_pm | dominance_positive | 0.7763 | 0.6397 | 0.9043 | 295 |
| old | actual | 4-10 | C_pm | reversal | 0.0339 | 0.0065 | 0.0691 | 295 |
| old | actual | 4-10 | C_pm | negligible | 0.0915 | 0.0231 | 0.1782 | 295 |
| old | actual | 4-10 | C_pm | unresolved | 0.0983 | 0.0269 | 0.1736 | 295 |
| old | actual | 11-16 | B | dominance_positive | 0.7984 | 0.6429 | 0.9028 | 243 |
| old | actual | 11-16 | B | reversal | 0.0206 | 0.0000 | 0.0588 | 243 |
| old | actual | 11-16 | B | negligible | 0.1728 | 0.0822 | 0.3067 | 243 |
| old | actual | 11-16 | B | unresolved | 0.0082 | 0.0000 | 0.0319 | 243 |
| old | actual | 11-16 | C | dominance_positive | 0.7984 | 0.6429 | 0.9028 | 243 |
| old | actual | 11-16 | C | reversal | 0.0206 | 0.0000 | 0.0588 | 243 |
| old | actual | 11-16 | C | negligible | 0.1728 | 0.0822 | 0.3067 | 243 |
| old | actual | 11-16 | C | unresolved | 0.0082 | 0.0000 | 0.0319 | 243 |
| old | actual | 11-16 | B_pm | dominance_positive | 0.7654 | 0.6184 | 0.8847 | 243 |
| old | actual | 11-16 | B_pm | reversal | 0.0165 | 0.0000 | 0.0518 | 243 |
| old | actual | 11-16 | B_pm | negligible | 0.1605 | 0.0775 | 0.2811 | 243 |
| old | actual | 11-16 | B_pm | unresolved | 0.0576 | 0.0066 | 0.1409 | 243 |
| old | actual | 11-16 | C_pm | dominance_positive | 0.7654 | 0.6184 | 0.8847 | 243 |
| old | actual | 11-16 | C_pm | reversal | 0.0165 | 0.0000 | 0.0518 | 243 |
| old | actual | 11-16 | C_pm | negligible | 0.1605 | 0.0775 | 0.2811 | 243 |
| old | actual | 11-16 | C_pm | unresolved | 0.0576 | 0.0066 | 0.1409 | 243 |
| old | actual | 17-30 | B | dominance_positive | 0.6109 | 0.4092 | 0.7743 | 586 |
| old | actual | 17-30 | B | reversal | 0.0392 | 0.0036 | 0.0926 | 586 |
| old | actual | 17-30 | B | negligible | 0.3430 | 0.2106 | 0.5107 | 586 |
| old | actual | 17-30 | B | unresolved | 0.0068 | 0.0000 | 0.0201 | 586 |
| old | actual | 17-30 | C | dominance_positive | 0.6109 | 0.4092 | 0.7743 | 586 |
| old | actual | 17-30 | C | reversal | 0.0392 | 0.0036 | 0.0926 | 586 |
| old | actual | 17-30 | C | negligible | 0.3430 | 0.2106 | 0.5107 | 586 |
| old | actual | 17-30 | C | unresolved | 0.0068 | 0.0000 | 0.0201 | 586 |
| old | actual | 17-30 | B_pm | dominance_positive | 0.5870 | 0.3656 | 0.7696 | 586 |
| old | actual | 17-30 | B_pm | reversal | 0.0273 | 0.0000 | 0.0737 | 586 |
| old | actual | 17-30 | B_pm | negligible | 0.3225 | 0.1892 | 0.4886 | 586 |
| old | actual | 17-30 | B_pm | unresolved | 0.0631 | 0.0166 | 0.1146 | 586 |
| old | actual | 17-30 | C_pm | dominance_positive | 0.5887 | 0.3656 | 0.7746 | 586 |
| old | actual | 17-30 | C_pm | reversal | 0.0273 | 0.0000 | 0.0737 | 586 |
| old | actual | 17-30 | C_pm | negligible | 0.3225 | 0.1892 | 0.4886 | 586 |
| old | actual | 17-30 | C_pm | unresolved | 0.0614 | 0.0150 | 0.1138 | 586 |
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
| old | own | 4-10 | B_pm | dominance_positive | 0.9492 | 0.8711 | 0.9961 | 295 |
| old | own | 4-10 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 295 |
| old | own | 4-10 | B_pm | negligible | 0.0407 | 0.0000 | 0.1229 | 295 |
| old | own | 4-10 | B_pm | unresolved | 0.0102 | 0.0000 | 0.0461 | 295 |
| old | own | 4-10 | C_pm | dominance_positive | 0.9492 | 0.8711 | 0.9961 | 295 |
| old | own | 4-10 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 295 |
| old | own | 4-10 | C_pm | negligible | 0.0407 | 0.0000 | 0.1229 | 295 |
| old | own | 4-10 | C_pm | unresolved | 0.0102 | 0.0000 | 0.0461 | 295 |
| old | own | 11-16 | B | dominance_positive | 0.9918 | 0.9706 | 1.0000 | 243 |
| old | own | 11-16 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| old | own | 11-16 | B | negligible | 0.0082 | 0.0000 | 0.0294 | 243 |
| old | own | 11-16 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 243 |
| old | own | 11-16 | C | dominance_positive | 0.9918 | 0.9706 | 1.0000 | 243 |
| old | own | 11-16 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| old | own | 11-16 | C | negligible | 0.0082 | 0.0000 | 0.0294 | 243 |
| old | own | 11-16 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 243 |
| old | own | 11-16 | B_pm | dominance_positive | 0.9712 | 0.9087 | 1.0000 | 243 |
| old | own | 11-16 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| old | own | 11-16 | B_pm | negligible | 0.0082 | 0.0000 | 0.0294 | 243 |
| old | own | 11-16 | B_pm | unresolved | 0.0206 | 0.0000 | 0.0669 | 243 |
| old | own | 11-16 | C_pm | dominance_positive | 0.9712 | 0.9087 | 1.0000 | 243 |
| old | own | 11-16 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| old | own | 11-16 | C_pm | negligible | 0.0082 | 0.0000 | 0.0294 | 243 |
| old | own | 11-16 | C_pm | unresolved | 0.0206 | 0.0000 | 0.0669 | 243 |
| old | own | 17-30 | B | dominance_positive | 0.9676 | 0.9147 | 1.0000 | 586 |
| old | own | 17-30 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | B | negligible | 0.0324 | 0.0000 | 0.0853 | 586 |
| old | own | 17-30 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | C | dominance_positive | 0.9676 | 0.9147 | 1.0000 | 586 |
| old | own | 17-30 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | C | negligible | 0.0324 | 0.0000 | 0.0853 | 586 |
| old | own | 17-30 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | B_pm | dominance_positive | 0.9590 | 0.9049 | 0.9981 | 586 |
| old | own | 17-30 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | B_pm | negligible | 0.0273 | 0.0000 | 0.0725 | 586 |
| old | own | 17-30 | B_pm | unresolved | 0.0137 | 0.0015 | 0.0301 | 586 |
| old | own | 17-30 | C_pm | dominance_positive | 0.9608 | 0.9061 | 0.9982 | 586 |
| old | own | 17-30 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| old | own | 17-30 | C_pm | negligible | 0.0273 | 0.0000 | 0.0725 | 586 |
| old | own | 17-30 | C_pm | unresolved | 0.0119 | 0.0000 | 0.0280 | 586 |
| new | actual | 1-3 | B | dominance_positive | 0.1094 | 0.0292 | 0.2239 | 128 |
| new | actual | 1-3 | B | reversal | 0.5391 | 0.2500 | 0.7851 | 128 |
| new | actual | 1-3 | B | negligible | 0.2266 | 0.0561 | 0.4474 | 128 |
| new | actual | 1-3 | B | unresolved | 0.1250 | 0.0227 | 0.2500 | 128 |
| new | actual | 1-3 | C | dominance_positive | 0.1094 | 0.0292 | 0.2239 | 128 |
| new | actual | 1-3 | C | reversal | 0.5391 | 0.2500 | 0.7851 | 128 |
| new | actual | 1-3 | C | negligible | 0.2266 | 0.0561 | 0.4474 | 128 |
| new | actual | 1-3 | C | unresolved | 0.1250 | 0.0227 | 0.2500 | 128 |
| new | actual | 1-3 | B_pm | dominance_positive | 0.0781 | 0.0084 | 0.1709 | 128 |
| new | actual | 1-3 | B_pm | reversal | 0.4453 | 0.2079 | 0.6400 | 128 |
| new | actual | 1-3 | B_pm | negligible | 0.1797 | 0.0403 | 0.3738 | 128 |
| new | actual | 1-3 | B_pm | unresolved | 0.2969 | 0.1597 | 0.4397 | 128 |
| new | actual | 1-3 | C_pm | dominance_positive | 0.0781 | 0.0084 | 0.1709 | 128 |
| new | actual | 1-3 | C_pm | reversal | 0.4453 | 0.2079 | 0.6400 | 128 |
| new | actual | 1-3 | C_pm | negligible | 0.1797 | 0.0403 | 0.3738 | 128 |
| new | actual | 1-3 | C_pm | unresolved | 0.2969 | 0.1597 | 0.4397 | 128 |
| new | actual | 4-10 | B | dominance_positive | 0.4305 | 0.2120 | 0.6717 | 295 |
| new | actual | 4-10 | B | reversal | 0.2136 | 0.1170 | 0.2847 | 295 |
| new | actual | 4-10 | B | negligible | 0.3153 | 0.1511 | 0.4760 | 295 |
| new | actual | 4-10 | B | unresolved | 0.0407 | 0.0000 | 0.1174 | 295 |
| new | actual | 4-10 | C | dominance_positive | 0.4305 | 0.2120 | 0.6717 | 295 |
| new | actual | 4-10 | C | reversal | 0.2136 | 0.1170 | 0.2847 | 295 |
| new | actual | 4-10 | C | negligible | 0.3153 | 0.1511 | 0.4760 | 295 |
| new | actual | 4-10 | C | unresolved | 0.0407 | 0.0000 | 0.1174 | 295 |
| new | actual | 4-10 | B_pm | dominance_positive | 0.4102 | 0.1597 | 0.6571 | 295 |
| new | actual | 4-10 | B_pm | reversal | 0.1864 | 0.0912 | 0.2613 | 295 |
| new | actual | 4-10 | B_pm | negligible | 0.2678 | 0.1351 | 0.3942 | 295 |
| new | actual | 4-10 | B_pm | unresolved | 0.1356 | 0.0149 | 0.3310 | 295 |
| new | actual | 4-10 | C_pm | dominance_positive | 0.4102 | 0.1597 | 0.6571 | 295 |
| new | actual | 4-10 | C_pm | reversal | 0.1864 | 0.0912 | 0.2613 | 295 |
| new | actual | 4-10 | C_pm | negligible | 0.2678 | 0.1351 | 0.3942 | 295 |
| new | actual | 4-10 | C_pm | unresolved | 0.1356 | 0.0149 | 0.3310 | 295 |
| new | actual | 11-16 | B | dominance_positive | 0.7284 | 0.5556 | 0.8734 | 243 |
| new | actual | 11-16 | B | reversal | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | actual | 11-16 | B | negligible | 0.2593 | 0.1213 | 0.4304 | 243 |
| new | actual | 11-16 | B | unresolved | 0.0082 | 0.0000 | 0.0357 | 243 |
| new | actual | 11-16 | C | dominance_positive | 0.7284 | 0.5556 | 0.8734 | 243 |
| new | actual | 11-16 | C | reversal | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | actual | 11-16 | C | negligible | 0.2593 | 0.1213 | 0.4304 | 243 |
| new | actual | 11-16 | C | unresolved | 0.0082 | 0.0000 | 0.0357 | 243 |
| new | actual | 11-16 | B_pm | dominance_positive | 0.7202 | 0.5556 | 0.8646 | 243 |
| new | actual | 11-16 | B_pm | reversal | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | actual | 11-16 | B_pm | negligible | 0.2387 | 0.1163 | 0.3861 | 243 |
| new | actual | 11-16 | B_pm | unresolved | 0.0370 | 0.0039 | 0.0860 | 243 |
| new | actual | 11-16 | C_pm | dominance_positive | 0.7202 | 0.5556 | 0.8646 | 243 |
| new | actual | 11-16 | C_pm | reversal | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | actual | 11-16 | C_pm | negligible | 0.2387 | 0.1163 | 0.3861 | 243 |
| new | actual | 11-16 | C_pm | unresolved | 0.0370 | 0.0039 | 0.0860 | 243 |
| new | actual | 17-30 | B | dominance_positive | 0.6314 | 0.4622 | 0.7909 | 586 |
| new | actual | 17-30 | B | reversal | 0.0512 | 0.0073 | 0.0959 | 586 |
| new | actual | 17-30 | B | negligible | 0.3123 | 0.1794 | 0.4679 | 586 |
| new | actual | 17-30 | B | unresolved | 0.0051 | 0.0000 | 0.0186 | 586 |
| new | actual | 17-30 | C | dominance_positive | 0.6314 | 0.4622 | 0.7909 | 586 |
| new | actual | 17-30 | C | reversal | 0.0478 | 0.0056 | 0.0925 | 586 |
| new | actual | 17-30 | C | negligible | 0.3123 | 0.1794 | 0.4679 | 586 |
| new | actual | 17-30 | C | unresolved | 0.0085 | 0.0000 | 0.0217 | 586 |
| new | actual | 17-30 | B_pm | dominance_positive | 0.6177 | 0.4559 | 0.7662 | 586 |
| new | actual | 17-30 | B_pm | reversal | 0.0358 | 0.0000 | 0.0783 | 586 |
| new | actual | 17-30 | B_pm | negligible | 0.2952 | 0.1748 | 0.4435 | 586 |
| new | actual | 17-30 | B_pm | unresolved | 0.0512 | 0.0144 | 0.0943 | 586 |
| new | actual | 17-30 | C_pm | dominance_positive | 0.6212 | 0.4568 | 0.7730 | 586 |
| new | actual | 17-30 | C_pm | reversal | 0.0358 | 0.0000 | 0.0783 | 586 |
| new | actual | 17-30 | C_pm | negligible | 0.2952 | 0.1748 | 0.4435 | 586 |
| new | actual | 17-30 | C_pm | unresolved | 0.0478 | 0.0098 | 0.0929 | 586 |
| new | own | 1-3 | B | dominance_positive | 0.0703 | 0.0000 | 0.2137 | 128 |
| new | own | 1-3 | B | reversal | 0.5859 | 0.2661 | 0.8595 | 128 |
| new | own | 1-3 | B | negligible | 0.3125 | 0.0800 | 0.6250 | 128 |
| new | own | 1-3 | B | unresolved | 0.0312 | 0.0000 | 0.0909 | 128 |
| new | own | 1-3 | C | dominance_positive | 0.0703 | 0.0000 | 0.2137 | 128 |
| new | own | 1-3 | C | reversal | 0.5859 | 0.2661 | 0.8595 | 128 |
| new | own | 1-3 | C | negligible | 0.3125 | 0.0800 | 0.6250 | 128 |
| new | own | 1-3 | C | unresolved | 0.0312 | 0.0000 | 0.0909 | 128 |
| new | own | 1-3 | B_pm | dominance_positive | 0.0938 | 0.0143 | 0.2056 | 128 |
| new | own | 1-3 | B_pm | reversal | 0.5312 | 0.2475 | 0.7956 | 128 |
| new | own | 1-3 | B_pm | negligible | 0.2422 | 0.0526 | 0.5096 | 128 |
| new | own | 1-3 | B_pm | unresolved | 0.1328 | 0.0438 | 0.2290 | 128 |
| new | own | 1-3 | C_pm | dominance_positive | 0.0938 | 0.0143 | 0.2056 | 128 |
| new | own | 1-3 | C_pm | reversal | 0.5312 | 0.2475 | 0.7956 | 128 |
| new | own | 1-3 | C_pm | negligible | 0.2422 | 0.0526 | 0.5096 | 128 |
| new | own | 1-3 | C_pm | unresolved | 0.1328 | 0.0438 | 0.2290 | 128 |
| new | own | 4-10 | B | dominance_positive | 0.4407 | 0.2092 | 0.6569 | 295 |
| new | own | 4-10 | B | reversal | 0.1932 | 0.0976 | 0.2734 | 295 |
| new | own | 4-10 | B | negligible | 0.3627 | 0.1818 | 0.5515 | 295 |
| new | own | 4-10 | B | unresolved | 0.0034 | 0.0000 | 0.0196 | 295 |
| new | own | 4-10 | C | dominance_positive | 0.4407 | 0.2092 | 0.6569 | 295 |
| new | own | 4-10 | C | reversal | 0.1932 | 0.0976 | 0.2734 | 295 |
| new | own | 4-10 | C | negligible | 0.3627 | 0.1818 | 0.5515 | 295 |
| new | own | 4-10 | C | unresolved | 0.0034 | 0.0000 | 0.0196 | 295 |
| new | own | 4-10 | B_pm | dominance_positive | 0.4542 | 0.2218 | 0.6654 | 295 |
| new | own | 4-10 | B_pm | reversal | 0.1831 | 0.0916 | 0.2525 | 295 |
| new | own | 4-10 | B_pm | negligible | 0.3356 | 0.1648 | 0.5294 | 295 |
| new | own | 4-10 | B_pm | unresolved | 0.0271 | 0.0000 | 0.0608 | 295 |
| new | own | 4-10 | C_pm | dominance_positive | 0.4542 | 0.2218 | 0.6654 | 295 |
| new | own | 4-10 | C_pm | reversal | 0.1831 | 0.0916 | 0.2525 | 295 |
| new | own | 4-10 | C_pm | negligible | 0.3356 | 0.1648 | 0.5294 | 295 |
| new | own | 4-10 | C_pm | unresolved | 0.0271 | 0.0000 | 0.0608 | 295 |
| new | own | 11-16 | B | dominance_positive | 0.9259 | 0.8042 | 1.0000 | 243 |
| new | own | 11-16 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | B | negligible | 0.0741 | 0.0000 | 0.1958 | 243 |
| new | own | 11-16 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | C | dominance_positive | 0.9259 | 0.8042 | 1.0000 | 243 |
| new | own | 11-16 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | C | negligible | 0.0741 | 0.0000 | 0.1958 | 243 |
| new | own | 11-16 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | B_pm | dominance_positive | 0.9300 | 0.8140 | 1.0000 | 243 |
| new | own | 11-16 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | B_pm | negligible | 0.0658 | 0.0000 | 0.1786 | 243 |
| new | own | 11-16 | B_pm | unresolved | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | own | 11-16 | C_pm | dominance_positive | 0.9300 | 0.8140 | 1.0000 | 243 |
| new | own | 11-16 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 243 |
| new | own | 11-16 | C_pm | negligible | 0.0658 | 0.0000 | 0.1786 | 243 |
| new | own | 11-16 | C_pm | unresolved | 0.0041 | 0.0000 | 0.0260 | 243 |
| new | own | 17-30 | B | dominance_positive | 0.9676 | 0.9147 | 1.0000 | 586 |
| new | own | 17-30 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | B | negligible | 0.0324 | 0.0000 | 0.0853 | 586 |
| new | own | 17-30 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | C | dominance_positive | 0.9676 | 0.9147 | 1.0000 | 586 |
| new | own | 17-30 | C | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | C | negligible | 0.0324 | 0.0000 | 0.0853 | 586 |
| new | own | 17-30 | C | unresolved | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | B_pm | dominance_positive | 0.9608 | 0.9061 | 1.0000 | 586 |
| new | own | 17-30 | B_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | B_pm | negligible | 0.0273 | 0.0000 | 0.0725 | 586 |
| new | own | 17-30 | B_pm | unresolved | 0.0119 | 0.0000 | 0.0277 | 586 |
| new | own | 17-30 | C_pm | dominance_positive | 0.9625 | 0.9074 | 1.0000 | 586 |
| new | own | 17-30 | C_pm | reversal | 0.0000 | 0.0000 | 0.0000 | 586 |
| new | own | 17-30 | C_pm | negligible | 0.0273 | 0.0000 | 0.0725 | 586 |
| new | own | 17-30 | C_pm | unresolved | 0.0102 | 0.0000 | 0.0248 | 586 |

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
| old | actual | 13 | 1 | 1 | 1 | 48 | 34 |
| old | actual | 14 | 2 | 3 | 1 | 48 | 34 |
| old | actual | 15 | 3 | 3 | 2 | 48 | 34 |
| old | actual | 16 | 3 | 3 | 2 | 48 | 34 |
| old | actual | 17 | 3 | 5 | 2 | 48 | 34 |
| old | actual | 18 | 5 | 4 | 2 | 48 | 34 |
| old | actual | 19 | 5 | 4 | 6 | 48 | 34 |
| old | actual | 20 | 5 | 5 | 2 | 48 | 34 |
| old | actual | 21 | 2 | 2 | 1 | 48 | 34 |
| old | actual | 22 | 1 | 1 | 1 | 48 | 34 |
| old | actual | 23 | 2 | 2 | 2 | 48 | 34 |
| old | actual | 24 | 1 | 1 | 1 | 48 | 34 |
| old | actual | 25 | 2 | 2 | 1 | 48 | 34 |
| old | actual | 26 | 3 | 3 | 2 | 48 | 34 |
| old | actual | 27 | 1 | 1 | 1 | 48 | 34 |
| old | actual | 28 | 0 | 0 | 0 | 48 | 34 |
| old | actual | 29 | 2 | 2 | 1 | 48 | 34 |
| old | actual | 30 | 1 | 0 | 1 | 48 | 34 |
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
| new | actual | 3 | 1 | 1 | 1 | 163 | 134 |
| new | actual | 4 | 3 | 3 | 1 | 163 | 134 |
| new | actual | 5 | 1 | 0 | 0 | 163 | 134 |
| new | actual | 6 | 0 | 0 | 0 | 163 | 134 |
| new | actual | 7 | 6 | 4 | 4 | 163 | 134 |
| new | actual | 8 | 8 | 12 | 6 | 163 | 134 |
| new | actual | 9 | 100 | 99 | 88 | 163 | 134 |
| new | actual | 10 | 0 | 0 | 0 | 163 | 134 |
| new | actual | 11 | 0 | 0 | 0 | 163 | 134 |
| new | actual | 12 | 0 | 0 | 0 | 163 | 134 |
| new | actual | 13 | 0 | 0 | 0 | 163 | 134 |
| new | actual | 14 | 0 | 0 | 0 | 163 | 134 |
| new | actual | 15 | 2 | 2 | 2 | 163 | 134 |
| new | actual | 16 | 1 | 1 | 2 | 163 | 134 |
| new | actual | 17 | 4 | 4 | 3 | 163 | 134 |
| new | actual | 18 | 1 | 1 | 1 | 163 | 134 |
| new | actual | 19 | 6 | 6 | 6 | 163 | 134 |
| new | actual | 20 | 4 | 4 | 2 | 163 | 134 |
| new | actual | 21 | 2 | 2 | 1 | 163 | 134 |
| new | actual | 22 | 1 | 1 | 1 | 163 | 134 |
| new | actual | 23 | 4 | 4 | 4 | 163 | 134 |
| new | actual | 24 | 1 | 1 | 2 | 163 | 134 |
| new | actual | 25 | 2 | 2 | 1 | 163 | 134 |
| new | actual | 26 | 3 | 3 | 4 | 163 | 134 |
| new | actual | 27 | 4 | 4 | 1 | 163 | 134 |
| new | actual | 28 | 0 | 0 | 0 | 163 | 134 |
| new | actual | 29 | 3 | 3 | 2 | 163 | 134 |
| new | actual | 30 | 6 | 6 | 2 | 163 | 134 |
| new | own | 1 | 0 | 0 | 0 | 132 | 122 |
| new | own | 2 | 0 | 0 | 0 | 132 | 122 |
| new | own | 3 | 0 | 0 | 0 | 132 | 122 |
| new | own | 4 | 0 | 0 | 0 | 132 | 122 |
| new | own | 5 | 0 | 0 | 0 | 132 | 122 |
| new | own | 6 | 0 | 0 | 0 | 132 | 122 |
| new | own | 7 | 0 | 0 | 0 | 132 | 122 |
| new | own | 8 | 0 | 0 | 0 | 132 | 122 |
| new | own | 9 | 132 | 132 | 122 | 132 | 122 |
| new | own | 10 | 0 | 0 | 0 | 132 | 122 |
| new | own | 11 | 0 | 0 | 0 | 132 | 122 |
| new | own | 12 | 0 | 0 | 0 | 132 | 122 |
| new | own | 13 | 0 | 0 | 0 | 132 | 122 |
| new | own | 14 | 0 | 0 | 0 | 132 | 122 |
| new | own | 15 | 0 | 0 | 0 | 132 | 122 |
| new | own | 16 | 0 | 0 | 0 | 132 | 122 |
| new | own | 17 | 0 | 0 | 0 | 132 | 122 |
| new | own | 18 | 0 | 0 | 0 | 132 | 122 |
| new | own | 19 | 0 | 0 | 0 | 132 | 122 |
| new | own | 20 | 0 | 0 | 0 | 132 | 122 |
| new | own | 21 | 0 | 0 | 0 | 132 | 122 |
| new | own | 22 | 0 | 0 | 0 | 132 | 122 |
| new | own | 23 | 0 | 0 | 0 | 132 | 122 |
| new | own | 24 | 0 | 0 | 0 | 132 | 122 |
| new | own | 25 | 0 | 0 | 0 | 132 | 122 |
| new | own | 26 | 0 | 0 | 0 | 132 | 122 |
| new | own | 27 | 0 | 0 | 0 | 132 | 122 |
| new | own | 28 | 0 | 0 | 0 | 132 | 122 |
| new | own | 29 | 0 | 0 | 0 | 132 | 122 |
| new | own | 30 | 0 | 0 | 0 | 132 | 122 |

## F5_1_profiles

720 rows in `F5_1_profiles.csv`.

## T5_curves_and_T5_6_delta

| rule | portfolio | band | curve | n | mean | q25 | median | q75 | q90 | share_sig_pos | pos_lo99 | pos_hi99 | share_sig_neg | neg_lo99 | neg_hi99 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| old | actual | all | linear | 1252 | 0.0177 | 0.0008 | 0.0102 | 0.0301 | 0.0431 | 0.6701 | 0.5355 | 0.8003 | 0.0168 | 0.0026 | 0.0359 |
| old | actual | all | concave | 1252 | 0.0165 | 0.0007 | 0.0088 | 0.0284 | 0.0394 | 0.6350 | 0.4940 | 0.7708 | 0.0184 | 0.0042 | 0.0368 |
| old | actual | all | convex | 1252 | 0.0162 | 0.0005 | 0.0092 | 0.0279 | 0.0421 | 0.6765 | 0.5666 | 0.7736 | 0.0112 | 0.0009 | 0.0244 |
| old | actual | all | top3_stress | 1252 | 0.0069 | 0.0000 | 0.0009 | 0.0109 | 0.0234 | 0.4177 | 0.3610 | 0.4911 | 0.0016 | 0.0000 | 0.0066 |
| old | actual | 1-3 | linear | 128 | 0.0029 | 0.0018 | 0.0026 | 0.0053 | 0.0075 | 0.4531 | 0.1964 | 0.6970 | 0.0156 | 0.0000 | 0.0580 |
| old | actual | 1-3 | concave | 128 | 0.0015 | 0.0010 | 0.0015 | 0.0029 | 0.0044 | 0.2891 | 0.0935 | 0.5328 | 0.0234 | 0.0000 | 0.0682 |
| old | actual | 1-3 | convex | 128 | 0.0051 | 0.0029 | 0.0043 | 0.0075 | 0.0106 | 0.7656 | 0.6418 | 0.8800 | 0.0156 | 0.0000 | 0.0580 |
| old | actual | 1-3 | top3_stress | 128 | 0.0043 | 0.0003 | 0.0014 | 0.0056 | 0.0128 | 0.3750 | 0.1587 | 0.6271 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 4-10 | linear | 295 | 0.0181 | 0.0056 | 0.0143 | 0.0273 | 0.0395 | 0.8475 | 0.7209 | 0.9561 | 0.0271 | 0.0000 | 0.0736 |
| old | actual | 4-10 | concave | 295 | 0.0138 | 0.0032 | 0.0093 | 0.0179 | 0.0346 | 0.7627 | 0.5793 | 0.9371 | 0.0305 | 0.0000 | 0.0836 |
| old | actual | 4-10 | convex | 295 | 0.0231 | 0.0091 | 0.0197 | 0.0364 | 0.0465 | 0.8780 | 0.7657 | 0.9671 | 0.0102 | 0.0000 | 0.0308 |
| old | actual | 4-10 | top3_stress | 295 | 0.0184 | 0.0097 | 0.0169 | 0.0281 | 0.0343 | 0.8712 | 0.7689 | 0.9599 | 0.0034 | 0.0000 | 0.0193 |
| old | actual | 11-16 | linear | 243 | 0.0284 | 0.0080 | 0.0277 | 0.0389 | 0.0526 | 0.8107 | 0.6548 | 0.9153 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 11-16 | concave | 243 | 0.0229 | 0.0065 | 0.0193 | 0.0285 | 0.0398 | 0.8066 | 0.6535 | 0.9109 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 11-16 | convex | 243 | 0.0298 | 0.0079 | 0.0298 | 0.0421 | 0.0599 | 0.7984 | 0.6429 | 0.9098 | 0.0041 | 0.0000 | 0.0262 |
| old | actual | 11-16 | top3_stress | 243 | 0.0093 | 0.0020 | 0.0067 | 0.0150 | 0.0214 | 0.7160 | 0.5826 | 0.8523 | 0.0000 | 0.0000 | 0.0000 |
| old | actual | 17-30 | linear | 586 | 0.0163 | 0.0000 | 0.0075 | 0.0301 | 0.0422 | 0.5700 | 0.3422 | 0.7542 | 0.0188 | 0.0000 | 0.0564 |
| old | actual | 17-30 | concave | 586 | 0.0186 | 0.0000 | 0.0116 | 0.0329 | 0.0423 | 0.5751 | 0.3451 | 0.7580 | 0.0188 | 0.0000 | 0.0564 |
| old | actual | 17-30 | convex | 586 | 0.0095 | 0.0000 | 0.0028 | 0.0158 | 0.0292 | 0.5051 | 0.3153 | 0.6568 | 0.0137 | 0.0000 | 0.0358 |
| old | actual | 17-30 | top3_stress | 586 | 0.0006 | 0.0000 | 0.0000 | 0.0003 | 0.0019 | 0.0751 | 0.0328 | 0.1232 | 0.0017 | 0.0000 | 0.0105 |
| old | own | all | linear | 1252 | 0.0243 | 0.0082 | 0.0241 | 0.0359 | 0.0458 | 0.8818 | 0.8110 | 0.9435 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | concave | 1252 | 0.0213 | 0.0062 | 0.0212 | 0.0322 | 0.0397 | 0.8482 | 0.7700 | 0.9256 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | convex | 1252 | 0.0220 | 0.0062 | 0.0189 | 0.0333 | 0.0452 | 0.8658 | 0.8097 | 0.9144 | 0.0000 | 0.0000 | 0.0000 |
| old | own | all | top3_stress | 1252 | 0.0078 | 0.0000 | 0.0026 | 0.0131 | 0.0249 | 0.4904 | 0.4275 | 0.5534 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | linear | 128 | 0.0033 | 0.0019 | 0.0025 | 0.0040 | 0.0062 | 0.3516 | 0.0984 | 0.6452 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | concave | 128 | 0.0018 | 0.0010 | 0.0014 | 0.0022 | 0.0034 | 0.1953 | 0.0164 | 0.4407 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | convex | 128 | 0.0055 | 0.0032 | 0.0042 | 0.0068 | 0.0104 | 0.7891 | 0.6018 | 0.9381 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 1-3 | top3_stress | 128 | 0.0044 | 0.0003 | 0.0014 | 0.0057 | 0.0134 | 0.3750 | 0.1587 | 0.6271 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | linear | 295 | 0.0164 | 0.0071 | 0.0125 | 0.0247 | 0.0331 | 0.9220 | 0.8201 | 0.9898 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | concave | 295 | 0.0097 | 0.0039 | 0.0070 | 0.0147 | 0.0200 | 0.8339 | 0.6794 | 0.9732 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | convex | 295 | 0.0242 | 0.0115 | 0.0192 | 0.0364 | 0.0466 | 0.9492 | 0.8557 | 0.9965 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 4-10 | top3_stress | 295 | 0.0198 | 0.0112 | 0.0181 | 0.0282 | 0.0340 | 0.9525 | 0.8669 | 0.9966 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | linear | 243 | 0.0334 | 0.0225 | 0.0314 | 0.0406 | 0.0551 | 0.9918 | 0.9706 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | concave | 243 | 0.0225 | 0.0146 | 0.0210 | 0.0288 | 0.0370 | 0.9794 | 0.9388 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | convex | 243 | 0.0382 | 0.0273 | 0.0354 | 0.0455 | 0.0661 | 0.9918 | 0.9706 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 11-16 | top3_stress | 243 | 0.0115 | 0.0054 | 0.0088 | 0.0165 | 0.0231 | 0.9095 | 0.7653 | 0.9920 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | linear | 586 | 0.0290 | 0.0173 | 0.0293 | 0.0393 | 0.0479 | 0.9317 | 0.8661 | 0.9916 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | concave | 586 | 0.0310 | 0.0243 | 0.0313 | 0.0374 | 0.0454 | 0.9437 | 0.8894 | 0.9936 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | convex | 586 | 0.0178 | 0.0048 | 0.0149 | 0.0279 | 0.0374 | 0.7884 | 0.7155 | 0.8638 | 0.0000 | 0.0000 | 0.0000 |
| old | own | 17-30 | top3_stress | 586 | 0.0010 | 0.0000 | 0.0000 | 0.0008 | 0.0030 | 0.1092 | 0.0435 | 0.1960 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | all | linear | 1252 | 0.0161 | 0.0000 | 0.0038 | 0.0296 | 0.0462 | 0.5192 | 0.3856 | 0.6460 | 0.0655 | 0.0215 | 0.1120 |
| new | actual | all | concave | 1252 | 0.0157 | 0.0000 | 0.0040 | 0.0296 | 0.0417 | 0.5272 | 0.3985 | 0.6331 | 0.0399 | 0.0135 | 0.0682 |
| new | actual | all | convex | 1252 | 0.0138 | 0.0000 | 0.0020 | 0.0223 | 0.0447 | 0.4832 | 0.3664 | 0.6030 | 0.0727 | 0.0288 | 0.1150 |
| new | actual | all | top3_stress | 1252 | 0.0050 | 0.0000 | 0.0000 | 0.0074 | 0.0217 | 0.3339 | 0.2512 | 0.4245 | 0.0982 | 0.0461 | 0.1392 |
| new | actual | 1-3 | linear | 128 | -0.0028 | -0.0032 | -0.0002 | 0.0003 | 0.0016 | 0.0781 | 0.0081 | 0.1603 | 0.3047 | 0.0606 | 0.5878 |
| new | actual | 1-3 | concave | 128 | -0.0018 | -0.0017 | -0.0002 | 0.0002 | 0.0039 | 0.1328 | 0.0000 | 0.3185 | 0.1406 | 0.0204 | 0.2761 |
| new | actual | 1-3 | convex | 128 | -0.0041 | -0.0056 | -0.0014 | 0.0000 | 0.0004 | 0.0703 | 0.0080 | 0.1458 | 0.3516 | 0.1250 | 0.6021 |
| new | actual | 1-3 | top3_stress | 128 | -0.0055 | -0.0089 | -0.0029 | -0.0001 | 0.0000 | 0.0156 | 0.0000 | 0.0630 | 0.5469 | 0.2477 | 0.8226 |
| new | actual | 4-10 | linear | 295 | 0.0048 | 0.0000 | 0.0009 | 0.0070 | 0.0169 | 0.3627 | 0.1569 | 0.5860 | 0.1119 | 0.0432 | 0.1937 |
| new | actual | 4-10 | concave | 295 | 0.0046 | 0.0000 | 0.0009 | 0.0055 | 0.0162 | 0.3797 | 0.2023 | 0.5584 | 0.0712 | 0.0218 | 0.1446 |
| new | actual | 4-10 | convex | 295 | 0.0047 | -0.0000 | 0.0004 | 0.0083 | 0.0198 | 0.3525 | 0.1579 | 0.5766 | 0.1424 | 0.0607 | 0.2168 |
| new | actual | 4-10 | top3_stress | 295 | 0.0024 | -0.0001 | 0.0001 | 0.0069 | 0.0142 | 0.3390 | 0.1508 | 0.5587 | 0.1695 | 0.0732 | 0.2418 |
| new | actual | 11-16 | linear | 243 | 0.0277 | 0.0006 | 0.0240 | 0.0414 | 0.0541 | 0.7160 | 0.5413 | 0.8614 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 11-16 | concave | 243 | 0.0212 | 0.0003 | 0.0171 | 0.0302 | 0.0423 | 0.6996 | 0.5049 | 0.8606 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 11-16 | convex | 243 | 0.0314 | 0.0006 | 0.0277 | 0.0455 | 0.0639 | 0.7078 | 0.5153 | 0.8609 | 0.0000 | 0.0000 | 0.0000 |
| new | actual | 11-16 | top3_stress | 243 | 0.0168 | 0.0001 | 0.0146 | 0.0244 | 0.0337 | 0.6914 | 0.5048 | 0.8406 | 0.0041 | 0.0000 | 0.0260 |
| new | actual | 17-30 | linear | 586 | 0.0212 | 0.0000 | 0.0150 | 0.0362 | 0.0511 | 0.6126 | 0.4045 | 0.7858 | 0.0171 | 0.0000 | 0.0549 |
| new | actual | 17-30 | concave | 586 | 0.0228 | 0.0000 | 0.0212 | 0.0364 | 0.0502 | 0.6160 | 0.4105 | 0.7848 | 0.0188 | 0.0000 | 0.0554 |
| new | actual | 17-30 | convex | 586 | 0.0151 | 0.0000 | 0.0050 | 0.0237 | 0.0450 | 0.5461 | 0.3688 | 0.6887 | 0.0068 | 0.0000 | 0.0285 |
| new | actual | 17-30 | top3_stress | 586 | 0.0037 | 0.0000 | 0.0000 | 0.0027 | 0.0138 | 0.2526 | 0.1696 | 0.3672 | 0.0034 | 0.0000 | 0.0140 |
| new | own | all | linear | 1252 | 0.0237 | 0.0004 | 0.0171 | 0.0399 | 0.0551 | 0.6933 | 0.6161 | 0.7869 | 0.0439 | 0.0146 | 0.0745 |
| new | own | all | concave | 1252 | 0.0210 | 0.0003 | 0.0209 | 0.0352 | 0.0452 | 0.6773 | 0.6017 | 0.7740 | 0.0048 | 0.0000 | 0.0158 |
| new | own | all | convex | 1252 | 0.0212 | 0.0002 | 0.0103 | 0.0350 | 0.0581 | 0.6334 | 0.5627 | 0.7131 | 0.0663 | 0.0299 | 0.0944 |
| new | own | all | top3_stress | 1252 | 0.0074 | 0.0000 | 0.0007 | 0.0124 | 0.0250 | 0.4305 | 0.3417 | 0.5254 | 0.0903 | 0.0417 | 0.1309 |
| new | own | 1-3 | linear | 128 | -0.0016 | -0.0026 | -0.0008 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.2422 | 0.0354 | 0.5088 |
| new | own | 1-3 | concave | 128 | -0.0008 | -0.0013 | -0.0004 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0234 | 0.0000 | 0.0833 |
| new | own | 1-3 | convex | 128 | -0.0030 | -0.0050 | -0.0015 | -0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.3594 | 0.1583 | 0.5798 |
| new | own | 1-3 | top3_stress | 128 | -0.0053 | -0.0089 | -0.0028 | -0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.5000 | 0.2330 | 0.7656 |
| new | own | 4-10 | linear | 295 | 0.0039 | 0.0000 | 0.0004 | 0.0063 | 0.0132 | 0.3492 | 0.1587 | 0.5623 | 0.0814 | 0.0287 | 0.1336 |
| new | own | 4-10 | concave | 295 | 0.0025 | 0.0000 | 0.0002 | 0.0038 | 0.0079 | 0.2881 | 0.0990 | 0.5138 | 0.0102 | 0.0000 | 0.0343 |
| new | own | 4-10 | convex | 295 | 0.0050 | -0.0000 | 0.0005 | 0.0089 | 0.0187 | 0.3729 | 0.1739 | 0.5831 | 0.1254 | 0.0517 | 0.1836 |
| new | own | 4-10 | top3_stress | 295 | 0.0029 | -0.0000 | 0.0001 | 0.0080 | 0.0148 | 0.3593 | 0.1727 | 0.5547 | 0.1661 | 0.0725 | 0.2444 |
| new | own | 11-16 | linear | 243 | 0.0352 | 0.0146 | 0.0342 | 0.0478 | 0.0657 | 0.9012 | 0.7611 | 0.9953 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | concave | 243 | 0.0231 | 0.0092 | 0.0221 | 0.0322 | 0.0442 | 0.8642 | 0.7214 | 0.9734 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | convex | 243 | 0.0431 | 0.0186 | 0.0400 | 0.0571 | 0.0815 | 0.9095 | 0.7714 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 11-16 | top3_stress | 243 | 0.0227 | 0.0113 | 0.0197 | 0.0293 | 0.0456 | 0.8848 | 0.7552 | 0.9828 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | linear | 586 | 0.0344 | 0.0168 | 0.0319 | 0.0460 | 0.0632 | 0.9317 | 0.8661 | 0.9916 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | concave | 586 | 0.0343 | 0.0255 | 0.0338 | 0.0414 | 0.0524 | 0.9437 | 0.8894 | 0.9936 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | convex | 586 | 0.0255 | 0.0048 | 0.0163 | 0.0386 | 0.0607 | 0.7884 | 0.7155 | 0.8638 | 0.0000 | 0.0000 | 0.0000 |
| new | own | 17-30 | top3_stress | 586 | 0.0060 | 0.0000 | 0.0003 | 0.0074 | 0.0208 | 0.3720 | 0.2706 | 0.4897 | 0.0000 | 0.0000 | 0.0000 |
| delta | actual | all | linear | 1252 | -0.0016 | -0.0071 | 0.0000 | 0.0013 | 0.0112 | 0.2244 | 0.1681 | 0.2971 | 0.3291 | 0.2432 | 0.4016 |
| delta | actual | all | concave | 1252 | -0.0008 | -0.0045 | 0.0000 | 0.0013 | 0.0082 | 0.2013 | 0.1551 | 0.2626 | 0.3003 | 0.2105 | 0.3960 |
| delta | actual | all | convex | 1252 | -0.0024 | -0.0107 | 0.0000 | 0.0016 | 0.0138 | 0.2356 | 0.1792 | 0.3025 | 0.3626 | 0.3124 | 0.4073 |
| delta | actual | all | top3_stress | 1252 | -0.0019 | -0.0069 | 0.0000 | 0.0012 | 0.0122 | 0.2196 | 0.1602 | 0.2913 | 0.2915 | 0.2330 | 0.3486 |
| delta | actual | 1-3 | linear | 128 | -0.0057 | -0.0080 | -0.0026 | -0.0014 | -0.0006 | 0.0234 | 0.0000 | 0.0813 | 0.4766 | 0.1393 | 0.7656 |
| delta | actual | 1-3 | concave | 128 | -0.0033 | -0.0048 | -0.0015 | -0.0005 | 0.0015 | 0.0391 | 0.0000 | 0.1301 | 0.3672 | 0.0643 | 0.6615 |
| delta | actual | 1-3 | convex | 128 | -0.0092 | -0.0140 | -0.0051 | -0.0029 | -0.0015 | 0.0078 | 0.0000 | 0.0473 | 0.7812 | 0.6364 | 0.9167 |
| delta | actual | 1-3 | top3_stress | 128 | -0.0098 | -0.0150 | -0.0042 | -0.0005 | -0.0000 | 0.0078 | 0.0000 | 0.0479 | 0.5469 | 0.2556 | 0.8042 |
| delta | actual | 4-10 | linear | 295 | -0.0133 | -0.0208 | -0.0116 | -0.0053 | 0.0000 | 0.0237 | 0.0000 | 0.0709 | 0.8102 | 0.6516 | 0.9440 |
| delta | actual | 4-10 | concave | 295 | -0.0092 | -0.0135 | -0.0068 | -0.0025 | 0.0000 | 0.0441 | 0.0000 | 0.1224 | 0.7390 | 0.5578 | 0.9290 |
| delta | actual | 4-10 | convex | 295 | -0.0184 | -0.0271 | -0.0176 | -0.0102 | 0.0000 | 0.0203 | 0.0000 | 0.0566 | 0.8576 | 0.7516 | 0.9512 |
| delta | actual | 4-10 | top3_stress | 295 | -0.0160 | -0.0224 | -0.0152 | -0.0090 | 0.0000 | 0.0136 | 0.0000 | 0.0568 | 0.8475 | 0.7326 | 0.9496 |
| delta | actual | 11-16 | linear | 243 | -0.0007 | -0.0098 | 0.0000 | 0.0069 | 0.0195 | 0.3868 | 0.2585 | 0.5098 | 0.3868 | 0.1966 | 0.5442 |
| delta | actual | 11-16 | concave | 243 | -0.0016 | -0.0066 | 0.0000 | 0.0038 | 0.0123 | 0.3086 | 0.1907 | 0.4214 | 0.3704 | 0.1521 | 0.5417 |
| delta | actual | 11-16 | convex | 243 | 0.0015 | -0.0095 | 0.0000 | 0.0107 | 0.0231 | 0.4156 | 0.2906 | 0.5430 | 0.3539 | 0.1860 | 0.4919 |
| delta | actual | 11-16 | top3_stress | 243 | 0.0075 | 0.0000 | 0.0038 | 0.0136 | 0.0213 | 0.5267 | 0.3801 | 0.6651 | 0.1605 | 0.0705 | 0.2480 |
| delta | actual | 17-30 | linear | 586 | 0.0049 | 0.0000 | 0.0000 | 0.0043 | 0.0168 | 0.3020 | 0.2017 | 0.4302 | 0.0307 | 0.0035 | 0.0655 |
| delta | actual | 17-30 | concave | 586 | 0.0042 | 0.0000 | 0.0000 | 0.0029 | 0.0142 | 0.2713 | 0.1946 | 0.3699 | 0.0358 | 0.0037 | 0.0745 |
| delta | actual | 17-30 | convex | 586 | 0.0055 | 0.0000 | 0.0000 | 0.0059 | 0.0188 | 0.3191 | 0.2160 | 0.4466 | 0.0256 | 0.0033 | 0.0571 |
| delta | actual | 17-30 | top3_stress | 586 | 0.0031 | 0.0000 | 0.0000 | 0.0025 | 0.0118 | 0.2423 | 0.1661 | 0.3520 | 0.0102 | 0.0000 | 0.0267 |
| delta | own | all | linear | 1252 | -0.0005 | -0.0077 | 0.0000 | 0.0041 | 0.0139 | 0.2867 | 0.2382 | 0.3323 | 0.3722 | 0.3240 | 0.4169 |
| delta | own | all | concave | 1252 | -0.0003 | -0.0045 | 0.0000 | 0.0022 | 0.0084 | 0.2436 | 0.1969 | 0.2847 | 0.3235 | 0.2686 | 0.3803 |
| delta | own | all | convex | 1252 | -0.0008 | -0.0118 | 0.0000 | 0.0067 | 0.0202 | 0.3091 | 0.2616 | 0.3533 | 0.3930 | 0.3487 | 0.4326 |
| delta | own | all | top3_stress | 1252 | -0.0004 | -0.0083 | 0.0000 | 0.0055 | 0.0174 | 0.3043 | 0.2291 | 0.3746 | 0.3115 | 0.2460 | 0.3666 |
| delta | own | 1-3 | linear | 128 | -0.0049 | -0.0061 | -0.0034 | -0.0020 | -0.0014 | 0.0000 | 0.0000 | 0.0000 | 0.5547 | 0.2569 | 0.8165 |
| delta | own | 1-3 | concave | 128 | -0.0026 | -0.0032 | -0.0018 | -0.0011 | -0.0008 | 0.0000 | 0.0000 | 0.0000 | 0.2969 | 0.0902 | 0.5403 |
| delta | own | 1-3 | convex | 128 | -0.0085 | -0.0108 | -0.0058 | -0.0035 | -0.0025 | 0.0000 | 0.0000 | 0.0000 | 0.8359 | 0.6667 | 0.9658 |
| delta | own | 1-3 | top3_stress | 128 | -0.0097 | -0.0149 | -0.0042 | -0.0005 | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.5625 | 0.2556 | 0.8362 |
| delta | own | 4-10 | linear | 295 | -0.0125 | -0.0175 | -0.0109 | -0.0075 | -0.0045 | 0.0000 | 0.0000 | 0.0000 | 0.9322 | 0.8356 | 0.9904 |
| delta | own | 4-10 | concave | 295 | -0.0072 | -0.0102 | -0.0061 | -0.0042 | -0.0025 | 0.0000 | 0.0000 | 0.0000 | 0.8814 | 0.7587 | 0.9788 |
| delta | own | 4-10 | convex | 295 | -0.0192 | -0.0266 | -0.0176 | -0.0120 | -0.0075 | 0.0000 | 0.0000 | 0.0000 | 0.9424 | 0.8423 | 0.9926 |
| delta | own | 4-10 | top3_stress | 295 | -0.0169 | -0.0223 | -0.0166 | -0.0104 | -0.0049 | 0.0136 | 0.0000 | 0.0470 | 0.9220 | 0.7932 | 0.9908 |
| delta | own | 11-16 | linear | 243 | 0.0018 | -0.0097 | 0.0030 | 0.0097 | 0.0191 | 0.5185 | 0.3728 | 0.7068 | 0.4074 | 0.2201 | 0.5357 |
| delta | own | 11-16 | concave | 243 | 0.0006 | -0.0065 | 0.0013 | 0.0054 | 0.0110 | 0.4280 | 0.2955 | 0.5551 | 0.3827 | 0.1681 | 0.5299 |
| delta | own | 11-16 | convex | 243 | 0.0049 | -0.0110 | 0.0059 | 0.0166 | 0.0291 | 0.5597 | 0.4216 | 0.7566 | 0.3786 | 0.2027 | 0.5135 |
| delta | own | 11-16 | top3_stress | 243 | 0.0112 | 0.0001 | 0.0097 | 0.0183 | 0.0279 | 0.6831 | 0.5142 | 0.8462 | 0.1770 | 0.0632 | 0.2985 |
| delta | own | 17-30 | linear | 586 | 0.0054 | 0.0000 | 0.0002 | 0.0084 | 0.0176 | 0.3976 | 0.3196 | 0.4846 | 0.0358 | 0.0032 | 0.0858 |
| delta | own | 17-30 | concave | 586 | 0.0033 | 0.0000 | 0.0001 | 0.0052 | 0.0106 | 0.3430 | 0.2577 | 0.4288 | 0.0239 | 0.0020 | 0.0545 |
| delta | own | 17-30 | convex | 586 | 0.0077 | 0.0000 | 0.0004 | 0.0114 | 0.0251 | 0.4283 | 0.3497 | 0.5132 | 0.0256 | 0.0020 | 0.0600 |
| delta | own | 17-30 | top3_stress | 586 | 0.0051 | 0.0000 | 0.0002 | 0.0066 | 0.0172 | 0.3601 | 0.2558 | 0.4737 | 0.0051 | 0.0000 | 0.0181 |

## H1

| n_team_games | share_neg_new | share_neg_old | diff_new_minus_old | diff_lo99 | diff_hi99 | n_new_reversals | crossing_share | crossing_lo99 | crossing_hi99 | supported |
|---|---|---|---|---|---|---|---|---|---|---|
| 163 | 0.3190 | 0.0000 | 0.3190 | 0.1074 | 0.5484 | 111 | 1.0000 | 1.0000 | 1.0000 | True |

## T5_attr_portfolio_effect

| rule | band | n | mean | q25 | median | q75 | q90 | share_nonzero |
|---|---|---|---|---|---|---|---|---|
| old | all | 1252 | -0.0066 | -0.0134 | 0.0000 | 0.0000 | 0.0022 | 0.4257 |
| old | 1-3 | 128 | -0.0004 | 0.0000 | 0.0000 | 0.0000 | 0.0020 | 0.0938 |
| old | 4-10 | 295 | 0.0016 | -0.0000 | 0.0000 | 0.0019 | 0.0132 | 0.3695 |
| old | 11-16 | 243 | -0.0050 | -0.0160 | 0.0000 | 0.0000 | 0.0022 | 0.4198 |
| old | 17-30 | 586 | -0.0127 | -0.0250 | -0.0036 | 0.0000 | 0.0000 | 0.5290 |
| new | all | 1252 | -0.0076 | -0.0099 | 0.0000 | 0.0000 | 0.0032 | 0.4329 |
| new | 1-3 | 128 | -0.0012 | -0.0001 | 0.0000 | 0.0004 | 0.0037 | 0.2109 |
| new | 4-10 | 295 | 0.0009 | 0.0000 | 0.0000 | 0.0014 | 0.0062 | 0.3017 |
| new | 11-16 | 243 | -0.0075 | -0.0091 | 0.0000 | 0.0000 | 0.0040 | 0.3951 |
| new | 17-30 | 586 | -0.0133 | -0.0222 | -0.0037 | 0.0000 | 0.0000 | 0.5631 |
| delta | all | 1252 | -0.0010 | -0.0002 | 0.0000 | 0.0001 | 0.0048 | 0.3019 |
| delta | 1-3 | 128 | -0.0008 | -0.0001 | 0.0000 | 0.0004 | 0.0030 | 0.1797 |
| delta | 4-10 | 295 | -0.0007 | -0.0006 | 0.0000 | 0.0001 | 0.0061 | 0.3458 |
| delta | 11-16 | 243 | -0.0026 | -0.0019 | 0.0000 | 0.0000 | 0.0069 | 0.3704 |
| delta | 17-30 | 586 | -0.0006 | -0.0000 | 0.0000 | 0.0001 | 0.0046 | 0.2782 |

## T5_7_rollover

| rule | portfolio | band | curve | rho | measure | n | mean | q25 | median | q75 | q90 | share_sign_flip | vbar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| old | actual | all | - | 0.0000 | M | 1252 | 0.0062 | -0.0000 | 0.0000 | 0.0000 | 0.0150 |  |  |
| old | actual | all | linear | 0.0000 | tau | 1252 | 0.0177 | 0.0008 | 0.0102 | 0.0301 | 0.0431 | 0.0000 | 0.5000 |
| old | actual | all | linear | 0.5000 | tau | 1252 | 0.0162 | 0.0008 | 0.0097 | 0.0284 | 0.0405 | 0.0032 | 0.5000 |
| old | actual | all | linear | 0.8000 | tau | 1252 | 0.0152 | 0.0006 | 0.0089 | 0.0274 | 0.0398 | 0.0048 | 0.5000 |
| old | actual | all | concave | 0.0000 | tau | 1252 | 0.0165 | 0.0007 | 0.0088 | 0.0284 | 0.0394 | 0.0000 | 0.6599 |
| old | actual | all | concave | 0.5000 | tau | 1252 | 0.0145 | 0.0007 | 0.0077 | 0.0263 | 0.0368 | 0.0072 | 0.6599 |
| old | actual | all | concave | 0.8000 | tau | 1252 | 0.0133 | 0.0006 | 0.0069 | 0.0240 | 0.0357 | 0.0104 | 0.6599 |
| old | actual | all | convex | 0.0000 | tau | 1252 | 0.0162 | 0.0005 | 0.0092 | 0.0279 | 0.0421 | 0.0000 | 0.3391 |
| old | actual | all | convex | 0.5000 | tau | 1252 | 0.0152 | 0.0004 | 0.0083 | 0.0267 | 0.0398 | 0.0024 | 0.3391 |
| old | actual | all | convex | 0.8000 | tau | 1252 | 0.0145 | 0.0003 | 0.0076 | 0.0255 | 0.0388 | 0.0064 | 0.3391 |
| old | actual | all | top3_stress | 0.0000 | tau | 1252 | 0.0069 | 0.0000 | 0.0009 | 0.0109 | 0.0234 | 0.0000 | 0.1000 |
| old | actual | all | top3_stress | 0.5000 | tau | 1252 | 0.0066 | 0.0000 | 0.0006 | 0.0105 | 0.0228 | 0.1142 | 0.1000 |
| old | actual | all | top3_stress | 0.8000 | tau | 1252 | 0.0064 | 0.0000 | 0.0005 | 0.0104 | 0.0223 | 0.1190 | 0.1000 |
| old | actual | 1-3 | - | 0.0000 | M | 128 | -0.0001 | -0.0000 | 0.0000 | 0.0000 | 0.0001 |  |  |
| old | actual | 1-3 | linear | 0.0000 | tau | 128 | 0.0029 | 0.0018 | 0.0026 | 0.0053 | 0.0075 | 0.0000 | 0.5000 |
| old | actual | 1-3 | linear | 0.5000 | tau | 128 | 0.0029 | 0.0018 | 0.0026 | 0.0054 | 0.0075 | 0.0000 | 0.5000 |
| old | actual | 1-3 | linear | 0.8000 | tau | 128 | 0.0030 | 0.0017 | 0.0026 | 0.0054 | 0.0074 | 0.0000 | 0.5000 |
| old | actual | 1-3 | concave | 0.0000 | tau | 128 | 0.0015 | 0.0010 | 0.0015 | 0.0029 | 0.0044 | 0.0000 | 0.6599 |
| old | actual | 1-3 | concave | 0.5000 | tau | 128 | 0.0015 | 0.0010 | 0.0015 | 0.0030 | 0.0044 | 0.0156 | 0.6599 |
| old | actual | 1-3 | concave | 0.8000 | tau | 128 | 0.0016 | 0.0010 | 0.0015 | 0.0030 | 0.0044 | 0.0234 | 0.6599 |
| old | actual | 1-3 | convex | 0.0000 | tau | 128 | 0.0051 | 0.0029 | 0.0043 | 0.0075 | 0.0106 | 0.0000 | 0.3391 |
| old | actual | 1-3 | convex | 0.5000 | tau | 128 | 0.0051 | 0.0029 | 0.0044 | 0.0076 | 0.0104 | 0.0000 | 0.3391 |
| old | actual | 1-3 | convex | 0.8000 | tau | 128 | 0.0051 | 0.0029 | 0.0044 | 0.0076 | 0.0107 | 0.0000 | 0.3391 |
| old | actual | 1-3 | top3_stress | 0.0000 | tau | 128 | 0.0043 | 0.0003 | 0.0014 | 0.0056 | 0.0128 | 0.0000 | 0.1000 |
| old | actual | 1-3 | top3_stress | 0.5000 | tau | 128 | 0.0043 | 0.0003 | 0.0014 | 0.0056 | 0.0128 | 0.0078 | 0.1000 |
| old | actual | 1-3 | top3_stress | 0.8000 | tau | 128 | 0.0043 | 0.0003 | 0.0015 | 0.0057 | 0.0128 | 0.0078 | 0.1000 |
| old | actual | 4-10 | - | 0.0000 | M | 295 | 0.0077 | -0.0000 | 0.0000 | 0.0020 | 0.0354 |  |  |
| old | actual | 4-10 | linear | 0.0000 | tau | 295 | 0.0181 | 0.0056 | 0.0143 | 0.0273 | 0.0395 | 0.0000 | 0.5000 |
| old | actual | 4-10 | linear | 0.5000 | tau | 295 | 0.0161 | 0.0058 | 0.0134 | 0.0252 | 0.0335 | 0.0102 | 0.5000 |
| old | actual | 4-10 | linear | 0.8000 | tau | 295 | 0.0150 | 0.0056 | 0.0124 | 0.0239 | 0.0314 | 0.0102 | 0.5000 |
| old | actual | 4-10 | concave | 0.0000 | tau | 295 | 0.0138 | 0.0032 | 0.0093 | 0.0179 | 0.0346 | 0.0000 | 0.6599 |
| old | actual | 4-10 | concave | 0.5000 | tau | 295 | 0.0113 | 0.0031 | 0.0084 | 0.0170 | 0.0261 | 0.0136 | 0.6599 |
| old | actual | 4-10 | concave | 0.8000 | tau | 295 | 0.0097 | 0.0031 | 0.0077 | 0.0153 | 0.0212 | 0.0237 | 0.6599 |
| old | actual | 4-10 | convex | 0.0000 | tau | 295 | 0.0231 | 0.0091 | 0.0197 | 0.0364 | 0.0465 | 0.0000 | 0.3391 |
| old | actual | 4-10 | convex | 0.5000 | tau | 295 | 0.0218 | 0.0091 | 0.0179 | 0.0352 | 0.0437 | 0.0034 | 0.3391 |
| old | actual | 4-10 | convex | 0.8000 | tau | 295 | 0.0210 | 0.0089 | 0.0168 | 0.0325 | 0.0432 | 0.0068 | 0.3391 |
| old | actual | 4-10 | top3_stress | 0.0000 | tau | 295 | 0.0184 | 0.0097 | 0.0169 | 0.0281 | 0.0343 | 0.0000 | 0.1000 |
| old | actual | 4-10 | top3_stress | 0.5000 | tau | 295 | 0.0180 | 0.0095 | 0.0166 | 0.0277 | 0.0335 | 0.0034 | 0.1000 |
| old | actual | 4-10 | top3_stress | 0.8000 | tau | 295 | 0.0178 | 0.0094 | 0.0165 | 0.0273 | 0.0328 | 0.0034 | 0.1000 |
| old | actual | 11-16 | - | 0.0000 | M | 243 | 0.0103 | -0.0000 | 0.0000 | 0.0002 | 0.0166 |  |  |
| old | actual | 11-16 | linear | 0.0000 | tau | 243 | 0.0284 | 0.0080 | 0.0277 | 0.0389 | 0.0526 | 0.0000 | 0.5000 |
| old | actual | 11-16 | linear | 0.5000 | tau | 243 | 0.0258 | 0.0062 | 0.0262 | 0.0378 | 0.0517 | 0.0000 | 0.5000 |
| old | actual | 11-16 | linear | 0.8000 | tau | 243 | 0.0243 | 0.0049 | 0.0256 | 0.0367 | 0.0472 | 0.0000 | 0.5000 |
| old | actual | 11-16 | concave | 0.0000 | tau | 243 | 0.0229 | 0.0065 | 0.0193 | 0.0285 | 0.0398 | 0.0000 | 0.6599 |
| old | actual | 11-16 | concave | 0.5000 | tau | 243 | 0.0194 | 0.0055 | 0.0187 | 0.0271 | 0.0360 | 0.0082 | 0.6599 |
| old | actual | 11-16 | concave | 0.8000 | tau | 243 | 0.0174 | 0.0040 | 0.0173 | 0.0261 | 0.0340 | 0.0082 | 0.6599 |
| old | actual | 11-16 | convex | 0.0000 | tau | 243 | 0.0298 | 0.0079 | 0.0298 | 0.0421 | 0.0599 | 0.0000 | 0.3391 |
| old | actual | 11-16 | convex | 0.5000 | tau | 243 | 0.0281 | 0.0063 | 0.0287 | 0.0421 | 0.0568 | 0.0082 | 0.3391 |
| old | actual | 11-16 | convex | 0.8000 | tau | 243 | 0.0270 | 0.0055 | 0.0284 | 0.0396 | 0.0549 | 0.0123 | 0.3391 |
| old | actual | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0093 | 0.0020 | 0.0067 | 0.0150 | 0.0214 | 0.0000 | 0.1000 |
| old | actual | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0088 | 0.0015 | 0.0063 | 0.0144 | 0.0213 | 0.0370 | 0.1000 |
| old | actual | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0085 | 0.0007 | 0.0061 | 0.0141 | 0.0213 | 0.0535 | 0.1000 |
| old | actual | 17-30 | - | 0.0000 | M | 586 | 0.0050 | -0.0000 | 0.0000 | 0.0000 | 0.0049 |  |  |
| old | actual | 17-30 | linear | 0.0000 | tau | 586 | 0.0163 | 0.0000 | 0.0075 | 0.0301 | 0.0422 | 0.0000 | 0.5000 |
| old | actual | 17-30 | linear | 0.5000 | tau | 586 | 0.0150 | 0.0000 | 0.0060 | 0.0286 | 0.0408 | 0.0017 | 0.5000 |
| old | actual | 17-30 | linear | 0.8000 | tau | 586 | 0.0143 | 0.0000 | 0.0045 | 0.0276 | 0.0404 | 0.0051 | 0.5000 |
| old | actual | 17-30 | concave | 0.0000 | tau | 586 | 0.0186 | 0.0000 | 0.0116 | 0.0329 | 0.0423 | 0.0000 | 0.6599 |
| old | actual | 17-30 | concave | 0.5000 | tau | 586 | 0.0169 | 0.0000 | 0.0090 | 0.0320 | 0.0399 | 0.0017 | 0.6599 |
| old | actual | 17-30 | concave | 0.8000 | tau | 586 | 0.0159 | 0.0000 | 0.0072 | 0.0316 | 0.0395 | 0.0017 | 0.6599 |
| old | actual | 17-30 | convex | 0.0000 | tau | 586 | 0.0095 | 0.0000 | 0.0028 | 0.0158 | 0.0292 | 0.0000 | 0.3391 |
| old | actual | 17-30 | convex | 0.5000 | tau | 586 | 0.0087 | 0.0000 | 0.0026 | 0.0144 | 0.0282 | 0.0000 | 0.3391 |
| old | actual | 17-30 | convex | 0.8000 | tau | 586 | 0.0082 | 0.0000 | 0.0018 | 0.0132 | 0.0278 | 0.0051 | 0.3391 |
| old | actual | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0006 | 0.0000 | 0.0000 | 0.0003 | 0.0019 | 0.0000 | 0.1000 |
| old | actual | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0004 | 0.0000 | 0.0000 | 0.0001 | 0.0012 | 0.2253 | 0.1000 |
| old | actual | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0002 | 0.0000 | 0.0000 | 0.0001 | 0.0013 | 0.2287 | 0.1000 |
| old | own | all | - | 0.0000 | M | 1252 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | all | linear | 0.0000 | tau | 1252 | 0.0243 | 0.0082 | 0.0241 | 0.0359 | 0.0458 | 0.0000 | 0.5000 |
| old | own | all | linear | 0.5000 | tau | 1252 | 0.0243 | 0.0082 | 0.0241 | 0.0359 | 0.0458 | 0.0000 | 0.5000 |
| old | own | all | linear | 0.8000 | tau | 1252 | 0.0243 | 0.0082 | 0.0241 | 0.0359 | 0.0458 | 0.0000 | 0.5000 |
| old | own | all | concave | 0.0000 | tau | 1252 | 0.0213 | 0.0062 | 0.0212 | 0.0322 | 0.0397 | 0.0000 | 0.6599 |
| old | own | all | concave | 0.5000 | tau | 1252 | 0.0213 | 0.0062 | 0.0212 | 0.0322 | 0.0397 | 0.0000 | 0.6599 |
| old | own | all | concave | 0.8000 | tau | 1252 | 0.0213 | 0.0062 | 0.0212 | 0.0322 | 0.0397 | 0.0000 | 0.6599 |
| old | own | all | convex | 0.0000 | tau | 1252 | 0.0220 | 0.0062 | 0.0189 | 0.0333 | 0.0452 | 0.0000 | 0.3391 |
| old | own | all | convex | 0.5000 | tau | 1252 | 0.0220 | 0.0062 | 0.0189 | 0.0333 | 0.0452 | 0.0000 | 0.3391 |
| old | own | all | convex | 0.8000 | tau | 1252 | 0.0220 | 0.0062 | 0.0189 | 0.0333 | 0.0452 | 0.0000 | 0.3391 |
| old | own | all | top3_stress | 0.0000 | tau | 1252 | 0.0078 | 0.0000 | 0.0026 | 0.0131 | 0.0249 | 0.0000 | 0.1000 |
| old | own | all | top3_stress | 0.5000 | tau | 1252 | 0.0078 | 0.0000 | 0.0026 | 0.0131 | 0.0249 | 0.0719 | 0.1000 |
| old | own | all | top3_stress | 0.8000 | tau | 1252 | 0.0078 | 0.0000 | 0.0026 | 0.0131 | 0.0249 | 0.0711 | 0.1000 |
| old | own | 1-3 | - | 0.0000 | M | 128 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 1-3 | linear | 0.0000 | tau | 128 | 0.0033 | 0.0019 | 0.0025 | 0.0040 | 0.0062 | 0.0000 | 0.5000 |
| old | own | 1-3 | linear | 0.5000 | tau | 128 | 0.0033 | 0.0019 | 0.0025 | 0.0040 | 0.0062 | 0.0000 | 0.5000 |
| old | own | 1-3 | linear | 0.8000 | tau | 128 | 0.0033 | 0.0019 | 0.0025 | 0.0040 | 0.0062 | 0.0000 | 0.5000 |
| old | own | 1-3 | concave | 0.0000 | tau | 128 | 0.0018 | 0.0010 | 0.0014 | 0.0022 | 0.0034 | 0.0000 | 0.6599 |
| old | own | 1-3 | concave | 0.5000 | tau | 128 | 0.0018 | 0.0010 | 0.0014 | 0.0022 | 0.0034 | 0.0000 | 0.6599 |
| old | own | 1-3 | concave | 0.8000 | tau | 128 | 0.0018 | 0.0010 | 0.0014 | 0.0022 | 0.0034 | 0.0000 | 0.6599 |
| old | own | 1-3 | convex | 0.0000 | tau | 128 | 0.0055 | 0.0032 | 0.0042 | 0.0068 | 0.0104 | 0.0000 | 0.3391 |
| old | own | 1-3 | convex | 0.5000 | tau | 128 | 0.0055 | 0.0032 | 0.0042 | 0.0068 | 0.0104 | 0.0000 | 0.3391 |
| old | own | 1-3 | convex | 0.8000 | tau | 128 | 0.0055 | 0.0032 | 0.0042 | 0.0068 | 0.0104 | 0.0000 | 0.3391 |
| old | own | 1-3 | top3_stress | 0.0000 | tau | 128 | 0.0044 | 0.0003 | 0.0014 | 0.0057 | 0.0134 | 0.0000 | 0.1000 |
| old | own | 1-3 | top3_stress | 0.5000 | tau | 128 | 0.0044 | 0.0003 | 0.0014 | 0.0057 | 0.0134 | 0.0078 | 0.1000 |
| old | own | 1-3 | top3_stress | 0.8000 | tau | 128 | 0.0044 | 0.0003 | 0.0014 | 0.0057 | 0.0134 | 0.0078 | 0.1000 |
| old | own | 4-10 | - | 0.0000 | M | 295 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 4-10 | linear | 0.0000 | tau | 295 | 0.0164 | 0.0071 | 0.0125 | 0.0247 | 0.0331 | 0.0000 | 0.5000 |
| old | own | 4-10 | linear | 0.5000 | tau | 295 | 0.0164 | 0.0071 | 0.0125 | 0.0247 | 0.0331 | 0.0000 | 0.5000 |
| old | own | 4-10 | linear | 0.8000 | tau | 295 | 0.0164 | 0.0071 | 0.0125 | 0.0247 | 0.0331 | 0.0000 | 0.5000 |
| old | own | 4-10 | concave | 0.0000 | tau | 295 | 0.0097 | 0.0039 | 0.0070 | 0.0147 | 0.0200 | 0.0000 | 0.6599 |
| old | own | 4-10 | concave | 0.5000 | tau | 295 | 0.0097 | 0.0039 | 0.0070 | 0.0147 | 0.0200 | 0.0000 | 0.6599 |
| old | own | 4-10 | concave | 0.8000 | tau | 295 | 0.0097 | 0.0039 | 0.0070 | 0.0147 | 0.0200 | 0.0000 | 0.6599 |
| old | own | 4-10 | convex | 0.0000 | tau | 295 | 0.0242 | 0.0115 | 0.0192 | 0.0364 | 0.0466 | 0.0000 | 0.3391 |
| old | own | 4-10 | convex | 0.5000 | tau | 295 | 0.0242 | 0.0115 | 0.0192 | 0.0364 | 0.0466 | 0.0000 | 0.3391 |
| old | own | 4-10 | convex | 0.8000 | tau | 295 | 0.0242 | 0.0115 | 0.0192 | 0.0364 | 0.0466 | 0.0000 | 0.3391 |
| old | own | 4-10 | top3_stress | 0.0000 | tau | 295 | 0.0198 | 0.0112 | 0.0181 | 0.0282 | 0.0340 | 0.0000 | 0.1000 |
| old | own | 4-10 | top3_stress | 0.5000 | tau | 295 | 0.0198 | 0.0112 | 0.0181 | 0.0282 | 0.0340 | 0.0000 | 0.1000 |
| old | own | 4-10 | top3_stress | 0.8000 | tau | 295 | 0.0198 | 0.0112 | 0.0181 | 0.0282 | 0.0340 | 0.0000 | 0.1000 |
| old | own | 11-16 | - | 0.0000 | M | 243 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 11-16 | linear | 0.0000 | tau | 243 | 0.0334 | 0.0225 | 0.0314 | 0.0406 | 0.0551 | 0.0000 | 0.5000 |
| old | own | 11-16 | linear | 0.5000 | tau | 243 | 0.0334 | 0.0225 | 0.0314 | 0.0406 | 0.0551 | 0.0000 | 0.5000 |
| old | own | 11-16 | linear | 0.8000 | tau | 243 | 0.0334 | 0.0225 | 0.0314 | 0.0406 | 0.0551 | 0.0000 | 0.5000 |
| old | own | 11-16 | concave | 0.0000 | tau | 243 | 0.0225 | 0.0146 | 0.0210 | 0.0288 | 0.0370 | 0.0000 | 0.6599 |
| old | own | 11-16 | concave | 0.5000 | tau | 243 | 0.0225 | 0.0146 | 0.0210 | 0.0288 | 0.0370 | 0.0000 | 0.6599 |
| old | own | 11-16 | concave | 0.8000 | tau | 243 | 0.0225 | 0.0146 | 0.0210 | 0.0288 | 0.0370 | 0.0000 | 0.6599 |
| old | own | 11-16 | convex | 0.0000 | tau | 243 | 0.0382 | 0.0273 | 0.0354 | 0.0455 | 0.0661 | 0.0000 | 0.3391 |
| old | own | 11-16 | convex | 0.5000 | tau | 243 | 0.0382 | 0.0273 | 0.0354 | 0.0455 | 0.0661 | 0.0000 | 0.3391 |
| old | own | 11-16 | convex | 0.8000 | tau | 243 | 0.0382 | 0.0273 | 0.0354 | 0.0455 | 0.0661 | 0.0000 | 0.3391 |
| old | own | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0115 | 0.0054 | 0.0088 | 0.0165 | 0.0231 | 0.0000 | 0.1000 |
| old | own | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0115 | 0.0054 | 0.0088 | 0.0165 | 0.0231 | 0.0000 | 0.1000 |
| old | own | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0115 | 0.0054 | 0.0088 | 0.0165 | 0.0231 | 0.0000 | 0.1000 |
| old | own | 17-30 | - | 0.0000 | M | 586 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| old | own | 17-30 | linear | 0.0000 | tau | 586 | 0.0290 | 0.0173 | 0.0293 | 0.0393 | 0.0479 | 0.0000 | 0.5000 |
| old | own | 17-30 | linear | 0.5000 | tau | 586 | 0.0290 | 0.0173 | 0.0293 | 0.0393 | 0.0479 | 0.0000 | 0.5000 |
| old | own | 17-30 | linear | 0.8000 | tau | 586 | 0.0290 | 0.0173 | 0.0293 | 0.0393 | 0.0479 | 0.0000 | 0.5000 |
| old | own | 17-30 | concave | 0.0000 | tau | 586 | 0.0310 | 0.0243 | 0.0313 | 0.0374 | 0.0454 | 0.0000 | 0.6599 |
| old | own | 17-30 | concave | 0.5000 | tau | 586 | 0.0310 | 0.0243 | 0.0313 | 0.0374 | 0.0454 | 0.0000 | 0.6599 |
| old | own | 17-30 | concave | 0.8000 | tau | 586 | 0.0310 | 0.0243 | 0.0313 | 0.0374 | 0.0454 | 0.0000 | 0.6599 |
| old | own | 17-30 | convex | 0.0000 | tau | 586 | 0.0178 | 0.0048 | 0.0149 | 0.0279 | 0.0374 | 0.0000 | 0.3391 |
| old | own | 17-30 | convex | 0.5000 | tau | 586 | 0.0178 | 0.0048 | 0.0149 | 0.0279 | 0.0374 | 0.0000 | 0.3391 |
| old | own | 17-30 | convex | 0.8000 | tau | 586 | 0.0178 | 0.0048 | 0.0149 | 0.0279 | 0.0374 | 0.0000 | 0.3391 |
| old | own | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0010 | 0.0000 | 0.0000 | 0.0008 | 0.0030 | 0.0000 | 0.1000 |
| old | own | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0010 | 0.0000 | 0.0000 | 0.0008 | 0.0030 | 0.1519 | 0.1000 |
| old | own | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0010 | 0.0000 | 0.0000 | 0.0008 | 0.0030 | 0.1502 | 0.1000 |
| new | actual | all | - | 0.0000 | M | 1252 | 0.0063 | -0.0000 | 0.0000 | 0.0000 | 0.0169 |  |  |
| new | actual | all | linear | 0.0000 | tau | 1252 | 0.0161 | 0.0000 | 0.0038 | 0.0296 | 0.0462 | 0.0000 | 0.5000 |
| new | actual | all | linear | 0.5000 | tau | 1252 | 0.0146 | 0.0000 | 0.0035 | 0.0274 | 0.0443 | 0.0312 | 0.5000 |
| new | actual | all | linear | 0.8000 | tau | 1252 | 0.0136 | 0.0000 | 0.0032 | 0.0255 | 0.0423 | 0.0367 | 0.5000 |
| new | actual | all | concave | 0.0000 | tau | 1252 | 0.0157 | 0.0000 | 0.0040 | 0.0296 | 0.0417 | 0.0000 | 0.6599 |
| new | actual | all | concave | 0.5000 | tau | 1252 | 0.0136 | 0.0000 | 0.0030 | 0.0273 | 0.0393 | 0.0032 | 0.6599 |
| new | actual | all | concave | 0.8000 | tau | 1252 | 0.0124 | 0.0000 | 0.0025 | 0.0248 | 0.0369 | 0.0088 | 0.6599 |
| new | actual | all | convex | 0.0000 | tau | 1252 | 0.0138 | 0.0000 | 0.0020 | 0.0223 | 0.0447 | 0.0000 | 0.3391 |
| new | actual | all | convex | 0.5000 | tau | 1252 | 0.0128 | 0.0000 | 0.0018 | 0.0212 | 0.0418 | 0.0040 | 0.3391 |
| new | actual | all | convex | 0.8000 | tau | 1252 | 0.0121 | 0.0000 | 0.0018 | 0.0196 | 0.0411 | 0.0104 | 0.3391 |
| new | actual | all | top3_stress | 0.0000 | tau | 1252 | 0.0050 | 0.0000 | 0.0000 | 0.0074 | 0.0217 | 0.0000 | 0.1000 |
| new | actual | all | top3_stress | 0.5000 | tau | 1252 | 0.0047 | 0.0000 | 0.0000 | 0.0069 | 0.0206 | 0.0647 | 0.1000 |
| new | actual | all | top3_stress | 0.8000 | tau | 1252 | 0.0045 | 0.0000 | 0.0000 | 0.0065 | 0.0196 | 0.0647 | 0.1000 |
| new | actual | 1-3 | - | 0.0000 | M | 128 | -0.0004 | -0.0000 | -0.0000 | 0.0000 | 0.0033 |  |  |
| new | actual | 1-3 | linear | 0.0000 | tau | 128 | -0.0028 | -0.0032 | -0.0002 | 0.0003 | 0.0016 | 0.0000 | 0.5000 |
| new | actual | 1-3 | linear | 0.5000 | tau | 128 | -0.0026 | -0.0031 | -0.0005 | 0.0000 | 0.0006 | 0.1094 | 0.5000 |
| new | actual | 1-3 | linear | 0.8000 | tau | 128 | -0.0026 | -0.0031 | -0.0008 | 0.0000 | 0.0004 | 0.1406 | 0.5000 |
| new | actual | 1-3 | concave | 0.0000 | tau | 128 | -0.0018 | -0.0017 | -0.0002 | 0.0002 | 0.0039 | 0.0000 | 0.6599 |
| new | actual | 1-3 | concave | 0.5000 | tau | 128 | -0.0016 | -0.0017 | -0.0001 | 0.0002 | 0.0022 | 0.0156 | 0.6599 |
| new | actual | 1-3 | concave | 0.8000 | tau | 128 | -0.0015 | -0.0016 | -0.0001 | 0.0001 | 0.0009 | 0.0312 | 0.6599 |
| new | actual | 1-3 | convex | 0.0000 | tau | 128 | -0.0041 | -0.0056 | -0.0014 | 0.0000 | 0.0004 | 0.0000 | 0.3391 |
| new | actual | 1-3 | convex | 0.5000 | tau | 128 | -0.0040 | -0.0061 | -0.0015 | 0.0000 | 0.0002 | 0.0234 | 0.3391 |
| new | actual | 1-3 | convex | 0.8000 | tau | 128 | -0.0040 | -0.0060 | -0.0016 | -0.0000 | 0.0002 | 0.0391 | 0.3391 |
| new | actual | 1-3 | top3_stress | 0.0000 | tau | 128 | -0.0055 | -0.0089 | -0.0029 | -0.0001 | 0.0000 | 0.0000 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.5000 | tau | 128 | -0.0055 | -0.0092 | -0.0029 | -0.0001 | 0.0000 | 0.0703 | 0.1000 |
| new | actual | 1-3 | top3_stress | 0.8000 | tau | 128 | -0.0055 | -0.0092 | -0.0029 | -0.0001 | 0.0000 | 0.0703 | 0.1000 |
| new | actual | 4-10 | - | 0.0000 | M | 295 | 0.0041 | -0.0000 | 0.0000 | 0.0023 | 0.0169 |  |  |
| new | actual | 4-10 | linear | 0.0000 | tau | 295 | 0.0048 | 0.0000 | 0.0009 | 0.0070 | 0.0169 | 0.0000 | 0.5000 |
| new | actual | 4-10 | linear | 0.5000 | tau | 295 | 0.0038 | -0.0000 | 0.0004 | 0.0063 | 0.0157 | 0.0814 | 0.5000 |
| new | actual | 4-10 | linear | 0.8000 | tau | 295 | 0.0031 | -0.0000 | 0.0004 | 0.0058 | 0.0136 | 0.0915 | 0.5000 |
| new | actual | 4-10 | concave | 0.0000 | tau | 295 | 0.0046 | 0.0000 | 0.0009 | 0.0055 | 0.0162 | 0.0000 | 0.6599 |
| new | actual | 4-10 | concave | 0.5000 | tau | 295 | 0.0033 | 0.0000 | 0.0007 | 0.0045 | 0.0114 | 0.0034 | 0.6599 |
| new | actual | 4-10 | concave | 0.8000 | tau | 295 | 0.0025 | 0.0000 | 0.0003 | 0.0040 | 0.0105 | 0.0169 | 0.6599 |
| new | actual | 4-10 | convex | 0.0000 | tau | 295 | 0.0047 | -0.0000 | 0.0004 | 0.0083 | 0.0198 | 0.0000 | 0.3391 |
| new | actual | 4-10 | convex | 0.5000 | tau | 295 | 0.0040 | -0.0000 | 0.0004 | 0.0073 | 0.0184 | 0.0068 | 0.3391 |
| new | actual | 4-10 | convex | 0.8000 | tau | 295 | 0.0036 | -0.0000 | 0.0005 | 0.0073 | 0.0171 | 0.0169 | 0.3391 |
| new | actual | 4-10 | top3_stress | 0.0000 | tau | 295 | 0.0024 | -0.0001 | 0.0001 | 0.0069 | 0.0142 | 0.0000 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.5000 | tau | 295 | 0.0022 | -0.0001 | 0.0001 | 0.0067 | 0.0138 | 0.0169 | 0.1000 |
| new | actual | 4-10 | top3_stress | 0.8000 | tau | 295 | 0.0021 | -0.0001 | 0.0001 | 0.0064 | 0.0132 | 0.0169 | 0.1000 |
| new | actual | 11-16 | - | 0.0000 | M | 243 | 0.0083 | -0.0000 | 0.0000 | 0.0000 | 0.0311 |  |  |
| new | actual | 11-16 | linear | 0.0000 | tau | 243 | 0.0277 | 0.0006 | 0.0240 | 0.0414 | 0.0541 | 0.0000 | 0.5000 |
| new | actual | 11-16 | linear | 0.5000 | tau | 243 | 0.0256 | 0.0006 | 0.0215 | 0.0385 | 0.0507 | 0.0041 | 0.5000 |
| new | actual | 11-16 | linear | 0.8000 | tau | 243 | 0.0244 | 0.0005 | 0.0192 | 0.0374 | 0.0484 | 0.0041 | 0.5000 |
| new | actual | 11-16 | concave | 0.0000 | tau | 243 | 0.0212 | 0.0003 | 0.0171 | 0.0302 | 0.0423 | 0.0000 | 0.6599 |
| new | actual | 11-16 | concave | 0.5000 | tau | 243 | 0.0185 | 0.0003 | 0.0154 | 0.0284 | 0.0377 | 0.0000 | 0.6599 |
| new | actual | 11-16 | concave | 0.8000 | tau | 243 | 0.0168 | 0.0003 | 0.0136 | 0.0261 | 0.0330 | 0.0041 | 0.6599 |
| new | actual | 11-16 | convex | 0.0000 | tau | 243 | 0.0314 | 0.0006 | 0.0277 | 0.0455 | 0.0639 | 0.0000 | 0.3391 |
| new | actual | 11-16 | convex | 0.5000 | tau | 243 | 0.0300 | 0.0005 | 0.0256 | 0.0435 | 0.0585 | 0.0000 | 0.3391 |
| new | actual | 11-16 | convex | 0.8000 | tau | 243 | 0.0291 | 0.0005 | 0.0231 | 0.0433 | 0.0572 | 0.0000 | 0.3391 |
| new | actual | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0168 | 0.0001 | 0.0146 | 0.0244 | 0.0337 | 0.0000 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0164 | 0.0001 | 0.0134 | 0.0240 | 0.0321 | 0.0000 | 0.1000 |
| new | actual | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0161 | 0.0001 | 0.0131 | 0.0234 | 0.0321 | 0.0000 | 0.1000 |
| new | actual | 17-30 | - | 0.0000 | M | 586 | 0.0080 | -0.0000 | 0.0000 | 0.0000 | 0.0251 |  |  |
| new | actual | 17-30 | linear | 0.0000 | tau | 586 | 0.0212 | 0.0000 | 0.0150 | 0.0362 | 0.0511 | 0.0000 | 0.5000 |
| new | actual | 17-30 | linear | 0.5000 | tau | 586 | 0.0192 | 0.0000 | 0.0143 | 0.0344 | 0.0472 | 0.0000 | 0.5000 |
| new | actual | 17-30 | linear | 0.8000 | tau | 586 | 0.0180 | 0.0000 | 0.0119 | 0.0330 | 0.0453 | 0.0000 | 0.5000 |
| new | actual | 17-30 | concave | 0.0000 | tau | 586 | 0.0228 | 0.0000 | 0.0212 | 0.0364 | 0.0502 | 0.0000 | 0.6599 |
| new | actual | 17-30 | concave | 0.5000 | tau | 586 | 0.0201 | 0.0000 | 0.0194 | 0.0358 | 0.0450 | 0.0017 | 0.6599 |
| new | actual | 17-30 | concave | 0.8000 | tau | 586 | 0.0185 | 0.0000 | 0.0156 | 0.0344 | 0.0414 | 0.0017 | 0.6599 |
| new | actual | 17-30 | convex | 0.0000 | tau | 586 | 0.0151 | 0.0000 | 0.0050 | 0.0237 | 0.0450 | 0.0000 | 0.3391 |
| new | actual | 17-30 | convex | 0.5000 | tau | 586 | 0.0137 | 0.0000 | 0.0046 | 0.0220 | 0.0394 | 0.0000 | 0.3391 |
| new | actual | 17-30 | convex | 0.8000 | tau | 586 | 0.0129 | 0.0000 | 0.0045 | 0.0213 | 0.0363 | 0.0051 | 0.3391 |
| new | actual | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0037 | 0.0000 | 0.0000 | 0.0027 | 0.0138 | 0.0000 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0033 | 0.0000 | 0.0000 | 0.0027 | 0.0119 | 0.1143 | 0.1000 |
| new | actual | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0031 | 0.0000 | 0.0000 | 0.0025 | 0.0111 | 0.1143 | 0.1000 |
| new | own | all | - | 0.0000 | M | 1252 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | all | linear | 0.0000 | tau | 1252 | 0.0237 | 0.0004 | 0.0171 | 0.0399 | 0.0551 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.5000 | tau | 1252 | 0.0237 | 0.0004 | 0.0171 | 0.0399 | 0.0551 | 0.0000 | 0.5000 |
| new | own | all | linear | 0.8000 | tau | 1252 | 0.0237 | 0.0004 | 0.0171 | 0.0399 | 0.0551 | 0.0000 | 0.5000 |
| new | own | all | concave | 0.0000 | tau | 1252 | 0.0210 | 0.0003 | 0.0209 | 0.0352 | 0.0452 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.5000 | tau | 1252 | 0.0210 | 0.0003 | 0.0209 | 0.0352 | 0.0452 | 0.0000 | 0.6599 |
| new | own | all | concave | 0.8000 | tau | 1252 | 0.0210 | 0.0003 | 0.0209 | 0.0352 | 0.0452 | 0.0000 | 0.6599 |
| new | own | all | convex | 0.0000 | tau | 1252 | 0.0212 | 0.0002 | 0.0103 | 0.0350 | 0.0581 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.5000 | tau | 1252 | 0.0212 | 0.0002 | 0.0103 | 0.0350 | 0.0581 | 0.0000 | 0.3391 |
| new | own | all | convex | 0.8000 | tau | 1252 | 0.0212 | 0.0002 | 0.0103 | 0.0350 | 0.0581 | 0.0000 | 0.3391 |
| new | own | all | top3_stress | 0.0000 | tau | 1252 | 0.0074 | 0.0000 | 0.0007 | 0.0124 | 0.0250 | 0.0000 | 0.1000 |
| new | own | all | top3_stress | 0.5000 | tau | 1252 | 0.0074 | 0.0000 | 0.0007 | 0.0124 | 0.0250 | 0.0998 | 0.1000 |
| new | own | all | top3_stress | 0.8000 | tau | 1252 | 0.0074 | 0.0000 | 0.0007 | 0.0124 | 0.0250 | 0.0990 | 0.1000 |
| new | own | 1-3 | - | 0.0000 | M | 128 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 1-3 | linear | 0.0000 | tau | 128 | -0.0016 | -0.0026 | -0.0008 | -0.0000 | 0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.5000 | tau | 128 | -0.0016 | -0.0026 | -0.0008 | -0.0000 | 0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | linear | 0.8000 | tau | 128 | -0.0016 | -0.0026 | -0.0008 | -0.0000 | 0.0000 | 0.0000 | 0.5000 |
| new | own | 1-3 | concave | 0.0000 | tau | 128 | -0.0008 | -0.0013 | -0.0004 | -0.0000 | 0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.5000 | tau | 128 | -0.0008 | -0.0013 | -0.0004 | -0.0000 | 0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | concave | 0.8000 | tau | 128 | -0.0008 | -0.0013 | -0.0004 | -0.0000 | 0.0000 | 0.0000 | 0.6599 |
| new | own | 1-3 | convex | 0.0000 | tau | 128 | -0.0030 | -0.0050 | -0.0015 | -0.0001 | 0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.5000 | tau | 128 | -0.0030 | -0.0050 | -0.0015 | -0.0001 | 0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | convex | 0.8000 | tau | 128 | -0.0030 | -0.0050 | -0.0015 | -0.0001 | 0.0000 | 0.0000 | 0.3391 |
| new | own | 1-3 | top3_stress | 0.0000 | tau | 128 | -0.0053 | -0.0089 | -0.0028 | -0.0001 | 0.0000 | 0.0000 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.5000 | tau | 128 | -0.0053 | -0.0089 | -0.0028 | -0.0001 | 0.0000 | 0.0703 | 0.1000 |
| new | own | 1-3 | top3_stress | 0.8000 | tau | 128 | -0.0053 | -0.0089 | -0.0028 | -0.0001 | 0.0000 | 0.0703 | 0.1000 |
| new | own | 4-10 | - | 0.0000 | M | 295 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 4-10 | linear | 0.0000 | tau | 295 | 0.0039 | 0.0000 | 0.0004 | 0.0063 | 0.0132 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.5000 | tau | 295 | 0.0039 | 0.0000 | 0.0004 | 0.0063 | 0.0132 | 0.0000 | 0.5000 |
| new | own | 4-10 | linear | 0.8000 | tau | 295 | 0.0039 | 0.0000 | 0.0004 | 0.0063 | 0.0132 | 0.0000 | 0.5000 |
| new | own | 4-10 | concave | 0.0000 | tau | 295 | 0.0025 | 0.0000 | 0.0002 | 0.0038 | 0.0079 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.5000 | tau | 295 | 0.0025 | 0.0000 | 0.0002 | 0.0038 | 0.0079 | 0.0000 | 0.6599 |
| new | own | 4-10 | concave | 0.8000 | tau | 295 | 0.0025 | 0.0000 | 0.0002 | 0.0038 | 0.0079 | 0.0000 | 0.6599 |
| new | own | 4-10 | convex | 0.0000 | tau | 295 | 0.0050 | -0.0000 | 0.0005 | 0.0089 | 0.0187 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.5000 | tau | 295 | 0.0050 | -0.0000 | 0.0005 | 0.0089 | 0.0187 | 0.0000 | 0.3391 |
| new | own | 4-10 | convex | 0.8000 | tau | 295 | 0.0050 | -0.0000 | 0.0005 | 0.0089 | 0.0187 | 0.0000 | 0.3391 |
| new | own | 4-10 | top3_stress | 0.0000 | tau | 295 | 0.0029 | -0.0000 | 0.0001 | 0.0080 | 0.0148 | 0.0000 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.5000 | tau | 295 | 0.0029 | -0.0000 | 0.0001 | 0.0080 | 0.0148 | 0.0475 | 0.1000 |
| new | own | 4-10 | top3_stress | 0.8000 | tau | 295 | 0.0029 | -0.0000 | 0.0001 | 0.0080 | 0.0148 | 0.0475 | 0.1000 |
| new | own | 11-16 | - | 0.0000 | M | 243 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 11-16 | linear | 0.0000 | tau | 243 | 0.0352 | 0.0146 | 0.0342 | 0.0478 | 0.0657 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.5000 | tau | 243 | 0.0352 | 0.0146 | 0.0342 | 0.0478 | 0.0657 | 0.0000 | 0.5000 |
| new | own | 11-16 | linear | 0.8000 | tau | 243 | 0.0352 | 0.0146 | 0.0342 | 0.0478 | 0.0657 | 0.0000 | 0.5000 |
| new | own | 11-16 | concave | 0.0000 | tau | 243 | 0.0231 | 0.0092 | 0.0221 | 0.0322 | 0.0442 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.5000 | tau | 243 | 0.0231 | 0.0092 | 0.0221 | 0.0322 | 0.0442 | 0.0000 | 0.6599 |
| new | own | 11-16 | concave | 0.8000 | tau | 243 | 0.0231 | 0.0092 | 0.0221 | 0.0322 | 0.0442 | 0.0000 | 0.6599 |
| new | own | 11-16 | convex | 0.0000 | tau | 243 | 0.0431 | 0.0186 | 0.0400 | 0.0571 | 0.0815 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.5000 | tau | 243 | 0.0431 | 0.0186 | 0.0400 | 0.0571 | 0.0815 | 0.0000 | 0.3391 |
| new | own | 11-16 | convex | 0.8000 | tau | 243 | 0.0431 | 0.0186 | 0.0400 | 0.0571 | 0.0815 | 0.0000 | 0.3391 |
| new | own | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0227 | 0.0113 | 0.0197 | 0.0293 | 0.0456 | 0.0000 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0227 | 0.0113 | 0.0197 | 0.0293 | 0.0456 | 0.0082 | 0.1000 |
| new | own | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0227 | 0.0113 | 0.0197 | 0.0293 | 0.0456 | 0.0082 | 0.1000 |
| new | own | 17-30 | - | 0.0000 | M | 586 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| new | own | 17-30 | linear | 0.0000 | tau | 586 | 0.0344 | 0.0168 | 0.0319 | 0.0460 | 0.0632 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.5000 | tau | 586 | 0.0344 | 0.0168 | 0.0319 | 0.0460 | 0.0632 | 0.0000 | 0.5000 |
| new | own | 17-30 | linear | 0.8000 | tau | 586 | 0.0344 | 0.0168 | 0.0319 | 0.0460 | 0.0632 | 0.0000 | 0.5000 |
| new | own | 17-30 | concave | 0.0000 | tau | 586 | 0.0343 | 0.0255 | 0.0338 | 0.0414 | 0.0524 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.5000 | tau | 586 | 0.0343 | 0.0255 | 0.0338 | 0.0414 | 0.0524 | 0.0000 | 0.6599 |
| new | own | 17-30 | concave | 0.8000 | tau | 586 | 0.0343 | 0.0255 | 0.0338 | 0.0414 | 0.0524 | 0.0000 | 0.6599 |
| new | own | 17-30 | convex | 0.0000 | tau | 586 | 0.0255 | 0.0048 | 0.0163 | 0.0386 | 0.0607 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.5000 | tau | 586 | 0.0255 | 0.0048 | 0.0163 | 0.0386 | 0.0607 | 0.0000 | 0.3391 |
| new | own | 17-30 | convex | 0.8000 | tau | 586 | 0.0255 | 0.0048 | 0.0163 | 0.0386 | 0.0607 | 0.0000 | 0.3391 |
| new | own | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0060 | 0.0000 | 0.0003 | 0.0074 | 0.0208 | 0.0000 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0060 | 0.0000 | 0.0003 | 0.0074 | 0.0208 | 0.1706 | 0.1000 |
| new | own | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0060 | 0.0000 | 0.0003 | 0.0074 | 0.0208 | 0.1689 | 0.1000 |
| delta | actual | all | - | 0.0000 | M | 1252 | 0.0001 | -0.0000 | 0.0000 | 0.0000 | 0.0057 |  |  |
| delta | actual | all | linear | 0.0000 | tau | 1252 | -0.0016 | -0.0071 | 0.0000 | 0.0013 | 0.0112 | 0.0000 | 0.5000 |
| delta | actual | all | linear | 0.5000 | tau | 1252 | -0.0016 | -0.0071 | 0.0000 | 0.0011 | 0.0102 | 0.0088 | 0.5000 |
| delta | actual | all | linear | 0.8000 | tau | 1252 | -0.0016 | -0.0071 | 0.0000 | 0.0010 | 0.0095 | 0.0120 | 0.5000 |
| delta | actual | all | concave | 0.0000 | tau | 1252 | -0.0008 | -0.0045 | 0.0000 | 0.0013 | 0.0082 | 0.0000 | 0.6599 |
| delta | actual | all | concave | 0.5000 | tau | 1252 | -0.0009 | -0.0041 | 0.0000 | 0.0008 | 0.0069 | 0.0248 | 0.6599 |
| delta | actual | all | concave | 0.8000 | tau | 1252 | -0.0009 | -0.0041 | 0.0000 | 0.0007 | 0.0064 | 0.0399 | 0.6599 |
| delta | actual | all | convex | 0.0000 | tau | 1252 | -0.0024 | -0.0107 | 0.0000 | 0.0016 | 0.0138 | 0.0000 | 0.3391 |
| delta | actual | all | convex | 0.5000 | tau | 1252 | -0.0024 | -0.0108 | 0.0000 | 0.0014 | 0.0131 | 0.0032 | 0.3391 |
| delta | actual | all | convex | 0.8000 | tau | 1252 | -0.0024 | -0.0104 | 0.0000 | 0.0013 | 0.0129 | 0.0072 | 0.3391 |
| delta | actual | all | top3_stress | 0.0000 | tau | 1252 | -0.0019 | -0.0069 | 0.0000 | 0.0012 | 0.0122 | 0.0000 | 0.1000 |
| delta | actual | all | top3_stress | 0.5000 | tau | 1252 | -0.0019 | -0.0066 | 0.0000 | 0.0013 | 0.0113 | 0.0431 | 0.1000 |
| delta | actual | all | top3_stress | 0.8000 | tau | 1252 | -0.0019 | -0.0066 | 0.0000 | 0.0014 | 0.0116 | 0.0439 | 0.1000 |
| delta | actual | 1-3 | - | 0.0000 | M | 128 | -0.0003 | -0.0000 | -0.0000 | 0.0000 | 0.0033 |  |  |
| delta | actual | 1-3 | linear | 0.0000 | tau | 128 | -0.0057 | -0.0080 | -0.0026 | -0.0014 | -0.0006 | 0.0000 | 0.5000 |
| delta | actual | 1-3 | linear | 0.5000 | tau | 128 | -0.0056 | -0.0080 | -0.0028 | -0.0017 | -0.0008 | 0.0234 | 0.5000 |
| delta | actual | 1-3 | linear | 0.8000 | tau | 128 | -0.0055 | -0.0081 | -0.0031 | -0.0017 | -0.0009 | 0.0312 | 0.5000 |
| delta | actual | 1-3 | concave | 0.0000 | tau | 128 | -0.0033 | -0.0048 | -0.0015 | -0.0005 | 0.0015 | 0.0000 | 0.6599 |
| delta | actual | 1-3 | concave | 0.5000 | tau | 128 | -0.0032 | -0.0045 | -0.0015 | -0.0006 | -0.0001 | 0.1016 | 0.6599 |
| delta | actual | 1-3 | concave | 0.8000 | tau | 128 | -0.0031 | -0.0042 | -0.0015 | -0.0009 | -0.0005 | 0.1406 | 0.6599 |
| delta | actual | 1-3 | convex | 0.0000 | tau | 128 | -0.0092 | -0.0140 | -0.0051 | -0.0029 | -0.0015 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | convex | 0.5000 | tau | 128 | -0.0091 | -0.0138 | -0.0052 | -0.0031 | -0.0015 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | convex | 0.8000 | tau | 128 | -0.0091 | -0.0130 | -0.0052 | -0.0031 | -0.0015 | 0.0000 | 0.3391 |
| delta | actual | 1-3 | top3_stress | 0.0000 | tau | 128 | -0.0098 | -0.0150 | -0.0042 | -0.0005 | -0.0000 | 0.0000 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.5000 | tau | 128 | -0.0098 | -0.0153 | -0.0045 | -0.0005 | -0.0000 | 0.0078 | 0.1000 |
| delta | actual | 1-3 | top3_stress | 0.8000 | tau | 128 | -0.0098 | -0.0155 | -0.0045 | -0.0005 | -0.0000 | 0.0078 | 0.1000 |
| delta | actual | 4-10 | - | 0.0000 | M | 295 | -0.0036 | -0.0005 | 0.0000 | 0.0000 | 0.0030 |  |  |
| delta | actual | 4-10 | linear | 0.0000 | tau | 295 | -0.0133 | -0.0208 | -0.0116 | -0.0053 | 0.0000 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | linear | 0.5000 | tau | 295 | -0.0124 | -0.0184 | -0.0114 | -0.0062 | 0.0000 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | linear | 0.8000 | tau | 295 | -0.0118 | -0.0178 | -0.0107 | -0.0064 | 0.0000 | 0.0000 | 0.5000 |
| delta | actual | 4-10 | concave | 0.0000 | tau | 295 | -0.0092 | -0.0135 | -0.0068 | -0.0025 | 0.0000 | 0.0000 | 0.6599 |
| delta | actual | 4-10 | concave | 0.5000 | tau | 295 | -0.0080 | -0.0127 | -0.0067 | -0.0028 | 0.0000 | 0.0475 | 0.6599 |
| delta | actual | 4-10 | concave | 0.8000 | tau | 295 | -0.0073 | -0.0114 | -0.0065 | -0.0032 | 0.0000 | 0.0576 | 0.6599 |
| delta | actual | 4-10 | convex | 0.0000 | tau | 295 | -0.0184 | -0.0271 | -0.0176 | -0.0102 | 0.0000 | 0.0000 | 0.3391 |
| delta | actual | 4-10 | convex | 0.5000 | tau | 295 | -0.0178 | -0.0264 | -0.0171 | -0.0105 | 0.0000 | 0.0102 | 0.3391 |
| delta | actual | 4-10 | convex | 0.8000 | tau | 295 | -0.0174 | -0.0260 | -0.0159 | -0.0102 | -0.0000 | 0.0169 | 0.3391 |
| delta | actual | 4-10 | top3_stress | 0.0000 | tau | 295 | -0.0160 | -0.0224 | -0.0152 | -0.0090 | 0.0000 | 0.0000 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.5000 | tau | 295 | -0.0158 | -0.0223 | -0.0148 | -0.0086 | 0.0000 | 0.0034 | 0.1000 |
| delta | actual | 4-10 | top3_stress | 0.8000 | tau | 295 | -0.0157 | -0.0220 | -0.0148 | -0.0083 | 0.0000 | 0.0068 | 0.1000 |
| delta | actual | 11-16 | - | 0.0000 | M | 243 | -0.0021 | -0.0000 | 0.0000 | 0.0000 | 0.0010 |  |  |
| delta | actual | 11-16 | linear | 0.0000 | tau | 243 | -0.0007 | -0.0098 | 0.0000 | 0.0069 | 0.0195 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | linear | 0.5000 | tau | 243 | -0.0002 | -0.0090 | 0.0000 | 0.0067 | 0.0172 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | linear | 0.8000 | tau | 243 | 0.0001 | -0.0082 | 0.0000 | 0.0063 | 0.0141 | 0.0000 | 0.5000 |
| delta | actual | 11-16 | concave | 0.0000 | tau | 243 | -0.0016 | -0.0066 | 0.0000 | 0.0038 | 0.0123 | 0.0000 | 0.6599 |
| delta | actual | 11-16 | concave | 0.5000 | tau | 243 | -0.0010 | -0.0066 | 0.0000 | 0.0038 | 0.0113 | 0.0082 | 0.6599 |
| delta | actual | 11-16 | concave | 0.8000 | tau | 243 | -0.0006 | -0.0062 | 0.0000 | 0.0037 | 0.0104 | 0.0082 | 0.6599 |
| delta | actual | 11-16 | convex | 0.0000 | tau | 243 | 0.0015 | -0.0095 | 0.0000 | 0.0107 | 0.0231 | 0.0000 | 0.3391 |
| delta | actual | 11-16 | convex | 0.5000 | tau | 243 | 0.0019 | -0.0086 | 0.0000 | 0.0106 | 0.0198 | 0.0041 | 0.3391 |
| delta | actual | 11-16 | convex | 0.8000 | tau | 243 | 0.0021 | -0.0084 | 0.0000 | 0.0104 | 0.0198 | 0.0165 | 0.3391 |
| delta | actual | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0075 | 0.0000 | 0.0038 | 0.0136 | 0.0213 | 0.0000 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0076 | 0.0000 | 0.0046 | 0.0136 | 0.0213 | 0.0288 | 0.1000 |
| delta | actual | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0077 | 0.0000 | 0.0048 | 0.0137 | 0.0208 | 0.0288 | 0.1000 |
| delta | actual | 17-30 | - | 0.0000 | M | 586 | 0.0030 | 0.0000 | 0.0000 | 0.0000 | 0.0098 |  |  |
| delta | actual | 17-30 | linear | 0.0000 | tau | 586 | 0.0049 | 0.0000 | 0.0000 | 0.0043 | 0.0168 | 0.0000 | 0.5000 |
| delta | actual | 17-30 | linear | 0.5000 | tau | 586 | 0.0042 | 0.0000 | 0.0000 | 0.0041 | 0.0140 | 0.0137 | 0.5000 |
| delta | actual | 17-30 | linear | 0.8000 | tau | 586 | 0.0037 | 0.0000 | 0.0000 | 0.0041 | 0.0125 | 0.0188 | 0.5000 |
| delta | actual | 17-30 | concave | 0.0000 | tau | 586 | 0.0042 | 0.0000 | 0.0000 | 0.0029 | 0.0142 | 0.0000 | 0.6599 |
| delta | actual | 17-30 | concave | 0.5000 | tau | 586 | 0.0032 | 0.0000 | 0.0000 | 0.0027 | 0.0109 | 0.0034 | 0.6599 |
| delta | actual | 17-30 | concave | 0.8000 | tau | 586 | 0.0026 | 0.0000 | 0.0000 | 0.0024 | 0.0092 | 0.0222 | 0.6599 |
| delta | actual | 17-30 | convex | 0.0000 | tau | 586 | 0.0055 | 0.0000 | 0.0000 | 0.0059 | 0.0188 | 0.0000 | 0.3391 |
| delta | actual | 17-30 | convex | 0.5000 | tau | 586 | 0.0050 | 0.0000 | 0.0000 | 0.0054 | 0.0170 | 0.0000 | 0.3391 |
| delta | actual | 17-30 | convex | 0.8000 | tau | 586 | 0.0047 | 0.0000 | 0.0000 | 0.0054 | 0.0162 | 0.0000 | 0.3391 |
| delta | actual | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0031 | 0.0000 | 0.0000 | 0.0025 | 0.0118 | 0.0000 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0030 | 0.0000 | 0.0000 | 0.0025 | 0.0108 | 0.0768 | 0.1000 |
| delta | actual | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0029 | 0.0000 | 0.0000 | 0.0025 | 0.0108 | 0.0768 | 0.1000 |
| delta | own | all | - | 0.0000 | M | 1252 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | all | linear | 0.0000 | tau | 1252 | -0.0005 | -0.0077 | 0.0000 | 0.0041 | 0.0139 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.5000 | tau | 1252 | -0.0005 | -0.0077 | 0.0000 | 0.0041 | 0.0139 | 0.0000 | 0.5000 |
| delta | own | all | linear | 0.8000 | tau | 1252 | -0.0005 | -0.0077 | 0.0000 | 0.0041 | 0.0139 | 0.0000 | 0.5000 |
| delta | own | all | concave | 0.0000 | tau | 1252 | -0.0003 | -0.0045 | 0.0000 | 0.0022 | 0.0084 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.5000 | tau | 1252 | -0.0003 | -0.0045 | 0.0000 | 0.0022 | 0.0084 | 0.0000 | 0.6599 |
| delta | own | all | concave | 0.8000 | tau | 1252 | -0.0003 | -0.0045 | 0.0000 | 0.0022 | 0.0084 | 0.0000 | 0.6599 |
| delta | own | all | convex | 0.0000 | tau | 1252 | -0.0008 | -0.0118 | 0.0000 | 0.0067 | 0.0202 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.5000 | tau | 1252 | -0.0008 | -0.0118 | 0.0000 | 0.0067 | 0.0202 | 0.0000 | 0.3391 |
| delta | own | all | convex | 0.8000 | tau | 1252 | -0.0008 | -0.0118 | 0.0000 | 0.0067 | 0.0202 | 0.0000 | 0.3391 |
| delta | own | all | top3_stress | 0.0000 | tau | 1252 | -0.0004 | -0.0083 | 0.0000 | 0.0055 | 0.0174 | 0.0000 | 0.1000 |
| delta | own | all | top3_stress | 0.5000 | tau | 1252 | -0.0004 | -0.0083 | 0.0000 | 0.0055 | 0.0174 | 0.0224 | 0.1000 |
| delta | own | all | top3_stress | 0.8000 | tau | 1252 | -0.0004 | -0.0083 | 0.0000 | 0.0055 | 0.0174 | 0.0224 | 0.1000 |
| delta | own | 1-3 | - | 0.0000 | M | 128 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 1-3 | linear | 0.0000 | tau | 128 | -0.0049 | -0.0061 | -0.0034 | -0.0020 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.5000 | tau | 128 | -0.0049 | -0.0061 | -0.0034 | -0.0020 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | linear | 0.8000 | tau | 128 | -0.0049 | -0.0061 | -0.0034 | -0.0020 | -0.0014 | 0.0000 | 0.5000 |
| delta | own | 1-3 | concave | 0.0000 | tau | 128 | -0.0026 | -0.0032 | -0.0018 | -0.0011 | -0.0008 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.5000 | tau | 128 | -0.0026 | -0.0032 | -0.0018 | -0.0011 | -0.0008 | 0.0000 | 0.6599 |
| delta | own | 1-3 | concave | 0.8000 | tau | 128 | -0.0026 | -0.0032 | -0.0018 | -0.0011 | -0.0008 | 0.0000 | 0.6599 |
| delta | own | 1-3 | convex | 0.0000 | tau | 128 | -0.0085 | -0.0108 | -0.0058 | -0.0035 | -0.0025 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.5000 | tau | 128 | -0.0085 | -0.0108 | -0.0058 | -0.0035 | -0.0025 | 0.0000 | 0.3391 |
| delta | own | 1-3 | convex | 0.8000 | tau | 128 | -0.0085 | -0.0108 | -0.0058 | -0.0035 | -0.0025 | 0.0000 | 0.3391 |
| delta | own | 1-3 | top3_stress | 0.0000 | tau | 128 | -0.0097 | -0.0149 | -0.0042 | -0.0005 | -0.0000 | 0.0000 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.5000 | tau | 128 | -0.0097 | -0.0149 | -0.0042 | -0.0005 | -0.0000 | 0.0000 | 0.1000 |
| delta | own | 1-3 | top3_stress | 0.8000 | tau | 128 | -0.0097 | -0.0149 | -0.0042 | -0.0005 | -0.0000 | 0.0000 | 0.1000 |
| delta | own | 4-10 | - | 0.0000 | M | 295 | 0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 4-10 | linear | 0.0000 | tau | 295 | -0.0125 | -0.0175 | -0.0109 | -0.0075 | -0.0045 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.5000 | tau | 295 | -0.0125 | -0.0175 | -0.0109 | -0.0075 | -0.0045 | 0.0000 | 0.5000 |
| delta | own | 4-10 | linear | 0.8000 | tau | 295 | -0.0125 | -0.0175 | -0.0109 | -0.0075 | -0.0045 | 0.0000 | 0.5000 |
| delta | own | 4-10 | concave | 0.0000 | tau | 295 | -0.0072 | -0.0102 | -0.0061 | -0.0042 | -0.0025 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.5000 | tau | 295 | -0.0072 | -0.0102 | -0.0061 | -0.0042 | -0.0025 | 0.0000 | 0.6599 |
| delta | own | 4-10 | concave | 0.8000 | tau | 295 | -0.0072 | -0.0102 | -0.0061 | -0.0042 | -0.0025 | 0.0000 | 0.6599 |
| delta | own | 4-10 | convex | 0.0000 | tau | 295 | -0.0192 | -0.0266 | -0.0176 | -0.0120 | -0.0075 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.5000 | tau | 295 | -0.0192 | -0.0266 | -0.0176 | -0.0120 | -0.0075 | 0.0000 | 0.3391 |
| delta | own | 4-10 | convex | 0.8000 | tau | 295 | -0.0192 | -0.0266 | -0.0176 | -0.0120 | -0.0075 | 0.0000 | 0.3391 |
| delta | own | 4-10 | top3_stress | 0.0000 | tau | 295 | -0.0169 | -0.0223 | -0.0166 | -0.0104 | -0.0049 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.5000 | tau | 295 | -0.0169 | -0.0223 | -0.0166 | -0.0104 | -0.0049 | 0.0000 | 0.1000 |
| delta | own | 4-10 | top3_stress | 0.8000 | tau | 295 | -0.0169 | -0.0223 | -0.0166 | -0.0104 | -0.0049 | 0.0000 | 0.1000 |
| delta | own | 11-16 | - | 0.0000 | M | 243 | -0.0000 | -0.0000 | -0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 11-16 | linear | 0.0000 | tau | 243 | 0.0018 | -0.0097 | 0.0030 | 0.0097 | 0.0191 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.5000 | tau | 243 | 0.0018 | -0.0097 | 0.0030 | 0.0097 | 0.0191 | 0.0000 | 0.5000 |
| delta | own | 11-16 | linear | 0.8000 | tau | 243 | 0.0018 | -0.0097 | 0.0030 | 0.0097 | 0.0191 | 0.0000 | 0.5000 |
| delta | own | 11-16 | concave | 0.0000 | tau | 243 | 0.0006 | -0.0065 | 0.0013 | 0.0054 | 0.0110 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.5000 | tau | 243 | 0.0006 | -0.0065 | 0.0013 | 0.0054 | 0.0110 | 0.0000 | 0.6599 |
| delta | own | 11-16 | concave | 0.8000 | tau | 243 | 0.0006 | -0.0065 | 0.0013 | 0.0054 | 0.0110 | 0.0000 | 0.6599 |
| delta | own | 11-16 | convex | 0.0000 | tau | 243 | 0.0049 | -0.0110 | 0.0059 | 0.0166 | 0.0291 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.5000 | tau | 243 | 0.0049 | -0.0110 | 0.0059 | 0.0166 | 0.0291 | 0.0000 | 0.3391 |
| delta | own | 11-16 | convex | 0.8000 | tau | 243 | 0.0049 | -0.0110 | 0.0059 | 0.0166 | 0.0291 | 0.0000 | 0.3391 |
| delta | own | 11-16 | top3_stress | 0.0000 | tau | 243 | 0.0112 | 0.0001 | 0.0097 | 0.0183 | 0.0279 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.5000 | tau | 243 | 0.0112 | 0.0001 | 0.0097 | 0.0183 | 0.0279 | 0.0000 | 0.1000 |
| delta | own | 11-16 | top3_stress | 0.8000 | tau | 243 | 0.0112 | 0.0001 | 0.0097 | 0.0183 | 0.0279 | 0.0000 | 0.1000 |
| delta | own | 17-30 | - | 0.0000 | M | 586 | -0.0000 | -0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |
| delta | own | 17-30 | linear | 0.0000 | tau | 586 | 0.0054 | 0.0000 | 0.0002 | 0.0084 | 0.0176 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.5000 | tau | 586 | 0.0054 | 0.0000 | 0.0002 | 0.0084 | 0.0176 | 0.0000 | 0.5000 |
| delta | own | 17-30 | linear | 0.8000 | tau | 586 | 0.0054 | 0.0000 | 0.0002 | 0.0084 | 0.0176 | 0.0000 | 0.5000 |
| delta | own | 17-30 | concave | 0.0000 | tau | 586 | 0.0033 | 0.0000 | 0.0001 | 0.0052 | 0.0106 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.5000 | tau | 586 | 0.0033 | 0.0000 | 0.0001 | 0.0052 | 0.0106 | 0.0000 | 0.6599 |
| delta | own | 17-30 | concave | 0.8000 | tau | 586 | 0.0033 | 0.0000 | 0.0001 | 0.0052 | 0.0106 | 0.0000 | 0.6599 |
| delta | own | 17-30 | convex | 0.0000 | tau | 586 | 0.0077 | 0.0000 | 0.0004 | 0.0114 | 0.0251 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.5000 | tau | 586 | 0.0077 | 0.0000 | 0.0004 | 0.0114 | 0.0251 | 0.0000 | 0.3391 |
| delta | own | 17-30 | convex | 0.8000 | tau | 586 | 0.0077 | 0.0000 | 0.0004 | 0.0114 | 0.0251 | 0.0000 | 0.3391 |
| delta | own | 17-30 | top3_stress | 0.0000 | tau | 586 | 0.0051 | 0.0000 | 0.0002 | 0.0066 | 0.0172 | 0.0000 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.5000 | tau | 586 | 0.0051 | 0.0000 | 0.0002 | 0.0066 | 0.0172 | 0.0478 | 0.1000 |
| delta | own | 17-30 | top3_stress | 0.8000 | tau | 586 | 0.0051 | 0.0000 | 0.0002 | 0.0066 | 0.0172 | 0.0478 | 0.1000 |

## T5_attr_seeding

| rule | portfolio | seed_group | value_class | verdict | share | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| old | actual | <0.01 | B | dominance_positive | 0.7131 | 0.5904 | 0.8182 | 366 |
| old | actual | <0.01 | B | reversal | 0.0519 | 0.0133 | 0.0856 | 366 |
| old | actual | <0.01 | B | negligible | 0.1831 | 0.0839 | 0.2962 | 366 |
| old | actual | <0.01 | B | unresolved | 0.0519 | 0.0194 | 0.1031 | 366 |
| old | actual | 0.01-0.05 | B | dominance_positive | 0.7179 | 0.5479 | 0.9189 | 78 |
| old | actual | 0.01-0.05 | B | reversal | 0.0513 | 0.0000 | 0.1482 | 78 |
| old | actual | 0.01-0.05 | B | negligible | 0.2308 | 0.0659 | 0.3774 | 78 |
| old | actual | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 78 |
| old | actual | >=0.05 | B | dominance_positive | 0.7215 | 0.6019 | 0.8212 | 808 |
| old | actual | >=0.05 | B | reversal | 0.0309 | 0.0076 | 0.0663 | 808 |
| old | actual | >=0.05 | B | negligible | 0.2401 | 0.1580 | 0.3378 | 808 |
| old | actual | >=0.05 | B | unresolved | 0.0074 | 0.0000 | 0.0245 | 808 |
| old | own | <0.01 | B | dominance_positive | 0.8989 | 0.7976 | 0.9863 | 366 |
| old | own | <0.01 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 366 |
| old | own | <0.01 | B | negligible | 0.1011 | 0.0137 | 0.2024 | 366 |
| old | own | <0.01 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 366 |
| old | own | 0.01-0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 78 |
| old | own | 0.01-0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 78 |
| old | own | 0.01-0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 78 |
| old | own | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 78 |
| old | own | >=0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 808 |
| old | own | >=0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 808 |
| old | own | >=0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 808 |
| old | own | >=0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 808 |
| new | actual | <0.01 | B | dominance_positive | 0.1339 | 0.0627 | 0.2134 | 366 |
| new | actual | <0.01 | B | reversal | 0.3552 | 0.2071 | 0.4955 | 366 |
| new | actual | <0.01 | B | negligible | 0.4290 | 0.2841 | 0.5884 | 366 |
| new | actual | <0.01 | B | unresolved | 0.0820 | 0.0231 | 0.1607 | 366 |
| new | actual | 0.01-0.05 | B | dominance_positive | 0.5641 | 0.3820 | 0.8000 | 78 |
| new | actual | 0.01-0.05 | B | reversal | 0.0385 | 0.0000 | 0.1455 | 78 |
| new | actual | 0.01-0.05 | B | negligible | 0.3974 | 0.1429 | 0.5926 | 78 |
| new | actual | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 78 |
| new | actual | >=0.05 | B | dominance_positive | 0.7364 | 0.6316 | 0.8127 | 808 |
| new | actual | >=0.05 | B | reversal | 0.0371 | 0.0102 | 0.0650 | 808 |
| new | actual | >=0.05 | B | negligible | 0.2228 | 0.1498 | 0.3152 | 808 |
| new | actual | >=0.05 | B | unresolved | 0.0037 | 0.0000 | 0.0129 | 808 |
| new | own | <0.01 | B | dominance_positive | 0.1639 | 0.0810 | 0.2450 | 366 |
| new | own | <0.01 | B | reversal | 0.3607 | 0.1970 | 0.5438 | 366 |
| new | own | <0.01 | B | negligible | 0.4617 | 0.3184 | 0.6129 | 366 |
| new | own | <0.01 | B | unresolved | 0.0137 | 0.0000 | 0.0421 | 366 |
| new | own | 0.01-0.05 | B | dominance_positive | 0.8077 | 0.5699 | 0.9733 | 78 |
| new | own | 0.01-0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 78 |
| new | own | 0.01-0.05 | B | negligible | 0.1923 | 0.0267 | 0.4301 | 78 |
| new | own | 0.01-0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 78 |
| new | own | >=0.05 | B | dominance_positive | 1.0000 | 1.0000 | 1.0000 | 808 |
| new | own | >=0.05 | B | reversal | 0.0000 | 0.0000 | 0.0000 | 808 |
| new | own | >=0.05 | B | negligible | 0.0000 | 0.0000 | 0.0000 | 808 |
| new | own | >=0.05 | B | unresolved | 0.0000 | 0.0000 | 0.0000 | 808 |

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
| new | holds_conditional_other | True | 529 | 0.1853 | 0.0907 | 0.2644 |
| new | holds_conditional_other | False | 723 | 0.0899 | 0.0363 | 0.1519 |
| new | holds_opponent_pick | True | 43 | 0.4884 | 0.2449 | 0.7778 |
| new | holds_opponent_pick | False | 1209 | 0.1175 | 0.0555 | 0.1598 |
| new | holds_pooled_pick | True | 379 | 0.1398 | 0.0328 | 0.2481 |
| new | holds_pooled_pick | False | 873 | 0.1260 | 0.0639 | 0.1900 |
| new | self_restricted | True | 103 | 0.1650 | 0.0090 | 0.3333 |
| new | self_restricted | False | 1149 | 0.1271 | 0.0575 | 0.1788 |
| new | opp_restricted | True | 103 | 0.1068 | 0.0000 | 0.2404 |
| new | opp_restricted | False | 1149 | 0.1323 | 0.0661 | 0.1781 |
| new | holds_conditional_other_state | True | 500 | 0.1760 | 0.0902 | 0.2400 |
| new | holds_conditional_other_state | False | 752 | 0.0997 | 0.0390 | 0.1619 |
| new | holds_opponent_pick_state | True | 40 | 0.5000 | 0.2542 | 0.7667 |
| new | holds_opponent_pick_state | False | 1212 | 0.1180 | 0.0559 | 0.1611 |

## T5_6_transitions

| portfolio | old | new | count |
|---|---|---|---|
| actual | dominance_positive | dominance_positive | 653 |
| actual | dominance_positive | negligible | 111 |
| actual | dominance_positive | reversal | 118 |
| actual | dominance_positive | unresolved | 18 |
| actual | negligible | dominance_positive | 26 |
| actual | negligible | negligible | 250 |
| actual | negligible | reversal | 2 |
| actual | negligible | unresolved | 1 |
| actual | reversal | dominance_positive | 4 |
| actual | reversal | negligible | 4 |
| actual | reversal | reversal | 39 |
| actual | reversal | unresolved | 1 |
| actual | unresolved | dominance_positive | 5 |
| actual | unresolved | negligible | 3 |
| actual | unresolved | reversal | 4 |
| actual | unresolved | unresolved | 13 |
| own | dominance_positive | dominance_positive | 931 |
| own | dominance_positive | negligible | 147 |
| own | dominance_positive | reversal | 132 |
| own | dominance_positive | unresolved | 5 |
| own | negligible | negligible | 37 |

## T5_headline_reversal_diff

| contrast | portfolio | verdict | share_a | share_b | diff | lo99 | hi99 | n |
|---|---|---|---|---|---|---|---|---|
| new_minus_old | actual | verdict_B | 0.1302 | 0.0383 | 0.0919 | 0.0392 | 0.1332 | 1252 |
| new_minus_old | actual | verdict_B_pm | 0.1070 | 0.0272 | 0.0799 | 0.0376 | 0.1113 | 1252 |
| new_minus_old | own | verdict_B | 0.1054 | 0.0000 | 0.1054 | 0.0510 | 0.1457 | 1252 |
| new_minus_old | own | verdict_B_pm | 0.0974 | 0.0000 | 0.0974 | 0.0471 | 0.1356 | 1252 |
| actual_minus_own | old | verdict_B | 0.0383 | 0.0000 | 0.0383 | 0.0165 | 0.0632 | 1252 |
| actual_minus_own | new | verdict_B | 0.1302 | 0.1054 | 0.0248 | 0.0055 | 0.0472 | 1252 |

## T5_4_typology

| rule | curve | type | share | lo99 | hi99 | n | tp_dominated_share |
|---|---|---|---|---|---|---|---|
| old | linear | both_lose | 0.4665 | 0.3037 | 0.6457 | 292 | 0.2877 |
| old | linear | both_win | 0.0016 | 0.0000 | 0.0097 | 1 | 0.0000 |
| old | linear | normal | 0.3914 | 0.2972 | 0.4650 | 245 | 0.7551 |
| old | linear | opposed | 0.0160 | 0.0015 | 0.0370 | 10 | 0.9000 |
| old | linear | one_sided_win | 0.0144 | 0.0000 | 0.0344 | 9 | 0.7778 |
| old | linear | no_own_stake | 0.1102 | 0.0347 | 0.2083 | 69 | 1.0000 |
| old | concave | both_lose | 0.4201 | 0.2591 | 0.6006 | 263 | 0.3270 |
| old | concave | both_win | 0.0016 | 0.0000 | 0.0097 | 1 | 0.0000 |
| old | concave | normal | 0.4105 | 0.3133 | 0.4969 | 257 | 0.7227 |
| old | concave | opposed | 0.0192 | 0.0048 | 0.0386 | 12 | 0.7500 |
| old | concave | one_sided_win | 0.0144 | 0.0000 | 0.0365 | 9 | 0.7778 |
| old | concave | no_own_stake | 0.1342 | 0.0526 | 0.2414 | 84 | 1.0000 |
| old | convex | both_lose | 0.4696 | 0.3379 | 0.5994 | 294 | 0.2177 |
| old | convex | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan |
| old | convex | normal | 0.4042 | 0.3338 | 0.4686 | 253 | 0.6574 |
| old | convex | opposed | 0.0096 | 0.0000 | 0.0241 | 6 | 0.8333 |
| old | convex | one_sided_win | 0.0128 | 0.0000 | 0.0353 | 8 | 0.6250 |
| old | convex | no_own_stake | 0.1038 | 0.0434 | 0.1872 | 65 | 1.0000 |
| old | top3_stress | both_lose | 0.1885 | 0.1321 | 0.2666 | 118 | 0.0085 |
| old | top3_stress | both_win | 0.0000 | 0.0000 | 0.0000 | 0 | nan |
| old | top3_stress | normal | 0.4585 | 0.3914 | 0.5428 | 287 | 0.1474 |
| old | top3_stress | opposed | 0.0000 | 0.0000 | 0.0000 | 0 | nan |
| old | top3_stress | one_sided_win | 0.0032 | 0.0000 | 0.0132 | 2 | 0.5000 |
| old | top3_stress | no_own_stake | 0.3498 | 0.2632 | 0.4262 | 219 | 0.9750 |
| new | linear | both_lose | 0.2827 | 0.1611 | 0.4045 | 177 | 0.2599 |
| new | linear | both_win | 0.0048 | 0.0000 | 0.0182 | 3 | 0.3333 |
| new | linear | normal | 0.3930 | 0.3234 | 0.4765 | 246 | 0.6138 |
| new | linear | opposed | 0.0799 | 0.0239 | 0.1476 | 50 | 0.4400 |
| new | linear | one_sided_win | 0.0415 | 0.0072 | 0.0908 | 26 | 0.7692 |
| new | linear | no_own_stake | 0.1981 | 0.0953 | 0.3164 | 124 | 1.0000 |
| new | concave | both_lose | 0.2955 | 0.1796 | 0.3960 | 185 | 0.3351 |
| new | concave | both_win | 0.0016 | 0.0000 | 0.0097 | 1 | 0.0000 |
| new | concave | normal | 0.4201 | 0.3483 | 0.4875 | 263 | 0.6412 |
| new | concave | opposed | 0.0431 | 0.0121 | 0.0812 | 27 | 0.4444 |
| new | concave | one_sided_win | 0.0335 | 0.0067 | 0.0747 | 21 | 0.7143 |
| new | concave | no_own_stake | 0.2061 | 0.1018 | 0.3312 | 129 | 1.0000 |
| new | convex | both_lose | 0.2476 | 0.1424 | 0.3650 | 155 | 0.2194 |
| new | convex | both_win | 0.0048 | 0.0000 | 0.0181 | 3 | 0.0000 |
| new | convex | normal | 0.3898 | 0.3162 | 0.4745 | 244 | 0.5205 |
| new | convex | opposed | 0.0815 | 0.0229 | 0.1483 | 51 | 0.2549 |
| new | convex | one_sided_win | 0.0543 | 0.0141 | 0.1009 | 34 | 0.6176 |
| new | convex | no_own_stake | 0.2220 | 0.1281 | 0.3244 | 139 | 1.0000 |
| new | top3_stress | both_lose | 0.1310 | 0.0731 | 0.1950 | 82 | 0.0244 |
| new | top3_stress | both_win | 0.0080 | 0.0000 | 0.0228 | 5 | 0.0000 |
| new | top3_stress | normal | 0.3387 | 0.2657 | 0.4405 | 212 | 0.2488 |
| new | top3_stress | opposed | 0.0671 | 0.0228 | 0.1176 | 42 | 0.0238 |
| new | top3_stress | one_sided_win | 0.1134 | 0.0459 | 0.1750 | 71 | 0.3333 |
| new | top3_stress | no_own_stake | 0.3419 | 0.2617 | 0.4321 | 214 | 1.0000 |

## T5_5_stakes_distribution

| rule | curve | measure | n | mean | q25 | median | q75 | q90 |
|---|---|---|---|---|---|---|---|---|
| old | linear | tp_share | 616 | 0.5662 | 0.4016 | 0.5297 | 0.7561 | 1.0000 |
| old | linear | tp_share_raw | 620 | 0.6184 | 0.4942 | 0.5801 | 0.7816 | 0.9440 |
| old | linear | hhi | 616 | 0.3089 | 0.2135 | 0.2793 | 0.3672 | 0.5000 |
| old | linear | n_material | 626 | 6.5000 | 4.0000 | 7.0000 | 9.0000 | 10.0000 |
| old | linear | mean_abs_third | 626 | 0.0017 | 0.0008 | 0.0015 | 0.0023 | 0.0034 |
| old | linear | mean_abs_third_raw | 626 | 0.0021 | 0.0012 | 0.0019 | 0.0027 | 0.0036 |
| old | concave | tp_share | 611 | 0.5917 | 0.4283 | 0.5566 | 0.8092 | 1.0000 |
| old | concave | tp_share_raw | 619 | 0.6433 | 0.5001 | 0.6061 | 0.8199 | 0.9571 |
| old | concave | hhi | 611 | 0.3144 | 0.2139 | 0.2868 | 0.3742 | 0.5000 |
| old | concave | n_material | 626 | 5.9409 | 4.0000 | 6.0000 | 8.0000 | 10.0000 |
| old | concave | mean_abs_third | 626 | 0.0018 | 0.0008 | 0.0016 | 0.0025 | 0.0035 |
| old | concave | mean_abs_third_raw | 626 | 0.0022 | 0.0012 | 0.0019 | 0.0028 | 0.0038 |
| old | convex | tp_share | 607 | 0.5073 | 0.3558 | 0.4909 | 0.6913 | 0.9273 |
| old | convex | tp_share_raw | 617 | 0.5941 | 0.4870 | 0.5454 | 0.7383 | 0.9232 |
| old | convex | hhi | 607 | 0.3605 | 0.2435 | 0.3205 | 0.4101 | 0.5173 |
| old | convex | n_material | 626 | 5.5128 | 3.0000 | 5.0000 | 8.0000 | 9.0000 |
| old | convex | mean_abs_third | 626 | 0.0013 | 0.0005 | 0.0011 | 0.0018 | 0.0027 |
| old | convex | mean_abs_third_raw | 626 | 0.0016 | 0.0009 | 0.0015 | 0.0022 | 0.0030 |
| old | top3_stress | tp_share | 445 | 0.3744 | 0.1430 | 0.3995 | 0.4766 | 0.8062 |
| old | top3_stress | tp_share_raw | 493 | 0.5314 | 0.4853 | 0.5011 | 0.5237 | 0.8618 |
| old | top3_stress | hhi | 445 | 0.5349 | 0.3570 | 0.4527 | 0.5997 | 1.0000 |
| old | top3_stress | n_material | 626 | 2.2748 | 0.0000 | 2.0000 | 4.0000 | 5.0000 |
| old | top3_stress | mean_abs_third | 626 | 0.0003 | 0.0000 | 0.0002 | 0.0005 | 0.0009 |
| old | top3_stress | mean_abs_third_raw | 626 | 0.0005 | 0.0001 | 0.0004 | 0.0008 | 0.0011 |
| new | linear | tp_share | 581 | 0.5886 | 0.4314 | 0.5242 | 0.7766 | 1.0000 |
| new | linear | tp_share_raw | 598 | 0.6354 | 0.5023 | 0.5822 | 0.7987 | 0.9749 |
| new | linear | hhi | 581 | 0.3177 | 0.2269 | 0.2995 | 0.3749 | 0.5000 |
| new | linear | n_material | 626 | 5.8083 | 3.0000 | 6.0000 | 8.0000 | 10.0000 |
| new | linear | mean_abs_third | 626 | 0.0017 | 0.0006 | 0.0013 | 0.0024 | 0.0036 |
| new | linear | mean_abs_third_raw | 626 | 0.0020 | 0.0009 | 0.0016 | 0.0027 | 0.0040 |
| new | concave | tp_share | 581 | 0.6074 | 0.4570 | 0.5492 | 0.8066 | 1.0000 |
| new | concave | tp_share_raw | 602 | 0.6500 | 0.5065 | 0.6111 | 0.8186 | 0.9775 |
| new | concave | hhi | 581 | 0.3099 | 0.2107 | 0.2916 | 0.3711 | 0.4957 |
| new | concave | n_material | 626 | 5.7796 | 3.2500 | 6.0000 | 8.0000 | 10.0000 |
| new | concave | mean_abs_third | 626 | 0.0018 | 0.0008 | 0.0015 | 0.0025 | 0.0036 |
| new | concave | mean_abs_third_raw | 626 | 0.0020 | 0.0011 | 0.0017 | 0.0028 | 0.0039 |
| new | convex | tp_share | 555 | 0.5384 | 0.3857 | 0.4904 | 0.7134 | 1.0000 |
| new | convex | tp_share_raw | 584 | 0.6160 | 0.5000 | 0.5567 | 0.7597 | 0.9586 |
| new | convex | hhi | 555 | 0.3844 | 0.2585 | 0.3326 | 0.4278 | 0.5910 |
| new | convex | n_material | 626 | 4.6502 | 2.0000 | 5.0000 | 7.0000 | 8.0000 |
| new | convex | mean_abs_third | 626 | 0.0014 | 0.0003 | 0.0009 | 0.0019 | 0.0033 |
| new | convex | mean_abs_third_raw | 626 | 0.0016 | 0.0006 | 0.0012 | 0.0022 | 0.0036 |
| new | top3_stress | tp_share | 463 | 0.4488 | 0.2723 | 0.4395 | 0.5422 | 1.0000 |
| new | top3_stress | tp_share_raw | 503 | 0.5803 | 0.4961 | 0.5054 | 0.6506 | 0.9763 |
| new | top3_stress | hhi | 463 | 0.4905 | 0.3382 | 0.4224 | 0.5200 | 1.0000 |
| new | top3_stress | n_material | 626 | 2.4696 | 0.0000 | 2.0000 | 4.0000 | 5.0000 |
| new | top3_stress | mean_abs_third | 626 | 0.0005 | 0.0000 | 0.0003 | 0.0007 | 0.0013 |
| new | top3_stress | mean_abs_third_raw | 626 | 0.0006 | 0.0001 | 0.0004 | 0.0009 | 0.0014 |
| new_minus_old | linear | tp_share | 581 | 0.0185 | -0.0315 | 0.0021 | 0.0783 | 0.1628 |
| new_minus_old | linear | hhi | 581 | 0.0206 | -0.0313 | 0.0009 | 0.0618 | 0.1480 |
| new_minus_old | linear | mean_abs_third | 626 | -0.0000 | -0.0004 | 0.0000 | 0.0004 | 0.0011 |
| new_minus_old | concave | tp_share | 579 | 0.0111 | -0.0309 | 0.0005 | 0.0662 | 0.1627 |
| new_minus_old | concave | hhi | 579 | 0.0079 | -0.0370 | 0.0000 | 0.0475 | 0.1239 |
| new_minus_old | concave | mean_abs_third | 626 | -0.0001 | -0.0003 | 0.0000 | 0.0004 | 0.0009 |
| new_minus_old | convex | tp_share | 555 | 0.0226 | -0.0462 | 0.0086 | 0.1033 | 0.2298 |
| new_minus_old | convex | hhi | 555 | 0.0357 | -0.0526 | 0.0024 | 0.0884 | 0.2000 |
| new_minus_old | convex | mean_abs_third | 626 | 0.0001 | -0.0005 | 0.0000 | 0.0006 | 0.0014 |
| new_minus_old | top3_stress | tp_share | 376 | 0.1045 | -0.0260 | 0.0659 | 0.3052 | 0.4680 |
| new_minus_old | top3_stress | hhi | 376 | -0.1013 | -0.3094 | -0.0443 | 0.0733 | 0.2523 |
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

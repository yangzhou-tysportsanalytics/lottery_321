"""Recompute every number quoted in Section 3 and write the provenance table (paper Appendix B).

Each row of the table is one number in the section text: its value, the function that produces it, the test
that covers it, and the recomputed value. The script fails loudly if a recomputed value does not match the
number quoted in the section, so the appendix cannot drift from the text.
Usage: python theory_numbers.py [--out PATH]
"""
import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import theory as TH  # noqa: E402
from lottery_rules import GROUP_BALLS, RELEGATED_FLOOR, N_LOTTERY, FLAT_2019_COMBOS  # noqa: E402
from value import CURVES  # noqa: E402

OUT = HERE.parents[1] / 'results/theory_numbers.md'
def _tol(want):
    """Half a unit in the last decimal the section quotes, so a value printed to 2 dp is checked to 2 dp.

    A wrongly rounded figure therefore fails: the convex-curve tau is -0.041475, and a text printing -0.042
    (error 0.000525) would be caught. A tiny epsilon is added
    so that a value exactly on the half-unit boundary, which rounds to the quoted figure, still passes."""
    txt = f'{want!r}'
    dec = len(txt.split('.')[1]) if '.' in txt else 0
    return 0.5 * 10 ** (-dec) + 1e-12


def rows():
    K = TH.position_kernels()
    Fn = np.cumsum(K['new'], axis=1)
    d34 = Fn[2] - Fn[3]
    exp_new = (K['new'] * np.arange(1, K['new'].shape[1] + 1)).sum(axis=1)
    exp_old = (K['old'] * np.arange(1, K['old'].shape[1] + 1)).sum(axis=1)
    # Corollary 2: own unprotected pick moves from position 4 to position 3, C = F3 - F4 over slots 1..30
    C = np.concatenate([d34, np.zeros(30 - len(d34))])
    d = np.diff(np.concatenate([[0.0], C]))
    taus = {name: float(d @ v) for name, v in CURVES.items()}
    out = [
        ('F3(1) - F4(1) at the relegation boundary', '-1/37 = -0.0270',
         float(d34[0]), float(Fraction(-1, 37)),
         'theory.position_kernels + cumsum', 'test_theory.py::kernel tests'),
        # The sign pattern of F3 - F4 quoted in the text (Proposition 1).
        ('F3 - F4, largest value over j <= 11', '-0.027 (negative throughout)',
         float(d34[:11].max()), -0.027, 'theory.position_kernels', 'test_theory.py'),
        ('F3 - F4 at slot 12', '+0.204', float(d34[11]), 0.204,
         'theory.position_kernels', 'test_theory.py'),
        ('F3 - F4, smallest value over j = 12..15', '+0.025 (positive throughout)',
         float(d34[11:15].min()), 0.025, 'theory.position_kernels', 'test_theory.py'),
        ('F3 - F4, slot of the minimum', 'minimum at j = 9', float(d34.argmin() + 1), 9.0,
         'theory.position_kernels', 'test_theory.py'),
        ('F3 - F4, value at the minimum', '-0.150', float(d34.min()), -0.150,
         'theory.position_kernels', 'test_theory.py'),
        ('expected slot, 3-2-1 positions 1-3', '8.093', float(exp_new[:3].mean()), 8.093,
         'theory.position_kernels', 'test_theory.py'),
        ('expected slot, 3-2-1 positions 4-10', '7.448', float(exp_new[3:10].mean()), 7.448,
         'theory.position_kernels', 'test_theory.py'),
        ('expected slot, 3-2-1 positions 11-14', '9.071', float(exp_new[10:14].mean()), 9.071,
         'theory.position_kernels', 'test_theory.py'),
        ('expected slot, 3-2-1 positions 15-16', '11.649', float(exp_new[14:16].mean()), 11.649,
         'theory.position_kernels', 'test_theory.py'),
        ('expected slot, old rule position 1', '3.66', float(exp_old[0]), 3.66,
         'lottery_rules.flattened_2019_fast', 'test_lottery_rules.py::test_matches_official_2019_table'),
        ('expected slot, old rule position 14', '13.73', float(exp_old[13]), 13.73,
         'lottery_rules.flattened_2019_fast', 'test_lottery_rules.py::test_matches_official_2019_table'),
        ('Corollary 2 tau, linear curve', '-0.022', taus['linear'], -0.022,
         'value.CURVES + position_kernels', 'test_theory.py'),
        ('Corollary 2 tau, concave curve', '-0.011', taus['concave'], -0.011,
         'value.CURVES + position_kernels', 'test_theory.py'),
        ('Corollary 2 tau, convex curve', '-0.041', taus['convex'], -0.041,
         'value.CURVES + position_kernels', 'test_theory.py'),
        ('Corollary 2 tau, top-3 curve', '-0.075', taus['top3_stress'], -0.075,
         'value.CURVES + position_kernels', 'test_theory.py'),
        ('3-2-1 total balls', '37', float(3 * GROUP_BALLS['bottom3'] + 7 * GROUP_BALLS['non_playin']
                                          + 4 * GROUP_BALLS['playin_9_10'] + 2 * GROUP_BALLS['playin_7_8_losers']),
         37.0, 'lottery_rules.GROUP_BALLS', 'test_lottery_rules.py'),
        ('relegated floor', '12', float(RELEGATED_FLOOR), 12.0, 'lottery_rules.RELEGATED_FLOOR',
         'test_lottery_rules.py::test_relegated_floor_twelve'),
        ('lottery field size', '16', float(N_LOTTERY), 16.0, 'lottery_rules.N_LOTTERY', 'test_lottery_rules.py'),
        ('old-rule combinations, worst team', '140 per 1000', float(FLAT_2019_COMBOS[0]), 140.0,
         'lottery_rules.FLAT_2019_COMBOS', 'test_lottery_rules.py::test_matches_official_2019_table'),
        ('adjacent-pair FOSD violations under 3-2-1', 'only the 3|4 pair',
         float(len({r for r, _ in TH.rank_monotone(K['new'])})), 1.0,
         'theory.rank_monotone', 'test_theory.py'),
        ('adjacent-pair FOSD violations under the old rule', 'none',
         float(len(TH.rank_monotone(K['old']))), 0.0, 'theory.rank_monotone', 'test_theory.py'),
    ]
    out += example_and_scan_rows()
    out += group_order_rows(K)
    return out


def group_order_rows(K):
    """The statement after Corollary 2 that every
    3-2-1 position in an earlier group has a slot distribution dominating that of every position in a later
    group, so that only a move from positions 4-10 into 1-3 lowers an own pick's value."""
    kn = K['new']
    full = np.zeros((30, 30)); full[:kn.shape[0], :kn.shape[1]] = kn
    for r in range(kn.shape[0], 30):
        full[r, r] = 1.0
    F = np.cumsum(full, axis=1)
    groups = [range(0, 3), range(3, 10), range(10, 14), range(14, 16), range(16, 30)]
    cross = min(float((F[r] - F[s]).min()) for a in range(5) for b in range(a + 1, 5)
                for r in groups[a] for s in groups[b] if not (a == 0 and b == 1))
    rel = min(float((F[r] - F[s]).min()) for r in groups[0] for s in groups[1])
    cross = 0.0 if abs(cross) < 1e-12 else cross
    import c3_rules as C3R
    field = tuple([(2, True, 1)] * 3 + [(3, False, 1)] * 7 + [(2, False, 1)] * 4 + [(1, False, 1)] * 2)
    Knf = np.array(C3R.new_kernel_components(field, floor=False)); Fnf = np.cumsum(Knf, axis=1)
    nofloor = float((Fnf[2] - Fnf[3]).max())
    nofloor = 0.0 if abs(nofloor) < 1e-12 else nofloor
    return [
        ('F3 - F4 without the floor, largest value over all slots (Section 5.5)', '0 (nonpositive)', nofloor, 0.0,
         'c3_rules.new_kernel_components(floor=False)', 'test_theory_numbers.py'),
        ('smallest F_r - F_s over positions r < s in different 3-2-1 groups', '0 (dominance)',
         cross, 0.0, 'theory.position_kernels', 'test_theory_numbers.py'),
        ('smallest F_r - F_s, r in 1-3 and s in 4-10 (within the non-play-in group)', '-0.150', rel, -0.150,
         'theory.position_kernels', 'test_theory_numbers.py'),
    ]


def example_and_scan_rows():
    """Further numbers quoted in Section 3 and Online Appendix D: the mass example of Online Appendix D.7, the minimum-slot example, the random-instance scan and the pool
    count. All exact; the scan is the registered property_scan (200 instances, seed 20260921)."""
    lin = CURVES['linear']
    m_old = float(TH.example_e3(rule='old')['C'][29]); m_new = float(TH.example_e3(rule='new')['C'][29])
    e5 = TH.example_e5(); tau5 = float(e5['d'] @ lin)
    sc = TH.property_scan()
    ov, nv = sc['old_violations'], sc['new_violations']
    pools = 0
    import importlib
    sys.path.insert(0, str(HERE / 'ledgers'))
    for y in range(2021, 2027):
        pools += len(getattr(importlib.import_module(f'router_{y}'), 'POOLS', ()))
    return [
        ('M, opponent top-4-protected pick, opponent crosses 3|4, old rule', '+0.041', m_old, 0.041,
         'theory.example_e3', 'test_theory.py'),
        ('M, same portfolio, 3-2-1', '-0.095', m_new, -0.095, 'theory.example_e3', 'test_theory.py'),
        ('Corollary 2 example with minimum slot 6, linear tau', '+0.010', tau5, 0.010,
         'theory.example_e5', 'test_theory.py'),
        ('random instances', '200', float(sc['n_instances']), 200.0, 'theory.property_scan', 'test_theory.py'),
        ('team-game cases', '1,622', float(sc['n_player_cases']), 1622.0, 'theory.property_scan', 'test_theory.py'),
        ('class-B violations, official old rule', '42', float(len(ov)), 42.0, 'theory.property_scan', 'test_theory.py'),
        ('instances with an old-rule violation', '39', float(len({x['instance'] for x in ov})), 39.0,
         'theory.property_scan', 'test_theory.py'),
        ('smallest C among old-rule violations', '-0.0014', float(min(x['minC'] for x in ov)), -0.0014,
         'theory.property_scan', 'test_theory.py'),
        ('class-B violations, strict-record old rule', '0', float(len(sc['old_strict_violations'])), 0.0,
         'theory.property_scan', 'test_theory.py'),
        ('3-2-1 violations not at the relegation boundary', '0',
         float(sum(1 for x in nv if not x['relegation_boundary'])), 0.0, 'theory.property_scan', 'test_theory.py'),
        ('3-2-1 violations with argmin j other than 9', '0', float(sum(1 for x in nv if x['argmin_j'] != 9)), 0.0,
         'theory.property_scan', 'test_theory.py'),
        ('pool groups across the six ledgers', '15', float(pools), 15.0, 'ledgers.*.POOLS',
         'test_routers_*.py'),
    ]


def check(rs=None):
    rs = rs or rows()
    bad = [(name, got, want) for name, _, got, want, _, _ in rs
           if want is not None and abs(got - want) > _tol(want)]
    return bad


def write(path=OUT):
    rs = rows()
    bad = check(rs)
    if bad:
        raise SystemExit('recomputed values differ from the section text: ' + json.dumps(bad))
    where = 'Sections 3 and 5.5 and Online Appendices A and D'
    lines = [f'# Appendix B. The exact numbers quoted in {where}, and where they come from', '',
             '*Generated by `src/lottery321/theory_numbers.py`, which recomputes each quoted value and '
             f'fails if it differs from the number quoted in {where} by more than half a unit in the last decimal quoted. No simulation is '
             'involved: every entry is an exact computation over the lottery kernels. The table lists the numbers the text quotes; '
             'full kernels and cumulative differences at every slot are produced by the same code and are not printed.*', '',
             '| quantity | as quoted | recomputed | produced by | covered by |',
             '|---|---|---|---|---|']
    esc = lambda s: s.replace('|', '\\|')             # a pipe inside a cell (3|4) must not split the row
    for name, quoted, got, _, fn, test in rs:
        lines.append(f'| {esc(name)} | {esc(quoted)} | {got:.4f} | `{fn}` | `{test}` |')
    lines += ['', 'The 3-2-1 kernel is `sequential_feasible` on the standard 16-team field, computed '
                  'exactly by dynamic programming over subsets; the old-rule kernel is '
                  '`flattened_2019_fast`, which reproduces the published 2019 odds table. Section 4.3 '
                  'records that the same 3-2-1 kernel reproduces all 64 marginals printed in the official '
                  'attachment after rounding.']
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return path, len(rs)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--out')
    a = ap.parse_args()
    p, n = write(a.out or OUT)
    print(f'{n} numbers checked and written to {p}')

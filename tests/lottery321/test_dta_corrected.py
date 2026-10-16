"""Tests for the corrected draw-then-adjust repair (dta_corrected, run tag dta2).

The checks do not reuse the repair under test as their own reference: they test properties the reading
states (feasibility, earliest/latest allowed slot, drawn order kept by the teams that are not moved), the
hand-worked counterexample, and agreement in distribution with the first repair where the two must agree
(floor only)."""
import sys, unittest
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src/lottery321'))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src/lottery321/ledgers'))
import dta_corrected as D
import league_sim as S
from lottery_rules import GROUP_BALLS, RELEGATED_FLOOR, repair_positions

N = 16


def field(restr):
    groups = ['bottom3'] * 3 + ['non_playin'] * 7 + ['playin_9_10'] * 4 + ['playin_7_8_losers'] * 2
    teams = [f'{g}_{i}' for i, g in enumerate(groups)]
    balls = {t: GROUP_BALLS[t.rsplit('_', 1)[0]] for t in teams}
    mx = {t: (RELEGATED_FLOOR if t.startswith('bottom3') else N) for t in teams}
    mn = {t: 1 for t in teams}
    used = set()
    for g, m in restr:
        t = next(u for u in teams if u.startswith(g) and u not in used); used.add(t); mn[t] = m
    return teams, balls, mx, mn


FIELDS = [[], [('bottom3', 2)], [('bottom3', 6)], [('non_playin', 2)], [('non_playin', 6)],
          [('playin_9_10', 6)], [('playin_7_8_losers', 2)], [('non_playin', 2), ('non_playin', 6)],
          [('bottom3', 6), ('bottom3', 6), ('non_playin', 6)], [('bottom3', 2), ('bottom3', 6), ('non_playin', 6)]]


def draws(teams, balls, k, seed):
    rng = np.random.default_rng(seed)
    w = np.array([balls[t] for t in teams], float)
    for row in np.argsort(rng.exponential(size=(k, len(teams))) / w, axis=1):
        yield [teams[i] for i in row]


def first_run_order(seq, mx, mn):
    """The order the first draw-then-adjust run produced (league_sim.new_draft_dta, written out)."""
    cons = [t for t in seq if mx[t] < N or mn[t] > 1]
    cpos = {t: r + 1 for r, t in enumerate(seq) if t in cons}
    if not any(cpos[t] > mx[t] or cpos[t] < mn[t] for t in cpos):
        return list(seq)
    fixed = repair_positions(cpos, None, None, mx, mn, N)
    others = [t for t in seq if t not in fixed]
    free = sorted(set(range(1, N + 1)) - set(fixed.values()))
    slot = dict(fixed); slot.update({t: free[k] for k, t in enumerate(others)})
    return sorted(seq, key=lambda t: slot[t])


class RepairOrder(unittest.TestCase):
    def test_counterexample_slot_13(self):
        teams, balls, mx, mn = field([('non_playin', 2)])
        X, B = 'non_playin_3', 'bottom3_0'
        rest = [t for t in teams if t not in (X, B)]
        seq = rest[:11] + [X, B] + rest[11:]
        U = seq[10]
        self.assertEqual(D.repair_order(seq, mx, mn)[10:13], [U, B, X])
        self.assertEqual(first_run_order(seq, mx, mn)[10:13], [B, X, U])     # the defect being fixed

    def test_properties_of_the_reading(self):
        for k, restr in enumerate(FIELDS):
            teams, balls, mx, mn = field(restr)
            for seq in draws(teams, balls, 3000, 100 + k):
                out = D.repair_order(seq, mx, mn)
                drawn = {t: r + 1 for r, t in enumerate(seq)}
                slot = {t: r + 1 for r, t in enumerate(out)}
                self.assertEqual(sorted(out), sorted(seq))
                for t in out:                                             # feasible
                    self.assertTrue(mn[t] <= slot[t] <= mx[t], (restr, seq, out))
                if not D._needs_repair(seq, mx, mn):
                    self.assertEqual(out, seq)
                # an unconstrained team is never placed after a later-drawn team that has no floor
                free = [t for t in seq if mx[t] == N and mn[t] == 1]
                for u in free:
                    for x in seq:
                        if mx[x] == N and drawn[u] < drawn[x]:
                            self.assertLess(slot[u], slot[x], (restr, seq, out, u, x))
                # floor violators end on the latest slots up to the floor
                late = [t for t in seq if drawn[t] > mx[t]]
                if late:
                    rel = sorted(slot[t] for t in seq if mx[t] < N)
                    self.assertEqual(rel[-len(late):], list(range(RELEGATED_FLOOR - len(late) + 1, RELEGATED_FLOOR + 1)))
                # with one restricted team, a team drawn too early lands exactly on its minimum
                if len(restr) == 1:
                    for t in seq:
                        if drawn[t] < mn[t]:
                            self.assertEqual(slot[t], mn[t])

    def test_floor_only_matches_first_run_in_distribution(self):
        """Without repeat restrictions the two repairs differ only by which relegated team takes which of
        the relegated teams' slots, so the sequence of team types is identical draw by draw."""
        teams, balls, mx, mn = field([])
        typ = lambda o: [t.rsplit('_', 1)[0] for t in o]
        for seq in draws(teams, balls, 20000, 7):
            self.assertEqual(typ(D.repair_order(seq, mx, mn)), typ(first_run_order(seq, mx, mn)))

    def test_mc_and_sampler_agree_and_kernel_is_valid(self):
        teams, balls, mx, mn = field([('non_playin', 2), ('bottom3', 6)])
        ref = D.draw_then_adjust_mc(teams, balls, mx, mn, draws=200000, seed=5)
        R = np.array([ref[t] for t in teams])
        np.testing.assert_allclose(R.sum(0), 1.0, atol=1e-12); np.testing.assert_allclose(R.sum(1), 1.0, atol=1e-12)
        for i, t in enumerate(teams):
            self.assertEqual(R[i, mx[t]:].sum(), 0.0); self.assertEqual(R[i, :mn[t] - 1].sum(), 0.0)
        WINS = np.arange(30) * 2
        PL = {'playoffs': set(range(16, 30)), 'nonplayin': list(range(10)), 'seeds910': [10, 11, 12, 13], 'losers78': [14, 15]}
        PRIO = np.linspace(0, 1, 30)
        mp = {0: 6, 4: 2}
        rng = np.random.default_rng(11); n = 40000; F = np.zeros((16, 16))
        for _ in range(n):
            order = D.new_draft_dta(WINS, PL, PRIO, rng.random(16), mp)
            self.assertEqual(order[16:], list(range(16, 30)))
            for s, t in enumerate(order[:16]):
                F[t, s] += 1
        F /= n
        members, rel, b2, mx2, mn2 = S._new_field(WINS, PL, PRIO, mp)
        ref2 = D.draw_then_adjust_mc(members, b2, mx2, mn2, draws=300000, seed=9)
        self.assertLess(np.abs(F - np.array([ref2[t] for t in range(16)])).max(), 0.012)

    def test_install_routes_simulate_to_the_corrected_repair(self):
        import importlib
        S2 = importlib.reload(S)
        old_k, old_d = S2._new_kernel_dta, S2.new_draft_dta
        D.S = S2
        D.install()
        try:
            self.assertIs(S2._new_kernel_dta, D._new_kernel_dta)
            self.assertIs(S2.new_draft_dta, D.new_draft_dta)
            WINS = np.arange(30) * 2
            PL = {'playoffs': set(range(16, 30)), 'nonplayin': list(range(10)), 'seeds910': [10, 11, 12, 13], 'losers78': [14, 15]}
            M = S2.new_marginal(WINS, PL, np.linspace(0, 1, 30), {4: 2}, 'draw_then_adjust')
            np.testing.assert_allclose(M.sum(0), 1.0, atol=1e-12); np.testing.assert_allclose(M.sum(1), 1.0, atol=1e-12)
        finally:
            S2._new_kernel_dta, S2.new_draft_dta = old_k, old_d


if __name__ == '__main__':
    unittest.main()

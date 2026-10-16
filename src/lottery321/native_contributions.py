"""Native-by-native contributions to one team's incentive in one game (exploratory; Online Appendix H.34).

Lemma 2(a) of the paper: a team's cumulative holdings difference is the sum over native picks of the
difference computed from that native's pick alone, C^c(j) = sum_n C^{c<-n}(j), whether or not the rights are
simple. The registered runs store holdings by holder, not by native, so this module re-simulates a single
focal game with the same world model as league_sim.simulate and keeps, for the chosen team, the holdings that come
from each native pick. Simple rights use the exact lottery marginals; pooled rights use `lottery_draws` joint
draft orders per world, exactly as in league_sim.simulate. Nothing in league_sim is changed.

Usage: python native_contributions.py   (runs the four pre-selected team-games; writes
       results/native_contributions/case_<k>.json)
"""
import json
import sys
import time
from datetime import timedelta
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / 'ledgers'))

import league_sim as S  # noqa: E402
import elo as E  # noqa: E402
import simulate as HR  # noqa: E402
from cutoff_state import build_state  # noqa: E402

ROOT = HERE.parents[1]
OUT = ROOT / 'results/native_contributions'

# Selection rule, fixed before any contribution was computed (2026-10-12): one team-game per portfolio
# category, mutually exclusive in this order of priority: (4) holds a pooled right; (2) holds the opponent's
# pick; (3) holds another team's pick conditionally; (1) holds no other pick and its own pick is protected.
# In each, the old-rule actual-portfolio class-B reversal with the largest |linear-curve tau| (earliest day
# on ties); category (1) has no old-rule reversal, so it takes the 3-2-1 reversal with the largest |tau|
# among team-games whose own-pick verdict is not a reversal.
CASES = (
    dict(label='own protected pick only', season='2020-21', day='2021-05-16', team='LAL', opp='NOP', rule='new'),
    dict(label="opponent's pick", season='2021-22', day='2022-03-27', team='NOP', opp='LAL', rule='old'),
    dict(label="another team's pick", season='2023-24', day='2024-04-14', team='POR', opp='SAC', rule='old'),
    dict(label='pooled right', season='2024-25', day='2025-04-13', team='UTA', opp='MIN', rule='old'),
)
CURVES = {
    'linear': lambda s: (30 - s) / 29,
}


def simulate_by_native(state, j_focal, team, n, seed, router, min_pick_new, batches=50, lottery_draws=4):
    """Holdings of `team` by native pick, (batches, branch, rule, native, slot) batch means; branch 0 = home
    team of the focal game wins. Same random-number use per world as league_sim.simulate."""
    T, TEAMS = S.T, S.TEAMS
    rem = state['remaining']; G = len(rem)
    probs = np.array([p for _, _, p in rem]); q = np.asarray(state['q'])
    rng = np.random.default_rng(seed)
    simple_idx = np.array([T[x] for x in router.simple_natives], int)
    HM = np.array([[T[router.simple(TEAMS[nat], s + 1)] for s in range(30)] for nat in simple_idx], int)
    c = T[team]
    mask = (HM == c)                                  # simple natives: slots at which `team` holds the pick
    inv = 1.0 / lottery_draws; per = n // batches
    base_w = np.asarray(state['wins'], int); base_h = np.asarray(state['h2h_wins'], int)
    hg = np.asarray(state['h2h_games_final'], int)
    out = np.zeros((batches, 2, 2, 30, 30))
    a, b, _ = rem[j_focal]
    for k in range(n):
        ug = rng.random(G); us = rng.random(30); up = rng.random(6); ud = rng.random(30)
        ul = rng.random((lottery_draws, 16))
        home_wins = ug < probs
        w = base_w.copy(); h = base_h.copy()
        for j, (x, y, _) in enumerate(rem):
            if y < 0:
                w[x] += int(home_wins[j]); continue
            if home_wins[j]:
                w[x] += 1; h[x, y] += 1
            else:
                w[y] += 1; h[y, x] += 1
        ww = w.copy(); hh = h.copy()
        if home_wins[j_focal]:
            ww[a] -= 1; hh[a, b] -= 1
        else:
            ww[b] -= 1; hh[b, a] -= 1
        Hk = np.zeros((2, 2, 30, 30))
        for br, (win, lose) in enumerate(((a, b), (b, a))):
            w2 = ww.copy(); h2 = hh.copy(); w2[win] += 1; h2[win, lose] += 1
            orders = S.conference_orders(w2, h2, hg, us, 'criteria')
            pl = S.playin(orders, up, q)
            for r in (0, 1):
                M = S.old_marginal(w2, pl, ud) if r == 0 else S.new_marginal(w2, pl, ud, min_pick_new)
                Hk[br, r, simple_idx] += M[simple_idx] * mask
                if router.pools:
                    for kk in range(lottery_draws):
                        order = S.old_draft(w2, pl, ud, ul[kk]) if r == 0 else S.new_draft(w2, pl, ud, ul[kk], min_pick_new)
                        pos = {TEAMS[t]: s + 1 for s, t in enumerate(order)}
                        native_at = {s: nat for nat, s in pos.items()}
                        for s, holder in router.pooled(pos).items():
                            if holder == team:
                                Hk[br, r, T[native_at[s]], s - 1] += inv
        out[k // per] += Hk
    return out / per


def summarize(Hb, home_is_team):
    """Loss-minus-win cumulative difference by native, and linear-curve tau with batch-means SE."""
    D = Hb[:, 1] - Hb[:, 0] if home_is_team else Hb[:, 0] - Hb[:, 1]   # (batches, rule, native, slot)
    C = np.cumsum(D, axis=-1)
    v = np.array([(30 - s) / 29 for s in range(1, 31)])
    tau_b = (D * v).sum(-1)                                             # (batches, rule, native)
    B = D.shape[0]
    res = {}
    for r, name in ((0, 'old'), (1, 'new')):
        rows = {}
        for nat in range(30):
            if np.abs(D[:, r, nat]).max() == 0 and np.abs(Hb[:, :, r, nat]).max() == 0:
                continue
            m = C[:, r, nat].mean(0); se = C[:, r, nat].std(0, ddof=1) / np.sqrt(B)
            t = tau_b[:, r, nat]
            rows[S.TEAMS[nat]] = dict(tau=float(t.mean()), tau_se=float(t.std(ddof=1) / np.sqrt(B)),
                                      C=[round(float(x), 5) for x in m], C_se=[round(float(x), 5) for x in se],
                                      M=float(m[-1]))
        tot = tau_b[:, r].sum(-1); Ct = C[:, r].sum(1)
        res[name] = dict(by_native=rows, total=dict(tau=float(tot.mean()), tau_se=float(tot.std(ddof=1) / np.sqrt(B)),
                                                      C=[round(float(x), 5) for x in Ct.mean(0)],
                                                      C_se=[round(float(x), 5) for x in Ct.std(0, ddof=1) / np.sqrt(B)]))
    return res


def run_case(case, games, n=32000):
    season, day = case['season'], case['day']
    todays = HR.window_days(games, season)[day]
    cutoff = min(g['start'] for g in todays) - timedelta(hours=6)
    state = build_state(games, season, cutoff)
    year = HR.draft_year(season)
    router = HR.router_for(year); mp = HR.restrictions(year)
    name = {i: t for t, i in E.IDX.items()}
    gid = next(g['game_id'] for g in todays if {name[g['h']], name[g['a']]} == {case['team'], case['opp']})
    j = state['remaining_ids'].index(gid)
    a, b, _ = state['remaining'][j]
    seed = int(day.replace('-', ''))
    t0 = time.time()
    Hb = simulate_by_native(state, j, case['team'], n, seed, router, mp)
    res = summarize(Hb, S.TEAMS[a] == case['team'])
    return dict(case, game_id=gid, home=S.TEAMS[a], away=S.TEAMS[b], n_worlds=n, seed=seed,
                secs=round(time.time() - t0, 1), result=res)


if __name__ == '__main__':
    games = E.load_games(HR.GAMES)
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 32000
    which = [int(x) for x in sys.argv[2:]] or range(len(CASES))
    OUT.mkdir(parents=True, exist_ok=True)
    for i in which:
        r = run_case(CASES[i], games, n)
        (OUT / f'case_{i + 1}.json').write_text(json.dumps(r, indent=1), encoding='utf-8')
        print(i + 1, r['label'], r['secs'], 's', flush=True)

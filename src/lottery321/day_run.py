"""adaptive runner: fixed-size batches, pre-declared looks, stop when precision is met.

Stopping rule (declared before any production run):
  metrics  = tau_old, tau_new, delta_tau on the LINEAR curve, both teams of every focal game
  target   = halfwidth <= 0.003 with z = 2.807034 (99%, multi-look adjusted)
  looks    = cumulative worlds 2,000 -> 8,000 -> 32,000; stop at the first look that meets the target
  failure  = still above target at 32,000: results kept and flagged `precision_met = False`
Batches of 40 worlds; each look adds a new block with its own seed (seed + look index) so blocks are
independent and the pooled batch means are exchangeable.
"""
import numpy as np

try:
    from league_sim import simulate
    from value import tau_table, precision_met
except ImportError:
    from .league_sim import simulate
    from .value import tau_table, precision_met

LOOKS = (2000, 8000, 32000)
BATCH = 40
TARGET = 0.003


def run_day(state, focal, seed, router=None, min_pick_new=None, looks=LOOKS, batch=BATCH, target=TARGET,
            probs_override=None, lottery_draws=4, new_procedure='sequential_feasible'):
    focal_teams = [(state['remaining'][j][0], state['remaining'][j][1]) for j in focal]
    blocks, blocks_own, done, log = [], [], 0, []
    Qsum = None
    for li, goal in enumerate(looks):
        add = goal - done
        if add % batch:
            raise ValueError('look sizes must be multiples of batch size')
        res = simulate(state, focal, n=add, seed=seed + li, router=router, min_pick_new=min_pick_new,
                       batches=add // batch, probs_override=probs_override, lottery_draws=lottery_draws,
                       new_procedure=new_procedure)
        blocks.append(res['DB']); blocks_own.append(res['DB_own']); Qsum = res['Q'] * add if Qsum is None else Qsum + res['Q'] * add
        STsum = res['ST'] * add if li == 0 else STsum + res['ST'] * add
        done = goal
        pooled = {'DB': np.concatenate(blocks, axis=0), 'DB_own': np.concatenate(blocks_own, axis=0),
                  'Q': Qsum / done, 'ST': STsum / done, 'n': done}
        rows = tau_table(pooled, focal_teams)
        met, worst = precision_met(rows, target)
        log.append({'look': li + 1, 'worlds': done, 'max_halfwidth_linear': worst, 'precision_met': met})
        if met:
            break
    pooled.update({'looks': log, 'precision_met': log[-1]['precision_met'], 'focal_teams': focal_teams})
    return pooled

"""NBA sporting win-record criteria, with explicit residual random-priority assumption.

Not an official NBA certification. Final point differential is unmodeled; if the
win-record criteria exhaust, use supplied random priority. Sporting and draft
lottery tie draws must use separate priorities.
"""
from fractions import Fraction
import numpy as np
try:
    from .teams import TEAMS
except ImportError:
    from teams import TEAMS

DIVISIONS = (
    ('BKN','BOS','NYK','PHI','TOR'),
    ('CHI','CLE','DET','IND','MIL'),
    ('ATL','CHA','MIA','ORL','WAS'),
    ('DEN','MIN','OKC','POR','UTA'),
    ('GSW','LAC','LAL','PHX','SAC'),
    ('DAL','HOU','MEM','NOP','SAS'),
)
DIVISION_MEMBERS = tuple(tuple(TEAMS.index(t) for t in d) for d in DIVISIONS)
DIVISION = {t:i for i,d in enumerate(DIVISION_MEMBERS) for t in d}
CONFERENCES = (tuple(range(15)), tuple(range(15,30)))


def eligible_by_record(wins, number=10):
    """Include every team tied at the raw-record threshold, before tiebreaks."""
    if number not in (8,10):raise ValueError('Eligible cutoff must be 8 or 10')
    result=[]
    for conf in CONFERENCES:
        threshold=sorted((wins[j] for j in conf),reverse=True)[number-1]
        result.append(tuple(t for t in conf if wins[t]>=threshold))
    return tuple(result)


def break_tie(group, h2h_wins, h2h_games, priority, division_winners, eligible,
              *, skip_division_winner=False, diagnostics=None):
    """Apply first separating criterion and restart each remaining tied subset.

    Caller supplies a same-conference tied group. This small helper deliberately
    does not validate a full 82-game season, so bad-case criteria can be tested
    independently. `conference_orders` is the public simulation entry point.
    """
    group=list(group)
    if len(group)<=1:return group
    conf=group[0]//15
    if any(t//15!=conf for t in group):raise ValueError('Cross-conference sporting tie')
    two=len(group)==2
    same_division=len({DIVISION[t] for t in group})==1
    criteria=['head','leader'] if two else ['leader','head']
    if same_division:criteria.append('division')
    criteria.extend(['conference','eligible_own'])
    if two:criteria.append('eligible_other')
    for criterion in criteria:
        if criterion=='leader':
            if skip_division_winner:continue
            values={t:int(t in division_winners) for t in group}
        else:
            opponents=(group if criterion=='head' else DIVISION_MEMBERS[DIVISION[group[0]]]
                       if criterion=='division' else CONFERENCES[conf]
                       if criterion=='conference' else eligible[conf]
                       if criterion=='eligible_own' else eligible[1-conf])
            values={}
            for t in group:
                numerator=sum(int(h2h_wins[t,j]) for j in opponents)
                denominator=sum(int(h2h_games[t,j]) for j in opponents)
                if denominator<=0:raise ValueError('Missing games for tiebreak criterion '+criterion)
                values[t]=Fraction(numerator,denominator)
        buckets={}
        for t,value in values.items():buckets.setdefault(value,[]).append(t)
        if len(buckets)>1:
            if diagnostics is not None:
                key='resolved_'+criterion
                diagnostics[key]=diagnostics.get(key,0)+1
            return [t for value in sorted(buckets,reverse=True)
                    for t in break_tie(buckets[value],h2h_wins,h2h_games,priority,division_winners,eligible,
                        skip_division_winner=skip_division_winner,diagnostics=diagnostics)]
    if diagnostics is not None:
        diagnostics['residual_groups']=diagnostics.get('residual_groups',0)+1
        diagnostics['residual_teams']=diagnostics.get('residual_teams',0)+len(group)
    # Research replacement for unknown final net point differential, not a claim
    # that all official NBA criteria reached a literal equality.
    return sorted(group,key=lambda t:priority[t])


def conference_orders(wins, h2h_wins, h2h_games, priority, mode='criteria', *, diagnostics=None):
    """Return [East order, West order] in teams.TEAMS indices, best first.

    criteria: current official top-10 eligibility definition, applied
      retrospectively with point-differential residual replaced by priority.
    criteria8: old-terminology top-8 sensitivity, NOT current official text.
    random: earlier record-based priority, then random priority.

    Hot-path checks are shapes/mode only. Call validate_complete_state separately
    on a representative/full input to audit matrix symmetry and 82 games each.
    """
    if mode not in ('criteria','criteria8','random'):raise ValueError('Unknown sporting tie mode')
    wins=np.asarray(wins);h2h_wins=np.asarray(h2h_wins);h2h_games=np.asarray(h2h_games);priority=np.asarray(priority)
    if wins.shape!=(30,) or priority.shape!=(30,) or h2h_wins.shape!=(30,30) or h2h_games.shape!=(30,30):
        raise ValueError('Tiebreak input shape mismatch')
    if mode=='random':
        return [sorted(conf,key=lambda t:(-int(wins[t]),priority[t])) for conf in CONFERENCES]
    eligible=eligible_by_record(wins,8 if mode=='criteria8' else 10)
    leaders=set()
    # Resolve division title first, without a provisional winner bonus. Throw
    # away the other relative positions: only the winning identity carries.
    for division in DIVISION_MEMBERS:
        maximum=max(wins[t] for t in division)
        tied=[t for t in division if wins[t]==maximum]
        leaders.add(break_tie(tied,h2h_wins,h2h_games,priority,set(),eligible,
                             skip_division_winner=True,diagnostics=diagnostics)[0])
    orders=[]
    for conf in CONFERENCES:
        grouped={}
        for t in conf:grouped.setdefault(int(wins[t]),[]).append(t)
        orders.append([t for record in sorted(grouped,reverse=True)
                       for t in break_tie(grouped[record],h2h_wins,h2h_games,priority,leaders,eligible,
                                          diagnostics=diagnostics)])
    return orders


def validate_complete_state(wins,h2h_wins,h2h_games,priority):
    w=np.asarray(wins);h=np.asarray(h2h_wins);g=np.asarray(h2h_games);p=np.asarray(priority)
    if w.shape!=(30,) or h.shape!=(30,30) or g.shape!=(30,30) or p.shape!=(30,):raise ValueError('State shapes')
    if not all(np.isfinite(x).all() for x in (w,h,g,p)):raise ValueError('Nonfinite state')
    if any((x<0).any() or not np.equal(x,np.floor(x)).all() for x in (w,h,g)):raise ValueError('Noninteger counts')
    if not np.array_equal(h+h.T,g) or not np.array_equal(g,g.T):raise ValueError('Head-to-head conservation')
    if np.diag(g).any() or np.diag(h).any():raise ValueError('Self game')
    if not np.all(g.sum(axis=1)==82) or not np.array_equal(h.sum(axis=1),w):raise ValueError('Final82-state conservation')
    if len(set(p))!=30:raise ValueError('Priority must be a strict random ordering')
    return True


def repeat_minimum(history, target_year):
    """Derive constraints keyed by ORIGINAL identity, never holder identity.

    history is {year:{original_team:first_round_position}}. Returns only logically
    established restrictions from supplied history. Partial input does NOT
    certify eligibility for omitted teams; contract coverage must be checked
    separately. Using this for 2024 is a hypothetical rule-transplant scenario.
    """
    if any(int(year)>=target_year for year in history):raise ValueError('History must precede target draft')
    normalized={int(year):picks for year,picks in history.items()}
    for picks in normalized.values():
        if any(t not in TEAMS or type(v)is not int or not 1<=v<=30 for t,v in picks.items()):
            raise ValueError('Original team or pick position invalid')
    last=normalized.get(target_year-1,{});prior=normalized.get(target_year-2,{})
    result={t:2 for t,pos in last.items() if pos==1}
    result.update({t:6 for t,pos in last.items() if pos<=5 and t in prior and prior[t]<=5})
    return result

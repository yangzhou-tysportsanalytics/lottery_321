"""2020 first-round rights ledger (historical, executable routing).

State: after the 2020-02-06 trade deadline, as of the March 2020 hiatus (draft order used records as
of 2020-03-11). route(pos) takes the final 2020 draft slot of every NATIVE first-round pick
(dict team -> 1..30, a permutation) and returns {slot: holder}. Lower slot = more favorable.
Evidence per native pick: ledger_2020_draft.json (same directory). Out-of-object fallbacks
(carryover to 2021+, second-rounders owed when a pick is protected) are recorded there, not routed here.
No 2020 first-round pick was part of a swap or multi-pick pool at the deadline.
"""
TEAMS = ('ATL', 'BKN', 'BOS', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL',
         'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'TOR',
         'UTA', 'WAS')

ASSUMPTIONS = []  # every branch of every 2020 condition is stated in the sources

# Realized slot -> (deadline holder, pre-draft holder, note). Empty: no post-deadline pre-draft change
# of ownership of a 2020 first (draft-day / post-draft trades are not listed).
POST_DEADLINE_CHANGES = {}


def _simple_holder(native, slot):
    if native == 'BKN': return 'BKN' if slot <= 14 else 'MIN'   # top-14 protected (via ATL)
    if native == 'PHI': return 'PHI' if slot <= 14 else 'BKN'   # top-14 protected (via LAC)
    if native == 'CLE': return 'CLE' if slot <= 10 else 'NOP'   # top-10 protected
    if native == 'IND': return 'IND' if slot <= 14 else 'MIL'   # top-14 protected
    if native == 'MIL': return 'MIL' if slot <= 7 else 'BOS'    # top-7 protected (via PHX)
    if native == 'DEN': return 'DEN' if slot <= 10 else 'OKC'   # top-10 protected
    if native == 'OKC': return 'OKC' if slot <= 20 else 'PHI'   # top-20 protected
    if native == 'UTA': return 'MEM' if 8 <= slot <= 14 else 'UTA'  # protected 1-7 and 15-30
    if native == 'GSW': return 'GSW' if slot <= 20 else 'BKN'   # top-20 protected
    if native == 'LAC': return 'NYK'                            # unprotected
    if native == 'HOU': return 'DEN'                            # unprotected
    if native == 'MEM': return 'MEM' if slot <= 6 else 'BOS'    # top-6 protected
    return native


def route(pos):
    if sorted(pos) != sorted(TEAMS) or sorted(pos.values()) != list(range(1, 31)):
        raise ValueError('pos must map all 30 native teams to a permutation of 1..30')
    return {pos[t]: _simple_holder(t, pos[t]) for t in TEAMS}


POOLS = ()
POOLED = {t for p in POOLS for t in p}


class Router2020:
    simple_natives = tuple(t for t in TEAMS if t not in POOLED)
    pools = POOLS

    @staticmethod
    def simple(native, slot):
        return _simple_holder(native, slot)

    @staticmethod
    def pooled(pos):
        """pos: native -> slot for (at least) the pooled natives. Returns {slot: holder} for pooled natives."""
        full = {t: pos[t] for t in POOLED}
        others = [s for s in range(1, 31) if s not in full.values()]
        filler = [t for t in TEAMS if t not in POOLED]
        full.update(dict(zip(filler, others)))
        out = route(full)
        return {full[t]: out[full[t]] for t in POOLED}

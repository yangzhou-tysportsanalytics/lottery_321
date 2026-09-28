"""2022 first-round rights ledger (executable routing), state after the 2022-02-10 trade deadline.

route(pos) takes the final 2022 draft slot of every NATIVE first-round pick (dict team -> 1..30,
a permutation) and returns {slot: holder}. Lower slot = more favorable.
Evidence (sources, paraphrased terms, realized draft) lives in ledger_2022_draft.json.
Out-of-object fallbacks (future-year picks, second-rounders owed if a pick is kept) are not routed here.
"""
TEAMS = ('ATL', 'BKN', 'BOS', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL',
         'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'TOR',
         'UTA', 'WAS')

ASSUMPTIONS = [
    "PHI: Brooklyn held an unprotected 2022 PHI first with an option to defer it to 2023. The option was "
    "exercised on 2022-06-01 (after the deadline), so the deadline holder is BKN at every slot; the "
    "deferral is listed in POST_DEADLINE_CHANGES rather than routed.",
    "BKN/HOU/MIA: follows HR_sep21's literal three-pick wording (HOU gets the two most favorable of the "
    "BKN, HOU and MIA picks, MIA the least favorable; if MIA's pick is 1-14 it is protected and each "
    "pick stays put: BKN's with HOU, HOU's with HOU, MIA's with MIA). HR_mar22 describes only a BKN-vs-MIA "
    "choice; the two readings differ only when HOU's own pick is the least favorable of the three.",
]

POST_DEADLINE_CHANGES = {
    23: ('BKN', 'PHI', 'Brooklyn exercised its option (2022-06-01) to defer the PHI pick to 2023; '
                       'Philadelphia selected at #23 itself.'),
}


def _protected(p, lo, hi): return lo <= p <= hi


def _simple_holder(native, slot):
    if native == 'DET': return 'DET' if slot <= 16 else 'OKC'
    if native == 'OKC': return 'OKC' if slot <= 14 else 'ATL'
    if native == 'POR': return 'POR' if slot <= 14 else 'CHI'
    if native == 'CHA': return 'CHA' if slot <= 18 else 'ATL'
    if native == 'TOR': return 'TOR' if slot <= 14 else 'SAS'
    if native == 'CLE': return 'CLE' if slot <= 14 else 'IND'
    if native == 'BOS': return 'BOS' if slot <= 4 else 'SAS'
    if native == 'UTA': return 'UTA' if slot <= 6 else 'MEM'
    if native == 'PHX': return 'PHX' if slot <= 12 else 'OKC'
    if native == 'LAC': return 'OKC'
    if native == 'PHI': return 'BKN'  # deferral option not exercised at the deadline (see ASSUMPTIONS)
    if native == 'NOP':  # three-way split
        if slot <= 4: return 'NOP'
        return 'POR' if slot <= 14 else 'CHA'
    if native == 'LAL': return 'NOP' if slot <= 10 else 'MEM'
    return native


POOLS = (('BKN', 'HOU', 'MIA'),)
POOLED = {t for p in POOLS for t in p}


def route(pos):
    if sorted(pos) != sorted(TEAMS) or sorted(pos.values()) != list(range(1, 31)):
        raise ValueError('pos must map all 30 native teams to a permutation of 1..30')
    h = {t: _simple_holder(t, pos[t]) for t in TEAMS if t not in POOLED}

    # BKN/HOU/MIA pool. HOU holds BKN's pick outright and a swap right with MIA (MIA top-14 protected).
    if _protected(pos['MIA'], 1, 14):
        h['BKN'], h['HOU'], h['MIA'] = 'HOU', 'HOU', 'MIA'
    else:
        # ASSUMPTION: literal HR_sep21 three-pick reading (HOU two best, MIA worst).
        r = sorted(['BKN', 'HOU', 'MIA'], key=lambda t: pos[t])
        h[r[0]], h[r[1]], h[r[2]] = 'HOU', 'HOU', 'MIA'

    return {pos[t]: h[t] for t in TEAMS}


class Router2022:
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

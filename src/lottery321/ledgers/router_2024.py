"""2024 NBA draft first-round rights ledger (historical, executable routing).

State: after the 2023-24 trade deadline (Feb 8, 2024). route(pos) takes the final 2024 draft position of every
NATIVE first-round pick (dict team -> 1..30, a permutation) and returns {position: holder}, where holder is the
team holding the pick under the deadline-state terms. Lower position = more favorable.
Evidence per native: ledger_2024_draft.json (same directory). Sources: Hoops Rumors 2023-08-09 list
(https://www.hoopsrumors.com/2023/08/traded-first-round-picks-for-2024-nba-draft.html) and 2024-03-08 check-in
(https://www.hoopsrumors.com/2024/03/checking-in-on-traded-2024-first-round-picks.html).
Post-deadline elections/trades are NOT applied here; see POST_DEADLINE_CHANGES.
"""
TEAMS = ('ATL', 'BKN', 'BOS', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL',
         'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'TOR',
         'UTA', 'WAS')

ASSUMPTIONS = [
    "Swap rights are exercised if and only if they give the holder a more favorable pick (lower slot).",
    "WAS/PHX/MEM: the WAS swap with PHX is resolved first, then MEM's swap ('subsequently' in HR Aug 2023). "
    "If WAS keeps its pick (1-12): WAS gets min(WAS,PHX); MEM swaps its own pick for the less favorable of the two "
    "(the pick left with PHX) if that is better; PHX ends with the remainder. If the WAS pick conveys to NYK (13-30), "
    "NYK takes it with no swap right and MEM may swap only against the PHX pick (HR Aug 2023 states this explicitly).",
    "OKC pool uses the general rule stated in HR Aug 2023: of the picks OKC controls that actually convey (own, LAC "
    "unprotected, HOU if 5-30, UTA if 11-30), UTA gets the least favorable, WAS the second-least, OKC all others. "
    "The 3-pick case (exactly one of HOU/UTA protected: OKC best, WAS middle, UTA worst) follows from that general "
    "sentence; HR only gave worked examples for the 2- and 4-pick cases.",
    "OKC pool: HR Mar 2024 describes the split as 'WAS gets the better of the LAC/OKC picks, UTA the worse'. That is "
    "the general rule applied to the projected standings; it differs from the general rule only if a conveyed HOU/UTA "
    "pick lands worse than both the LAC and OKC picks. The general (original-terms) rule is encoded.",
    "UTA's own pick, if it conveys (11-30), enters the OKC pool and can come back to UTA as the least favorable pick "
    "(literal reading of the pool rule).",
    "LAL: NOP held the LAL 2024 pick (unprotected) with an option to defer it to 2025. NOP made the election on "
    "2024-06-01 (after the deadline and the lottery; Hoops Rumors 2024-06-01), so the deadline holder is NOP for "
    "every slot; the election is recorded in POST_DEADLINE_CHANGES.",
]

# slot -> (deadline_holder, draft_holder, note); only for the REALIZED 2024 draft
POST_DEADLINE_CHANGES = {
    17: ('NOP', 'LAL', 'NOP elected on 2024-06-01 to defer the LAL pick to 2025; LAL selected at #17.'),
}


def route(pos):
    if sorted(pos) != sorted(TEAMS) or sorted(pos.values()) != list(range(1, 31)):
        raise ValueError('pos must map all 30 native teams to a permutation of 1..30')
    h = {t: _simple_holder(t, pos[t]) for t in TEAMS if t not in POOLED}
    h.update(_pool_wpm(pos))
    h.update(_pool_okc(pos))
    h.update(_pool_milnop(pos))
    return {pos[t]: h[t] for t in TEAMS}


def _pool_wpm(pos):
    """WAS (top-12 prot. to NYK) + WAS swap with PHX + MEM swap vs least favorable of WAS/PHX."""
    h = {}
    if pos['WAS'] <= 12:
        # WAS keeps its pick and may swap with PHX
        b, w = sorted(['WAS', 'PHX'], key=lambda t: pos[t])
        h[b], h[w] = 'WAS', 'PHX'
        # ASSUMPTION: MEM then swaps its own pick for the less favorable of the two (held by PHX) if better
        if pos[w] < pos['MEM']:
            h[w], h['MEM'] = 'MEM', 'PHX'
        else:
            h['MEM'] = 'MEM'
    else:
        h['WAS'] = 'NYK'  # NYK takes it, no swap right
        if pos['PHX'] < pos['MEM']:
            h['PHX'], h['MEM'] = 'MEM', 'PHX'
        else:
            h['PHX'], h['MEM'] = 'PHX', 'MEM'
    return h


def _pool_okc(pos):
    """OKC-controlled picks: own, LAC (unprot.), HOU (top-4 prot.), UTA (top-10 prot.)."""
    h = {}
    conveyed = ['OKC', 'LAC']
    if pos['HOU'] <= 4:
        h['HOU'] = 'HOU'
    else:
        conveyed.append('HOU')
    if pos['UTA'] <= 10:
        h['UTA'] = 'UTA'
    else:
        conveyed.append('UTA')
    r = sorted(conveyed, key=lambda t: pos[t])  # most favorable first
    # ASSUMPTION: general rule -> least favorable to UTA, second-least to WAS, rest to OKC
    h[r[-1]] = 'UTA'
    h[r[-2]] = 'WAS'
    for t in r[:-2]:
        h[t] = 'OKC'
    return h


def _pool_milnop(pos):
    b, w = sorted(['MIL', 'NOP'], key=lambda t: pos[t])
    return {b: 'NOP', w: 'MIL'}


# ------------------------------------------------------------------ decomposed form for exact lotteries
def _simple_holder(native, slot):
    if native == 'BKN': return 'HOU'
    if native == 'LAL': return 'NOP'  # deadline state; deferral elected post-deadline (POST_DEADLINE_CHANGES)
    if native == 'TOR': return 'TOR' if slot <= 6 else 'SAS'
    if native == 'DET': return 'DET' if slot <= 18 else 'NYK'
    if native == 'IND': return 'IND' if slot <= 3 else 'TOR'
    if native == 'CHA': return 'CHA' if slot <= 14 else 'SAS'
    if native == 'POR': return 'POR' if slot <= 14 else 'CHI'
    if native == 'GSW': return 'GSW' if slot <= 4 else 'POR'
    if native == 'SAC': return 'SAC' if slot <= 14 else 'ATL'
    if native == 'DAL': return 'DAL' if slot <= 10 else 'NYK'
    return native


POOLS = (('MEM', 'PHX', 'WAS'), ('HOU', 'LAC', 'OKC', 'UTA'), ('MIL', 'NOP'))
POOLED = {t for p in POOLS for t in p}


class Router2024:
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

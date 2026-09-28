"""2026 NBA draft first-round rights ledger (historical, executable routing).

State: after the 2025-26 trade deadline (Feb 5, 2026). route(pos) takes the final 2026 draft position of every
NATIVE first-round pick (dict team -> 1..30, a permutation) and returns {position: holder} under the
deadline-state terms. Lower position = more favorable. 2019-2026 lottery rules applied upstream (not here).
Evidence per native: ledger_2026_draft.json (same directory).
Main source: Hoops Rumors "Traded First-Round Picks For 2026 NBA Draft"
(https://www.hoopsrumors.com/2025/08/traded-first-round-picks-for-2026-nba-draft.html; dated 2025-08-27 but
maintained: the version consulted includes the Feb 2026 deadline deals and an explicit "details at bottom" section
for the two swap networks, incl. the UTA-outside-top-8 and WAS-outside-top-8 branches). Deadline deals:
https://www.hoopsrumors.com/2026/02/2026-nba-trade-deadline-recap.html (IND->LAC Zubac trade; OKC->PHI rank-2
pool right in the McCain trade), https://www.hoopsrumors.com/2026/02/mavericks-to-trade-anthony-davis-to-wizards.html
(WAS->DAL least-favorable pool right), https://www.nba.com/news/kevin-huerter-jaden-ivey-trade-2026 (DET-MIN
swap protected 1-19).
Post-deadline pre-draft trades are NOT applied here; see POST_DEADLINE_CHANGES (empty: no 2026 first moved
between the deadline and the draft). Note: #13 (MIA) was part of the Giannis Antetokounmpo trade agreed on the
eve of round 1 (reported late Monday June 22/23, 2026; round 1 was Tuesday June 23) and completed July 6;
NBA.com lists Miami as selecting (traded to MIL), which equals the deadline holder, so it is not listed as a
change (same convention as the 2025 module). All other realized trades (#16, 17, 21, 24, 25, 26, 28, 29, 30)
were draft-night or later.
"""
TEAMS = ('ATL', 'BKN', 'BOS', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL',
         'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'TOR',
         'UTA', 'WAS')

ASSUMPTIONS = [
    "Swap / best-of rights are exercised if and only if they give the holder a more favorable pick (lower slot).",
    "UTA best-of right (UTA slot 1-8): resolved as UTA swapping with MIN first, then with CLE. This ordering is "
    "not stated as such; it is the order that reproduces Hoops Rumors' closed form for the pick facing ATL "
    "('least favorable of CLE's pick and the more favorable of UTA's (if top 8) or MIN's'): if CLE's pick is "
    "the best of the three, CLE receives the better of the UTA/MIN picks and MIN the worse.",
    "DET-MIN swap (protected 1-19): DET's swap applies to the pick MIN holds after the UTA swap. If that is MIN's "
    "own pick it is eligible only at slots 20-30; if MIN holds UTA's pick (UTA took MIN's), it is eligible at any "
    "slot. Literal reading of Hoops Rumors listing 'the Jazz's pick (if in the top eight)' among the picks DET "
    "can receive without the top-19 qualifier; the Hoops Rumors closed forms for DET/MIN are internally "
    "inconsistent in some branches (e.g. MIN's own pick in 1-19), so the sequential form is used.",
    "HOU top-4 protected (HOU slot 1-4): HOU keeps its pick and it leaves the OKC/HOU/LAC pool. PHI gets the "
    "more favorable of OKC/LAC (stated by CBS Philadelphia's report on the McCain trade). "
    "Assumed: DAL, holder of the 'least favorable of the three', gets the other one, and OKC gets none.",
    "ATL/SAS/CLE: SAS's swap with ATL is resolved first; ATL then swaps the pick it holds with the pick CLE holds "
    "after the UTA step (Hoops Rumors closed form).",
]

# slot -> (deadline_holder, draft_holder, note); only for the REALIZED 2026 draft
POST_DEADLINE_CHANGES = {}


def route(pos):
    if sorted(pos) != sorted(TEAMS) or sorted(pos.values()) != list(range(1, 31)):
        raise ValueError('pos must map all 30 native teams to a permutation of 1..30')
    h = {t: _simple_holder(t, pos[t]) for t in TEAMS if t not in POOLED}
    h.update(_pool_uta_chain(pos))
    h.update(_pool_was_mem(pos))
    h.update(_pool_okc(pos))
    h.update(_pool_mil_nop(pos))
    assert set(h) == set(TEAMS) and set(h.values()) <= set(TEAMS)
    return {pos[t]: h[t] for t in TEAMS}


def _pool_uta_chain(pos):
    """Six-team network: SAS/ATL swap, UTA best-of (UTA/MIN/CLE, only if UTA 1-8, else UTA->OKC),
    DET/MIN swap (MIN own pick protected 1-19), ATL/CLE swap."""
    holds = {t: t for t in ('ATL', 'CLE', 'DET', 'MIN', 'SAS', 'UTA')}  # team -> native pick it currently holds
    h = {}

    def swap(a, b, cond=True):
        """Team a takes team b's held pick if cond and it is more favorable."""
        if cond and pos[holds[b]] < pos[holds[a]]:
            holds[a], holds[b] = holds[b], holds[a]

    # SAS gets the more favorable of the SAS and ATL picks
    swap('SAS', 'ATL')
    if pos['UTA'] <= 8:
        # ASSUMPTION: MIN swap first, then CLE (reproduces the Hoops Rumors closed form)
        swap('UTA', 'MIN')
        swap('UTA', 'CLE')
        h[holds['UTA']] = 'UTA'
    else:
        h['UTA'] = 'OKC'  # top-8 protection lost; UTA's swap rights not in play (Hoops Rumors)
        holds['UTA'] = None
    # DET swap with the pick MIN holds; MIN's own pick is protected 1-19
    # ASSUMPTION: protection applies only to MIN's own pick (UTA's pick held by MIN is always eligible)
    m = holds['MIN']
    swap('DET', 'MIN', cond=(m != 'MIN') or pos['MIN'] >= 20)
    # ATL (holding the worse of ATL/SAS) swaps with the pick CLE holds
    swap('ATL', 'CLE')
    for team in ('ATL', 'CLE', 'DET', 'MIN', 'SAS'):
        h[holds[team]] = team
    return h


def _pool_was_mem(pos):
    """WAS top-8 to NYK; if WAS 1-8, WAS takes the better of WAS/PHX. MEM gets the two best of
    {MEM, ORL, third}, CHA the worst, where third = the WAS/PHX pick WAS did not take (PHX if WAS 9-30)."""
    h = {}
    if pos['WAS'] <= 8:
        b, w = sorted(['WAS', 'PHX'], key=lambda t: pos[t])
        h[b] = 'WAS'; third = w
    else:
        h['WAS'] = 'NYK'; third = 'PHX'
    r = sorted(['MEM', 'ORL', third], key=lambda t: pos[t])
    h[r[0]], h[r[1]], h[r[2]] = 'MEM', 'MEM', 'CHA'
    return h


def _pool_okc(pos):
    """OKC most favorable, PHI second, DAL least of OKC/HOU/LAC; HOU's pick top-4 protected."""
    if pos['HOU'] <= 4:
        # HOU keeps its pick. PHI gets the more favorable of OKC/LAC (CBS Philadelphia on the McCain trade).
        # ASSUMPTION: DAL (least-favorable right) gets the other one.
        b, w = sorted(['OKC', 'LAC'], key=lambda t: pos[t])
        return {'HOU': 'HOU', b: 'PHI', w: 'DAL'}
    r = sorted(['OKC', 'HOU', 'LAC'], key=lambda t: pos[t])
    return {r[0]: 'OKC', r[1]: 'PHI', r[2]: 'DAL'}


def _pool_mil_nop(pos):
    b, w = sorted(['MIL', 'NOP'], key=lambda t: pos[t])
    return {b: 'ATL', w: 'MIL'}


# ------------------------------------------------------------------ decomposed form for exact lotteries
def _simple_holder(native, slot):
    if native == 'IND': return 'LAC' if 5 <= slot <= 9 else 'IND'  # protected 1-4 and 10-30
    if native == 'PHI': return 'PHI' if slot <= 4 else 'OKC'
    if native == 'POR': return 'POR' if slot <= 14 else 'CHI'
    return native


POOLS = (('ATL', 'CLE', 'DET', 'MIN', 'SAS', 'UTA'), ('MEM', 'ORL', 'PHX', 'WAS'), ('HOU', 'LAC', 'OKC'),
         ('MIL', 'NOP'))
POOLED = {t for p in POOLS for t in p}


class Router2026:
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

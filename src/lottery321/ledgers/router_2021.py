"""2021 first-round rights ledger (historical, executable routing).

State: after the 2021-03-25 trade deadline (conditions per Hoops Rumors 2021-04-14). route(pos) takes the
final 2021 draft slot of every NATIVE first-round pick (dict team -> 1..30, a permutation) and returns
{slot: holder}. Lower slot = more favorable. Evidence per native pick: ledger_2021_draft.json (same
directory). Out-of-object fallbacks (2022+ carryovers, second-rounders) are recorded there, not routed here.
"""
TEAMS = ('ATL', 'BKN', 'BOS', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL',
         'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'TOR',
         'UTA', 'WAS')

ASSUMPTIONS = [
    "HOU/BKN swap: HOU exercises it at most once, giving up its least favorable eligible pick, and only "
    "when BKN's pick is more favorable (sources say HOU may swap 'any'/'either' of its picks for BKN's "
    "unprotected pick; the choice rule is the value-maximizing literal reading).",
    "HOU/BKN swap eligibility: HOU's step-1 pick (own, or the least favorable of OKC/MIA/HOU), POR's pick "
    "if it conveys (15-30) and DET's pick if it conveys (17-30). MIL's pick (acquired by HOU in March 2021, "
    "after the Harden trade that created the swap) is NOT eligible; sources list only the former.",
    "NYK/LAC swap 'top-four protection' (single source, pick not named): read as LAC's pick being "
    "protected, i.e. no swap when LAC's pick lands 1-4. NYK may swap only its own pick (not DAL's).",
]

# Realized slot -> (deadline holder, pre-draft holder, note).
POST_DEADLINE_CHANGES = {
    16: ('BOS', 'OKC', 'BOS traded its 2021 first (#16) to OKC on 2021-06-18 (Kemba Walker / Al Horford '
                       'trade), after the deadline and before the draft.'),
}


def _simple_holder(native, slot):
    if native == 'DAL': return 'NYK'                            # unprotected
    if native == 'MIL': return 'MIL' if slot <= 9 else 'HOU'    # top-9 protected (swap for HOU 2nd)
    if native == 'UTA': return 'MEM' if 8 <= slot <= 14 else 'UTA'  # protected 1-7 and 15-30
    if native == 'LAL': return 'NOP' if slot <= 7 else 'LAL'    # protected 8-30
    if native == 'MIN': return 'MIN' if slot <= 3 else 'GSW'    # top-3 protected
    if native == 'CHI': return 'CHI' if slot <= 4 else 'ORL'    # top-4 protected
    if native == 'GSW': return 'GSW' if slot <= 20 else 'OKC'   # top-20 protected
    return native


def route(pos):
    if sorted(pos) != sorted(TEAMS) or sorted(pos.values()) != list(range(1, 31)):
        raise ValueError('pos must map all 30 native teams to a permutation of 1..30')
    h = {t: _simple_holder(t, pos[t]) for t in TEAMS if t not in POOLED}

    # --- NYK/LAC swap: NYK takes the more favorable of the two
    # ASSUMPTION: 'top-four protection' protects LAC's pick -> no swap if LAC lands 1-4.
    if pos['LAC'] <= 4:
        h['NYK'], h['LAC'] = 'NYK', 'LAC'
    else:
        b, w = sorted(['NYK', 'LAC'], key=lambda t: pos[t])
        h[b], h[w] = 'NYK', 'LAC'

    # --- Step 1: OKC swap right with HOU (HOU top-4 protected); MIA's pick is owed to OKC unprotected
    if pos['HOU'] <= 4:
        h['HOU'], h['OKC'], h['MIA'] = 'HOU', 'OKC', 'OKC'
        hou_step1 = 'HOU'
    else:
        r = sorted(['OKC', 'MIA', 'HOU'], key=lambda t: pos[t])
        h[r[0]] = h[r[1]] = 'OKC'
        h[r[2]] = 'HOU'
        hou_step1 = r[2]
    # POR top-14 protected, DET top-16 protected, both owed to HOU
    h['POR'] = 'POR' if pos['POR'] <= 14 else 'HOU'
    h['DET'] = 'DET' if pos['DET'] <= 16 else 'HOU'
    h['BKN'] = 'BKN'

    # --- Step 2: HOU may swap one eligible pick for BKN's (unprotected)
    # ASSUMPTION: single swap of HOU's least favorable eligible pick, only if BKN's is more favorable;
    # ASSUMPTION: eligible = step-1 pick + POR/DET if conveyed (MIL's pick excluded).
    eligible = [hou_step1] + [t for t in ('POR', 'DET') if h[t] == 'HOU']
    worst = max(eligible, key=lambda t: pos[t])
    if pos['BKN'] < pos[worst]:
        h['BKN'], h[worst] = 'HOU', 'BKN'

    return {pos[t]: h[t] for t in TEAMS}


POOLS = (('BKN', 'DET', 'HOU', 'MIA', 'OKC', 'POR'), ('LAC', 'NYK'))
POOLED = {t for p in POOLS for t in p}


class Router2021:
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

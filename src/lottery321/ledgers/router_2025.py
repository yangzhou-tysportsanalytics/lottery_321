"""2025 NBA draft first-round rights ledger (historical, executable routing).

State: after the 2024-25 trade deadline (Feb 6, 2025). route(pos) takes the final 2025 draft position of every
NATIVE first-round pick (dict team -> 1..30, a permutation) and returns {position: holder} under the
deadline-state terms. Lower position = more favorable.
Evidence per native: ledger_2025_draft.json (same directory). Sources: Hoops Rumors 2025-03-09 check-in
(https://www.hoopsrumors.com/2025/03/checking-in-on-traded-2025-first-round-picks.html) and the 2024-08-13 list
(https://www.hoopsrumors.com/2024/08/traded-first-round-picks-for-2025-nba-draft.html; appears updated later).
Post-deadline pre-draft trades are NOT applied here; see POST_DEADLINE_CHANGES.
Note: #10 (HOU->PHX, Durant trade), #22 (ATL->BKN, Porzingis trade) and #29 (PHX->CHA) were agreed before the
draft but completed after it; NBA.com lists HOU/ATL/PHX as selecting, which equals the deadline holder, so they
are not listed as changes.
"""
TEAMS = ('ATL', 'BKN', 'BOS', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL',
         'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'TOR',
         'UTA', 'WAS')

ASSUMPTIONS = [
    "Swap rights are exercised if and only if they give the holder a more favorable pick (lower slot).",
    "OKC swap right: OKC may swap its own pick for the LAC pick or the HOU pick; when both are eligible and better "
    "than its own, OKC takes the more favorable one. The team whose pick OKC takes receives OKC's pick.",
    "HOU's 'top-10 protected' on the OKC swap is read as: OKC cannot take HOU's pick if it lands 1-10 "
    "(then OKC can only use the LAC option).",
    "Order: OKC's swap is resolved before HOU's swap with BKN, and HOU's BKN swap applies to whichever pick HOU "
    "holds in place of its own (its own, or OKC's pick received via the OKC swap), per HR Mar 2025. "
    "The HOU/BKN swap for the PHX pick is unprotected.",
]

# slot -> (deadline_holder, draft_holder, note); only for the REALIZED 2025 draft
POST_DEADLINE_CHANGES = {
    16: ('ORL', 'MEM', 'ORL traded its 2025 first to MEM in the Desmond Bane trade (2025-06-15).'),
    23: ('IND', 'NOP', 'IND traded #23 to NOP for its own 2026 first (2025-06-17).'),
}


def route(pos):
    if sorted(pos) != sorted(TEAMS) or sorted(pos.values()) != list(range(1, 31)):
        raise ValueError('pos must map all 30 native teams to a permutation of 1..30')
    h = {t: _simple_holder(t, pos[t]) for t in TEAMS if t not in POOLED}
    h.update(_pool_clemin(pos))
    h.update(_pool_okc_network(pos))
    return {pos[t]: h[t] for t in TEAMS}


def _pool_clemin(pos):
    b, w = sorted(['CLE', 'MIN'], key=lambda t: pos[t])
    return {b: 'UTA', w: 'PHX'}


def _pool_okc_network(pos):
    """OKC swap (vs LAC, or HOU top-10 prot.), then HOU swap with BKN for the PHX pick (BKN holds PHX)."""
    h = {'OKC': 'OKC', 'LAC': 'LAC', 'HOU': 'HOU'}
    # ASSUMPTION: HOU's pick is not eligible for OKC's swap if it lands 1-10
    cands = ['LAC'] + (['HOU'] if pos['HOU'] > 10 else [])
    best = min(cands, key=lambda t: pos[t])  # ASSUMPTION: OKC takes the more favorable eligible pick
    hou_holds = 'HOU'
    if pos[best] < pos['OKC']:
        h[best], h['OKC'] = 'OKC', best
        if best == 'HOU':
            hou_holds = 'OKC'  # ASSUMPTION: HOU's BKN swap then applies to the OKC pick it received
    # HOU swap with BKN for the PHX pick
    if pos['PHX'] < pos[hou_holds]:
        h['PHX'], h[hou_holds] = 'HOU', 'BKN'
    else:
        h['PHX'] = 'BKN'
    return h


# ------------------------------------------------------------------ decomposed form for exact lotteries
def _simple_holder(native, slot):
    if native == 'NYK': return 'BKN'
    if native == 'ATL': return 'SAS'
    if native == 'LAL': return 'ATL'
    if native == 'MIL': return 'NOP' if slot <= 4 else 'BKN'
    if native == 'PHI': return 'PHI' if slot <= 6 else 'OKC'
    if native == 'DET': return 'DET' if slot <= 13 else 'MIN'
    if native == 'CHA': return 'CHA' if slot <= 14 else 'SAC'
    if native == 'MIA': return 'MIA' if slot <= 14 else 'OKC'
    if native == 'WAS': return 'WAS' if slot <= 10 else 'NYK'
    if native == 'DEN': return 'DEN' if slot <= 5 else 'ORL'
    if native == 'UTA': return 'UTA' if slot <= 10 else 'OKC'
    if native == 'POR': return 'POR' if slot <= 14 else 'CHI'
    if native == 'GSW': return 'GSW' if slot <= 10 else 'MIA'
    if native == 'SAC': return 'SAC' if slot <= 12 else 'ATL'
    if native == 'MEM': return 'MEM' if slot <= 14 else 'WAS'
    return native


POOLS = (('CLE', 'MIN'), ('HOU', 'LAC', 'OKC', 'PHX'))
POOLED = {t for p in POOLS for t in p}


class Router2025:
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

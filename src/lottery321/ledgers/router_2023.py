"""2023 first-round rights ledger (executable routing), state after the 2023-02-09 trade deadline.

route(pos) takes the final 2023 draft slot of every NATIVE first-round pick (dict team -> 1..30,
a permutation) and returns {slot: holder}. Lower slot = more favorable.
Evidence (sources, paraphrased terms, realized draft) lives in ledger_2023_draft.json.
Out-of-object fallbacks (future-year picks, second-rounders owed if a pick is kept) are not routed here.
"""
TEAMS = ('ATL', 'BKN', 'BOS', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL',
         'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'TOR',
         'UTA', 'WAS')

ASSUMPTIONS = [
    "LAC/MIL/OKC: swaps are applied sequentially as HR_mar23 describes (OKC first takes the better of the "
    "OKC and LAC picks; HOU may then swap MIL's pick for the pick LAC is left with).",
    "LAC/MIL/OKC: HOU's swap is 'top-six protected' (HR_aug22, Bucks entry). Read literally as applying to "
    "the pick the Clippers hold after OKC's swap, i.e. the less favorable of the OKC/LAC picks: if that "
    "pick is 1-6, HOU cannot swap. This reproduces HR_aug22's Clippers entry (LAC gets the least "
    "favorable of the three, or the second-most favorable if the OKC and LAC picks are both 1-6) except "
    "in one corner case: MIL's pick is more favorable than both and both are 1-6. There the sequential "
    "reading gives LAC the least favorable of the three, not the second-most favorable.",
    "BKN/HOU/PHI: HOU's swap with BKN is applied before BKN's PHI-vs-own choice (equivalent to HR_aug22's "
    "wording: BKN gets PHI's pick if it is the most favorable, otherwise the second-most favorable of the "
    "three; UTA gets the least favorable). No protections on any of the three picks.",
]

# The Porzingis three-team trade (MEM #25 to BOS, then to DET) was agreed pre-draft but NBA.com lists
# Memphis as the selecting team, so the realized holder is recorded as MEM. No routed changes.
POST_DEADLINE_CHANGES = {}


def _protected(p, lo, hi): return lo <= p <= hi


def _simple_holder(native, slot):
    if native == 'DET': return 'DET' if slot <= 18 else 'NYK'
    if native == 'CHA': return 'CHA' if slot <= 16 else 'SAS'
    if native == 'DAL': return 'DAL' if slot <= 10 else 'NYK'
    if native == 'NYK': return 'NYK' if slot <= 14 else 'POR'
    if native == 'CLE': return 'CLE' if slot <= 14 else 'IND'
    if native == 'BOS': return 'BOS' if slot <= 12 else 'IND'
    if native == 'DEN': return 'DEN' if slot <= 14 else 'CHA'
    if native == 'CHI': return 'CHI' if slot <= 4 else 'ORL'
    if native == 'WAS': return 'WAS' if slot <= 14 else 'NYK'
    if native == 'POR': return 'POR' if slot <= 14 else 'CHI'
    if native == 'MIN': return 'UTA'
    if native == 'PHX': return 'BKN'
    return native


POOLS = (('BKN', 'HOU', 'PHI'), ('LAC', 'MIL', 'OKC'), ('LAL', 'NOP'))
POOLED = {t for p in POOLS for t in p}


def route(pos):
    if sorted(pos) != sorted(TEAMS) or sorted(pos.values()) != list(range(1, 31)):
        raise ValueError('pos must map all 30 native teams to a permutation of 1..30')
    h = {t: _simple_holder(t, pos[t]) for t in TEAMS if t not in POOLED}

    # BKN/HOU/PHI: HOU swaps its own pick for BKN's if better (unprotected); BKN then takes the better of
    # the pick it is left with and PHI's; UTA gets the other.
    hb, bl = sorted(['HOU', 'BKN'], key=lambda t: pos[t])
    h[hb] = 'HOU'
    b, w = sorted([bl, 'PHI'], key=lambda t: pos[t])
    h[b], h[w] = 'BKN', 'UTA'

    # LAC/MIL/OKC: OKC takes the better of OKC/LAC (unprotected); HOU (holder of MIL's unprotected pick)
    # may swap MIL's pick for the pick LAC is left with, top-6 protected. LAC gets the remainder.
    ob, lw = sorted(['OKC', 'LAC'], key=lambda t: pos[t])
    h[ob] = 'OKC'
    if _protected(pos[lw], 1, 6):  # ASSUMPTION: protection applies to the post-OKC-swap LAC pick
        h['MIL'], h[lw] = 'HOU', 'LAC'
    else:
        b, w = sorted(['MIL', lw], key=lambda t: pos[t])
        h[b], h[w] = 'HOU', 'LAC'

    # LAL/NOP: unprotected swap held by NOP.
    b, w = sorted(['LAL', 'NOP'], key=lambda t: pos[t])
    h[b], h[w] = 'NOP', 'LAL'

    return {pos[t]: h[t] for t in TEAMS}


class Router2023:
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

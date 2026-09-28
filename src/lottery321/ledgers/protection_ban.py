"""C3 component P: routers with the top-12..15 protections replaced by a compliant alternative.

The 3-2-1 release bans protections in the top-12 to top-15 range on newly traded picks. For the component
decomposition we apply the ban to every such protection in the ledgers (C3 registration, section 2), in two
registered variants, both of which are run and reported:
    'A'  tighten: the native keeps its pick at slots 1..11 and conveys it from 12 on;
    'B'  loosen:  the native keeps its pick at slots 1..16 and conveys it from 17 on.
Conveyances that only apply inside a range (UTA 2021, IND 2026) and protections outside 12..15 are untouched.

AFFECTED lists the native picks whose protection threshold P falls in 12..15, with the holder they convey
to. Three of them sit inside a pool and need the pool logic re-applied with the new threshold: POR 2021 (the
HOU/BKN two-step swap), MIA 2022 (the BKN/HOU/MIA swap) and WAS 2024 (the WAS/PHX/MEM swaps).
"""
import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from teams import TEAMS  # noqa: E402

VARIANTS = {'A': 11, 'B': 16}

# year -> {native: (threshold P, kind)}; kind 'simple' or 'pool'
AFFECTED = {
    2021: {'POR': (14, 'pool')},        # POR sits inside the HOU/BKN two-step swap
    2022: {'CLE': (14, 'simple'), 'OKC': (14, 'simple'), 'POR': (14, 'simple'), 'TOR': (14, 'simple'),
           'PHX': (12, 'simple'), 'MIA': (14, 'pool')},
    2023: {'CLE': (14, 'simple'), 'DEN': (14, 'simple'), 'NYK': (14, 'simple'), 'POR': (14, 'simple'),
           'WAS': (14, 'simple'), 'BOS': (12, 'simple')},
    2024: {'CHA': (14, 'simple'), 'POR': (14, 'simple'), 'SAC': (14, 'simple'), 'WAS': (12, 'pool')},
    2025: {'CHA': (14, 'simple'), 'MEM': (14, 'simple'), 'MIA': (14, 'simple'), 'POR': (14, 'simple'),
           'DET': (13, 'simple'), 'SAC': (12, 'simple')},
    2026: {'POR': (14, 'simple')},
}


def base(year):
    return importlib.import_module(f'router_{year}')


def _simple_ban(year, variant):
    """New simple-holder function with the affected thresholds moved to the variant's slot."""
    mod = base(year); new_p = VARIANTS[variant]
    rules = {}
    for nat, (p, kind) in AFFECTED[year].items():
        if kind != 'simple':
            continue
        keep = mod._simple_holder(nat, p)          # holder when protected (the native itself)
        conveyed = mod._simple_holder(nat, p + 1)  # holder when the pick conveys
        if keep != nat:
            raise ValueError(f'{year} {nat}: protection does not keep the pick with the native')
        rules[nat] = (new_p, conveyed)

    def holder(native, slot):
        if native in rules:
            lim, conveyed = rules[native]
            return native if slot <= lim else conveyed
        return mod._simple_holder(native, slot)
    return holder


def _route_2021_ban(pos, p):
    """Full 2021 route with the POR protection at top-`p` (POR sits inside the HOU/BKN pool, so the whole
    two-step swap has to be replayed; mirrors router_2021.route)."""
    mod = base(2021)
    h = {t: mod._simple_holder(t, pos[t]) for t in TEAMS if t not in mod.POOLED}
    if pos['LAC'] <= 4:
        h['NYK'], h['LAC'] = 'NYK', 'LAC'
    else:
        b, w = sorted(['NYK', 'LAC'], key=lambda t: pos[t])
        h[b], h[w] = 'NYK', 'LAC'
    if pos['HOU'] <= 4:
        h['HOU'], h['OKC'], h['MIA'] = 'HOU', 'OKC', 'OKC'
        hou_step1 = 'HOU'
    else:
        r = sorted(['OKC', 'MIA', 'HOU'], key=lambda t: pos[t])
        h[r[0]] = h[r[1]] = 'OKC'
        h[r[2]] = 'HOU'
        hou_step1 = r[2]
    h['POR'] = 'POR' if pos['POR'] <= p else 'HOU'          # <- the banned protection
    h['DET'] = 'DET' if pos['DET'] <= 16 else 'HOU'
    h['BKN'] = 'BKN'
    eligible = [hou_step1] + [t for t in ('POR', 'DET') if h[t] == 'HOU']
    worst = max(eligible, key=lambda t: pos[t])
    if pos['BKN'] < pos[worst]:
        h['BKN'], h[worst] = 'HOU', 'BKN'
    return {pos[t]: h[t] for t in TEAMS}


def _pool_2022_ban(pos, p):
    """BKN/HOU/MIA with the MIA protection at top-`p`."""
    if pos['MIA'] <= p:
        return {'BKN': 'HOU', 'HOU': 'HOU', 'MIA': 'MIA'}
    r = sorted(['BKN', 'HOU', 'MIA'], key=lambda t: pos[t])
    return {r[0]: 'HOU', r[1]: 'HOU', r[2]: 'MIA'}


def _pool_2024_ban(pos, p):
    """WAS/PHX/MEM with the WAS protection at top-`p` (same logic as router_2024._pool_wpm)."""
    h = {}
    if pos['WAS'] <= p:
        b, w = sorted(['WAS', 'PHX'], key=lambda t: pos[t])
        h[b], h[w] = 'WAS', 'PHX'
        if pos[w] < pos['MEM']:
            h[w], h['MEM'] = 'MEM', 'PHX'
        else:
            h['MEM'] = 'MEM'
    else:
        h['WAS'] = 'NYK'
        if pos['PHX'] < pos['MEM']:
            h['PHX'], h['MEM'] = 'MEM', 'PHX'
        else:
            h['PHX'], h['MEM'] = 'PHX', 'MEM'
    return h


def make_router(year, variant):
    """Router object (simple_natives / pools / simple / pooled / route) for the ban variant."""
    mod = base(year); new_p = VARIANTS[variant]
    holder = _simple_ban(year, variant)
    POOLS = mod.POOLS
    POOLED = mod.POOLED
    # natives whose banned protection sits inside a pool, so the pool logic must be replayed
    in_pool = {n for n in AFFECTED[year] if n in POOLED}
    if in_pool and year not in (2021, 2022, 2024):
        raise ValueError(f'{year}: pool-level ban not implemented for {sorted(in_pool)}')

    def route(pos):
        if sorted(pos) != sorted(TEAMS) or sorted(pos.values()) != list(range(1, 31)):
            raise ValueError('pos must map all 30 native teams to a permutation of 1..30')
        if year == 2021:
            return _route_2021_ban(pos, new_p)
        h = {t: holder(t, pos[t]) for t in TEAMS if t not in POOLED}
        if year == 2022:
            h.update(_pool_2022_ban(pos, new_p))
        elif year == 2024:
            h.update(_pool_2024_ban(pos, new_p))
            h.update(mod._pool_okc(pos))
            h.update(mod._pool_milnop(pos))
        else:                                      # pools without an affected protection: unchanged
            full = mod.route(pos)
            for t in POOLED:
                h[t] = full[pos[t]]
        return {pos[t]: h[t] for t in TEAMS}

    class Router:
        simple_natives = tuple(t for t in TEAMS if t not in POOLED)
        pools = POOLS
        ban_variant = variant
        ban_year = year

        @staticmethod
        def simple(native, slot):
            return holder(native, slot)

        @staticmethod
        def pooled(p):
            full = {t: p[t] for t in POOLED}
            others = [s for s in range(1, 31) if s not in full.values()]
            filler = [t for t in TEAMS if t not in POOLED]
            full.update(dict(zip(filler, others)))
            out = route(full)
            return {full[t]: out[full[t]] for t in POOLED}

    Router.route = staticmethod(route)
    Router.__name__ = f'Router{year}Ban{variant}'
    return Router


def affected_count():
    return sum(len(v) for v in AFFECTED.values())

# Historical first-round rights ledger — schema (one JSON file per draft year)

File: ledger_<YEAR>_draft.json
{
  "draft_year": 2023,
  "season": "2022-23",
  "state_as_of": "after the trade deadline (the late-season window is after the deadline)",
  "sources": [{"id": "HR_apr", "title": "...", "url": "...", "date": "YYYY-MM-DD", "role": "conditions"},
              {"id": "NBA_results", "title": "...", "url": "...", "role": "realized holders"}],
  "natives": {                      # all 30 teams, keyed by native team code (ATL BKN BOS CHA CHI CLE DAL DEN DET GSW
                                    # HOU IND LAC LAL MEM MIA MIL MIN NOP NYK OKC ORL PHI PHX POR SAC SAS TOR UTA WAS)
    "ATL": {"rule": {...}, "sources": ["HR_apr"], "text": "short paraphrase of the condition", "confidence": "high|medium|low"}
  },
  "realized": {                     # the actual 2023 draft, picks 1-30: who PICKED at each slot and whose native pick it was
    "1": {"native": "SAS", "holder": "SAS"}, "...": {}
  },
  "forfeited": ["..."],             # natives whose first-round pick was forfeited (e.g. league penalty), if any
  "open_issues": ["anything ambiguous, conflicting between sources, or not expressible in the rule grammar"]
}

Rule grammar (slot = the native pick's final draft slot 1..30):
  {"type": "own"}                                            native keeps it
  {"type": "to", "holder": "X"}                              unconditionally conveyed to X (after any chain of trades,
                                                             give the FINAL holder at the deadline)
  {"type": "protected", "keep": [[1, 4]], "else": "X"}       native keeps if slot in any listed range, else X gets it
  {"type": "reverse", "to_if": [[1, 16]], "holder": "X"}     X gets it if slot in range, else native keeps
  {"type": "pool", "members": ["MIL", "NOP"],                picks of the listed natives are sorted from most to least
   "allocation": [{"holder": "NOP", "rank": 1},              favorable (lower slot = better); holder with rank r gets the
                  {"holder": "ATL", "rank": 2}],             r-th best. Use for swaps ("X gets the better of A and B")
   "conditions": ["free text for any clause the ranks       and multi-team pools. Put the SAME pool object under every
                   cannot express, e.g. 'if both in top 4,   member native. If a pool member's pick is itself protected
                   NOP keeps both'"]}                        before entering the pool, say so in conditions.
  {"type": "forfeited"}                                      pick forfeited, no one selects with it
If a rule cannot be expressed, use the closest form, set confidence "low", and explain in open_issues.

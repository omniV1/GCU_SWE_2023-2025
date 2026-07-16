# Spaced Repetition Redo Rules

Use this with your mistake log after every solve attempt.

## Redo cadence
- Redo 1: +1 day
- Redo 2: +3 days
- Redo 3: +7 days
- Redo 4: +14 days

## How to log misses
1. Add one row per missed problem in `mistake_log_template.csv`.
2. Set `next_redo_date` to the nearest scheduled date.
3. Use `miss_type` from this shortlist:
   - pattern_misread
   - edge_case_missed
   - complexity_too_high
   - implementation_bug
   - communication_gap

## Redo scoring
- `pass_fast`: solved inside target interview time.
- `pass_slow`: solved correctly but too slowly.
- `fail`: still stuck or incorrect.

If a redo result is `fail`, restart the cadence from +1 day.

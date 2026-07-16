# Weekly Retrospective Playbook

Run this every week on your light/review day.

## Inputs
- `logs/mistake_log_template.csv`
- `logs/kpi_tracker_template.csv`
- latest two `mocks/mock_scorecard.md` entries

## KPI definitions
- **Solve rate** = solved problems / attempted problems.
- **Median solve time** = median minutes on medium attempts.
- **First-try pass rate** = first submissions accepted / total submissions.
- **Explanation clarity** = average mock score (0-5 scale).

## Weekly review checklist
1. Fill this week's KPI row in `kpi_tracker_template.csv`.
2. Count miss types from the mistake log.
3. Pick one dominant failure mode.
4. Choose next week's pattern focus based on that failure mode.
5. Schedule 2 targeted redo blocks for that pattern.

## Adjustment rules
- If solve rate < 60%: reduce new problems, increase re-solves by 50%.
- If median solve time > 35 min: enforce stricter 5-minute design cap.
- If first-try pass rate < 70%: add explicit edge-case checklist before code run.
- If explanation clarity < 4/5: require 10-minute verbal recap after every solve.

## Reflection prompt (write 3-5 bullets)
- What improved this week?
- What repeatedly failed?
- Which pattern is still not automatic?
- What single change has the highest leverage for next week?

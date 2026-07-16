# 7-Day OA Execution Calendar (Pass-Focused)

This is a no-guesswork plan for the next 7 days.

## Daily pass criteria
- Solve at least 4 variants/day.
- At least 70% asserts passing by end of day.
- One no-autocomplete timed rep/day.
- Log misses immediately in `interview_prep/logs/mistake_log_template.csv`.

## Day 1 (Hashing + Sliding Window)
- Block A (90 min): `coding/01_hashing_variants.py`
- Block B (90 min): `coding/02_sliding_window_variants.py`
- Timer rule: 30 min max per variant, 10 min review after each.
- Must-pass edge cases:
  - empty input
  - duplicates / repeated chars
  - single element

## Day 2 (Intervals + Greedy)
- Block A (90 min): `coding/03_intervals_greedy_variants.py` v1/v2
- Block B (60 min): same file v3 + re-solve yesterday's weakest variant
- Timer rule: 35 min max for v2 (harder), 20 min review.
- Must-pass edge cases:
  - touching intervals like `[1,4]` and `[4,5]`
  - full overlap duplicates
  - empty intervals

## Day 3 (Graphs / Grid BFS-DFS)
- Block A (90 min): `coding/04_graph_grid_variants.py` v1/v2
- Block B (60 min): v3 + one re-solve from Day 1 or 2
- Timer rule: draw neighbor logic before coding (2 min max).
- Must-pass edge cases:
  - 1x1 grid
  - blocked start/end
  - disconnected regions

## Day 4 (Heap + Binary Search on Answer)
- Block A (90 min): `coding/05_heap_binary_search_variants.py` v1/v2
- Block B (60 min): v3 + one re-solve from previous misses
- Timer rule: write monotonic condition before binary search loop.
- Must-pass edge cases:
  - `k=1`
  - all same values
  - large pile + tight hour limit

## Day 5 (Amazon Story Wrappers)
- Block A (90 min): `coding/06_amazon_style_story_variants.py` v1/v2
- Block B (60 min): v3 + one story-to-pattern translation drill
- Timer rule: spend first 2 minutes naming underlying pattern out loud.
- Must-pass edge cases:
  - tie-break sorting
  - zero inventory
  - empty request/task lists

## Day 6 (Full Mock OA Day)
- Mock format (total ~90 min):
  - Problem 1: pick one unsolved variant from Days 1-3 (35 min)
  - Problem 2: pick one unsolved variant from Days 4-5 (35 min)
  - 20 min: postmortem and re-solve failed test paths
- No autocomplete for full mock.
- Fill `interview_prep/mocks/mock_scorecard.md`.

## Day 7 (Final polish + Django sprint)
- Block A (60 min): re-solve top 3 misses with no notes.
- Block B (60 min): `django/django_rapid_fire_qa.md` verbal answers.
- Block C (45 min): one prompt from `django/django_code_prompts.md`.
- Block D (30 min): run confidence set:
  - one hashing variant
  - one sliding-window variant
  - one graph/heap variant

## Day 7 stop rule
- Stop heavy prep at least 10-12 hours before OA.
- Final hour: review pattern triggers and complexity cheats only.

## Run command
Use this command anytime to run all coding packs:
`python interview_prep/amazon_oa_week/coding/run_amazon_oa_week.py`

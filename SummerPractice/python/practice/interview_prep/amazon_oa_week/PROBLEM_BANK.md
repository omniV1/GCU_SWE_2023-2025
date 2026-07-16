# Amazon Problem Bank

## Easiest way (NeetCode / LeetCode-style lab)
```bash
cd SummerPractice/python/practice/amazon_lab
python serve.py
```
Opens **http://127.0.0.1:8765** — roadmap by pattern, editor, Submit tests, timer, progress toward a top-100 bank.

- Roadmap: Arrays & Hashing → Two Pointers → … (NeetCode order, Amazon-weighted)
- Each problem: YOU ALREADY KNOW / WHAT'S NEW / TRACE + interview line
- Expand bank: edit `amazon_lab/seed_problems.py`, run `python seed_problems.py`

Legacy single-file UI (still works): [`../amazon_interview_lab.html`](../amazon_interview_lab.html)

## Pattern ladder (Python files)
`coding/hash_pattern_lab.py` — progressive Hash Lab (L0→L5)

| Lesson | Upgrade |
|--------|---------|
| L0 | set vs dict demos |
| L1 | Contains Duplicate — set membership |
| L2 | Two Sum — same scan, complement + index dict |
| L3 | Group Anagrams — signature key → list bucket |
| L4 | Top K Frequent — count then rank |
| L5 | Subarray Sum K — Two Sum on prefix sums |
| LQ | Closing quiz |

```bash
python interview_prep/amazon_oa_week/coding/hash_pattern_lab.py L0
python interview_prep/amazon_oa_week/coding/hash_pattern_lab.py L1
```

Answer key: `coding/hash_pattern_lab_worked.py`

## After the lab — Amazon mixed drills
`coding/07_amazon_common_problems.py` — timed reps
`coding/08_amazon_hard_problems.py` — harder stretch

## Rule
UI lab or Python ladder first. `07` is interview pace, not first-time learning.

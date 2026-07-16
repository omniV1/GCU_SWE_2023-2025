# Amazon Lab (NeetCode-style)

Local LeetCode-like trainer for Amazon OA / phone / loop prep.

## Start
```bash
cd SummerPractice/python/practice/amazon_lab
python seed_problems.py   # first time / when adding problems
python serve.py
```

Browser opens at **http://127.0.0.1:8765**

## Features
- NeetCode **roadmap** by pattern category
- Progressive **YOU ALREADY KNOW / WHAT'S NEW** bridges
- In-browser Python (Pyodide) Run + Submit
- 35-min interview timer + protocol modal
- Progress saved in localStorage
- Data-driven bank in `data/problems.json` (easy to grow toward 100+)

## Expand the bank
1. Edit `seed_problems.py` — add another `P(...)` entry
2. Add NeetCode-style samples in `neetcode_examples.py` + Python **code walkthroughs** in `code_walks.py`
3. Run `python seed_problems.py`
4. Refresh the browser

## Layout
```
amazon_lab/
  serve.py              # local server
  seed_problems.py      # generates problems.json
  data/problems.json    # problem bank
  static/index.html
  static/app.js
  static/styles.css
```

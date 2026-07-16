"""
Amazon Common Problems — NeetCode-style roadmap (PRACTICE)
=========================================================

HOW TO USE
----------
*** LEARN HASHING FIRST (pattern ladder) ***
       python hash_pattern_lab.py L0
       python hash_pattern_lab.py L1
  ... up through L5 + LQ. That file STACKS each lesson on the last.

This file (07) is the AMAZON MIXED DRILL after the lab clicks —
timed reps, not the place you first learn the pattern.

  1. Pick ONE problem code (C01, C02, ...).
  2. Fill the function from its STEPS.
  3. Test ONLY that problem:
       python 07_amazon_common_problems.py C01
  4. Progress check:
       python 07_amazon_common_problems.py

Stuck > 15 min?
       For hashing: hash_pattern_lab_worked.py
       For this file: 07_amazon_common_problems_worked.py


ROADMAP (do top → bottom)
-------------------------
  [0] hash_pattern_lab.py   L0→L5   ← do this first
  [1] Arrays & Hashing      C01 → C02 → C03 → C11
  [2] Sliding Window        C04 → C05
  [3] Stack                 C09
  [4] Intervals             C06
  [5] Graphs / BFS-DFS      C07 → C08 → C12
  [6] One-pass greedy       C10
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from typing import List


# #############################################################################
#  PATTERN: Arrays & Hashing
#  When: "seen before?", pairs, frequency, group-by-key, anagrams
#  Tool: dict / set / Counter
# #############################################################################


# --- C01 Two Sum (LC 1) ------------------------------------------------------
"""
PROBLEM: indices of two nums that add to target. One solution. No reuse.

EXAMPLE: [2,7,11,15], target=9 → [0,1]

INTUITION:
  Remember everything you've already walked past in a dict: value → index.
  At nums[i], ask: "have I already seen (target - nums[i])?"
  Yes → return both indices. No → store nums[i] and keep walking.

STEPS:
  1. seen = {}
  2. for i, num in enumerate(nums):
  3.     need = target - num
  4.     if need in seen: return [seen[need], i]
  5.     seen[num] = i

TIME O(n)  SPACE O(n)
"""


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []

# --- C02 Group Anagrams (LC 49) ----------------------------------------------
"""
PROBLEM: group words that use the exact same letters.

EXAMPLE: ["eat","tea","tan","ate","nat","bat"]
  → groups like [["eat","tea","ate"],["tan","nat"],["bat"]]

INTUITION:
  Anagrams share the same sorted letters.
  "eat" and "tea" both become key "aet".
  Bucket words in a dict keyed by that signature.

STEPS:
  1. groups = defaultdict(list)
  2. for word in strs:
  3.     key = "".join(sorted(word))
  4.     groups[key].append(word)
  5. return list(groups.values())

TIME O(n * k log k)  SPACE O(n*k)
"""


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


# --- C03 Top K Frequent (LC 347) ---------------------------------------------
"""
PROBLEM: return the k most common numbers (any order).

EXAMPLE: [1,1,1,2,2,3], k=2 → [1,2]

INTUITION:
  Count frequencies. Sort unique values by count (high→low). Take first k.

STEPS:
  1. freq = Counter(nums)
  2. ranked = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
  3. return ranked[:k]

TIME O(n + u log u)  SPACE O(u)
"""


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)
    # >>> YOU: sort keys by freq descending, return first k
    pass


# --- C11 Subarray Sum Equals K (LC 560) --------------------------------------
"""
PROBLEM: count contiguous subarrays that sum to k.

EXAMPLE: [1,1,1], k=2 → 2

INTUITION:
  prefix = running sum.
  If (prefix - k) was an earlier prefix, the middle chunk sums to k.
  Keep a dict: how many times each prefix value has appeared. Start with {0:1}.

STEPS:
  1. seen = {0: 1}; prefix = 0; ans = 0
  2. for num in nums:
  3.     prefix += num
  4.     ans += seen.get(prefix - k, 0)
  5.     seen[prefix] = seen.get(prefix, 0) + 1
  6. return ans

TIME O(n)  SPACE O(n)
"""


def subarray_sum(nums: List[int], k: int) -> int:
    seen = {0: 1}
    prefix = 0
    ans = 0
    for num in nums:
        prefix += num
        # >>> YOU: add how many times (prefix - k) has been seen
        # >>> YOU: then record this prefix in seen
        pass
    return ans


# #############################################################################
#  PATTERN: Sliding Window
#  When: contiguous subarray/substring, longest/shortest under a rule
#  Invariant: everything in [left, right] is valid
# #############################################################################


# --- C04 Longest Substring Without Repeating (LC 3) --------------------------
"""
PROBLEM: longest substring with all unique chars → return LENGTH.

EXAMPLE: "abcabcbb" → 3

INTUITION:
  Grow right. If new char is already inside the window, move left until
  that char is gone. Track max window length.

STEPS:
  1. left=0; best=0; window=set()
  2. for right, ch in enumerate(s):
  3.     while ch in window: remove s[left]; left += 1
  4.     add ch; best = max(best, right-left+1)
  5. return best

TIME O(n)  SPACE O(alphabet)
"""


def length_of_longest_substring(s: str) -> int:
    left = 0
    best = 0
    window = set()
    for right, ch in enumerate(s):
        # >>> YOU: while ch in window, shrink from left
        # >>> YOU: add ch, update best
        pass
    return best


# --- C05 Min Size Subarray Sum (LC 209) --------------------------------------
"""
PROBLEM: shortest contiguous subarray with sum >= target (nums > 0). Else 0.

EXAMPLE: target=7, [2,3,1,2,4,3] → 2

INTUITION:
  Expand right (add). While sum >= target, record length and shrink left.

STEPS:
  1. left=0; total=0; best=inf
  2. for right, num in enumerate(nums):
  3.     total += num
  4.     while total >= target:
  5.         best = min(best, right-left+1)
  6.         total -= nums[left]; left += 1
  7. return 0 if best==inf else best

TIME O(n)  SPACE O(1)
"""


def min_subarray_len(target: int, nums: List[int]) -> int:
    left = 0
    total = 0
    best = float("inf")
    for right, num in enumerate(nums):
        total += num
        # >>> YOU: while total >= target, update best and shrink left
        pass
    return 0 if best == float("inf") else best


# #############################################################################
#  PATTERN: Stack
#  When: matching / nesting / most-recent unmatched
# #############################################################################


# --- C09 Valid Parentheses (LC 20) -------------------------------------------
"""
PROBLEM: is "()[]{}"-style string valid?

EXAMPLE: "([])" → True   "(]" → False

INTUITION:
  Openers go on a stack. A closer MUST match the top opener. Stack empty at end.

STEPS:
  1. pairs = {')':'(', ']':'[', '}':'{'}
  2. stack = []
  3. for ch in s:
  4.     if opener: push
  5.     else: if empty or pop() != pairs[ch]: return False
  6. return stack empty

TIME O(n)  SPACE O(n)
"""


def is_valid_parentheses(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        # >>> YOU: push openers; on closer check match with pop
        pass
    return len(stack) == 0


# #############################################################################
#  PATTERN: Intervals
#  When: overlapping ranges. Usually sort by start, then scan.
# #############################################################################


# --- C06 Merge Intervals (LC 56) ---------------------------------------------
"""
PROBLEM: merge overlapping intervals.

EXAMPLE: [[1,3],[2,6],[8,10]] → [[1,6],[8,10]]

INTUITION:
  Sort by start. If next.start <= current.end → overlap → extend end.
  Else start a new merged interval.

STEPS:
  1. sort by start
  2. merged = [first]
  3. for each next:
  4.     if next.start <= merged[-1].end: extend end
  5.     else append next
  6. return merged

TIME O(n log n)  SPACE O(n)
"""


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0][:]]
    for start, end in intervals[1:]:
        # >>> YOU: overlap → extend merged[-1][1]; else append [start,end]
        pass
    return merged


# #############################################################################
#  PATTERN: Graphs / Grids (DFS / BFS)
#  When: islands, connected components, unweighted shortest path
# #############################################################################


# --- C07 Number of Islands (LC 200) ------------------------------------------
"""
PROBLEM: count '1'-islands (4-directional).

INTUITION:
  Every fresh '1' starts an island. DFS/BFS sinks the whole island so you
  don't double-count.

STEPS:
  1. islands = 0
  2. for each cell if '1': islands += 1; dfs to mark visited
  3. dfs: if OOB or not '1' return; set '0'; recurse 4 dirs

TIME O(mn)  SPACE O(mn)
"""


def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> None:
        # >>> YOU: base cases; mark visited; recurse 4 neighbors
        pass

    islands = 0
    for r in range(rows):
        for c in range(cols):
            # >>> YOU: if land, count++ and dfs
            pass
    return islands


# --- C08 Rotting Oranges (LC 994) --------------------------------------------
"""
PROBLEM: minutes until all fresh rot. Impossible → -1.
  0 empty, 1 fresh, 2 rotten. Rot spreads to 4-adj each minute.

INTUITION:
  Multi-source BFS: queue ALL initial rotten. Each queue layer = 1 minute.

STEPS:
  1. count fresh; enqueue all rotten
  2. while queue and fresh > 0:
  3.     process one full layer; infect neighbors; minutes += 1
  4. return minutes if fresh==0 else -1

TIME O(mn)  SPACE O(mn)
"""


def oranges_rotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # >>> YOU: BFS by layers until fresh==0 or queue empty
    pass
    return minutes if fresh == 0 else -1


# --- C12 Course Schedule (LC 207) --------------------------------------------
"""
PROBLEM: can you finish all courses given prereqs [a,b] = "b before a"?

INTUITION:
  Directed graph. Cycle → impossible.
  Kahn/BFS: repeatedly take courses with indegree 0.

STEPS:
  1. build graph b→a; indegree[a]++
  2. queue all indegree 0
  3. pop; taken++; reduce neighbor indegrees; enqueue new zeros
  4. return taken == num_courses

TIME O(V+E)  SPACE O(V+E)
"""


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    indegree = [0] * num_courses
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1

    q = deque([i for i in range(num_courses) if indegree[i] == 0])
    taken = 0
    # >>> YOU: BFS topo; count how many courses you can take
    pass
    return taken == num_courses


# #############################################################################
#  PATTERN: One-pass running state
#  When: best answer while scanning once; track a running min/max
# #############################################################################


# --- C10 Best Time Buy/Sell Stock (LC 121) -----------------------------------
"""
PROBLEM: one buy + one later sell. Max profit (or 0).

EXAMPLE: [7,1,5,3,6,4] → 5

INTUITION:
  Remember cheapest price so far. Profit if selling today = price - min_so_far.

STEPS:
  1. min_price = inf; best = 0
  2. for price: update min_price; update best with price-min_price
  3. return best

TIME O(n)  SPACE O(1)
"""


def max_profit(prices: List[int]) -> int:
    min_price = float("inf")
    best = 0
    for price in prices:
        # >>> YOU: update min_price and best
        pass
    return best


# =============================================================================
# TESTS — learn one problem at a time (this will NOT scream at unfinished ones)
# =============================================================================
import sys


def _sorted_groups(groups: List[List[str]]) -> List[List[str]]:
    return sorted([sorted(g) for g in groups])


def _test_C01() -> None:
    assert set(two_sum([2, 7, 11, 15], 9)) == {0, 1}
    assert set(two_sum([3, 2, 4], 6)) == {1, 2}
    assert set(two_sum([3, 3], 6)) == {0, 1}


def _test_C02() -> None:
    assert _sorted_groups(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == _sorted_groups(
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    )
    assert _sorted_groups(group_anagrams([""])) == [[""]]
    assert _sorted_groups(group_anagrams(["a"])) == [["a"]]


def _test_C03() -> None:
    assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert top_k_frequent([1], 1) == [1]


def _test_C04() -> None:
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0


def _test_C05() -> None:
    assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2
    assert min_subarray_len(4, [1, 4, 4]) == 1
    assert min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0


def _test_C06() -> None:
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge_intervals([[1, 4], [0, 4]]) == [[0, 4]]


def _test_C07() -> None:
    g1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert num_islands([row[:] for row in g1]) == 1
    g2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert num_islands([row[:] for row in g2]) == 3
    assert num_islands([["0"]]) == 0


def _test_C08() -> None:
    assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert oranges_rotting([[0, 2]]) == 0


def _test_C09() -> None:
    assert is_valid_parentheses("()") is True
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("(]") is False
    assert is_valid_parentheses("([])") is True
    assert is_valid_parentheses("{[()]}") is True


def _test_C10() -> None:
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([1]) == 0


def _test_C11() -> None:
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
    assert subarray_sum([1], 0) == 0


def _test_C12() -> None:
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    assert can_finish(1, []) is True


TESTS = {
    "C01": ("Two Sum", _test_C01),
    "C02": ("Group Anagrams", _test_C02),
    "C03": ("Top K Frequent", _test_C03),
    "C04": ("Longest Substring No Repeat", _test_C04),
    "C05": ("Min Size Subarray Sum", _test_C05),
    "C06": ("Merge Intervals", _test_C06),
    "C07": ("Number of Islands", _test_C07),
    "C08": ("Rotting Oranges", _test_C08),
    "C09": ("Valid Parentheses", _test_C09),
    "C10": ("Best Time Buy/Sell Stock", _test_C10),
    "C11": ("Subarray Sum Equals K", _test_C11),
    "C12": ("Course Schedule", _test_C12),
}


def _run_one(code: str) -> str:
    name, fn = TESTS[code]
    try:
        fn()
        print(f"  PASS  {code}  {name}")
        return "pass"
    except Exception as exc:
        # unfinished / wrong — tell you which one, don't nuke the whole run
        short = str(exc).split("\n")[0] if str(exc) else type(exc).__name__
        print(f"  ----  {code}  {name}  (not passing yet: {type(exc).__name__})")
        if short and short != "False":
            print(f"        tip: re-read STEPS under {code}, or run: python 07_amazon_common_problems.py {code}")
        return "fail"


if __name__ == "__main__":
    args = [a.upper() for a in sys.argv[1:]]
    if args and args[0] in ("-H", "--HELP", "HELP"):
        print("Usage:")
        print("  python 07_amazon_common_problems.py C01   # test ONE problem")
        print("  python 07_amazon_common_problems.py       # progress report card")
        raise SystemExit(0)

    if args:
        # Test only what you asked for — this is how you learn
        unknown = [a for a in args if a not in TESTS]
        if unknown:
            print(f"Unknown code(s): {unknown}. Pick from: {', '.join(TESTS)}")
            raise SystemExit(1)
        print("Testing:")
        results = [_run_one(code) for code in args]
        if all(r == "pass" for r in results):
            print("\nNice. That one is locked in. Go to the next code.")
            raise SystemExit(0)
        print("\nNot quite — stay on this problem. STEPS are above the function.")
        raise SystemExit(1)

    # Full report card: never aborts on first fail
    print("Progress (unfinished = normal, keep going one at a time):\n")
    passed = 0
    for code in TESTS:
        if _run_one(code) == "pass":
            passed += 1
    print(f"\n{passed}/{len(TESTS)} passing.")
    if passed < len(TESTS):
        # hint the first failing one
        for code, (name, fn) in TESTS.items():
            try:
                fn()
            except Exception:
                print(f"Next up: {code} ({name})")
                print(f"  python 07_amazon_common_problems.py {code}")
                break
    else:
        print("Roadmap complete. Move to 08_amazon_hard_problems.py")

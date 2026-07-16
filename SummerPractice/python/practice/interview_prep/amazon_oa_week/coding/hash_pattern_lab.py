"""
HASH PATTERN LAB — Progressive ladder (learn hashing BEFORE Amazon mixed drills)
================================================================================

Each lesson UPGRADES the previous one. Do NOT skip.

  L0  Tools (set + dict)          — read only, run demos
  L1  Contains Duplicate          — set: "have I seen this value?"
  L2  Two Sum                     — dict stores INDEX + ask for complement
  L3  Group Anagrams              — dict key = signature; value = list bucket
  L4  Top K Frequent              — dict COUNTS; then rank keys
  L5  Subarray Sum Equals K       — Two Sum idea on PREFIX sums

HOW TO USE
----------
  1. Start at L0. Read it. Run:  python hash_pattern_lab.py L0
  2. Fill the next lesson. Test ONLY that lesson:
         python hash_pattern_lab.py L1
  3. When PASS, go to the next lesson. Progress report:
         python hash_pattern_lab.py

Stuck > 15 min on ONE lesson?
  Open hash_pattern_lab_worked.py for that function only. Close it. Retype.

AFTER this lab is green: use 07_amazon_common_problems.py as timed Amazon reps
(not as the place you learn hashing).
"""

from __future__ import annotations

from re import I
import sys
from collections import Counter, defaultdict
from typing import List


# #############################################################################
# L0 — THE TOOLS (no blank to fill — just run and understand)
# #############################################################################
"""
GOAL OF THIS WHOLE LAB
  Learn ONE family of tricks: look stuff up in O(1) while you scan once.

TWO BOXES
  set  = "have I seen this thing?"          (yes / no)
  dict = "have I seen this thing → WHAT?"   (value stores extra info)

RUN THIS LESSON:
  python hash_pattern_lab.py L0
"""


def demo_set_and_dict() -> None:
    """Interactive teaching demos. No return value — just prints."""
    print("--- SET: membership only ---")
    seen = set()
    for x in [3, 1, 3, 2]:
        if x in seen:
            print(f"  {x} already in set -> DUPLICATE")
        else:
            seen.add(x)
            print(f"  add {x}; set now = {seen}")

    print("\n--- DICT: membership + payload ---")
    # same scan idea, but we store the INDEX of each value
    index_of = {}
    nums = [2, 7, 11]
    for i, x in enumerate(nums):
        index_of[x] = i
        print(f"  saw value {x} at index {i}; dict = {index_of}")

    print("\n--- COMPLEMENT (the Two Sum / Subarray Sum trick) ---")
    target = 9
    for i, x in enumerate([2, 7, 11]):
        need = target - x
        print(f"  at {x}, need {need}. In dict? {need in index_of}")


# #############################################################################
# L1 — Contains Duplicate
# #############################################################################
"""
YOU ALREADY KNOW (from L0)
  A set answers "have I seen this?" in O(1).

WHAT'S NEW
  Turn that into a function: walk the array once; if a value is already in
  the set → True. Else add it. If you finish → False.

TRACE  nums = [1, 2, 3, 1]
  i=0 num=1  set={}      1 not in set → add → {1}
  i=1 num=2  set={1}     2 not in set → add → {1,2}
  i=2 num=3  set={1,2}   3 not in set → add → {1,2,3}
  i=3 num=1  set={1,2,3} 1 IS in set  → return True

TEMPLATE (same shape every hashing scan):
  box = set()
  for x in nums:
      if x already in box: return True
      put x in box
  return False
"""


def contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
       


# #############################################################################
# L2 — Two Sum
# #############################################################################
"""
YOU ALREADY KNOW (from L1)
  Same one-pass scan. "Have I seen this before?" with a set.

WHAT'S NEW (ONE upgrade)
  1) Use a dict instead of a set, so you can store the INDEX of each value.
  2) Don't ask "have I seen this num?" — ask "have I seen the COMPLEMENT?"
       need = target - num
       if need is already in the dict → return [its index, my index]

  Same walk. Richer question. Richer box.

TRACE  nums=[2,7,11,15] target=9
  i=0 num=2  need=7  dict={}           7 not in dict → store 2→0
  i=1 num=7  need=2  dict={2:0}        2 IS in dict  → return [0,1]

WHY THIS IS STILL L1's pattern
  L1: if x in seen → done
  L2: if (target-x) in seen → done
  The scan is identical. Only the LOOKUP KEY changed (x vs complement).
"""


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}  # value -> index   (dict upgrade from L1's set)
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []



# #############################################################################
# L3 — Group Anagrams
# #############################################################################
"""
YOU ALREADY KNOW (from L2)
  Dict maps a KEY → something useful (in L2: value → index).

WHAT'S NEW (ONE upgrade)
  The key is no longer "the number itself."
  The key is a SIGNATURE of the word = letters sorted + joined.
    "eat" / "tea" / "ate" all become key "aet"
  The value is a LIST (bucket) of original words that share that signature.

  Still a dict. Still one pass. Only what you store under the key changed.

TRACE  ["eat","tea","bat"]
  "eat" → key "aet" → groups = {"aet": ["eat"]}
  "tea" → key "aet" → groups = {"aet": ["eat","tea"]}
  "bat" → key "abt" → groups = {"aet": [...], "abt": ["bat"]}
  return the lists: [["eat","tea"], ["bat"]]

BRIDGE FROM L2
  L2 key = the number itself
  L3 key = sorted(word) glued into a string
  Same tool: dict. Different key recipe.
"""


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)  # signature -> [words]
    for word in strs:
        # >>> YOU: key = "".join(sorted(word))
        key = "".join(sorted(word))
        # >>> YOU: groups[key].append(word)
        groups[key].append(word)
    return list(groups.values())


# #############################################################################
# L4 — Top K Frequent Elements
# #############################################################################
"""
YOU ALREADY KNOW
  L1/L2: walk once, stuffing a set/dict as you go.
  L3:    dict key -> list bucket. You FILLED the dict, then used it.

  Top K uses that SAME fill. It does NOT sort letters like L3.

WHAT'S NEW (two phases — Phase 1 is old, Phase 2 is new)
  Phase 1 — COUNT (looks exactly like L1's loop, but values are +1 counts):
      freq = {}
      for x in nums:
          freq[x] = freq.get(x, 0) + 1
      # after [1,1,1,2,2,3]  ->  {1: 3, 2: 2, 3: 1}

  Phase 2 — RANK (the only new idea):
      Sort the KEYS by their counts (high to low), take first k.
      [1, 2, 3] sorted by count -> [1, 2, 3];  k=2 -> [1, 2]

WHY THIS IS NOT L3 (read this — you almost reused L3 by accident)
  L3: key = "".join(sorted("eat")) = "aet"   # key is a RECIPE from letters
  L4: key = 1                                 # key IS the number itself
  Do NOT call sorted() on the number. That is the L3 move. Wrong here.

TRACE Phase 1 (same style as L1/L2)  nums=[1,1,1,2,2,3]
  x=1  freq={}         -> freq[1]=1     dict={1:1}
  x=1  freq={1:1}      -> freq[1]=2     dict={1:2}
  x=1  freq={1:2}      -> freq[1]=3     dict={1:3}
  x=2  freq={1:3}      -> freq[2]=1     dict={1:3, 2:1}
  x=2  freq={1:3,2:1}  -> freq[2]=2     dict={1:3, 2:2}
  x=3                  -> freq[3]=1     dict={1:3, 2:2, 3:1}

TRACE Phase 2
  keys = [1, 2, 3]
  sort by freq[key] high->low -> [1, 2, 3]
  return first k=2 -> [1, 2]

SHORTHAND (ok AFTER you can write Phase 1 by hand)
  Counter(nums) builds Phase 1 for you. Still say out loud: "count, then top k."
"""


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    # Phase 1: COUNT — same one-pass dict fill as L1/L2 (NOT L3 sorting)
    freq = {}
    for x in nums:
        # >>> YOU: bump the count for x
        # hint: freq[x] = freq.get(x, 0) + 1
        pass

    # Phase 2: RANK — NEW. Sort keys by counts, take top k.
    # >>> YOU: ranked = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
    # >>> YOU: return ranked[:k]
    pass


# #############################################################################
# L5 — Subarray Sum Equals K   (Two Sum for running totals)
# #############################################################################
"""
YOU ALREADY KNOW (from L2 + L4)
  L2: ask for a COMPLEMENT while scanning; look it up in a dict.
  L4: dict values can be COUNTS (how many times a key appeared).

WHAT'S NEW (THE BOSS UPGRADE)
  Instead of storing array VALUES, store PREFIX SUMS (running totals).

  prefix = sum of everything from the left up to here.
  If (prefix - k) showed up earlier as a prefix, the chunk BETWEEN
  those two prefixes sums to exactly k.

  That is Two Sum's complement idea:
    L2 need = target - num
    L5 need = k      - (nothing) wait — look up (prefix - k)

TRACE  nums=[1,1,1] k=2
  start: seen={0:1}  (empty prefix counts as 0, seen once)
  +1 → prefix=1  look up 1-2=-1  miss  → seen={0:1, 1:1}  ans=0
  +1 → prefix=2  look up 2-2=0   HIT 1 → ans=1  seen={0:1,1:1,2:1}
  +1 → prefix=3  look up 3-2=1   HIT 1 → ans=2  seen={...,3:1}
  return 2

SAY THIS OUT LOUD
  "Subarray Sum K is Two Sum on prefix sums, and the dict stores COUNTS
   of prefixes like Top K stored counts of values."
"""


def subarray_sum(nums: List[int], k: int) -> int:
    seen = {0: 1}  # prefix_value -> how many times we've seen it
    prefix = 0
    ans = 0
    for num in nums:
        prefix += num
        # >>> YOU: ans += how many times (prefix - k) appears in seen
        # >>> YOU: then record this prefix: seen[prefix] = seen.get(prefix,0)+1
        pass
    return ans


# #############################################################################
# CLOSING QUIZ — forces the ladder into memory (answer by filling, then run LQ)
# #############################################################################
"""
Fill each return with the lesson code as a string: "L1", "L2", "L3", "L4", or "L5".
Run:  python hash_pattern_lab.py LQ
"""


def quiz_which_lesson_set_membership() -> str:
    """Which lesson is JUST 'have I seen this value' with a set?"""
    # >>> YOU: return "L?"
    return ""


def quiz_which_lesson_complement_on_values() -> str:
    """Which lesson asks for target - num while scanning?"""
    # >>> YOU
    return ""


def quiz_which_lesson_signature_key() -> str:
    """Which lesson makes a sorted-letters key to bucket words?"""
    # >>> YOU
    return ""


def quiz_which_lesson_two_sum_on_prefixes() -> str:
    """Which lesson is 'Two Sum for running totals'?"""
    # >>> YOU
    return ""


# =============================================================================
# RUNNER — one lesson at a time (unfinished later lessons are normal)
# =============================================================================
def _sorted_groups(groups: List[List[str]]) -> List[List[str]]:
    return sorted([sorted(g) for g in groups])


def _test_L0() -> None:
    demo_set_and_dict()
    print("  (L0 is demos only - if you read the prints, you're done)")


def _test_L1() -> None:
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1]) is False


def _test_L2() -> None:
    assert set(two_sum([2, 7, 11, 15], 9)) == {0, 1}
    assert set(two_sum([3, 2, 4], 6)) == {1, 2}
    assert set(two_sum([3, 3], 6)) == {0, 1}


def _test_L3() -> None:
    assert _sorted_groups(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == _sorted_groups(
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    )
    assert _sorted_groups(group_anagrams([""])) == [[""]]
    assert _sorted_groups(group_anagrams(["a"])) == [["a"]]


def _test_L4() -> None:
    assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert top_k_frequent([1], 1) == [1]


def _test_L5() -> None:
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
    assert subarray_sum([1], 0) == 0


def _test_LQ() -> None:
    assert quiz_which_lesson_set_membership() == "L1"
    assert quiz_which_lesson_complement_on_values() == "L2"
    assert quiz_which_lesson_signature_key() == "L3"
    assert quiz_which_lesson_two_sum_on_prefixes() == "L5"


TESTS = {
    "L0": ("Tools: set + dict demos", _test_L0),
    "L1": ("Contains Duplicate", _test_L1),
    "L2": ("Two Sum (complement)", _test_L2),
    "L3": ("Group Anagrams (signature key)", _test_L3),
    "L4": ("Top K Frequent (count then rank)", _test_L4),
    "L5": ("Subarray Sum K (Two Sum on prefixes)", _test_L5),
    "LQ": ("Closing quiz (ladder check)", _test_LQ),
}


def _run_one(code: str) -> str:
    name, fn = TESTS[code]
    try:
        fn()
        print(f"  PASS  {code}  {name}")
        return "pass"
    except Exception as exc:
        print(f"  ----  {code}  {name}  (not yet: {type(exc).__name__})")
        print(f"        stay here -> python hash_pattern_lab.py {code}")
        return "fail"


if __name__ == "__main__":
    args = [a.upper() for a in sys.argv[1:]]
    if args and args[0] in ("-H", "--HELP", "HELP"):
        print("Usage:")
        print("  python hash_pattern_lab.py L0    # demos")
        print("  python hash_pattern_lab.py L1    # one lesson")
        print("  python hash_pattern_lab.py       # progress card")
        raise SystemExit(0)

    if args:
        unknown = [a for a in args if a not in TESTS]
        if unknown:
            print(f"Unknown: {unknown}. Use: {', '.join(TESTS)}")
            raise SystemExit(1)
        print("Testing:")
        results = [_run_one(c) for c in args]
        if all(r == "pass" for r in results):
            print("\nLocked. Next lesson up the ladder.")
            raise SystemExit(0)
        print("\nRe-read YOU ALREADY KNOW / WHAT'S NEW / TRACE above this function.")
        raise SystemExit(1)

    print("Hash lab progress (unfinished = normal):\n")
    passed = 0
    # L0 always "runs"; count it separately for coding lessons
    for code in TESTS:
        if _run_one(code) == "pass":
            passed += 1
    print(f"\n{passed}/{len(TESTS)} passing.")
    for code, (name, fn) in TESTS.items():
        try:
            fn()
        except Exception:
            print(f"Next up: {code} ({name})")
            print(f"  python hash_pattern_lab.py {code}")
            break
    else:
        print("Hash ladder complete. Timed reps -> 07_amazon_common_problems.py")

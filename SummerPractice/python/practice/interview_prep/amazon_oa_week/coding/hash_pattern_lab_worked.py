"""
WORKED ANSWERS — hash_pattern_lab.py

Peek ONLY after 15+ min stuck on ONE lesson.
Read that function. Close this file. Retype from memory. Re-test:
  python hash_pattern_lab.py L?
"""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    # Phase 1: same scan as L1 — dict values are counts
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1
    # Phase 2: rank keys by those counts
    ranked = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
    return ranked[:k]


def subarray_sum(nums: List[int], k: int) -> int:
    seen = {0: 1}
    prefix = 0
    ans = 0
    for num in nums:
        prefix += num
        ans += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return ans


def quiz_which_lesson_set_membership() -> str:
    return "L1"


def quiz_which_lesson_complement_on_values() -> str:
    return "L2"


def quiz_which_lesson_signature_key() -> str:
    return "L3"


def quiz_which_lesson_two_sum_on_prefixes() -> str:
    return "L5"


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert set(two_sum([2, 7, 11, 15], 9)) == {0, 1}
    assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert subarray_sum([1, 1, 1], 2) == 2
    assert quiz_which_lesson_two_sum_on_prefixes() == "L5"
    print("Worked hash lab answer key OK.")

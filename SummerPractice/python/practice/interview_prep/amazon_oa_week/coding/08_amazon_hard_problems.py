"""
Amazon Harder Problem Bank (phone / loop stretch)

How to use:
  1. Clear common bank first (07_amazon_common_problems.py).
  2. Do these with full live-coding narration (45 min each).
  3. Run:
       python 08_amazon_hard_problems.py

These show up in Amazon phone screens and loop medium/hard rounds.
"""

from __future__ import annotations

import heapq
from collections import defaultdict, deque
from typing import List, Optional


# =============================================================================
# H01 — LRU Cache  (LC 146)  | Pattern: hash map + doubly linked list
# =============================================================================
"""
PROBLEM
  Design a data structure that follows the constraints of a Least Recently
  Used (LRU) cache.

  Implement the LRUCache class:
    LRUCache(capacity)  Initialize with positive size capacity.
    get(key)            Return value if key exists, else -1.
    put(key, value)     Update or insert. If capacity exceeded, evict the
                        least recently used key before inserting.

  get and put must run in O(1) average time.

EXAMPLES
  LRUCache(2)
  put(1, 1)   # {1=1}
  put(2, 2)   # {1=1, 2=2}
  get(1)      # returns 1
  put(3, 3)   # evicts key 2 -> {1=1, 3=3}
  get(2)      # returns -1
  put(4, 4)   # evicts key 1 -> {3=3, 4=4}
  get(1)      # -1
  get(3)      # 3
  get(4)      # 4

THINK FIRST
  dict: key -> node. Doubly linked list for recency (head=MRU, tail=LRU)
  OR use OrderedDict.move_to_end in Python interviews if allowed — then
  explain the O(1) list idea underneath.
"""


class LRUCache:
    def __init__(self, capacity: int):
        # TODO
        pass

    def get(self, key: int) -> int:
        # TODO
        pass

    def put(self, key: int, value: int) -> None:
        # TODO
        pass


# =============================================================================
# H02 — Word Ladder  (LC 127)  | Pattern: BFS on implicit graph
# =============================================================================
"""
PROBLEM
  A transformation sequence from beginWord to endWord using a dictionary
  wordList is a sequence beginWord -> s1 -> s2 -> ... -> sk such that:
    - Every adjacent pair differs by exactly one letter
    - Every si is in wordList (beginWord does not need to be)
    - sk == endWord

  Return the number of words in the shortest transformation sequence,
  or 0 if no such sequence exists.

EXAMPLES
  beginWord = "hit", endWord = "cog",
  wordList = ["hot","dot","dog","lot","log","cog"]  ->  5
    ("hit" -> "hot" -> "dot" -> "dog" -> "cog")

  beginWord = "hit", endWord = "cog",
  wordList = ["hot","dot","dog","lot","log"]        ->  0

CONSTRAINTS
  1 <= len(beginWord) <= 10
  endWord.length == beginWord.length
  1 <= len(wordList) <= 5000
  All words same length, lowercase.

THINK FIRST
  Each word is a node. Edges to words at distance 1. BFS for shortest path.
"""


def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    # TODO
    pass


# =============================================================================
# H03 — Merge K Sorted Lists  (LC 23)  | Pattern: heap / divide & conquer
# =============================================================================
"""
PROBLEM
  You are given an array of k linked lists, each sorted in ascending order.
  Merge all the linked lists into one sorted linked list and return it.

  We represent list nodes as ListNode below.

EXAMPLES
  lists = [[1,4,5],[1,3,4],[2,6]]  ->  [1,1,2,3,4,4,5,6]
  lists = []                      ->  []
  lists = [[]]                    ->  []

THINK FIRST
  Min-heap of current heads: O(N log k).
"""


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # TODO
    pass


# =============================================================================
# H04 — Trapping Rain Water  (LC 42)  | Pattern: two pointers / stack
# =============================================================================
"""
PROBLEM
  Given n non-negative integers representing an elevation map where the
  width of each bar is 1, compute how much water it can trap after raining.

EXAMPLES
  height = [0,1,0,2,1,0,1,3,2,1,2,1]  ->  6
  height = [4,2,0,3,2,5]              ->  9

CONSTRAINTS
  n == len(height)
  1 <= n <= 2 * 10^4
  0 <= height[i] <= 10^5

THINK FIRST
  Water at i = min(maxL, maxR) - height[i].
  Two pointers: advance the side with smaller max wall.
"""


def trap(height: List[int]) -> int:
    # TODO
    pass


# =============================================================================
# H05 — Binary Search on Answer: Koko Eating Bananas  (LC 875)
# =============================================================================
"""
PROBLEM
  Koko loves bananas. There are n piles of bananas, piles[i] bananas in
  the i-th pile. Guards return in h hours.
  Koko can decide her bananas-per-hour eating speed k. Each hour she
  chooses one pile and eats k bananas from it. If the pile has < k, she
  eats all and won't eat more that hour.
  Return the minimum integer k such that she can eat all bananas within h hours.

EXAMPLES
  piles = [3,6,7,11], h = 8      ->  4
  piles = [30,11,23,4,20], h = 5 ->  30
  piles = [30,11,23,4,20], h = 6 ->  23

CONSTRAINTS
  1 <= len(piles) <= 10^4
  piles.length <= h <= 10^9
  1 <= piles[i] <= 10^9

THINK FIRST
  Binary search speed in [1, max(piles)].
  feasible(k) = sum(ceil(p/k) for p in piles) <= h  (monotonic).
"""


def min_eating_speed(piles: List[int], h: int) -> int:
    # TODO
    pass


# =============================================================================
# H06 — Word Break  (LC 139)  | Pattern: DP + hash set
# =============================================================================
"""
PROBLEM
  Given a string s and a dictionary of strings wordDict, return true if s
  can be segmented into a space-separated sequence of one or more
  dictionary words.
  Note: the same word may be reused multiple times.

EXAMPLES
  s = "leetcode", wordDict = ["leet","code"]           -> True
  s = "applepenapple", wordDict = ["apple","pen"]      -> True
  s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] -> False

CONSTRAINTS
  1 <= len(s) <= 300
  1 <= len(wordDict) <= 1000
  1 <= len(wordDict[i]) <= 20
  s and words consist of lowercase letters.
  All dictionary words are unique.

THINK FIRST
  dp[i] = True if s[:i] can be segmented.
  Transition: for each end i, try word endings at i.
"""


def word_break(s: str, word_dict: List[str]) -> bool:
    # TODO
    pass


# =============================================================================
# H07 — Amazon story: Top K Keywords with Tie-break
# =============================================================================
"""
PROBLEM (Amazon OA-style wrapper)
  Support tickets produce a list of keywords.
  Return the top k most frequent keywords.
  If two keywords have the same frequency, the lexicographically smaller
  one ranks higher.

EXAMPLES
  keywords = ["a","b","a","c","b","a"], k = 2  ->  ["a","b"]
  keywords = ["i","love","leetcode","i","love","coding"], k = 2
    -> ["i","love"]   (both freq 2; "i" < "love")

THINK FIRST
  Counter, then sorted(keys, key=lambda w: (-freq[w], w))[:k]
"""


def top_k_keywords(keywords: List[str], k: int) -> List[str]:
    # TODO
    pass


# =============================================================================
# Helpers / TESTS — do not edit
# =============================================================================
def _list_from_vals(vals: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def _vals_from_list(node: Optional[ListNode]) -> List[int]:
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    # H01 LRU
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    # H02 Word Ladder
    assert (
        ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    )
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert ladder_length("a", "c", ["a", "b", "c"]) == 2

    # H03 Merge K Lists
    lists = [
        _list_from_vals([1, 4, 5]),
        _list_from_vals([1, 3, 4]),
        _list_from_vals([2, 6]),
    ]
    assert _vals_from_list(merge_k_lists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert _vals_from_list(merge_k_lists([])) == []
    assert _vals_from_list(merge_k_lists([None])) == []

    # H04 Trap
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    assert trap([1]) == 0

    # H05 Koko
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23

    # H06 Word Break
    assert word_break("leetcode", ["leet", "code"]) is True
    assert word_break("applepenapple", ["apple", "pen"]) is True
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False

    # H07 Amazon story
    assert top_k_keywords(["a", "b", "a", "c", "b", "a"], 2) == ["a", "b"]
    assert top_k_keywords(["i", "love", "leetcode", "i", "love", "coding"], 2) == [
        "i",
        "love",
    ]
    assert top_k_keywords(["x"], 1) == ["x"]

    print("All 7 HARDER Amazon problems passed.")

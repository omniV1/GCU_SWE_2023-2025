"""
Seed / expand the NeetCode-style Amazon problem bank.

Run:
  python seed_problems.py

Adds/updates data/problems.json. Safe to re-run — merges by id.
"""

from __future__ import annotations

import json
from pathlib import Path

import neetcode_examples
import python_pattern_guides
import when_to_use
import real_world_hooks

ROOT = Path(__file__).parent
OUT = ROOT / "data" / "problems.json"

# NeetCode roadmap order (Amazon-weighted)
ROADMAP = [
    ("Arrays & Hashing", "arrays-hashing"),
    ("Two Pointers", "two-pointers"),
    ("Sliding Window", "sliding-window"),
    ("Stack", "stack"),
    ("Binary Search", "binary-search"),
    ("Linked List", "linked-list"),
    ("Trees", "trees"),
    ("Heap / Priority Queue", "heap"),
    ("Backtracking", "backtracking"),
    ("Graphs", "graphs"),
    ("1-D DP", "dp-1d"),
    ("Intervals", "intervals"),
    ("Greedy", "greedy"),
    ("Amazon Story Wrappers", "amazon-story"),
]


def P(
    id: str,
    title: str,
    category: str,
    difficulty: str,
    pattern: str,
    already: str,
    new: str,
    trace: str,
    say: str,
    complexity: str,
    hint: str,
    starter: str,
    solution: str,
    fn: str,
    tests: list,
    lc: int | None = None,
    amazon: bool = True,
) -> dict:
    return {
        "id": id,
        "title": title,
        "category": category,
        "difficulty": difficulty,
        "pattern": pattern,
        "alreadyKnow": already,
        "whatsNew": new,
        "trace": trace,
        "sayOutLoud": say,
        "complexity": complexity,
        "hint": hint,
        "starter": starter.strip("\n") + "\n",
        "solution": solution.strip("\n") + "\n",
        "fn": fn,
        "tests": tests,
        "lc": lc,
        "amazon": amazon,
    }


PROBLEMS: list[dict] = [
    # -------- Arrays & Hashing --------
    P(
        "ah-contains-duplicate",
        "Contains Duplicate",
        "arrays-hashing",
        "easy",
        "Hash set",
        "You can scan an array once.",
        "Use a set: if you've seen the value before, return True.",
        "nums=[1,2,3,1] -> see 1 again -> True",
        "I'll use a set for O(1) membership while I scan once.",
        "Time O(n), Space O(n)",
        "if x in seen: return True; seen.add(x)",
        """
def contains_duplicate(nums):
    seen = set()
    for x in nums:
        # >>> YOU
        pass
    return False
""",
        """
def contains_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
""",
        "contains_duplicate",
        [
            {"args": [[1, 2, 3, 1]], "expect": True},
            {"args": [[1, 2, 3, 4]], "expect": False},
            {"args": [[1]], "expect": False},
        ],
        lc=217,
    ),
    P(
        "ah-valid-anagram",
        "Valid Anagram",
        "arrays-hashing",
        "easy",
        "Counter / frequency map",
        "Sets tell yes/no. Dicts can store COUNTS.",
        "Count letters in s and t; compare the two frequency maps.",
        "'anagram' vs 'nagaram' -> same counts -> True",
        "I'll compare character frequency maps — Counter or hand-built dict.",
        "Time O(n), Space O(1) alphabet",
        "from collections import Counter; return Counter(s)==Counter(t)",
        """
from collections import Counter

def is_anagram(s, t):
    # >>> YOU
    pass
""",
        """
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
""",
        "is_anagram",
        [
            {"args": ["anagram", "nagaram"], "expect": True},
            {"args": ["rat", "car"], "expect": False},
            {"args": ["", ""], "expect": True},
        ],
        lc=242,
    ),
    P(
        "ah-two-sum",
        "Two Sum",
        "arrays-hashing",
        "easy",
        "Hash map + complement",
        "Contains Duplicate taught membership. Valid Anagram taught counts.",
        "Store value->index. Ask for complement target-num.",
        "[2,7,11,15] t=9 -> need 7 after seeing 2 -> [0,1]",
        "Same one-pass hash idea — look up target minus current.",
        "Time O(n), Space O(n)",
        "need=target-num; if need in seen: return [seen[need], i]",
        """
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        # >>> YOU
        pass
    return []
""",
        """
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []
""",
        "two_sum",
        [
            {"args": [[2, 7, 11, 15], 9], "expect": [0, 1], "unorderedPair": True},
            {"args": [[3, 2, 4], 6], "expect": [1, 2], "unorderedPair": True},
            {"args": [[3, 3], 6], "expect": [0, 1], "unorderedPair": True},
        ],
        lc=1,
    ),
    P(
        "ah-group-anagrams",
        "Group Anagrams",
        "arrays-hashing",
        "medium",
        "Signature key -> bucket",
        "Two Sum: dict key was the number itself.",
        "Key is ''.join(sorted(word)). Value is a list of words sharing that signature.",
        "eat/tea/ate share key 'aet'",
        "Still a dict — only the key recipe changed (sorted letters).",
        "Time O(n*k log k), Space O(n*k)",
        "key=''.join(sorted(word)); groups[key].append(word)",
        """
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for word in strs:
        # >>> YOU
        pass
    return list(groups.values())
""",
        """
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())
""",
        "group_anagrams",
        [
            {
                "args": [["eat", "tea", "tan", "ate", "nat", "bat"]],
                "expectGroups": [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
            },
            {"args": [[""]], "expectGroups": [[""]]},
        ],
        lc=49,
    ),
    P(
        "ah-top-k-frequent",
        "Top K Frequent Elements",
        "arrays-hashing",
        "medium",
        "Count then rank",
        "Group Anagrams buckets by signature. Here key IS the number.",
        "Phase 1: count frequencies. Phase 2: sort keys by count, take top k. NOT letter-sorting.",
        "[1,1,1,2,2,3] k=2 -> counts {1:3,2:2,3:1} -> [1,2]",
        "I count with a dict like Contains Duplicate, then rank keys — I do not make anagram signatures.",
        "Time O(n + u log u), Space O(u)",
        "freq[x]=freq.get(x,0)+1; then sorted by freq reverse[:k]",
        """
def top_k_frequent(nums, k):
    freq = {}
    for x in nums:
        # >>> Phase 1 count
        pass
    # >>> Phase 2 rank and return top k
    pass
""",
        """
def top_k_frequent(nums, k):
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1
    ranked = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
    return ranked[:k]
""",
        "top_k_frequent",
        [
            {"args": [[1, 1, 1, 2, 2, 3], 2], "expectSet": [1, 2]},
            {"args": [[1], 1], "expect": [1]},
        ],
        lc=347,
    ),
    P(
        "ah-product-except-self",
        "Product of Array Except Self",
        "arrays-hashing",
        "medium",
        "Prefix / suffix products",
        "You can do one left-to-right pass storing running state.",
        "Left products, then right products multiplied in — no division.",
        "[1,2,3,4] -> [24,12,8,6]",
        "I'll build prefix products, then multiply by suffix products in a second pass.",
        "Time O(n), Space O(1) extra excluding output",
        "out[i] left product, then multiply running right",
        """
def product_except_self(nums):
    n = len(nums)
    out = [1] * n
    # >>> YOU: left pass then right pass
    pass
""",
        """
def product_except_self(nums):
    n = len(nums)
    out = [1] * n
    left = 1
    for i in range(n):
        out[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        out[i] *= right
        right *= nums[i]
    return out
""",
        "product_except_self",
        [
            {"args": [[1, 2, 3, 4]], "expect": [24, 12, 8, 6]},
            {"args": [[-1, 1, 0, -3, 3]], "expect": [0, 0, 9, 0, 0]},
        ],
        lc=238,
    ),
    P(
        "ah-longest-consecutive",
        "Longest Consecutive Sequence",
        "arrays-hashing",
        "medium",
        "Set + only start of streaks",
        "Set membership is O(1).",
        "Put all in a set. Only start counting when num-1 is NOT in the set.",
        "[100,4,200,1,3,2] -> streak 1..4 length 4",
        "I'll only begin a streak at numbers that have no predecessor in the set.",
        "Time O(n), Space O(n)",
        "if num-1 not in seen: count upward",
        """
def longest_consecutive(nums):
    seen = set(nums)
    best = 0
    for num in seen:
        # >>> YOU
        pass
    return best
""",
        """
def longest_consecutive(nums):
    seen = set(nums)
    best = 0
    for num in seen:
        if num - 1 not in seen:
            length = 1
            while num + length in seen:
                length += 1
            best = max(best, length)
    return best
""",
        "longest_consecutive",
        [
            {"args": [[100, 4, 200, 1, 3, 2]], "expect": 4},
            {"args": [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]], "expect": 9},
            {"args": [[]], "expect": 0},
        ],
        lc=128,
    ),
    P(
        "ah-subarray-sum-k",
        "Subarray Sum Equals K",
        "arrays-hashing",
        "medium",
        "Prefix sum + hash (Two Sum on totals)",
        "Two Sum: look up complement. Top K: dict stores counts.",
        "Store prefix sums and counts. Look up prefix-k.",
        "[1,1,1] k=2 -> 2 subarrays",
        "This is Two Sum for running totals.",
        "Time O(n), Space O(n)",
        "ans += seen.get(prefix-k,0); seen[prefix]=...",
        """
def subarray_sum(nums, k):
    seen = {0: 1}
    prefix = 0
    ans = 0
    for num in nums:
        # >>> YOU
        pass
    return ans
""",
        """
def subarray_sum(nums, k):
    seen = {0: 1}
    prefix = 0
    ans = 0
    for num in nums:
        prefix += num
        ans += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return ans
""",
        "subarray_sum",
        [
            {"args": [[1, 1, 1], 2], "expect": 2},
            {"args": [[1, 2, 3], 3], "expect": 2},
        ],
        lc=560,
    ),
    # -------- Two Pointers --------
    P(
        "tp-valid-palindrome",
        "Valid Palindrome",
        "two-pointers",
        "easy",
        "Converging two pointers",
        "You can skip non-alphanumeric while scanning.",
        "Left and right move inward; compare lowercased letters/digits.",
        "'A man, a plan, a canal: Panama' -> True",
        "I'll skip junk characters and compare from both ends.",
        "Time O(n), Space O(1)",
        "while L<R: skip non-alnum; compare lower",
        """
def is_palindrome(s):
    L, R = 0, len(s) - 1
    while L < R:
        # >>> YOU
        pass
    return True
""",
        """
def is_palindrome(s):
    L, R = 0, len(s) - 1
    while L < R:
        while L < R and not s[L].isalnum():
            L += 1
        while L < R and not s[R].isalnum():
            R -= 1
        if s[L].lower() != s[R].lower():
            return False
        L += 1
        R -= 1
    return True
""",
        "is_palindrome",
        [
            {"args": ["A man, a plan, a canal: Panama"], "expect": True},
            {"args": ["race a car"], "expect": False},
            {"args": [" "], "expect": True},
        ],
        lc=125,
    ),
    P(
        "tp-two-sum-ii",
        "Two Sum II (sorted)",
        "two-pointers",
        "medium",
        "Converging pointers on sorted array",
        "Two Sum used a hash map. Input is sorted now.",
        "Left/right: too small move left up; too big move right down. Return 1-indexed.",
        "[2,7,11,15] t=9 -> [1,2]",
        "Sorted means I can trade the hash map for two pointers and O(1) extra space.",
        "Time O(n), Space O(1)",
        "sum too small: L+=1; too big: R-=1",
        """
def two_sum(numbers, target):
    L, R = 0, len(numbers) - 1
    while L < R:
        # >>> YOU
        pass
    return []
""",
        """
def two_sum(numbers, target):
    L, R = 0, len(numbers) - 1
    while L < R:
        s = numbers[L] + numbers[R]
        if s == target:
            return [L + 1, R + 1]
        if s < target:
            L += 1
        else:
            R -= 1
    return []
""",
        "two_sum",
        [
            {"args": [[2, 7, 11, 15], 9], "expect": [1, 2]},
            {"args": [[2, 3, 4], 6], "expect": [1, 3]},
        ],
        lc=167,
    ),
    P(
        "tp-3sum",
        "3Sum",
        "two-pointers",
        "medium",
        "Sort + fix one + two pointers",
        "Two Sum II on sorted arrays.",
        "Sort. Fix nums[i], two-pointer the rest for -nums[i]. Skip duplicates.",
        "[-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]",
        "I'll sort, fix one value, then Two Sum II the remainder while skipping dupes.",
        "Time O(n^2), Space O(1) extra",
        "for i: L,R two pointer for -nums[i]; skip duplicates",
        """
def three_sum(nums):
    nums = sorted(nums)
    out = []
    # >>> YOU
    pass
    return out
""",
        """
def three_sum(nums):
    nums = sorted(nums)
    out = []
    n = len(nums)
    for i in range(n):
        if i and nums[i] == nums[i - 1]:
            continue
        L, R = i + 1, n - 1
        while L < R:
            s = nums[i] + nums[L] + nums[R]
            if s == 0:
                out.append([nums[i], nums[L], nums[R]])
                L += 1
                R -= 1
                while L < R and nums[L] == nums[L - 1]:
                    L += 1
                while L < R and nums[R] == nums[R + 1]:
                    R -= 1
            elif s < 0:
                L += 1
            else:
                R -= 1
    return out
""",
        "three_sum",
        [
            {
                "args": [[-1, 0, 1, 2, -1, -4]],
                "expectGroups": [[-1, -1, 2], [-1, 0, 1]],
            },
            {"args": [[0, 1, 1]], "expectGroups": []},
            {"args": [[0, 0, 0]], "expectGroups": [[0, 0, 0]]},
        ],
        lc=15,
    ),
    P(
        "tp-container-water",
        "Container With Most Water",
        "two-pointers",
        "medium",
        "Converging pointers · area",
        "Two pointers from both ends.",
        "Area = min(hL,hR)*(R-L). Move the shorter side inward.",
        "[1,8,6,2,5,4,8,3,7] -> 49",
        "I'll move the pointer at the shorter wall — that's the only way area can grow.",
        "Time O(n), Space O(1)",
        "move the side with smaller height",
        """
def max_area(height):
    L, R = 0, len(height) - 1
    best = 0
    while L < R:
        # >>> YOU
        pass
    return best
""",
        """
def max_area(height):
    L, R = 0, len(height) - 1
    best = 0
    while L < R:
        best = max(best, min(height[L], height[R]) * (R - L))
        if height[L] < height[R]:
            L += 1
        else:
            R -= 1
    return best
""",
        "max_area",
        [
            {"args": [[1, 8, 6, 2, 5, 4, 8, 3, 7]], "expect": 49},
            {"args": [[1, 1]], "expect": 1},
        ],
        lc=11,
    ),
    # -------- Sliding Window --------
    P(
        "sw-best-stock",
        "Best Time to Buy and Sell Stock",
        "sliding-window",
        "easy",
        "Running min (window cousin)",
        "One-pass running state.",
        "Track min price so far; best = price - min.",
        "[7,1,5,3,6,4] -> 5",
        "I'll remember the cheapest so far and the best profit if I sell today.",
        "Time O(n), Space O(1)",
        "min_price=min(...); best=max(best, price-min_price)",
        """
def max_profit(prices):
    min_price = float("inf")
    best = 0
    for price in prices:
        # >>> YOU
        pass
    return best
""",
        """
def max_profit(prices):
    min_price = float("inf")
    best = 0
    for price in prices:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
    return best
""",
        "max_profit",
        [
            {"args": [[7, 1, 5, 3, 6, 4]], "expect": 5},
            {"args": [[7, 6, 4, 3, 1]], "expect": 0},
        ],
        lc=121,
    ),
    P(
        "sw-longest-substring",
        "Longest Substring Without Repeating Characters",
        "sliding-window",
        "medium",
        "Sliding window + set",
        "Hash set membership.",
        "Expand right; shrink left while duplicate in window; track max length.",
        "'abcabcbb' -> 3",
        "Invariant: chars in [left,right] are unique.",
        "Time O(n), Space O(alphabet)",
        "while ch in window: remove s[left]; left+=1",
        """
def length_of_longest_substring(s):
    left = 0
    best = 0
    window = set()
    for right, ch in enumerate(s):
        # >>> YOU
        pass
    return best
""",
        """
def length_of_longest_substring(s):
    left = 0
    best = 0
    window = set()
    for right, ch in enumerate(s):
        while ch in window:
            window.remove(s[left])
            left += 1
        window.add(ch)
        best = max(best, right - left + 1)
    return best
""",
        "length_of_longest_substring",
        [
            {"args": ["abcabcbb"], "expect": 3},
            {"args": ["bbbbb"], "expect": 1},
            {"args": ["pwwkew"], "expect": 3},
            {"args": [""], "expect": 0},
        ],
        lc=3,
    ),
    P(
        "sw-min-subarray",
        "Minimum Size Subarray Sum",
        "sliding-window",
        "medium",
        "Window · shrink while valid",
        "Longest unique: shrink when INVALID.",
        "Flip: shrink while still VALID (sum>=target) to minimize length.",
        "target=7 [2,3,1,2,4,3] -> 2",
        "Same window tool — flipped stop rule.",
        "Time O(n), Space O(1)",
        "while total>=target: update best; shrink left",
        """
def min_subarray_len(target, nums):
    left = 0
    total = 0
    best = float("inf")
    for right, num in enumerate(nums):
        total += num
        # >>> YOU
        pass
    return 0 if best == float("inf") else best
""",
        """
def min_subarray_len(target, nums):
    left = 0
    total = 0
    best = float("inf")
    for right, num in enumerate(nums):
        total += num
        while total >= target:
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if best == float("inf") else best
""",
        "min_subarray_len",
        [
            {"args": [7, [2, 3, 1, 2, 4, 3]], "expect": 2},
            {"args": [4, [1, 4, 4]], "expect": 1},
            {"args": [11, [1, 1, 1, 1, 1, 1, 1, 1]], "expect": 0},
        ],
        lc=209,
    ),
    # -------- Stack --------
    P(
        "st-valid-parentheses",
        "Valid Parentheses",
        "stack",
        "easy",
        "Stack matching",
        "Most-recent unmatched opener matters.",
        "Push openers; closer must match stack top; empty at end.",
        "'([])' True, '(]' False",
        "Stack holds unmatched opens.",
        "Time O(n), Space O(n)",
        "pairs map; pop must match",
        """
def is_valid(s):
    pairs = {')':'(', ']':'[', '}':'{'}
    stack = []
    for ch in s:
        # >>> YOU
        pass
    return len(stack) == 0
""",
        """
def is_valid(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return len(stack) == 0
""",
        "is_valid",
        [
            {"args": ["()"], "expect": True},
            {"args": ["()[]{}"], "expect": True},
            {"args": ["(]"], "expect": False},
            {"args": ["([])"], "expect": True},
        ],
        lc=20,
    ),
    P(
        "st-daily-temperatures",
        "Daily Temperatures",
        "stack",
        "medium",
        "Monotonic stack",
        "Valid parentheses: stack of opens.",
        "Stack of indices with decreasing temps; when warmer found, resolve waits.",
        "[73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]",
        "I'll keep a decreasing stack of indices until a warmer day appears.",
        "Time O(n), Space O(n)",
        "while stack and warmer: ans[stack.pop()]=dist",
        """
def daily_temperatures(temperatures):
    n = len(temperatures)
    ans = [0] * n
    stack = []
    for i, t in enumerate(temperatures):
        # >>> YOU
        pass
    return ans
""",
        """
def daily_temperatures(temperatures):
    n = len(temperatures)
    ans = [0] * n
    stack = []
    for i, t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)
    return ans
""",
        "daily_temperatures",
        [
            {
                "args": [[73, 74, 75, 71, 69, 72, 76, 73]],
                "expect": [1, 1, 4, 2, 1, 1, 0, 0],
            },
            {"args": [[30, 40, 50, 60]], "expect": [1, 1, 1, 0]},
        ],
        lc=739,
    ),
    # -------- Binary Search --------
    P(
        "bs-binary-search",
        "Binary Search",
        "binary-search",
        "easy",
        "Classic binary search",
        "Array is sorted.",
        "Mid compare; discard half each time.",
        "[-1,0,3,5,9,12] target 9 -> index 4",
        "I'll binary search and return the index or -1.",
        "Time O(log n), Space O(1)",
        "while L<=R: mid; move L/R",
        """
def search(nums, target):
    L, R = 0, len(nums) - 1
    while L <= R:
        # >>> YOU
        pass
    return -1
""",
        """
def search(nums, target):
    L, R = 0, len(nums) - 1
    while L <= R:
        mid = (L + R) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            L = mid + 1
        else:
            R = mid - 1
    return -1
""",
        "search",
        [
            {"args": [[-1, 0, 3, 5, 9, 12], 9], "expect": 4},
            {"args": [[-1, 0, 3, 5, 9, 12], 2], "expect": -1},
        ],
        lc=704,
    ),
    P(
        "bs-koko",
        "Koko Eating Bananas",
        "binary-search",
        "medium",
        "Binary search on answer",
        "Classic BS searches a sorted array. Here the ANSWER SPACE is sorted.",
        "Search speed in [1, max(pile)]. feasible(mid) if hours needed <= h.",
        "[3,6,7,11] h=8 -> 4",
        "I'll binary search the minimum feasible eating speed.",
        "Time O(n log M), Space O(1)",
        "feasible(speed)=sum(ceil(p/speed))<=h",
        """
import math

def min_eating_speed(piles, h):
    def feasible(speed):
        # >>> YOU
        pass
    lo, hi = 1, max(piles)
    while lo < hi:
        # >>> YOU binary search
        pass
    return lo
""",
        """
import math

def min_eating_speed(piles, h):
    def feasible(speed):
        return sum(math.ceil(p / speed) for p in piles) <= h

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
""",
        "min_eating_speed",
        [
            {"args": [[3, 6, 7, 11], 8], "expect": 4},
            {"args": [[30, 11, 23, 4, 20], 5], "expect": 30},
            {"args": [[30, 11, 23, 4, 20], 6], "expect": 23},
        ],
        lc=875,
    ),
    # -------- Heap --------
    P(
        "hp-kth-largest",
        "Kth Largest Element in an Array",
        "heap",
        "medium",
        "Min-heap of size k",
        "Top K Frequent ranked by sorting. Heap keeps only k.",
        "Push into min-heap; pop when size > k; top is answer.",
        "[3,2,1,5,6,4] k=2 -> 5",
        "I'll keep a size-k min-heap of the largest values seen.",
        "Time O(n log k), Space O(k)",
        "heapq; if len>k: heappop",
        """
import heapq

def find_kth_largest(nums, k):
    heap = []
    for x in nums:
        # >>> YOU
        pass
    return heap[0]
""",
        """
import heapq

def find_kth_largest(nums, k):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
""",
        "find_kth_largest",
        [
            {"args": [[3, 2, 1, 5, 6, 4], 2], "expect": 5},
            {"args": [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4], "expect": 4},
        ],
        lc=215,
    ),
    # -------- Graphs --------
    P(
        "gr-num-islands",
        "Number of Islands",
        "graphs",
        "medium",
        "DFS/BFS flood fill",
        "Visit neighbors; mark visited.",
        "Each fresh '1' starts an island; flood-fill the component.",
        "Classic grid: count components of land.",
        "I'll DFS/BFS each unvisited land cell and count starts.",
        "Time O(mn), Space O(mn)",
        "sink to '0' and recurse 4 dirs",
        """
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        # >>> YOU
        pass

    islands = 0
    for r in range(rows):
        for c in range(cols):
            # >>> YOU
            pass
    return islands
""",
        """
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)
    return islands
""",
        "num_islands",
        [
            {
                "args": [
                    [
                        ["1", "1", "0", "0", "0"],
                        ["1", "1", "0", "0", "0"],
                        ["0", "0", "1", "0", "0"],
                        ["0", "0", "0", "1", "1"],
                    ]
                ],
                "expect": 3,
                "deepcopy": True,
            },
            {"args": [[["0"]]], "expect": 0, "deepcopy": True},
        ],
        lc=200,
    ),
    P(
        "gr-rotting-oranges",
        "Rotting Oranges",
        "graphs",
        "medium",
        "Multi-source BFS",
        "Number of Islands DFS. Now spread by minutes.",
        "Queue ALL initial rotten. Each BFS layer = 1 minute.",
        "[[2,1,1],[1,1,0],[0,1,1]] -> 4",
        "Multi-source BFS from every rotten orange at once.",
        "Time O(mn), Space O(mn)",
        "count fresh; layer BFS until fresh==0",
        """
from collections import deque

def oranges_rotting(grid):
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
    # >>> YOU BFS
    pass
    return minutes if fresh == 0 else -1
""",
        """
from collections import deque

def oranges_rotting(grid):
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
    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        minutes += 1
    return minutes if fresh == 0 else -1
""",
        "oranges_rotting",
        [
            {"args": [[[2, 1, 1], [1, 1, 0], [0, 1, 1]]], "expect": 4, "deepcopy": True},
            {"args": [[[2, 1, 1], [0, 1, 1], [1, 0, 1]]], "expect": -1, "deepcopy": True},
            {"args": [[[0, 2]]], "expect": 0, "deepcopy": True},
        ],
        lc=994,
    ),
    P(
        "gr-course-schedule",
        "Course Schedule",
        "graphs",
        "medium",
        "Topo sort / cycle detect",
        "Directed dependencies.",
        "Cycle => False. Kahn: repeatedly take indegree-0.",
        "2, [[1,0]] True; [[1,0],[0,1]] False",
        "I'll topo-sort; if I can't take all courses, there's a cycle.",
        "Time O(V+E), Space O(V+E)",
        "indegree queue BFS",
        """
from collections import defaultdict, deque

def can_finish(num_courses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * num_courses
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1
    q = deque([i for i in range(num_courses) if indegree[i] == 0])
    taken = 0
    # >>> YOU
    pass
    return taken == num_courses
""",
        """
from collections import defaultdict, deque

def can_finish(num_courses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * num_courses
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1
    q = deque([i for i in range(num_courses) if indegree[i] == 0])
    taken = 0
    while q:
        course = q.popleft()
        taken += 1
        for nxt in graph[course]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    return taken == num_courses
""",
        "can_finish",
        [
            {"args": [2, [[1, 0]]], "expect": True},
            {"args": [2, [[1, 0], [0, 1]]], "expect": False},
            {"args": [1, []], "expect": True},
        ],
        lc=207,
    ),
    # -------- Intervals --------
    P(
        "in-merge-intervals",
        "Merge Intervals",
        "intervals",
        "medium",
        "Sort + greedy merge",
        "Sort unlocks linear scans.",
        "Sort by start; merge when next.start <= cur.end.",
        "[[1,3],[2,6],[8,10]] -> [[1,6],[8,10]]",
        "Sort by start, then extend or append.",
        "Time O(n log n), Space O(n)",
        "if start<=last_end: extend else append",
        """
def merge(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0][:]]
    for start, end in intervals[1:]:
        # >>> YOU
        pass
    return merged
""",
        """
def merge(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0][:]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
""",
        "merge",
        [
            {
                "args": [[[1, 3], [2, 6], [8, 10], [15, 18]]],
                "expect": [[1, 6], [8, 10], [15, 18]],
            },
            {"args": [[[1, 4], [4, 5]]], "expect": [[1, 5]]},
        ],
        lc=56,
    ),
    # -------- DP --------
    P(
        "dp-climbing-stairs",
        "Climbing Stairs",
        "dp-1d",
        "easy",
        "1-D DP / Fibonacci",
        "Reach n from n-1 or n-2.",
        "dp[i] = dp[i-1] + dp[i-2].",
        "n=3 -> 3 ways",
        "Ways to reach i is sum of ways to reach i-1 and i-2.",
        "Time O(n), Space O(1)",
        "a,b = b, a+b rolling",
        """
def climb_stairs(n):
    # >>> YOU
    pass
""",
        """
def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
""",
        "climb_stairs",
        [
            {"args": [2], "expect": 2},
            {"args": [3], "expect": 3},
            {"args": [5], "expect": 8},
        ],
        lc=70,
    ),
    P(
        "dp-house-robber",
        "House Robber",
        "dp-1d",
        "medium",
        "1-D DP decisions",
        "Climbing stairs summed prior states.",
        "At each house: rob (prev2+val) or skip (prev1).",
        "[1,2,3,1] -> 4",
        "I'll track best if I rob/skip this house using two rolling values.",
        "Time O(n), Space O(1)",
        "rob, skip = skip+x, max(rob,skip) style",
        """
def rob(nums):
    # >>> YOU
    pass
""",
        """
def rob(nums):
    prev2 = 0
    prev1 = 0
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1
""",
        "rob",
        [
            {"args": [[1, 2, 3, 1]], "expect": 4},
            {"args": [[2, 7, 9, 3, 1]], "expect": 12},
        ],
        lc=198,
    ),
    P(
        "dp-coin-change",
        "Coin Change",
        "dp-1d",
        "medium",
        "Unbounded knapsack DP",
        "House robber chose take/skip once. Coins can reuse.",
        "dp[a] = min coins for amount a. Update with each coin.",
        "coins=[1,2,5] amount=11 -> 3",
        "I'll DP bottom-up the fewest coins for each amount up to target.",
        "Time O(amount * n), Space O(amount)",
        "dp[x]=min(dp[x], dp[x-coin]+1)",
        """
def coin_change(coins, amount):
    # >>> YOU
    pass
""",
        """
def coin_change(coins, amount):
    INF = amount + 1
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return -1 if dp[amount] == INF else dp[amount]
""",
        "coin_change",
        [
            {"args": [[1, 2, 5], 11], "expect": 3},
            {"args": [[2], 3], "expect": -1},
            {"args": [[1], 0], "expect": 0},
        ],
        lc=322,
    ),
    # -------- Trees (values as nested lists via simple recursion on arrays? Use leetcode-style lists hard in JSON)
    # We'll use recursive TreeNode built in starter from list level-order helpers in tests via Python side
    # For simplicity: problem statements that take nested list encoding in the function itself.
    P(
        "tr-max-depth",
        "Maximum Depth of Binary Tree",
        "trees",
        "easy",
        "DFS tree depth",
        "Recursion on structure.",
        "depth = 1 + max(left, right). Null -> 0.",
        "TreeNode built from level-order list in the harness.",
        "I'll recurse: empty node is 0, else 1 plus max child depth.",
        "Time O(n), Space O(h)",
        "return 0 if not root else 1+max(dfs L, dfs R)",
        """
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    # >>> YOU
    pass
""",
        """
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
""",
        "max_depth",
        [
            {
                "setup": """
def _build(vals):
    if not vals:
        return None
    nodes = [None if v is None else TreeNode(v) for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root
root = _build([3,9,20,None,None,15,7])
""",
                "call": "max_depth(root)",
                "expect": 3,
            }
        ],
        lc=104,
    ),
    # -------- Linked List --------
    P(
        "ll-reverse-list",
        "Reverse Linked List",
        "linked-list",
        "easy",
        "Iterative pointer flip",
        "Walk a chain with prev/curr.",
        "Flip next pointers: next = curr.next; curr.next = prev; advance.",
        "[1,2,3] -> [3,2,1]",
        "I'll reverse with three pointers — prev, curr, next.",
        "Time O(n), Space O(1)",
        "save next, flip curr.next to prev, advance",
        """
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    # >>> YOU
    pass
""",
        """
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
""",
        "reverse_list",
        [
            {
                "setup": """
def _to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out
def _from_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next
head = _from_list([1,2,3,4,5])
""",
                "call": "_to_list(reverse_list(head))",
                "expect": [5, 4, 3, 2, 1],
            }
        ],
        lc=206,
    ),
    P(
        "ll-has-cycle",
        "Linked List Cycle",
        "linked-list",
        "easy",
        "Floyd tortoise/hare",
        "Two pointers walking a list.",
        "Slow +1, fast +2. If they meet, cycle.",
        "1->2->3->2 has cycle -> True",
        "I'll use Floyd: slow and fast; meet means cycle.",
        "Time O(n), Space O(1)",
        "while fast and fast.next: slow=slow.next; fast=fast.next.next",
        """
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    # >>> YOU
    pass
""",
        """
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
""",
        "has_cycle",
        [
            {
                "setup": """
a = ListNode(1); b = ListNode(2); c = ListNode(3)
a.next = b; b.next = c; c.next = b
""",
                "call": "has_cycle(a)",
                "expect": True,
            },
            {
                "setup": """
a = ListNode(1); b = ListNode(2)
a.next = b
""",
                "call": "has_cycle(a)",
                "expect": False,
            },
        ],
        lc=141,
    ),
    P(
        "ll-merge-two",
        "Merge Two Sorted Lists",
        "linked-list",
        "easy",
        "Dummy + two pointers",
        "Merge two sorted arrays with two indices.",
        "Same idea on nodes — attach the smaller head each step.",
        "[1,2,4]+[1,3,4] -> [1,1,2,3,4,4]",
        "I'll use a dummy head and always advance the smaller list.",
        "Time O(n+m), Space O(1)",
        "if l1.val <= l2.val: take l1 else take l2",
        """
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    # >>> YOU
    pass
""",
        """
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    dummy = ListNode(0)
    cur = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    cur.next = list1 or list2
    return dummy.next
""",
        "merge_two_lists",
        [
            {
                "setup": """
def _to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out
def _from_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next
l1 = _from_list([1,2,4])
l2 = _from_list([1,3,4])
""",
                "call": "_to_list(merge_two_lists(l1, l2))",
                "expect": [1, 1, 2, 3, 4, 4],
            }
        ],
        lc=21,
    ),
    # -------- more Trees --------
    P(
        "tr-invert-tree",
        "Invert Binary Tree",
        "trees",
        "easy",
        "DFS swap children",
        "Max depth walked both children.",
        "Swap left/right recursively (or BFS).",
        "[4,2,7,1,3,6,9] inverted structure",
        "I'll swap children at each node, then recurse.",
        "Time O(n), Space O(h)",
        "root.left, root.right = invert(right), invert(left)",
        """
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    # >>> YOU
    pass
""",
        """
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
""",
        "invert_tree",
        [
            {
                "setup": """
def _build(vals):
    if not vals: return None
    nodes = [None if v is None else TreeNode(v) for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root
def _level(root):
    if not root: return []
    from collections import deque
    q = deque([root]); out = []
    while q:
        n = q.popleft()
        if not n:
            out.append(None); continue
        out.append(n.val)
        q.append(n.left); q.append(n.right)
    while out and out[-1] is None: out.pop()
    return out
root = _build([4,2,7,1,3,6,9])
""",
                "call": "_level(invert_tree(root))",
                "expect": [4, 7, 2, 9, 6, 3, 1],
            }
        ],
        lc=226,
    ),
    P(
        "tr-same-tree",
        "Same Tree",
        "trees",
        "easy",
        "Recursive structural compare",
        "DFS both trees in parallel.",
        "Values equal AND left same AND right same.",
        "[1,2,3] vs [1,2,3] -> True",
        "I'll recurse: null match, else vals + both subtrees.",
        "Time O(n), Space O(h)",
        "if not p and not q: True; if not p or not q: False",
        """
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p, q):
    # >>> YOU
    pass
""",
        """
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
""",
        "is_same_tree",
        [
            {
                "setup": """
def _build(vals):
    if not vals: return None
    nodes = [None if v is None else TreeNode(v) for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root
p = _build([1,2,3]); q = _build([1,2,3])
""",
                "call": "is_same_tree(p, q)",
                "expect": True,
            },
            {
                "setup": """
def _build(vals):
    if not vals: return None
    nodes = [None if v is None else TreeNode(v) for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root
p = _build([1,2]); q = _build([1,None,2])
""",
                "call": "is_same_tree(p, q)",
                "expect": False,
            },
        ],
        lc=100,
    ),
    P(
        "tr-level-order",
        "Binary Tree Level Order Traversal",
        "trees",
        "medium",
        "BFS queue by level",
        "DFS knows one path; BFS knows layers.",
        "Queue: for each level size, drain that many nodes.",
        "[3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]",
        "I'll BFS and group by level using queue length.",
        "Time O(n), Space O(n)",
        "for _ in range(len(q)): pop and enqueue children",
        """
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    # >>> YOU
    pass
""",
        """
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []
    q = deque([root])
    out = []
    while q:
        level = []
        for _ in range(len(q)):
            n = q.popleft()
            level.append(n.val)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        out.append(level)
    return out
""",
        "level_order",
        [
            {
                "setup": """
def _build(vals):
    if not vals: return None
    nodes = [None if v is None else TreeNode(v) for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root
root = _build([3,9,20,None,None,15,7])
""",
                "call": "level_order(root)",
                "expect": [[3], [9, 20], [15, 7]],
            }
        ],
        lc=102,
    ),
    P(
        "tr-lca-bst",
        "Lowest Common Ancestor of a BST",
        "trees",
        "medium",
        "BST property walk",
        "BST left < root < right.",
        "If both < root go left; both > root go right; else root is LCA.",
        "root=6, p=2,q=8 -> 6",
        "I'll walk using BST order until the split point.",
        "Time O(h), Space O(1)",
        "while True: if both < go left; both > go right; else return",
        """
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    # >>> YOU
    pass
""",
        """
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
""",
        "lowest_common_ancestor",
        [
            {
                "setup": """
def _build(vals):
    if not vals: return None
    nodes = [None if v is None else TreeNode(v) for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root
root = _build([6,2,8,0,4,7,9,None,None,3,5])
p = TreeNode(2); q = TreeNode(8)
""",
                "call": "lowest_common_ancestor(root, p, q).val",
                "expect": 6,
            }
        ],
        lc=235,
    ),
    # -------- Backtracking --------
    P(
        "bt-subsets",
        "Subsets",
        "backtracking",
        "medium",
        "Include / exclude DFS",
        "Decision trees: take or skip.",
        "At each index: append path copy; recurse with/without nums[i].",
        "[1,2] -> [[],[1],[2],[1,2]]",
        "I'll backtrack include/exclude for every index.",
        "Time O(n*2^n), Space O(n)",
        "dfs(i): append copy; for j from i: push, dfs(j+1), pop",
        """
def subsets(nums):
    # >>> YOU
    pass
""",
        """
def subsets(nums):
    out = []
    path = []
    def dfs(start):
        out.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
    dfs(0)
    return out
""",
        "subsets",
        [
            {"args": [[1, 2]], "expectGroups": [[], [1], [2], [1, 2]]},
            {"args": [[0]], "expectGroups": [[], [0]]},
        ],
        lc=78,
    ),
    P(
        "bt-permutations",
        "Permutations",
        "backtracking",
        "medium",
        "Swap / used-set DFS",
        "Subsets chose include/exclude. Perms choose order.",
        "Build path; skip used indices; recurse until len==n.",
        "[1,2,3] has 6 perms",
        "I'll DFS building a path, skipping indices already used.",
        "Time O(n*n!), Space O(n)",
        "if len(path)==n: record; else try unused nums",
        """
def permute(nums):
    # >>> YOU
    pass
""",
        """
def permute(nums):
    out = []
    path = []
    used = [False] * len(nums)
    def dfs():
        if len(path) == len(nums):
            out.append(path[:])
            return
        for i, x in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(x)
            dfs()
            path.pop()
            used[i] = False
    dfs()
    return out
""",
        "permute",
        [
            {"args": [[1, 2, 3]], "expectGroups": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]},
        ],
        lc=46,
    ),
    P(
        "bt-combination-sum",
        "Combination Sum",
        "backtracking",
        "medium",
        "Reuse candidates DFS",
        "Subsets / coin change thinking: can reuse.",
        "From start index, try each coin; recurse with same i (reuse); subtract target.",
        "candidates=[2,3,6,7] target=7 -> [[2,2,3],[7]]",
        "I'll DFS from index i, reuse allowed by not incrementing i.",
        "Time exponential, Space O(target)",
        "dfs(i, remain): if 0 record; for j from i: push, dfs(j), pop",
        """
def combination_sum(candidates, target):
    # >>> YOU
    pass
""",
        """
def combination_sum(candidates, target):
    out = []
    path = []
    def dfs(start, remain):
        if remain == 0:
            out.append(path[:])
            return
        if remain < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            dfs(i, remain - candidates[i])
            path.pop()
    dfs(0, target)
    return out
""",
        "combination_sum",
        [
            {"args": [[2, 3, 6, 7], 7], "expectGroups": [[2, 2, 3], [7]]},
            {"args": [[2, 3, 5], 8], "expectGroups": [[2, 2, 2, 2], [2, 3, 3], [3, 5]]},
        ],
        lc=39,
    ),
    # -------- Greedy / Intervals / more Stack / Window --------
    P(
        "gd-jump-game",
        "Jump Game",
        "greedy",
        "medium",
        "Reach farthest greedy",
        "Scan once tracking a bound.",
        "Track farthest reachable index; fail if i > farthest.",
        "[2,3,1,1,4] -> True; [3,2,1,0,4] -> False",
        "I'll track farthest; if I ever stand beyond it, False.",
        "Time O(n), Space O(1)",
        "farthest = max(farthest, i + nums[i])",
        """
def can_jump(nums):
    # >>> YOU
    pass
""",
        """
def can_jump(nums):
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + jump)
    return True
""",
        "can_jump",
        [
            {"args": [[2, 3, 1, 1, 4]], "expect": True},
            {"args": [[3, 2, 1, 0, 4]], "expect": False},
        ],
        lc=55,
    ),
    P(
        "in-non-overlap",
        "Non-overlapping Intervals",
        "intervals",
        "medium",
        "Sort + greedy erase",
        "Merge intervals sorted by start.",
        "Sort by end; count overlaps when next.start < last_end.",
        "[[1,2],[2,3],[3,4],[1,3]] remove 1",
        "I'll sort by end and greedily keep non-overlapping.",
        "Time O(n log n), Space O(1)",
        "sort by end; if start >= end keep else remove++",
        """
def erase_overlap_intervals(intervals):
    # >>> YOU
    pass
""",
        """
def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda x: x[1])
    end = float("-inf")
    remove = 0
    for s, e in intervals:
        if s >= end:
            end = e
        else:
            remove += 1
    return remove
""",
        "erase_overlap_intervals",
        [
            {"args": [[[1, 2], [2, 3], [3, 4], [1, 3]]], "expect": 1},
            {"args": [[[1, 2], [1, 2], [1, 2]]], "expect": 2},
        ],
        lc=435,
    ),
    P(
        "st-min-stack",
        "Min Stack",
        "stack",
        "medium",
        "Aux stack for running min",
        "Normal stack push/pop.",
        "Second stack tracks current minimum after each push.",
        "push -2,0,-3; getMin=-3; pop; top=0; getMin=-2",
        "I'll keep a second stack of mins so getMin is O(1).",
        "Time O(1) ops, Space O(n)",
        "on push: mins.append(min(x, mins[-1] if mins else x))",
        """
class MinStack:
    def __init__(self):
        # >>> YOU
        pass
    def push(self, val):
        pass
    def pop(self):
        pass
    def top(self):
        pass
    def getMin(self):
        pass
""",
        """
class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []
    def push(self, val):
        self.stack.append(val)
        self.mins.append(val if not self.mins else min(val, self.mins[-1]))
    def pop(self):
        self.stack.pop()
        self.mins.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.mins[-1]
""",
        "MinStack",
        [
            {
                "setup": """
s = MinStack()
s.push(-2); s.push(0); s.push(-3)
a = s.getMin(); s.pop(); b = s.top(); c = s.getMin()
""",
                "call": "[a, b, c]",
                "expect": [-3, 0, -2],
            }
        ],
        lc=155,
    ),
    P(
        "sw-max-avg-subarray",
        "Maximum Average Subarray I",
        "sliding-window",
        "easy",
        "Fixed window sum",
        "Min subarray length was variable window.",
        "Fixed k: slide sum -= left; += right; track max avg.",
        "[1,12,-5,-6,50,3] k=4 -> 12.75",
        "I'll keep a fixed window of size k and track max average.",
        "Time O(n), Space O(1)",
        "window sum slide by 1",
        """
def find_max_average(nums, k):
    # >>> YOU
    pass
""",
        """
def find_max_average(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best / k
""",
        "find_max_average",
        [
            {"args": [[1, 12, -5, -6, 50, 3], 4], "expect": 12.75},
            {"args": [[5], 1], "expect": 5.0},
        ],
        lc=643,
    ),
    P(
        "ah-encode-decode",
        "Encode and Decode Strings",
        "arrays-hashing",
        "medium",
        "Length-prefix protocol",
        "Join with delimiter breaks if delimiter is in strings.",
        "Encode each as len#str so decode is unambiguous.",
        "['lint','code'] <-> '4#lint4#code'",
        "I'll length-prefix each string so decode is O(n).",
        "Time O(n), Space O(n)",
        "encode: f'{len(s)}#{s}'; decode walk integers",
        """
def encode(strs):
    # >>> YOU
    pass

def decode(s):
    # >>> YOU
    pass
""",
        """
def encode(strs):
    return "".join(f"{len(x)}#{x}" for x in strs)

def decode(s):
    out = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        out.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length
    return out
""",
        "encode",
        [
            {
                "setup": "payload = encode(['lint','code','love','you'])",
                "call": "decode(payload)",
                "expect": ["lint", "code", "love", "you"],
            },
            {
                "setup": "payload = encode(['','a','#b'])",
                "call": "decode(payload)",
                "expect": ["", "a", "#b"],
            },
        ],
        lc=271,
    ),
    P(
        "bs-search-2d",
        "Search a 2D Matrix",
        "binary-search",
        "medium",
        "Treat matrix as sorted array",
        "Classic binary search on 1D.",
        "Index mid // cols, mid % cols — same binary search.",
        "[[1,3,5],[7,9,11]] target 9 -> True",
        "I'll binary search as if the matrix were flattened.",
        "Time O(log(m*n)), Space O(1)",
        "lo/hi on 0..m*n-1; map to row/col",
        """
def search_matrix(matrix, target):
    # >>> YOU
    pass
""",
        """
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // n][mid % n]
        if val == target:
            return True
        if val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
""",
        "search_matrix",
        [
            {"args": [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3], "expect": True},
            {"args": [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13], "expect": False},
        ],
        lc=74,
    ),
    P(
        "hp-last-stone",
        "Last Stone Weight",
        "heap",
        "easy",
        "Max-heap smash",
        "Kth largest used heap for ranking.",
        "Repeatedly smash two heaviest; push difference.",
        "[2,7,4,1,8,1] -> 1",
        "I'll max-heap smash until ≤1 stone left.",
        "Time O(n log n), Space O(n)",
        "heapq with negatives for max-heap",
        """
import heapq

def last_stone_weight(stones):
    # >>> YOU
    pass
""",
        """
import heapq

def last_stone_weight(stones):
    h = [-s for s in stones]
    heapq.heapify(h)
    while len(h) > 1:
        a = -heapq.heappop(h)
        b = -heapq.heappop(h)
        if a != b:
            heapq.heappush(h, -(a - b))
    return -h[0] if h else 0
""",
        "last_stone_weight",
        [
            {"args": [[2, 7, 4, 1, 8, 1]], "expect": 1},
            {"args": [[1]], "expect": 1},
        ],
        lc=1046,
    ),
    P(
        "gr-clone-graph",
        "Clone Graph",
        "graphs",
        "medium",
        "DFS/BFS + hash map copy",
        "Visited set on graphs. Now copy nodes.",
        "Map old->new; recurse neighbors attaching clones.",
        "1--2 / |  | / 4--3 cloned structure",
        "I'll DFS with a dict old node -> cloned node.",
        "Time O(n+e), Space O(n)",
        "if node in map return clone; else create and recurse neighbors",
        """
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node):
    # >>> YOU
    pass
""",
        """
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node):
    if not node:
        return None
    clones = {}
    def dfs(n):
        if n in clones:
            return clones[n]
        copy = Node(n.val)
        clones[n] = copy
        for nb in n.neighbors:
            copy.neighbors.append(dfs(nb))
        return copy
    return dfs(node)
""",
        "clone_graph",
        [
            {
                "setup": """
n1=Node(1); n2=Node(2); n3=Node(3); n4=Node(4)
n1.neighbors=[n2,n4]; n2.neighbors=[n1,n3]; n3.neighbors=[n2,n4]; n4.neighbors=[n1,n3]
c = clone_graph(n1)
""",
                "call": "[c.val, sorted(x.val for x in c.neighbors), c is not n1]",
                "expect": [1, [2, 4], True],
            }
        ],
        lc=133,
    ),
    P(
        "dp-longest-palindrome-subseq",
        "Longest Palindromic Subsequence",
        "dp-1d",
        "medium",
        "2D DP / LCS with reverse",
        "Palindrome two pointers on contiguous. Here gaps allowed.",
        "LPS(s) = LCS(s, reverse(s)).",
        "'bbbab' -> 4",
        "I'll compute LCS of s and reverse(s).",
        "Time O(n^2), Space O(n^2)",
        "dp[i][j] from LCS template",
        """
def longest_palindrome_subseq(s):
    # >>> YOU
    pass
""",
        """
def longest_palindrome_subseq(s):
    t = s[::-1]
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][n]
""",
        "longest_palindrome_subseq",
        [
            {"args": ["bbbab"], "expect": 4},
            {"args": ["cbbd"], "expect": 2},
        ],
        lc=516,
    ),
    # -------- Amazon stories --------
    P(
        "am-top-k-keywords",
        "Top K Keywords (Amazon story)",
        "amazon-story",
        "medium",
        "Count + tie-break sort",
        "Top K Frequent on numbers.",
        "Same count — but ties: lexicographically smaller keyword ranks higher.",
        "['i','love','leetcode','i','love','coding'] k=2 -> ['i','love']",
        "Strip the story: Counter + sort by (-freq, word).",
        "Time O(n + u log u), Space O(u)",
        "sorted(keys, key=lambda w: (-freq[w], w))[:k]",
        """
from collections import Counter

def top_k_keywords(keywords, k):
    # >>> YOU
    pass
""",
        """
from collections import Counter

def top_k_keywords(keywords, k):
    freq = Counter(keywords)
    ranked = sorted(freq.keys(), key=lambda w: (-freq[w], w))
    return ranked[:k]
""",
        "top_k_keywords",
        [
            {
                "args": [["i", "love", "leetcode", "i", "love", "coding"], 2],
                "expect": ["i", "love"],
            },
            {"args": [["a", "b", "a", "c", "b", "a"], 2], "expect": ["a", "b"]},
        ],
        lc=None,
    ),
    P(
        "am-optimal-utilization",
        "Optimal Utilization (Amazon story)",
        "amazon-story",
        "medium",
        "Two pointer / sort pairs near target",
        "Two Sum / two pointers on sorted values.",
        "Pair forward+return ids whose sum is closest to target without exceeding.",
        "forward=[[1,2],[2,4]] return=[[1,3]] target=7 -> [[2,1]] (4+3)",
        "Strip story: sort both; two pointers; track best sum <= target.",
        "Time O(n log n + m log m), Space O(1) excluding output",
        "sort; i=0 j=m-1; update best when sum<=target",
        """
def optimal_utilization(forward, returns, target):
    # >>> YOU
    pass
""",
        """
def optimal_utilization(forward, returns, target):
    forward = sorted(forward, key=lambda x: x[1])
    returns = sorted(returns, key=lambda x: x[1])
    i, j = 0, len(returns) - 1
    best = -1
    out = []
    while i < len(forward) and j >= 0:
        s = forward[i][1] + returns[j][1]
        if s > target:
            j -= 1
            continue
        if s > best:
            best = s
            out = [[forward[i][0], returns[j][0]]]
        elif s == best:
            out.append([forward[i][0], returns[j][0]])
        i += 1
    return out
""",
        "optimal_utilization",
        [
            {
                "args": [[[1, 2], [2, 4], [3, 6]], [[1, 2]], 7],
                "expect": [[2, 1]],
            },
            {
                "args": [[[1, 3], [2, 5], [3, 7], [4, 10]], [[1, 2], [2, 3], [3, 4], [4, 5]], 10],
                "expectGroups": [[2, 4], [3, 2]],
            },
        ],
        lc=None,
    ),
]


def enrich(problem: dict) -> dict:
    """Attach NeetCode-style prompt / examples / mockups when available."""
    lesson = neetcode_examples.get(problem["id"])
    if lesson:
        problem["prompt"] = lesson["prompt"]
        problem["examples"] = lesson["examples"]
        problem["constraints"] = lesson.get("constraints", "")
    else:
        problem.setdefault("prompt", "")
        problem.setdefault("constraints", "")
        # Fallback: synthesize plain examples from first tests
        examples = []
        for t in problem.get("tests", [])[:2]:
            if "args" in t:
                examples.append(
                    {
                        "input": ", ".join(repr(a) for a in t["args"]),
                        "output": repr(t.get("expect", t.get("expectSet", t.get("expectGroups", "?")))),
                        "explanation": "See pattern bridge + TRACE for the walkthrough.",
                        "mockup": problem.get("trace", ""),
                    }
                )
        problem.setdefault("examples", examples)
    guide = python_pattern_guides.get_guide(problem["id"], problem["category"])
    guide["whenToUse"] = real_world_hooks.merge_into(
        when_to_use.get_problem_when(problem["id"], problem["category"]),
        problem["id"],
    )
    problem["patternGuide"] = guide
    return problem


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    problems = [enrich(dict(p)) for p in PROBLEMS]
    with_examples = sum(1 for p in problems if p.get("examples"))
    with_mockups = sum(
        1 for p in problems for e in p.get("examples", []) if e.get("mockup")
    )
    with_code = sum(1 for p in problems if p.get("patternGuide", {}).get("template"))
    payload = {
        "roadmap": [{"id": cid, "title": title} for title, cid in ROADMAP],
        "problems": problems,
        "patternPicker": when_to_use.build_picker(),
        "meta": {
            "goal": 100,
            "count": len(problems),
            "examples": with_examples,
            "mockups": with_mockups,
            "codeWalks": with_code,
            "note": "NeetCode-style: intuition + algorithm + blank template. Full solution only via Hint/Solution after you try.",
        },
    }
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {len(problems)} problems -> {OUT}")
    print(
        f"Examples {with_examples}/{len(problems)} · code walks {with_code} · ASCII mockups {with_mockups}"
    )
    print(f"Progress toward top-100 style bank: {len(problems)}/100")


if __name__ == "__main__":
    main()

"""
NeetCode-style prompts, sample I/O, explanations, ASCII + Python code mockups.

Merged into problems.json by seed_problems.py.
"""

from __future__ import annotations


def Ex(inp: str, out: str, explanation: str, mockup: str = "", code: str = "") -> dict:
    return {
        "input": inp.strip("\n"),
        "output": out.strip("\n"),
        "explanation": explanation.strip("\n"),
        "mockup": mockup.strip("\n"),
        "code": code.strip("\n"),
    }


def Lesson(
    prompt: str,
    examples: list[dict],
    constraints: str = "",
) -> dict:
    return {
        "prompt": prompt.strip("\n"),
        "examples": examples,
        "constraints": constraints.strip("\n"),
    }


# ---------------------------------------------------------------------------
# Catalog keyed by problem id
# ---------------------------------------------------------------------------

CATALOG: dict[str, dict] = {
    "ah-contains-duplicate": Lesson(
        """Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.""",
        [
            Ex(
                "nums = [1, 2, 3, 1]",
                "true",
                "The value `1` appears at index 0 and again at index 3.",
                """
  nums:  [ 1 | 2 | 3 | 1 ]
           ^           ^
           same value → duplicate → true

  seen walk:
    1 → {} add 1
    2 → {1} add 2
    3 → {1,2} add 3
    1 → {1,2,3}  already in set → True
""",
            ),
            Ex(
                "nums = [1, 2, 3, 4]",
                "false",
                "All values are distinct.",
                """
  nums:  [ 1 | 2 | 3 | 4 ]
  seen grows {1}→{1,2}→{1,2,3}→{1,2,3,4}
  never hits a repeat → false
""",
            ),
            Ex(
                "nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]",
                "true",
                "`1` (and later other values) repeats.",
                "",
            ),
        ],
        "1 <= nums.length <= 10^5\n-10^9 <= nums[i] <= 10^9",
    ),
    "ah-valid-anagram": Lesson(
        """Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.""",
        [
            Ex(
                's = "anagram", t = "nagaram"',
                "true",
                "Both strings have the same character counts.",
                """
  s: a n a g r a m     counts: a:3 n:1 g:1 r:1 m:1
  t: n a g a r a m     counts: a:3 n:1 g:1 r:1 m:1
                       maps equal → true
""",
            ),
            Ex(
                's = "rat", t = "car"',
                "false",
                "`t` uses 'c' instead of 't'.",
                """
  s: r:1 a:1 t:1
  t: c:1 a:1 r:1
  t≠s → false
""",
            ),
        ],
        "1 <= s.length, t.length <= 5 * 10^4\ns and t consist of lowercase English letters.",
    ),
    "ah-two-sum": Lesson(
        """Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.

You may assume that each input has **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.""",
        [
            Ex(
                "nums = [2, 7, 11, 15], target = 9",
                "[0, 1]",
                "Because nums[0] + nums[1] == 2 + 7 == 9, we return [0, 1].",
                """
  target = 9

  i=0  num=2   need 7   seen={}        store 2→0
  i=1  num=7   need 2   seen={2:0}     2 is in seen → [0,1]

       [ 2 | 7 | 11 | 15 ]
         ↑   ↑
         0   1   sum to 9
""",
            ),
            Ex(
                "nums = [3, 2, 4], target = 6",
                "[1, 2]",
                "nums[1] + nums[2] == 2 + 4 == 6.",
                """
  i=0  3  need 3  store 3→0
  i=1  2  need 4  store 2→1
  i=2  4  need 2  found at 1 → [1,2]
""",
            ),
            Ex(
                "nums = [3, 3], target = 6",
                "[0, 1]",
                "Both 3's form the pair (different indices).",
                "",
            ),
        ],
        "2 <= nums.length <= 10^4\n-10^9 <= nums[i] <= 10^9\n-10^9 <= target <= 10^9\nOnly one valid answer exists.",
    ),
    "ah-group-anagrams": Lesson(
        """Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.""",
        [
            Ex(
                'strs = ["eat","tea","tan","ate","nat","bat"]',
                '[["bat"],["nat","tan"],["ate","eat","tea"]]',
                "Strings with the same sorted signature (or count key) land in the same bucket.",
                """
  word → sorted key → bucket
  eat  → aet        → [eat]
  tea  → aet        → [eat, tea]
  tan  → ant        → [tan]
  ate  → aet        → [eat, tea, ate]
  nat  → ant        → [tan, nat]
  bat  → abt        → [bat]

  buckets:  aet:[eat,tea,ate]  ant:[tan,nat]  abt:[bat]
""",
            ),
            Ex(
                'strs = [""]',
                '[[""]]',
                "Single empty string is its own group.",
                "",
            ),
            Ex(
                'strs = ["a"]',
                '[["a"]]',
                "Single character group.",
                "",
            ),
        ],
        "1 <= strs.length <= 10^4\n0 <= strs[i].length <= 100\nstrs[i] consists of lowercase English letters.",
    ),
    "ah-top-k-frequent": Lesson(
        """Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.""",
        [
            Ex(
                "nums = [1, 1, 1, 2, 2, 3], k = 2",
                "[1, 2]",
                "`1` appears 3 times, `2` appears 2 times — those are the top 2.",
                """
  Phase 1 — count (like Contains Duplicate, but store counts):
    1 → 3,  2 → 2,  3 → 1

  Phase 2 — rank by frequency (NOT Group Anagrams):
    freq 3: [1]
    freq 2: [2]
    freq 1: [3]
    take top k=2 → [1, 2]
""",
            ),
            Ex(
                "nums = [1], k = 1",
                "[1]",
                "Only one element exists.",
                "",
            ),
        ],
        "1 <= nums.length <= 10^5\nk is in the range [1, the number of unique elements in the array].\nIt is guaranteed that the answer is unique.",
    ),
    "ah-product-except-self": Lesson(
        """Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.""",
        [
            Ex(
                "nums = [1, 2, 3, 4]",
                "[24, 12, 8, 6]",
                "For index 0: 2*3*4=24; index 1: 1*3*4=12; and so on.",
                """
  nums:     [ 1 | 2 | 3 | 4 ]

  left:     [ 1 | 1 | 2 | 6 ]     prefix products (exclude self)
  right:    [24 |12 | 4 | 1 ]     suffix products
  answer:   [24 |12 | 8 | 6 ]     left[i] * right[i]
""",
            ),
            Ex(
                "nums = [-1, 1, 0, -3, 3]",
                "[0, 0, 9, 0, 0]",
                "The zero forces most products to 0; only index 2 multiplies nonzeros.",
                "",
            ),
        ],
        "2 <= nums.length <= 10^5\n-30 <= nums[i] <= 30\nThe product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.",
    ),
    "ah-longest-consecutive": Lesson(
        """Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.""",
        [
            Ex(
                "nums = [100, 4, 200, 1, 3, 2]",
                "4",
                "The longest consecutive sequence is `[1, 2, 3, 4]`. Therefore its length is 4.",
                """
  set = {100, 4, 200, 1, 3, 2}

  Only start a streak when (x-1) NOT in set:
    1 is a start (0 missing): 1→2→3→4  length 4
    100 start: length 1
    200 start: length 1
  best = 4
""",
            ),
            Ex(
                "nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]",
                "9",
                "The longest sequence is `[0,1,2,3,4,5,6,7,8]`.",
                "",
            ),
        ],
        "0 <= nums.length <= 10^5\n-10^9 <= nums[i] <= 10^9",
    ),
    "ah-subarray-sum-k": Lesson(
        """Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.""",
        [
            Ex(
                "nums = [1, 1, 1], k = 2",
                "2",
                "The subarrays `[1,1]` (indices 0–1) and `[1,1]` (indices 1–2) both sum to 2.",
                """
  prefix: 0 → 1 → 2 → 3
  At prefix=2, need prefix-k=0 → seen once → +1  (subarray [1,1])
  At prefix=3, need 1 → seen once → +1            (subarray [1,1])
  answer = 2

  (Two Sum idea: complement on prefix sums)
""",
            ),
            Ex(
                "nums = [1, 2, 3], k = 3",
                "2",
                "`[1,2]` and `[3]` both sum to 3.",
                "",
            ),
        ],
        "1 <= nums.length <= 2 * 10^4\n-1000 <= nums[i] <= 1000\n-10^7 <= k <= 10^7",
    ),
    "ah-encode-decode": Lesson(
        """Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Implement `encode` and `decode`.""",
        [
            Ex(
                'strs = ["lint","code","love","you"]',
                'encode → "4#lint4#code4#love3#you"\ndecode → ["lint","code","love","you"]',
                "Length-prefix avoids ambiguity if '#' appears inside a string.",
                """
  "lint" → "4#lint"
  "code" → "4#code"
  join:  4#lint 4#code 4#love 3#you

  decode walk:
    read int until '#', then take that many chars
""",
            ),
            Ex(
                'strs = ["","a","#b"]',
                '["","a","#b"] after round-trip',
                "Empty string and embedded `#` still round-trip correctly.",
                "",
            ),
        ],
        "0 <= strs.length < 100\n0 <= strs[i].length < 200\nstrs[i] contains any possible characters out of 256 valid ASCII characters.",
    ),
    "tp-valid-palindrome": Lesson(
        """A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.""",
        [
            Ex(
                's = "A man, a plan, a canal: Panama"',
                "true",
                '"amanaplanacanalpanama" is a palindrome.',
                """
  cleaned: a m a n a p l a n a c a n a l p a n a m a
           L→                                       ←R
  compare pairs moving inward — all match → true
""",
            ),
            Ex(
                's = "race a car"',
                "false",
                '"raceacar" is not a palindrome.',
                "",
            ),
        ],
        "1 <= s.length <= 2 * 10^5\ns consists only of printable ASCII characters.",
    ),
    "tp-two-sum-ii": Lesson(
        """Given a **1-indexed** array of integers `numbers` that is already **sorted** in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, **added by one** as an integer array `[index1, index2]` of length 2.

Your solution must use only constant extra space.""",
        [
            Ex(
                "numbers = [2, 7, 11, 15], target = 9",
                "[1, 2]",
                "The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.",
                """
  L=0 (2)   R=3 (15)   sum=17 > 9 → R--
  L=0 (2)   R=2 (11)   sum=13 > 9 → R--
  L=0 (2)   R=1 (7)    sum=9  → return [1,2] (1-indexed)
""",
            ),
            Ex(
                "numbers = [2, 3, 4], target = 6",
                "[1, 3]",
                "2 + 4 = 6.",
                "",
            ),
        ],
        "2 <= numbers.length <= 3 * 10^4\n-1000 <= numbers[i] <= 1000\nnumbers is sorted in non-decreasing order.\n-1000 <= target <= 1000\nThe tests are generated such that there is exactly one solution.",
    ),
    "tp-3sum": Lesson(
        """Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.""",
        [
            Ex(
                "nums = [-1, 0, 1, 2, -1, -4]",
                "[[-1, -1, 2], [-1, 0, 1]]",
                "The distinct triplets that sum to 0.",
                """
  sort: [-4, -1, -1, 0, 1, 2]

  fix i=-1, two-pointer L/R on rest:
    -1 + -1 + 2 = 0  ✓
    -1 +  0 + 1 = 0  ✓
  skip duplicate i values
""",
            ),
            Ex(
                "nums = [0, 1, 1]",
                "[]",
                "The only possible triplet does not sum to 0.",
                "",
            ),
            Ex(
                "nums = [0, 0, 0]",
                "[[0, 0, 0]]",
                "The only possible triplet sums to 0.",
                "",
            ),
        ],
        "3 <= nums.length <= 3000\n-10^5 <= nums[i] <= 10^5",
    ),
    "tp-container-water": Lesson(
        """You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Notice** that you may not slant the container.""",
        [
            Ex(
                "height = [1, 8, 6, 2, 5, 4, 8, 3, 7]",
                "49",
                "The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.",
                """
        |           |
        |     |     |         |
        | |   | | | |   |     |
  idx 0 1 2 3 4 5 6 7 8

  L at h=8 (i=1), R at h=7 (i=8)
  width = 7, min(8,7)=7 → area 49
  move the shorter side inward while tracking max
""",
            ),
            Ex(
                "height = [1, 1]",
                "1",
                "Only one possible container of width 1 and height 1.",
                "",
            ),
        ],
        "n == height.length\n2 <= n <= 10^5\n0 <= height[i] <= 10^4",
    ),
    "sw-best-stock": Lesson(
        """You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.""",
        [
            Ex(
                "prices = [7, 1, 5, 3, 6, 4]",
                "5",
                "Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.",
                """
  day:    1  2  3  4  5  6
  price:  7  1  5  3  6  4
             buy ----↑---- sell
  track min_so_far; at each day max_profit = max(price - min)
""",
            ),
            Ex(
                "prices = [7, 6, 4, 3, 1]",
                "0",
                "No profitable transaction — prices only fall.",
                "",
            ),
        ],
        "1 <= prices.length <= 10^5\n0 <= prices[i] <= 10^4",
    ),
    "sw-longest-substring": Lesson(
        """Given a string `s`, find the length of the **longest substring** without repeating characters.""",
        [
            Ex(
                's = "abcabcbb"',
                "3",
                "The answer is `\"abc\"`, with the length of 3.",
                """
  window grows until repeat; then shrink left past the old copy:

  a b c a b c b b
  [---] len 3
    [---] len 3
      ...
  best = 3
""",
            ),
            Ex(
                's = "bbbbb"',
                "1",
                "The answer is `\"b\"`, with the length of 1.",
                "",
            ),
            Ex(
                's = "pwwkew"',
                "3",
                "The answer is `\"wke\"`, with the length of 3. Notice that the answer must be a substring, `\"pwke\"` is a subsequence and not a substring.",
                "",
            ),
        ],
        "0 <= s.length <= 5 * 10^4\ns consists of English letters, digits, symbols and spaces.",
    ),
    "sw-min-subarray": Lesson(
        """Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.""",
        [
            Ex(
                "target = 7, nums = [2, 3, 1, 2, 4, 3]",
                "2",
                "The subarray `[4, 3]` has the minimal length under the problem constraint.",
                """
  expand R until sum >= target, then shrink L:
    [2,3,1,2] sum=8 len=4
    shrink → ... → [4,3] sum=7 len=2  best=2
""",
            ),
            Ex(
                "target = 4, nums = [1, 4, 4]",
                "1",
                "A single `4` meets the target.",
                "",
            ),
        ],
        "1 <= target <= 10^9\n1 <= nums.length <= 10^5\n1 <= nums[i] <= 10^4",
    ),
    "sw-max-avg-subarray": Lesson(
        """You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value. Any answer with a calculation error less than `10^-5` will be accepted.""",
        [
            Ex(
                "nums = [1, 12, -5, -6, 50, 3], k = 4",
                "12.75000",
                "Maximum average is `(12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75`.",
                """
  fixed window of size 4:
    [1,12,-5,-6] avg 0.5
    [12,-5,-6,50] avg 12.75  ← best
    [-5,-6,50,3] avg 10.5
""",
            ),
            Ex(
                "nums = [5], k = 1",
                "5.00000",
                "Only one possible window.",
                "",
            ),
        ],
        "n == nums.length\n1 <= k <= n <= 10^5\n-10^4 <= nums[i] <= 10^4",
    ),
    "st-valid-parentheses": Lesson(
        """Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.""",
        [
            Ex(
                's = "()"',
                "true",
                "Simple matching pair.",
                """
  stack:  (   → push
          )   → matches ( → pop
  empty → true
""",
            ),
            Ex(
                's = "()[]{}"',
                "true",
                "All pairs close correctly.",
                "",
            ),
            Ex(
                's = "(]"',
                "false",
                "Wrong closing type.",
                """
  stack: ( → push
         ] → expects ) but got ] → false
""",
            ),
        ],
        "1 <= s.length <= 10^4\ns consists of parentheses only '()[]{}'.",
    ),
    "st-daily-temperatures": Lesson(
        """Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.""",
        [
            Ex(
                "temperatures = [73, 74, 75, 71, 69, 72, 76, 73]",
                "[1, 1, 4, 2, 1, 1, 0, 0]",
                "Use a monotonic decreasing stack of indices; when a warmer day arrives, pop and fill waits.",
                """
  day:  0   1   2   3   4   5   6   7
  temp: 73  74  75  71  69  72  76  73
  ans:  1   1   4   2   1   1   0   0
              └── wait 4 days until 76
""",
            ),
            Ex(
                "temperatures = [30, 40, 50, 60]",
                "[1, 1, 1, 0]",
                "Each day is warmer than the previous until the last.",
                "",
            ),
        ],
        "1 <= temperatures.length <= 10^5\n30 <= temperatures[i] <= 100",
    ),
    "st-min-stack": Lesson(
        """Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.""",
        [
            Ex(
                """MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2""",
                "[-3, 0, -2]",
                "A parallel mins stack tracks the running minimum after each push.",
                """
  vals:  -2 → 0 → -3     then pop
  mins:  -2 →-2 → -3         mins → -2

  getMin before pop = -3
  top after pop = 0
  getMin after pop = -2
""",
            ),
        ],
        "-2^31 <= val <= 2^31 - 1\nMethods pop, top and getMin operations will always be called on non-empty stacks.\nAt most 3 * 10^4 calls will be made to push, pop, top, and getMin.",
    ),
    "bs-binary-search": Lesson(
        """Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.""",
        [
            Ex(
                "nums = [-1, 0, 3, 5, 9, 12], target = 9",
                "4",
                "`9` exists in `nums` and its index is `4`.",
                """
  lo=0 hi=5 mid=2 val=3 < 9 → lo=3
  lo=3 hi=5 mid=4 val=9 == target → 4
""",
            ),
            Ex(
                "nums = [-1, 0, 3, 5, 9, 12], target = 2",
                "-1",
                "`2` does not exist in `nums` so return `-1`.",
                "",
            ),
        ],
        "1 <= nums.length <= 10^4\n-10^4 < nums[i], target < 10^4\nAll the integers in nums are unique.\nnums is sorted in ascending order.",
    ),
    "bs-koko": Lesson(
        """Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.""",
        [
            Ex(
                "piles = [3, 6, 7, 11], h = 8",
                "4",
                "With speed 4 she finishes in 8 hours.",
                """
  binary search k on [1 .. max(piles)]:
    k=4 → hours = ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4)
                = 1+2+2+3 = 8  ≤ h → try smaller
  minimum feasible k = 4
""",
            ),
            Ex(
                "piles = [30, 11, 23, 4, 20], h = 5",
                "30",
                "Must eat the largest pile in one hour-ish budget → k=30.",
                "",
            ),
        ],
        "1 <= piles.length <= 10^4\npiles.length <= h <= 10^9\n1 <= piles[i] <= 10^9",
    ),
    "bs-search-2d": Lesson(
        """You are given an `m x n` integer matrix `matrix` with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

You must write a solution in `O(log(m * n))` time complexity.""",
        [
            Ex(
                "matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3",
                "true",
                "Treat as a flattened sorted array of length m*n and binary search.",
                """
  [  1  3  5  7 ]
  [ 10 11 16 20 ]
  [ 23 30 34 60 ]

  mid index → row = mid // cols, col = mid % cols
  target 3 found → true
""",
            ),
            Ex(
                "matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13",
                "false",
                "13 is not present.",
                "",
            ),
        ],
        "m == matrix.length\nn == matrix[i].length\n1 <= m, n <= 100\n-10^4 <= matrix[i][j], target <= 10^4",
    ),
    "ll-reverse-list": Lesson(
        """Given the `head` of a singly linked list, reverse the list, and return the reversed list.""",
        [
            Ex(
                "head = [1, 2, 3, 4, 5]",
                "[5, 4, 3, 2, 1]",
                "Flip each `next` pointer while walking the list.",
                """
  null ← 1 ← 2 ← 3 ← 4 ← 5
         prev/curr walk:

  prev=None  curr=1
  nxt=2; 1.next=None; prev=1; curr=2
  ...
  return prev (5)
""",
            ),
            Ex(
                "head = [1, 2]",
                "[2, 1]",
                "Two-node reverse.",
                "",
            ),
        ],
        "The number of nodes in the list is the range [0, 5000].\n-5000 <= Node.val <= 5000",
    ),
    "ll-has-cycle": Lesson(
        """Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.""",
        [
            Ex(
                "head = [3, 2, 0, -4], pos = 1  (tail connects to node index 1)",
                "true",
                "There is a cycle: the tail connects back to the node with value 2.",
                """
  3 → 2 → 0 → -4
      ↑_________|

  Floyd: slow +1, fast +2; they meet inside the cycle → true
""",
            ),
            Ex(
                "head = [1, 2], pos = 0",
                "true",
                "Tail connects to the head.",
                "",
            ),
            Ex(
                "head = [1], pos = -1",
                "false",
                "No cycle.",
                "",
            ),
        ],
        "The number of the nodes in the list is in the range [0, 10^4].\n-10^5 <= Node.val <= 10^5\npos is -1 or a valid index in the linked-list.",
    ),
    "ll-merge-two": Lesson(
        """You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.""",
        [
            Ex(
                "list1 = [1, 2, 4], list2 = [1, 3, 4]",
                "[1, 1, 2, 3, 4, 4]",
                "Always attach the smaller current head (dummy node technique).",
                """
  dummy → …
     take 1 (l1) → take 1 (l2) → take 2 → take 3 → take 4 → take 4
""",
            ),
            Ex(
                "list1 = [], list2 = []",
                "[]",
                "Both empty.",
                "",
            ),
        ],
        "The number of nodes in both lists is in the range [0, 50].\n-100 <= Node.val <= 100\nBoth list1 and list2 are sorted in non-decreasing order.",
    ),
    "tr-max-depth": Lesson(
        """Given the `root` of a binary tree, return its maximum depth.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.""",
        [
            Ex(
                "root = [3, 9, 20, null, null, 15, 7]",
                "3",
                "Path 3 → 20 → 15 (or 7) has length 3.",
                """
      3          depth 1
     / \\
    9  20        depth 2
       / \\
      15  7      depth 3   → answer 3
""",
            ),
            Ex(
                "root = [1, null, 2]",
                "2",
                "Longest path has 2 nodes.",
                "",
            ),
        ],
        "The number of nodes in the tree is in the range [0, 10^4].\n-100 <= Node.val <= 100",
    ),
    "tr-invert-tree": Lesson(
        """Given the `root` of a binary tree, invert the tree, and return its root.

Mirror every node by swapping left and right children.""",
        [
            Ex(
                "root = [4, 2, 7, 1, 3, 6, 9]",
                "[4, 7, 2, 9, 6, 3, 1]",
                "Swap children at every node.",
                """
      4                 4
     / \\      →        / \\
    2   7             7   2
   / \\ / \\           / \\ / \\
  1  3 6  9         9  6 3  1
""",
            ),
            Ex(
                "root = [2, 1, 3]",
                "[2, 3, 1]",
                "Simple three-node invert.",
                "",
            ),
        ],
        "The number of nodes in the tree is in the range [0, 100].\n-100 <= Node.val <= 100",
    ),
    "tr-same-tree": Lesson(
        """Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.""",
        [
            Ex(
                "p = [1, 2, 3], q = [1, 2, 3]",
                "true",
                "Identical structure and values.",
                """
    1          1
   / \\   ==   / \\
  2   3      2   3
""",
            ),
            Ex(
                "p = [1, 2], q = [1, null, 2]",
                "false",
                "Structure differs (left vs right child).",
                """
    1          1
   /            \\
  2              2
""",
            ),
        ],
        "The number of nodes in both trees is in the range [0, 100].\n-10^4 <= Node.val <= 10^4",
    ),
    "tr-level-order": Lesson(
        """Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).""",
        [
            Ex(
                "root = [3, 9, 20, null, null, 15, 7]",
                "[[3], [9, 20], [15, 7]]",
                "BFS: drain `len(queue)` nodes per level.",
                """
      3            level 0 → [3]
     / \\
    9  20          level 1 → [9, 20]
       / \\
      15  7        level 2 → [15, 7]
""",
            ),
            Ex(
                "root = [1]",
                "[[1]]",
                "Single node.",
                "",
            ),
        ],
        "The number of nodes in the tree is in the range [0, 2000].\n-1000 <= Node.val <= 1000",
    ),
    "tr-lca-bst": Lesson(
        """Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).”""",
        [
            Ex(
                "root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8",
                "6",
                "The LCA of nodes 2 and 8 is 6.",
                """
          6  ← split: p left, q right → LCA
         / \\
        2   8
       / \\ / \\
      0  4 7  9
""",
            ),
            Ex(
                "root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4",
                "2",
                "The LCA of nodes 2 and 4 is 2 (a node can be a descendant of itself).",
                "",
            ),
        ],
        "The number of nodes in the tree is in the range [2, 10^5].\n-10^9 <= Node.val <= 10^9\nAll Node.val are unique.\np != q\np and q will exist in the BST.",
    ),
    "hp-kth-largest": Lesson(
        """Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Can you solve it without sorting?""",
        [
            Ex(
                "nums = [3, 2, 1, 5, 6, 4], k = 2",
                "5",
                "Sorted descending: [6,5,4,3,2,1] → 2nd is 5. Heap of size k also works.",
                """
  min-heap size k:
    push 3,2,1,5 → heap [1,2,3,5] size> k? pop 1 → [2,3,5]
    push 6 → pop 2 → [3,5,6]
    push 4 → pop 3 → [4,5,6]
    peek = 4? wait size k=2: maintain only 2...
  With k=2 min-heap holding largest 2: end peek = 5
""",
            ),
            Ex(
                "nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4",
                "4",
                "4th largest is 4.",
                "",
            ),
        ],
        "1 <= k <= nums.length <= 10^5\n-10^4 <= nums[i] <= 10^4",
    ),
    "hp-last-stone": Lesson(
        """You are given an array of integers `stones` where `stones[i]` is the weight of the `ith` stone.

We are playing a game with the stones. On each turn, we choose the **heaviest two stones** and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:
- If `x == y`, both stones are destroyed.
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is at most 1 stone left.

Return the weight of the last remaining stone. If there are no stones left, return `0`.""",
        [
            Ex(
                "stones = [2, 7, 4, 1, 8, 1]",
                "1",
                "Smash 8 and 7 → 1; continue until one stone weight 1 remains.",
                """
  max-heap: 8,7,4,2,1,1
  smash 8&7 → push 1
  smash 4&2 → push 2
  ...
  last = 1
""",
            ),
            Ex(
                "stones = [1]",
                "1",
                "Already one stone.",
                "",
            ),
        ],
        "1 <= stones.length <= 30\n1 <= stones[i] <= 1000",
    ),
    "gr-num-islands": Lesson(
        """Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.""",
        [
            Ex(
                """grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]""",
                "1",
                "One connected land component.",
                """
  1 1 1 1 0
  1 1 0 1 0
  1 1 0 0 0
  0 0 0 0 0
  └──────── one island (DFS/BFS flood fill)
""",
            ),
            Ex(
                """grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]""",
                "3",
                "Three separate islands.",
                "",
            ),
        ],
        "m == grid.length\nn == grid[i].length\n1 <= m, n <= 300\ngrid[i][j] is '0' or '1'.",
    ),
    "gr-rotting-oranges": Lesson(
        """You are given an `m x n` grid where each cell can have one of three values:
- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.""",
        [
            Ex(
                "grid = [[2,1,1],[1,1,0],[0,1,1]]",
                "4",
                "Multi-source BFS from all initially rotten oranges.",
                """
  minute 0:  2 1 1
             1 1 0
             0 1 1

  minute 1:  2 2 1
             2 1 0
             0 1 1
  ...
  minute 4: all fresh gone → 4
""",
            ),
            Ex(
                "grid = [[2,1,1],[0,1,1],[1,0,1]]",
                "-1",
                "The bottom-left orange never gets reached.",
                "",
            ),
        ],
        "m == grid.length\nn == grid[i].length\n1 <= m, n <= 10\ngrid[i][j] is 0, 1, or 2.",
    ),
    "gr-course-schedule": Lesson(
        """There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

For example, the pair `[0, 1]` indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.""",
        [
            Ex(
                "numCourses = 2, prerequisites = [[1, 0]]",
                "true",
                "Take course 0 then course 1. No cycle.",
                """
  0 → 1   (edge: must take 0 before 1)
  Kahn / DFS cycle detect → no cycle → true
""",
            ),
            Ex(
                "numCourses = 2, prerequisites = [[1, 0], [0, 1]]",
                "false",
                "Cycle: 0 needs 1 and 1 needs 0.",
                """
  0 ⇄ 1  cycle → false
""",
            ),
        ],
        "1 <= numCourses <= 2000\n0 <= prerequisites.length <= 5000\nprerequisites[i].length == 2\n0 <= ai, bi < numCourses\nAll the pairs prerequisites[i] are unique.",
    ),
    "gr-clone-graph": Lesson(
        """Given a reference of a node in a **connected** undirected graph.

Return a **deep copy** (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.""",
        [
            Ex(
                "adjList = [[2,4],[1,3],[2,4],[1,3]]",
                "cloned graph with same structure, different objects",
                "DFS/BFS with a map old→new so each node is copied once.",
                """
  1 —— 2
  |    |
  4 —— 3

  clones[old] = new Node(val)
  then wire neighbors via recursion
""",
            ),
        ],
        "The number of nodes in the graph is in the range [0, 100].\n1 <= Node.val <= 100\nNode.val is unique for each node.\nThere are no repeated edges and no self-loops in the graph.\nThe Graph is connected and all nodes can be visited starting from the given node.",
    ),
    "bt-subsets": Lesson(
        """Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.""",
        [
            Ex(
                "nums = [1, 2, 3]",
                "[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]",
                "At each index: include or skip (backtracking).",
                """
           []
     /     |     \\
    [1]   [2]    [3]
   /  \\     \\
 [1,2][1,3] [2,3]
   |
 [1,2,3]
""",
            ),
            Ex(
                "nums = [0]",
                "[[],[0]]",
                "Empty set plus {[0]}.",
                "",
            ),
        ],
        "1 <= nums.length <= 10\n-10 <= nums[i] <= 10\nAll the numbers of nums are unique.",
    ),
    "bt-permutations": Lesson(
        """Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.""",
        [
            Ex(
                "nums = [1, 2, 3]",
                "[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]",
                "Build a path; skip used indices until length == n.",
                """
  choose 1 → choose 2 → choose 3 → [1,2,3]
           → choose 3 → choose 2 → [1,3,2]
  choose 2 → ...
""",
            ),
            Ex(
                "nums = [0, 1]",
                "[[0,1],[1,0]]",
                "Two permutations.",
                "",
            ),
        ],
        "1 <= nums.length <= 6\n-10 <= nums[i] <= 10\nAll the integers of nums are unique.",
    ),
    "bt-combination-sum": Lesson(
        """Given an array of **distinct** integers `candidates` and a target integer `target`, return a list of all **unique combinations** of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.""",
        [
            Ex(
                "candidates = [2, 3, 6, 7], target = 7",
                "[[2,2,3],[7]]",
                "2+2+3 and 7. Reuse allowed by not advancing the start index.",
                """
  dfs(remain=7):
    take 2 → remain 5 → take 2 → remain 3 → take 3 → 0  record [2,2,3]
    take 7 → remain 0  record [7]
""",
            ),
            Ex(
                "candidates = [2, 3, 5], target = 8",
                "[[2,2,2,2],[2,3,3],[3,5]]",
                "Three unique combinations.",
                "",
            ),
        ],
        "1 <= candidates.length <= 30\n2 <= candidates[i] <= 40\nAll elements of candidates are distinct.\n1 <= target <= 40",
    ),
    "gd-jump-game": Lesson(
        """You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.""",
        [
            Ex(
                "nums = [2, 3, 1, 1, 4]",
                "true",
                "Jump 1 step from index 0 to 1, then 3 steps to the last index.",
                """
  index: 0 1 2 3 4
  jump:  2 3 1 1 4
  farthest track: 2 → 4 (reachable) → True
""",
            ),
            Ex(
                "nums = [3, 2, 1, 0, 4]",
                "false",
                "You will always arrive at index 3 with jump 0; cannot go further.",
                """
  farthest stuck at 3; index 4 never reachable → False
""",
            ),
        ],
        "1 <= nums.length <= 10^4\n0 <= nums[i] <= 10^5",
    ),
    "in-merge-intervals": Lesson(
        """Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.""",
        [
            Ex(
                "intervals = [[1,3],[2,6],[8,10],[15,18]]",
                "[[1,6],[8,10],[15,18]]",
                "Since intervals [1,3] and [2,6] overlap, merge them into [1,6].",
                """
  sort by start:
  [1,3] then [2,6] overlap → merge [1,6]
  [8,10] no overlap
  [15,18] no overlap
""",
            ),
            Ex(
                "intervals = [[1,4],[4,5]]",
                "[[1,5]]",
                "Intervals that touch at an endpoint still merge.",
                "",
            ),
        ],
        "1 <= intervals.length <= 10^4\nintervals[i].length == 2\n0 <= starti <= endi <= 10^4",
    ),
    "in-non-overlap": Lesson(
        """Given an array of intervals `intervals` where `intervals[i] = [starti, endi]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are **non-overlapping**. For example, `[1, 2]` and `[2, 3]` are non-overlapping.""",
        [
            Ex(
                "intervals = [[1,2],[2,3],[3,4],[1,3]]",
                "1",
                "Remove `[1,3]` then the rest don't overlap.",
                """
  sort by end:
  keep [1,2], keep [2,3], keep [3,4], drop overlapping [1,3]
  removals = 1
""",
            ),
            Ex(
                "intervals = [[1,2],[1,2],[1,2]]",
                "2",
                "You need to remove two to leave one.",
                "",
            ),
        ],
        "1 <= intervals.length <= 10^5\nintervals[i].length == 2\n-5 * 10^4 <= starti < endi <= 5 * 10^4",
    ),
    "dp-climbing-stairs": Lesson(
        """You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?""",
        [
            Ex(
                "n = 2",
                "2",
                "1+1 or 2.",
                """
  ways(n) = ways(n-1) + ways(n-2)   (Fibonacci)
  n=1 → 1
  n=2 → 2
""",
            ),
            Ex(
                "n = 3",
                "3",
                "1+1+1, 1+2, 2+1.",
                "",
            ),
        ],
        "1 <= n <= 45",
    ),
    "dp-house-robber": Lesson(
        """You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.""",
        [
            Ex(
                "nums = [1, 2, 3, 1]",
                "4",
                "Rob house 1 (money = 1) and then rob house 3 (money = 3). Total = 4.",
                """
  take/skip recurrence:
  dp[i] = max(dp[i-1], dp[i-2] + nums[i])
  houses: 1  2  3  1
  best:   1  2  4  4
""",
            ),
            Ex(
                "nums = [2, 7, 9, 3, 1]",
                "12",
                "Rob houses 1, 3, and 5 → 2+9+1=12.",
                "",
            ),
        ],
        "1 <= nums.length <= 100\n0 <= nums[i] <= 400",
    ),
    "dp-coin-change": Lesson(
        """You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.""",
        [
            Ex(
                "coins = [1, 2, 5], amount = 11",
                "3",
                "11 = 5 + 5 + 1",
                """
  dp[a] = min coins for amount a
  for a in 1..11:
    try each coin: dp[a] = min(dp[a], dp[a-coin]+1)
  dp[11] = 3
""",
            ),
            Ex(
                "coins = [2], amount = 3",
                "-1",
                "Cannot make 3 with only 2's.",
                "",
            ),
        ],
        "1 <= coins.length <= 12\n1 <= coins[i] <= 2^31 - 1\n0 <= amount <= 10^4",
    ),
    "dp-longest-palindrome-subseq": Lesson(
        """Given a string `s`, find the longest palindromic **subsequence**'s length in `s`.

A **subsequence** is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.""",
        [
            Ex(
                's = "bbbab"',
                "4",
                "One possible longest palindromic subsequence is `\"bbbb\"`.",
                """
  LPS(s) = LCS(s, reverse(s))
  s = bbbab
  rev = babbb
  LCS length = 4
""",
            ),
            Ex(
                's = "cbbd"',
                "2",
                "One possible longest palindromic subsequence is `\"bb\"`.",
                "",
            ),
        ],
        "1 <= s.length <= 1000\ns consists only of lowercase English letters.",
    ),
    "am-top-k-keywords": Lesson(
        """**Amazon-style wrapper.** You are given a list of keywords from customer reviews and an integer `k`.

Return the `k` most frequent keywords. If two keywords have the same frequency, the **lexicographically smaller** keyword ranks higher.

(This is the Top K Frequent pattern with a tie-break — strip the story in interview.)""",
        [
            Ex(
                'keywords = ["i","love","leetcode","i","love","coding"], k = 2',
                '["i","love"]',
                "`i` and `love` both appear twice; `i` comes first lexicographically among ties with coding? Here both beat coding (freq 1). Rank by (-freq, word).",
                """
  counts: i:2 love:2 leetcode:1 coding:1
  sort key: (-freq, word)
  → i, love, coding, leetcode
  top 2 → ["i","love"]
""",
            ),
            Ex(
                'keywords = ["a","b","a","c","b","a"], k = 2',
                '["a","b"]',
                "a appears thrice, b twice.",
                "",
            ),
        ],
        "1 <= keywords.length <= 10^5\n1 <= k <= number of unique keywords",
    ),
    "am-optimal-utilization": Lesson(
        """**Amazon-style wrapper (Optimal Utilization / airplane route pairing).**

You are given two lists of pairs:
- `forwardRoutingList` — `[id, travelDuration]`
- `returnRoutingList` — `[id, travelDuration]`
and an integer `maxTravelDist`.

Return the pair(s) of ids `[forwardId, returnId]` whose durations sum to the largest value **≤ maxTravelDist**. If multiple pairs share that best sum, return all of them.

Strip the story: sorted arrays + two pointers / scan for best sum ≤ target.""",
        [
            Ex(
                "forward = [[1,2],[2,4],[3,6]], return = [[1,2]], target = 7",
                "[[2,1]]",
                "4+2=6 is the best sum ≤ 7 (6+2=8 exceeds).",
                """
  candidates ≤ 7:
    2+2=4, 4+2=6, 6+2=8 ✗
  best = 6 → ids [2,1]
""",
            ),
            Ex(
                "forward = [[1,3],[2,5],[3,7],[4,10]], return = [[1,2],[2,3],[3,4],[4,5]], target = 10",
                "[[2,4],[3,2]]",
                "Both pairs sum to 10.",
                "",
            ),
        ],
        "1 <= n, m <= 10^5 durations are positive integers",
    ),
}


def get(problem_id: str) -> dict | None:
    lesson = CATALOG.get(problem_id)
    if not lesson:
        return None
    # Do not attach full solution code to examples — pattern tab teaches via blanks.
    return {
        "prompt": lesson["prompt"],
        "constraints": lesson.get("constraints", ""),
        "examples": [dict(ex) for ex in lesson["examples"]],
    }

"""
NeetCode-style pattern guides — teach HOW to think, not the answer.

Shows: intuition, brute force, algorithm steps, template WITH BLANKS,
example dry-run, demo simulation. Full solution stays in editor only
(after you try) via Hint / Solution buttons.
"""

from __future__ import annotations


def Guide(
    intuition: str,
    algorithm: list[str],
    template: str,
    hints: list[dict],
    trace: list[dict] | None = None,
    demo: str = "",
    brute: str = "",
    pitfalls: list[str] | None = None,
    complexity: str = "",
) -> dict:
    return {
        "intuition": intuition.strip(),
        "brute": brute.strip(),
        "algorithm": algorithm,
        "template": template.strip("\n") + "\n",
        "hints": hints,
        "trace": trace or [],
        "demo": demo.strip("\n"),
        "pitfalls": pitfalls or [],
        "complexity": complexity.strip(),
    }


# ---------------------------------------------------------------------------
# Custom guides (hashing ladder quality)
# ---------------------------------------------------------------------------

PATTERN_GUIDES: dict[str, dict] = {
    "ah-contains-duplicate": Guide(
        intuition=(
            "You only need one question as you scan left-to-right: "
            "**have I seen this number before?** "
            "A hash set answers that in O(1) average time."
        ),
        brute="Nested loops — compare every pair. O(n²) time.",
        algorithm=[
            "Create an empty hash set `seen`.",
            "Loop each number `n` in `nums`.",
            "If `n` is already in `seen`, return True (duplicate).",
            "Otherwise add `n` to `seen`.",
            "If the loop finishes, return False.",
        ],
        template='''\
def contains_duplicate(nums):
    seen = set()

    for n in nums:
        # YOU: if n is already in seen, return True
        # YOU: otherwise add n to seen

    # YOU: return False when loop ends without a duplicate
    pass
''',
        hints=[
            {"where": "inside loop", "job": "Use `if n in seen:` before adding."},
            {"where": "inside loop", "job": "Use `seen.add(n)` only when n is new."},
            {"where": "after loop", "job": "`return False` — never found a repeat."},
        ],
        trace=[
            {"step": "start", "vars": "nums=[1,2,3,1], seen={}", "note": "empty set"},
            {"step": "n=1", "vars": "1 not in seen", "note": "add -> {1}"},
            {"step": "n=2", "vars": "2 not in seen", "note": "add -> {1,2}"},
            {"step": "n=3", "vars": "3 not in seen", "note": "add -> {1,2,3}"},
            {"step": "n=1", "vars": "1 IN seen", "note": "return True"},
        ],
        demo='''\
# Dry-run Example 1 (simulation only — not your submission)
nums = [1, 2, 3, 1]
seen = set()
print("Simulating Example 1:", nums)
for n in nums:
    print(f"  n={n}  seen={seen}")
    if n in seen:
        print("  -> duplicate! answer = True")
        break
    seen.add(n)
else:
    print("  -> no duplicate, answer = False")
''',
        pitfalls=[
            "Adding to `seen` before checking — first element looks like its own duplicate.",
            "Using a list for `seen` — membership becomes O(n).",
        ],
        complexity="Time O(n), Space O(n)",
    ),
    "ah-two-sum": Guide(
        intuition=(
            "Same one-pass scan as Contains Duplicate — but upgrade the box from **set** to **dict** "
            "so you store each value's **index**. "
            "Each step ask: **have I already seen the complement (target - current)?**"
        ),
        brute="Check every pair of indices. O(n²) time.",
        algorithm=[
            "Create empty dict `seen` mapping value -> index.",
            "Loop `i, num` with `enumerate(nums)`.",
            "Compute `need = target - num`.",
            "If `need` is in `seen`, return `[seen[need], i]`.",
            "Otherwise store `seen[num] = i` (after the check, not before).",
            "Return empty list if no pair (problem guarantees one pair exists).",
        ],
        template='''\
def two_sum(nums, target):
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        need = target - num
        # YOU: if need is in seen, return [seen[need], i]
        # YOU: store num -> i in seen (after the check above)

    pass
''',
        hints=[
            {"where": "need lookup", "job": "`if need in seen: return [seen[need], i]`"},
            {"where": "store line", "job": "`seen[num] = i` — must run AFTER the check."},
            {"where": "why order matters", "job": "[3,3] target 6: store-before-check pairs index with itself."},
        ],
        trace=[
            {"step": "i=0 num=2", "vars": "need=7, seen={}", "note": "7 missing -> store 2:0"},
            {"step": "i=1 num=7", "vars": "need=2, seen={2:0}", "note": "2 found -> [0,1]"},
        ],
        demo='''\
nums, target = [2, 7, 11, 15], 9
seen = {}
print("Simulating Two Sum:", nums, "target=", target)
for i, num in enumerate(nums):
    need = target - num
    print(f"  i={i} num={num} need={need} seen={seen}")
    if need in seen:
        print(f"  -> pair found: [{seen[need]}, {i}]")
        break
    seen[num] = i
''',
        pitfalls=[
            "Storing before checking — classic [3,3] / target 6 bug.",
            "Returning values instead of indices.",
        ],
        complexity="Time O(n), Space O(n)",
    ),
    "ah-group-anagrams": Guide(
        intuition=(
            "Anagrams share the same **signature** when you sort their letters. "
            "Use a dict: **signature -> list of words** with that signature."
        ),
        brute="Compare every pair of strings after sorting. O(n² * k log k).",
        algorithm=[
            "Create `groups = defaultdict(list)`.",
            "For each word, build `key = ''.join(sorted(word))`.",
            "Append word to `groups[key]`.",
            "Return `list(groups.values())`.",
        ],
        template='''\
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        # YOU: build a signature key from sorted letters
        # YOU: append word to groups[key]

    return list(groups.values())
''',
        hints=[
            {"where": "key", "job": '`key = "".join(sorted(word))` — anagrams share this.'},
            {"where": "bucket", "job": "`groups[key].append(word)`"},
            {"where": "not this", "job": "Do NOT use `sorted(nums)` on numbers — that's Top K, not here."},
        ],
        trace=[
            {"step": "eat", "vars": 'key="aet"', "note": 'bucket ["eat"]'},
            {"step": "tea", "vars": 'key="aet"', "note": 'bucket ["eat","tea"]'},
            {"step": "bat", "vars": 'key="abt"', "note": "new bucket"},
        ],
        demo='''\
from collections import defaultdict
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = defaultdict(list)
for word in strs:
    key = "".join(sorted(word))
    groups[key].append(word)
    print(f'  "{word}" -> key "{key}"')
print("groups:", dict(groups))
''',
        pitfalls=["Using the raw word as key — 'eat' and 'tea' won't group."],
        complexity="Time O(n * k log k), Space O(n * k)",
    ),
    "ah-top-k-frequent": Guide(
        intuition=(
            "**Phase 1:** count how often each number appears (dict, same one-pass idea). "
            "**Phase 2:** rank keys by count and take the top k. "
            "This is NOT Group Anagrams — you do not sort digits/letters of a single number."
        ),
        brute="Sort all unique numbers by frequency. O(n log n).",
        algorithm=[
            "Phase 1 — COUNT: loop nums, bump `freq[x] = freq.get(x,0)+1`.",
            "Phase 2 — RANK: sort keys of freq by count descending.",
            "Return first k keys from that ranking.",
        ],
        template='''\
def top_k_frequent(nums, k):
    # Phase 1 — COUNT
    freq = {}
    for x in nums:
        # YOU: bump freq[x] by 1 (freq.get helps on first sighting)

    # Phase 2 — RANK (new — not letter sorting!)
    # YOU: ranked = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
    # YOU: return ranked[:k]
    pass
''',
        hints=[
            {"where": "count", "job": "`freq[x] = freq.get(x, 0) + 1`"},
            {"where": "rank", "job": "Sort keys by `freq[x]`, highest first."},
            {"where": "trap", "job": "Key is the number itself (1,2,3) — not sorted(str(x))."},
        ],
        trace=[
            {"step": "phase 1", "vars": "freq={1:3, 2:2, 3:1}", "note": "from [1,1,1,2,2,3]"},
            {"step": "phase 2", "vars": "rank [1,2,3]", "note": "k=2 -> [1,2]"},
        ],
        demo='''\
nums, k = [1, 1, 1, 2, 2, 3], 2
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1
print("counts:", freq)
ranked = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
print("top k keys:", ranked[:k])
''',
        pitfalls=[
            "Using sorted(str(x)) or Group Anagrams logic on numbers.",
            "Forgetting phase 2 — returning the freq dict instead of top k keys.",
        ],
        complexity="Time O(n + u log u), Space O(u) unique count",
    ),
    "ah-subarray-sum-k": Guide(
        intuition=(
            "Two Sum on **prefix sums**. "
            "If current prefix minus k appeared before, the subarray between those prefixes sums to k. "
            "Dict stores **how many times** each prefix appeared (counts, not just indices)."
        ),
        brute="Check every subarray start/end. O(n²).",
        algorithm=[
            "Init `count` dict with `count[0] = 1` (empty prefix).",
            "Walk nums, maintain running `prefix` sum.",
            "Add `count[prefix - k]` to answer (valid earlier prefixes).",
            "Bump `count[prefix]` by 1.",
            "Return answer.",
        ],
        template='''\
from collections import defaultdict

def subarray_sum(nums, k):
    count = defaultdict(int)
    count[0] = 1
    prefix = 0
    ans = 0

    for num in nums:
        prefix += num
        # YOU: ans += count[prefix - k]
        # YOU: count[prefix] += 1

    return ans
''',
        hints=[
            {"where": "lookup", "job": "`ans += count[prefix - k]` — how many starts work?"},
            {"where": "seed", "job": "`count[0] = 1` — subarrays starting at index 0."},
            {"where": "+= not if", "job": "Use += because the same prefix can appear multiple times."},
        ],
        trace=[
            {"step": "+1", "vars": "prefix=1, need=-1 miss", "note": "ans=0"},
            {"step": "+1", "vars": "prefix=2, need=0 hit x1", "note": "ans=1"},
            {"step": "+1", "vars": "prefix=3, need=1 hit x1", "note": "ans=2"},
        ],
        demo='''\
nums, k = [1, 1, 1], 2
from collections import defaultdict
count = defaultdict(int); count[0] = 1
prefix = ans = 0
for num in nums:
    prefix += num
    ans += count[prefix - k]
    print(f"  +{num} prefix={prefix} ways={count[prefix-k]} ans={ans}")
    count[prefix] += 1
print("answer:", ans)
''',
        pitfalls=["Forgetting count[0]=1.", "Using if instead of += on count lookup."],
        complexity="Time O(n), Space O(n)",
    ),
    "ah-valid-anagram": Guide(
        intuition="Two anagrams have identical character counts. Compare frequency maps.",
        brute="Sort both strings and compare. O(n log n).",
        algorithm=[
            "If lengths differ, return False.",
            "Count chars in `s` and `t` (Counter or hand-built dict).",
            "Return whether counts match.",
        ],
        template='''\
from collections import Counter

def is_anagram(s, t):
    # YOU: return whether Counter(s) == Counter(t)
    # (or build two freq dicts and compare)
    pass
''',
        hints=[{"where": "one-liner", "job": "`return Counter(s) == Counter(t)`"}],
        trace=[{"step": "compare", "vars": "same letter counts", "note": "True for anagram/nagaram"}],
        demo='''\
from collections import Counter
s, t = "anagram", "nagaram"
print("Counter(s):", dict(Counter(s)))
print("Counter(t):", dict(Counter(t)))
print("match?", Counter(s) == Counter(t))
''',
        pitfalls=["Only checking length, not counts."],
        complexity="Time O(n), Space O(1) alphabet",
    ),
    "ah-product-except-self": Guide(
        intuition=(
            "Answer[i] = (product of everything left of i) * (product of everything right of i). "
            "Two passes — no division."
        ),
        brute="For each i, multiply all others. O(n²).",
        algorithm=[
            "First pass left-to-right: fill answer with prefix products.",
            "Track running `left` product as you go.",
            "Second pass right-to-left: multiply suffix products into answer.",
        ],
        template='''\
def product_except_self(nums):
    n = len(nums)
    answer = [1] * n
    left = 1
    for i in range(n):
        # YOU: answer[i] = left, then update left *= nums[i]

    right = 1
    for i in range(n - 1, -1, -1):
        # YOU: answer[i] *= right, then update right *= nums[i]

    return answer
''',
        hints=[
            {"where": "left pass", "job": "Store prefix product BEFORE multiplying in current num."},
            {"where": "right pass", "job": "Same idea from the right side."},
        ],
        trace=[{"step": "left", "vars": "[1,1,2,6]", "note": "then right -> [24,12,8,6]"}],
        demo='''\
nums = [1, 2, 3, 4]
answer = [1]*4
left = 1
for i in range(len(nums)):
    answer[i] = left
    left *= nums[i]
    print(f"  left pass i={i} answer[i]={answer[i]} left={left}")
''',
        pitfalls=["Using division — breaks on zeros and often banned."],
        complexity="Time O(n), Space O(1) excluding output",
    ),
    "ah-longest-consecutive": Guide(
        intuition=(
            "Put all numbers in a set. Only **start** counting when `x-1` is missing — "
            "that guarantees each streak is walked once."
        ),
        brute="Sort and scan for consecutive runs. O(n log n).",
        algorithm=[
            "Build set from nums.",
            "For each x in set, skip if x-1 exists (not a start).",
            "Walk x, x+1, x+2... while in set; track max length.",
        ],
        template='''\
def longest_consecutive(nums):
    s = set(nums)
    best = 0

    for x in s:
        # YOU: skip if (x - 1) is in s — not a streak start
        # YOU: walk forward counting length while (x + length) in s
        # YOU: best = max(best, length)

    return best
''',
        hints=[
            {"where": "start check", "job": "`if (x - 1) in s: continue`"},
            {"where": "walk", "job": "`while (x + length) in s: length += 1`"},
        ],
        trace=[{"step": "x=1", "vars": "0 not in set", "note": "walk 1,2,3,4 len=4"}],
        demo='''\
nums = [100, 4, 200, 1, 3, 2]
s = set(nums)
for x in sorted(s):
    if (x-1) in s:
        print(f"  {x}: skip (not start)")
        continue
    length = 1
    while (x+length) in s:
        length += 1
    print(f"  {x}: streak length {length}")
''',
        pitfalls=["Starting a streak at every number — O(n²) re-walks."],
        complexity="Time O(n), Space O(n)",
    ),
    "sw-longest-substring": Guide(
        intuition="Sliding window [L,R]. If char repeats inside window, jump L past its last index.",
        algorithm=[
            "Track last index of each char in `seen`.",
            "Expand R; if char seen at index >= L, move L to seen[char]+1.",
            "Update seen[char]=R and max window length.",
        ],
        template='''\
def length_of_longest_substring(s):
    seen = {}
    L = 0
    best = 0

    for R, ch in enumerate(s):
        # YOU: if ch in seen and seen[ch] >= L: move L
        # YOU: update seen[ch] = R
        # YOU: best = max(best, R - L + 1)

    return best
''',
        hints=[
            {"where": "shrink", "job": "`L = seen[ch] + 1` when ch repeats in window."},
            {"where": "length", "job": "`R - L + 1` is current window size."},
        ],
        trace=[{"step": "R=3 'a'", "vars": "L jumps to 1", "note": "window len 3"}],
        demo='''\
s = "abcabcbb"
seen = {}; L = best = 0
for R, ch in enumerate(s):
    if ch in seen and seen[ch] >= L:
        L = seen[ch] + 1
    seen[ch] = R
    best = max(best, R - L + 1)
    print(f"  R={R} ch={ch!r} L={L} window={s[L:R+1]!r} best={best}")
''',
        pitfalls=["Only shrinking L by 1 instead of jumping."],
        complexity="Time O(n), Space O(min(n, alphabet))",
    ),
    "sw-best-stock": Guide(
        intuition="Track cheapest price so far; at each day compute profit if sold today.",
        algorithm=[
            "Init min_price = inf, best = 0.",
            "Each price: update min_price, best = max(best, price - min_price).",
        ],
        template='''\
def max_profit(prices):
    min_price = float("inf")
    best = 0

    for price in prices:
        # YOU: min_price = min(min_price, price)
        # YOU: best = max(best, price - min_price)

    return best
''',
        hints=[{"where": "order", "job": "Buy (min) must come before sell (today's price)."}],
        trace=[{"step": "price=6", "vars": "min=1 profit=5", "note": "best=5"}],
        demo='''\
prices = [7, 1, 5, 3, 6, 4]
min_p = float("inf"); best = 0
for p in prices:
    min_p = min(min_p, p)
    best = max(best, p - min_p)
    print(f"  price={p} min={min_p} best={best}")
''',
        pitfalls=["Finding max price before min — invalid transaction."],
        complexity="Time O(n), Space O(1)",
    ),
    "tp-two-sum-ii": Guide(
        intuition="Sorted array -> two pointers L and R. Move the pointer that fixes the sum.",
        algorithm=[
            "L=0, R=len-1.",
            "If sum == target return [L+1, R+1] (1-indexed).",
            "If sum too small, L++. If too big, R--.",
        ],
        template='''\
def two_sum_sorted(numbers, target):
    L, R = 0, len(numbers) - 1

    while L < R:
        total = numbers[L] + numbers[R]
        # YOU: if total == target: return [L+1, R+1]
        # YOU: elif total < target: L += 1
        # YOU: else: R -= 1

    pass
''',
        hints=[{"where": "indices", "job": "Problem wants 1-indexed [L+1, R+1]."}],
        trace=[{"step": "L=0,R=1", "vars": "2+7=9", "note": "return [1,2]"}],
        demo='''\
nums, target = [2, 7, 11, 15], 9
L, R = 0, len(nums)-1
while L < R:
    t = nums[L] + nums[R]
    print(f"  L={L}({nums[L]}) R={R}({nums[R]}) sum={t}")
    if t == target: print(f"  -> [{L+1},{R+1}]"); break
    elif t < target: L += 1
    else: R -= 1
''',
        pitfalls=["Returning 0-indexed indices."],
        complexity="Time O(n), Space O(1)",
    ),
    "st-valid-parentheses": Guide(
        intuition="Stack holds open brackets waiting for a match.",
        algorithm=[
            "Push openers onto stack.",
            "On closer: stack must be non-empty and top must match.",
            "Pop on match; return False on mismatch.",
            "End: return whether stack is empty.",
        ],
        template='''\
def is_valid(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for ch in s:
        if ch in "([{":
            # YOU: push ch
            pass
        else:
            # YOU: if stack empty or top != pairs[ch]: return False
            # YOU: pop stack

    # YOU: return whether stack is empty
    pass
''',
        hints=[
            {"where": "close", "job": "Check `not stack` before comparing stack[-1]."},
        ],
        trace=[{"step": "')'", "vars": "stack had '('", "note": "pop -> empty -> True"}],
        demo='''\
s = "()[]{}"
stack = []
pairs = {")": "(", "]": "[", "}": "{"}
for ch in s:
    print(f"  ch={ch!r} stack={stack}")
''',
        pitfalls=["Pop without checking empty stack."],
        complexity="Time O(n), Space O(n)",
    ),
    "bs-binary-search": Guide(
        intuition="Halve the search space each step on a sorted array.",
        algorithm=[
            "lo=0, hi=len-1.",
            "While lo <= hi: mid = (lo+hi)//2.",
            "If nums[mid]==target return mid.",
            "If nums[mid] < target: lo=mid+1 else hi=mid-1.",
            "Return -1.",
        ],
        template='''\
def search(nums, target):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        # YOU: compare nums[mid] to target, update lo or hi or return mid

    return -1
''',
        hints=[{"where": "loop", "job": "Use `while lo <= hi` so single-element arrays work."}],
        trace=[{"step": "mid=4", "vars": "nums[4]=9", "note": "found"}],
        demo='''\
nums, target = [-1,0,3,5,9,12], 9
lo, hi = 0, len(nums)-1
while lo <= hi:
    mid = (lo+hi)//2
    print(f"  search [{lo},{hi}] mid={mid} val={nums[mid]}")
    if nums[mid]==target: print(f"  -> index {mid}"); break
    elif nums[mid] < target: lo = mid+1
    else: hi = mid-1
''',
        pitfalls=["Off-by-one on lo/hi updates causes infinite loops."],
        complexity="Time O(log n), Space O(1)",
    ),
    "dp-climbing-stairs": Guide(
        intuition="Ways to reach step n = ways(n-1) + ways(n-2). Fibonacci.",
        algorithm=[
            "Base: 1 way for n=1, 2 ways for n=2.",
            "Roll two variables forward instead of full array.",
        ],
        template='''\
def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2  # ways for step 1 and 2
    for _ in range(3, n + 1):
        # YOU: a, b = b, a + b
        pass
    return b
''',
        hints=[{"where": "roll", "job": "`a, b = b, a + b` each iteration."}],
        trace=[{"step": "n=3", "vars": "a,b = 1,2 -> 2,3", "note": "3 ways"}],
        demo='''\
n = 3
a, b = 1, 2
for step in range(3, n+1):
    a, b = b, a+b
    print(f"  step {step}: {b} ways")
''',
        pitfalls=["Pure recursion without memo — exponential."],
        complexity="Time O(n), Space O(1)",
    ),
}

# ---------------------------------------------------------------------------
# Category templates (blanks only — no full answers)
# ---------------------------------------------------------------------------

CATEGORY_GUIDES: dict[str, dict] = {
    "arrays-hashing": Guide(
        intuition="One pass + hash structure. Set = seen? Dict = seen -> payload or counts.",
        algorithm=[
            "Pick set vs dict based on what you need to remember.",
            "Single loop left-to-right.",
            "Ask a lookup question each iteration.",
            "Update structure; early return if done.",
        ],
        template='''\
def solve(nums):
    seen = {}  # or set()

    for x in nums:
        # YOU: lookup question (x? complement? prefix?)
        # YOU: update seen
        pass

    # YOU: return default
''',
        hints=[{"where": "core", "job": "Define what the key and value mean before coding."}],
    ),
    "two-pointers": Guide(
        intuition="Two indices on sorted (or opposite ends) data; move one based on comparison.",
        algorithm=["Init L and R.", "Compute from L and R.", "Move pointer that improves answer."],
        template='''\
def solve(arr):
    L, R = 0, len(arr) - 1
    while L < R:
        # YOU: compute from arr[L], arr[R]
        # YOU: move L or R
        pass
''',
        hints=[{"where": "move", "job": "Sorted sum too small -> L++. Too big -> R--."}],
    ),
    "sliding-window": Guide(
        intuition="Expand R to grow window; shrink L while invalid.",
        algorithm=["L=0.", "For each R, add to window.", "While invalid, remove L and L++.", "Track best."],
        template='''\
def solve(arr):
    L = 0
    best = 0
    for R in range(len(arr)):
        # YOU: expand window with arr[R]
        # YOU: while window invalid: shrink from L
        # YOU: update best
        pass
    return best
''',
        hints=[{"where": "invalid", "job": "Define what makes YOUR window invalid first."}],
    ),
    "stack": Guide(
        intuition="Stack = 'waiting' items (open brackets, cooler days, etc.).",
        algorithm=["Push on open / interesting event.", "Pop when match or resolution."],
        template='''\
def solve(items):
    stack = []
    for x in items:
        # YOU: push or pop based on x vs stack[-1]
        pass
''',
        hints=[{"where": "pop", "job": "Always check stack non-empty before stack[-1]."}],
    ),
    "binary-search": Guide(
        intuition="Search space is monotonic — binary search on index or on answer.",
        algorithm=["lo/hi bounds.", "Test mid.", "Discard half."],
        template='''\
def solve(lo, hi):
    while lo <= hi:
        mid = (lo + hi) // 2
        # YOU: if feasible(mid): move hi or return
        # YOU: else: move lo
        pass
''',
        hints=[{"where": "feasible", "job": "Write a helper that returns True/False for mid."}],
    ),
    "linked-list": Guide(
        intuition="Draw prev / curr / nxt. Never lose the head reference.",
        algorithm=["Init pointers.", "Save next before mutating.", "Advance."],
        template='''\
def solve(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        # YOU: mutate pointers
        prev, curr = curr, nxt
    return prev  # often new head
''',
        hints=[{"where": "save", "job": "`nxt = curr.next` before changing curr.next."}],
    ),
    "trees": Guide(
        intuition="DFS: base case on null. BFS: queue processes level by level.",
        algorithm=["Null check.", "Recurse or queue children.", "Combine results."],
        template='''\
def dfs(node):
    if not node:
        return 0  # base
    # YOU: left = dfs(node.left); right = dfs(node.right)
    # YOU: return combine(node.val, left, right)
    pass
''',
        hints=[{"where": "base", "job": "Null node is always the base case."}],
    ),
    "heap": Guide(
        intuition="heapq is min-heap. Negate for max. Size-k heap for top k streaming.",
        algorithm=["Push items.", "If heap too big, pop smallest."],
        template='''\
import heapq

def solve(items, k):
    h = []
    for x in items:
        # YOU: heappush (maybe -x for max-heap)
        # YOU: if len(h) > k: heappop
        pass
''',
        hints=[{"where": "kth largest", "job": "Keep min-heap of size k; peek is kth largest."}],
    ),
    "graphs": Guide(
        intuition="Mark visited. BFS = layers. DFS = recursion/stack flood fill.",
        algorithm=["Build graph or use grid neighbors.", "Traverse unvisited nodes.", "Mark visited."],
        template='''\
def solve(grid):
    # YOU: loop cells / nodes
    # YOU: if unvisited: dfs or bfs from here
    pass

def dfs(r, c):
    # YOU: bounds + visited check
    # YOU: mark visited, visit neighbors
    pass
''',
        hints=[{"where": "visited", "job": "Mark BEFORE exploring neighbors to avoid cycles."}],
    ),
    "backtracking": Guide(
        intuition="Choose -> recurse -> undo. Record when constraint satisfied.",
        algorithm=["Base case record.", "Loop choices.", "Apply, dfs, remove."],
        template='''\
def solve(nums):
    out, path = [], []

    def dfs(start):
        # YOU: if done: append path copy; return
        for i in range(start, len(nums)):
            # YOU: path.append(...); dfs(...); path.pop()
            pass

    dfs(0)
    return out
''',
        hints=[{"where": "undo", "job": "Always pop/backtrack after recursive call."}],
    ),
    "dp-1d": Guide(
        intuition="dp[i] = best answer using first i items. Fill bottom-up.",
        algorithm=["Define dp[0] base.", "Loop i, combine dp[i-1] and dp[i-2] or choices."],
        template='''\
def solve(n):
    dp = [0] * (n + 1)
    dp[0] = 0  # YOU: set base case(s)
    for i in range(1, n + 1):
        # YOU: dp[i] = best of choices
        pass
    return dp[n]
''',
        hints=[{"where": "define", "job": "Write one sentence: what does dp[i] mean?"}],
    ),
    "intervals": Guide(
        intuition="Sort intervals first. Merge or greedy based on start or end.",
        algorithm=["Sort.", "Compare current to last kept interval.", "Merge or append."],
        template='''\
def solve(intervals):
    intervals.sort(key=lambda x: x[0])
    out = [intervals[0]]
    for s, e in intervals[1:]:
        # YOU: overlap with out[-1]? merge : append
        pass
    return out
''',
        hints=[{"where": "sort key", "job": "Merge by start; non-overlap greedy often by end."}],
    ),
    "greedy": Guide(
        intuition="Make locally best choice each step; know why it works for this problem.",
        algorithm=["Track best/farthest/reachable.", "Update each step.", "Return."],
        template='''\
def solve(nums):
    best = 0
    for x in nums:
        # YOU: greedy update
        pass
    return best
''',
        hints=[{"where": "proof", "job": "Say out loud WHY greedy is safe for this problem."}],
    ),
    "amazon-story": Guide(
        intuition="Strip nouns. Map to Top K, two pointers, intervals, etc.",
        algorithm=[
            "Restate in plain arrays/strings.",
            "Name the LC pattern.",
            "Code the pattern — ignore business story.",
        ],
        template='''\
def solve(story_input):
    # YOU: translate story -> arrays / counts / pairs
    # YOU: apply named pattern (Counter, two pointers, ...)
    pass
''',
        hints=[{"where": "strip", "job": "Keywords -> frequency. Routes -> pairs with sums."}],
    ),
}


def get_guide(problem_id: str, category: str) -> dict:
    if problem_id in PATTERN_GUIDES:
        return PATTERN_GUIDES[problem_id]
    base = CATEGORY_GUIDES.get(category, CATEGORY_GUIDES["arrays-hashing"])
    return {
        **base,
        "intuition": base["intuition"] + f" (Apply to: {problem_id.replace('-', ' ')})",
    }

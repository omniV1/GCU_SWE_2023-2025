"""
Python code walkthroughs for each example (NeetCode-style - real code, not just diagrams).

Keyed by problem id -> list of code strings aligned with example index.
Merged in neetcode_examples.get().
"""

from __future__ import annotations

CODE_WALKS: dict[str, list[str]] = {
    "ah-contains-duplicate": [
        '''\
def contains_duplicate(nums):          # nums = [1, 2, 3, 1]
    seen = set()                       # seen = {}

    for x in nums:
        if x in seen:                  # x=1: already in seen?
            return True
        seen.add(x)
        # step: x=1  seen={1}
        # step: x=2  seen={1,2}
        # step: x=3  seen={1,2,3}
        # step: x=1  1 in seen -> return True

    return False
# -> True
''',
        '''\
def contains_duplicate(nums):          # nums = [1, 2, 3, 4]
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
        # {1} -> {1,2} -> {1,2,3} -> {1,2,3,4}
    return False                       # no repeats
# -> False
''',
        '''\
# early exit on first repeat
seen = set()
for x in [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]:
    if x in seen:                      # second 1 hits immediately
        return True                    # -> True
    seen.add(x)
''',
    ],
    "ah-valid-anagram": [
        '''\
from collections import Counter

def is_anagram(s, t):                  # s="anagram" t="nagaram"
    return Counter(s) == Counter(t)
    # Counter(s) = {'a':3,'n':1,'g':1,'r':1,'m':1}
    # Counter(t) = {'n':1,'a':3,'g':1,'r':1,'m':1}
    # equal -> True
''',
        '''\
from collections import Counter
# Counter("rat") = {r:1, a:1, t:1}
# Counter("car") = {c:1, a:1, r:1}
# maps differ -> False
''',
    ],
    "ah-two-sum": [
        '''\
def two_sum(nums, target):             # [2,7,11,15], target=9
    seen = {}                          # value -> index

    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
        # i=0 num=2 need=7  seen={}      -> store {2:0}
        # i=1 num=7 need=2  seen={2:0}   -> 2 found! return [0,1]

# -> [0, 1]
''',
        '''\
# nums=[3,2,4] target=6
seen = {}
# i=0 num=3 need=3  store {3:0}
# i=1 num=2 need=4  store {3:0, 2:1}
# i=2 num=4 need=2  2 in seen -> [1, 2]
''',
        '''\
# nums=[3,3] target=6
# i=0 store {3:0}
# i=1 need=3 found at 0 -> [0, 1]
''',
    ],
    "ah-group-anagrams": [
        '''\
from collections import defaultdict

def group_anagrams(strs):
    buckets = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))    # signature
        buckets[key].append(word)
        # "eat" -> "aet" -> {"aet": ["eat"]}
        # "tea" -> "aet" -> {"aet": ["eat","tea"]}
        # "tan" -> "ant" -> {"ant": ["tan"]}
        # "ate" -> "aet" -> {"aet": ["eat","tea","ate"]}
        # ...

    return list(buckets.values())
''',
        'buckets = {"": [""]}  # empty string is its own group',
        'buckets = {"a": ["a"]}',
    ],
    "ah-top-k-frequent": [
        '''\
from collections import Counter

def top_k_frequent(nums, k):           # [1,1,1,2,2,3], k=2
    # Phase 1 - COUNT (hash map)
    freq = Counter(nums)               # {1:3, 2:2, 3:1}

    # Phase 2 - RANK by frequency (NOT Group Anagrams)
    ranked = sorted(freq.keys(), key=lambda x: -freq[x])
    # ranked = [1, 2, 3]   because 3 > 2 > 1 frequency
    return ranked[:k]                  # [1, 2]
''',
        '''\
freq = Counter([1])  # {1:1}
return [1]           # k=1
''',
    ],
    "ah-product-except-self": [
        '''\
def product_except_self(nums):         # [1,2,3,4]
    n = len(nums)
    answer = [1] * n

    # left products
    left = 1
    for i in range(n):
        answer[i] = left               # [1, 1, 2, 6]
        left *= nums[i]

    # multiply right products
    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right             # [24, 12, 8, 6]
        right *= nums[i]

    return answer                      # [24, 12, 8, 6]
''',
        '''\
# zeros force most slots to 0; only the zero-index gets nonzero product
# nums=[-1,1,0,-3,3] -> [0,0,9,0,0]
''',
    ],
    "ah-longest-consecutive": [
        '''\
def longest_consecutive(nums):
    s = set(nums)                      # {100,4,200,1,3,2}
    best = 0

    for x in s:
        if x - 1 in s:                 # not a streak START
            continue
        length = 1
        while x + length in s:
            length += 1
        best = max(best, length)
        # x=1 starts: 1,2,3,4 -> length 4
        # x=100 -> 1; x=200 -> 1

    return best                        # 4
''',
        '''\
# streak 0..8 -> length 9
s = set([0,3,7,2,5,8,4,6,0,1])
# start at 0 only ( -1 missing )
''',
    ],
    "ah-subarray-sum-k": [
        '''\
from collections import defaultdict

def subarray_sum(nums, k):             # [1,1,1], k=2
    count = defaultdict(int)
    count[0] = 1                       # empty prefix
    prefix = 0
    ans = 0

    for num in nums:
        prefix += num
        ans += count[prefix - k]       # how many prefixes give sum k
        count[prefix] += 1
        # num=1 prefix=1  need=-1? 0 -> +0  count={0:1,1:1}
        # num=1 prefix=2  need=0  -> +1     (subarray [1,1])
        # num=1 prefix=3  need=1  -> +1     (subarray [1,1])

    return ans                         # 2
''',
        '''\
# [1,2,3] k=3
# prefixes 1,3,6 -> hits at prefix=3 (need 0) and prefix=6 (need 3)
# ans = 2
''',
    ],
    "ah-encode-decode": [
        '''\
def encode(strs):
    return "".join(f"{len(x)}#{x}" for x in strs)
    # ["lint","code"] -> "4#lint4#code"

def decode(s):
    out, i = [], 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        out.append(s[j+1 : j+1+length])
        i = j + 1 + length
    return out
    # "4#lint4#code" -> ["lint","code"]
''',
        '''\
encode(["", "a", "#b"]) -> "0#1#a2##b"
decode that -> ["", "a", "#b"]   # '#' inside payload is fine
''',
    ],
    "tp-valid-palindrome": [
        '''\
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
        # "A man, a plan, a canal: Panama"
        # compare a<->a, m<->m, a<->a ... all match
    return True                        # -> True
''',
        '''\
# "race a car" -> cleaned "raceacar"
# L='r' R='r' ok; ... eventually 'e' vs 'a' -> False
''',
    ],
    "tp-two-sum-ii": [
        '''\
def two_sum(numbers, target):          # [2,7,11,15], 9
    L, R = 0, len(numbers) - 1
    while L < R:
        total = numbers[L] + numbers[R]
        if total == target:
            return [L + 1, R + 1]       # 1-indexed
        if total < target:
            L += 1
        else:
            R -= 1
        # 2+15=17 > 9 -> R--
        # 2+11=13 > 9 -> R--
        # 2+7=9 -> return [1,2]
''',
        '''\
# [2,3,4] target=6 -> L=0 R=2 -> 2+4=6 -> [1,3]
''',
    ],
    "tp-3sum": [
        '''\
def three_sum(nums):
    nums.sort()                        # [-4,-1,-1,0,1,2]
    out = []
    for i in range(len(nums)):
        if i and nums[i] == nums[i-1]:
            continue                   # skip duplicate anchors
        L, R = i + 1, len(nums) - 1
        while L < R:
            total = nums[i] + nums[L] + nums[R]
            if total == 0:
                out.append([nums[i], nums[L], nums[R]])
                L += 1
                R -= 1
                while L < R and nums[L] == nums[L-1]:
                    L += 1
            elif total < 0:
                L += 1
            else:
                R -= 1
    # -> [[-1,-1,2], [-1,0,1]]
    return out
''',
        "nums=[0,1,1] -> no triplet sums to 0 -> []",
        "nums=[0,0,0] -> only [[0,0,0]]",
    ],
    "tp-container-water": [
        '''\
def max_area(height):                  # [1,8,6,2,5,4,8,3,7]
    L, R = 0, len(height) - 1
    best = 0
    while L < R:
        area = min(height[L], height[R]) * (R - L)
        best = max(best, area)
        if height[L] < height[R]:
            L += 1
        else:
            R -= 1
        # best known: L=1 (8), R=8 (7)
        # min(8,7)*(8-1) = 49
    return best                        # 49
''',
        "height=[1,1] -> min(1,1)*1 = 1",
    ],
    "sw-best-stock": [
        '''\
def max_profit(prices):                # [7,1,5,3,6,4]
    min_price = float("inf")
    best = 0
    for price in prices:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
        # price=7  min=7  best=0
        # price=1  min=1  best=0
        # price=5  min=1  best=4
        # price=3  min=1  best=4
        # price=6  min=1  best=5   <- buy 1 sell 6
        # price=4  min=1  best=5
    return best                        # 5
''',
        '''\
# strictly decreasing -> never profitable
best stays 0
''',
    ],
    "sw-longest-substring": [
        '''\
def length_of_longest_substring(s):    # "abcabcbb"
    seen = {}
    L = 0
    best = 0
    for R, ch in enumerate(s):
        if ch in seen and seen[ch] >= L:
            L = seen[ch] + 1           # shrink past old copy
        seen[ch] = R
        best = max(best, R - L + 1)
        # R=0 'a' window "a"    best=1
        # R=1 'b' window "ab"   best=2
        # R=2 'c' window "abc"  best=3
        # R=3 'a' move L->1      "bca" best=3
    return best                        # 3
''',
        's="bbbbb" -> window always size 1 -> 1',
        's="pwwkew" -> best window "wke" -> 3',
    ],
    "sw-min-subarray": [
        '''\
def min_sub_array_len(target, nums):   # target=7, [2,3,1,2,4,3]
    L = 0
    total = 0
    best = float("inf")
    for R, x in enumerate(nums):
        total += x
        while total >= target:
            best = min(best, R - L + 1)
            total -= nums[L]
            L += 1
        # grows to [2,3,1,2] sum=8 len=4
        # shrinks... eventually [4,3] sum=7 len=2
    return 0 if best == float("inf") else best  # 2
''',
        "target=4 nums=[1,4,4] -> single [4] -> length 1",
    ],
    "sw-max-avg-subarray": [
        '''\
def find_max_average(nums, k):         # [1,12,-5,-6,50,3], k=4
    window = sum(nums[:k])             # 1+12-5-6 = 2
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i-k]  # slide by 1
        best = max(best, window)
        # i=4: window = 2+50-1 = 51
        # i=5: window = 51+3-12 = 42
    return best / k                    # 51/4 = 12.75
''',
        "nums=[5] k=1 -> 5.0",
    ],
    "st-valid-parentheses": [
        '''\
def is_valid(s):                       # "()"
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)           # push '('
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()                # ')' matches '('
    return not stack                   # empty -> True
''',
        '''\
# "()[]{}" - each closer pops matching opener -> empty -> True
''',
        '''\
stack = ["("]
# ch=']' expects ')' but top is '(' -> False
''',
    ],
    "st-daily-temperatures": [
        '''\
def daily_temperatures(temperatures):
    n = len(temperatures)
    ans = [0] * n
    stack = []                         # indices, temps decreasing

    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            ans[j] = i - j             # wait days
        stack.append(i)
        # ... when 76 arrives, pops cooler days and fills waits
    return ans
    # [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
''',
        "# strictly rising: each waits 1 day; last waits 0",
    ],
    "st-min-stack": [
        '''\
class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []                 # parallel running-min

    def push(self, val):
        self.stack.append(val)
        self.mins.append(val if not self.mins else min(val, self.mins[-1]))
        # push -2: stack=[-2] mins=[-2]
        # push  0: stack=[-2,0] mins=[-2,-2]
        # push -3: stack=[-2,0,-3] mins=[-2,-2,-3]

    def pop(self):
        self.stack.pop()
        self.mins.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.mins[-1]
# getMin->-3; pop; top->0; getMin->-2
''',
    ],
    "bs-binary-search": [
        '''\
def search(nums, target):              # [-1,0,3,5,9,12], 9
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
        # mid=2 val=3 < 9 -> lo=3
        # mid=4 val=9 == target -> return 4
    return -1
''',
        "# target=2 never equals nums[mid] -> -1",
    ],
    "bs-koko": [
        '''\
import math

def min_eating_speed(piles, h):        # [3,6,7,11], h=8
    def hours(k):
        return sum(math.ceil(p / k) for p in piles)

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours(mid) <= h:
            hi = mid                   # try slower
        else:
            lo = mid + 1
        # hours(4)=1+2+2+3=8 <= 8 -> feasible
    return lo                          # 4
''',
        "h=5 forces k near max(piles)=30",
    ],
    "bs-search-2d": [
        '''\
def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // n][mid % n]  # flatten index -> row,col
        if val == target:
            return True                # found 3
        if val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
''',
        "target=13 never hits -> False",
    ],
    "ll-reverse-list": [
        '''\
def reverse_list(head):                # 1->2->3->4->5
    prev = None
    curr = head
    while curr:
        nxt = curr.next                # save
        curr.next = prev               # flip
        prev = curr
        curr = nxt
        # after: None<-1<-2<-3<-4<-5
    return prev                        # new head = 5
''',
        "# 1->2 becomes 2->1",
    ],
    "ll-has-cycle": [
        '''\
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next               # +1
        fast = fast.next.next          # +2
        if slow is fast:
            return True                # met inside cycle
    return False
# 3->2->0->-4
#      ^______|
# slow/fast eventually collide -> True
''',
        "1->2->1 cycle -> True",
        "single node no next -> False",
    ],
    "ll-merge-two": [
        '''\
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
        # take 1,1,2,3,4,4 in order
    cur.next = list1 or list2
    return dummy.next
''',
        "both empty -> None",
    ],
    "tr-max-depth": [
        '''\
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
    #      3
    #     / \\
    #    9  20
    #       / \\
    #      15  7
    # depth(15)=1, depth(20)=2, depth(3)=3
''',
        "# [1,null,2] -> 1 + depth(right=2) = 2",
    ],
    "tr-invert-tree": [
        '''\
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
    #      4              4
    #     / \\     ->      / \\
    #    2   7          7   2
''',
        "# [2,1,3] -> [2,3,1]",
    ],
    "tr-same-tree": [
        '''\
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    # both [1,2,3] -> True
''',
        '''\
# p has left child, q has right child -> structure fails -> False
''',
    ],
    "tr-level-order": [
        '''\
from collections import deque

def level_order(root):
    if not root:
        return []
    q = deque([root])
    out = []
    while q:
        level = []
        for _ in range(len(q)):        # drain this level
            n = q.popleft()
            level.append(n.val)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        out.append(level)
        # level0=[3], level1=[9,20], level2=[15,7]
    return out
''',
        "root=[1] -> [[1]]",
    ],
    "tr-lca-bst": [
        '''\
def lowest_common_ancestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root                # split point = LCA
    # p=2 left of 6, q=8 right of 6 -> return 6
''',
        "# p=2 q=4 both on left; walk down until split/at p -> 2",
    ],
    "hp-kth-largest": [
        '''\
import heapq

def find_kth_largest(nums, k):         # [3,2,1,5,6,4], k=2
    heap = []                          # min-heap of size k
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
        # keep only the k largest; peek is kth
        # end heap ~= [5,6] -> peek 5
    return heap[0]                     # 5
''',
        "# k=4 -> 4th largest = 4",
    ],
    "hp-last-stone": [
        '''\
import heapq

def last_stone_weight(stones):
    h = [-s for s in stones]
    heapq.heapify(h)                   # max-heap via negatives
    while len(h) > 1:
        a = -heapq.heappop(h)
        b = -heapq.heappop(h)
        if a != b:
            heapq.heappush(h, -(a - b))
        # smash 8&7 -> push 1; continue...
    return -h[0] if h else 0           # 1
''',
        "stones=[1] -> 1",
    ],
    "gr-num-islands": [
        '''\
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r, c):
        if r<0 or c<0 or r>=rows or c>=cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"               # sink visited land
        dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)              # flood one island
    return islands                     # 1
''',
        "# three separate '1' components -> islands = 3",
    ],
    "gr-rotting-oranges": [
        '''\
from collections import deque

def oranges_rotting(grid):
    q = deque()
    fresh = 0
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 2: q.append((r, c))
            if val == 1: fresh += 1

    minutes = 0
    while q and fresh:
        for _ in range(len(q)):        # one minute = one BFS layer
            r, c = q.popleft()
            for nr, nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        minutes += 1
    return minutes if fresh == 0 else -1  # 4
''',
        "# unreachable fresh orange remains -> -1",
    ],
    "gr-course-schedule": [
        '''\
from collections import defaultdict, deque

def can_finish(numCourses, prerequisites):
    graph = defaultdict(list)
    indeg = [0] * numCourses
    for a, b in prerequisites:         # b -> a
        graph[b].append(a)
        indeg[a] += 1

    q = deque([i for i in range(numCourses) if indeg[i] == 0])
    taken = 0
    while q:
        node = q.popleft()
        taken += 1
        for nei in graph[node]:
            indeg[nei] -= 1
            if indeg[nei] == 0:
                q.append(nei)
    return taken == numCourses
    # [[1,0]] -> take 0 then 1 -> True
''',
        "# [[1,0],[0,1]] cycle -> taken < numCourses -> False",
    ],
    "gr-clone-graph": [
        '''\
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
    # map old->new so each node cloned once; wire neighbors
''',
    ],
    "bt-subsets": [
        '''\
def subsets(nums):                     # [1,2,3]
    out, path = [], []

    def dfs(start):
        out.append(path[:])            # record every state
        for i in range(start, len(nums)):
            path.append(nums[i])
            dfs(i + 1)
            path.pop()                 # backtrack

    dfs(0)
    return out
    # [], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]
''',
        "nums=[0] -> [[], [0]]",
    ],
    "bt-permutations": [
        '''\
def permute(nums):                     # [1,2,3]
    out, path = [], []
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
    return out                         # 6 permutations
''',
        "nums=[0,1] -> [[0,1],[1,0]]",
    ],
    "bt-combination-sum": [
        '''\
def combination_sum(candidates, target):  # [2,3,6,7], 7
    out, path = [], []

    def dfs(start, remain):
        if remain == 0:
            out.append(path[:])
            return
        if remain < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            dfs(i, remain - candidates[i])  # i not i+1 -> reuse
            path.pop()

    dfs(0, target)
    return out                         # [[2,2,3],[7]]
''',
        "# target=8 -> [[2,2,2,2],[2,3,3],[3,5]]",
    ],
    "gd-jump-game": [
        '''\
def can_jump(nums):                    # [2,3,1,1,4]
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + jump)
        # i=0 farthest=2
        # i=1 farthest=max(2,1+3)=4  -> index 4 reachable
    return True
''',
        '''\
# [3,2,1,0,4] farthest sticks at 3; i=4 > 3 -> False
''',
    ],
    "in-merge-intervals": [
        '''\
def merge(intervals):
    intervals.sort()                   # by start
    out = [intervals[0]]
    for s, e in intervals[1:]:
        if s <= out[-1][1]:            # overlap / touch
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
        # [1,3]+[2,6] -> [1,6]
    return out                         # [[1,6],[8,10],[15,18]]
''',
        "# [1,4]+[4,5] touch -> merge [1,5]",
    ],
    "in-non-overlap": [
        '''\
def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda x: x[1])  # sort by END
    end = float("-inf")
    remove = 0
    for s, e in intervals:
        if s >= end:
            end = e                    # keep
        else:
            remove += 1                # drop overlapping
    return remove
    # keep [1,2],[2,3],[3,4]; drop [1,3] -> 1
''',
        "# three identical [1,2] -> remove 2",
    ],
    "dp-climbing-stairs": [
        '''\
def climb_stairs(n):                   # n=2
    if n <= 2:
        return n
    a, b = 1, 2                        # ways(1), ways(2)
    for _ in range(3, n + 1):
        a, b = b, a + b                # Fibonacci
    return b
    # n=2 -> 2   (1+1 or 2)
''',
        "# n=3 -> ways(2)+ways(1)=2+1=3",
    ],
    "dp-house-robber": [
        '''\
def rob(nums):                         # [1,2,3,1]
    prev2 = 0                          # dp[i-2]
    prev1 = 0                          # dp[i-1]
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
        # x=1 -> 1
        # x=2 -> max(1, 0+2)=2
        # x=3 -> max(2, 1+3)=4
        # x=1 -> max(4, 2+1)=4
    return prev1                       # 4
''',
        "# [2,7,9,3,1] -> 12 (2+9+1)",
    ],
    "dp-coin-change": [
        '''\
def coin_change(coins, amount):        # [1,2,5], 11
    INF = amount + 1
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
        # dp[11] built from dp[10]+1, dp[9]+1, dp[6]+1 -> 3
    return -1 if dp[amount] == INF else dp[amount]
''',
        "# coins=[2] amount=3 -> impossible -> -1",
    ],
    "dp-longest-palindrome-subseq": [
        '''\
def longest_palindrome_subseq(s):      # "bbbab"
    t = s[::-1]                        # "babbb"
    n = len(s)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][n]                    # LCS(s, rev(s)) = 4
''',
        's="cbbd" -> LPS length 2 ("bb")',
    ],
    "am-top-k-keywords": [
        '''\
from collections import Counter

def top_k_keywords(keywords, k):
    freq = Counter(keywords)
    # {"i":2,"love":2,"leetcode":1,"coding":1}
    ranked = sorted(freq.keys(), key=lambda w: (-freq[w], w))
    # sort by higher freq first, then alphabetical
    # -> ["i","love","coding","leetcode"]
    return ranked[:k]                  # ["i","love"]
''',
        'freq a:3 b:2 -> ["a","b"]',
    ],
    "am-optimal-utilization": [
        '''\
def optimal_utilization(forward, returns, target):
    forward = sorted(forward, key=lambda x: x[1])
    returns = sorted(returns, key=lambda x: x[1])
    i, j = 0, len(returns) - 1
    best, out = -1, []
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
    # forward ids 1,2,3 durations 2,4,6; return [1,2]
    # best <=7 is 4+2=6 -> [[2,1]]
    return out
''',
        "# multiple pairs at sum==10 -> return all best pairs",
    ],
}

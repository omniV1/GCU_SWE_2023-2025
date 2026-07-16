"""
WORKED ANSWERS for 07_amazon_common_problems.py

Use ONLY after 15+ min stuck. Read ONE function. Close. Retype from memory.
Do NOT copy-paste into the practice file forever — that teaches nothing.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from typing import List


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
    freq = Counter(nums)
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


def length_of_longest_substring(s: str) -> int:
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


def min_subarray_len(target: int, nums: List[int]) -> int:
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


def is_valid_parentheses(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return len(stack) == 0


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
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


def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> None:
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


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
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


def max_profit(prices: List[int]) -> int:
    min_price = float("inf")
    best = 0
    for price in prices:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
    return best


if __name__ == "__main__":
    # smoke check so you know this answer key itself is correct
    assert set(two_sum([2, 7, 11, 15], 9)) == {0, 1}
    assert length_of_longest_substring("abcabcbb") == 3
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    print("Worked answer key OK.")

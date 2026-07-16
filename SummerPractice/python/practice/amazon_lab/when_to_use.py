"""
When to use each pattern — recognition signals for interviews.

Merged into problems.json as patternPicker + per-problem whenToUse.
"""

from __future__ import annotations

import real_world_hooks

# ---------------------------------------------------------------------------
# Category-level: "I see this in the problem -> reach for this pattern"
# ---------------------------------------------------------------------------

CATEGORY_WHEN: dict[str, dict] = {
    "arrays-hashing": {
        "title": "Arrays & Hashing",
        "oneLiner": "Need O(1) lookup while scanning once.",
        "useWhen": [
            "Find two values / indices / complements in one pass",
            "Count frequency of elements or characters",
            "Group items by a key or signature",
            "Detect duplicate or 'seen before?'",
            "Subarray sum / count with prefix sums",
            "Unsorted array but need fast membership",
        ],
        "keywords": [
            "two sum", "duplicate", "anagram", "frequency", "most common",
            "group", "subarray sum", "prefix", "complement", "count occurrences",
        ],
        "notWhen": [
            "Array is sorted AND you only need pair sum -> try Two Pointers first",
            "Need contiguous subarray with a sliding constraint -> Sliding Window",
            "Explicitly need sorted order output without hash -> sort + two pointers",
        ],
        "askYourself": [
            "Can I answer with one pass if I remember what I've seen?",
            "Is the question about counts, pairs, or grouping?",
            "Do I need value -> index, value -> count, or key -> bucket?",
        ],
    },
    "two-pointers": {
        "title": "Two Pointers",
        "oneLiner": "Sorted data or opposite ends; move L or R based on comparison.",
        "useWhen": [
            "Array/string is sorted (or can be sorted)",
            "Find pair/triplet with target sum",
            "Compare from both ends (palindrome, container area)",
            "Remove duplicates in-place on sorted array",
            "Merge two sorted sequences",
        ],
        "keywords": [
            "sorted", "palindrome", "two sum II", "3sum", "container",
            "pair with sum", "in-place", "non-decreasing",
        ],
        "notWhen": [
            "Unsorted and need original indices -> hashing",
            "Need all subarrays / variable window -> sliding window",
        ],
        "askYourself": [
            "Is the input sorted (or sortable without breaking the problem)?",
            "Can I move one pointer based on whether sum is too small/big?",
        ],
    },
    "sliding-window": {
        "title": "Sliding Window",
        "oneLiner": "Contiguous subarray/substring; expand R, shrink L when invalid.",
        "useWhen": [
            "Longest/shortest contiguous subarray with sum constraint",
            "Longest substring without repeats",
            "Fixed-size window of length k (max average, etc.)",
            "Buy/sell with running min (special case of window on index)",
        ],
        "keywords": [
            "subarray", "substring", "contiguous", "window", "longest",
            "minimum size", "at most k distinct", "without repeating",
            "max average", "consecutive elements",
        ],
        "notWhen": [
            "Non-contiguous subsequence -> DP or greedy",
            "Pair in unsorted array -> hash",
            "Count subarrays by sum k with negatives -> prefix hash (Arrays & Hashing)",
        ],
        "askYourself": [
            "Does 'contiguous' or 'substring/subarray' appear?",
            "Can I expand right and only shrink left when a rule breaks?",
        ],
    },
    "stack": {
        "title": "Stack",
        "oneLiner": "Process in order; match/resolve against the most recent unmatched item.",
        "useWhen": [
            "Valid parentheses / bracket matching",
            "Next greater/smaller element (monotonic stack)",
            "Evaluate expressions, daily temperatures",
            "Undo/match with most recent opener",
        ],
        "keywords": [
            "parentheses", "brackets", "valid", "next greater", "daily temperatures",
            "monotonic", "matching", "nested",
        ],
        "notWhen": [
            "Need global sorted order -> heap or sort",
            "Graph connectivity -> BFS/DFS",
        ],
        "askYourself": [
            "Am I matching a closing thing to the last opening thing?",
            "Do I need 'next bigger/smaller' while scanning left-to-right?",
        ],
    },
    "binary-search": {
        "title": "Binary Search",
        "oneLiner": "Search space is monotonic — halve it each step.",
        "useWhen": [
            "Sorted array lookup",
            "Find boundary (first >= x, last <= x)",
            "Minimize/maximize answer where feasible(mid) is monotonic",
            "Matrix flattened as sorted (search 2D)",
            "Koko bananas, ship packages, capacity problems",
        ],
        "keywords": [
            "sorted", "log n", "find minimum maximum", "feasible",
            "search rotated", "2d matrix", "eating speed", "capacity",
        ],
        "notWhen": [
            "Unsorted one-pass membership -> hash",
            "All pairs -> two pointers or hash",
        ],
        "askYourself": [
            "If I try a candidate mid, can I tell 'too low' vs 'too high' in O(1)?",
            "Is the answer space sorted or monotonic?",
        ],
    },
    "linked-list": {
        "title": "Linked List",
        "oneLiner": "Pointer tricks: prev/curr/nxt, fast/slow, dummy head.",
        "useWhen": [
            "Reverse, merge, reorder list",
            "Cycle detection (Floyd tortoise/hare)",
            "Find middle, nth from end",
            "Two lists with different lengths",
        ],
        "keywords": [
            "linked list", "ListNode", "reverse", "merge", "cycle",
            "intersection", "middle node", "remove nth",
        ],
        "notWhen": [
            "Random access by index needed -> array",
            "Tree structure -> tree DFS/BFS",
        ],
        "askYourself": [
            "Do I need slow/fast pointers or prev/curr/nxt?",
            "Will a dummy head simplify edge cases?",
        ],
    },
    "trees": {
        "title": "Trees",
        "oneLiner": "DFS for paths/structure; BFS for level-by-level.",
        "useWhen": [
            "Height, depth, same tree, invert, path sum",
            "Level order / zigzag traversal",
            "BST property (LCA, validate, kth smallest)",
            "Diameter, max path (often DFS return values)",
        ],
        "keywords": [
            "binary tree", "TreeNode", "root", "leaf", "depth", "height",
            "level order", "BST", "subtree", "LCA",
        ],
        "notWhen": [
            "General graph with cycles -> graph BFS/DFS + visited",
            "Sorted array problem disguised as tree walk -> maybe just BST property",
        ],
        "askYourself": [
            "What do I return from each node to its parent?",
            "Do I need all nodes at depth d (BFS) or a root-to-leaf path (DFS)?",
        ],
    },
    "heap": {
        "title": "Heap / Priority Queue",
        "oneLiner": "Repeatedly need the current min or max efficiently.",
        "useWhen": [
            "Kth largest/smallest (size-k heap)",
            "Top k frequent after counting",
            "Merge k sorted lists",
            "Stream of numbers — keep best k",
            "Two smallest/largest at each step",
        ],
        "keywords": [
            "kth largest", "kth smallest", "top k", "priority", "heap",
            "merge k", "most frequent", "smallest range",
        ],
        "notWhen": [
            "Full sort is fine and n is small -> sort",
            "Only need one pass count -> hash then sort keys",
        ],
        "askYourself": [
            "Do I only care about the best k items, not full ordering?",
            "Am I merging many sorted things?",
        ],
    },
    "backtracking": {
        "title": "Backtracking",
        "oneLiner": "Build choice by choice; undo when dead end.",
        "useWhen": [
            "All subsets, permutations, combinations",
            "Combination sum (reuse allowed or not)",
            "Generate all valid boards/parentheses",
            "Explore all paths with constraints",
        ],
        "keywords": [
            "all possible", "subsets", "permutations", "combinations",
            "combination sum", "generate", "partition", "choose",
        ],
        "notWhen": [
            "Count only (not enumerate) -> often DP",
            "Greedy proof exists -> greedy",
            "Single optimal path -> DP/graph",
        ],
        "askYourself": [
            "Do they want ALL answers or just one?",
            "Choose -> recurse -> undo — does that fit?",
        ],
    },
    "graphs": {
        "title": "Graphs",
        "oneLiner": "Nodes + edges; mark visited; BFS for layers, DFS for flood fill.",
        "useWhen": [
            "Grid as graph (islands, rotting oranges)",
            "Course prerequisites / cycle detection",
            "Shortest path in unweighted graph (BFS)",
            "Clone graph, connected components",
            "Topological sort",
        ],
        "keywords": [
            "graph", "grid", "islands", "adjacent", "course schedule",
            "prerequisites", "connected", "shortest path", "clone",
            "rotting", "BFS", "DFS",
        ],
        "notWhen": [
            "Tree with single parent -> tree DFS (simpler)",
            "Sorted array -> not graph",
        ],
        "askYourself": [
            "Can I model this as nodes and neighbors?",
            "Do I need shortest steps (BFS) or just reachability (DFS)?",
        ],
    },
    "dp-1d": {
        "title": "1-D DP",
        "oneLiner": "Optimal substructure on a line; dp[i] from dp[i-1], dp[i-2], ...",
        "useWhen": [
            "Climbing stairs, house robber (take/skip)",
            "Coin change (min coins)",
            "Longest increasing subsequence style",
            "Decode ways, word break",
            "Max profit with state on index",
        ],
        "keywords": [
            "minimum", "maximum ways", "fewest", "rob", "stairs",
            "coin change", "cannot use adjacent", "subsequence optimal",
        ],
        "notWhen": [
            "Contiguous subarray only -> sliding window or prefix hash",
            "Generate all -> backtracking",
            "Greedy works with proof -> greedy",
        ],
        "askYourself": [
            "Can I define dp[i] = best answer using first i items?",
            "Are there only a few previous states that matter (i-1, i-2)?",
        ],
    },
    "intervals": {
        "title": "Intervals",
        "oneLiner": "Sort by start or end; merge or greedy pick.",
        "useWhen": [
            "Merge overlapping intervals",
            "Insert interval",
            "Meeting rooms / min rooms",
            "Non-overlapping interval count",
            "Schedule maximum events",
        ],
        "keywords": [
            "intervals", "overlap", "merge", "meetings", "schedule",
            "start time", "end time", "non-overlapping",
        ],
        "notWhen": [
            "Points on a line without intervals -> sweep or hash",
            "Single contiguous subarray -> sliding window",
        ],
        "askYourself": [
            "Should I sort by start or by end?",
            "Does merging or greedy 'keep earliest end' apply?",
        ],
    },
    "greedy": {
        "title": "Greedy",
        "oneLiner": "Local best choice each step; know why it works.",
        "useWhen": [
            "Jump game (furthest reachable)",
            "Activity selection / max non-overlapping (by end)",
            "Assign cookies, partition labels (sometimes)",
            "Minimum arrows to burst balloons (after sort)",
        ],
        "keywords": [
            "can reach", "minimum number", "maximum you can",
            "greedy", "farthest", "schedule as many",
        ],
        "notWhen": [
            "Need global optimum with overlapping subproblems -> DP",
            "All combinations -> backtracking",
        ],
        "askYourself": [
            "Does picking the locally best option never block a better global answer?",
            "Can I sort first to make greedy obvious?",
        ],
    },
    "amazon-story": {
        "title": "Amazon Story Wrappers",
        "oneLiner": "Strip the story; name the underlying LC pattern in 60 seconds.",
        "useWhen": [
            "Keywords, reviews, routes, warehouses, utilization",
            "Top k with tie-break rules",
            "Pair items from two lists with sum constraint",
            "Log parsing / frequency on strings",
        ],
        "keywords": [
            "keyword", "review", "route", "forward", "return",
            "utilization", "customer", "order", "warehouse", "pair",
        ],
        "notWhen": [
            "Never invent a new algorithm for the story — map to known pattern",
        ],
        "askYourself": [
            "If I rename nouns to nums/strings, which NeetCode bucket is this?",
            "Is it count + top k? Two pointers on sorted pairs? Interval merge?",
        ],
    },
}

# Quick decision tree (shown in UI)
DECISION_STEPS: list[dict] = [
    {
        "q": "Does the problem say contiguous subarray or substring?",
        "yes": "Sliding Window (or prefix hash if sum equals k with negatives)",
        "no": "next",
    },
    {
        "q": "Is the array sorted (or sortable) and you need a pair/triplet sum?",
        "yes": "Two Pointers",
        "no": "next",
    },
    {
        "q": "Do you need O(1) lookup of something you've seen (count, index, complement)?",
        "yes": "Arrays & Hashing",
        "no": "next",
    },
    {
        "q": "Is it a tree or BST?",
        "yes": "Trees (DFS/BFS)",
        "no": "next",
    },
    {
        "q": "Is it a grid, graph, prerequisites, or connected components?",
        "yes": "Graphs",
        "no": "next",
    },
    {
        "q": "Do you need ALL combinations/subsets/permutations?",
        "yes": "Backtracking",
        "no": "next",
    },
    {
        "q": "Is the search space or answer monotonic (binary search on answer)?",
        "yes": "Binary Search",
        "no": "next",
    },
    {
        "q": "Do you need top k / repeated min-max?",
        "yes": "Heap",
        "no": "next",
    },
    {
        "q": "Intervals, meetings, overlap?",
        "yes": "Intervals",
        "no": "next",
    },
    {
        "q": "Optimal take/skip or min coins on a sequence?",
        "yes": "1-D DP",
        "no": "Re-read constraints — start with brute force then upgrade",
    },
]

# Per-problem: concrete triggers (merged into patternGuide.whenToUse)
PROBLEM_WHEN: dict[str, dict] = {
    "ah-contains-duplicate": {
        "reachFor": "Hash SET — membership only",
        "signals": ["any duplicate?", "distinct?", "appears twice"],
        "notThis": ["need indices of pair -> Two Sum", "count how many -> Counter"],
    },
    "ah-two-sum": {
        "reachFor": "Hash DICT — complement lookup + store index",
        "signals": ["two numbers add to target", "return indices", "exactly one solution"],
        "notThis": ["array already sorted -> Two Sum II two pointers", "all pairs -> sort + two pointers"],
    },
    "ah-group-anagrams": {
        "reachFor": "Hash DICT — key = signature, value = bucket list",
        "signals": ["group anagrams", "same letters rearranged"],
        "notThis": ["just check two strings -> Valid Anagram", "top k words -> count + sort"],
    },
    "ah-top-k-frequent": {
        "reachFor": "Count (hash) then rank — NOT letter-sort keys",
        "signals": ["k most frequent", "top k elements"],
        "notThis": ["Group Anagrams sorts letters inside a word", "need kth only -> heap size k"],
    },
    "ah-subarray-sum-k": {
        "reachFor": "Prefix sum + hash of prefix COUNTS",
        "signals": ["subarray sum equals k", "number of subarrays", "contiguous sum"],
        "notThis": ["only positive nums min length -> sliding window", "max sum subarray -> Kadane"],
    },
    "ah-valid-anagram": {
        "reachFor": "Frequency map / Counter",
        "signals": ["anagram?", "same characters"],
        "notThis": ["many strings -> Group Anagrams"],
    },
    "ah-product-except-self": {
        "reachFor": "Prefix + suffix passes (no division)",
        "signals": ["product except self", "no division", "O(n) no extra array"],
        "notThis": ["simple product -> one pass", "subarray product -> sliding window unlikely"],
    },
    "ah-longest-consecutive": {
        "reachFor": "Hash SET + only start streaks at sequence beginnings",
        "signals": ["longest consecutive sequence", "unsorted", "O(n)"],
        "notThis": ["sorted -> scan once", "subarray -> window/hash"],
    },
    "sw-longest-substring": {
        "reachFor": "Sliding window + last seen index",
        "signals": ["longest substring", "without repeating", "distinct characters"],
        "notThis": ["subsequence not substring -> DP", "exactly k distinct -> window + hash count"],
    },
    "sw-best-stock": {
        "reachFor": "One pass: track min price, max profit",
        "signals": ["buy and sell stock once", "max profit", "best day"],
        "notThis": ["unlimited transactions -> different pattern", "cooldown -> DP"],
    },
    "sw-min-subarray": {
        "reachFor": "Variable sliding window (sum >= target)",
        "signals": ["minimum length subarray", "sum >= target", "positive integers"],
        "notThis": ["negative numbers -> prefix hash", "max length -> different constraint"],
    },
    "tp-two-sum-ii": {
        "reachFor": "Two pointers on SORTED array",
        "signals": ["sorted", "two numbers", "1-indexed indices"],
        "notThis": ["unsorted -> hash Two Sum"],
    },
    "tp-3sum": {
        "reachFor": "Sort + fix one + two pointers",
        "signals": ["three numbers sum to zero", "triplets", "no duplicate triplets"],
        "notThis": ["two sum only -> simpler", "any length subarray -> hash/window"],
    },
    "tp-valid-palindrome": {
        "reachFor": "Two pointers inward + skip junk",
        "signals": ["palindrome", "alphanumeric only", "ignore case"],
        "notThis": ["longest palindromic substring -> expand or DP"],
    },
    "st-valid-parentheses": {
        "reachFor": "Stack match open/close",
        "signals": ["valid parentheses", "brackets match", "nested"],
        "notThis": ["generate all -> backtracking", "longest valid substring -> stack variant"],
    },
    "bs-binary-search": {
        "reachFor": "Classic binary search on sorted array",
        "signals": ["sorted array", "find target", "O(log n)"],
        "notThis": ["unsorted -> hash", "find first bad -> binary search on answer variant"],
    },
    "gr-num-islands": {
        "reachFor": "Grid DFS/BFS flood fill",
        "signals": ["number of islands", "connected 1s", "grid"],
        "notThis": ["shortest path steps -> BFS with distance", "tree -> simpler DFS"],
    },
    "gr-course-schedule": {
        "reachFor": "Graph cycle detect / topological sort",
        "signals": ["prerequisites", "can finish all courses", "dependency"],
        "notThis": ["shortest path -> BFS", "tree ordering -> DFS postorder"],
    },
    "dp-climbing-stairs": {
        "reachFor": "1-D DP / Fibonacci",
        "signals": ["how many ways", "1 or 2 steps", "distinct ways"],
        "notThis": ["min cost -> weighted DP", "forbidden steps -> DP with state"],
    },
    "dp-house-robber": {
        "reachFor": "Take/skip DP on line",
        "signals": ["cannot rob adjacent", "maximum money", "non-adjacent"],
        "notThis": ["circular houses -> DP variant", "path on tree -> tree DP"],
    },
    "am-top-k-keywords": {
        "reachFor": "Strip story -> Counter + sort by (-freq, word)",
        "signals": ["top k keywords", "most frequent words", "tie-break lexicographic"],
        "notThis": ["Top K Frequent Elements on integers — same pattern"],
    },
}


def get_category_when(category_id: str) -> dict:
    return CATEGORY_WHEN.get(category_id, CATEGORY_WHEN["arrays-hashing"])


def get_problem_when(problem_id: str, category_id: str) -> dict:
    if problem_id in PROBLEM_WHEN:
        base = dict(PROBLEM_WHEN[problem_id])
    else:
        cat = get_category_when(category_id)
        base = {
            "reachFor": cat["title"],
            "signals": cat["keywords"][:4],
            "notThis": cat["notWhen"][:2],
        }
    return real_world_hooks.merge_into(base, problem_id)


def build_picker() -> dict:
    return {
        "decisionSteps": DECISION_STEPS,
        "categories": [
            {"id": cid, **data}
            for cid, data in CATEGORY_WHEN.items()
        ],
    }

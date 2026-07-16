"""
Memorable real-world hooks — "when you hear this in an interview/OA, think this problem."

Merged into whenToUse.realWorld + whenToUse.interviewHeard
"""

from __future__ import annotations

# problem_id -> { realWorld, interviewHeard, lcAnchor (optional) }
REAL_WORLD: dict[str, dict] = {
    "ah-contains-duplicate": {
        "interviewHeard": "Has this user ID / email / SKU appeared before in the batch?",
        "realWorld": "Fraud check: scan millions of checkout events — if the same payment fingerprint appears twice, flag duplicate. One hash set pass, O(n).",
        "lcAnchor": "LC 217 — classic warm-up; same pattern as 'first repeated character' stories.",
    },
    "ah-two-sum": {
        "interviewHeard": "Find two packages whose weights exactly hit the shipping limit.",
        "realWorld": "Amazon OA favorite: pair items from an unsorted list that sum to a target (gift card balance, carton weight). Return positions, not values.",
        "lcAnchor": "LC 1 — if they say sorted array, switch to Two Sum II.",
    },
    "ah-valid-anagram": {
        "interviewHeard": "Are these two login tokens the same letters rearranged?",
        "realWorld": "Compare two strings built from the same character multiset — typo squatting detection, scrambled warehouse bin codes.",
        "lcAnchor": "LC 242",
    },
    "ah-group-anagrams": {
        "interviewHeard": "Cluster customer review keywords that are rearrangements of each other.",
        "realWorld": "Search logs: group queries that are anagrams ('listen' / 'silent') for trending topic buckets.",
        "lcAnchor": "LC 49",
    },
    "ah-top-k-frequent": {
        "interviewHeard": "What are the k most-clicked product IDs this hour?",
        "realWorld": "Metrics dashboard: count events in a hash map, then rank — Top K Keywords OA is the same with tie-break on strings.",
        "lcAnchor": "LC 347 area; Amazon story: Top K Keywords.",
    },
    "ah-product-except-self": {
        "interviewHeard": "Each warehouse reports throughput relative to all other sites combined.",
        "realWorld": "Without division: each output slot = product of everything left × everything right — latency attribution across nodes.",
        "lcAnchor": "LC 238",
    },
    "ah-longest-consecutive": {
        "interviewHeard": "Longest run of consecutive ticket numbers in an unsorted dump.",
        "realWorld": "ID sequences in shuffled logs — hash set + only start counting when n-1 is missing.",
        "lcAnchor": "LC 128",
    },
    "ah-subarray-sum-k": {
        "interviewHeard": "How many contiguous hour-blocks of sales sum exactly to the promo threshold?",
        "realWorld": "Prefix sum + count of earlier prefixes — same complement idea as Two Sum on running totals.",
        "lcAnchor": "LC 560",
    },
    "ah-encode-decode": {
        "interviewHeard": "Serialize a list of variable-length strings for the wire without delimiter collisions.",
        "realWorld": "Length-prefix encoding (4#lint) — used in RPC/log framing when delimiters appear inside payloads.",
        "lcAnchor": "LC 271",
    },
    "tp-valid-palindrome": {
        "interviewHeard": "Is this product code the same forwards and backwards ignoring dashes?",
        "realWorld": "Two pointers from both ends, skip junk chars — palindrome checks on user input.",
        "lcAnchor": "LC 125",
    },
    "tp-two-sum-ii": {
        "interviewHeard": "Sorted price list — pick two products that hit budget (return 1-indexed positions).",
        "realWorld": "Two pointers on sorted array — move L/R based on sum vs target. NOT hash — array is already sorted.",
        "lcAnchor": "LC 167",
    },
    "tp-3sum": {
        "interviewHeard": "Find three shipment weights that balance to zero variance (sum to zero).",
        "realWorld": "Sort + fix one value + two pointers — watch duplicate triplets.",
        "lcAnchor": "LC 15",
    },
    "tp-container-water": {
        "interviewHeard": "Two vertical barriers — max water trapped between them.",
        "realWorld": "Classic two-pointer from ends; area = min height × width.",
        "lcAnchor": "LC 11",
    },
    "sw-best-stock": {
        "interviewHeard": "One buy, one sell — max profit on historical prices.",
        "realWorld": "Track min price so far, best spread — stock ticker one-pass.",
        "lcAnchor": "LC 121",
    },
    "sw-longest-substring": {
        "interviewHeard": "Longest stretch of a log with no repeated error code.",
        "realWorld": "Sliding window + last-seen index — shrink when char repeats inside window.",
        "lcAnchor": "LC 3",
    },
    "sw-min-subarray": {
        "interviewHeard": "Shortest contiguous hours of sales that hit quota (all positive).",
        "realWorld": "Variable window — expand until sum >= target, shrink to minimize length.",
        "lcAnchor": "LC 209",
    },
    "sw-max-avg-subarray": {
        "interviewHeard": "Best k-hour average throughput in a metrics stream.",
        "realWorld": "Fixed-size sliding window sum / k.",
        "lcAnchor": "LC 643",
    },
    "st-valid-parentheses": {
        "interviewHeard": "Is this nested JSON/bracket config valid?",
        "realWorld": "Stack matches each closer to the most recent opener — config validators.",
        "lcAnchor": "LC 20",
    },
    "st-daily-temperatures": {
        "interviewHeard": "Days until a warmer day for each daily reading.",
        "realWorld": "Monotonic decreasing stack of indices — classic 'next greater element'.",
        "lcAnchor": "LC 739",
    },
    "st-min-stack": {
        "interviewHeard": "Stack that supports getMin in O(1) — rolling min in a stream.",
        "realWorld": "Parallel min stack alongside values — design data structure question.",
        "lcAnchor": "LC 155",
    },
    "bs-binary-search": {
        "interviewHeard": "Find SKU in sorted catalog in log time.",
        "realWorld": "Halve search space on sorted data — foundation for harder BS-on-answer problems.",
        "lcAnchor": "LC 704",
    },
    "bs-koko": {
        "interviewHeard": "Minimum conveyor speed to finish all packages by deadline.",
        "realWorld": "Binary search on answer — feasible(speed) monotonic, minimize speed.",
        "lcAnchor": "LC 875",
    },
    "bs-search-2d": {
        "interviewHeard": "Find value in row-column sorted matrix as if one long sorted array.",
        "realWorld": "Binary search with index → (row, col) mapping.",
        "lcAnchor": "LC 74",
    },
    "ll-reverse-list": {
        "interviewHeard": "Reverse a singly linked chain (undo stack, playlist).",
        "realWorld": "prev/curr/nxt pointer flip in one pass.",
        "lcAnchor": "LC 206",
    },
    "ll-has-cycle": {
        "interviewHeard": "Does this linked process chain loop forever?",
        "realWorld": "Floyd tortoise/hare — cycle detection in linked structures.",
        "lcAnchor": "LC 141",
    },
    "ll-merge-two": {
        "interviewHeard": "Merge two sorted delivery ID lists into one.",
        "realWorld": "Dummy head + two pointers — merge pattern for sorted linked lists.",
        "lcAnchor": "LC 21",
    },
    "tr-max-depth": {
        "interviewHeard": "How deep is this org chart / category tree?",
        "realWorld": "DFS: 1 + max(left, right) on null base.",
        "lcAnchor": "LC 104",
    },
    "tr-invert-tree": {
        "interviewHeard": "Mirror a binary tree (swap left/right all the way down).",
        "realWorld": "Recursive swap children — tree DFS.",
        "lcAnchor": "LC 226",
    },
    "tr-same-tree": {
        "interviewHeard": "Are these two category hierarchies identical?",
        "realWorld": "Parallel DFS structural compare.",
        "lcAnchor": "LC 100",
    },
    "tr-level-order": {
        "interviewHeard": "Print org chart level by level.",
        "realWorld": "BFS queue — drain len(queue) per level.",
        "lcAnchor": "LC 102",
    },
    "tr-lca-bst": {
        "interviewHeard": "Lowest common manager for two employees in a BST org.",
        "realWorld": "Walk BST using ordering — split point is LCA.",
        "lcAnchor": "LC 235",
    },
    "hp-kth-largest": {
        "interviewHeard": "Kth highest latency in today's sample (without full sort).",
        "realWorld": "Size-k min-heap streaming top k.",
        "lcAnchor": "LC 215",
    },
    "hp-last-stone": {
        "interviewHeard": "Repeatedly smash two heaviest stones — last weight left.",
        "realWorld": "Max-heap via negated heapq in Python.",
        "lcAnchor": "LC 1046",
    },
    "gr-num-islands": {
        "interviewHeard": "Count disconnected warehouse zones on a grid map.",
        "realWorld": "Flood fill DFS/BFS — Amazon loves grid graphs.",
        "lcAnchor": "LC 200",
    },
    "gr-rotting-oranges": {
        "interviewHeard": "Minutes until all fresh inventory adjacent to rotten spreads.",
        "realWorld": "Multi-source BFS from all rotten cells at once.",
        "lcAnchor": "LC 994",
    },
    "gr-course-schedule": {
        "interviewHeard": "Can you finish all training modules given prerequisites?",
        "realWorld": "Cycle detection / topological sort — dependency graphs.",
        "lcAnchor": "LC 207",
    },
    "gr-clone-graph": {
        "interviewHeard": "Deep copy a network of connected nodes.",
        "realWorld": "DFS + hash map old→new node.",
        "lcAnchor": "LC 133",
    },
    "bt-subsets": {
        "interviewHeard": "All possible feature flag combinations.",
        "realWorld": "Backtracking include/exclude each element.",
        "lcAnchor": "LC 78",
    },
    "bt-permutations": {
        "interviewHeard": "All orderings of tasks on a truck route.",
        "realWorld": "Backtracking with used[] array.",
        "lcAnchor": "LC 46",
    },
    "bt-combination-sum": {
        "interviewHeard": "Which coin combos make exact change (reuse allowed)?",
        "realWorld": "DFS reuse same index — combination sum pattern.",
        "lcAnchor": "LC 39",
    },
    "gd-jump-game": {
        "interviewHeard": "Can you reach the last delivery stop given max jump per mile?",
        "realWorld": "Greedy farthest reachable index.",
        "lcAnchor": "LC 55",
    },
    "in-merge-intervals": {
        "interviewHeard": "Merge overlapping meeting / shift windows.",
        "realWorld": "Sort by start, merge if overlap — scheduling.",
        "lcAnchor": "LC 56",
    },
    "in-non-overlap": {
        "interviewHeard": "Minimum meetings to cancel so none overlap.",
        "realWorld": "Sort by end, greedy keep — interval scheduling.",
        "lcAnchor": "LC 435",
    },
    "dp-climbing-stairs": {
        "interviewHeard": "How many ways to climb n steps taking 1 or 2 at a time?",
        "realWorld": "Fibonacci DP — count paths.",
        "lcAnchor": "LC 70",
    },
    "dp-house-robber": {
        "interviewHeard": "Max value robbing houses without hitting neighbors.",
        "realWorld": "Take/skip DP on a line — max of prev vs prev2+current.",
        "lcAnchor": "LC 198",
    },
    "dp-coin-change": {
        "interviewHeard": "Fewest coins to make exact change.",
        "realWorld": "Unbounded knapsack DP bottom-up.",
        "lcAnchor": "LC 322",
    },
    "dp-longest-palindrome-subseq": {
        "interviewHeard": "Longest palindrome you can build by deleting chars from a string.",
        "realWorld": "LCS(s, reverse(s)).",
        "lcAnchor": "LC 516",
    },
    "am-top-k-keywords": {
        "interviewHeard": "Top k words in reviews; break ties alphabetically.",
        "realWorld": "Amazon OA wrapper on Top K Frequent — Counter + sort (-freq, word).",
        "lcAnchor": "Not LC — pure Amazon OA story.",
    },
    "am-optimal-utilization": {
        "interviewHeard": "Pair a forward route with a return route closest to target without going over.",
        "realWorld": "Amazon airplane utilization OA — two sorted lists + two pointers / scan.",
        "lcAnchor": "Not LC — map to two-sum-on-sorted-pairs.",
    },
}


def merge_into(when: dict, problem_id: str) -> dict:
    hook = REAL_WORLD.get(problem_id, {})
    if hook:
        when = {**when, **hook}
    return when

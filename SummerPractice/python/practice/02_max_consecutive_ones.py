"""
Problem 02: Max Consecutive Ones

Reinforces the pattern from LC 605 (Can Place Flowers):
    walk an array index-by-index, maintain running state as you go,
    update a final answer based on that state. Edge conditions at
    the end of the array matter!

------------------------------------------------------------------------
PROBLEM

Given a binary list `nums` (each element is 0 or 1), return the
maximum number of CONSECUTIVE 1's in the list.

------------------------------------------------------------------------
EXAMPLES

Example 1:
    Input:  nums = [1, 1, 0, 1, 1, 1]
    Output: 3
    Explanation: The longest run of 1's is the final three -> length 3.
                 (The first two 1's are a run of 2, which is shorter.)

Example 2:
    Input:  nums = [1, 0, 1, 1, 0, 1]
    Output: 2

Example 3:
    Input:  nums = [0, 0, 0]
    Output: 0

Example 4:
    Input:  nums = [1, 1, 1, 1]
    Output: 4

------------------------------------------------------------------------
CONSTRAINTS
    1 <= len(nums) <= 10^5
    nums[i] is 0 or 1.

------------------------------------------------------------------------
WHAT TO THINK ABOUT BEFORE CODING

1. You need TWO pieces of state as you scan:
     - the length of the CURRENT run of 1's you're in
     - the BEST (longest) run you've seen so far
   What should each start at? When does each update?

2. When you see a 1, the current run extends by 1.
   When you see a 0, the current run resets. To what?

3. When do you compare "current run" against "best run"?
   Is it enough to do it only when you see a 0, or do you also
   need to do it somewhere else?  (Hint: think about the LAST
   element of the list being a 1 -- you never hit a 0 to trigger
   the comparison. This is the LC 605-style edge case.)
"""


def findMaxConsecutiveOnes(nums):
    """
    :type nums: list[int]
    :rtype: int
    """
    # YOUR CODE HERE
    pass


# ------------------------------------------------------------------------
# TESTS
# ------------------------------------------------------------------------
if __name__ == "__main__":
    cases = [
        ([1, 1, 0, 1, 1, 1],   3),
        ([1, 0, 1, 1, 0, 1],   2),
        ([0, 0, 0],            0),
        ([1, 1, 1, 1],         4),   # all ones -> tests the "end of array" edge case
        ([1],                  1),   # single element, one
        ([0],                  0),   # single element, zero
        ([0, 1, 0, 1, 0, 1],   1),   # alternating
        ([1, 1, 1, 0, 1, 1],   3),   # longest run is at the start
    ]

    passed = 0
    for i, (nums, expected) in enumerate(cases, start=1):
        got = findMaxConsecutiveOnes(nums)
        ok = got == expected
        status = "PASS" if ok else "FAIL"
        print(f"Case {i}: {status}  (expected {expected}, got {got})")
        if ok:
            passed += 1

    print(f"\n{passed}/{len(cases)} cases passed")


# ------------------------------------------------------------------------
# HINTS (progressive)
# ------------------------------------------------------------------------
#
# HINT 1 (state variables):
#     current = 0          # length of the run you're currently in
#     best    = 0          # longest run seen so far
#
# HINT 2 (update rule inside the loop):
#     for num in nums:
#         if num == 1:
#             current += 1
#             # ...
#         else:
#             current = 0
#
# HINT 3 (where to update `best`):
#     You can either:
#       (a) update best inside the `if num == 1` branch:  best = max(best, current)
#       (b) update best only when you see a 0, BUT then you also have to
#           remember to check once more AFTER the loop ends, because a list
#           that ends on 1's never triggered the zero-branch update.
#     Option (a) is simpler and has no trailing edge case. Prefer it.
#
# HINT 4 (complexity):
#     O(n) time, O(1) space. One pass, no extra structures.
#
# CONNECTION TO LC 605:
#     Both problems walk the array once while tracking state. The "edge at
#     the end" issue -- forgetting to do a final check after the loop --
#     is the same class of bug as forgetting that index 0 has no left
#     neighbor. Handle edges deliberately, not accidentally.

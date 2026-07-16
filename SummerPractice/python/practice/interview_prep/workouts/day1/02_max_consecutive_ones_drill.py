"""
Day 1 Drill 2: Max Consecutive Ones

Goal:
- Practice one-pass state tracking.
- Keep current streak and best streak.

Timer target: 15 minutes
"""


def findMaxConsecutiveOnes(nums):
    """
    :type nums: list[int]
    :rtype: int
    """
    # return the max of the sum of each consecutive ones
    max_consecutive_ones = 0
    current_consecutive_ones = 0
    for num in nums:
        if num == 1:
            current_consecutive_ones += 1
        else:
            max_consecutive_ones = max(max_consecutive_ones, current_consecutive_ones)
            current_consecutive_ones = 0
    return max(max_consecutive_ones, current_consecutive_ones)

  


if __name__ == "__main__":
    cases = [
        ([1, 1, 0, 1, 1, 1], 3),
        ([1, 0, 1, 1, 0, 1], 2),
        ([0, 0, 0], 0),
        ([1, 1, 1, 1], 4),
        ([1], 1),
        ([0], 0),
        ([0, 1, 0, 1, 0, 1], 1),
        ([1, 1, 1, 0, 1, 1], 3),
    ]

    passed = 0
    for i, (nums, expected) in enumerate(cases, start=1):
        got = findMaxConsecutiveOnes(nums)
        ok = got == expected
        print(f"Case {i}: {'PASS' if ok else 'FAIL'} (expected {expected}, got {got})")
        if ok:
            passed += 1

    print(f"\n{passed}/{len(cases)} cases passed")

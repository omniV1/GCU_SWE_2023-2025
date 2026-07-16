"""
Day 2 Drill 2: Move Zeroes (LC 283)

Pattern: two pointers in array (in-place).
"""


def moveZeroes(nums):
    """
    :type nums: list[int]
    :rtype: None
    """
    # TODO: implement from memory, modify nums in place
    pass


if __name__ == "__main__":
    cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 1], [1, 0, 0]),
        ([4, 0, 5, 0, 0, 3], [4, 5, 3, 0, 0, 0]),
    ]

    passed = 0
    for i, (nums, expected) in enumerate(cases, start=1):
        moveZeroes(nums)
        ok = nums == expected
        print(f"Case {i}: {'PASS' if ok else 'FAIL'} (expected {expected}, got {nums})")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} cases passed")

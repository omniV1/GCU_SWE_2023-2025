"""
Pattern Pack: Sliding Window Variants
"""


def longest_unique_substring_v1(s):
    """Length of longest substring without repeating chars."""
    # TODO
    pass


def max_sum_subarray_k_v2(nums, k):
    """Maximum sum of any contiguous subarray of size k."""
    # TODO
    pass


def min_len_subarray_at_least_target_v3(target, nums):
    """Minimum length of contiguous subarray with sum >= target, else 0."""
    # TODO
    pass


if __name__ == "__main__":
    # v1 edge cases
    assert longest_unique_substring_v1("abcabcbb") == 3
    assert longest_unique_substring_v1("bbbbb") == 1
    assert longest_unique_substring_v1("") == 0

    # v2 edge cases
    assert max_sum_subarray_k_v2([1, 2, 3, 4, 5], 2) == 9
    assert max_sum_subarray_k_v2([-2, -1, -3], 2) == -3
    assert max_sum_subarray_k_v2([5], 1) == 5

    # v3 edge cases
    assert min_len_subarray_at_least_target_v3(7, [2, 3, 1, 2, 4, 3]) == 2
    assert min_len_subarray_at_least_target_v3(100, [1, 2, 3]) == 0
    assert min_len_subarray_at_least_target_v3(4, [4]) == 1

    print("All sliding window variants passed.")

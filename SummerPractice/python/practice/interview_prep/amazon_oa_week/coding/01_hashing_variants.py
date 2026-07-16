"""
Pattern Pack: Hashing / Frequency / Pairing
"""

from collections import Counter


def two_sum_v1(nums, target):
    """Return indices of two values that sum to target."""
    # use a hash map to store the indices of the numbers
    # for each number, check if the target - number is in the hash map
    # if it is, return the indices
    # if it is not, add the number and its index to the hash map
    hash_map = {}
    for i, num in enumerate(nums):
        if target - num in hash_map:
            return [hash_map[target - num], i]
        hash_map[num] = i
    return []


def two_sum_v2_count_pairs(nums, target):
    """Return number of unique index pairs whose values sum to target."""
    #  create an empty array that we will fill with pairs that sum to target.
    seen = {} 
    # initalize pairs to 0 
    pairs = 0
    # create a for loop to iterate through the given array
    for x in nums: 
        # set target such that when target is for example 3 x is 7
        need = target - x
        # Do we currently have at least one unmatched complement available?
        if seen.get(need,0)>0:
        # if the above is true add 1 to pairs 
            pairs += 1 
        # if the above is true consume one count of the complement
            seen[need] -= 1
        else:
            # if the above is not true and seen of a given is iterated forward through the array
            seen[x] = seen.get(x,0) + 1
    return pairs


def sort_by_frequency_v3(nums):
    """
    Sort by ascending frequency, then ascending value.
    Example: [4,4,1,2,2,3] -> [1,3,2,2,4,4]
    """
    # counter gives each values frequency
    freq = Counter(nums)
    # sort key (freq[x], x) -> lower frequency first, if tied lower numeric value first
    return sorted(nums, key=lambda x: (freq[x], x))

    


if __name__ == "__main__":
    # v1
    out = two_sum_v1([2, 7, 11, 15], 9)
    assert out in ([0, 1], [1, 0])
    assert set(two_sum_v1([3, 2, 4], 6)) == {1, 2}

    # v2 edge cases
    assert two_sum_v2_count_pairs([1, 1, 1, 1], 2) == 2
    assert two_sum_v2_count_pairs([1, 2, 3, 4, 5], 6) == 2
    assert two_sum_v2_count_pairs([], 10) == 0

    # v3 edge cases
    assert sort_by_frequency_v3([4, 4, 1, 2, 2, 3]) == [1, 3, 2, 2, 4, 4]
    assert sort_by_frequency_v3([5]) == [5]
    assert sort_by_frequency_v3([]) == []

    print("All hashing variants passed.")

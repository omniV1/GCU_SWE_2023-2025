"""
Hashing OA Drill Set

Run:
    python 00_hashing_bootcamp_drills.py
"""

from collections import Counter



def contains_duplicate_drill(nums):
    """
    Given an integer array nums, return True if any value appears at least twice
    in the array, and return False if every element is distinct.
    """
    seen = set()    

    for x in nums: 
        if x in seen: 
            return True
        else: 
           seen.add(x)
    return False 
     


    

def first_unique_char_index_drill(s):
    """
    Given a string s, return the index of the first non-repeating character.
    If it does not exist, return -1.
    """
    freq = Counter(s)
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
        
    return -1 


def is_anagram_drill(s, t):
    """
    Given two strings s and t, return True if t is an anagram of s, and
    False otherwise.
    """
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t) 
        
    
    



def two_sum_disjoint_pairs_drill(nums, target):
    """
    Given an integer array nums and an integer target, return the number of
    disjoint pairs whose sum is target. Each element may be used at most once.
    """
    
    


def subarray_sum_equals_k_drill(nums, k):
    """
    Given an integer array nums and an integer k, return the total number of
    continuous subarrays whose sum equals k.
    """
    pass


if __name__ == "__main__":
    # Public sample tests
    assert contains_duplicate_drill([1, 2, 3, 1]) is True
    assert contains_duplicate_drill([1, 2, 3, 4]) is False

    assert first_unique_char_index_drill("leetcode") == 0
    assert first_unique_char_index_drill("aabb") == -1

    assert is_anagram_drill("anagram", "nagaram") is True
    assert is_anagram_drill("rat", "car") is False

    assert two_sum_disjoint_pairs_drill([1, 1, 1, 1], 2) == 2
    assert two_sum_disjoint_pairs_drill([1, 2, 3, 4, 5], 6) == 2

    assert subarray_sum_equals_k_drill([1, 1, 1], 2) == 2
    assert subarray_sum_equals_k_drill([1, 2, 3], 3) == 2

    print("All sample tests passed.")

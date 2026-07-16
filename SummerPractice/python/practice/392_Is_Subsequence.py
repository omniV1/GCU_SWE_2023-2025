class Solution(object):
    def isSubsequence(self, s, t):
        """
        Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

        A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
        """
        # Your code here
        # below we had two pointers walking through the strings, and if the characters match, we move the left pointer to the right.
        # if the left pointer reaches the end of the string s, then s is a subsequence of t.
        # if the right pointer reaches the end of the string t, then s is not a subsequence of t.
        # if the left pointer reaches the end of the string s, then s is a subsequence of t.
        # Ensure we do not start out of bounds of the strings.
        left = 0
        right = 0
        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
            right += 1
        return left == len(s)
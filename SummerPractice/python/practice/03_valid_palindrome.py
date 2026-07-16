"""
Problem 03: Valid Palindrome

Reinforces the pattern from LC 345 (Reverse Vowels):
    two pointers walking inward from both ends of a string,
    skipping characters that don't qualify, doing work only when
    both pointers are "interesting."

------------------------------------------------------------------------
PROBLEM

A phrase is a PALINDROME if, after:
    - converting all uppercase letters to lowercase
    - removing all non-alphanumeric characters
it reads the same forward and backward.

Given a string `s`, return True if it's a palindrome, False otherwise.

------------------------------------------------------------------------
EXAMPLES

Example 1:
    Input:  s = "A man, a plan, a canal: Panama"
    Output: True
    Explanation: After cleaning -> "amanaplanacanalpanama", which reads
                 the same forward and backward.

Example 2:
    Input:  s = "race a car"
    Output: False
    Explanation: After cleaning -> "raceacar". 'r' != 'r' (yes), 'a' != 'a',
                 but 'c' != 'a' at the third comparison. Not a palindrome.

Example 3:
    Input:  s = " "
    Output: True
    Explanation: After cleaning -> "". An empty string is trivially a
                 palindrome. (Important edge case!)

Example 4:
    Input:  s = "0P"
    Output: False
    Explanation: After cleaning -> "0p". '0' != 'p'. Not a palindrome.
                 Note: alphanumerics include digits, so '0' stays.

------------------------------------------------------------------------
CONSTRAINTS
    1 <= len(s) <= 2 * 10^5
    s consists of printable ASCII characters.

------------------------------------------------------------------------
WHAT TO THINK ABOUT BEFORE CODING

1. DON'T build a cleaned copy of the string and reverse it -- that works
   but uses O(n) extra space. Use TWO POINTERS on the original string
   and handle skipping inline. Same idea as reverse-vowels.

2. At each step of the two-pointer walk:
       - If left points to a non-alphanumeric character, skip it (left += 1)
       - If right points to a non-alphanumeric character, skip it (right -= 1)
       - Otherwise compare the two characters (case-insensitively).
         If they differ -> return False immediately. Otherwise advance both.

3. Python helpers you'll want:
       ch.isalnum()    -> True if ch is a letter or digit
       ch.lower()      -> lowercase version of the character
   These are string methods -- you call them like "A".lower().

4. Loop condition:
       while left < right:
           ...
   When left >= right you've checked everything without finding a mismatch,
   so return True.
"""


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# ------------------------------------------------------------------------
# TESTS
# ------------------------------------------------------------------------
if __name__ == "__main__":
    cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car",                     False),
        (" ",                              True),    # edge: empty after cleaning
        ("0P",                             False),   # edge: digit vs letter
        ("a",                              True),    # single char
        ("ab",                             False),
        ("aa",                             True),
        (".,!?",                           True),    # all punctuation -> empty -> True
        ("Was it a car or a cat I saw?",   True),
        ("No 'x' in Nixon",                True),
    ]

    passed = 0
    for i, (s, expected) in enumerate(cases, start=1):
        got = isPalindrome(s)
        ok = got == expected
        status = "PASS" if ok else "FAIL"
        print(f"Case {i}: {status}  input={s!r}  (expected {expected}, got {got})")
        if ok:
            passed += 1

    print(f"\n{passed}/{len(cases)} cases passed")


# ------------------------------------------------------------------------
# HINTS (progressive)
# ------------------------------------------------------------------------
#
# HINT 1 (setup):
#     left, right = 0, len(s) - 1
#
# HINT 2 (skeleton):
#     while left < right:
#         # skip non-alphanumerics on the left
#         # skip non-alphanumerics on the right
#         # compare (case-insensitively)
#         # if mismatch -> return False
#         # otherwise advance both pointers
#     return True
#
# HINT 3 (the skipping loops):
#     You need INNER while-loops to skip junk, but be CAREFUL to also
#     re-check `left < right` inside them so you don't walk off the end
#     on a string like ".,!?":
#
#         while left < right and not s[left].isalnum():
#             left += 1
#         while left < right and not s[right].isalnum():
#             right -= 1
#
# HINT 4 (the comparison):
#     if s[left].lower() != s[right].lower():
#         return False
#     left += 1
#     right -= 1
#
# HINT 5 (complexity):
#     O(n) time -- each index is visited at most once by either pointer.
#     O(1) space -- we never build a copy of the string.
#
# CONNECTION TO LC 345:
#     Same two-pointer shape. In reverse-vowels you SWAPPED when both
#     pointers landed on a vowel. Here you COMPARE when both land on an
#     alphanumeric. The skeleton is the same; only the "what to do when
#     both qualify" step changes. Learn the skeleton -- you'll use it a lot.

"""
Day 2 Drill 3: Is Subsequence (LC 392)

Pattern: two pointers on two strings.
"""


def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # TODO: implement from memory
    pass


if __name__ == "__main__":
    cases = [
        (("abc", "ahbgdc"), True),
        (("axc", "ahbgdc"), False),
        (("", "ahbgdc"), True),
        (("abc", ""), False),
        (("ace", "abcde"), True),
    ]

    passed = 0
    for i, ((s, t), expected) in enumerate(cases, start=1):
        got = isSubsequence(s, t)
        ok = got == expected
        print(f"Case {i}: {'PASS' if ok else 'FAIL'} (expected {expected}, got {got})")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} cases passed")

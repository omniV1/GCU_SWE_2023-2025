"""
Day 1 Drill 3: Valid Palindrome

Goal:
- Practice two pointers with skip logic.
- Compare only alphanumeric chars (case-insensitive).

Timer target: 20 minutes
"""


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    # TODO: Implement this from memory.
    pass


if __name__ == "__main__":
    cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
        ("a", True),
        ("ab", False),
        ("aa", True),
        (".,!?", True),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon", True),
    ]

    passed = 0
    for i, (s, expected) in enumerate(cases, start=1):
        got = isPalindrome(s)
        ok = got == expected
        print(f"Case {i}: {'PASS' if ok else 'FAIL'} input={s!r} (expected {expected}, got {got})")
        if ok:
            passed += 1

    print(f"\n{passed}/{len(cases)} cases passed")

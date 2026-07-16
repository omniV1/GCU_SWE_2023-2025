"""
Day 2 Drill 4: Valid Parentheses (LC 20)

Pattern: stack basics.
"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    # TODO: implement from memory
    pass


if __name__ == "__main__":
    cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
    ]

    passed = 0
    for i, (s, expected) in enumerate(cases, start=1):
        got = isValid(s)
        ok = got == expected
        print(f"Case {i}: {'PASS' if ok else 'FAIL'} (expected {expected}, got {got})")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} cases passed")

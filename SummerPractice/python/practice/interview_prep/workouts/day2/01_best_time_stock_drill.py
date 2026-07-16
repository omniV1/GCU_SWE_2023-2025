"""
Day 2 Drill 1: Best Time to Buy and Sell Stock (LC 121)

Pattern: single-pass state tracking
Track minimum seen so far and best profit.
"""


def maxProfit(prices):
    """
    :type prices: list[int]
    :rtype: int
    """
    # TODO: implement from memory
    pass


if __name__ == "__main__":
    cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2], 1),
        ([2, 1, 2, 1, 0, 1, 2], 2),
        ([3], 0),
    ]

    passed = 0
    for i, (prices, expected) in enumerate(cases, start=1):
        got = maxProfit(prices)
        ok = got == expected
        print(f"Case {i}: {'PASS' if ok else 'FAIL'} (expected {expected}, got {got})")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} cases passed")

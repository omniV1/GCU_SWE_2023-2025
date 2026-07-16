"""
Day 1 Drill 1: Richest Customer Wealth

Goal:
- Practice array reduction pattern quickly.
- Return the maximum row sum from a 2D list.

Timer target: 10 minutes
"""


def maximumWealth(accounts):
    """
    :type accounts: list[list[int]]
    :rtype: int
    """
    # return the max of the sum of each customer's accounts
    # use a list comprehension to sum each customer's accounts
    # use the max function to find the maximum sum
    return max((sum(customer) for customer in accounts), default=0)

# if this file is run directly, run the tests
if __name__ == "__main__":
    # define the test cases
    cases = [
        ([[1, 2, 3], [3, 2, 1]], 6),
        ([[1, 5], [7, 3], [3, 5]], 10),
        ([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17),
        ([[100]], 100),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 3),
    ]
    # initialize the number of passed tests
    passed = 0
    for i, (accounts, expected) in enumerate(cases, start=1):
        got = maximumWealth(accounts)
        ok = got == expected
        print(f"Case {i}: {'PASS' if ok else 'FAIL'} (expected {expected}, got {got})")
        if ok:
            passed += 1

    print(f"\n{passed}/{len(cases)} cases passed")

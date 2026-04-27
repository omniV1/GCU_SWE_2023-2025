"""
Problem 01: Richest Customer Wealth

Reinforces the pattern from LC 1431 (Kids With Candies):
    iterate through a collection, compute a single summary value per element,
    then reduce across all elements.

------------------------------------------------------------------------
PROBLEM

You are given an m x n 2D list `accounts`, where accounts[i][j] is the
amount of money the i-th customer has in the j-th bank.

Return the WEALTH that the richest customer has.

A customer's wealth = the sum of their money across all banks.
The richest customer = the customer with the maximum total wealth.

------------------------------------------------------------------------
EXAMPLES

Example 1:
    Input:  accounts = [[1, 2, 3],
                        [3, 2, 1]]
    Output: 6
    Explanation: Both customers have total wealth of 6.

Example 2:
    Input:  accounts = [[1, 5],
                        [7, 3],
                        [3, 5]]
    Output: 10
    Explanation: Customer 1 has 1+5 = 6. Customer 2 has 7+3 = 10.
                 Customer 3 has 3+5 = 8. The richest is customer 2.

Example 3:
    Input:  accounts = [[2, 8, 7],
                        [7, 1, 3],
                        [1, 9, 5]]
    Output: 17

------------------------------------------------------------------------
CONSTRAINTS
    m == len(accounts)
    n == len(accounts[i])
    1 <= m, n <= 50
    1 <= accounts[i][j] <= 100
"""


def maximumWealth(accounts):
    """
    :type accounts: list[list[int]]
    :rtype: int
    """
    # YOUR CODE HERE
    return max(sum(customer) for customer in accounts)


# ------------------------------------------------------------------------
# TESTS
# Run this file directly:  python 01_richest_customer.py
# ------------------------------------------------------------------------
if __name__ == "__main__":
    cases = [
        ([[1, 2, 3], [3, 2, 1]],                     6),
        ([[1, 5], [7, 3], [3, 5]],                  10),
        ([[2, 8, 7], [7, 1, 3], [1, 9, 5]],         17),
        ([[100]],                                  100),   # single customer, single bank
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]],          3),   # all equal
    ]

    passed = 0
    for i, (accounts, expected) in enumerate(cases, start=1):
        got = maximumWealth(accounts)
        ok = got == expected
        status = "PASS" if ok else "FAIL"
        print(f"Case {i}: {status}  (expected {expected}, got {got})")
        if ok:
            passed += 1

    print(f"\n{passed}/{len(cases)} cases passed")


# ------------------------------------------------------------------------
# HINTS (peek only if stuck — progressive, reveal one at a time)
# ------------------------------------------------------------------------
#
# HINT 1:
#   Each row in `accounts` is one customer. The wealth of a customer is the
#   SUM of that row. You need the MAXIMUM wealth across all customers.
#
# HINT 2:
#   Python built-ins do the heavy lifting:
#       sum(a_list)     -> sums all numbers in the list
#       max(an_iter)    -> returns the largest element
#   How do you apply `sum` to EACH row and then take the `max` of those sums?
#
# HINT 3 (Pythonic):
#   A list comprehension like  [sum(row) for row in accounts]  gives you
#   the wealth of every customer. Wrap it in max(...) and you're done.
#
# HINT 4 (complexity):
#   m = number of customers, n = banks per customer.
#   Best solution is O(m * n) time, O(1) extra space
#   (or O(m) if you build a list of totals first).
#
# STUCK? Ask your tutor to walk you through it.

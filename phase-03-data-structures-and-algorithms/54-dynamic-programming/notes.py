# ======================================================================
# 54 — Dynamic Programming  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Fibonacci: naive vs memoized vs tabulated
# ----------------------------------------------------------------------
print("\n--- Example 1: Fibonacci: naive vs memoized vs tabulated ---")
from functools import lru_cache

# Memoized (top-down) — O(n)
@lru_cache(maxsize=None)
def fib_memo(n):
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

# Tabulated (bottom-up) — O(n) time, O(1) space
def fib_tab(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print([fib_memo(i) for i in range(10)])   # 0..34
print("fib(50) =", fib_tab(50))           # 12586269025

# ----------------------------------------------------------------------
# Example 2: Coin change: fewest coins (bottom-up DP)
# ----------------------------------------------------------------------
print("\n--- Example 2: Coin change: fewest coins (bottom-up DP) ---")
def coin_change(coins, amount):
    # dp[x] = fewest coins to make x; INF means impossible
    INF = float("inf")
    dp = [0] + [INF] * amount
    for x in range(1, amount + 1):
        for coin in coins:
            if coin <= x and dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
    return dp[amount] if dp[amount] != INF else -1

print(coin_change([1, 3, 4], 6))    # 2  (3 + 3) -> greedy would say 3!
print(coin_change([2], 3))          # -1 (impossible)
print(coin_change([1, 2, 5], 11))   # 3  (5 + 5 + 1)

# ----------------------------------------------------------------------
# Example 3: 0/1 knapsack and longest common subsequence
# ----------------------------------------------------------------------
print("\n--- Example 3: 0/1 knapsack and longest common subsequence ---")
def knapsack(weights, values, capacity):
    n = len(weights)
    # dp[i][c] = best value using first i items with capacity c
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for c in range(capacity + 1):
            dp[i][c] = dp[i - 1][c]                    # skip item i
            if weights[i - 1] <= c:                    # or take it
                dp[i][c] = max(dp[i][c],
                               dp[i - 1][c - weights[i - 1]] + values[i - 1])
    return dp[n][capacity]

print(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))   # 9

def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

print(lcs("ABCBDAB", "BDCAB"))   # 4  ("BCAB")

print("\nDone! Tip: change values above and run again to learn by experiment.")

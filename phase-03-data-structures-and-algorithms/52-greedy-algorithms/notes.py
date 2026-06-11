# ======================================================================
# 52 — Greedy Algorithms  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Activity selection (interval scheduling)
# ----------------------------------------------------------------------
print("\n--- Example 1: Activity selection (interval scheduling) ---")
def max_activities(intervals):
    # Greedy: always take the activity that FINISHES earliest
    intervals.sort(key=lambda x: x[1])      # sort by end time
    chosen = []
    last_end = float("-inf")
    for start, end in intervals:
        if start >= last_end:               # no overlap -> take it
            chosen.append((start, end))
            last_end = end
    return chosen

acts = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11)]
result = max_activities(acts)
print("count:", len(result))    # 4
print(result)                   # [(1,4),(5,7),(8,11)] (+one more)

# ----------------------------------------------------------------------
# Example 2: Coin change (greedy works for canonical coins)
# ----------------------------------------------------------------------
print("\n--- Example 2: Coin change (greedy works for canonical coins) ---")
def greedy_coins(amount, coins):
    coins = sorted(coins, reverse=True)     # biggest first
    used = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            used.append(coin)
    return used if amount == 0 else None

print(greedy_coins(63, [25, 10, 5, 1]))   # [25, 25, 10, 1, 1, 1]
print("coins used:", len(greedy_coins(63, [25, 10, 5, 1])))   # 6

# WARNING: greedy can FAIL on non-canonical coin sets:
# amount=6, coins=[1,3,4] -> greedy gives 4+1+1 (3 coins),
# but optimal is 3+3 (2 coins). Use DP there.

# ----------------------------------------------------------------------
# Example 3: Fractional knapsack (greedy by value/weight ratio)
# ----------------------------------------------------------------------
print("\n--- Example 3: Fractional knapsack (greedy by value/weight ratio) ---")
def fractional_knapsack(capacity, items):
    # items: list of (value, weight); we may take FRACTIONS
    items = sorted(items, key=lambda it: it[0] / it[1], reverse=True)
    total = 0.0
    for value, weight in items:
        if capacity >= weight:
            capacity -= weight              # take all of it
            total += value
        else:
            total += value * (capacity / weight)   # take the fraction
            break
    return total

items = [(60, 10), (100, 20), (120, 30)]   # (value, weight)
print(fractional_knapsack(50, items))      # 240.0

print("\nDone! Tip: change values above and run again to learn by experiment.")

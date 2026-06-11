# ======================================================================
# 53 — Divide and Conquer  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Fast exponentiation in O(log n)
# ----------------------------------------------------------------------
print("\n--- Example 1: Fast exponentiation in O(log n) ---")
def power(base, exp):
    if exp == 0:                  # base case
        return 1
    half = power(base, exp // 2)  # conquer once, reuse
    if exp % 2 == 0:
        return half * half        # combine: x^n = (x^(n/2))^2
    else:
        return half * half * base

print(power(2, 10))   # 1024
print(power(3, 5))    # 243
# Only ~log2(exp) multiplications instead of exp-1.

# ----------------------------------------------------------------------
# Example 2: Maximum subarray via divide and conquer
# ----------------------------------------------------------------------
print("\n--- Example 2: Maximum subarray via divide and conquer ---")
def max_subarray(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo == hi:                  # base case: single element
        return arr[lo]
    mid = (lo + hi) // 2
    left = max_subarray(arr, lo, mid)        # best in left half
    right = max_subarray(arr, mid + 1, hi)   # best in right half

    # best crossing the midpoint
    left_sum = float("-inf"); total = 0
    for i in range(mid, lo - 1, -1):
        total += arr[i]; left_sum = max(left_sum, total)
    right_sum = float("-inf"); total = 0
    for i in range(mid + 1, hi + 1):
        total += arr[i]; right_sum = max(right_sum, total)
    cross = left_sum + right_sum

    return max(left, right, cross)

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6

# ----------------------------------------------------------------------
# Example 3: Count occurrences and find max with divide and conquer
# ----------------------------------------------------------------------
print("\n--- Example 3: Count occurrences and find max with divide and conquer ---")
def find_max(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo == hi:                  # one element
        return arr[lo]
    mid = (lo + hi) // 2
    return max(find_max(arr, lo, mid), find_max(arr, mid + 1, hi))

print(find_max([3, 7, 1, 9, 2, 8]))   # 9

# Karatsuba-style idea: multiply by splitting (shown simply here)
def sum_divide(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    return sum_divide(arr[:mid]) + sum_divide(arr[mid:])

print(sum_divide([1, 2, 3, 4, 5]))    # 15

print("\nDone! Tip: change values above and run again to learn by experiment.")

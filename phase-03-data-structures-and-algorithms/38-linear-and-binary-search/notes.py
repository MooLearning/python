# ======================================================================
# 38 — Linear and Binary Search  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Linear vs binary search
# ----------------------------------------------------------------------
print("\n--- Example 1: Linear vs binary search ---")
def linear_search(arr, target):       # O(n)
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1

def binary_search(arr, target):       # O(log n) — arr MUST be sorted
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1              # search right half
        else:
            hi = mid - 1              # search left half
    return -1

data = [1, 3, 5, 7, 9, 11, 13]
print(linear_search(data, 9))   # 4
print(binary_search(data, 9))   # 4
print(binary_search(data, 8))   # -1 (not found)

# ----------------------------------------------------------------------
# Example 2: Recursive binary search and step count
# ----------------------------------------------------------------------
print("\n--- Example 2: Recursive binary search and step count ---")
def binary_search_rec(arr, target, lo=0, hi=None, steps=0):
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1, steps
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid, steps + 1
    if arr[mid] < target:
        return binary_search_rec(arr, target, mid + 1, hi, steps + 1)
    return binary_search_rec(arr, target, lo, mid - 1, steps + 1)

big = list(range(0, 1_000_000, 2))   # 500k sorted evens
idx, steps = binary_search_rec(big, 999_998)
print(f"found at index {idx} in just {steps} steps")  # ~19 steps

# ----------------------------------------------------------------------
# Example 3: Using the bisect module
# ----------------------------------------------------------------------
print("\n--- Example 3: Using the bisect module ---")
import bisect

scores = [10, 20, 30, 40, 50]

# Where would 35 be inserted to keep order?
print(bisect.bisect_left(scores, 35))   # 3

# Insert while keeping the list sorted
bisect.insort(scores, 35)
print(scores)                           # [10, 20, 30, 35, 40, 50]

# Membership test in O(log n)
def contains(sorted_list, x):
    i = bisect.bisect_left(sorted_list, x)
    return i < len(sorted_list) and sorted_list[i] == x

print(contains(scores, 35))             # True
print(contains(scores, 36))             # False

print("\nDone! Tip: change values above and run again to learn by experiment.")

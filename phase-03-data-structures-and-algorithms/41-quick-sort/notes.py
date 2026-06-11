# ======================================================================
# 41 — Quick Sort  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Readable quick sort (extra-list partition)
# ----------------------------------------------------------------------
print("\n--- Example 1: Readable quick sort (extra-list partition) ---")
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]                  # middle element as pivot
    left = [x for x in arr if x < pivot]        # smaller
    mid = [x for x in arr if x == pivot]        # equal (handles dupes)
    right = [x for x in arr if x > pivot]       # larger
    return quick_sort(left) + mid + quick_sort(right)

print(quick_sort([3, 6, 1, 8, 2, 9, 4]))   # [1, 2, 3, 4, 6, 8, 9]
print(quick_sort([5, 5, 5, 1, 9]))         # [1, 5, 5, 5, 9]

# ----------------------------------------------------------------------
# Example 2: In-place Lomuto partition scheme
# ----------------------------------------------------------------------
print("\n--- Example 2: In-place Lomuto partition scheme ---")
def quick_sort_inplace(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        p = partition(arr, lo, hi)
        quick_sort_inplace(arr, lo, p - 1)      # sort left of pivot
        quick_sort_inplace(arr, p + 1, hi)      # sort right of pivot
    return arr

def partition(arr, lo, hi):
    pivot = arr[hi]                             # last element as pivot
    i = lo - 1                                  # boundary of smaller region
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]     # swap smaller item left
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]   # pivot into place
    return i + 1

print(quick_sort_inplace([9, 3, 7, 1, 8, 2]))   # [1, 2, 3, 7, 8, 9]

# ----------------------------------------------------------------------
# Example 3: Quickselect: k-th smallest without full sort
# ----------------------------------------------------------------------
print("\n--- Example 3: Quickselect: k-th smallest without full sort ---")
import random

def quickselect(arr, k):                # k is 1-based: k=1 -> smallest
    if not 1 <= k <= len(arr):
        raise ValueError("k out of range")
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    if k <= len(lows):
        return quickselect(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot                    # k falls in the pivot block
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

data = [7, 2, 9, 4, 1, 8, 3]
print("3rd smallest:", quickselect(data, 3))   # 3
print("1st smallest:", quickselect(data, 1))   # 1

print("\nDone! Tip: change values above and run again to learn by experiment.")

# ======================================================================
# 40 — Merge Sort  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Classic recursive merge sort
# ----------------------------------------------------------------------
print("\n--- Example 1: Classic recursive merge sort ---")
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:        # <= keeps it STABLE
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])            # leftovers (one side is empty)
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:                  # base case
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])       # sort each half
    right = merge_sort(arr[mid:])
    return merge(left, right)          # combine

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# [3, 9, 10, 27, 38, 43, 82]

# ----------------------------------------------------------------------
# Example 2: Watch the divide-and-conquer recursion
# ----------------------------------------------------------------------
print("\n--- Example 2: Watch the divide-and-conquer recursion ---")
def merge_sort_verbose(arr, depth=0):
    pad = "  " * depth
    print(f"{pad}split {arr}")
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_verbose(arr[:mid], depth + 1)
    right = merge_sort_verbose(arr[mid:], depth + 1)
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: merged.append(left[i]); i += 1
        else: merged.append(right[j]); j += 1
    merged += left[i:] + right[j:]
    print(f"{pad}merge -> {merged}")
    return merged

merge_sort_verbose([5, 2, 4, 1])

# ----------------------------------------------------------------------
# Example 3: Merging k sorted lists with heapq
# ----------------------------------------------------------------------
print("\n--- Example 3: Merging k sorted lists with heapq ---")
import heapq

def merge_k(lists):
    return list(heapq.merge(*lists))   # heapq.merge merges sorted iterables

a = [1, 4, 7]
b = [2, 5, 8]
c = [3, 6, 9]
print(merge_k([a, b, c]))   # [1,2,3,4,5,6,7,8,9]

# Counting inversions as a side effect of merging
def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, l_inv = count_inversions(arr[:mid])
    right, r_inv = count_inversions(arr[mid:])
    merged, split = [], 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
            split += len(left) - i      # all remaining left items are inversions
    merged += left[i:] + right[j:]
    return merged, l_inv + r_inv + split

_, inv = count_inversions([2, 4, 1, 3, 5])
print("inversions:", inv)   # 3

print("\nDone! Tip: change values above and run again to learn by experiment.")

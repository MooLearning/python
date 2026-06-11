# ======================================================================
# 42 — Heap, Counting and Radix Sort  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Heap sort using heapq
# ----------------------------------------------------------------------
print("\n--- Example 1: Heap sort using heapq ---")
import heapq

def heap_sort(arr):
    h = arr[:]            # copy
    heapq.heapify(h)      # O(n) build a min-heap
    return [heapq.heappop(h) for _ in range(len(h))]   # pop smallest n times

print(heap_sort([5, 3, 8, 1, 9, 2]))   # [1, 2, 3, 5, 8, 9]

# Manual sift-down heap sort (in place, max-heap)
def heapify(a, n, i):
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and a[l] > a[largest]: largest = l
    if r < n and a[r] > a[largest]: largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

def heap_sort_inplace(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):     # build max-heap
        heapify(a, n, i)
    for end in range(n - 1, 0, -1):         # pop max to the end
        a[0], a[end] = a[end], a[0]
        heapify(a, end, 0)
    return a

print(heap_sort_inplace([4, 10, 3, 5, 1]))   # [1, 3, 4, 5, 10]

# ----------------------------------------------------------------------
# Example 2: Counting sort for small-range integers
# ----------------------------------------------------------------------
print("\n--- Example 2: Counting sort for small-range integers ---")
def counting_sort(arr):
    if not arr:
        return arr
    lo, hi = min(arr), max(arr)
    counts = [0] * (hi - lo + 1)
    for x in arr:
        counts[x - lo] += 1          # tally each value
    out = []
    for i, c in enumerate(counts):
        out.extend([i + lo] * c)     # rebuild in order
    return out

print(counting_sort([4, 2, 2, 8, 3, 3, 1]))   # [1, 2, 2, 3, 3, 4, 8]
print(counting_sort([0, -3, -1, 2, -3]))      # handles negatives via offset

# ----------------------------------------------------------------------
# Example 3: LSD radix sort for non-negative integers
# ----------------------------------------------------------------------
print("\n--- Example 3: LSD radix sort for non-negative integers ---")
def counting_sort_by_digit(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10
    for x in arr:
        count[(x // exp) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]            # prefix sums -> positions
    for x in reversed(arr):                 # reversed keeps it STABLE
        d = (x // exp) % 10
        count[d] -= 1
        output[count[d]] = x
    return output

def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:                # one pass per digit
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr

print(radix_sort([170, 45, 75, 90, 2, 802, 24, 66]))
# [2, 24, 45, 66, 75, 90, 170, 802]

print("\nDone! Tip: change values above and run again to learn by experiment.")

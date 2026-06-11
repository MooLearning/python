# ======================================================================
# 39 — Basic Sorts (Bubble, Selection, Insertion)  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Bubble sort with early-exit optimization
# ----------------------------------------------------------------------
print("\n--- Example 1: Bubble sort with early-exit optimization ---")
def bubble_sort(arr):
    a = arr[:]                       # copy so we don't mutate the input
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):   # last i items already in place
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:              # no swaps -> already sorted
            break
    return a

print(bubble_sort([5, 2, 9, 1, 5, 6]))   # [1, 2, 5, 5, 6, 9]
print(bubble_sort([1, 2, 3]))            # one pass, then exits

# ----------------------------------------------------------------------
# Example 2: Selection sort
# ----------------------------------------------------------------------
print("\n--- Example 2: Selection sort ---")
def selection_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):    # find smallest in the rest
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]   # swap it into place
    return a

print(selection_sort([64, 25, 12, 22, 11]))   # [11, 12, 22, 25, 64]

# ----------------------------------------------------------------------
# Example 3: Insertion sort (fast on nearly-sorted data)
# ----------------------------------------------------------------------
print("\n--- Example 3: Insertion sort (fast on nearly-sorted data) ---")
def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:  # shift bigger items right
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key                # drop key into the gap
    return a

print(insertion_sort([12, 11, 13, 5, 6]))   # [5, 6, 11, 12, 13]
print(insertion_sort([1, 2, 3, 5, 4]))      # nearly sorted -> few shifts

print("\nDone! Tip: change values above and run again to learn by experiment.")

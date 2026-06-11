# 42 — Heap, Counting and Radix Sort

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

Beyond comparison sorts there are **heap sort** (build a heap, repeatedly extract the min/max — O(n log n), in place) and the **non-comparison** sorts: **counting sort** tallies how many of each value exist (O(n + k) for values in range k), and **radix sort** sorts numbers digit by digit using counting sort as a subroutine (O(d·(n + b))).

## Why it matters

Counting and radix sort beat the O(n log n) comparison lower bound when keys are small integers or fixed-width — crucial for sorting huge integer/string datasets. Heap sort gives guaranteed O(n log n) with O(1) extra space.

## Key concepts

- **Heap sort** — heapify then pop the root n times — O(n log n), in place.
- **Counting sort** — Count occurrences, then rebuild — O(n + k), stable if done right.
- **Radix sort** — Sort by each digit (LSD→MSD) using a stable counting sort.
- **Non-comparison** — These don't compare pairs, so they dodge the n log n bound.
- **Range matters** — Counting sort is great when k (value range) is small, bad when huge.
- **Stability** — Radix sort REQUIRES a stable inner sort to work correctly.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Counting sort needs a small value range k — for huge ranges its O(k) memory explodes.
- ⚠️ Radix sort's inner counting sort MUST be stable, or digits clobber each other.
- ⚠️ Plain counting/radix sort assumes non-negative integers; negatives need an offset or split.
- ⚠️ `heapq` is a MIN-heap; for a max-heap push negated values or use `_heapify_max` tricks.
- ⚠️ Heap sort is not stable; counting/radix can be stable if you build output carefully.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


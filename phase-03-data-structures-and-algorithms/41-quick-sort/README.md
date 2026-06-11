# 41 — Quick Sort

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Quick sort** is a divide-and-conquer sort that picks a **pivot**, **partitions** the list so smaller items go left and larger go right, then recursively sorts each side. Average time is **O(n log n)** and it sorts **in place** (O(log n) stack), which makes it very fast in practice. Worst case is O(n^2) (bad pivots), mitigated by random or median pivots.

## Why it matters

It's one of the most-used sorts in the real world and the key example of partitioning — a technique that also solves quickselect (finding the k-th smallest in O(n) average). Understanding pivots and partitioning is interview gold.

## Key concepts

- **Pivot** — The element you partition around (first, last, random, or median).
- **Partition** — Rearrange so left < pivot ≤ right; returns the pivot's final index.
- **In place** — Sorts within the array — O(log n) stack, O(1) extra data.
- **Average O(n log n)** — Balanced partitions give log n levels of O(n) work.
- **Worst O(n^2)** — Already-sorted data with a naive pivot makes lopsided splits.
- **Quickselect** — Partition-only search for the k-th smallest — O(n) average.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Naive pivot (first/last) on sorted data gives O(n^2) — use a random or median-of-three pivot.
- ⚠️ Forgetting the `== pivot` group makes duplicates loop or vanish; handle equals explicitly.
- ⚠️ The in-place version mutates the input list; copy first if you must keep the original.
- ⚠️ Off-by-one in partition indices is the classic bug — return the pivot's final index carefully.
- ⚠️ Deep recursion on adversarial input can hit Python's recursion limit; recurse the smaller side first.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


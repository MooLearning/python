# 40 — Merge Sort

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Merge sort** is a **divide-and-conquer** algorithm: split the list in half, recursively sort each half, then **merge** the two sorted halves into one. It runs in **O(n log n)** in all cases and is **stable**, but uses O(n) extra space. The clever part is the linear-time merge of two already-sorted lists with two pointers.

## Why it matters

It's the textbook introduction to divide-and-conquer and to provably O(n log n) sorting. Its merge step reappears in external sorting, merging k sorted streams, and counting inversions.

## Key concepts

- **Divide** — Split the array into two halves at the midpoint.
- **Conquer** — Recursively sort each half (base case: length ≤ 1).
- **Merge** — Combine two sorted halves in O(n) using two pointers.
- **O(n log n)** — log n levels of splitting × O(n) work to merge per level.
- **Stable** — Equal elements keep their original relative order.
- **Extra space** — Needs O(n) scratch space for the merge (not in-place).

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Use `<=` (not `<`) in the merge to keep the sort STABLE.
- ⚠️ Merge sort is NOT in-place — it needs O(n) extra memory.
- ⚠️ Forgetting to append the leftovers (`left[i:]`, `right[j:]`) drops elements.
- ⚠️ The base case is `len(arr) <= 1`; without it the recursion never stops.
- ⚠️ Slicing (`arr[:mid]`) copies — fine for learning, but adds overhead vs index-based merge.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


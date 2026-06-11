# 38 — Linear and Binary Search

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Searching** finds where (or whether) a value exists in a collection. **Linear search** scans every element — O(n) — and works on any list. **Binary search** repeatedly halves a **sorted** list by comparing with the middle — O(log n) — turning a million-item search into ~20 steps. Python's `bisect` module gives binary search out of the box.

## Why it matters

Binary search is the canonical O(log n) algorithm and the gateway to 'search the answer space' techniques used across DSA. Knowing when data is sorted (so you can binary-search) is a major efficiency win.

## Key concepts

- **Linear search** — Check each element in turn — O(n), no ordering needed.
- **Binary search** — Halve a SORTED range each step — O(log n).
- **lo/mid/hi** — Track the search window; `mid = (lo + hi) // 2`.
- **Sorted precondition** — Binary search is wrong on unsorted data.
- **bisect module** — `bisect_left`/`insort` for fast search & ordered insert.
- **Search the answer** — Binary-search over a value range, not just an array.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Binary search REQUIRES a sorted list — on unsorted data it returns wrong answers.
- ⚠️ `mid = (lo + hi) // 2` then move to `mid + 1` / `mid - 1`, or you can loop forever.
- ⚠️ Sorting first costs O(n log n); for a single search, linear O(n) may be cheaper.
- ⚠️ Off-by-one bugs are common — decide `<=` vs `<` for the `while` condition and stick to it.
- ⚠️ `list.index(x)` is linear O(n); for sorted data use `bisect` for O(log n).

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


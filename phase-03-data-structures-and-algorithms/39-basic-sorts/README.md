# 39 — Basic Sorts (Bubble, Selection, Insertion)

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

The three **basic sorts** are simple O(n^2) algorithms great for learning: **bubble sort** repeatedly swaps adjacent out-of-order pairs; **selection sort** repeatedly finds the smallest remaining item and places it; **insertion sort** grows a sorted prefix by inserting each new item into place. Insertion sort is genuinely fast on small or nearly-sorted data.

## Why it matters

They build core intuition about comparisons, swaps, in-place work, and stability — the vocabulary you'll reuse for the fast O(n log n) sorts. Insertion sort also powers the small-array base case inside real-world hybrid sorts like Timsort.

## Key concepts

- **Bubble sort** — Swap adjacent pairs; biggest 'bubbles' to the end each pass.
- **Selection sort** — Select the min of the unsorted part; swap it to the front.
- **Insertion sort** — Insert each element into the growing sorted prefix.
- **In-place** — All three sort the list without extra arrays — O(1) space.
- **Stability** — Bubble & insertion are stable; selection sort is not.
- **Best case** — Insertion sort is O(n) on already-sorted input (early exit).

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ All three are O(n^2) — fine for learning or tiny lists, too slow for large data.
- ⚠️ Selection sort is NOT stable: equal keys can be reordered.
- ⚠️ For real code just use `sorted()` / `list.sort()` (Timsort, O(n log n) and stable).
- ⚠️ Forgetting the early-exit flag makes bubble sort do useless passes on sorted input.
- ⚠️ Off-by-one in the inner range (`n-1-i`) either skips the last pair or indexes out of range.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


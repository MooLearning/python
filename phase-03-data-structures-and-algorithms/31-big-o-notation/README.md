# 31 — Big-O Notation

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Big-O notation** describes how an algorithm's running time (or memory) grows as the input size `n` grows. It ignores constants and small terms to capture the *shape* of growth: O(1) constant, O(log n) logarithmic, O(n) linear, O(n log n), O(n^2) quadratic, O(2^n) exponential. You compare algorithms by their worst-case Big-O.

## Why it matters

It's the universal language for 'will this scale?'. An O(n^2) solution that's fine for 100 items can freeze on 100,000. Every DSA topic and every coding interview leans on reasoning about Big-O.

## Key concepts

- **O(1)** — Constant — same work regardless of n (e.g. dict lookup, list index).
- **O(log n)** — Halves the problem each step (binary search).
- **O(n)** — Touches each item once (a single loop, linear search).
- **O(n log n)** — Efficient sorts (merge sort, Timsort).
- **O(n^2)** — Nested loops over the data (bubble sort, all pairs).
- **Drop constants/lower terms** — O(2n + 5) is O(n); O(n^2 + n) is O(n^2).

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
def constant(n):          # O(1): work doesn't depend on n
    return n * 2

def linear(arr):          # O(n): one pass
    ops = 0
    for _ in arr:
        ops += 1
    return ops

def quadratic(arr):       # O(n^2): nested loops -> all pairs
    ops = 0
    for _ in arr:
        for _ in arr:
            ops += 1
    return ops

for n in (10, 100, 1000):
    data = list(range(n))
    print(f"n={n:5} | linear ops={linear(data):6} | quadratic ops={quadratic(data)}")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Big-O is about GROWTH, not absolute speed: an O(n) with huge constants can lose to O(n^2) on small n.
- ⚠️ Worst case vs average case differ — quicksort is O(n log n) average but O(n^2) worst case.
- ⚠️ Nested loops aren't always O(n^2): if the inner loop runs a fixed number of times, it's O(n).
- ⚠️ Watch hidden costs: `x in a_list` is O(n), but `x in a_set` is O(1).
- ⚠️ Space complexity matters too — a recursive solution may be O(n) time but O(n) stack space.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


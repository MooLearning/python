# 46 — Heaps

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **heap** is a complete binary tree stored in an array that keeps the smallest (min-heap) or largest (max-heap) element at the root. It gives **O(1)** peek at the extreme, **O(log n)** push and pop, and **O(n)** to build from a list. Python's `heapq` module implements a min-heap on a plain list — the backbone of **priority queues**.

## Why it matters

Heaps power priority queues: schedulers, Dijkstra's shortest path, A* search, event simulation, and 'top-k / k-th largest' problems. When you need the best item repeatedly without fully sorting, reach for a heap.

## Key concepts

- **Heap property** — Every parent ≤ (min-heap) or ≥ (max-heap) its children.
- **Array layout** — children of i are 2i+1 and 2i+2; parent is (i-1)//2.
- **push / pop** — O(log n): sift-up on insert, sift-down on removal.
- **peek** — O(1) — the root is `heap[0]`.
- **heapify** — Turn a list into a heap in O(n).
- **Priority queue** — Pop items in priority order; store (priority, item) tuples.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import heapq

h = []
for x in [5, 3, 8, 1, 9, 2]:
    heapq.heappush(h, x)         # O(log n) each
print("min (peek):", h[0])       # 1  -> root is always the smallest
print("pop:", heapq.heappop(h))  # 1
print("pop:", heapq.heappop(h))  # 2

# Build a heap from a list in O(n)
data = [9, 4, 7, 1, 2, 6]
heapq.heapify(data)
print("heapified:", data)        # [1, 2, 6, 9, 4, 7] (heap order)
print("3 smallest:", heapq.nsmallest(3, [9, 4, 7, 1, 2, 6]))   # [1, 2, 4]
print("3 largest :", heapq.nlargest(3, [9, 4, 7, 1, 2, 6]))    # [9, 7, 6]
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ `heapq` is a MIN-heap only; negate values (or wrap) for max-heap behavior.
- ⚠️ `heap[0]` peeks the min, but the rest of the list is NOT sorted — don't read it as sorted.
- ⚠️ Pushing non-comparable items (e.g. dicts) errors on ties; use a (priority, counter, item) tuple.
- ⚠️ Mutating the underlying list directly breaks the heap invariant — only use heapq functions.
- ⚠️ `sorted(heap)` is O(n log n); if you only need the top-k, use nlargest/nsmallest or a size-k heap.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


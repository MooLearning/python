# 36 — Queues

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **queue** is a **FIFO** (First-In, First-Out) collection: you add at the **rear** (`enqueue`) and remove from the **front** (`dequeue`) — like a line at a checkout. Use `collections.deque`, which supports O(1) `append` and `popleft`. A plain list's `pop(0)` is O(n), so avoid it. Variants: **circular queue**, **priority queue** (heap), **deque** (double-ended).

## Why it matters

Queues model fair, in-order processing: task schedulers, print spoolers, breadth-first search, and producer/consumer pipelines. BFS — one of the most important graph algorithms — is just a queue.

## Key concepts

- **enqueue** — Add to the rear — `deque.append(x)` (O(1)).
- **dequeue** — Remove from the front — `deque.popleft()` (O(1)).
- **FIFO order** — First item added is the first removed.
- **deque** — Double-ended queue: O(1) at BOTH ends; the right tool in Python.
- **Why not list.pop(0)** — Removing the front of a list shifts everything — O(n).
- **Priority queue** — Removes the smallest/largest first — use `heapq`, not plain FIFO.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
from collections import deque

q = deque()
q.append("a")          # enqueue at rear
q.append("b")
q.append("c")
print("front:", q[0])  # a
print("dequeue:", q.popleft())   # a  (O(1))
print("dequeue:", q.popleft())   # b
print("remaining:", list(q))     # ['c']
print("size:", len(q))           # 1
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Don't use `list.pop(0)` for a queue — it's O(n). Use `collections.deque.popleft()`.
- ⚠️ `deque[i]` indexing in the middle is O(n); deques are optimized for the ends.
- ⚠️ A queue is FIFO; a stack is LIFO — picking the wrong one reverses your order.
- ⚠️ `popleft()`/`pop()` on an empty deque raises IndexError — check `if q:` first.
- ⚠️ A priority queue is NOT a plain FIFO — use `heapq` when order depends on priority.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


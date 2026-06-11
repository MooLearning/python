# 32 — Arrays and Dynamic Arrays

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

An **array** stores items in contiguous memory so any element is reachable by index in O(1). Python's built-in `list` is a **dynamic array**: it grows automatically and supports indexing, slicing, append/pop at the end (O(1) amortized), and insert/remove in the middle (O(n)). 2D arrays are lists of lists.

## Why it matters

Arrays are the most fundamental data structure — the basis for strings, matrices, stacks, heaps, and almost every algorithm. Mastering indexing, slicing, and common patterns (prefix sums, two-pointer, rotation) unlocks the rest of DSA.

## Key concepts

- **Index access** — `a[i]` is O(1); the position is computed directly from memory.
- **Append/pop end** — O(1) amortized at the end; insert/remove elsewhere is O(n) (shifts).
- **Slicing** — `a[i:j]` copies a sub-array — handy but O(k) in time and space.
- **2D arrays** — Lists of lists; build with comprehensions, not `[[0]*n]*m` (shared rows!).
- **Prefix sums** — Precompute running totals to answer range-sum queries in O(1).
- **In-place vs copy** — Operations like reverse() mutate; sorted()/[::-1] make copies.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
a = [10, 20, 30, 40]
print(a[0], a[-1])         # 10 40  -> O(1) index
a.append(50)               # O(1) amortized at the end
a.insert(1, 15)            # O(n): shifts everything right -> [10,15,20,30,40,50]
print(a)
a.pop()                    # O(1): remove last
a.pop(0)                   # O(n): remove first, shifts left
print(a)                   # [15, 20, 30, 40]
print(a[1:3])              # [20, 30] -> slice copy
print(20 in a)             # O(n) membership scan -> True
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ `[[0]*n]*m` creates m references to the SAME row — use `[[0]*n for _ in range(m)]`.
- ⚠️ `list.insert(0, x)` and `list.pop(0)` are O(n); use `collections.deque` for fast ends.
- ⚠️ `x in a_list` is O(n); if you do many membership checks, use a set.
- ⚠️ Slicing copies data — `a[:]` is a shallow copy, not a view (unlike NumPy).
- ⚠️ Modifying a list while iterating over it skips elements; iterate a copy or build a new list.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


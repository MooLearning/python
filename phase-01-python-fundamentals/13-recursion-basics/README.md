# 13 — Recursion Basics

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Recursion** is when a function calls itself to solve a smaller version of the same problem. Every recursive function needs a **base case** (when to stop) and a **recursive case** (call itself on something smaller, moving toward the base case). Classic examples: factorial, Fibonacci, and summing a list.

## Why it matters

Recursion is the natural way to express problems with self-similar structure: trees, graphs, divide-and-conquer sorting, and backtracking. It's a core mental model you'll use heavily in DSA (Phase 3).

## Key concepts

- **Base case** — The simplest input where the answer is known directly — stops the recursion.
- **Recursive case** — Solve a smaller subproblem and combine: `n * factorial(n-1)`.
- **Call stack** — Each call waits for its sub-call; too deep -> RecursionError.
- **Progress toward base** — Each call MUST get closer to the base case or it loops forever.
- **Recursion vs iteration** — Anything recursive can be written as a loop; pick the clearer one.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
def factorial(n):
    if n <= 1:               # base case: 0! and 1! are 1
        return 1
    return n * factorial(n - 1)   # recursive case: shrink toward the base

print(factorial(5))   # 120  (5*4*3*2*1)

# Trace: factorial(3) = 3*factorial(2) = 3*2*factorial(1) = 3*2*1 = 6
print(factorial(3))   # 6
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Forgetting the base case (or never reaching it) causes infinite recursion -> RecursionError.
- ⚠️ Python's default recursion limit is ~1000; very deep recursion crashes. Use iteration for huge depths.
- ⚠️ Naive recursive Fibonacci is exponential — add memoization (`@lru_cache`) or use a loop.
- ⚠️ Slicing (`items[1:]`) copies the list each call — fine for learning, costly for big inputs.
- ⚠️ Each recursive call uses stack memory; recursion isn't free even when correct.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


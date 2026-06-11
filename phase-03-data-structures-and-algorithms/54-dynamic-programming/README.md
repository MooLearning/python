# 54 — Dynamic Programming

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Dynamic programming (DP)** solves problems with **overlapping subproblems** and **optimal substructure** by solving each subproblem **once** and storing the result. Two styles: **top-down memoization** (recursion + a cache) and **bottom-up tabulation** (fill a table iteratively). DP turns exponential brute force into polynomial time — e.g. naive Fibonacci O(2ⁿ) becomes O(n).

## Why it matters

DP is the heavyweight technique for optimization and counting problems: knapsack, edit distance, longest common subsequence, coin change, path counting. It's notoriously common in interviews and powers real systems (diff tools, spell-checkers, bioinformatics).

## Key concepts

- **Overlapping subproblems** — The same sub-answer is needed many times.
- **Optimal substructure** — Optimal answer builds from optimal sub-answers.
- **Memoization** — Top-down recursion that caches results (`@lru_cache`).
- **Tabulation** — Bottom-up: fill a DP table from base cases upward.
- **State & transition** — Define what dp[i] means and how it builds from earlier states.
- **Space optimization** — Often only the last row/few values are needed.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
from functools import lru_cache

# Memoized (top-down) — O(n)
@lru_cache(maxsize=None)
def fib_memo(n):
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

# Tabulated (bottom-up) — O(n) time, O(1) space
def fib_tab(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print([fib_memo(i) for i in range(10)])   # 0..34
print("fib(50) =", fib_tab(50))           # 12586269025
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ DP needs BOTH overlapping subproblems and optimal substructure — otherwise use greedy/D&C.
- ⚠️ Define your state precisely (what dp[i] MEANS) before writing the transition.
- ⚠️ Initialize base cases correctly — a wrong dp[0] poisons the whole table.
- ⚠️ Watch index off-by-ones: dp tables are often sized n+1 with a 1-based shift.
- ⚠️ Memoize on hashable args; `@lru_cache` won't work if you pass lists/dicts as arguments.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


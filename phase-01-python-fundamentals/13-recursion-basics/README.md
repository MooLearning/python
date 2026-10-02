# 13 — Recursion Basics

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

⏱️ ~30 min · Loop: `README → notes.py → practice.md` · Prereq: [12 — Scope (local, global, nonlocal)](../12-scope/)

## What is it?

**Recursion** is when a function solves a problem by calling itself on a
smaller version of the same problem. Every recursive function has two parts: a
**base case** that answers the tiniest input directly (and stops the chain),
and a **recursive case** that shrinks the input, calls itself, and combines
the result. Factorial (`n! = n * (n-1)!`), list sums, and Fibonacci are the
classic first specimens.

Picture a set of Russian nesting dolls. Each doll contains a smaller copy of
herself, until the last solid doll that holds nothing — that solid one is the
base case. Opening the set means lifting each shell and asking "what's inside";
closing it means stacking the answers back up, biggest last. Recursion opens
calls the same way and combines results on the way back out. Forget the solid
doll and you open forever — Python eventually stops you with `RecursionError`.

## Why it matters

- **Self-similar problems:** directory trees, JSON nesting, and linked
  structures are naturally "a smaller version of the same thing."
- **Algorithm vocabulary:** divide-and-conquer sorts, tree/graph traversals,
  and backtracking searches are all taught recursively first.
- **Elegant counting:** countdowns, powers, digit counts, and string reversals
  read beautifully as base + shrink + combine.
- **AI-career hook:** decision trees, search, and dynamic-programming
  recurrences (plus memoised Fibonacci with `@lru_cache`) preview Phase 3 DSA.

## How it works

Mental model — three promises every recursive function must keep:

1. **Base case:** `if n <= 1: return 1` — answer directly, no self-call.
2. **Shrink:** each call moves closer to the base (`n - 1`, `items[1:]`, `s[1:]`).
3. **Combine:** use the sub-answer to build yours (`n * factorial(n - 1)`).
4. **Unwind:** calls resolve inside-out as the stack collapses.

```text
factorial(3) ──► 3 * factorial(2) ──► 3 * 2 * factorial(1) ──► 3*2*1 = 6
   (waiting)         (waiting)             (base: return 1)      (unwind)
```

Each waiting call occupies a stack frame. Too many frames (default limit
~1000) means the base was missed or the input was simply too deep — reach for
a loop or memoization instead.

## Key concepts

- **Base case** — `if n <= 1: return 1` stops `factorial`; every path must reach one.
- **Recursive case** — `return n * factorial(n - 1)` shrinks and combines.
- **Call stack** — callers wait while sub-calls run; depth costs memory.
- **Empty-input base** — `if not items: return 0` anchors `sum_list`.
- **String shrink** — `reverse(s[1:]) + s[0]` moves the head to the tail.
- **Double recursion** — `fib(n - 1) + fib(n - 2)` branches twice per call.
- **Exponential blowup** — naive `fib` recomputes values; `fib(35)` already crawls.
- **Memoization fix** — `@lru_cache(maxsize=None)` on `fib_fast` makes `fib_fast(50)` instant.
- **Recursion vs loop** — `sum_list` as a `for` loop is plainer and stack-free for huge inputs.

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

The `if` is the solid doll: `factorial(1)` returns without calling again.
Larger inputs peel one layer (`n - 1`) and multiply on the way back, so
`factorial(5)` unwinds as `5*4*3*2*1`. More dolls await in `notes.py`:
Example 2 ("Sum a list and reverse a string recursively") shrinks slices,
and Example 3 ("Fibonacci, and why naive recursion can be slow") contrasts
plain `fib` with a cached `fib_fast` that reaches `fib_fast(50)` instantly.

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

Two-minute prediction (think before running): `sum_list([1, 2, 3])` expands to
`1 + sum_list([2, 3])` — write out the next two expansions down to the empty
list, then unwind the additions by hand. What single changed line would make it
multiply instead of add, and what would your trace give for `[2, 3, 4]`?

## Common mistakes & gotchas

- ⚠️ Forgetting the base case (or never reaching it) causes infinite recursion -> RecursionError.
- ⚠️ Python's default recursion limit is ~1000; very deep recursion crashes. Use iteration for huge depths.
- ⚠️ Naive recursive Fibonacci is exponential — add memoization (`@lru_cache`) or use a loop.
- ⚠️ Slicing (`items[1:]`) copies the list each call — fine for learning, costly for big inputs.
- ⚠️ Each recursive call uses stack memory; recursion isn't free even when correct.

## Cheat sheet

```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
def sum_list(xs):
    return 0 if not xs else xs[0] + sum_list(xs[1:])
def reverse(s):
    return s if len(s) <= 1 else reverse(s[1:]) + s[0]
from functools import lru_cache
@lru_cache(maxsize=None)
def fib_fast(n):
    return n if n < 2 else fib_fast(n - 1) + fib_fast(n - 2)
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

## What's next

Recursion handled — now make code bulletproof in [`14 — Exception Handling`](../14-exception-handling/).

# 53 — Divide and Conquer

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Divide and conquer** solves a problem by (1) **dividing** it into smaller subproblems of the same type, (2) **conquering** them recursively, and (3) **combining** their answers. Merge sort, quick sort, binary search, fast exponentiation, and Karatsuba multiplication all follow this template. The cost is captured by a **recurrence** like T(n) = 2T(n/2) + O(n).

## Why it matters

It's a fundamental design paradigm that yields elegant O(n log n) and O(log n) algorithms, and it parallelizes naturally. Recognizing a problem as 'split, solve halves, merge' is a powerful, reusable mental model.

## Key concepts

- **Divide** — Break the input into smaller subproblems (often halves).
- **Conquer** — Solve each subproblem recursively (base case stops it).
- **Combine** — Merge sub-answers into the full answer.
- **Recurrence** — T(n) = a·T(n/b) + f(n) describes the running time.
- **Master theorem** — A formula to solve common divide-and-conquer recurrences.
- **Examples** — Merge/quick sort, binary search, power, maximum subarray.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
def power(base, exp):
    if exp == 0:                  # base case
        return 1
    half = power(base, exp // 2)  # conquer once, reuse
    if exp % 2 == 0:
        return half * half        # combine: x^n = (x^(n/2))^2
    else:
        return half * half * base

print(power(2, 10))   # 1024
print(power(3, 5))    # 243
# Only ~log2(exp) multiplications instead of exp-1.
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Always define a base case (smallest subproblem) or recursion never terminates.
- ⚠️ The 'combine' step often dominates the cost — analyze it to get the recurrence right.
- ⚠️ Slicing (`arr[:mid]`) copies data; pass lo/hi indices to avoid O(n) copies per call.
- ⚠️ Not every split is balanced — lopsided division can degrade O(n log n) to O(n²).
- ⚠️ Deep recursion risks stack overflow; consider iterative versions for very large n.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


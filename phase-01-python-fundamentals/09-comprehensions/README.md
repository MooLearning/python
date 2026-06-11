# 09 — Comprehensions

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **comprehension** builds a list, set, or dict in a single readable line by describing *what you want* rather than writing a manual loop. List form: `[expr for item in iterable if condition]`. There are set `{...}` and dict `{k: v for ...}` versions too.

## Why it matters

Comprehensions are concise, fast, and extremely common in real Python and data work. Reading and writing them fluently makes your code shorter and clearer than equivalent loops.

## Key concepts

- **List comprehension** — `[x*x for x in range(5)]` -> [0,1,4,9,16].
- **Filtering** — Add `if`: `[x for x in nums if x > 0]`.
- **Transform + filter** — `[f(x) for x in data if cond(x)]` in one line.
- **Dict comprehension** — `{k: v for k, v in pairs}` builds a dict.
- **Set comprehension** — `{x % 3 for x in nums}` builds a set of unique results.
- **Nested / conditional expr** — `[a if a>0 else 0 for a in xs]` puts the if/else BEFORE for.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
# The loop way
squares = []
for x in range(6):
    squares.append(x * x)
print(squares)            # [0, 1, 4, 9, 16, 25]

# The comprehension way (same result, one line)
squares = [x * x for x in range(6)]
print(squares)

# With a filter: keep only evens, then square them
evens_sq = [x * x for x in range(10) if x % 2 == 0]
print(evens_sq)           # [0, 4, 16, 36, 64]
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ The filtering `if` goes at the END; the `if/else` *expression* goes at the FRONT (before `for`).
- ⚠️ Deeply nested comprehensions become unreadable — if it needs comments, use a real loop.
- ⚠️ `{}` alone is an empty DICT, not an empty set. Use `set()` for an empty set.
- ⚠️ A comprehension creates a brand-new list each time; it doesn't modify the source iterable.
- ⚠️ Don't call expensive functions twice; comprehensions evaluate the expression for every item.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


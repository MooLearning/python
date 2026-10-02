# 11 — Lambda, Map, Filter and Reduce

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

⏱️ ~25 min · Loop: `README → notes.py → practice.md` · Prereq: [10 — Functions](../10-functions/)

## What is it?

A **lambda** is a tiny anonymous function written inline: `lambda x: x * 2`.
It exists to be handed to something else. Its three classic partners are
**map** (apply a function to every item), **filter** (keep only items passing
a test), and **reduce** (fold everything into a single value, imported from
`functools`). Together they express the "functional" style: data flows through
small transformations instead of explicit loops.

Imagine a sushi conveyor belt with three stations. At the first, a stamper
(`map`) presses every plate into a new shape. Next, a bouncer (`filter`) lifts
off plates that fail the taste test. Finally, a compactor (`reduce`) squashes
everything left into one takeaway box. A `lambda` is the sticky note on each
station saying what to do — used once, thrown away, never given a formal job
title like `def` would.

## Why it matters

- **Sorting smarts:** `sorted(people, key=lambda p: p[1])` and `max(rows,
  key=len)` rank by computed values without writing helper functions.
- **Compact pipelines:** `map`/`filter` transform API responses, filenames, or
  readings in one pass when a full comprehension feels heavy-handed.
- **Aggregation:** `reduce` folds lists into products, totals with a start
  value, or "best so far" picks like the longest string.
- **AI-career hook:** preprocessing chains (tokenise → filter empties → embed)
  and `key=` sorting of model candidates mirror these functional pipelines.

## How it works

Mental model — pick the station that matches your goal:

1. **One-line function:** `lambda args: expression` builds a function with no
   name and no statements — just a value to compute.
2. **map:** `map(func, items)` applies `func` to EACH item, lazily.
3. **filter:** `filter(test, items)` keeps only items where `test` is truthy.
4. **reduce:** `reduce(combine, items, start?)` folds left to right:
   `(((start ⊕ a) ⊕ b) ⊕ c)`.

```text
items ──► [ map:    transform each ] ──► [ filter: keep if True ] ──► list(...)
items ──► [ reduce: acc + next, repeat ] ──► single value
```

`map` and `filter` return lazy iterators in Python 3 — wrap them in `list()`
to see results. When the pipeline gets hard to read, a comprehension is the
better tool for the same job.

## Key concepts

- **Lambda shape** — `double = lambda x: x * 2`; call it via `double(5)` → `10`.
- **Single expression only** — `lambda x: x * 2` is fine; loops or `=` inside are not.
- **`map` is lazy** — `list(map(lambda x: x * x, nums))` realises `[1, 4, 9, ...]`.
- **`filter` keeps truthy** — `list(filter(lambda x: x % 2 == 0, nums))` keeps evens.
- **`reduce` folds** — `reduce(lambda acc, x: acc * x, [1, 2, 3, 4])` gives `24`.
- **Start value** — `reduce(lambda a, x: a + x, nums, 0)` seeds the accumulator.
- **`key=` callbacks** — `sorted(words, key=len)` orders shortest → longest.
- **Lambda as key** — `sorted(people, key=lambda p: p[1])` sorts tuples by age.
- **Comprehension rival** — `[x * x for x in nums if x % 2 == 0]` often reads clearer.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
double = lambda x: x * 2          # same as: def double(x): return x*2
print(double(5))                  # 10

# Real-world use: sort by a computed key
people = [("Ada", 36), ("Bo", 19), ("Cy", 54)]
by_age = sorted(people, key=lambda person: person[1])
print(by_age)                     # sorted by the age (2nd item)

words = ["banana", "kiwi", "apple"]
print(sorted(words, key=len))     # shortest to longest
```

The sticky-note function `double` works immediately, but the real payoff is
`key=`: instead of sorting names alphabetically, the lambda tells `sorted` to
compare the age field, and `len` ranks words by length. Next in `notes.py`:
Example 2 ("map and filter") squares numbers, keeps evens, and shows the
comprehension equivalent, while Example 3 ("reduce for folding values")
multiplies a list, seeds a sum, and picks the longest word.

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

Two-minute prediction (no running yet): what does
`list(map(lambda w: w[::-1], ["ab", "cde"]))` produce, and what would
`list(filter(lambda w: len(w) > 2, ["ab", "cde", "f"]))` keep? Now combine them
in your head — filter first, then map the survivors — guess the final list,
and only then verify with a quick script.

## Common mistakes & gotchas

- ⚠️ `map`/`filter` return lazy ITERATORS in Python 3 — print them and you get `<map object>`. Wrap in `list()`.
- ⚠️ A lambda can only hold ONE expression — no statements, loops, or assignments inside.
- ⚠️ Don't assign a lambda to a name (`f = lambda x: ...`); just use `def` — it's clearer and debuggable.
- ⚠️ `reduce` must be imported from functools; it's not a built-in. For sums/products prefer `sum()` / `math.prod()`.
- ⚠️ Overusing map/filter/lambda can be less readable than a simple comprehension — pick the clearer one.

## Cheat sheet

```python
double = lambda x: x * 2
nums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x * x, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))
from functools import reduce
print(reduce(lambda a, x: a * x, [2, 3, 4]))  # 24
print(sorted(["bb", "a", "ccc"], key=len))
print(max([("A", 30), ("B", 45)], key=lambda p: p[1]))
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

## What's next

Bumped into names appearing and vanishing? Go to [`12 — Scope (local, global, nonlocal)`](../12-scope/) to learn the LEGB lookup rules.

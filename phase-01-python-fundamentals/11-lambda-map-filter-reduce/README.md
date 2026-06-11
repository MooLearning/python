# 11 — Lambda, Map, Filter and Reduce

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **lambda** is a tiny, anonymous one-line function: `lambda x: x*2`. It pairs naturally with **map** (apply a function to every item), **filter** (keep items that pass a test), and **reduce** (combine all items into one value). These are the building blocks of the 'functional' style.

## Why it matters

You'll see lambdas everywhere as `key=` arguments to `sorted()`, `min()`, and `max()`, and map/filter are concise ways to transform data. Understanding them helps you read others' code and write compact pipelines.

## Key concepts

- **lambda** — `lambda args: expression` — a function with no name and a single expression.
- **map(func, iterable)** — Applies func to each item; returns a lazy iterator (wrap in list()).
- **filter(func, iterable)** — Keeps items where func returns True.
- **reduce(func, iterable)** — From functools; folds items into one value (e.g., product).
- **key= functions** — `sorted(data, key=lambda x: x[1])` sorts by a computed value.

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

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ `map`/`filter` return lazy ITERATORS in Python 3 — print them and you get `<map object>`. Wrap in `list()`.
- ⚠️ A lambda can only hold ONE expression — no statements, loops, or assignments inside.
- ⚠️ Don't assign a lambda to a name (`f = lambda x: ...`); just use `def` — it's clearer and debuggable.
- ⚠️ `reduce` must be imported from functools; it's not a built-in. For sums/products prefer `sum()` / `math.prod()`.
- ⚠️ Overusing map/filter/lambda can be less readable than a simple comprehension — pick the clearer one.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


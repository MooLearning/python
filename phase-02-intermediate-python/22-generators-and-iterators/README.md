# 22 — Generators and Iterators

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

An **iterator** is an object you can step through one item at a time with `next()`. A **generator** is the easy way to create one: write a normal function but use `yield` instead of `return`. Generators produce values **lazily** (on demand), so they can represent huge or even infinite sequences without using much memory.

## Why it matters

Lazy evaluation is a superpower for data: stream a multi-gigabyte file line by line, generate an infinite sequence, or build efficient pipelines that compute only what's needed. Generators make memory-light, composable code.

## Key concepts

- **iterable vs iterator** — Iterable = can be looped (list); iterator = produces items via next().
- **yield** — Pauses the function, returns a value, and resumes where it left off next time.
- **Lazy evaluation** — Values are produced one at a time, only when requested.
- **Generator expression** — `(x*x for x in range(10))` — like a comprehension but lazy.
- **Infinite generators** — A `while True: yield` loop can run forever; take only what you need.
- **next() / StopIteration** — next() pulls the next value; raises StopIteration when exhausted.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
def countdown(n):
    while n > 0:
        yield n          # pause here and hand back n
        n -= 1           # resume here on the next call

gen = countdown(3)
print(next(gen))   # 3
print(next(gen))   # 2
for x in gen:      # continue from where next() left off
    print("loop:", x)   # 1

# Generators are single-use: once exhausted, they're done
print(list(countdown(4)))   # [4, 3, 2, 1]
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ A generator is exhausted after ONE full pass — iterate it again and you get nothing. Recreate it.
- ⚠️ `yield` makes the WHOLE function a generator; calling it runs no code until you iterate it.
- ⚠️ Don't call `list()` on an infinite generator — it never ends. Use itertools.islice or a break.
- ⚠️ Generator expressions use parentheses `()`; brackets `[]` build a full list eagerly in memory.
- ⚠️ You can't index a generator (`gen[0]` fails) — convert to a list first if you need random access.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


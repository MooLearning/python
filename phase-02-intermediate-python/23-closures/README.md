# 23 — Closures

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **closure** is a function that 'remembers' variables from the scope where it was created, even after that outer scope has finished. You make one by defining a function **inside** another function and returning the inner one. The inner function 'closes over' the outer variables.

## Why it matters

Closures let you create configured, stateful functions without classes — function factories, callbacks, and the machinery behind decorators. They're a clean way to attach data to behavior.

## Key concepts

- **Nested functions** — A function defined inside another function.
- **Free variables** — Variables used by the inner function but defined in the enclosing one.
- **Returning a function** — The outer returns the inner, which keeps access to those variables.
- **State without classes** — Closures can hold mutable state via `nonlocal`.
- **__closure__** — Shows the captured cells; mostly for curiosity/debugging.
- **Late binding** — Closures capture VARIABLES, not values — a classic loop gotcha.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor     # 'factor' is remembered from the enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10))   # 20
print(triple(10))   # 30
# Each closure remembers its OWN factor:
print(double.__closure__[0].cell_contents)   # 2
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Late binding: a closure captures the VARIABLE, not its value at creation. In loops, use a default arg to freeze it.
- ⚠️ To MODIFY an enclosing variable you need `nonlocal`; reading it works without.
- ⚠️ Each call to the factory creates a NEW, independent closure with its own captured variables.
- ⚠️ Closures keep their captured objects alive (can't be garbage-collected) — watch memory with large captures.
- ⚠️ If you find yourself adding lots of state to a closure, a class may be clearer.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


# 10 — Functions

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **function** is a reusable, named block of code defined with `def`. It can take **parameters** (inputs), do work, and `return` a result. Python supports **default values**, **keyword arguments**, and catch-all `*args` (extra positional) and `**kwargs` (extra keyword) parameters.

## Why it matters

Functions are how you avoid repeating yourself and how you break big problems into small, testable pieces. Every library you'll use is just a collection of functions. Writing clear functions is the single biggest step from 'scripting' to 'programming'.

## Key concepts

- **def / return** — `def add(a, b): return a + b`. No return -> the function returns None.
- **Parameters vs arguments** — Parameters are names in the def; arguments are values you pass.
- **Default values** — `def greet(name='friend'):` makes name optional.
- **Keyword arguments** — Call with names for clarity: `area(width=3, height=4)`.
- ***args / **kwargs** — Accept any number of extra positional / keyword arguments.
- **Docstrings** — A string on the first line documents what the function does.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
def add(a, b):
    "Return the sum of a and b."   # docstring
    return a + b

result = add(3, 4)
print("add(3, 4) =", result)       # 7

# A function with no return gives back None
def shout(text):
    print(text.upper() + "!")

value = shout("hello")             # prints HELLO!
print("shout returned:", value)    # None
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ NEVER use a mutable default like `def f(items=[]):` — the SAME list is reused across calls. Use `None` and create inside.
- ⚠️ A function with no `return` returns `None`; `x = print('hi')` makes x None, not 'hi'.
- ⚠️ Positional arguments must come before keyword arguments in a call.
- ⚠️ Indentation defines the function body; a mis-indented line silently leaves the function.
- ⚠️ Shadowing built-ins (naming a function `list` or `sum`) breaks them for the rest of your code.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


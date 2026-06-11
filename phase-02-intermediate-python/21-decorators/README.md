# 21 — Decorators

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **decorator** is a function that takes another function and returns a new, enhanced version of it — without changing the original's code. You apply one with the `@decorator` syntax above a function. They're used for logging, timing, caching, access control, and registering functions.

## Why it matters

Decorators let you add behavior to many functions in a reusable, declarative way. You'll meet them constantly: `@property`, `@staticmethod`, `@app.route` in Flask, `@lru_cache`, and `@pytest.fixture`. Understanding them demystifies a lot of 'magic'.

## Key concepts

- **Functions are objects** — You can pass them around, return them, and store them in variables.
- **Wrapper function** — An inner function that runs code before/after calling the original.
- **@decorator syntax** — `@deco` above `def f` is sugar for `f = deco(f)`.
- **functools.wraps** — Preserves the original function's name/docstring on the wrapper.
- **Decorators with arguments** — A decorator factory: a function returning a decorator.
- ***args, **kwargs** — Wrappers use them to forward any arguments to the wrapped function.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import functools

def shout(func):
    @functools.wraps(func)            # keep func's name/docstring
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) # call the original
        return result.upper() + "!"   # enhance the result
    return wrapper

@shout                                 # same as greet = shout(greet)
def greet(name):
    return f"hello {name}"

print(greet("ada"))     # HELLO ADA!
print(greet.__name__)   # greet  (thanks to functools.wraps)
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Always use `@functools.wraps(func)` on the wrapper, or you lose the original name, docstring, and help().
- ⚠️ A wrapper must accept `*args, **kwargs` and forward them, or it breaks functions with different signatures.
- ⚠️ Remember to RETURN the wrapped function's result, or every decorated function silently returns None.
- ⚠️ Decorators run at definition time (when the `@` line is reached), not when the function is called.
- ⚠️ Stacked decorators apply bottom-up: the one nearest the def wraps first.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


# 14 — Exception Handling

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Exceptions** are errors that happen while a program runs (dividing by zero, a missing file, bad input). Instead of crashing, you can **catch** them with `try`/`except`. `else` runs when no error occurred, `finally` always runs (great for cleanup), and `raise` lets you signal your own errors.

## Why it matters

Real programs face messy input and unreliable resources. Graceful error handling is the difference between a program that crashes and one that recovers, logs the problem, and keeps going. It's essential for files, networks, and APIs.

## Key concepts

- **try / except** — Run risky code; if it raises, jump to the matching except block.
- **Specific exceptions** — Catch `ValueError`, `KeyError`, etc. — not bare `except:`.
- **else** — Runs only if the try block succeeded with no exception.
- **finally** — Always runs (success or failure) — perfect for closing resources.
- **raise** — Trigger an exception yourself: `raise ValueError('bad input')`.
- **Exception object** — `except ValueError as e:` lets you inspect the message.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Can't divide by zero!")
        return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # message, then None

# Catch different errors differently
for value in ["42", "oops"]:
    try:
        print("parsed:", int(value))
    except ValueError as e:
        print("Bad number:", e)
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Avoid bare `except:` — it hides bugs and even catches Ctrl-C. Catch specific exceptions.
- ⚠️ Don't put a huge block in `try`; wrap only the line(s) that can actually fail.
- ⚠️ `except` order matters: put specific exceptions before general ones (Exception last).
- ⚠️ Swallowing errors silently (`except: pass`) makes debugging miserable — at least log them.
- ⚠️ `finally` runs even if you `return` inside try — use it for cleanup, not for return values.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


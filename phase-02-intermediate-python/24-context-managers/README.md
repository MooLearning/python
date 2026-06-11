# 24 — Context Managers

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **context manager** is the object behind the `with` statement. It guarantees setup and **cleanup** happen around a block of code — even if an error occurs. `with open(...)` is the famous example (it always closes the file). You can write your own with a class (`__enter__`/`__exit__`) or, more simply, with `@contextmanager`.

## Why it matters

Resource leaks (unclosed files, sockets, database connections, unreleased locks) are a common source of bugs. Context managers make 'always clean up' automatic and readable. They also handle setup/teardown for timers, temporary settings, and transactions.

## Key concepts

- **with statement** — Runs setup, yields control to the block, then runs cleanup.
- **__enter__ / __exit__** — The class protocol: enter returns the resource, exit cleans up.
- **@contextmanager** — Decorator that turns a generator (with one yield) into a context manager.
- **Cleanup on error** — __exit__ runs even when the block raises — perfect for closing things.
- **Multiple managers** — `with a() as x, b() as y:` manages several at once.
- **contextlib** — Helpers like suppress, redirect_stdout, closing.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
# Manual way -- easy to forget close(), and a crash skips it:
f = open("demo.txt", "w", encoding="utf-8")
f.write("hi")
f.close()

# The 'with' way -- close() is GUARANTEED, even on error:
with open("demo.txt", "r", encoding="utf-8") as f:
    print(f.read())     # hi
# file is now closed automatically
print("closed?", f.closed)   # True

import os
os.remove("demo.txt")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ In a class manager, `__exit__` returning True SUPPRESSES the exception — usually you want False/None.
- ⚠️ With @contextmanager, put `yield` inside try/finally so cleanup runs even when the block raises.
- ⚠️ The value after `as` comes from what `__enter__` returns (or what you `yield`), not the manager itself.
- ⚠️ `with` is for resource lifetimes, not general flow control — don't abuse it.
- ⚠️ Opening multiple resources? Use one `with a, b:` so all get cleaned up correctly.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


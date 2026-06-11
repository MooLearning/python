# 30 — Logging

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Logging** records what your program does while it runs. It's far better than scattering `print()` calls: you get **severity levels** (DEBUG, INFO, WARNING, ERROR, CRITICAL), timestamps, the source module, and you can route messages to files, the console, or both — and turn the detail up or down without editing your code.

## Why it matters

When something breaks in production (or in a long training run), logs are how you find out what happened. Good logging turns 'it crashed somehow' into 'here's exactly where and why'. It's a habit that separates hobby scripts from real software.

## Key concepts

- **Levels** — DEBUG < INFO < WARNING < ERROR < CRITICAL; set a threshold and below it is hidden.
- **Logger** — Get one with `logging.getLogger(__name__)`; don't just use the root logger.
- **Handlers** — Where logs go: StreamHandler (console), FileHandler (file), etc.
- **Formatter** — Controls the layout: time, level, name, message.
- **basicConfig** — Quick one-call setup for simple scripts.
- **exception()** — Logs an ERROR plus the full traceback inside an except block.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,                                   # show DEBUG and above
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%H:%M:%S",
    force=True,                                            # re-apply config
)

logging.debug("detailed info for diagnosing problems")
logging.info("things are working as expected")
logging.warning("something unexpected, but we continue")
logging.error("a serious problem occurred")
# Output goes to the console (stderr) with timestamp and level
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Call `basicConfig` ONCE, early; later calls do nothing if logging is already configured.
- ⚠️ Use lazy formatting: `log.info('x=%s', x)` not `log.info(f'x={x}')` — args are only formatted if the level is active.
- ⚠️ Default level is WARNING, so INFO/DEBUG messages won't show until you lower the threshold.
- ⚠️ Use `log.exception(...)` inside `except` blocks to capture the traceback automatically.
- ⚠️ Don't use logging to print normal program OUTPUT for users — that's what print() is for; logging is for diagnostics.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


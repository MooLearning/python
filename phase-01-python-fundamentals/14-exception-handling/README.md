# 14 — Exception Handling

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

⏱️ ~25 min · 🔁 `README → notes.py → practice.md` · ⬅️ Prerequisite: `../13-recursion-basics/`

## What is it?

**Exceptions** are errors that surface while your program is already running — a division by zero, a missing dictionary key, a user typing `"oops"` where a number belongs. Python doesn't just shrug; it *raises* an exception object and stops the current path unless something catches it.

That's where `try` / `except` comes in. You wrap the risky line in `try`, name the failure you expect in `except`, and decide what happens instead of a crash. Add `else` for "only if nothing went wrong" and `finally` for "always run this cleanup", plus `raise` when *you* want to report a problem loudly.

🎪 **Analogy — the trapeze safety net.** A circus act doesn't remove gravity; it rigs a net underneath. Most nights the flyer never touches it (the happy path). On a bad night the net catches the fall, the announcer says something calm, and the show continues. `try` is the act, `except` is the net, `finally` is the crew folding the net afterward no matter what happened.

## Why it matters

- **Messy humans, messy world.** Every `input()`, CSV row, JSON response, or file read can be malformed. Handling `ValueError`, `KeyError`, or `FileNotFoundError` turns a crash into a helpful message and a retry.
- **Resources you don't control.** Networks time out, disks fill up, APIs return surprises. Code that anticipates failure can log the problem, back off, and keep the rest of the pipeline alive.
- **AI / career hook.** Data scripts and model training loops process millions of rows — one bad row shouldn't kill a 6-hour job. Interviewers also love asking about `try` / `except` / `else` / `finally` ordering, so this topic pays off twice.

## How it works

Think of it as a four-door checkpoint:

1. Python runs the `try` block line by line.
2. If nothing raises, it skips every `except` and runs `else` (if present).
3. If an exception raises, Python freezes the `try` block and looks for a matching `except` from top to bottom — first match wins.
4. `finally` runs no matter what: success, handled error, unhandled error, even `return`.
5. If no `except` matches, the exception keeps bubbling up until something catches it or the program exits with a traceback.

```text
try → success? → else → finally → continue
         |
       raises → matching except? → handle → finally → continue
                                → no match → finally → bubble up
```

## Key concepts

- **Try the risky bit** — `try: n = int(text)` isolates exactly the line that can fail.
- **Catch something specific** — `except ValueError:` beats a bare `except:` every time.
- **Name the error** — `except ValueError as e:` gives you `e` to log or display.
- **Branch on failure type** — `except ZeroDivisionError:` versus `except ValueError:` handle different problems differently.
- **Catch several at once** — `except (KeyError, TypeError) as e:` shares one handler for a tuple of types.
- **Else means "no crash"** — `else: print(n)` runs only when the `try` block fully succeeded.
- **Finally always runs** — `finally: print("done")` is your cleanup guarantee, even after `return`.
- **Raise your own** — `raise ValueError("age can't be negative")` signals bad input to your callers.

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

The walkthrough: `safe_divide(10, 2)` never raises, so it returns `5.0` straight from `try`. With `(10, 0)` Python raises `ZeroDivisionError`, jumps into the matching `except`, prints the warning, and returns `None`. The loop below shows the same idea for parsing: `"42"` converts cleanly while `"oops"` raises `ValueError`, which we catch as `e` and report.

Keep going in `notes.py` — Example 2 is **"else and finally"** (the success-only branch plus guaranteed cleanup), and Example 3 is **"Raising your own exceptions"** (guard functions with `raise` plus catching a tuple of types).

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

⏳ 2-minute tinkering: predict what this prints, then run it to check. After that, change `"nope"` to `"100"` and predict again before re-running — pay attention to when `else` runs versus when `finally` runs:

```python
def read_config(text):
    try:
        number = int(text)
    except ValueError:
        print("Not a valid integer")
    else:
        print("Success! Got", number)
    finally:
        print("done checking")

read_config("nope")
```

No solution here — experiment and trust the output.

## Common mistakes & gotchas

- ⚠️ Avoid bare `except:` — it hides bugs and even catches Ctrl-C. Catch specific exceptions.
- ⚠️ Don't put a huge block in `try`; wrap only the line(s) that can actually fail.
- ⚠️ `except` order matters: put specific exceptions before general ones (Exception last).
- ⚠️ Swallowing errors silently (`except: pass`) makes debugging miserable — at least log them.
- ⚠️ `finally` runs even if you `return` inside try — use it for cleanup, not for return values.

## Cheat sheet

```python
try:
    n = int("42")
except ValueError as e:
    print("bad:", e)
else:
    print("ok:", n)
finally:
    print("done")
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

You'll parse risky strings, guard division, handle missing keys, practice `finally`, `raise` your own errors, and sum only the valid numbers in a messy list.

## What's next

Finished catching falling trapeze artists? Head to [`../15-file-handling/`](../15-file-handling/) — where you'll read and write files, and immediately need everything you just learned about handling errors gracefully.

# 04 — Input, Output and Type Casting

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

`print()` sends text **out** to the screen; `input()` reads text **in** from the user. Crucially, `input()` ALWAYS returns a `str`, so to do math you must **cast** (convert) it with `int()` or `float()`. Casting also goes the other way: `str(42)` turns a number into text.

## Why it matters

Almost every interactive program reads input and prints output. Understanding that input is always text — and how to convert between types — fixes the classic `'10' + 5` crash.

## Key concepts

- **print()** — Outputs values; `sep=` and `end=` control separators and line endings.
- **input(prompt)** — Pauses and returns whatever the user types — as a string.
- **int() / float()** — Convert a string (or number) to an integer / decimal.
- **str()** — Convert any value to its text form.
- **f-strings** — `f"{name} is {age}"` embeds values directly in text — the modern way to format.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
name = "Ada"
age = 36

# f-strings: put variables inside {curly braces}
print(f"{name} is {age} years old.")

# sep controls what goes BETWEEN items; end controls what goes at the END
print("a", "b", "c", sep="-")        # a-b-c
print("no newline here ->", end=" ")
print("...continued on same line")

# Format numbers: 2 decimal places
pi = 3.14159
print(f"pi is about {pi:.2f}")        # pi is about 3.14
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ `input()` returns a string ALWAYS. `input() + 1` crashes; cast with `int()` first.
- ⚠️ `int("3.5")` raises ValueError — you can't int() a decimal string. Use `int(float("3.5"))`.
- ⚠️ `int(9.9)` gives `9` (it truncates toward zero); it does NOT round. Use `round()` to round.
- ⚠️ You can't do `"age: " + 30` — concatenate strings only. Use an f-string or `str(30)`.
- ⚠️ Empty string, 0, 0.0, None and empty containers are all 'falsy' — `bool()` of them is False.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


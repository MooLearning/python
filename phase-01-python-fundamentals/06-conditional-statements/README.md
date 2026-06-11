# 06 — Conditional Statements

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

Conditional statements let your program **make decisions**. `if` runs a block when a condition is True; `elif` ('else if') checks another condition; `else` is the fallback. Python uses **indentation** (not braces) to mark which lines belong to each branch.

## Why it matters

Decision-making is the heart of logic. Validating input, branching on cases, and reacting to data all rely on conditionals. Get the indentation and truthiness rules right and the rest of programming opens up.

## Key concepts

- **if / elif / else** — Check conditions in order; the FIRST true branch runs, the rest are skipped.
- **Indentation** — 4 spaces define a block. Consistency is mandatory — Python enforces it.
- **Truthiness** — Non-zero numbers, non-empty strings/lists are 'truthy'; 0, '', [], None are 'falsy'.
- **Comparison chaining** — `if 0 < x < 10:` is valid and reads like math.
- **Ternary expression** — `label = 'even' if n % 2 == 0 else 'odd'` — a one-line if/else.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:        # only checked if the previous test was False
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)   # B
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Use `==` to compare, not `=` (which assigns). `if x = 5:` is a SyntaxError.
- ⚠️ Indentation must be consistent (4 spaces is standard). Mixing tabs and spaces causes errors.
- ⚠️ Every `if`/`elif`/`else` line ends with a colon `:` — forgetting it is a SyntaxError.
- ⚠️ `elif` only runs if earlier conditions were False. Order your branches from most to least specific.
- ⚠️ `if items == True:` is fragile — just write `if items:` to test truthiness.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


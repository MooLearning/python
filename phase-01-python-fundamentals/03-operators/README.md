# 03 — Operators

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Operators** are symbols that perform actions on values. Python groups them into **arithmetic** (`+ - * / // % **`), **comparison** (`== != < > <= >=`), **logical** (`and or not`), **assignment** (`= += -=` …) and **bitwise** (`& | ^ ~ << >>`). Comparisons and logical operators always produce a `bool`.

## Why it matters

Operators are how you compute, compare and make decisions. Logical and comparison operators in particular power every `if` statement and loop condition you'll ever write.

## Key concepts

- **Arithmetic** — `+ - * /` plus `//` (floor div), `%` (remainder), `**` (power).
- **Comparison** — `==` equal, `!=` not equal, `< > <= >=`. Returns True/False.
- **Logical** — `and`, `or`, `not` combine boolean expressions.
- **Assignment shortcuts** — `x += 1` means `x = x + 1`. Also -=, *=, /=, //=, **=, %=.
- **Bitwise** — Operate on the binary bits of integers: & | ^ ~ << >>.
- **Operator precedence** — `**` before `* /` before `+ -`; use parentheses when unsure.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
a, b = 17, 5
print("add ", a + b)    # 22
print("sub ", a - b)    # 12
print("mul ", a * b)    # 85
print("div ", a / b)    # 3.4   (float)
print("floor", a // b)  # 3     (drops the decimal)
print("mod ", a % b)    # 2     (remainder)
print("pow ", a ** b)   # 1419857
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ `/` always returns a float, even `4 / 2` gives `2.0`. Use `//` for integer division.
- ⚠️ `%` of negative numbers may surprise you: `-7 % 3` is `2` in Python, not `-1`.
- ⚠️ `and`/`or` return one of the operands, not always True/False: `0 or 'x'` is `'x'`.
- ⚠️ Don't confuse `&`/`|` (bitwise) with `and`/`or` (logical). `5 and 3` is `3`, but `5 & 3` is `1`.
- ⚠️ Precedence traps: `2 + 3 * 4` is 14, not 20. Use parentheses to be explicit.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


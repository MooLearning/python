# 05 — Strings and Methods

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **string** is an ordered sequence of characters in quotes. Strings are **immutable** (you can't change them in place — every 'edit' makes a new string). They come with dozens of handy **methods** like `.upper()`, `.strip()`, `.split()`, `.replace()`, and `.find()`, and they support **indexing** (`s[0]`) and **slicing** (`s[1:4]`).

## Why it matters

Text is everywhere — file names, user input, CSV rows, API responses, NLP data. String slicing and methods are some of the most-used tools in all of Python.

## Key concepts

- **Indexing** — `s[0]` is the first char, `s[-1]` the last. Counting starts at 0.
- **Slicing** — `s[start:stop:step]`; stop is excluded. `s[::-1]` reverses.
- **Immutability** — `s[0] = 'x'` is illegal. Build a new string instead.
- **Common methods** — .upper/.lower/.strip/.split/.join/.replace/.find/.startswith.
- **f-strings** — Format values into text: `f"{x:>5}"` right-aligns in width 5.
- **in operator** — `'cat' in 'concatenate'` checks for a substring.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
s = "Python"
print(s[0])     # P    (first character, index 0)
print(s[-1])    # n    (last character)
print(s[0:3])   # Pyt  (indices 0,1,2 -- stop is excluded)
print(s[2:])    # thon (from index 2 to the end)
print(s[:2])    # Py   (start to index 1)
print(s[::-1])  # nohtyP (reverse using step -1)
print(len(s))   # 6    (number of characters)
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Strings are immutable: `s[0] = 'X'` raises TypeError. Create a new string instead.
- ⚠️ Indexing past the end (`s[100]`) raises IndexError, but SLICING past the end is safe.
- ⚠️ `.find()` returns -1 when not found (no error); `.index()` raises ValueError. Pick deliberately.
- ⚠️ `.split()` with no argument splits on ANY whitespace and drops empties — different from `.split(' ')`.
- ⚠️ Methods return NEW strings; `s.upper()` alone does nothing unless you store the result.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


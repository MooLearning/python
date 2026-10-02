# 02 — Variables and Data Types

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

*⏱️ ~25 min · Loop: `README → notes.py → practice.md` · Prerequisite: [`01-installation-and-setup`](../01-installation-and-setup/).*

## What is it?

A **variable** is a name you bind to a value with `=`, as in `age = 25`. Python is dynamically typed:
you never declare a type, the value itself carries one, and the same name can later point at a
completely different type. The five everyday types are `int` (whole numbers like `25`), `float`
(decimals like `19.99`), `str` (text like `"Ada"`), `bool` (`True` / `False`), and `NoneType` (the
one-off value `None` meaning "nothing here yet").

Ask for any value's type with `type()`, reassign freely with `x = ...`, and assign several names at
once with `a, b, c = 1, 2, 3`. Numbers follow school arithmetic with two Python twists: `/` always
yields a `float`, and `float` math is approximate (`0.1 + 0.2` is not exactly `0.3`).

Picture a pantry of glass jars with sticky-note labels. The jar's *contents* are the value (`25`,
`"Ada"`), the sticky note is the variable name (`age`, `name`), and the jar's *shape* is the type —
spice jar for `int`, measuring jug for `float`, labelled tin for `str`. Peeling a label off one jar
and sticking it on another is reassignment: `x = 10` then `x = "now I am text"` never changes the
old jar, it just moves the label. `type()` is you picking up a jar and reading its shape.

## Why it matters

- Every program state is variables: counters, totals, usernames, flags, missing values (`None`).
  Choosing the right type decides what operations even make sense — `"42" + 1` explodes, `42 + 1` sings.
- Dynamic typing is fast to write but easy to trip on: a variable that was an `int` can silently become
  a `str` three functions later, so checking `type()` is a core debugging reflex.
- Career hook: in data/AI work a column of `int`s vs `float`s vs `str`s changes memory use, plots, and
  model training. Pandas and NumPy types are just these built-ins grown up — master them here first.

## How it works

Mental model — a variable is a *reference*, not a box:

1. **Create** — `age = 25` builds an `int` object `25` somewhere in memory.
2. **Bind** — the name `age` is a sticky note pointing at that object.
3. **Rebind** — `age = "Ada"` points the same note at a new `str` object; the old `25` is untouched.
4. **Inspect** — `type(age)` asks the *object*, never the name, what it is.

```text
name "age" ──points to──> ┌─────────────┐
                          │  int  │  25 │
                          └─────────────┘
after age = "Ada":

name "age" ──points to──> ┌─────────────┐
                          │  str │ "Ada"│
                          └─────────────┘
```

Same name, different object, different type — no declaration, no complaint.

## Key concepts

- **Variable** — a name bound to an object: `x = 10`; rebinding moves the name, e.g. `x = "hi"`.
- **Dynamic typing** — names have no fixed type: `v = None` then `v = 100` is legal.
- **int** — whole numbers of any size: `candies = 25`.
- **float** — decimals, always approximate: `price = 19.99` and `0.1 + 0.2` shows the wobble.
- **str** — text in quotes: `name = "Ada"`; digits in quotes stay text, e.g. `"42"`.
- **bool** — exactly two values with capitals: `is_student = True`.
- **None** — the "no value" sentinel: `nothing = None` whose `type(nothing)` is `NoneType`.
- **`type()`** — reveals the object's type: `type(3.0)` is `<class 'float'>`.
- **Multiple assignment & swap** — `a, b = b, a` exchanges values with no temp variable.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
age = 25            # int  (whole number)
price = 19.99       # float (decimal)
name = "Ada"        # str  (text)
is_student = True   # bool (True/False)
nothing = None      # NoneType (absence of a value)

# type() tells you the data type of a value
print(age, "->", type(age))
print(price, "->", type(price))
print(name, "->", type(name))
print(is_student, "->", type(is_student))
print(nothing, "->", type(nothing))
```

This is Example 1 from `notes.py`: five assignments cover the five starter types, then each line
pairs a value with its `type()` so you see the pattern — the *literal's shape* decides the type, not
any declaration. Note the capitals in `True` and the bare `None`, both classic spelling traps.

Keep going in `notes.py`: Example 2 ("Variables are dynamic and can be reassigned") rebinds `x` from
`int` to `str` and swaps `a, b` in one line, and Example 3 ("Numbers behave like math; watch int vs
float") contrasts `/` vs `//`, powers with `**`, and the famous `0.1 + 0.2` surprise.

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

Two-minute challenge (no solution — predict, then run): guess the output of these three lines before
executing them — `x = 7` then `x = 7 / 2` then `print(x, type(x))`. Does `x` hold an `int` or a
`float`, and why? Tinker: change the middle line to `x = 7 // 2` and to `x = "7"`, re-run each time,
and explain in one sentence what moved — the label or the jar?

## Common mistakes & gotchas

- ⚠️ `True`/`False`/`None` are capitalized. `true` or `null` will raise a NameError.
- ⚠️ `=` assigns a value; `==` compares two values. Mixing them up is the #1 beginner bug.
- ⚠️ Floats are approximate: `0.1 + 0.2 != 0.3`. Use `round()` or `math.isclose()` to compare.
- ⚠️ Variable names can't start with a digit and can't contain spaces. Use snake_case: `my_score`.
- ⚠️ Assigning to a name doesn't copy the value for lists/objects — it points to the SAME object (more on this later).

## Cheat sheet

```python
age = 25                        # int
price = 19.99                   # float
name = "Ada"                    # str
is_student = True               # bool (capital T!)
nothing = None                  # NoneType
print(type(price))              # <class 'float'>
a, b = 1, 2; a, b = b, a        # assign many, swap trick
print(7 / 2, 7 // 2, 2 ** 10)   # 3.5  3  1024
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

## What's next

Head to [`../03-operators/`](../03-operators/) to put those variables to work — arithmetic, comparisons,
logic, and shortcuts that turn stored values into decisions.

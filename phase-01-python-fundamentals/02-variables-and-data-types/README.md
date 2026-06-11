# 02 — Variables and Data Types

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **variable** is a name that points to a value, created with `=`. Python figures out the **type** automatically. The core built-in types you'll use constantly are `int` (whole numbers), `float` (decimals), `str` (text), `bool` (True/False), and `NoneType` (the special value `None`). You never declare a type — you just assign.

## Why it matters

Variables and types are the atoms of every program. Knowing how Python stores values and how types behave (and convert) prevents a huge class of beginner bugs, like adding a string to a number.

## Key concepts

- **Variable** — A label for a value: `x = 10`. Re-assigning just re-points the label.
- **Dynamic typing** — A variable can hold an int now and a string later — Python doesn't mind.
- **int / float** — Whole numbers vs decimals. `3` is int, `3.0` is float.
- **str** — Text in quotes: `'hi'` or "hi".
- **bool** — `True` or `False` (note the capital letters).
- **None** — Represents 'no value yet'; its type is NoneType.
- **type()** — Ask Python the type of any value: `type(3.0)`.

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

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ `True`/`False`/`None` are capitalized. `true` or `null` will raise a NameError.
- ⚠️ `=` assigns a value; `==` compares two values. Mixing them up is the #1 beginner bug.
- ⚠️ Floats are approximate: `0.1 + 0.2 != 0.3`. Use `round()` or `math.isclose()` to compare.
- ⚠️ Variable names can't start with a digit and can't contain spaces. Use snake_case: `my_score`.
- ⚠️ Assigning to a name doesn't copy the value for lists/objects — it points to the SAME object (more on this later).

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


# 20 — Dunder (Magic) Methods

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Dunder** (double-underscore) methods, also called **magic** or **special** methods, let your objects work with Python's built-in syntax. Define `__str__` for `print()`, `__len__` for `len()`, `__eq__` for `==`, `__add__` for `+`, `__getitem__` for `obj[i]`, and more. They're how you make custom classes feel native.

## Why it matters

Dunder methods turn your objects into first-class citizens: comparable, printable, iterable, addable. They're the secret behind why NumPy arrays support `+` and why a DataFrame supports `df[col]`. Implementing a few makes your classes intuitive to use.

## Key concepts

- **__init__** — Constructor/initializer (you already know this one).
- **__str__ / __repr__** — Human-readable string vs unambiguous developer string.
- **__len__** — Makes `len(obj)` work.
- **__eq__ / __lt__** — Define `==` and `<` so objects compare and sort.
- **__add__** — Define `obj1 + obj2`.
- **__getitem__** — Define `obj[key]` indexing; also enables iteration as a fallback.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):           # for developers / the REPL / debugging
        return f"Point(x={self.x}, y={self.y})"
    def __str__(self):            # for end users / print()
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(p)          # (3, 4)        -> uses __str__
print(str(p))     # (3, 4)
print(repr(p))    # Point(x=3, y=4) -> uses __repr__
print([p, p])     # lists show __repr__ of items
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ If you define `__eq__`, also define `__hash__` (or set it) if you want objects usable in sets/dicts.
- ⚠️ `__repr__` should be unambiguous (ideally valid code); `__str__` is for friendly display. Define __repr__ at least.
- ⚠️ `__add__` should return a NEW object, not mutate self — match how numbers behave.
- ⚠️ Forgetting `__repr__` makes debugging painful (you see `<object at 0x...>`).
- ⚠️ Comparison dunders should return NotImplemented for unsupported types, not raise — lets Python try the reflected op.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


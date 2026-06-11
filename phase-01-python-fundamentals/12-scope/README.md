# 12 — Scope (local, global, nonlocal)

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Scope** is the region of code where a name is visible. Python uses the **LEGB** rule to find names: **L**ocal (inside the current function), **E**nclosing (an outer function), **G**lobal (the module/file level), then **B**uilt-in. The `global` and `nonlocal` keywords let you reassign names from outer scopes.

## Why it matters

Scope explains why a variable 'disappears' outside a function, why you sometimes get surprising `UnboundLocalError`s, and how closures work. Knowing LEGB removes a whole category of confusing bugs.

## Key concepts

- **Local** — Names assigned inside a function — invisible outside it.
- **Enclosing** — The scope of an outer function around a nested one.
- **Global** — Names at the top level of the file.
- **Built-in** — Names Python provides (print, len, range...).
- **global keyword** — Lets a function REASSIGN a module-level variable.
- **nonlocal keyword** — Lets a nested function REASSIGN a variable in its enclosing function.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
x = "global"

def show():
    x = "local"          # a NEW local variable, separate from the global
    print("inside:", x)  # local

show()
print("outside:", x)     # global  -- unchanged

def reader():
    print("reading global:", x)   # OK to READ the global without 'global'
reader()
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Assigning to a name ANYWHERE in a function makes it local for the WHOLE function — causing UnboundLocalError if you read it first.
- ⚠️ Overusing `global` makes code hard to follow and test. Prefer passing values in and returning them out.
- ⚠️ `nonlocal` targets the nearest enclosing FUNCTION scope, not the global scope.
- ⚠️ You can READ a global inside a function without declaring it; you only need `global` to REASSIGN it.
- ⚠️ Loop variables (`for i in ...`) leak into the surrounding scope after the loop — they aren't function-scoped.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


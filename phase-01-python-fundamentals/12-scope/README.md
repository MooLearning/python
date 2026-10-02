# 12 — Scope (local, global, nonlocal)

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

⏱️ ~25 min · Loop: `README → notes.py → practice.md` · Prereq: [11 — Lambda, Map, Filter and Reduce](../11-lambda-map-filter-reduce/)

## What is it?

**Scope** is the region of code where a name is visible. When Python meets a
variable, it searches the **LEGB** chain in order: **L**ocal (inside the
current function), **E**nclosing (an outer function wrapping a nested one),
**G**lobal (top level of the module), then **B**uilt-in (`print`, `len`,
...). Reading an outer name is free, but *reassigning* one needs permission:
`global` rebinds a module-level name, `nonlocal` rebinds the nearest enclosing
function's name.

Think of an apartment building. Your bedroom (local) has sticky notes only you
see. The family flat around it (enclosing) shares a fridge calendar. The lobby
bulletin board (global) is visible to every flat, and the city's emergency
numbers posted by the door (built-in) work for everyone. You can read the lobby
board from your room, but if you want to replace it you must announce it with
`global` — otherwise you just pinned a lookalike note on your own wall.

## Why it matters

- **Explains vanishing variables:** why an assignment inside a function stays
  invisible outside, and why reading a global "just works."
- **Decodes `UnboundLocalError`:** any assignment in a function marks the name
  local for the *whole* body, so reading it first explodes.
- **Powers closures:** counters, decorators, and callbacks remember state via
  enclosing scope plus `nonlocal` instead of globals.
- **AI-career hook:** training loops, config objects, and notebook state get
  tangled fast — disciplined scope (pass in, return out) keeps experiments sane.

## How it works

Mental model — name lookup walks outward until it finds a match:

1. **L — Local:** parameters and assignments in the current function.
2. **E — Enclosing:** the nearest outer *function* (skipped if none).
3. **G — Global:** names at the top of the file/module.
4. **B — Built-in:** Python's own names like `len` and `range`.

```text
name? ──► Local? ──no──► Enclosing? ──no──► Global? ──no──► Built-in? ──no──► NameError
              │               │                 │                  │
             YES              YES               YES                YES → use it
```

Two override rules: `global x` inside a function means "rebind the lobby
board," and `nonlocal x` in a nested function means "rebind the flat's
calendar." Both only affect *assignment*; plain reads need no keyword.

## Key concepts

- **Local shadowing** — `x = "local"` inside `show()` hides the global `x`.
- **Reading globals is fine** — `print(x)` inside `reader()` needs no keyword.
- **Assignment marks local** — any `x = ...` in a body makes `x` local everywhere in it.
- **`global` rebinds** — `global counter` then `counter += 1` updates the module value.
- **`nonlocal` rebinds** — `nonlocal total` inside `add()` updates the enclosing `total`.
- **Closures remember** — `acc = make_adder(); acc(5)` keeps `total` between calls.
- **LEGB order** — `len` resolves to `B` unless you shadow it with your own `len`.
- **Loop leakage** — `for i in range(3): pass` leaves `i == 2` visible afterwards.
- **Prefer pure style** — `def inc(c): return c + 1` beats mutating a global.

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

`show()` pins its own bedroom note: the global `x` survives untouched, proving
assignment creates a separate local. `reader()` never assigns, so its `x`
falls through L and E straight to the lobby board. Continue in `notes.py`:
Example 2 ("global and nonlocal") bumps a module counter and builds a
remembering adder, and Example 3 ("The classic UnboundLocalError trap") shows
the read-before-assign crash and the `global` fix.

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

Two-minute prediction (don't run first): with `value = 100` at the top, what
happens when a function does `print(value)` on line one and `value = 1` on
line two — and what single keyword on line one of the body changes the outcome?
Sketch the LEGB lookup for the `print` line in both versions, then run
`notes.py` Example 3 to confirm.

## Common mistakes & gotchas

- ⚠️ Assigning to a name ANYWHERE in a function makes it local for the WHOLE function — causing UnboundLocalError if you read it first.
- ⚠️ Overusing `global` makes code hard to follow and test. Prefer passing values in and returning them out.
- ⚠️ `nonlocal` targets the nearest enclosing FUNCTION scope, not the global scope.
- ⚠️ You can READ a global inside a function without declaring it; you only need `global` to REASSIGN it.
- ⚠️ Loop variables (`for i in ...`) leak into the surrounding scope after the loop — they aren't function-scoped.

## Cheat sheet

```python
counter = 0
def increment():
    global counter; counter += 1  # rebind module name
def make_adder():
    total = 0
    def add(n):
        nonlocal total            # rebind enclosing name
        total += n
        return total
    return add
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

## What's next

Ready for functions that call themselves? Step into [`13 — Recursion Basics`](../13-recursion-basics/) to meet base cases and the call stack.

# 10 — Functions

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

⏱️ ~25 min · Loop: `README → notes.py → practice.md` · Prereq: [09 — Comprehensions](../09-comprehensions/)

## What is it?

A **function** is a named, reusable block of code defined with `def`. You hand
it **parameters** (inputs), it runs its body, and it optionally hands back a
value with `return`. Python adds flexible calling conventions on top: **default
values** for optional parameters, **keyword arguments** for clarity, and
catch-all `*args` (extra positional values) plus `**kwargs` (extra named values).

Picture a recipe card taped inside a kitchen cupboard. The card names the dish,
lists ingredients with substitutes ("cheese = cheddar if you don't say"), and
gives steps that always produce the same plate. You don't re-learn cooking each
night — you call the card with whatever you have. Functions are those cards:
write the logic once, then `greet("Ada")` or `area(width=3, height=4)` whenever
you're hungry for a result.

## Why it matters

- **Kill repetition:** a validation, formatter, or metric computed in three
  places becomes one tested function instead of three drifting copies.
- **Decompose problems:** big scripts turn into small, nameable steps you can
  reason about, test, and rearrange independently.
- **Speak library:** NumPy, pandas, and every API you will meet are just
  collections of functions — parameters, defaults, and returns are the dialect.
- **AI-career hook:** feature functions, loss helpers, and evaluation routines
  are shared across experiments; clean signatures make research reproducible.

## How it works

Mental model — a function call is a round trip:

1. **Define** once with `def name(params):` and an indented body.
2. **Call** with arguments: `add(3, 4)` binds `a=3, b=4` for that run.
3. **Execute** the body top to bottom with those local bindings.
4. **Return** a value to the caller — or `None` if no `return` runs.

```text
caller ── arguments ──► [ function body ] ── return value ──► caller
                          (params are local copies/names)
```

Defaults fill in missing arguments at call time; `*args` scoops leftover
positionals into a tuple and `**kwargs` scoops leftover keywords into a dict.

## Key concepts

- **Define and return** — `def add(a, b): return a + b`; no `return` means `None`.
- **Parameters vs arguments** — `def f(name)` declares a parameter; `f("Ada")` passes an argument.
- **Default values** — `def greet(name, greeting="Hello"):` makes `greeting` optional.
- **Keyword arguments** — `area(width=3, height=4)` is explicit; order stops mattering.
- **Mixed calls** — `greet("Bo", greeting="Hi")` combines positional and keyword styles.
- **`*args` tuple** — `def total(*args): return sum(args)` accepts any count: `total(1, 2, 3)`.
- **``**kwargs`` dict** — `def describe(**kwargs): ...` captures `describe(role="dev")`.
- **Multiple returns** — `return min(nums), max(nums)` packs a tuple; unpack with `lo, hi = min_max(xs)`.
- **Docstrings** — `"Return the sum."` as the first line documents `help(add)`.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
def add(a, b):
    "Return the sum of a and b."   # docstring
    return a + b

result = add(3, 4)
print("add(3, 4) =", result)       # 7

# A function with no return gives back None
def shout(text):
    print(text.upper() + "!")

value = shout("hello")             # prints HELLO!
print("shout returned:", value)    # None
```

`add` shows the classic round trip: parameters in, computed value out via
`return`. `shout` is the contrast — it *does* something (prints) but returns
nothing, so Python hands back `None`. Keep going in `notes.py`: Example 2
("Default values and keyword arguments") makes greetings optional and order-free,
and Example 3 ("*args and **kwargs for flexible functions") totals anything and
returns min/max pairs.

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

Two-minute prediction (don't run yet): what do `print(greet("Ada"))`,
`print(greet("Ada", "Welcome"))`, and `print(total())` output if `greet` has a
default greeting and `total` sums `*args` — and what type is the result of each?
Now tinker: call `describe(name="Ada", role="pioneer", city="London")` in your
head, guess the printed lines, then run `notes.py` to check.

## Common mistakes & gotchas

- ⚠️ NEVER use a mutable default like `def f(items=[]):` — the SAME list is reused across calls. Use `None` and create inside.
- ⚠️ A function with no `return` returns `None`; `x = print('hi')` makes x None, not 'hi'.
- ⚠️ Positional arguments must come before keyword arguments in a call.
- ⚠️ Indentation defines the function body; a mis-indented line silently leaves the function.
- ⚠️ Shadowing built-ins (naming a function `list` or `sum`) breaks them for the rest of your code.

## Cheat sheet

```python
def add(a, b):
    return a + b
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet("Ada", greeting="Hi"))   # keyword call
def total(*args):
    return sum(args)                 # total(1, 2, 3) -> 6
def describe(**kwargs):
    return kwargs                    # dict of extras
low, high = min([4, 9, 1, 7]), max([4, 9, 1, 7])
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

## What's next

Ready for throwaway one-liners? Continue to [`11 — Lambda, Map, Filter and Reduce`](../11-lambda-map-filter-reduce/) to process collections functionally.

# 16 — Modules and Packages

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

⏱️ ~25 min · 🔁 `README → notes.py → practice.md` · ⬅️ Prerequisite: `../15-file-handling/`

## What is it?

A **module** is any `.py` file whose code you can borrow with `import`. A **package** is a folder of related modules you address with dots, like `pkg.module`. Python arrives with a giant **standard library** — `math`, `random`, `json`, `datetime`, `statistics`, `collections` — so most everyday jobs already have a tested tool waiting.

Imports come in three flavors: `import x` keeps the namespace (`x.thing`), `from x import y` pulls a name directly into yours (`y`), and `import x as alias` renames on arrival (`import json as J`). A file can be both a reusable module *and* a runnable script thanks to the `if __name__ == "__main__":` guard.

🧱 **Analogy — the LEGO workshop.** You could carve every brick from raw plastic, or you could reach for the bins of ready-made bricks sorted by shape and color. The standard library is that wall of bins: wheels, windows, hinges — each labeled and quality-checked. Your own modules are the custom sub-assemblies you build once (a car chassis, a castle gate) and then snap into many bigger models without rebuilding them each time.

## Why it matters

- **Stop rewriting solved problems.** Need statistics, dates, randomness, or JSON? The standard library already handles edge cases you'd rather not rediscover.
- **Grow without chaos.** Splitting a big script into focused modules (`data.py`, `model.py`, `plot.py`) keeps each file readable and lets teammates work in parallel.
- **AI / career hook.** Real ML code is `import numpy as np` on line one. Knowing import styles, aliases, and the `__main__` guard is the baseline for reading any open-source repo or Kaggle notebook.

## How it works

Picture the import machine in four moves:

1. `import x` finds `x.py` (or a package folder), runs it once, and caches it in `sys.modules`.
2. Names inside become attributes: `x.thing`. Nothing leaks into your file uninvited.
3. `from x import y` runs the same load but binds just `y` into your namespace for direct use.
4. `import x as alias` binds the whole module under a shorter name, like `np` or `J`.
5. When Python runs a file directly, it sets `__name__` to `"__main__"`; when the file is imported, `__name__` is the module name — which is exactly what the guard checks.

```text
your_script.py → import math → load + cache → math.pi / math.sqrt()
               → from x import y → bind y directly
               → __name__ == "__main__"? run demo : stay quiet
```

## Key concepts

- **Plain import** — `import math` then `math.sqrt(81)` keeps things namespaced and clear.
- **Direct import** — `from statistics import mean` lets you call `mean([1, 2, 3])` with no prefix.
- **Alias import** — `import json as J` shortens long names; `J.dumps({"a": 1})` is the classic move.
- **Standard library** — `import random, datetime, collections` covers dice rolls, dates, and counters.
- **Explore a module** — `print(dir(math))` lists everything a module offers.
- **The main guard** — `if __name__ == "__main__":` runs demo code only as a script, not on import.
- **Packages group modules** — `import pkg.module` addresses a module inside a folder with dots.
- **Cache, not re-run** — Python imports each module once; re-importing reuses the cached version.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import math
import random
from datetime import date

print(math.pi)                 # 3.141592653589793
print(math.factorial(5))       # 120

random.seed(0)                 # make randomness repeatable for demos
print(random.randint(1, 6))    # a dice roll
print(random.choice(["a", "b", "c"]))

print(date.today().year >= 2020)   # True
```

The walkthrough: `math.pi` and `math.factorial(5)` show namespaced access to a full module. Seeding `random` with `0` makes the dice roll and the `choice()` repeatable, which is gold for demos and debugging. Finally `from datetime import date` pulls just one class into the namespace so `date.today()` reads naturally.

Keep exploring in `notes.py` — Example 2 is **"Different import styles"** (whole-module vs. `from`-imports vs. aliases with `statistics`, `json`, and `string`), and Example 3 is **"The `__name__` guard (module vs script)"** (a `greet()` function that only demos itself when run directly).

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

⏳ 2-minute experiment: predict what each `print` outputs, then run to verify. Next, remove the `if __name__ == "__main__":` line (keeping its body) and reason about what would change if someone *imported* your file instead of running it:

```python
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("world"))
    print("Running as a script.")
```

No solution here — test both the run and the import mental model.

## Common mistakes & gotchas

- ⚠️ `from module import *` dumps everything into your namespace and can clash — avoid it.
- ⚠️ Naming your file the same as a stdlib module (e.g. `random.py`) shadows the real one.
- ⚠️ Circular imports (A imports B which imports A) cause errors — restructure your modules.
- ⚠️ Forgetting `if __name__ == '__main__':` makes your demo code run when the file is imported.
- ⚠️ Re-importing doesn't re-run a module; Python caches it. Restart or use importlib.reload to refresh.

## Cheat sheet

```python
import math
import json as J
from statistics import mean
print(math.sqrt(81))
print(J.dumps({"a": 1}))
print(mean([10, 20, 30]))
if __name__ == "__main__":
    print("run as script")
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

You'll pull square roots, seed randomness, average lists, serialize JSON, count letters with `Counter`, and write your own `__main__` guard.

## What's next

Bricks sorted and stacked? Step into [`../17-virtual-environments/`](../17-virtual-environments/) — where each project gets its own isolated toolbox so dependency versions never fight again.

# 16 — Modules and Packages

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **module** is just a `.py` file you can import to reuse its code. A **package** is a folder of modules (historically marked by an `__init__.py`). Python ships a huge **standard library** (math, random, os, json, datetime...). You import with `import x`, `from x import y`, or `import x as alias`.

## Why it matters

You don't write everything from scratch — you stand on the shoulders of the standard library and third-party packages. Organizing your own code into modules keeps projects maintainable as they grow.

## Key concepts

- **import x** — Loads a module; access its contents as `x.thing`.
- **from x import y** — Pulls a specific name into your namespace: use `y` directly.
- **import x as alias** — Rename on import: `import numpy as np`.
- **Standard library** — Batteries included: math, random, os, sys, json, datetime, collections...
- **__name__ == '__main__'** — True only when the file is run directly, not imported.
- **Package** — A directory of modules; import submodules with dots: `pkg.module`.

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

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ `from module import *` dumps everything into your namespace and can clash — avoid it.
- ⚠️ Naming your file the same as a stdlib module (e.g. `random.py`) shadows the real one.
- ⚠️ Circular imports (A imports B which imports A) cause errors — restructure your modules.
- ⚠️ Forgetting `if __name__ == '__main__':` makes your demo code run when the file is imported.
- ⚠️ Re-importing doesn't re-run a module; Python caches it. Restart or use importlib.reload to refresh.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


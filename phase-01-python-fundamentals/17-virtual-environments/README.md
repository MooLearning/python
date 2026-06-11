# 17 — Virtual Environments

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **virtual environment** is an isolated, per-project copy of Python and its installed packages. You create one with `python -m venv .venv`, **activate** it, then `pip install` packages that live ONLY inside that project. This stops different projects from fighting over package versions.

## Why it matters

Project A might need pandas 1.x while Project B needs 2.x. Installing globally creates conflicts and 'works on my machine' chaos. Virtual environments + a `requirements.txt` make your projects reproducible — essential for real ML work and collaboration.

## Key concepts

- **venv** — Built-in tool: `python -m venv .venv` creates an isolated environment folder.
- **Activation** — `source .venv/bin/activate` (mac/Linux) or `.venv\Scripts\activate` (Windows).
- **pip freeze** — Lists installed packages with versions: `pip freeze > requirements.txt`.
- **requirements.txt** — A text list of dependencies; `pip install -r requirements.txt` reinstalls them.
- **Isolation** — Packages install into the active env, not system-wide.
- **sys.prefix** — Shows which environment Python is currently using.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import sys
import os

# When a venv is active, sys.prefix differs from sys.base_prefix
in_venv = sys.prefix != sys.base_prefix
print("Running inside a virtual environment?", in_venv)
print("Environment path (sys.prefix):", sys.prefix)

# The VIRTUAL_ENV env var is set by activation scripts
print("VIRTUAL_ENV =", os.environ.get("VIRTUAL_ENV", "(not set)"))
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Creating a venv isn't enough — you must ACTIVATE it each new terminal session.
- ⚠️ If `pip install` seems to go to the wrong place, your venv probably isn't active; check `which python`.
- ⚠️ Add `.venv/` to `.gitignore` — never commit the environment; commit `requirements.txt` instead.
- ⚠️ `pip freeze` captures EXACT versions; great for reproducibility but pin thoughtfully for libraries.
- ⚠️ Activating in one terminal doesn't affect others — each shell needs its own activation.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


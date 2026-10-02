# 17 — Virtual Environments

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

⏱️ ~20 min · 🔁 `README → notes.py → practice.md` · ⬅️ Prerequisite: `../16-modules-and-packages/`

## What is it?

A **virtual environment** is a private, per-project copy of Python plus its own installed packages. You scaffold one with `python -m venv .venv`, **activate** it so your shell points at it, and then every `pip install` lands inside that project instead of polluting your whole machine.

Activation flips two signals your tools can see: `sys.prefix` diverges from `sys.base_prefix`, and the `VIRTUAL_ENV` environment variable appears. Pair the environment with a `requirements.txt` file (made by `pip freeze`) and anyone can recreate your exact setup with one install command.

🏠 **Analogy — separate apartment kitchens.** Sharing one kitchen with five roommates means someone always moves your spices or replaces your olive oil. A virtual environment gives each project its own apartment kitchen: same stove model (Python), but its own pantry (site-packages) stocked exactly how that recipe needs it. Upgrading pandas in one apartment never ruins dinner in another, and `requirements.txt` is the grocery list you hand a friend so their kitchen matches yours.

## Why it matters

- **Version peace.** Project A needs pandas 1.x while Project B needs 2.x — separate environments let both truths coexist on one laptop.
- **Reproducibility.** A committed `requirements.txt` plus a documented Python version turns "works on my machine" into "works on every machine".
- **AI / career hook.** ML projects stack heavy, fussy dependencies (numpy, torch, transformers). Hiring managers and teammates expect you to isolate them per project and never `sudo pip install` into system Python.

## How it works

The lifecycle is five shell moves plus one Python check:

1. **Create** — `python -m venv .venv` copies Python and makes an empty package folder.
2. **Activate** — `source .venv/bin/activate` (mac/Linux) or `.venv\Scripts\Activate.ps1` (Windows) points your shell at it.
3. **Install** — `pip install requests pandas` drops packages only into the active env.
4. **Record** — `pip freeze > requirements.txt` snapshots exact versions for sharing.
5. **Leave / restore** — `deactivate` exits; later, `pip install -r requirements.txt` rebuilds the same pantry.

```text
create (.venv/) → activate → pip install → freeze → deactivate
                       ↓
              sys.prefix != sys.base_prefix (in a venv!)
```

## Key concepts

- **Create with venv** — `python -m venv .venv` builds the isolated folder (standard library, no install needed).
- **Activate per shell** — `source .venv/bin/activate` reroutes `python` and `pip` for that terminal only.
- **Check your Python** — `sys.executable` prints which interpreter is actually running your code.
- **Detect the env** — `sys.prefix != sys.base_prefix` is `True` only inside an active venv.
- **Read the flag** — `os.environ.get("VIRTUAL_ENV")` shows the active env path, or `None` outside one.
- **Snapshot versions** — `pip freeze > requirements.txt` writes every pinned dependency to a file.
- **Rebuild anywhere** — `pip install -r requirements.txt` recreates the same environment on a new machine.
- **Never commit .venv** — the folder is huge and OS-specific; version the recipe (`requirements.txt`), not the kitchen.

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

The walkthrough: comparing `sys.prefix` to `sys.base_prefix` is the canonical in-Python venv test — equal means system Python, different means isolated. Printing `sys.prefix` shows *which* environment is active, and `os.environ.get("VIRTUAL_ENV", "(not set)")` reads the marker the activation script sets, defaulting gracefully when you forgot to activate.

Continue in `notes.py` — Example 2 is **"The typical workflow (these are shell commands, shown as text)"** (create → activate → install → freeze → deactivate as printable steps), and Example 3 is **"Inspect installed packages from Python"** (listing distributions with `importlib.metadata`).

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

⏳ 2-minute detective work: run the snippet below twice — once normally and once after activating any venv (create one if needed). Predict how each of the three lines changes between runs, especially what happens to `VIRTUAL_ENV` when no venv is active:

```python
import sys
import os
print(sys.prefix != sys.base_prefix)
print(sys.executable)
print(os.environ.get("VIRTUAL_ENV", "(not set)"))
```

No solution here — compare the two outputs side by side and explain the difference to yourself.

## Common mistakes & gotchas

- ⚠️ Creating a venv isn't enough — you must ACTIVATE it each new terminal session.
- ⚠️ If `pip install` seems to go to the wrong place, your venv probably isn't active; check `which python`.
- ⚠️ Add `.venv/` to `.gitignore` — never commit the environment; commit `requirements.txt` instead.
- ⚠️ `pip freeze` captures EXACT versions; great for reproducibility but pin thoughtfully for libraries.
- ⚠️ Activating in one terminal doesn't affect others — each shell needs its own activation.

## Cheat sheet

```python
import sys
import os
print(sys.prefix != sys.base_prefix)
print(sys.executable)
print(os.environ.get("VIRTUAL_ENV", "no venv active"))
print(sys.prefix)
import importlib.metadata as meta
print(len(list(meta.distributions())))
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

You'll detect an active venv, rehearse the create/activate/freeze/install commands, read `VIRTUAL_ENV`, justify `.gitignore`, and confirm your interpreter with `sys.executable`.

Tip: keep one terminal tab per project, each with its own env activated — your future self will thank you.

## What's next

Kitchens separated and grocery lists written? Level up to [`../../phase-02-intermediate-python/18-oop-classes-and-objects/`](../../phase-02-intermediate-python/18-oop-classes-and-objects/) — Phase 2 begins with classes and objects, where your organized, isolated Python finally starts modeling the real world.

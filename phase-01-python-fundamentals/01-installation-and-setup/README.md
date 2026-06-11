# 01 — Installation and Setup

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

Before you can write Python, you need three things on your computer: the **Python interpreter** (the program that runs your code), a **code editor** (most people use VS Code), and **pip** (Python's package installer, which comes bundled with modern Python). You write code in `.py` files and run them, or you type code line-by-line in the interactive shell (the REPL).

## Why it matters

Everything in this entire roadmap depends on a working Python install. Getting comfortable with running scripts, using the REPL, and installing packages with pip now will save you hours of confusion later.

## Key concepts

- **Interpreter** — The `python`/`python3` program that reads and executes your code.
- **REPL** — Read-Eval-Print-Loop: type `python` with no file to get an interactive shell.
- **Script** — A `.py` file you run with `python myfile.py`.
- **pip** — Installs third-party packages: `pip install numpy`.
- **PATH** — The OS setting that lets you type `python` from any folder.
- **IDE / VS Code** — An editor with autocompletion, debugging and a built-in terminal.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import sys       # info about the Python interpreter
import platform  # info about your operating system

# sys.version is a string describing the running interpreter
print("Python version:", sys.version.split()[0])

# Where is the python executable that is running this file?
print("Interpreter path:", sys.executable)

# What OS are you on?
print("Operating system:", platform.system(), platform.release())
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ On macOS/Linux the command is often `python3` (and `pip3`), not `python`. On Windows use `py`.
- ⚠️ `pip install x` installs for ONE Python. If you have several Pythons, packages can 'go missing'. Use `python -m pip install x` to be sure.
- ⚠️ Forgetting to SAVE the file before running it — you then run the old version.
- ⚠️ ‘python’ not found usually means Python isn't on your PATH; re-run the installer and tick 'Add to PATH'.
- ⚠️ Don't name your file the same as a module you import (e.g. `random.py`) — Python will import your file instead of the real module.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


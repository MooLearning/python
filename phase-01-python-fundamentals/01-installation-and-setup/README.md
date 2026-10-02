# 01 — Installation and Setup

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

*⏱️ ~20 min · Loop: `README → notes.py → practice.md` · Prerequisite: none — start here, this is topic 01.*

## What is it?

To run Python you need three pieces working together: the **interpreter** (the `python` / `python3`
program that actually executes your code), a **code editor** (VS Code is the default choice in this
repo), and **pip** (the package installer that ships with modern Python). You write code either as a
saved `.py` **script** that runs top to bottom, or line by line in the interactive **REPL** you get by
typing `python` with no filename.

Think of the interpreter as the engine, your `.py` file as the route map, and the REPL as a test
track. The editor is where you draw the map, pip is how you bolt on extra parts, and `PATH` is the
signpost system that lets your terminal find the engine from any folder.

Think of moving into a new workshop before building anything. You would not start sawing wood before
checking the power works, laying out your workbench, and learning where the supply store is. That is
exactly what this topic is: plugging in the interpreter, arranging VS Code, confirming `pip` works,
and running your first script so every later topic starts on solid ground.

## Why it matters

- Every later topic assumes you can create a file, run it with `python notes.py`, read the traceback
  when it fails, and install a package with `pip install <name>` without guessing which Python got it.
- The REPL is your fastest feedback loop: test one line of syntax, inspect a value with `type()` or
  `dir()`, and confirm a stdlib module imports — all in seconds, without creating a file.
- Career hook: Python/AI work lives in environments — interpreters, virtual envs, package versions.
  Engineers who can answer "which Python am I running, and where did this package install?" debug
  deployment and notebook issues far faster than those who cannot.

## How it works

Mental model — code goes from text to result in four steps:

1. **Write** code in a `.py` file (or type one line into the REPL).
2. **Run** it with `python <file>.py` — the OS finds the interpreter via `PATH`.
3. **Interpret** — Python parses your text, compiles it to bytecode, and the interpreter executes it.
4. **Output** — `print()` results appear in the terminal; `pip` fetches extra libraries on demand.

Tiny map of the flow:

```text
[hello.py] --(python hello.py)--> [interpreter] --> terminal output
                                        ^
                                        | pip install numpy
                                   [package index]
```

Check each link when something breaks: file saved? right `python`? package installed for *that* Python?

## Key concepts

- **Interpreter** — the program that runs code: check it with `python --version`.
- **REPL** — interactive shell from bare `python`; great for `2 + 2` or `import math` experiments.
- **Script** — a saved file run top to bottom: `python hello.py`.
- **pip** — installs packages, e.g. `pip install numpy`; safest form is `python -m pip install numpy`.
- **PATH** — OS lookup list so `python` works anywhere; "not found" means PATH is misconfigured.
- **`sys` module** — lets code inspect itself: `sys.version` and `sys.executable` name your runtime.
- **`platform` module** — reports the OS: `platform.system()` returns `'Darwin'`, `'Linux'`, or `'Windows'`.
- **Standard library** — modules like `math` and `statistics` ship with Python, no `pip` needed.
- **Editor (VS Code)** — autocompletion, integrated terminal, and debugger around the same interpreter.

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

This is Example 1 from `notes.py` — it interrogates the runtime itself instead of printing fixed
text. `sys.version.split()[0]` grabs just the `3.x.y` number, `sys.executable` shows *which* Python
is running (vital when several are installed), and `platform` names the OS underneath.

Keep going in `notes.py`: Example 2 ("Your first script") saves and runs a tiny `hello.py`-style
greeting, and Example 3 ("Confirm a standard-library module loads") proves `math` and `statistics`
import with no `pip` step and computes `math.sqrt(144)`.

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

Two-minute challenge (predict before you run, no peeking at the answer): open a REPL with `python`
(or `python3`), type `import sys` then `sys.executable`, and guess what it prints. Now create a file
named `whereami.py` containing `import sys; print(sys.executable)` and run it with
`python whereami.py`. Do both print the same path? Tinker: what changes if you run the file from a
different folder, or with `python3` instead of `python`?

## Common mistakes & gotchas

- ⚠️ On macOS/Linux the command is often `python3` (and `pip3`), not `python`. On Windows use `py`.
- ⚠️ `pip install x` installs for ONE Python. If you have several Pythons, packages can 'go missing'. Use `python -m pip install x` to be sure.
- ⚠️ Forgetting to SAVE the file before running it — you then run the old version.
- ⚠️ 'python' not found usually means Python isn't on your PATH; re-run the installer and tick 'Add to PATH'.
- ⚠️ Don't name your file the same as a module you import (e.g. `random.py`) — Python will import your file instead of the real module.

## Cheat sheet

```python
import sys; print(sys.version.split()[0])  # version number only
import sys; print(sys.executable)   # path of the running interpreter
import platform; print(platform.system())  # OS name
import math; print(math.sqrt(144))  # stdlib needs no pip install
import statistics; print(statistics.mean([1, 2, 3]))  # also stdlib
print("Hello,", "learner" + "!")    # your first script output
print(sys.path[0])                     # folder Python runs from
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

## What's next

Head to [`../02-variables-and-data-types/`](../02-variables-and-data-types/) to give your working
setup something to remember — names, numbers, text, and truth values.

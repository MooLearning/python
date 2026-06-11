# 15 — File Handling

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

File handling lets your program **read from** and **write to** files on disk. The modern way is the `with open(path, mode) as f:` block, which automatically closes the file for you. Modes: `'r'` read, `'w'` write (overwrites!), `'a'` append, `'r+'` read/write. Always pass `encoding='utf-8'` for text.

## Why it matters

Programs need to persist data — config, logs, datasets, results. Reading CSVs for data science, saving model outputs, processing text files: all start with file handling. The `with` pattern prevents the classic 'forgot to close the file' resource leak.

## Key concepts

- **open(path, mode)** — Opens a file; returns a file object. Pair with `with` to auto-close.
- **with statement** — `with open(...) as f:` closes the file even if an error occurs.
- **Modes** — 'r' read, 'w' overwrite, 'a' append, 'x' create-new, add 'b' for binary.
- **read / readline / readlines** — Whole file / one line / list of lines. Or just iterate the file.
- **write / writelines** — Write a string / a list of strings (you add newlines yourself).
- **encoding** — Use encoding='utf-8' for text to avoid platform-dependent bugs.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import os
path = "demo.txt"

# WRITE mode 'w' creates (or OVERWRITES) the file
with open(path, "w", encoding="utf-8") as f:
    f.write("first line\n")
    f.write("second line\n")

# READ the whole file
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
print(content)

os.remove(path)   # clean up the demo file
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Mode `'w'` ERASES the file's contents immediately. Use `'a'` to add without losing data.
- ⚠️ Always use `with open(...)` so the file is closed automatically — even when an error occurs.
- ⚠️ `f.read()` loads the WHOLE file into memory; for big files iterate line by line instead.
- ⚠️ Lines from a file keep their trailing `\n`; call `.strip()` when you don't want it.
- ⚠️ Without `encoding='utf-8'`, behavior differs across operating systems and can corrupt text.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


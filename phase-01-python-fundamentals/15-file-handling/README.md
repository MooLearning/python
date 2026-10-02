# 15 — File Handling

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

⏱️ ~30 min · 🔁 `README → notes.py → practice.md` · ⬅️ Prerequisite: `../14-exception-handling/`

## What is it?

File handling is how your program talks to the disk — **reading** data in and **writing** results out. The modern pattern is the context manager `with open(path, mode, encoding="utf-8") as f:`, which opens the file, hands you a file object, and closes it automatically even if an error interrupts you.

The `mode` picks the attitude: `'r'` reads, `'w'` writes (creating or overwriting), `'a'` appends without erasing, and `'b'` switches to binary for images or model weights. Text files yield strings line by line, so you choose between slurping everything with `f.read()` or streaming lazily with `for line in f:`.

📓 **Analogy — the library checkout desk.** Borrowing a book means checking it out, reading it, and returning it — forget the return and someone else can't use it. `open()` is the checkout, the file object is the book in your hands, and the `with` block is the ultra-reliable librarian who reshelves it for you even if you storm out mid-chapter. Picking `'w'` versus `'a'` is like choosing between replacing the notebook's pages and simply continuing on the next blank one.

## Why it matters

- **Persistence.** Config files, logs, scraped pages, experiment results — anything that must survive after the program exits lives in a file first.
- **Data work.** Reading CSVs, line-delimited JSON, and plain-text datasets is step zero of almost every Python data or ML task; writing cleaned output is step one.
- **AI / career hook.** Training scripts read datasets, write checkpoints, and append logs. Knowing streaming reads, encodings, and `FileNotFoundError` handling keeps thousand-file pipelines from choking on file ten.

## How it works

The mental model is open → use → auto-close:

1. `open(path, mode, encoding="utf-8")` asks the OS for the file and returns a file object.
2. Inside the `with` block you `read()` / iterate (input) or `write()` (output).
3. Leaving the `with` block — normally or via exception — closes the file and flushes writes to disk.
4. The cursor moves as you read or write, so a second `read()` without rewinding returns what's left.
5. Missing files raise `FileNotFoundError` on read; `'w'` and `'a'` instead create the file if needed.

```text
with open(path, mode) as f: → read / write → [error?] → auto-close
```

## Key concepts

- **Open with a mode** — `open("a.txt", "r", encoding="utf-8")` picks read, write, append, or create.
- **Auto-close with with** — `with open("a.txt") as f:` guarantees the file closes, even on error.
- **Read it all** — `content = f.read()` slurps the whole file into one string.
- **Stream line by line** — `for line in f:` is memory-friendly for huge logs and datasets.
- **Split lines** — `lines = f.readlines()` returns a list with trailing `\n` still attached.
- **Write strings** — `f.write("hello\n")` writes exactly what you pass; you own the newlines.
- **Append, don't erase** — `open("log.txt", "a", encoding="utf-8")` adds to the end safely.
- **Always set encoding** — `encoding="utf-8"` keeps text consistent across macOS, Linux, and Windows.

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

The walkthrough: the first `with` block opens `demo.txt` in `'w'` mode, creating it fresh and writing two lines. The second block reopens it in `'r'` mode and `f.read()` pulls everything back into `content` for printing. The final `os.remove(path)` deletes the demo so repeated runs start clean — a handy habit for throwaway examples.

Next in `notes.py`: Example 2 is **"Appending and reading line by line"** (growing `log.txt` with `'a'` and streaming it with `enumerate`), and Example 3 is **"Safe reading with error handling"** (a `FileNotFoundError` fallback plus summing numbers from a file).

Run every example in this topic with:

```bash
python notes.py
```

## Try it yourself

⏳ 2-minute prediction: this snippet writes one line, appends two more, then reads. Guess the exact printed output (including numbers and spacing) before you run it — then try swapping `'a'` to `'w'` in the second block and predict again:

```python
with open("tinker.txt", "w", encoding="utf-8") as f:
    f.write("line 1\n")
with open("tinker.txt", "a", encoding="utf-8") as f:
    f.write("line 2\n")
with open("tinker.txt", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(i, line.strip())
```

No solution here — run it, then clean up the file yourself.

## Common mistakes & gotchas

- ⚠️ Mode `'w'` ERASES the file's contents immediately. Use `'a'` to add without losing data.
- ⚠️ Always use `with open(...)` so the file is closed automatically — even when an error occurs.
- ⚠️ `f.read()` loads the WHOLE file into memory; for big files iterate line by line instead.
- ⚠️ Lines from a file keep their trailing `\n`; call `.strip()` when you don't want it.
- ⚠️ Without `encoding='utf-8'`, behavior differs across operating systems and can corrupt text.

## Cheat sheet

```python
with open("a.txt", "w", encoding="utf-8") as f:
    f.write("hi\n")
with open("a.txt", "r", encoding="utf-8") as f:
    text = f.read()
with open("a.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

You'll write and re-read files, append lines, count lines, sum numbers, survive a missing file, and filter a log for error lines.

## What's next

Comfortable checking books in and out? Continue to [`../16-modules-and-packages/`](../16-modules-and-packages/) — where you'll stop reinventing code and start importing it like a pro.

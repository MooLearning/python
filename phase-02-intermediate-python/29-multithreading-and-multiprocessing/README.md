# 29 — Multithreading and Multiprocessing

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

Two ways to do more than one thing at once. **Threads** share memory and are great for **I/O-bound** work (waiting on files, network) — but Python's **GIL** means threads don't speed up pure CPU work. **Processes** each have their own Python interpreter, so they DO use multiple CPU cores — ideal for **CPU-bound** work. `concurrent.futures` gives a simple, unified interface to both.

## Why it matters

Downloading 100 URLs, reading many files, or crunching numbers across cores: concurrency can turn minutes into seconds. Knowing the I/O-bound (threads) vs CPU-bound (processes) distinction is the key to choosing the right tool.

## Key concepts

- **GIL** — Global Interpreter Lock: only one thread runs Python bytecode at a time.
- **I/O-bound vs CPU-bound** — Waiting (network/disk) vs computing (math). Threads help the first; processes the second.
- **Thread** — Lightweight, shares memory; use threading or ThreadPoolExecutor.
- **Process** — Separate memory and interpreter; use multiprocessing or ProcessPoolExecutor.
- **concurrent.futures** — Executor.map / submit -> futures; the easiest high-level API.
- **Race conditions** — Shared mutable state across threads needs a Lock to stay consistent.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import time
from concurrent.futures import ThreadPoolExecutor

def fake_download(url):
    time.sleep(0.2)                 # pretend we're waiting on the network
    return f"{url} -> 200"

urls = [f"site{i}.com" for i in range(5)]

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(fake_download, urls))   # run concurrently
print(results)
print(f"threaded: {time.perf_counter() - start:.2f}s (≈0.2s, not 1.0s)")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Threads do NOT speed up CPU-bound Python code because of the GIL — use processes for that.
- ⚠️ multiprocessing code must be guarded by `if __name__ == '__main__':` (especially on Windows/macOS).
- ⚠️ Shared mutable state across threads without a Lock causes race conditions (lost updates).
- ⚠️ Always `join()` threads/processes (or use a `with` executor) so the program waits for them.
- ⚠️ Processes don't share memory — data is pickled to/from them, which has overhead and requires picklable objects.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


# ======================================================================
# 24 — Context Managers  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Why 'with' beats manual cleanup
# ----------------------------------------------------------------------
print("\n--- Example 1: Why 'with' beats manual cleanup ---")
# Manual way -- easy to forget close(), and a crash skips it:
f = open("demo.txt", "w", encoding="utf-8")
f.write("hi")
f.close()

# The 'with' way -- close() is GUARANTEED, even on error:
with open("demo.txt", "r", encoding="utf-8") as f:
    print(f.read())     # hi
# file is now closed automatically
print("closed?", f.closed)   # True

import os
os.remove("demo.txt")

# ----------------------------------------------------------------------
# Example 2: Writing a context manager with a class
# ----------------------------------------------------------------------
print("\n--- Example 2: Writing a context manager with a class ---")
class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self                      # value bound to 'as'
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.perf_counter() - self.start
        print(f"Block took {self.elapsed*1000:.2f} ms")
        return False                     # False = don't suppress exceptions

with Timer() as t:
    total = sum(range(1_000_000))
print("result:", total)

# ----------------------------------------------------------------------
# Example 3: The easy way: @contextmanager
# ----------------------------------------------------------------------
print("\n--- Example 3: The easy way: @contextmanager ---")
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")     # setup (everything before yield)
    yield                  # the 'with' block runs here
    print(f"</{name}>")    # cleanup (everything after yield)

with tag("p"):
    print("hello")
# Output:
# <p>
# hello
# </p>

# Cleanup still runs if the block raises -- wrap yield in try/finally for that:
@contextmanager
def safe_open(path, mode):
    f = open(path, mode, encoding="utf-8")
    try:
        yield f
    finally:
        f.close()          # always runs

with safe_open("t.txt", "w") as f:
    f.write("data")
import os; os.remove("t.txt")

print("\nDone! Tip: change values above and run again to learn by experiment.")

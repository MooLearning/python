# ======================================================================
# 16 — Modules and Packages  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Importing from the standard library
# ----------------------------------------------------------------------
print("\n--- Example 1: Importing from the standard library ---")
import math
import random
from datetime import date

print(math.pi)                 # 3.141592653589793
print(math.factorial(5))       # 120

random.seed(0)                 # make randomness repeatable for demos
print(random.randint(1, 6))    # a dice roll
print(random.choice(["a", "b", "c"]))

print(date.today().year >= 2020)   # True

# ----------------------------------------------------------------------
# Example 2: Different import styles
# ----------------------------------------------------------------------
print("\n--- Example 2: Different import styles ---")
# 1) import the whole module
import statistics
print(statistics.mean([2, 4, 6]))      # 4

# 2) import specific names (use them directly)
from statistics import median, mode
print(median([1, 3, 5, 7]))            # 4.0

# 3) import with an alias (very common in data science)
import json as J
print(J.dumps({"ok": True}))           # {"ok": true}

# Explore what a module offers
import string
print(string.ascii_lowercase)          # abcdefghijklmnopqrstuvwxyz

# ----------------------------------------------------------------------
# Example 3: The __name__ guard (module vs script)
# ----------------------------------------------------------------------
print("\n--- Example 3: The __name__ guard (module vs script) ---")
# This pattern lets a file work BOTH as an importable module AND a script.
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Runs only when you do `python thisfile.py`,
    # NOT when another file does `import thisfile`.
    print(greet("world"))
    print("Running as a script.")

print("\nDone! Tip: change values above and run again to learn by experiment.")

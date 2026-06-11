# ======================================================================
# 15 — File Handling  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Writing and reading a text file
# ----------------------------------------------------------------------
print("\n--- Example 1: Writing and reading a text file ---")
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

# ----------------------------------------------------------------------
# Example 2: Appending and reading line by line
# ----------------------------------------------------------------------
print("\n--- Example 2: Appending and reading line by line ---")
import os
path = "log.txt"

with open(path, "w", encoding="utf-8") as f:
    f.write("line 1\n")

# APPEND mode 'a' adds to the end without erasing
with open(path, "a", encoding="utf-8") as f:
    f.write("line 2\n")
    f.write("line 3\n")

# Iterating a file yields one line at a time (memory friendly)
with open(path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(i, line.strip())   # strip removes the trailing \n

os.remove(path)

# ----------------------------------------------------------------------
# Example 3: Safe reading with error handling
# ----------------------------------------------------------------------
print("\n--- Example 3: Safe reading with error handling ---")
def read_or_default(path, default="(no file)"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return default

print(read_or_default("does_not_exist.txt"))   # (no file)

# Read all lines into a list
import os
with open("nums.txt", "w", encoding="utf-8") as f:
    f.write("10\n20\n30\n")
with open("nums.txt", "r", encoding="utf-8") as f:
    numbers = [int(line) for line in f]
print("sum:", sum(numbers))    # 60
os.remove("nums.txt")

print("\nDone! Tip: change values above and run again to learn by experiment.")

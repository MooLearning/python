# ======================================================================
# 05 — Strings and Methods  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Indexing and slicing
# ----------------------------------------------------------------------
print("\n--- Example 1: Indexing and slicing ---")
s = "Python"
print(s[0])     # P    (first character, index 0)
print(s[-1])    # n    (last character)
print(s[0:3])   # Pyt  (indices 0,1,2 -- stop is excluded)
print(s[2:])    # thon (from index 2 to the end)
print(s[:2])    # Py   (start to index 1)
print(s[::-1])  # nohtyP (reverse using step -1)
print(len(s))   # 6    (number of characters)

# ----------------------------------------------------------------------
# Example 2: Essential string methods
# ----------------------------------------------------------------------
print("\n--- Example 2: Essential string methods ---")
text = "   Hello, World!   "
print(text.strip())             # 'Hello, World!'  (trim whitespace)
print(text.strip().upper())     # 'HELLO, WORLD!'
print("a,b,c".split(","))       # ['a', 'b', 'c']
print("-".join(["2026", "06", "09"]))  # '2026-06-09'
print("banana".replace("a", "o"))      # 'bonono'
print("hello".find("l"))        # 2  (index of first 'l', -1 if absent)
print("data.csv".endswith(".csv"))     # True

# ----------------------------------------------------------------------
# Example 3: Building and formatting strings
# ----------------------------------------------------------------------
print("\n--- Example 3: Building and formatting strings ---")
name = "Ada"
score = 95.5

# f-strings are the cleanest way to format
print(f"{name} scored {score:.1f}%")

# Alignment and padding inside a width
for item in ["egg", "milk", "bread"]:
    print(f"{item:<8}| ${len(item):>2}")  # left/right aligned columns

# Strings are immutable: this makes a NEW string
greeting = "hi"
louder = greeting + "!!!"
print(greeting, louder)   # original unchanged

print("\nDone! Tip: change values above and run again to learn by experiment.")

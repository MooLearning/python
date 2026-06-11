# ======================================================================
# 09 — Comprehensions  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: List comprehensions vs loops
# ----------------------------------------------------------------------
print("\n--- Example 1: List comprehensions vs loops ---")
# The loop way
squares = []
for x in range(6):
    squares.append(x * x)
print(squares)            # [0, 1, 4, 9, 16, 25]

# The comprehension way (same result, one line)
squares = [x * x for x in range(6)]
print(squares)

# With a filter: keep only evens, then square them
evens_sq = [x * x for x in range(10) if x % 2 == 0]
print(evens_sq)           # [0, 4, 16, 36, 64]

# ----------------------------------------------------------------------
# Example 2: Transforming text and conditional expressions
# ----------------------------------------------------------------------
print("\n--- Example 2: Transforming text and conditional expressions ---")
words = ["hi", "world", "ok", "python"]

# Uppercase every word
print([w.upper() for w in words])

# Keep only long words
print([w for w in words if len(w) > 2])

# if/else INSIDE the expression (note position: before 'for')
labels = ["long" if len(w) > 2 else "short" for w in words]
print(labels)             # ['short', 'long', 'short', 'long']

# ----------------------------------------------------------------------
# Example 3: Dict and set comprehensions
# ----------------------------------------------------------------------
print("\n--- Example 3: Dict and set comprehensions ---")
# Dict comprehension: number -> its square
sq_map = {n: n * n for n in range(1, 6)}
print(sq_map)             # {1:1, 2:4, 3:9, 4:16, 5:25}

# Invert a dict (swap keys and values)
prices = {"apple": 3, "pear": 5}
by_price = {v: k for k, v in prices.items()}
print(by_price)           # {3: 'apple', 5: 'pear'}

# Set comprehension: unique remainders
print({n % 3 for n in range(10)})   # {0, 1, 2}

print("\nDone! Tip: change values above and run again to learn by experiment.")

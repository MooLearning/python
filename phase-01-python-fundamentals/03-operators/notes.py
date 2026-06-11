# ======================================================================
# 03 — Operators  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Arithmetic operators
# ----------------------------------------------------------------------
print("\n--- Example 1: Arithmetic operators ---")
a, b = 17, 5
print("add ", a + b)    # 22
print("sub ", a - b)    # 12
print("mul ", a * b)    # 85
print("div ", a / b)    # 3.4   (float)
print("floor", a // b)  # 3     (drops the decimal)
print("mod ", a % b)    # 2     (remainder)
print("pow ", a ** b)   # 1419857

# ----------------------------------------------------------------------
# Example 2: Comparison and logical operators
# ----------------------------------------------------------------------
print("\n--- Example 2: Comparison and logical operators ---")
x = 7
# Comparisons return booleans
print(x > 5)          # True
print(x == 10)        # False

# Combine conditions with and / or / not
print(x > 5 and x < 10)   # True  (both must be true)
print(x < 0 or x > 100)   # False (neither is true)
print(not (x == 7))       # False

# Python lets you "chain" comparisons like math
print(0 < x < 10)         # True

# ----------------------------------------------------------------------
# Example 3: Assignment shortcuts and bitwise basics
# ----------------------------------------------------------------------
print("\n--- Example 3: Assignment shortcuts and bitwise basics ---")
score = 0
score += 10   # same as score = score + 10
score *= 2    # now 20
print("score:", score)

# Bitwise works on binary representations
print(5 & 3)   # 1   (101 & 011 = 001)
print(5 | 3)   # 7   (101 | 011 = 111)
print(5 ^ 3)   # 6   (XOR)
print(1 << 4)  # 16  (shift bits left = multiply by 2**4)

print("\nDone! Tip: change values above and run again to learn by experiment.")

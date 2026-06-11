# ======================================================================
# 04 — Input, Output and Type Casting  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: print with sep, end, and f-strings
# ----------------------------------------------------------------------
print("\n--- Example 1: print with sep, end, and f-strings ---")
name = "Ada"
age = 36

# f-strings: put variables inside {curly braces}
print(f"{name} is {age} years old.")

# sep controls what goes BETWEEN items; end controls what goes at the END
print("a", "b", "c", sep="-")        # a-b-c
print("no newline here ->", end=" ")
print("...continued on same line")

# Format numbers: 2 decimal places
pi = 3.14159
print(f"pi is about {pi:.2f}")        # pi is about 3.14

# ----------------------------------------------------------------------
# Example 2: Reading input is always a string
# ----------------------------------------------------------------------
print("\n--- Example 2: Reading input is always a string ---")
# NOTE: input() pauses for typing. Here we simulate it so the file runs anywhere.
def input(_prompt=""):           # remove this line to use real keyboard input
    return "42"                  # pretend the user typed 42

raw = input("Enter a number: ")
print("raw value:", raw, "type:", type(raw))   # it's a str!

number = int(raw)                # cast text -> integer
print("number + 8 =", number + 8)              # now math works

# ----------------------------------------------------------------------
# Example 3: Casting between types (and what breaks)
# ----------------------------------------------------------------------
print("\n--- Example 3: Casting between types (and what breaks) ---")
print(int("100") + 1)     # 101  -> str of digits -> int
print(float("3.5") * 2)   # 7.0  -> str -> float
print(str(2026) + "!")    # 2026! -> int -> str so we can concatenate
print(int(9.9))           # 9    -> float -> int TRUNCATES (does not round)
print(bool(0), bool(""), bool(3))  # False False True

print("\nDone! Tip: change values above and run again to learn by experiment.")

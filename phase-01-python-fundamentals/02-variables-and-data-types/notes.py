# ======================================================================
# 02 — Variables and Data Types  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Creating variables and checking their types
# ----------------------------------------------------------------------
print("\n--- Example 1: Creating variables and checking their types ---")
age = 25            # int  (whole number)
price = 19.99       # float (decimal)
name = "Ada"        # str  (text)
is_student = True   # bool (True/False)
nothing = None      # NoneType (absence of a value)

# type() tells you the data type of a value
print(age, "->", type(age))
print(price, "->", type(price))
print(name, "->", type(name))
print(is_student, "->", type(is_student))
print(nothing, "->", type(nothing))

# ----------------------------------------------------------------------
# Example 2: Variables are dynamic and can be reassigned
# ----------------------------------------------------------------------
print("\n--- Example 2: Variables are dynamic and can be reassigned ---")
x = 10
print(x, type(x))   # int

x = "now I am text"
print(x, type(x))   # str  -- same name, new type, no error

# Multiple assignment at once
a, b, c = 1, 2, 3
print("a, b, c =", a, b, c)

# Swap values without a temp variable (a classic Python trick)
a, b = b, a
print("after swap:", a, b)

# ----------------------------------------------------------------------
# Example 3: Numbers behave like math; watch int vs float
# ----------------------------------------------------------------------
print("\n--- Example 3: Numbers behave like math; watch int vs float ---")
print(7 + 3)      # 10   (int + int -> int)
print(7 / 2)      # 3.5  (/ ALWAYS gives a float)
print(7 // 2)     # 3    (// is floor division -> int here)
print(2 ** 10)    # 1024 (** is power)
print(0.1 + 0.2)  # 0.30000000000000004  (floats are approximate!)

print("\nDone! Tip: change values above and run again to learn by experiment.")

# ======================================================================
# 14 — Exception Handling  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Catching specific exceptions
# ----------------------------------------------------------------------
print("\n--- Example 1: Catching specific exceptions ---")
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Can't divide by zero!")
        return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # message, then None

# Catch different errors differently
for value in ["42", "oops"]:
    try:
        print("parsed:", int(value))
    except ValueError as e:
        print("Bad number:", e)

# ----------------------------------------------------------------------
# Example 2: else and finally
# ----------------------------------------------------------------------
print("\n--- Example 2: else and finally ---")
def read_config(text):
    try:
        number = int(text)
    except ValueError:
        print("Not a valid integer")
    else:
        print("Success! Got", number)   # only if no exception
    finally:
        print("done checking")           # always runs

read_config("100")
print("---")
read_config("nope")

# ----------------------------------------------------------------------
# Example 3: Raising your own exceptions
# ----------------------------------------------------------------------
print("\n--- Example 3: Raising your own exceptions ---")
def set_age(age):
    if age < 0:
        raise ValueError(f"age can't be negative: {age}")
    return age

print(set_age(30))     # 30
try:
    set_age(-5)
except ValueError as e:
    print("Rejected:", e)

# You can catch multiple types at once
try:
    data = {"a": 1}
    print(data["z"])
except (KeyError, TypeError) as e:
    print("Lookup failed:", repr(e))

print("\nDone! Tip: change values above and run again to learn by experiment.")

# ======================================================================
# 06 — Conditional Statements  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Basic if / elif / else
# ----------------------------------------------------------------------
print("\n--- Example 1: Basic if / elif / else ---")
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:        # only checked if the previous test was False
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)   # B

# ----------------------------------------------------------------------
# Example 2: Truthiness and combined conditions
# ----------------------------------------------------------------------
print("\n--- Example 2: Truthiness and combined conditions ---")
name = ""          # empty string is "falsy"
items = [1, 2, 3]  # non-empty list is "truthy"

if not name:
    print("Please enter your name.")

if items:
    print("You have", len(items), "items.")

age = 25
has_ticket = True
if age >= 18 and has_ticket:
    print("Welcome in!")

# ----------------------------------------------------------------------
# Example 3: Ternary expression (one-line if/else)
# ----------------------------------------------------------------------
print("\n--- Example 3: Ternary expression (one-line if/else) ---")
for n in range(1, 6):
    label = "even" if n % 2 == 0 else "odd"
    print(n, "is", label)

# Useful for choosing a value inline
temp = 30
status = "hot" if temp > 28 else "comfortable"
print(status)   # hot

print("\nDone! Tip: change values above and run again to learn by experiment.")

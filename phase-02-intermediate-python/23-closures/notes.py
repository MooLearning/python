# ======================================================================
# 23 — Closures  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: A function factory (the canonical closure)
# ----------------------------------------------------------------------
print("\n--- Example 1: A function factory (the canonical closure) ---")
def make_multiplier(factor):
    def multiply(x):
        return x * factor     # 'factor' is remembered from the enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10))   # 20
print(triple(10))   # 30
# Each closure remembers its OWN factor:
print(double.__closure__[0].cell_contents)   # 2

# ----------------------------------------------------------------------
# Example 2: Closures that hold state with nonlocal
# ----------------------------------------------------------------------
print("\n--- Example 2: Closures that hold state with nonlocal ---")
def make_counter():
    count = 0
    def increment():
        nonlocal count        # modify the enclosing variable
        count += 1
        return count
    return increment

c1 = make_counter()
c2 = make_counter()          # independent state
print(c1(), c1(), c1())      # 1 2 3
print(c2())                  # 1  (separate counter)

# ----------------------------------------------------------------------
# Example 3: The late-binding loop trap (and the fix)
# ----------------------------------------------------------------------
print("\n--- Example 3: The late-binding loop trap (and the fix) ---")
# BUG: all functions share the SAME variable i (captured by reference)
funcs_bug = []
for i in range(3):
    funcs_bug.append(lambda: i)
print([f() for f in funcs_bug])   # [2, 2, 2]  -- not [0,1,2]!

# FIX: capture the current value via a default argument
funcs_fixed = []
for i in range(3):
    funcs_fixed.append(lambda i=i: i)
print([f() for f in funcs_fixed]) # [0, 1, 2]

print("\nDone! Tip: change values above and run again to learn by experiment.")

# ======================================================================
# 12 — Scope (local, global, nonlocal)  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Local vs global
# ----------------------------------------------------------------------
print("\n--- Example 1: Local vs global ---")
x = "global"

def show():
    x = "local"          # a NEW local variable, separate from the global
    print("inside:", x)  # local

show()
print("outside:", x)     # global  -- unchanged

def reader():
    print("reading global:", x)   # OK to READ the global without 'global'
reader()

# ----------------------------------------------------------------------
# Example 2: global and nonlocal
# ----------------------------------------------------------------------
print("\n--- Example 2: global and nonlocal ---")
counter = 0

def increment():
    global counter        # without this, the next line creates a local!
    counter += 1

increment()
increment()
print("counter:", counter)   # 2

def make_adder():
    total = 0
    def add(n):
        nonlocal total     # reassign the ENCLOSING total, not a new local
        total += n
        return total
    return add

acc = make_adder()
print(acc(10))   # 10
print(acc(5))    # 15  (state remembered via the enclosing scope)

# ----------------------------------------------------------------------
# Example 3: The classic UnboundLocalError trap
# ----------------------------------------------------------------------
print("\n--- Example 3: The classic UnboundLocalError trap ---")
value = 100

def buggy():
    # Because we ASSIGN to value below, Python treats it as LOCAL everywhere
    # in this function -> reading it first raises UnboundLocalError.
    try:
        print(value)      # error: local 'value' used before assignment
        value = 1
    except UnboundLocalError as e:
        print("Caught:", e)

buggy()

def fixed():
    global value
    print(value)          # now refers to the global -> 100
    value = 1
fixed()

print("\nDone! Tip: change values above and run again to learn by experiment.")

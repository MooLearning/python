# ======================================================================
# 10 — Functions  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Defining and calling functions
# ----------------------------------------------------------------------
print("\n--- Example 1: Defining and calling functions ---")
def add(a, b):
    "Return the sum of a and b."   # docstring
    return a + b

result = add(3, 4)
print("add(3, 4) =", result)       # 7

# A function with no return gives back None
def shout(text):
    print(text.upper() + "!")

value = shout("hello")             # prints HELLO!
print("shout returned:", value)    # None

# ----------------------------------------------------------------------
# Example 2: Default values and keyword arguments
# ----------------------------------------------------------------------
print("\n--- Example 2: Default values and keyword arguments ---")
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Ada"))                    # Hello, Ada!
print(greet("Ada", "Welcome"))         # Welcome, Ada!
print(greet(greeting="Hi", name="Bo")) # keyword args -> order doesn't matter

def area(width, height):
    return width * height
print(area(height=4, width=3))         # 12

# ----------------------------------------------------------------------
# Example 3: *args and **kwargs for flexible functions
# ----------------------------------------------------------------------
print("\n--- Example 3: *args and **kwargs for flexible functions ---")
def total(*args):              # args is a tuple of everything passed
    return sum(args)
print(total(1, 2, 3, 4))       # 10

def describe(**kwargs):        # kwargs is a dict of named arguments
    for key, value in kwargs.items():
        print(f"{key} = {value}")
describe(name="Ada", role="pioneer")

# Returning multiple values (really returns a tuple)
def min_max(nums):
    return min(nums), max(nums)
low, high = min_max([4, 9, 1, 7])
print("low/high:", low, high)  # 1 9

print("\nDone! Tip: change values above and run again to learn by experiment.")

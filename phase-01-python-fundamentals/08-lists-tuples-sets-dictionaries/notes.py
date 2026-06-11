# ======================================================================
# 08 — Lists, Tuples, Sets and Dictionaries  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Lists: ordered and mutable
# ----------------------------------------------------------------------
print("\n--- Example 1: Lists: ordered and mutable ---")
nums = [3, 1, 2]
nums.append(4)         # add to end -> [3, 1, 2, 4]
nums.sort()            # sort in place -> [1, 2, 3, 4]
print(nums, "len", len(nums))
print("first/last:", nums[0], nums[-1])
print("slice:", nums[1:3])     # [2, 3]
nums.remove(2)         # remove first matching value
print("after remove:", nums)

# ----------------------------------------------------------------------
# Example 2: Tuples and sets
# ----------------------------------------------------------------------
print("\n--- Example 2: Tuples and sets ---")
# Tuple: fixed, immutable -> safe for coordinates, records
point = (3, 4)
x, y = point           # unpacking
print("x,y =", x, y)
# point[0] = 9         # would raise TypeError (immutable)

# Set: unique items, fast membership, set algebra
a = {1, 2, 3, 3, 2}
print("unique:", a)            # {1, 2, 3}
b = {3, 4, 5}
print("union:", a | b)         # {1,2,3,4,5}
print("intersection:", a & b)  # {3}
print("3 in a?", 3 in a)       # True (very fast)

# ----------------------------------------------------------------------
# Example 3: Dictionaries: key-value lookups
# ----------------------------------------------------------------------
print("\n--- Example 3: Dictionaries: key-value lookups ---")
ages = {"Ada": 36, "Linus": 54}
ages["Grace"] = 85             # add / update
print(ages["Ada"])            # 36
print(ages.get("Nobody", "?")) # safe lookup with default -> '?'

# Iterate keys, values, or both
for name, age in ages.items():
    print(f"{name} is {age}")

print("keys:", list(ages.keys()))
print("Ada known?", "Ada" in ages)   # checks KEYS

print("\nDone! Tip: change values above and run again to learn by experiment.")

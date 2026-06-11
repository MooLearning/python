# ======================================================================
# 32 — Arrays and Dynamic Arrays  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Core list operations and their costs
# ----------------------------------------------------------------------
print("\n--- Example 1: Core list operations and their costs ---")
a = [10, 20, 30, 40]
print(a[0], a[-1])         # 10 40  -> O(1) index
a.append(50)               # O(1) amortized at the end
a.insert(1, 15)            # O(n): shifts everything right -> [10,15,20,30,40,50]
print(a)
a.pop()                    # O(1): remove last
a.pop(0)                   # O(n): remove first, shifts left
print(a)                   # [15, 20, 30, 40]
print(a[1:3])              # [20, 30] -> slice copy
print(20 in a)             # O(n) membership scan -> True

# ----------------------------------------------------------------------
# Example 2: Building 2D arrays correctly
# ----------------------------------------------------------------------
print("\n--- Example 2: Building 2D arrays correctly ---")
rows, cols = 3, 4

# WRONG: every row is the SAME list object
bad = [[0] * cols] * rows
bad[0][0] = 9
print("bad  :", bad)       # the 9 appears in EVERY row!

# RIGHT: a comprehension makes independent rows
grid = [[0] * cols for _ in range(rows)]
grid[0][0] = 9
print("good :", grid)      # only row 0 changed

# Access and iterate
grid[1][2] = 5
for r in range(rows):
    print(grid[r])

# ----------------------------------------------------------------------
# Example 3: Prefix sums for fast range queries
# ----------------------------------------------------------------------
print("\n--- Example 3: Prefix sums for fast range queries ---")
nums = [3, 1, 4, 1, 5, 9, 2]

# Precompute prefix[i] = sum of nums[0:i]
prefix = [0] * (len(nums) + 1)
for i, x in enumerate(nums):
    prefix[i + 1] = prefix[i] + x

def range_sum(lo, hi):      # sum of nums[lo:hi+1] in O(1)
    return prefix[hi + 1] - prefix[lo]

print("prefix:", prefix)
print("sum[2..5] =", range_sum(2, 5))   # 4+1+5+9 = 19
print("sum[0..6] =", range_sum(0, 6))   # 25

print("\nDone! Tip: change values above and run again to learn by experiment.")

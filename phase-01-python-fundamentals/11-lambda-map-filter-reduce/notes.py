# ======================================================================
# 11 — Lambda, Map, Filter and Reduce  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: lambda and sorting with key=
# ----------------------------------------------------------------------
print("\n--- Example 1: lambda and sorting with key= ---")
double = lambda x: x * 2          # same as: def double(x): return x*2
print(double(5))                  # 10

# Real-world use: sort by a computed key
people = [("Ada", 36), ("Bo", 19), ("Cy", 54)]
by_age = sorted(people, key=lambda person: person[1])
print(by_age)                     # sorted by the age (2nd item)

words = ["banana", "kiwi", "apple"]
print(sorted(words, key=len))     # shortest to longest

# ----------------------------------------------------------------------
# Example 2: map and filter
# ----------------------------------------------------------------------
print("\n--- Example 2: map and filter ---")
nums = [1, 2, 3, 4, 5, 6]

# map: transform every item (remember to wrap in list to see it)
squares = list(map(lambda x: x * x, nums))
print(squares)                    # [1, 4, 9, 16, 25, 36]

# filter: keep items that pass the test
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)                      # [2, 4, 6]

# Often a comprehension is clearer than map/filter:
print([x * x for x in nums if x % 2 == 0])   # [4, 16, 36]

# ----------------------------------------------------------------------
# Example 3: reduce for folding values
# ----------------------------------------------------------------------
print("\n--- Example 3: reduce for folding values ---")
from functools import reduce

nums = [1, 2, 3, 4, 5]

# reduce(func, iterable): combine left-to-right into a single value
product = reduce(lambda acc, x: acc * x, nums)
print("product:", product)        # 120  (1*2*3*4*5)

total = reduce(lambda acc, x: acc + x, nums, 0)  # 0 is the start value
print("sum:", total)              # 15  (but just use sum(nums)!)

longest = reduce(lambda a, b: a if len(a) >= len(b) else b,
                 ["hi", "hello", "hey"])
print("longest:", longest)        # hello

print("\nDone! Tip: change values above and run again to learn by experiment.")

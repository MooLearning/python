# ======================================================================
# 13 — Recursion Basics  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Factorial: the 'hello world' of recursion
# ----------------------------------------------------------------------
print("\n--- Example 1: Factorial: the 'hello world' of recursion ---")
def factorial(n):
    if n <= 1:               # base case: 0! and 1! are 1
        return 1
    return n * factorial(n - 1)   # recursive case: shrink toward the base

print(factorial(5))   # 120  (5*4*3*2*1)

# Trace: factorial(3) = 3*factorial(2) = 3*2*factorial(1) = 3*2*1 = 6
print(factorial(3))   # 6

# ----------------------------------------------------------------------
# Example 2: Sum a list and reverse a string recursively
# ----------------------------------------------------------------------
print("\n--- Example 2: Sum a list and reverse a string recursively ---")
def sum_list(items):
    if not items:            # base case: empty list sums to 0
        return 0
    return items[0] + sum_list(items[1:])   # first + sum of the rest

print(sum_list([1, 2, 3, 4]))   # 10

def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]   # reverse the tail, put first char at the end

print(reverse("hello"))   # olleh

# ----------------------------------------------------------------------
# Example 3: Fibonacci, and why naive recursion can be slow
# ----------------------------------------------------------------------
print("\n--- Example 3: Fibonacci, and why naive recursion can be slow ---")
def fib(n):
    if n < 2:                # base cases: fib(0)=0, fib(1)=1
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(10)])   # 0 1 1 2 3 5 8 13 21 34

# The naive version recomputes the same values exponentially.
# 'memoization' caches results to make it fast:
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_fast(n):
    return n if n < 2 else fib_fast(n - 1) + fib_fast(n - 2)

print(fib_fast(50))   # 12586269025  (instant, thanks to caching)

print("\nDone! Tip: change values above and run again to learn by experiment.")

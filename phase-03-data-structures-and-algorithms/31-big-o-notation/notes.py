# ======================================================================
# 31 — Big-O Notation  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Counting operations for different complexities
# ----------------------------------------------------------------------
print("\n--- Example 1: Counting operations for different complexities ---")
def constant(n):          # O(1): work doesn't depend on n
    return n * 2

def linear(arr):          # O(n): one pass
    ops = 0
    for _ in arr:
        ops += 1
    return ops

def quadratic(arr):       # O(n^2): nested loops -> all pairs
    ops = 0
    for _ in arr:
        for _ in arr:
            ops += 1
    return ops

for n in (10, 100, 1000):
    data = list(range(n))
    print(f"n={n:5} | linear ops={linear(data):6} | quadratic ops={quadratic(data)}")

# ----------------------------------------------------------------------
# Example 2: Timing: linear vs quadratic growth
# ----------------------------------------------------------------------
print("\n--- Example 2: Timing: linear vs quadratic growth ---")
import time

def time_it(fn, data):
    start = time.perf_counter()
    fn(data)
    return (time.perf_counter() - start) * 1000   # ms

def find_dupes_slow(arr):     # O(n^2)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

def has_dupes_fast(arr):      # O(n) using a set
    seen = set()
    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False

data = list(range(2000))      # no duplicates -> worst case
print(f"O(n^2): {time_it(find_dupes_slow, data):.1f} ms")
print(f"O(n)  : {time_it(has_dupes_fast, data):.3f} ms")

# ----------------------------------------------------------------------
# Example 3: Why we drop constants and lower-order terms
# ----------------------------------------------------------------------
print("\n--- Example 3: Why we drop constants and lower-order terms ---")
# Two algorithms doing 'n' vs '3n + 100' steps:
def a(n): return n
def b(n): return 3 * n + 100

for n in (10, 1000, 1_000_000):
    print(f"n={n:9} | a={a(n):10} | b={b(n):10} | ratio={b(n)/a(n):.3f}")
# As n grows huge, the ratio approaches the constant 3 and the +100 vanishes.
# So both are O(n): the GROWTH SHAPE is what matters, not the constants.

print("\nDone! Tip: change values above and run again to learn by experiment.")

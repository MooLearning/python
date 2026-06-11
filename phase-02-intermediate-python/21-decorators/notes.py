# ======================================================================
# 21 — Decorators  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Your first decorator
# ----------------------------------------------------------------------
print("\n--- Example 1: Your first decorator ---")
import functools

def shout(func):
    @functools.wraps(func)            # keep func's name/docstring
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) # call the original
        return result.upper() + "!"   # enhance the result
    return wrapper

@shout                                 # same as greet = shout(greet)
def greet(name):
    return f"hello {name}"

print(greet("ada"))     # HELLO ADA!
print(greet.__name__)   # greet  (thanks to functools.wraps)

# ----------------------------------------------------------------------
# Example 2: A timing decorator (logs how long a function takes)
# ----------------------------------------------------------------------
print("\n--- Example 2: A timing decorator (logs how long a function takes) ---")
import functools, time

def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed*1000:.2f} ms")
        return result
    return wrapper

@timed
def slow_sum(n):
    return sum(range(n))

print(slow_sum(1_000_000))   # prints timing, then the result

# ----------------------------------------------------------------------
# Example 3: Decorator with arguments (a factory)
# ----------------------------------------------------------------------
print("\n--- Example 3: Decorator with arguments (a factory) ---")
import functools

def repeat(times):                     # outer: takes the argument
    def decorator(func):               # middle: takes the function
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # inner: does the work
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def ping():
    print("ping")

ping()    # prints ping three times

# Built-in caching decorator -- memoization for free:
from functools import lru_cache
@lru_cache
def fib(n): return n if n < 2 else fib(n-1) + fib(n-2)
print(fib(30))   # fast

print("\nDone! Tip: change values above and run again to learn by experiment.")

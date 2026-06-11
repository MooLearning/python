# ======================================================================
# 22 — Generators and Iterators  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: A generator function with yield
# ----------------------------------------------------------------------
print("\n--- Example 1: A generator function with yield ---")
def countdown(n):
    while n > 0:
        yield n          # pause here and hand back n
        n -= 1           # resume here on the next call

gen = countdown(3)
print(next(gen))   # 3
print(next(gen))   # 2
for x in gen:      # continue from where next() left off
    print("loop:", x)   # 1

# Generators are single-use: once exhausted, they're done
print(list(countdown(4)))   # [4, 3, 2, 1]

# ----------------------------------------------------------------------
# Example 2: Lazy = memory efficient (infinite sequences)
# ----------------------------------------------------------------------
print("\n--- Example 2: Lazy = memory efficient (infinite sequences) ---")
def naturals():
    n = 1
    while True:        # infinite! safe because it's lazy
        yield n
        n += 1

import itertools
first_five = list(itertools.islice(naturals(), 5))
print(first_five)      # [1, 2, 3, 4, 5]

# Generator expression: like a comprehension but lazy (parentheses, not brackets)
squares = (x * x for x in range(1, 1_000_000))
print(next(squares), next(squares))   # 1 4  (only computes what we ask for)
print(sum(x for x in range(1_000_000)))   # streamed, low memory

# ----------------------------------------------------------------------
# Example 3: Building a pipeline of generators
# ----------------------------------------------------------------------
print("\n--- Example 3: Building a pipeline of generators ---")
def read_lines():
    data = "apple,3\nbanana,7\ncherry,2\n"
    for line in data.strip().split("\n"):
        yield line

def parse(lines):
    for line in lines:
        name, count = line.split(",")
        yield name, int(count)

def only_big(pairs, threshold):
    for name, count in pairs:
        if count >= threshold:
            yield name

# Chain them -- nothing runs until we iterate the final result
pipeline = only_big(parse(read_lines()), threshold=3)
print(list(pipeline))   # ['apple', 'banana']

print("\nDone! Tip: change values above and run again to learn by experiment.")

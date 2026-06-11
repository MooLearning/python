# ======================================================================
# 56 — Bit Manipulation  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Core bitwise operations
# ----------------------------------------------------------------------
print("\n--- Example 1: Core bitwise operations ---")
a, b = 0b1100, 0b1010      # 12 and 10
print(bin(a & b))    # 0b1000  AND -> bits set in BOTH (8)
print(bin(a | b))    # 0b1110  OR  -> bits set in EITHER (14)
print(bin(a ^ b))    # 0b0110  XOR -> bits set in exactly one (6)
print(a << 1)        # 24  left shift = multiply by 2
print(a >> 1)        # 6   right shift = integer divide by 2

# Even/odd via the lowest bit
for n in [4, 7, 10, 13]:
    print(n, "is", "odd" if n & 1 else "even")

# ----------------------------------------------------------------------
# Example 2: Get, set, clear, and toggle a specific bit
# ----------------------------------------------------------------------
print("\n--- Example 2: Get, set, clear, and toggle a specific bit ---")
def get_bit(x, i):    return (x >> i) & 1        # is bit i set?
def set_bit(x, i):    return x | (1 << i)        # turn bit i ON
def clear_bit(x, i):  return x & ~(1 << i)       # turn bit i OFF
def toggle_bit(x, i): return x ^ (1 << i)        # flip bit i

x = 0b1010                 # 10
print(get_bit(x, 1))       # 1
print(get_bit(x, 0))       # 0
print(bin(set_bit(x, 0)))  # 0b1011 (11)
print(bin(clear_bit(x, 1)))# 0b1000 (8)
print(bin(toggle_bit(x, 3)))# 0b0010 (2)

# ----------------------------------------------------------------------
# Example 3: Classic bit tricks
# ----------------------------------------------------------------------
print("\n--- Example 3: Classic bit tricks ---")
# Count set bits (Brian Kernighan's algorithm)
def count_bits(x):
    count = 0
    while x:
        x &= x - 1          # clears the lowest set bit each loop
        count += 1
    return count
print(count_bits(0b10110110))   # 5

# Is a power of two? (exactly one bit set)
def is_power_of_two(x):
    return x > 0 and (x & (x - 1)) == 0
print(is_power_of_two(16))   # True
print(is_power_of_two(18))   # False

# Find the single number where every other value appears twice
def single_number(nums):
    result = 0
    for n in nums:
        result ^= n         # pairs cancel out, leaving the unique one
    return result
print(single_number([4, 1, 2, 1, 2]))   # 4

# Swap two numbers without a temporary variable
p, q = 5, 9
p ^= q; q ^= p; p ^= q
print(p, q)                  # 9 5

print("\nDone! Tip: change values above and run again to learn by experiment.")

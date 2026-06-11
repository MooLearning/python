# 56 — Bit Manipulation

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Bit manipulation** works directly on the binary representation of integers using bitwise operators: **AND** `&`, **OR** `|`, **XOR** `^`, **NOT** `~`, and **shifts** `<<`/`>>`. These let you set, clear, toggle, and test individual bits, and unlock fast tricks: check even/odd, multiply/divide by powers of two, swap without a temp, and use integers as compact sets (bitmasks).

## Why it matters

Bit tricks give O(1) operations and tiny memory footprints, crucial in low-level code, graphics, cryptography, and competitive programming. Bitmask DP and subset enumeration are powerful interview tools.

## Key concepts

- **AND / OR / XOR** — & tests/masks, | sets, ^ toggles/finds differences.
- **Shifts** — x << n multiplies by 2ⁿ; x >> n divides by 2ⁿ.
- **Get/set/clear bit** — Use masks `1 << i` with &, |, and & ~.
- **XOR properties** — x ^ x = 0, x ^ 0 = x — finds the unique unpaired value.
- **Bitmask as a set** — Bit i set means element i is present.
- **x & (x-1)** — Clears the lowest set bit — counts bits / tests power of two.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
a, b = 0b1100, 0b1010      # 12 and 10
print(bin(a & b))    # 0b1000  AND -> bits set in BOTH (8)
print(bin(a | b))    # 0b1110  OR  -> bits set in EITHER (14)
print(bin(a ^ b))    # 0b0110  XOR -> bits set in exactly one (6)
print(a << 1)        # 24  left shift = multiply by 2
print(a >> 1)        # 6   right shift = integer divide by 2

# Even/odd via the lowest bit
for n in [4, 7, 10, 13]:
    print(n, "is", "odd" if n & 1 else "even")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Operator precedence: `&`, `|`, `^` bind LOOSER than `==`/`+` — wrap them in parentheses.
- ⚠️ Python ints are arbitrary precision; `~x` is `-x-1`, not a fixed-width complement.
- ⚠️ Shifting by a negative amount raises ValueError; shifting a negative number sign-extends.
- ⚠️ `x & 1` tests odd/even; don't confuse `&` (bitwise) with `and` (logical).
- ⚠️ Bitmask indices are 0-based: element i corresponds to `1 << i`, not `1 << (i-1)`.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


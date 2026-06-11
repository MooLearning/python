# 56 — Bit Manipulation: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Check if 42 is even using a bit operation.

*Hint: Lowest bit.*

<details>
<summary>✅ Solution</summary>

```python
n = 42
print(n & 1 == 0)  # True (even)
```

</details>

## Exercise 2

Set the 3rd bit (index 2) of 0b1001.

*Hint: OR with a mask.*

<details>
<summary>✅ Solution</summary>

```python
x = 0b1001
print(bin(x | (1 << 2)))  # 0b1101
```

</details>

## Exercise 3

Count the number of 1 bits in 29 (0b11101).

*Hint: Kernighan or bin().*

<details>
<summary>✅ Solution</summary>

```python
def count(x):
    c = 0
    while x: x &= x - 1; c += 1
    return c
print(count(29))  # 4
```

</details>

## Exercise 4

Check if 64 is a power of two.

*Hint: x & (x-1) == 0.*

<details>
<summary>✅ Solution</summary>

```python
def is_pow2(x):
    return x > 0 and (x & (x - 1)) == 0
print(is_pow2(64))  # True
```

</details>

## Exercise 5

Find the unique number in [2,3,2,4,4] using XOR.

*Hint: Pairs cancel.*

<details>
<summary>✅ Solution</summary>

```python
def unique(a):
    r = 0
    for x in a: r ^= x
    return r
print(unique([2, 3, 2, 4, 4]))  # 3
```

</details>

## Exercise 6

Multiply 6 by 8 using only a bit shift.

*Hint: 8 = 2^3.*

<details>
<summary>✅ Solution</summary>

```python
print(6 << 3)  # 48
```

</details>

## Exercise 7

Toggle the lowest bit of 0b1011 and print the result.

*Hint: XOR with 1.*

<details>
<summary>✅ Solution</summary>

```python
x = 0b1011
print(bin(x ^ 1))  # 0b1010
```

</details>

## Exercise 8

Generate all subsets of [1,2,3] using bitmasks.

*Hint: Iterate 0..2^n-1.*

<details>
<summary>✅ Solution</summary>

```python
def subsets(nums):
    n = len(nums); out = []
    for mask in range(1 << n):
        out.append([nums[i] for i in range(n) if mask & (1 << i)])
    return out
print(subsets([1, 2, 3]))
# [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

</details>


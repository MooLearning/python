# 53 — Divide and Conquer: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute 2^16 with fast exponentiation.

*Hint: Square the half-power.*

<details>
<summary>✅ Solution</summary>

```python
def power(b, e):
    if e == 0: return 1
    half = power(b, e // 2)
    return half * half * (b if e % 2 else 1)
print(power(2, 16))  # 65536
```

</details>

## Exercise 2

Find the max of [4,2,9,7] using divide and conquer.

*Hint: Max of halves.*

<details>
<summary>✅ Solution</summary>

```python
def find_max(a):
    if len(a) == 1: return a[0]
    mid = len(a) // 2
    return max(find_max(a[:mid]), find_max(a[mid:]))
print(find_max([4, 2, 9, 7]))  # 9
```

</details>

## Exercise 3

Sum [1,2,3,4] by splitting in halves.

*Hint: Recurse and add.*

<details>
<summary>✅ Solution</summary>

```python
def s(a):
    if len(a) == 1: return a[0]
    m = len(a) // 2
    return s(a[:m]) + s(a[m:])
print(s([1, 2, 3, 4]))  # 10
```

</details>

## Exercise 4

Count elements equal to target 2 in [2,1,2,3,2] by divide and conquer.

*Hint: Combine counts.*

<details>
<summary>✅ Solution</summary>

```python
def count(a, t):
    if not a: return 0
    if len(a) == 1: return 1 if a[0] == t else 0
    m = len(a) // 2
    return count(a[:m], t) + count(a[m:], t)
print(count([2, 1, 2, 3, 2], 2))  # 3
```

</details>

## Exercise 5

State the recurrence for merge sort.

*Hint: Two halves plus a merge.*

<details>
<summary>✅ Solution</summary>

**T(n) = 2·T(n/2) + O(n)** — two subproblems of half the size, plus O(n) to merge.
By the master theorem this solves to **O(n log n)**.

</details>

## Exercise 6

Compute the number of digits of 12345 by repeatedly halving? No — count via // 10.

*Hint: Recursive count.*

<details>
<summary>✅ Solution</summary>

```python
def digits(n):
    return 1 if n < 10 else 1 + digits(n // 10)
print(digits(12345))  # 5
```

</details>

## Exercise 7

Multiply two numbers using recursion (a*b = a + a*(b-1)).

*Hint: Linear recursion.*

<details>
<summary>✅ Solution</summary>

```python
def mult(a, b):
    if b == 0: return 0
    return a + mult(a, b - 1)
print(mult(6, 7))  # 42
```

</details>

## Exercise 8

Find both min and max of [3,1,4,1,5] in one divide-and-conquer pass.

*Hint: Return a pair.*

<details>
<summary>✅ Solution</summary>

```python
def min_max(a, lo=0, hi=None):
    if hi is None: hi = len(a) - 1
    if lo == hi: return a[lo], a[lo]
    mid = (lo + hi) // 2
    lmin, lmax = min_max(a, lo, mid)
    rmin, rmax = min_max(a, mid + 1, hi)
    return min(lmin, rmin), max(lmax, rmax)
print(min_max([3, 1, 4, 1, 5]))  # (1, 5)
```

</details>


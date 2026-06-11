# 03 — Operators: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Print the quotient and remainder of 29 divided by 6.

*Hint: Use // and %.*

<details>
<summary>✅ Solution</summary>

```python
print(29 // 6)  # 4
print(29 % 6)   # 5
```

</details>

## Exercise 2

Check whether 50 is between 10 and 100 (inclusive) using a chained comparison.

*Hint: 10 <= x <= 100*

<details>
<summary>✅ Solution</summary>

```python
x = 50
print(10 <= x <= 100)  # True
```

</details>

## Exercise 3

Given temp = 30, print True if it is warm (20 <= temp <= 35).

*Hint: Logical and / chaining.*

<details>
<summary>✅ Solution</summary>

```python
temp = 30
print(20 <= temp <= 35)  # True
```

</details>

## Exercise 4

Use a compound assignment to triple the value of n = 7, then print it.

*Hint: n *= 3*

<details>
<summary>✅ Solution</summary>

```python
n = 7
n *= 3
print(n)  # 21
```

</details>

## Exercise 5

Is a number even? Print True if 12 is even using the modulo operator.

*Hint: even means % 2 == 0*

<details>
<summary>✅ Solution</summary>

```python
print(12 % 2 == 0)  # True
```

</details>

## Exercise 6

Evaluate and explain: 2 + 3 * 4 ** 2. What is the order?

*Hint: ** first, then *, then +.*

<details>
<summary>✅ Solution</summary>

```python
print(2 + 3 * 4 ** 2)  # 4**2=16, *3=48, +2=50 -> 50
```

</details>

## Exercise 7

Use bitwise AND to test if 6 has its lowest bit set (i.e., is it odd?).

*Hint: 6 & 1*

<details>
<summary>✅ Solution</summary>

```python
print(6 & 1)        # 0  -> lowest bit not set
print(6 & 1 == 1)   # False -> 6 is even
```

</details>

## Exercise 8

Without using **, multiply 7 by 8 using a bit shift where possible, else explain why not.

*Hint: Shifts only multiply by powers of 2.*

<details>
<summary>✅ Solution</summary>

8 is `2**3`, so `7 << 3` equals `7 * 8 = 56`.
```python
print(7 << 3)  # 56
```
You can only use a shift when one factor is a power of two.

</details>


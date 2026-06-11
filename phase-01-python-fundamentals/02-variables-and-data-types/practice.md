# 02 — Variables and Data Types: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Create variables for your name (str), age (int) and height in metres (float), then print all three.

*Hint: Three assignments, one print.*

<details>
<summary>✅ Solution</summary>

```python
name = "Sam"
age = 20
height = 1.75
print(name, age, height)
```

</details>

## Exercise 2

Print the type of the value 42, of 4.2, and of '42'.

*Hint: Use type().*

<details>
<summary>✅ Solution</summary>

```python
print(type(42))
print(type(4.2))
print(type("42"))
```

</details>

## Exercise 3

Swap the values of a = 5 and b = 9 without using a third variable.

*Hint: a, b = b, a*

<details>
<summary>✅ Solution</summary>

```python
a, b = 5, 9
a, b = b, a
print(a, b)  # 9 5
```

</details>

## Exercise 4

Predict then verify: what is 7 // 2 and what is 7 / 2?

*Hint: // floors, / makes a float.*

<details>
<summary>✅ Solution</summary>

```python
print(7 // 2)  # 3
print(7 / 2)   # 3.5
```

</details>

## Exercise 5

Compute 2 to the power 10 and print it.

*Hint: Use **.*

<details>
<summary>✅ Solution</summary>

```python
print(2 ** 10)  # 1024
```

</details>

## Exercise 6

Assign 1, 2, 3 to x, y, z in a single line and print their sum.

*Hint: Multiple assignment.*

<details>
<summary>✅ Solution</summary>

```python
x, y, z = 1, 2, 3
print(x + y + z)  # 6
```

</details>

## Exercise 7

Show that 0.1 + 0.2 is not exactly 0.3, then compare them safely.

*Hint: math.isclose*

<details>
<summary>✅ Solution</summary>

```python
import math
print(0.1 + 0.2)                       # 0.30000000000000004
print(math.isclose(0.1 + 0.2, 0.3))    # True
```

</details>

## Exercise 8

Create a variable set to None, then change it to 100 and print its type before and after.

*Hint: type() twice.*

<details>
<summary>✅ Solution</summary>

```python
v = None
print(type(v))   # <class 'NoneType'>
v = 100
print(type(v))   # <class 'int'>
```

</details>


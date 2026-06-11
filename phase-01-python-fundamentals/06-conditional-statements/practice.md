# 06 — Conditional Statements: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Print 'positive', 'negative', or 'zero' for the number n = -4.

*Hint: Three branches.*

<details>
<summary>✅ Solution</summary>

```python
n = -4
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")
```

</details>

## Exercise 2

Print 'even' or 'odd' for 17 using a ternary expression.

*Hint: x if cond else y.*

<details>
<summary>✅ Solution</summary>

```python
n = 17
print("even" if n % 2 == 0 else "odd")  # odd
```

</details>

## Exercise 3

Given age = 70, print 'child' (<13), 'adult' (13-64) or 'senior' (65+).

*Hint: Order branches.*

<details>
<summary>✅ Solution</summary>

```python
age = 70
if age < 13:
    print("child")
elif age <= 64:
    print("adult")
else:
    print("senior")
```

</details>

## Exercise 4

Check if the string s = '' is empty using truthiness (not len).

*Hint: if not s:*

<details>
<summary>✅ Solution</summary>

```python
s = ""
if not s:
    print("empty")
```

</details>

## Exercise 5

Print 'leap' if year 2024 is a leap year, else 'common'.

*Hint: Divisible by 4 and (not by 100 or by 400).*

<details>
<summary>✅ Solution</summary>

```python
y = 2024
if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
    print("leap")
else:
    print("common")
```

</details>

## Exercise 6

Given a number, print 'FizzBuzz' if divisible by both 3 and 5, else the number. Test 15.

*Hint: Check %3==0 and %5==0.*

<details>
<summary>✅ Solution</summary>

```python
n = 15
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
else:
    print(n)
```

</details>

## Exercise 7

Grade 0-100 into A/B/C/D/F bands and print the grade for 67.

*Hint: Cascading elifs.*

<details>
<summary>✅ Solution</summary>

```python
s = 67
if s >= 90: print("A")
elif s >= 80: print("B")
elif s >= 70: print("C")
elif s >= 60: print("D")
else: print("F")  # D
```

</details>

## Exercise 8

Given username and password, print 'access granted' only if username=='admin' and password=='1234'.

*Hint: Combine with and.*

<details>
<summary>✅ Solution</summary>

```python
username, password = "admin", "1234"
if username == "admin" and password == "1234":
    print("access granted")
else:
    print("denied")
```

</details>


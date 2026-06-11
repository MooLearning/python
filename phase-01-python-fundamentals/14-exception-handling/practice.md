# 14 — Exception Handling: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Safely convert the string 'abc' to int, printing 'invalid' instead of crashing.

*Hint: Catch ValueError.*

<details>
<summary>✅ Solution</summary>

```python
try:
    int("abc")
except ValueError:
    print("invalid")
```

</details>

## Exercise 2

Write divide(a,b) that returns None and prints a message on division by zero.

*Hint: ZeroDivisionError.*

<details>
<summary>✅ Solution</summary>

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("nope")
        return None
print(divide(6, 0))
```

</details>

## Exercise 3

Look up a missing key 'x' in {'a':1} and print 'missing' instead of raising.

*Hint: KeyError.*

<details>
<summary>✅ Solution</summary>

```python
d = {"a": 1}
try:
    print(d["x"])
except KeyError:
    print("missing")
```

</details>

## Exercise 4

Use finally to always print 'cleanup' whether or not an error happens.

*Hint: try/finally.*

<details>
<summary>✅ Solution</summary>

```python
try:
    x = 1 / 1
finally:
    print("cleanup")
```

</details>

## Exercise 5

Raise a ValueError if a withdrawal amount is greater than balance 100.

*Hint: raise.*

<details>
<summary>✅ Solution</summary>

```python
def withdraw(amount, balance=100):
    if amount > balance:
        raise ValueError("insufficient funds")
    return balance - amount
try:
    withdraw(150)
except ValueError as e:
    print(e)
```

</details>

## Exercise 6

Catch both KeyError and IndexError with one except clause.

*Hint: except (A, B).*

<details>
<summary>✅ Solution</summary>

```python
try:
    [][5]
except (KeyError, IndexError) as e:
    print("caught", type(e).__name__)
```

</details>

## Exercise 7

Loop over ['10','x','5'], summing only the valid integers; skip bad ones.

*Hint: try inside loop.*

<details>
<summary>✅ Solution</summary>

```python
total = 0
for v in ["10", "x", "5"]:
    try:
        total += int(v)
    except ValueError:
        continue
print(total)  # 15
```

</details>

## Exercise 8

Use try/except/else: parse '7', and only if it succeeds print its square.

*Hint: else block.*

<details>
<summary>✅ Solution</summary>

```python
try:
    n = int("7")
except ValueError:
    print("bad")
else:
    print(n ** 2)  # 49
```

</details>


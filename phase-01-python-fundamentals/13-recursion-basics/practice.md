# 13 — Recursion Basics: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Write factorial(n) recursively and print factorial(6).

*Hint: Base case n<=1.*

<details>
<summary>✅ Solution</summary>

```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
print(factorial(6))  # 720
```

</details>

## Exercise 2

Write a recursive function to sum numbers from 1 to n. Test n=5.

*Hint: n + sum(n-1).*

<details>
<summary>✅ Solution</summary>

```python
def s(n):
    return 0 if n == 0 else n + s(n - 1)
print(s(5))  # 15
```

</details>

## Exercise 3

Recursively count down from n to 1, printing each. Test n=4.

*Hint: Print then recurse.*

<details>
<summary>✅ Solution</summary>

```python
def countdown(n):
    if n < 1:
        return
    print(n)
    countdown(n - 1)
countdown(4)
```

</details>

## Exercise 4

Write a recursive power(base, exp) (exp>=0). Test power(2,8).

*Hint: base * power(base, exp-1).*

<details>
<summary>✅ Solution</summary>

```python
def power(base, exp):
    return 1 if exp == 0 else base * power(base, exp - 1)
print(power(2, 8))  # 256
```

</details>

## Exercise 5

Recursively reverse the string 'recursion'.

*Hint: tail + first char.*

<details>
<summary>✅ Solution</summary>

```python
def rev(s):
    return s if len(s) <= 1 else rev(s[1:]) + s[0]
print(rev("recursion"))  # noisrucer
```

</details>

## Exercise 6

Write recursive fib(n) and print the 10th Fibonacci number (fib(10)).

*Hint: fib(n-1)+fib(n-2).*

<details>
<summary>✅ Solution</summary>

```python
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(10))  # 55
```

</details>

## Exercise 7

Count the number of digits in an integer recursively. Test 9043.

*Hint: n//10 each step.*

<details>
<summary>✅ Solution</summary>

```python
def digits(n):
    n = abs(n)
    return 1 if n < 10 else 1 + digits(n // 10)
print(digits(9043))  # 4
```

</details>

## Exercise 8

Speed up your fib with @lru_cache and compute fib(40).

*Hint: from functools import lru_cache.*

<details>
<summary>✅ Solution</summary>

```python
from functools import lru_cache
@lru_cache(None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(40))  # 102334155
```

</details>


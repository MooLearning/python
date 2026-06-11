# 23 — Closures: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Write make_adder(n) returning a function that adds n to its argument.

*Hint: Return inner function.*

<details>
<summary>✅ Solution</summary>

```python
def make_adder(n):
    def add(x): return x + n
    return add
print(make_adder(5)(10))  # 15
```

</details>

## Exercise 2

Create a power factory: make_power(exp) so make_power(2)(5)==25.

*Hint: x ** exp.*

<details>
<summary>✅ Solution</summary>

```python
def make_power(exp):
    def p(x): return x ** exp
    return p
print(make_power(2)(5))  # 25
```

</details>

## Exercise 3

Build a counter closure that returns 1,2,3 on successive calls.

*Hint: nonlocal.*

<details>
<summary>✅ Solution</summary>

```python
def counter():
    n = 0
    def step():
        nonlocal n; n += 1; return n
    return step
c = counter()
print(c(), c(), c())  # 1 2 3
```

</details>

## Exercise 4

Show two counters from the same factory are independent.

*Hint: Two instances.*

<details>
<summary>✅ Solution</summary>

```python
def counter():
    n = 0
    def step():
        nonlocal n; n += 1; return n
    return step
a, b = counter(), counter()
print(a(), a(), b())  # 1 2 1
```

</details>

## Exercise 5

Demonstrate the late-binding bug with lambdas in a loop.

*Hint: Capture by reference.*

<details>
<summary>✅ Solution</summary>

```python
fs = [lambda: i for i in range(3)]
print([f() for f in fs])  # [2, 2, 2]
```

</details>

## Exercise 6

Fix the late-binding bug using default arguments.

*Hint: lambda i=i.*

<details>
<summary>✅ Solution</summary>

```python
fs = [lambda i=i: i for i in range(3)]
print([f() for f in fs])  # [0, 1, 2]
```

</details>

## Exercise 7

Write make_accumulator() that keeps a running total across calls.

*Hint: nonlocal total.*

<details>
<summary>✅ Solution</summary>

```python
def make_accumulator():
    total = 0
    def add(x):
        nonlocal total; total += x; return total
    return add
acc = make_accumulator()
print(acc(10), acc(5))  # 10 15
```

</details>

## Exercise 8

Write a closure that remembers a greeting prefix and greets names.

*Hint: Capture prefix.*

<details>
<summary>✅ Solution</summary>

```python
def greeter(prefix):
    def greet(name): return f"{prefix}, {name}!"
    return greet
hi = greeter("Hello")
print(hi("Ada"))  # Hello, Ada!
```

</details>


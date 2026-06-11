# 22 — Generators and Iterators: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Write a generator that yields the squares of 1..5.

*Hint: yield in a loop.*

<details>
<summary>✅ Solution</summary>

```python
def squares():
    for i in range(1, 6):
        yield i * i
print(list(squares()))  # [1, 4, 9, 16, 25]
```

</details>

## Exercise 2

Use a generator expression to sum the squares of 0..9 lazily.

*Hint: (x*x for x in ...).*

<details>
<summary>✅ Solution</summary>

```python
print(sum(x * x for x in range(10)))  # 285
```

</details>

## Exercise 3

Write a generator that yields the Fibonacci numbers, take the first 8.

*Hint: Track two values.*

<details>
<summary>✅ Solution</summary>

```python
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
import itertools
print(list(itertools.islice(fib(), 8)))  # [0,1,1,2,3,5,8,13]
```

</details>

## Exercise 4

Use next() three times on a generator and observe the values.

*Hint: next().*

<details>
<summary>✅ Solution</summary>

```python
def g():
    yield "a"; yield "b"; yield "c"
it = g()
print(next(it), next(it), next(it))  # a b c
```

</details>

## Exercise 5

Write a generator that yields only even numbers from a list.

*Hint: yield with if.*

<details>
<summary>✅ Solution</summary>

```python
def evens(seq):
    for x in seq:
        if x % 2 == 0:
            yield x
print(list(evens([1, 2, 3, 4, 5, 6])))  # [2, 4, 6]
```

</details>

## Exercise 6

Create an infinite counter generator and take the first 4 values with islice.

*Hint: while True.*

<details>
<summary>✅ Solution</summary>

```python
import itertools
def count_from(n):
    while True:
        yield n; n += 1
print(list(itertools.islice(count_from(10), 4)))  # [10,11,12,13]
```

</details>

## Exercise 7

Show that a generator is empty on a second pass.

*Hint: Iterate twice.*

<details>
<summary>✅ Solution</summary>

```python
def g():
    yield 1; yield 2
it = g()
print(list(it))  # [1, 2]
print(list(it))  # [] -> exhausted
```

</details>

## Exercise 8

Chain two generators: one yields 1..5, the next yields only those >2.

*Hint: Pipeline.*

<details>
<summary>✅ Solution</summary>

```python
def nums():
    yield from range(1, 6)
def big(src):
    for x in src:
        if x > 2: yield x
print(list(big(nums())))  # [3, 4, 5]
```

</details>


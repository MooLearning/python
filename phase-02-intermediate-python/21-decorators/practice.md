# 21 — Decorators: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Write a decorator that prints 'calling' before running any function. Decorate hi().

*Hint: wrapper prints then calls.*

<details>
<summary>✅ Solution</summary>

```python
def announce(f):
    def w(*a, **k):
        print("calling")
        return f(*a, **k)
    return w
@announce
def hi(): print("hi")
hi()
```

</details>

## Exercise 2

Write a decorator double that doubles the numeric return value of a function.

*Hint: Return f()*2.*

<details>
<summary>✅ Solution</summary>

```python
def double(f):
    def w(*a, **k): return f(*a, **k) * 2
    return w
@double
def five(): return 5
print(five())  # 10
```

</details>

## Exercise 3

Use functools.wraps and confirm the wrapped function keeps its name.

*Hint: wraps.*

<details>
<summary>✅ Solution</summary>

```python
import functools
def deco(f):
    @functools.wraps(f)
    def w(*a, **k): return f(*a, **k)
    return w
@deco
def hello(): pass
print(hello.__name__)  # hello
```

</details>

## Exercise 4

Write a decorator that counts how many times a function was called.

*Hint: Use an attribute.*

<details>
<summary>✅ Solution</summary>

```python
def counter(f):
    def w(*a, **k):
        w.calls += 1
        return f(*a, **k)
    w.calls = 0
    return w
@counter
def go(): pass
go(); go()
print(go.calls)  # 2
```

</details>

## Exercise 5

Write a parametrized decorator repeat(n) that runs a function n times.

*Hint: Factory pattern.*

<details>
<summary>✅ Solution</summary>

```python
def repeat(n):
    def deco(f):
        def w(*a, **k):
            for _ in range(n): r = f(*a, **k)
            return r
        return w
    return deco
@repeat(2)
def beep(): print("beep")
beep()
```

</details>

## Exercise 6

Cache an expensive function with functools.lru_cache and call it twice.

*Hint: @lru_cache.*

<details>
<summary>✅ Solution</summary>

```python
from functools import lru_cache
@lru_cache
def square(n):
    print("computing")
    return n * n
print(square(4)); print(square(4))  # computes once
```

</details>

## Exercise 7

Write a decorator that catches exceptions and returns None instead of crashing.

*Hint: try/except in wrapper.*

<details>
<summary>✅ Solution</summary>

```python
def safe(f):
    def w(*a, **k):
        try: return f(*a, **k)
        except Exception: return None
    return w
@safe
def bad(): return 1 / 0
print(bad())  # None
```

</details>

## Exercise 8

Stack two decorators (upper then exclaim) and observe the order.

*Hint: Bottom-up application.*

<details>
<summary>✅ Solution</summary>

```python
def upper(f):
    def w(*a, **k): return f(*a, **k).upper()
    return w
def exclaim(f):
    def w(*a, **k): return f(*a, **k) + "!"
    return w
@exclaim
@upper
def hi(): return "hi"
print(hi())  # HI!
```

</details>


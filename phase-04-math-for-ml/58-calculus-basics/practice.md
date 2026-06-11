# 58 — Calculus Basics: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Estimate the derivative of x^2 at x=5.

*Hint: Central difference.*

<details>
<summary>✅ Solution</summary>

```python
def deriv(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)
print(round(deriv(lambda x: x ** 2, 5)))  # 10
```

</details>

## Exercise 2

Estimate the derivative of x^3 at x=1.

*Hint: Should be 3.*

<details>
<summary>✅ Solution</summary>

```python
def deriv(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)
print(round(deriv(lambda x: x ** 3, 1)))  # 3
```

</details>

## Exercise 3

Approximate the area under x from 0 to 2.

*Hint: Triangle area = 2.*

<details>
<summary>✅ Solution</summary>

```python
def integrate(f, a, b, n=1000):
    h = (b - a) / n
    return h * (f(a)/2 + f(b)/2 + sum(f(a + i*h) for i in range(1, n)))
print(round(integrate(lambda x: x, 0, 2)))  # 2
```

</details>

## Exercise 4

Do one gradient-descent step on f(x)=(x-3)^2 from x=0, lr=0.1.

*Hint: x -= lr*2(x-3).*

<details>
<summary>✅ Solution</summary>

```python
x = 0.0; lr = 0.1
x = x - lr * 2 * (x - 3)
print(x)  # 0.6
```

</details>

## Exercise 5

What learning rate behavior causes divergence? Explain briefly.

*Hint: Too large.*

<details>
<summary>✅ Solution</summary>

A learning rate that is **too large** makes each step overshoot the minimum and
land farther away, so |x| grows every step and f(x) blows up — **divergence**. A
smaller learning rate converges (just more slowly).

</details>

## Exercise 6

Find the minimum of f(x)=x^2+4x+4 with gradient descent.

*Hint: Derivative 2x+4.*

<details>
<summary>✅ Solution</summary>

```python
def grad(x): return 2 * x + 4
x = 0.0
for _ in range(100):
    x -= 0.1 * grad(x)
print(round(x))  # -2
```

</details>

## Exercise 7

Numerically check that the derivative of sin at 0 is 1.

*Hint: cos(0)=1.*

<details>
<summary>✅ Solution</summary>

```python
import math
def deriv(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)
print(round(deriv(math.sin, 0)))  # 1
```

</details>

## Exercise 8

Minimize f(x,y)=x^2+y^2 with gradient descent (start (3,4)).

*Hint: Grad=(2x,2y).*

<details>
<summary>✅ Solution</summary>

```python
x, y = 3.0, 4.0
for _ in range(100):
    x -= 0.1 * 2 * x
    y -= 0.1 * 2 * y
print(round(x, 2), round(y, 2))  # 0.0 0.0
```

</details>


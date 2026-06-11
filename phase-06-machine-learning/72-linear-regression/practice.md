# 72 — Linear Regression: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Fit a line to (1,2),(2,4),(3,6): find the slope.

*Hint: Closed form.*

<details>
<summary>✅ Solution</summary>

```python
xs, ys = [1, 2, 3], [2, 4, 6]
n = len(xs); xb = sum(xs) / n; yb = sum(ys) / n
num = sum((x - xb) * (y - yb) for x, y in zip(xs, ys))
den = sum((x - xb) ** 2 for x in xs)
print(num / den)  # 2.0
```

</details>

## Exercise 2

Predict y at x=10 for y=3x+1.

*Hint: Plug in.*

<details>
<summary>✅ Solution</summary>

```python
print(3 * 10 + 1)  # 31
```

</details>

## Exercise 3

Compute the mean squared error of preds [2,4] vs [3,5].

*Hint: Mean of squares.*

<details>
<summary>✅ Solution</summary>

```python
pred, true = [2, 4], [3, 5]
print(sum((p - t) ** 2 for p, t in zip(pred, true)) / len(true))  # 1.0
```

</details>

## Exercise 4

Compute R^2 when SS_res=2 and SS_tot=10.

*Hint: 1 - res/tot.*

<details>
<summary>✅ Solution</summary>

```python
print(1 - 2 / 10)  # 0.8
```

</details>

## Exercise 5

Find the intercept given slope=2, x̄=3, ȳ=8.

*Hint: ȳ - slope*x̄.*

<details>
<summary>✅ Solution</summary>

```python
print(8 - 2 * 3)  # 2
```

</details>

## Exercise 6

One gradient-descent step for w on MSE: w=0,lr=0.1,grad=-4.

*Hint: w -= lr*grad.*

<details>
<summary>✅ Solution</summary>

```python
w, lr, grad = 0, 0.1, -4
print(w - lr * grad)  # 0.4
```

</details>

## Exercise 7

What does an R^2 of 1.0 mean?

*Hint: Perfect fit.*

<details>
<summary>✅ Solution</summary>

The model explains **100% of the variance** in the target — predictions match the
actual values exactly (perfect fit on this data).

</details>

## Exercise 8

Why are outliers dangerous for least squares?

*Hint: Squared penalty.*

<details>
<summary>✅ Solution</summary>

Least squares minimizes **squared** errors, so a single far-off point contributes a
huge penalty and can drag the whole line toward it, hurting all other predictions.

</details>


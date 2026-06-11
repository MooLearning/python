# 71 — Bias-Variance Tradeoff: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Train error 0.01, test error 5.0 — over or underfit?

*Hint: Big gap.*

<details>
<summary>✅ Solution</summary>

**Overfitting** (high variance): tiny training error but large test error means the
model memorized the training data and fails to generalize.

</details>

## Exercise 2

Train error 4.5, test error 4.7 — over or underfit?

*Hint: Both high.*

<details>
<summary>✅ Solution</summary>

**Underfitting** (high bias): error is high on both sets, so the model is too simple
to capture the pattern.

</details>

## Exercise 3

Compute MSE of constant predictor 5 for truths [2,8].

*Hint: Mean sq error.*

<details>
<summary>✅ Solution</summary>

```python
true = [2, 8]
print(sum((5 - t) ** 2 for t in true) / len(true))  # 9.0
```

</details>

## Exercise 4

Fix for overfitting: name two options.

*Hint: Data/regularize.*

<details>
<summary>✅ Solution</summary>

1) Get **more training data**. 2) **Regularize** / reduce model complexity (fewer
features, smaller degree, L1/L2 penalties, dropout).

</details>

## Exercise 5

Fix for underfitting: name two options.

*Hint: Complexity/features.*

<details>
<summary>✅ Solution</summary>

1) Use a **more complex model** (higher degree, more layers). 2) Add **better
features** so the signal is learnable.

</details>

## Exercise 6

Which has higher variance: degree-1 line or degree-15 polynomial?

*Hint: Complex = variance.*

<details>
<summary>✅ Solution</summary>

The **degree-15 polynomial** — high complexity makes it wiggle to fit noise, so it
varies a lot with the training sample (high variance).

</details>

## Exercise 7

Compute the train-test error gap for 0.9 vs 0.6 accuracy.

*Hint: Subtract.*

<details>
<summary>✅ Solution</summary>

```python
print(0.9 - 0.6)  # 0.30 -> large gap, likely overfit
```

</details>

## Exercise 8

As model complexity rises, what happens to bias and variance?

*Hint: Opposite directions.*

<details>
<summary>✅ Solution</summary>

**Bias decreases** (model fits training data better) while **variance increases**
(more sensitive to the specific training sample). Total error is U-shaped.

</details>


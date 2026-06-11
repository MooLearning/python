# 92 — Gradient Descent and Optimizers: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

One GD step on f(x)=x^2 from x=5, lr=0.1.

*Hint: x -= lr*2x.*

<details>
<summary>✅ Solution</summary>

```python
x, lr = 5, 0.1
print(x - lr * 2 * x)  # 4.0
```

</details>

## Exercise 2

What does momentum add to GD?

*Hint: Velocity.*

<details>
<summary>✅ Solution</summary>

A **velocity** term that accumulates past gradients, so the optimizer accelerates in
consistent directions and rolls through small bumps/plateaus — faster convergence.

</details>

## Exercise 3

Batch vs stochastic GD: which uses one sample per step?

*Hint: Definition.*

<details>
<summary>✅ Solution</summary>

**Stochastic gradient descent (SGD)** uses **one sample** per update (noisy but
fast). Batch GD uses the whole dataset per step.

</details>

## Exercise 4

If lr=1.01 on f(x)=x^2, does it converge?

*Hint: Overshoot.*

<details>
<summary>✅ Solution</summary>

**No** — the step overshoots the minimum and grows each iteration (|x| increases),
so it **diverges**. The update needs lr < 1 here for stability.

</details>

## Exercise 5

Compute velocity v = 0.9*v - 0.1*g for v=0,g=4.

*Hint: Plug in.*

<details>
<summary>✅ Solution</summary>

```python
v, g = 0, 4
print(0.9 * v - 0.1 * g)  # -0.4
```

</details>

## Exercise 6

Which optimizer combines momentum and adaptive rates?

*Hint: Name it.*

<details>
<summary>✅ Solution</summary>

**Adam** — it keeps a momentum estimate (first moment) and a per-parameter adaptive
scale from squared gradients (second moment).

</details>

## Exercise 7

Why shuffle data for mini-batch GD?

*Hint: Avoid bias.*

<details>
<summary>✅ Solution</summary>

So consecutive batches aren't correlated/ordered (e.g. sorted by class), which would
bias each gradient estimate. Shuffling makes batches representative.

</details>

## Exercise 8

What's the most important hyperparameter in training?

*Hint: LR.*

<details>
<summary>✅ Solution</summary>

The **learning rate** — it controls step size and most directly determines whether
training converges, how fast, and how well.

</details>


# 79 — Gradient Boosting: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute residuals of preds [2,4,6] vs truth [3,5,5].

*Hint: actual - predicted.*

<details>
<summary>✅ Solution</summary>

```python
pred, true = [2, 4, 6], [3, 5, 5]
print([t - p for p, t in zip(pred, true)])  # [1, 1, -1]
```

</details>

## Exercise 2

Update a prediction p=5 by lr=0.1 times step=4.

*Hint: p += lr*step.*

<details>
<summary>✅ Solution</summary>

```python
p, lr, step = 5, 0.1, 4
print(p + lr * step)  # 5.4
```

</details>

## Exercise 3

How does boosting differ from bagging (one line)?

*Hint: Sequential vs parallel.*

<details>
<summary>✅ Solution</summary>

**Boosting** trains learners **sequentially**, each fixing the previous errors
(reduces bias). **Bagging** trains learners **independently in parallel** and
averages them (reduces variance).

</details>

## Exercise 4

Final prediction = sum of [3.0, 0.5, -0.2]. Compute it.

*Hint: Additive model.*

<details>
<summary>✅ Solution</summary>

```python
print(sum([3.0, 0.5, -0.2]))  # 3.3
```

</details>

## Exercise 5

Why use a small learning rate?

*Hint: Robustness.*

<details>
<summary>✅ Solution</summary>

A small learning rate makes each tree contribute a little, so the ensemble learns
**gradually and robustly**, reducing overfitting — at the cost of needing more
trees.

</details>

## Exercise 6

What kind of trees are used as weak learners?

*Hint: Shallow.*

<details>
<summary>✅ Solution</summary>

**Shallow** trees (often stumps, or depth ≤ ~3). Each only needs to be slightly
better than chance; depth comes from combining many of them.

</details>

## Exercise 7

Mean residual of [2,-1,2,-3]?

*Hint: Average.*

<details>
<summary>✅ Solution</summary>

```python
r = [2, -1, 2, -3]
print(sum(r) / len(r))  # 0.0
```

</details>

## Exercise 8

If lr=0.1 and you want similar power to lr=0.5 with 100 trees, more or fewer trees?

*Hint: Tradeoff.*

<details>
<summary>✅ Solution</summary>

**More** trees. Lower learning rate means each step is smaller, so you need
proportionally **more estimators** to reach the same total fit.

</details>


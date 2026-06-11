# 97 — Dropout and Batch Normalization: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

With dropout p=0.5 inverted, scale a surviving activation of 3.

*Hint: / (1-p).*

<details>
<summary>✅ Solution</summary>

```python
p = 0.5
print(3 / (1 - p))  # 6.0
```

</details>

## Exercise 2

Is dropout active during inference?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**No.** Dropout is applied only during **training**; at inference all neurons are
used (the framework switches it off automatically).

</details>

## Exercise 3

Normalize [2,4,6] to zero mean (subtract mean).

*Hint: x - mean.*

<details>
<summary>✅ Solution</summary>

```python
d = [2, 4, 6]
m = sum(d) / len(d)
print([x - m for x in d])  # [-2, 0, 2]
```

</details>

## Exercise 4

After batch norm, what are the mean and variance (before scale/shift)?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Mean 0 and variance 1** — batch norm standardizes the activations, then applies
learnable scale (γ) and shift (β).

</details>

## Exercise 5

What does dropout help prevent?

*Hint: Overfitting.*

<details>
<summary>✅ Solution</summary>

**Overfitting** — by randomly dropping units it stops the network from co-adapting/
relying on specific neurons, acting as a regularizer.

</details>

## Exercise 6

Compute batch variance of [1,3] (population).

*Hint: pvariance.*

<details>
<summary>✅ Solution</summary>

```python
import statistics as st
print(st.pvariance([1, 3]))  # 1.0
```

</details>

## Exercise 7

Why does batch norm allow higher learning rates?

*Hint: Stability.*

<details>
<summary>✅ Solution</summary>

By keeping each layer's input distribution stable (mean 0 / var 1), BN **smooths the
loss landscape**, reducing the risk of exploding activations — so larger, faster
learning-rate steps stay stable.

</details>

## Exercise 8

Typical dropout rate range?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

Commonly **0.2 to 0.5**. Too high (e.g. 0.8) removes so much signal it can cause
underfitting.

</details>


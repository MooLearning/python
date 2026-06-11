# 88 — Regularization (L1, L2): Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute the L2 penalty Σw² for w=[3,4].

*Hint: Sum of squares.*

<details>
<summary>✅ Solution</summary>

```python
w = [3, 4]
print(sum(wi ** 2 for wi in w))  # 25
```

</details>

## Exercise 2

Compute the L1 penalty Σ|w| for w=[-3,4].

*Hint: Sum of abs.*

<details>
<summary>✅ Solution</summary>

```python
w = [-3, 4]
print(sum(abs(wi) for wi in w))  # 7
```

</details>

## Exercise 3

Soft-threshold w=0.3 with lambda=0.5.

*Hint: Within band -> 0.*

<details>
<summary>✅ Solution</summary>

```python
def st(w, lam):
    return w - lam if w > lam else (w + lam if w < -lam else 0.0)
print(st(0.3, 0.5))  # 0.0
```

</details>

## Exercise 4

Which penalty produces sparse models?

*Hint: Zeros weights.*

<details>
<summary>✅ Solution</summary>

**L1 (Lasso)** — its constant-magnitude gradient drives small weights exactly to
**zero**, performing automatic feature selection. L2 only shrinks them.

</details>

## Exercise 5

As lambda increases, do weights grow or shrink?

*Hint: Penalty effect.*

<details>
<summary>✅ Solution</summary>

**Shrink** toward zero — a larger penalty makes large weights more costly, producing
a simpler, more biased (but lower-variance) model.

</details>

## Exercise 6

Add L2 gradient 2*lambda*w for lambda=0.5, w=4.

*Hint: Compute.*

<details>
<summary>✅ Solution</summary>

```python
print(2 * 0.5 * 4)  # 4.0
```

</details>

## Exercise 7

Why standardize before regularizing?

*Hint: Fair penalty.*

<details>
<summary>✅ Solution</summary>

The penalty acts on weight magnitudes, which depend on feature scale. Without
standardizing, features with small ranges get large weights and are penalized
disproportionately. Scaling makes the penalty fair across features.

</details>

## Exercise 8

What does Elastic Net combine?

*Hint: L1 + L2.*

<details>
<summary>✅ Solution</summary>

**Both L1 and L2** penalties — getting Lasso's sparsity plus Ridge's stability
(handles correlated features better than pure L1).

</details>


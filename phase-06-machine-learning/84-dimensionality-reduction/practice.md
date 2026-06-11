# 84 — Dimensionality Reduction (t-SNE): Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute the variance of each column of [[1,3],[2,3],[3,3]].

*Hint: Per-column.*

<details>
<summary>✅ Solution</summary>

```python
import statistics as st
cols = list(zip(*[[1, 3], [2, 3], [3, 3]]))
print([st.pvariance(c) for c in cols])  # [0.66.., 0.0]
```

</details>

## Exercise 2

Drop columns with zero variance from that data.

*Hint: Keep var>0.*

<details>
<summary>✅ Solution</summary>

```python
import statistics as st
data = [[1, 3], [2, 3], [3, 3]]
cols = list(zip(*data))
keep = [i for i, c in enumerate(cols) if st.pvariance(c) > 0]
print(keep)  # [0]
```

</details>

## Exercise 3

Why is high dimensionality a problem (one line)?

*Hint: Curse.*

<details>
<summary>✅ Solution</summary>

The **curse of dimensionality**: as features grow, data becomes sparse and
distances between points become similar, so models need exponentially more data and
distance-based methods degrade.

</details>

## Exercise 4

Is t-SNE output suitable as model features?

*Hint: Viz only.*

<details>
<summary>✅ Solution</summary>

**No** — t-SNE is for **visualization** only. Its coordinates are non-deterministic
and don't preserve global structure, so they shouldn't be used as model inputs.

</details>

## Exercise 5

Pick the 2 highest-variance feature indices given vars [0.1,5,0.2,3].

*Hint: Sort desc.*

<details>
<summary>✅ Solution</summary>

```python
vars = [0.1, 5, 0.2, 3]
idx = sorted(range(4), key=lambda i: -vars[i])[:2]
print(sorted(idx))  # [1, 3]
```

</details>

## Exercise 6

PCA vs t-SNE: which is linear?

*Hint: Recall definitions.*

<details>
<summary>✅ Solution</summary>

**PCA** is linear (projection onto variance-maximizing axes). **t-SNE** is
non-linear, modeling local neighborhood probabilities.

</details>

## Exercise 7

Reduce [5,2,9,1] keeping the 2 largest values' positions.

*Hint: Top-2 indices.*

<details>
<summary>✅ Solution</summary>

```python
vals = [5, 2, 9, 1]
print(sorted(sorted(range(4), key=lambda i: -vals[i])[:2]))  # [0, 2]
```

</details>

## Exercise 8

Name one benefit of dimensionality reduction.

*Hint: Any valid.*

<details>
<summary>✅ Solution</summary>

Any of: faster training, less overfitting, lower storage, removing redundant/
correlated features, or enabling 2-D **visualization** of the data.

</details>


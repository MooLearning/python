# 83 — Principal Component Analysis (PCA): Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Center the data [2,4,6] (subtract the mean).

*Hint: x - mean.*

<details>
<summary>✅ Solution</summary>

```python
d = [2, 4, 6]
m = sum(d) / len(d)
print([x - m for x in d])  # [-2.0, 0.0, 2.0]
```

</details>

## Exercise 2

Compute the variance of centered [-2,0,2].

*Hint: Mean of squares.*

<details>
<summary>✅ Solution</summary>

```python
c = [-2, 0, 2]
print(sum(x ** 2 for x in c) / len(c))  # 2.666...
```

</details>

## Exercise 3

Explained variance ratio for eigenvalues [3,1].

*Hint: ev/total.*

<details>
<summary>✅ Solution</summary>

```python
ev = [3, 1]
print(ev[0] / sum(ev))  # 0.75
```

</details>

## Exercise 4

How many components to keep 90% with ratios [0.8,0.15,0.05]?

*Hint: Cumulate.*

<details>
<summary>✅ Solution</summary>

```python
ratios = [0.8, 0.15, 0.05]
c = 0; n = 0
for r in ratios:
    n += 1; c += r
    if c >= 0.9: break
print(n)  # 2
```

</details>

## Exercise 5

Why standardize before PCA?

*Hint: Variance fairness.*

<details>
<summary>✅ Solution</summary>

PCA maximizes variance, so a feature measured in large units (e.g. salary) would
dominate the components purely due to scale. **Standardizing** gives each feature
equal footing.

</details>

## Exercise 6

Project point (1,1) onto direction (0.707,0.707).

*Hint: Dot product.*

<details>
<summary>✅ Solution</summary>

```python
print(round(1 * 0.707 + 1 * 0.707, 3))  # 1.414
```

</details>

## Exercise 7

Trace (sum of variances) of covariance [[4,0],[0,1]].

*Hint: a + d.*

<details>
<summary>✅ Solution</summary>

```python
print(4 + 1)  # 5
```

</details>

## Exercise 8

Is PCA supervised or unsupervised?

*Hint: Uses labels?*

<details>
<summary>✅ Solution</summary>

**Unsupervised** — PCA uses only the feature matrix X (its variance/covariance
structure); it never looks at labels y.

</details>


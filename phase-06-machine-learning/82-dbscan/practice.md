# 82 — DBSCAN: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Count neighbors of (0,0) within eps=1 among [(0,0),(0.5,0),(2,0)].

*Hint: Distance <= eps.*

<details>
<summary>✅ Solution</summary>

```python
import math
pts = [(0, 0), (0.5, 0), (2, 0)]
print(sum(1 for p in pts if math.dist((0, 0), p) <= 1))  # 2
```

</details>

## Exercise 2

Is a point with 4 neighbors a core point if min_pts=3?

*Hint: Compare.*

<details>
<summary>✅ Solution</summary>

```python
print(4 >= 3)  # True -> core
```

</details>

## Exercise 3

What label does DBSCAN give an isolated outlier?

*Hint: Noise.*

<details>
<summary>✅ Solution</summary>

**Noise** (typically labeled **-1**) — it is neither a core point nor within eps of
one.

</details>

## Exercise 4

Does DBSCAN need the number of clusters in advance?

*Hint: Density-driven.*

<details>
<summary>✅ Solution</summary>

**No.** The number of clusters emerges from the density structure (eps + min_pts);
you don't specify k.

</details>

## Exercise 5

Classify: 1 neighbor, min_pts=3 — core or not?

*Hint: Below threshold.*

<details>
<summary>✅ Solution</summary>

```python
print("core" if 1 >= 3 else "not core")  # not core
```

</details>

## Exercise 6

Why scale features before DBSCAN?

*Hint: Distance based.*

<details>
<summary>✅ Solution</summary>

DBSCAN measures density via Euclidean distance, so unscaled features with large
ranges dominate. **Standardizing** makes eps meaningful across all features.

</details>

## Exercise 7

Name the two DBSCAN parameters.

*Hint: eps, min_pts.*

<details>
<summary>✅ Solution</summary>

**eps** (neighborhood radius) and **min_samples / min_pts** (minimum neighbors for
a core point).

</details>

## Exercise 8

If eps is too large, what happens?

*Hint: Over-merge.*

<details>
<summary>✅ Solution</summary>

Everything falls within everyone's neighborhood, so distinct clusters **merge into
one giant blob** (and almost nothing is labeled noise).

</details>


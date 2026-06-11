# 80 — K-Means Clustering: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute the centroid (mean) of points [(0,0),(2,2),(4,4)].

*Hint: Average coords.*

<details>
<summary>✅ Solution</summary>

```python
pts = [(0, 0), (2, 2), (4, 4)]
cx = sum(p[0] for p in pts) / len(pts)
cy = sum(p[1] for p in pts) / len(pts)
print((cx, cy))  # (2.0, 2.0)
```

</details>

## Exercise 2

Assign point (1,1) to the nearer of centroids (0,0),(5,5).

*Hint: Min distance.*

<details>
<summary>✅ Solution</summary>

```python
import math
def d(a, b): return math.dist(a, b)
p = (1, 1); cents = [(0, 0), (5, 5)]
print(min(range(2), key=lambda i: d(p, cents[i])))  # 0
```

</details>

## Exercise 3

Compute inertia for points [(0,0),(2,0)] around centroid (1,0).

*Hint: Sum sq dist.*

<details>
<summary>✅ Solution</summary>

```python
import math
c = (1, 0)
print(sum(math.dist(p, c) ** 2 for p in [(0, 0), (2, 0)]))  # 2.0
```

</details>

## Exercise 4

What does the elbow method help choose?

*Hint: Number of clusters.*

<details>
<summary>✅ Solution</summary>

The value of **k** (number of clusters). You plot inertia vs k and pick the 'elbow'
where adding more clusters stops sharply reducing inertia.

</details>

## Exercise 5

Why scale features before K-Means?

*Hint: Distance fairness.*

<details>
<summary>✅ Solution</summary>

K-Means uses Euclidean distance, so a large-range feature dominates the clustering.
**Standardizing** gives each feature comparable influence.

</details>

## Exercise 6

Move centroid to the mean of assigned [(1,2),(3,4),(5,0)].

*Hint: Mean.*

<details>
<summary>✅ Solution</summary>

```python
pts = [(1, 2), (3, 4), (5, 0)]
print((sum(p[0] for p in pts)/3, sum(p[1] for p in pts)/3))  # (3.0, 2.0)
```

</details>

## Exercise 7

Why run K-Means multiple times?

*Hint: Random init.*

<details>
<summary>✅ Solution</summary>

Because the result depends on the **random initial centroids**, different runs can
converge to different (worse) solutions. Running several times (n_init) and keeping
the lowest-inertia result avoids bad local minima.

</details>

## Exercise 8

Name the two alternating steps of K-Means.

*Hint: Assign/update.*

<details>
<summary>✅ Solution</summary>

1) **Assignment** — assign each point to its nearest centroid. 2) **Update** — move
each centroid to the mean of its assigned points. Repeat until stable.

</details>


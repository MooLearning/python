# 74 — K-Nearest Neighbors (KNN): Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute Euclidean distance between (0,0) and (3,4).

*Hint: sqrt of sum of squares.*

<details>
<summary>✅ Solution</summary>

```python
import math
print(math.sqrt((3 - 0) ** 2 + (4 - 0) ** 2))  # 5.0
```

</details>

## Exercise 2

Majority vote of ['A','B','A'].

*Hint: Counter.*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
print(Counter(["A", "B", "A"]).most_common(1)[0][0])  # A
```

</details>

## Exercise 3

Find the 1 nearest of [1,5,9] to the query 4.

*Hint: min by distance.*

<details>
<summary>✅ Solution</summary>

```python
pts = [1, 5, 9]
print(min(pts, key=lambda p: abs(p - 4)))  # 5
```

</details>

## Exercise 4

KNN-regress: average the 2 nearest values to x=3 in [(1,10),(2,20),(5,50)].

*Hint: Mean of 2.*

<details>
<summary>✅ Solution</summary>

```python
data = [(1, 10), (2, 20), (5, 50)]
near = sorted(data, key=lambda it: abs(3 - it[0]))[:2]
print(sum(v for _, v in near) / 2)  # 15.0
```

</details>

## Exercise 5

Why scale features before KNN?

*Hint: Distance fairness.*

<details>
<summary>✅ Solution</summary>

KNN uses distances, so a feature with a large numeric range (e.g. salary in the
thousands) dominates one with a small range (e.g. age). **Scaling** puts all
features on comparable footing so each contributes fairly.

</details>

## Exercise 6

With k=1, what is the training accuracy usually?

*Hint: Memorization.*

<details>
<summary>✅ Solution</summary>

Usually **100%** — each training point's nearest neighbor is itself. That's a sign
k=1 can overfit; evaluate on a separate test set.

</details>

## Exercise 7

Compute Manhattan distance between (1,2) and (4,6).

*Hint: Sum of abs diffs.*

<details>
<summary>✅ Solution</summary>

```python
print(abs(1 - 4) + abs(2 - 6))  # 7
```

</details>

## Exercise 8

Is KNN a lazy or eager learner? Why?

*Hint: No training phase.*

<details>
<summary>✅ Solution</summary>

**Lazy.** It does no real training — it just stores the data and defers all
computation (distance + vote) to **prediction time**.

</details>


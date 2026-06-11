# 77 — Random Forests: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Draw a bootstrap sample of [1,2,3] (with replacement) using seed 0.

*Hint: random.choice x3.*

<details>
<summary>✅ Solution</summary>

```python
import random
random.seed(0)
data = [1, 2, 3]
print([random.choice(data) for _ in range(3)])
```

</details>

## Exercise 2

Majority-vote the predictions [1,1,0,1,0].

*Hint: Counter.*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
print(Counter([1, 1, 0, 1, 0]).most_common(1)[0][0])  # 1
```

</details>

## Exercise 3

What fraction of rows appear in a bootstrap sample on average?

*Hint: ~63%.*

<details>
<summary>✅ Solution</summary>

About **63.2%** (1 − 1/e). The remaining ~37% are 'out-of-bag' and can be used for
free validation.

</details>

## Exercise 4

Average the regression predictions [2.0,3.0,4.0].

*Hint: Mean.*

<details>
<summary>✅ Solution</summary>

```python
preds = [2.0, 3.0, 4.0]
print(sum(preds) / len(preds))  # 3.0
```

</details>

## Exercise 5

Why does a forest reduce variance vs a single tree?

*Hint: Decorrelation.*

<details>
<summary>✅ Solution</summary>

Averaging many **decorrelated** trees (each on different rows/features) cancels out
their individual errors/noise, so the ensemble is far more **stable** (lower
variance) than any single high-variance tree.

</details>

## Exercise 6

How many trees in RandomForestClassifier(n_estimators=50)?

*Hint: Read the param.*

<details>
<summary>✅ Solution</summary>

**50** trees — `n_estimators` sets the number of trees in the forest.

</details>

## Exercise 7

Combine 3 trees voting [A,B,A] — final class?

*Hint: Majority.*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
print(Counter(["A", "B", "A"]).most_common(1)[0][0])  # A
```

</details>

## Exercise 8

Name one advantage of random forests over a single decision tree.

*Hint: Stability.*

<details>
<summary>✅ Solution</summary>

Lower **variance / overfitting** (more accurate and stable), thanks to averaging
many decorrelated trees — at the cost of interpretability.

</details>


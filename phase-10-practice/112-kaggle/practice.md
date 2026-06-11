# 112 — Kaggle: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute accuracy of preds [1,0,1] vs truth [1,1,1].

*Hint: Mean correct.*

<details>
<summary>✅ Solution</summary>

```python
pred, true = [1, 0, 1], [1, 1, 1]
print(sum(p == t for p, t in zip(pred, true)) / len(true))  # 0.666
```

</details>

## Exercise 2

Make a baseline that predicts the majority class of [0,0,1].

*Hint: Most common.*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
print(Counter([0, 0, 1]).most_common(1)[0][0])  # 0
```

</details>

## Exercise 3

Format a submission row id=5, pred=1 as CSV.

*Hint: Join.*

<details>
<summary>✅ Solution</summary>

```python
print(f"{5},{1}")  # 5,1
```

</details>

## Exercise 4

Why trust local CV over the public leaderboard?

*Hint: Overfitting.*

<details>
<summary>✅ Solution</summary>

The public leaderboard is a **small, fixed slice** you can accidentally overfit by
tuning to it. Robust **cross-validation** estimates generalization better and tracks
the hidden private score.

</details>

## Exercise 5

What is the first model you should build?

*Hint: Baseline.*

<details>
<summary>✅ Solution</summary>

A **simple baseline** (e.g. predict the mean/majority, or a basic model) to
establish a score to beat and verify the end-to-end pipeline works.

</details>

## Exercise 6

Predict with threshold 4.0: is 6.5 hours a pass?

*Hint: Compare.*

<details>
<summary>✅ Solution</summary>

```python
print(int(6.5 >= 4.0))  # 1
```

</details>

## Exercise 7

Name one cause of data leakage.

*Hint: Any valid.*

<details>
<summary>✅ Solution</summary>

Fitting a scaler/encoder on test data, including a feature derived from the target,
or using future information — all leak info and inflate validation scores.

</details>

## Exercise 8

Compute mean CV score of [0.81,0.79,0.83].

*Hint: Mean.*

<details>
<summary>✅ Solution</summary>

```python
s = [0.81, 0.79, 0.83]
print(round(sum(s) / len(s), 3))  # 0.81
```

</details>


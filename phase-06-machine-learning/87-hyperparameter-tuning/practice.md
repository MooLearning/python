# 87 — Hyperparameter Tuning: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Is tree max_depth a parameter or hyperparameter?

*Hint: Set before training.*

<details>
<summary>✅ Solution</summary>

A **hyperparameter** — you set it before training. The split thresholds the tree
learns from data are its parameters.

</details>

## Exercise 2

How many combos in a 3x4 grid?

*Hint: Multiply.*

<details>
<summary>✅ Solution</summary>

```python
print(3 * 4)  # 12
```

</details>

## Exercise 3

Pick the best k by accuracy {1:0.6,3:0.8,5:0.7}.

*Hint: Max by value.*

<details>
<summary>✅ Solution</summary>

```python
scores = {1: 0.6, 3: 0.8, 5: 0.7}
print(max(scores, key=scores.get))  # 3
```

</details>

## Exercise 4

Why not tune on the test set?

*Hint: Leakage.*

<details>
<summary>✅ Solution</summary>

Tuning on the test set **leaks** its information into model selection, so the test
score no longer reflects true generalization. Use cross-validation for tuning and
reserve the test set for one final evaluation.

</details>

## Exercise 5

Grid has 5 lrs and 4 depths and 3-fold CV: how many fits?

*Hint: lr*depth*folds.*

<details>
<summary>✅ Solution</summary>

```python
print(5 * 4 * 3)  # 60
```

</details>

## Exercise 6

When does random search beat grid search?

*Hint: Many params.*

<details>
<summary>✅ Solution</summary>

When the search space is **large/high-dimensional**. Random search samples the space
more efficiently and often finds good configs with far fewer trials than exhaustive
grid search.

</details>

## Exercise 7

Sample one random (lr, depth) from lrs [0.1,1], depths [2,5] with seed 0.

*Hint: random.choice.*

<details>
<summary>✅ Solution</summary>

```python
import random
random.seed(0)
print((random.choice([0.1, 1]), random.choice([2, 5])))
```

</details>

## Exercise 8

After tuning, how many times evaluate on the test set?

*Hint: Once.*

<details>
<summary>✅ Solution</summary>

**Exactly once**, at the very end, to get an unbiased estimate of generalization.
Repeated peeking turns the test set into a validation set.

</details>


# 76 — Decision Trees: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute the Gini impurity of [A,A,B,B].

*Hint: 1 - sum p^2.*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
labels = ["A", "A", "B", "B"]
n = len(labels)
print(1 - sum((c / n) ** 2 for c in Counter(labels).values()))  # 0.5
```

</details>

## Exercise 2

What Gini value means a perfectly pure node?

*Hint: Single class.*

<details>
<summary>✅ Solution</summary>

**0.0** — all samples belong to one class, so there is no impurity.

</details>

## Exercise 3

Split [1,2,3,9,10] at threshold 5: list the two groups.

*Hint: <= vs >.*

<details>
<summary>✅ Solution</summary>

```python
data = [1, 2, 3, 9, 10]
print([x for x in data if x <= 5], [x for x in data if x > 5])
```

</details>

## Exercise 4

Predict with leaf rule: x[0]<=4 -> 'cat' else 'dog' for x=(6,).

*Hint: Compare.*

<details>
<summary>✅ Solution</summary>

```python
x = (6,)
print("cat" if x[0] <= 4 else "dog")  # dog
```

</details>

## Exercise 5

Why limit max_depth?

*Hint: Prevent overfitting.*

<details>
<summary>✅ Solution</summary>

Deep trees keep splitting until leaves are pure, memorizing noise (**overfitting**).
Limiting depth keeps the tree simpler so it **generalizes** to new data.

</details>

## Exercise 6

Compute weighted Gini: left [A,A] (gini0), right [A,B] (gini0.5), sizes 2 and 2.

*Hint: Weighted avg.*

<details>
<summary>✅ Solution</summary>

```python
print((2 * 0.0 + 2 * 0.5) / 4)  # 0.25
```

</details>

## Exercise 7

Do decision trees need feature scaling?

*Hint: Threshold-based.*

<details>
<summary>✅ Solution</summary>

**No.** Splits compare a feature to a threshold, which is unaffected by monotonic
scaling — so standardization/normalization is unnecessary for trees.

</details>

## Exercise 8

Majority class of leaf labels [1,1,1,0].

*Hint: Most common.*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
print(Counter([1, 1, 1, 0]).most_common(1)[0][0])  # 1
```

</details>


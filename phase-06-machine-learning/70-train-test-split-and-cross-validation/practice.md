# 70 — Train/Test Split and Cross-Validation: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Split [1..10] into 70% train / 30% test by slicing.

*Hint: int(0.7*n).*

<details>
<summary>✅ Solution</summary>

```python
data = list(range(1, 11))
s = int(0.7 * len(data))
print(data[:s], data[s:])
```

</details>

## Exercise 2

Shuffle [1,2,3,4,5] reproducibly with seed 0.

*Hint: random.seed + shuffle.*

<details>
<summary>✅ Solution</summary>

```python
import random
random.seed(0)
d = [1, 2, 3, 4, 5]; random.shuffle(d)
print(d)
```

</details>

## Exercise 3

How many samples per fold for n=20, k=5?

*Hint: n // k.*

<details>
<summary>✅ Solution</summary>

```python
print(20 // 5)  # 4
```

</details>

## Exercise 4

Average the CV scores [0.8,0.9,0.85].

*Hint: Mean.*

<details>
<summary>✅ Solution</summary>

```python
s = [0.8, 0.9, 0.85]
print(round(sum(s) / len(s), 3))  # 0.85
```

</details>

## Exercise 5

Why use cross-validation over a single split?

*Hint: Reliability.*

<details>
<summary>✅ Solution</summary>

A single split's score depends on luck (which rows landed in test). **K-fold CV**
averages over k different splits, giving a more **stable, reliable** estimate and
using every sample for both training and validation.

</details>

## Exercise 6

Generate 3-fold test index ranges for n=9.

*Hint: Equal thirds.*

<details>
<summary>✅ Solution</summary>

```python
n, k = 9, 3
size = n // k
print([list(range(i * size, (i + 1) * size)) for i in range(k)])
```

</details>

## Exercise 7

What is stratified splitting?

*Hint: Preserve class ratios.*

<details>
<summary>✅ Solution</summary>

**Stratified** splitting keeps the **proportion of each class** the same in every
fold/split as in the full dataset — crucial for imbalanced data so a fold isn't
missing a rare class.

</details>

## Exercise 8

Compute the std of CV scores [0.8,0.82,0.78].

*Hint: statistics.pstdev.*

<details>
<summary>✅ Solution</summary>

```python
import statistics as st
print(round(st.pstdev([0.8, 0.82, 0.78]), 4))
```

</details>


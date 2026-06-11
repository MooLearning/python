# 78 — Naive Bayes: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Apply Bayes: P(A|B)=P(B|A)P(A)/P(B) with P(B|A)=0.8,P(A)=0.25,P(B)=0.4.

*Hint: Plug in.*

<details>
<summary>✅ Solution</summary>

```python
print(0.8 * 0.25 / 0.4)  # 0.5
```

</details>

## Exercise 2

Why add 1 in Laplace smoothing?

*Hint: Avoid zero probability.*

<details>
<summary>✅ Solution</summary>

So a feature never seen with a class doesn't make its likelihood **0** (which would
zero out the entire product). Adding 1 to every count keeps all probabilities
positive.

</details>

## Exercise 3

Compute a Gaussian likelihood at x=mean (peak).

*Hint: Max density.*

<details>
<summary>✅ Solution</summary>

```python
import math
var = 4.0
print(round(1 / math.sqrt(2 * math.pi * var), 4))  # peak density
```

</details>

## Exercise 4

Sum log-probs log(0.5)+log(0.25).

*Hint: Logs add.*

<details>
<summary>✅ Solution</summary>

```python
import math
print(round(math.log(0.5) + math.log(0.25), 4))
```

</details>

## Exercise 5

Which NB variant for word-count features?

*Hint: Counts.*

<details>
<summary>✅ Solution</summary>

**Multinomial** Naive Bayes — designed for discrete **count** features such as word
frequencies in text.

</details>

## Exercise 6

Compute the prior P(spam) from 3 spam / 5 total docs.

*Hint: count/total.*

<details>
<summary>✅ Solution</summary>

```python
print(3 / 5)  # 0.6
```

</details>

## Exercise 7

Why use logs instead of multiplying probabilities?

*Hint: Underflow.*

<details>
<summary>✅ Solution</summary>

Multiplying many small probabilities **underflows** to 0 in floating point. Summing
their **logarithms** is numerically stable and monotonic (preserves the ranking).

</details>

## Exercise 8

Pick the class with higher score: spam=-5.2, ham=-6.1.

*Hint: Max (least negative).*

<details>
<summary>✅ Solution</summary>

```python
scores = {"spam": -5.2, "ham": -6.1}
print(max(scores, key=scores.get))  # spam
```

</details>


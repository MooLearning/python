# 89 — Ensemble Methods: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Majority-vote the labels ['spam','ham','spam'].

*Hint: Counter.*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
print(Counter(["spam", "ham", "spam"]).most_common(1)[0][0])  # spam
```

</details>

## Exercise 2

Average the probabilities [0.6,0.8,0.4] and threshold at 0.5.

*Hint: Mean + compare.*

<details>
<summary>✅ Solution</summary>

```python
probs = [0.6, 0.8, 0.4]
avg = sum(probs) / len(probs)
print(avg, 1 if avg >= 0.5 else 0)  # 0.6 1
```

</details>

## Exercise 3

Which ensemble reduces variance: bagging or boosting?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Bagging** reduces variance (averaging independent models). Boosting primarily
reduces **bias** by sequentially correcting errors.

</details>

## Exercise 4

Which reduces bias: bagging or boosting?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Boosting** — each model focuses on the previous models' mistakes, reducing bias
(at some risk of higher variance/overfitting).

</details>

## Exercise 5

What does a stacking meta-model take as input?

*Hint: Base predictions.*

<details>
<summary>✅ Solution</summary>

The **predictions (outputs) of the base models** — the meta-model learns how best to
combine them into a final prediction.

</details>

## Exercise 6

Why must ensemble members be diverse?

*Hint: Errors cancel.*

<details>
<summary>✅ Solution</summary>

If models make **different errors**, averaging/voting cancels them out. Identical
models make identical mistakes, so combining them adds nothing.

</details>

## Exercise 7

Tie-break a vote ['A','B'] — what's a simple rule?

*Hint: Any deterministic rule.*

<details>
<summary>✅ Solution</summary>

Use a deterministic tie-break: e.g. pick the class with higher prior, the
alphabetically first label, or fall back to the single most accurate base model.

</details>

## Exercise 8

3 models with 70% accuracy and independent errors: is the vote usually higher?

*Hint: Wisdom of crowds.*

<details>
<summary>✅ Solution</summary>

**Yes** — if their errors are independent, majority voting corrects cases where only
one model is wrong, pushing combined accuracy **above 70%** (wisdom of crowds).

</details>


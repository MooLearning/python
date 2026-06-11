# 69 — ML Overview: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Classify by threshold: predict 'big' if x>10 else 'small' for x=7.

*Hint: Compare to threshold.*

<details>
<summary>✅ Solution</summary>

```python
def predict(x):
    return "big" if x > 10 else "small"
print(predict(7))  # small
```

</details>

## Exercise 2

Is spam detection supervised or unsupervised? Why?

*Hint: Labeled emails.*

<details>
<summary>✅ Solution</summary>

**Supervised** — you train on emails already **labeled** spam/not-spam, then predict
labels for new emails. (Grouping unlabeled emails into themes would be unsupervised.)

</details>

## Exercise 3

Compute MAE between predictions [2,4] and truth [3,5].

*Hint: Mean abs error.*

<details>
<summary>✅ Solution</summary>

```python
pred, true = [2, 4], [3, 5]
print(sum(abs(p - t) for p, t in zip(pred, true)) / len(true))  # 1.0
```

</details>

## Exercise 4

Learn a slope from [(1,3),(2,6)] as avg(y/x).

*Hint: Average the ratios.*

<details>
<summary>✅ Solution</summary>

```python
data = [(1, 3), (2, 6)]
print(sum(y / x for x, y in data) / len(data))  # 3.0
```

</details>

## Exercise 5

Name the target (label) vs features for predicting house price from area, rooms.

*Hint: y vs X.*

<details>
<summary>✅ Solution</summary>

**Label (y):** house price. **Features (X):** area, number of rooms. The model
learns a mapping X → y from past sales.

</details>

## Exercise 6

Decide: clustering customers by behavior is which ML type?

*Hint: No labels.*

<details>
<summary>✅ Solution</summary>

**Unsupervised learning** (clustering) — there are no predefined labels; the
algorithm discovers groups from the data itself.

</details>

## Exercise 7

Predict with model y=2x+1 at x=4.

*Hint: Plug in.*

<details>
<summary>✅ Solution</summary>

```python
def model(x): return 2 * x + 1
print(model(4))  # 9
```

</details>

## Exercise 8

Why split data into train and test sets?

*Hint: Measure generalization.*

<details>
<summary>✅ Solution</summary>

To estimate how the model performs on **unseen** data. Testing on training data
rewards memorization; a held-out test set measures real **generalization**.

</details>


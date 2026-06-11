# 85 — Classification Metrics: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute accuracy: 8 correct of 10.

*Hint: correct/total.*

<details>
<summary>✅ Solution</summary>

```python
print(8 / 10)  # 0.8
```

</details>

## Exercise 2

Compute precision with TP=5, FP=5.

*Hint: TP/(TP+FP).*

<details>
<summary>✅ Solution</summary>

```python
print(5 / (5 + 5))  # 0.5
```

</details>

## Exercise 3

Compute recall with TP=5, FN=15.

*Hint: TP/(TP+FN).*

<details>
<summary>✅ Solution</summary>

```python
print(5 / (5 + 15))  # 0.25
```

</details>

## Exercise 4

Compute F1 with precision=0.5, recall=0.25.

*Hint: Harmonic mean.*

<details>
<summary>✅ Solution</summary>

```python
p, r = 0.5, 0.25
print(round(2 * p * r / (p + r), 3))  # 0.333
```

</details>

## Exercise 5

Count TP in true=[1,0,1], pred=[1,1,1].

*Hint: Both 1.*

<details>
<summary>✅ Solution</summary>

```python
t, p = [1, 0, 1], [1, 1, 1]
print(sum(1 for a, b in zip(t, p) if a == 1 and b == 1))  # 2
```

</details>

## Exercise 6

Why is accuracy bad for 99% negative data?

*Hint: Majority predictor.*

<details>
<summary>✅ Solution</summary>

Always predicting the majority class scores **99% accuracy** while catching **none**
of the rare positives. Accuracy hides this failure — precision/recall expose it.

</details>

## Exercise 7

Which metric matters most for cancer screening?

*Hint: Cost of FN.*

<details>
<summary>✅ Solution</summary>

**Recall (sensitivity)** — missing a real case (false negative) is dangerous, so you
want to catch as many true positives as possible, even at some precision cost.

</details>

## Exercise 8

What ROC-AUC value means random guessing?

*Hint: Baseline.*

<details>
<summary>✅ Solution</summary>

**0.5** — equivalent to a coin flip. 1.0 is a perfect ranker; below 0.5 is worse
than random (predictions inverted).

</details>


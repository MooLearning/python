# 73 — Logistic Regression: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute sigmoid(0).

*Hint: 1/(1+e^0).*

<details>
<summary>✅ Solution</summary>

```python
import math
print(1 / (1 + math.exp(-0)))  # 0.5
```

</details>

## Exercise 2

Classify probability 0.7 with threshold 0.5.

*Hint: Compare.*

<details>
<summary>✅ Solution</summary>

```python
p = 0.7
print(1 if p >= 0.5 else 0)  # 1
```

</details>

## Exercise 3

Compute sigmoid(2) rounded to 3 dp.

*Hint: Formula.*

<details>
<summary>✅ Solution</summary>

```python
import math
print(round(1 / (1 + math.exp(-2)), 3))  # 0.881
```

</details>

## Exercise 4

Why is it called regression but used for classification?

*Hint: Linear score.*

<details>
<summary>✅ Solution</summary>

It performs linear **regression on the log-odds** (a continuous score), then maps
that score to a probability with the sigmoid. The continuous-score fitting is the
'regression'; thresholding the probability gives a class.

</details>

## Exercise 5

Compute the linear score w*x+b for w=2,x=3,b=-5.

*Hint: Dot + bias.*

<details>
<summary>✅ Solution</summary>

```python
print(2 * 3 + (-5))  # 1
```

</details>

## Exercise 6

At what score z does sigmoid output exactly 0.5?

*Hint: z=0.*

<details>
<summary>✅ Solution</summary>

At **z = 0**, sigmoid(0) = 0.5 — that's the decision boundary where the model is
maximally uncertain.

</details>

## Exercise 7

Predicted 0.9 for true label 1 — is log loss small or large?

*Hint: Confident correct.*

<details>
<summary>✅ Solution</summary>

**Small.** The model was confident and correct, so cross-entropy
(-log 0.9 ≈ 0.105) is low. Confident *wrong* predictions get large loss.

</details>

## Exercise 8

Move the threshold to 0.3: does recall go up or down?

*Hint: Lower bar.*

<details>
<summary>✅ Solution</summary>

**Recall goes up** (and precision usually down): a lower threshold labels more
samples positive, catching more true positives but also more false positives.

</details>


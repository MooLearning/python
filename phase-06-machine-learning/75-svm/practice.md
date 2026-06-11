# 75 — Support Vector Machines (SVM): Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Classify (3,3) with boundary x+y-5: which side?

*Hint: Sign of score.*

<details>
<summary>✅ Solution</summary>

```python
score = 3 + 3 - 5
print(1 if score >= 0 else 0, score)  # 1 1
```

</details>

## Exercise 2

What are support vectors?

*Hint: Closest points.*

<details>
<summary>✅ Solution</summary>

The training points **closest to the decision boundary** — they 'support' (define)
the margin. Moving or removing them changes the boundary; other points don't.

</details>

## Exercise 3

Compute the score w·x+b for w=(2,-1), x=(3,4), b=1.

*Hint: Dot + bias.*

<details>
<summary>✅ Solution</summary>

```python
w, x, b = (2, -1), (3, 4), 1
print(sum(wi * xi for wi, xi in zip(w, x)) + b)  # 3
```

</details>

## Exercise 4

Why use the RBF kernel?

*Hint: Non-linear data.*

<details>
<summary>✅ Solution</summary>

The **RBF kernel** maps data into a higher-dimensional space where **non-linearly
separable** classes (like concentric circles) become separable by a hyperplane.

</details>

## Exercise 5

A perceptron update: w=[0,0], y=1, x=(2,3), lr=0.1. New w?

*Hint: w += lr*y*x.*

<details>
<summary>✅ Solution</summary>

```python
w = [0.0, 0.0]; y, x, lr = 1, (2, 3), 0.1
w = [w[i] + lr * y * x[i] for i in range(2)]
print(w)  # [0.2, 0.3]
```

</details>

## Exercise 6

What does a large C do in an SVM?

*Hint: Less regularization.*

<details>
<summary>✅ Solution</summary>

A **large C** penalizes misclassifications heavily, producing a **narrower margin**
that fits training data more tightly (less regularization, more overfitting risk).
Small C allows a wider margin with some errors.

</details>

## Exercise 7

Is the margin wider with C small or large?

*Hint: Tradeoff.*

<details>
<summary>✅ Solution</summary>

**Smaller C** → wider margin (more tolerance for misclassified points). Larger C →
narrower margin that classifies training points more strictly.

</details>

## Exercise 8

Predict class of (1,1) with perceptron w=[0.2,0.3], b=-1.

*Hint: Sign.*

<details>
<summary>✅ Solution</summary>

```python
w, b = [0.2, 0.3], -1
print(1 if w[0]*1 + w[1]*1 + b >= 0 else -1)  # -1
```

</details>


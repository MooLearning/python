# 72 — Linear Regression

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Linear regression** fits a straight line (or hyperplane) `y = w·x + b` to predict a continuous target by minimizing the **mean squared error**. With one feature it has a closed-form solution (least squares: slope and intercept from the data); with many features you solve the normal equations or use **gradient descent**. It's the simplest, most interpretable regression model.

## Why it matters

It's the entry point to predictive modeling: fast, interpretable (each weight is a feature's effect), and the foundation for logistic regression, regularization, and neural networks. Many real relationships are approximately linear.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Line equation** — y = w·x + b: weight (slope) and bias (intercept).
- **Least squares** — Choose w, b to minimize summed squared errors.
- **Closed form** — slope = cov(x,y)/var(x); intercept = ȳ − slope·x̄.
- **Gradient descent** — Iteratively step weights downhill on the MSE.
- **R² score** — Fraction of variance explained (1 = perfect, 0 = mean).
- **Residuals** — Actual − predicted; should look like random noise.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
# Hours studied vs exam score
xs = [1, 2, 3, 4, 5]
ys = [52, 60, 67, 75, 81]

n = len(xs)
x_bar = sum(xs) / n
y_bar = sum(ys) / n

# slope = sum((xi-x̄)(yi-ȳ)) / sum((xi-x̄)^2)
num = sum((x - x_bar) * (y - y_bar) for x, y in zip(xs, ys))
den = sum((x - x_bar) ** 2 for x in xs)
slope = num / den
intercept = y_bar - slope * x_bar
print(f"y = {slope:.2f} * x + {intercept:.2f}")

def predict(x):
    return slope * x + intercept

# R^2 = 1 - SS_res / SS_tot
ss_res = sum((y - predict(x)) ** 2 for x, y in zip(xs, ys))
ss_tot = sum((y - y_bar) ** 2 for y in ys)
print("R^2:", round(1 - ss_res / ss_tot, 4))
print("predict 6 hrs ->", round(predict(6), 1))
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Linear regression assumes a roughly linear relationship — check residual plots.
- ⚠️ Outliers heavily distort least squares (squared errors punish big misses).
- ⚠️ Highly correlated features (multicollinearity) make coefficients unstable.
- ⚠️ Gradient descent needs a sensible learning rate and scaled features to converge.
- ⚠️ Extrapolating far outside the training range is unreliable — the line keeps going forever.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


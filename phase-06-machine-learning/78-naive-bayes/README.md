# 78 — Naive Bayes

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Naive Bayes** classifiers apply **Bayes' theorem** with a 'naive' assumption: features are **conditionally independent** given the class. They estimate P(class) and P(feature|class) from training data, then pick the class with the highest posterior. Variants: **Gaussian** (continuous features), **Multinomial** (counts, e.g. word frequencies), and **Bernoulli** (binary features).

## Why it matters

Despite the simplistic independence assumption, Naive Bayes is fast, needs little data, and works remarkably well for text (spam filtering, sentiment). It's a classic strong baseline for high-dimensional sparse data.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Bayes' theorem** — P(class|x) ∝ P(x|class)·P(class).
- **Conditional independence** — Assume features don't interact given the class.
- **Prior** — Base rate of each class P(class).
- **Likelihood** — P(feature|class), modeled by Gaussian/Multinomial/Bernoulli.
- **Laplace smoothing** — Add 1 to counts so unseen features don't zero out.
- **Log probabilities** — Sum logs instead of multiplying to avoid underflow.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import math
import statistics as st

# features: (height_ft, weight_lb) -> class
train = [((5.0, 100), "cat"), ((5.5, 110), "cat"), ((4.8, 95), "cat"),
         ((6.5, 200), "dog"), ((7.0, 220), "dog"), ((6.8, 210), "dog")]

classes = set(label for _, label in train)
priors, stats = {}, {}
for c in classes:
    feats = [f for f, label in train if label == c]
    priors[c] = len(feats) / len(train)
    # mean and variance of each feature column for this class
    stats[c] = [(st.mean(col), st.pvariance(col) or 1e-6) for col in zip(*feats)]

def gaussian(x, mean, var):
    return math.exp(-(x - mean) ** 2 / (2 * var)) / math.sqrt(2 * math.pi * var)

def predict(x):
    best_c, best_p = None, -1.0
    for c in classes:
        p = priors[c]
        for xi, (m, v) in zip(x, stats[c]):
            p *= gaussian(xi, m, v)
        if p > best_p:
            best_c, best_p = c, p
    return best_c

print("(5.2, 105) ->", predict((5.2, 105)))   # cat
print("(6.9, 205) ->", predict((6.9, 205)))   # dog
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Without smoothing, an unseen feature gives probability 0 and zeros the whole product.
- ⚠️ Multiply many small probabilities → underflow; sum LOG-probabilities instead.
- ⚠️ The independence assumption is usually false, but the classifier is still useful.
- ⚠️ Use the RIGHT variant: Gaussian for continuous, Multinomial for counts, Bernoulli for binary.
- ⚠️ Probabilities are often poorly calibrated (too extreme) — trust the ranking, not the value.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


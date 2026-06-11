# 69 — ML Overview

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Machine learning** is getting computers to learn patterns from data instead of being explicitly programmed with rules. The main families are **supervised** (learn from labeled examples to predict — classification & regression), **unsupervised** (find structure in unlabeled data — clustering, dimensionality reduction), and **reinforcement** (learn by trial and reward). The workflow: data → features → train a model → evaluate → predict.

## Why it matters

ML powers recommendations, fraud detection, language models, vision, and forecasting. Knowing the categories and the train/evaluate/predict loop frames every later topic and helps you pick the right tool for a problem.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Supervised** — Labeled data; predict a target (classification/regression).
- **Unsupervised** — No labels; find groups or structure (clustering, PCA).
- **Reinforcement** — Learn actions from rewards via trial and error.
- **Features & labels** — Inputs (X) and the answer to predict (y).
- **Train vs predict** — Fit parameters on training data, then predict on new data.
- **Generalization** — Doing well on UNSEEN data, not just memorizing training data.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
# Learn a threshold to classify animals as 'cat' or 'dog' by weight (kg).
train = [(4, "cat"), (5, "cat"), (3.5, "cat"), (20, "dog"), (25, "dog"), (18, "dog")]

# 'Training' = compute the midpoint between class averages
cats = [w for w, label in train if label == "cat"]
dogs = [w for w, label in train if label == "dog"]
threshold = (sum(cats) / len(cats) + sum(dogs) / len(dogs)) / 2
print("learned threshold:", round(threshold, 2), "kg")

def predict(weight):
    return "dog" if weight > threshold else "cat"

# Predict on NEW, unseen examples
for w in [6, 15, 22]:
    print(f"{w} kg -> {predict(w)}")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ More data and better features usually beat a fancier algorithm — start simple.
- ⚠️ Evaluate on data the model never saw; training accuracy alone is misleading.
- ⚠️ Garbage labels = garbage model; supervised learning is only as good as its labels.
- ⚠️ Not every problem is ML — if simple rules work, use them; ML adds complexity.
- ⚠️ Correlation learned by a model isn't causation — be careful about deployment decisions.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


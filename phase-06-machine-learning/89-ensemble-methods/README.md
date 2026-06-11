# 89 — Ensemble Methods

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Ensemble methods** combine multiple models into one stronger predictor. **Voting/averaging** blends diverse models (hard vote = majority label, soft vote = average probabilities). **Bagging** trains the same model on bootstrap samples to cut variance (random forests). **Boosting** trains models sequentially to fix errors and cut bias (gradient boosting). **Stacking** trains a meta-model on base models' outputs.

## Why it matters

Ensembles almost always beat single models — they win Kaggle competitions and power production systems — by exploiting model diversity so individual errors cancel out. Understanding the four patterns lets you mix models effectively.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Voting** — Combine different models: majority (hard) or averaged probs (soft).
- **Bagging** — Same model on bootstrap samples; reduces variance.
- **Boosting** — Sequential models that fix predecessors; reduces bias.
- **Stacking** — A meta-model learns to combine base models' predictions.
- **Diversity** — Ensembles help most when members make different errors.
- **Wisdom of crowds** — Averaging many decent, diverse models beats one.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
from collections import Counter

# Three simple 'models' each return a class label for an input.
def model_a(x): return "spam" if x > 5 else "ham"
def model_b(x): return "spam" if x > 3 else "ham"
def model_c(x): return "spam" if x > 7 else "ham"

def hard_vote(x):
    votes = [model_a(x), model_b(x), model_c(x)]
    return Counter(votes).most_common(1)[0][0], votes

for x in [2, 6, 8]:
    decision, votes = hard_vote(x)
    print(f"x={x}: votes={votes} -> {decision}")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Ensembles help only if members are DIVERSE — combining identical models gains nothing.
- ⚠️ Soft voting needs well-calibrated probabilities; otherwise hard voting can be safer.
- ⚠️ Stacking can overfit if the meta-model sees the same data base models trained on — use CV folds.
- ⚠️ Ensembles cost more compute/memory and are harder to interpret and deploy.
- ⚠️ A bad model can drag down a vote — weight or drop weak members.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


# 85 — Classification Metrics

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Classification metrics** judge how well a classifier labels data. From the **confusion matrix** (TP, FP, TN, FN) come **accuracy** (overall correct), **precision** (of predicted positives, how many are right), **recall/sensitivity** (of actual positives, how many were caught), and **F1** (their harmonic mean). **ROC-AUC** summarizes the precision/recall trade-off across thresholds.

## Why it matters

Accuracy alone lies on imbalanced data (99% accuracy by always predicting the majority). Precision vs recall captures the cost of false positives vs false negatives — central to medical, fraud, and safety decisions.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Confusion matrix** — Counts of TP, FP, TN, FN.
- **Accuracy** — (TP+TN)/all — fraction correct.
- **Precision** — TP/(TP+FP) — correctness of positive predictions.
- **Recall** — TP/(TP+FN) — coverage of actual positives.
- **F1 score** — Harmonic mean of precision and recall.
- **ROC-AUC** — Ranking quality across all thresholds (0.5 = random, 1 = perfect).

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

TP = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
TN = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 0)
FP = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
FN = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
print(f"TP={TP} FP={FP} TN={TN} FN={FN}")

accuracy = (TP + TN) / len(y_true)
precision = TP / (TP + FP) if (TP + FP) else 0
recall = TP / (TP + FN) if (TP + FN) else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0
print(f"accuracy : {accuracy:.3f}")
print(f"precision: {precision:.3f}")
print(f"recall   : {recall:.3f}")
print(f"F1       : {f1:.3f}")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Accuracy is misleading on imbalanced classes — a constant predictor can score high.
- ⚠️ Precision and recall trade off; lowering the threshold raises recall but lowers precision.
- ⚠️ F1 balances precision/recall but ignores true negatives — not always what you want.
- ⚠️ Pick the metric by cost: false negatives in cancer screening matter more than false positives.
- ⚠️ ROC-AUC needs scores/probabilities, not hard labels; PR-AUC is better for heavy imbalance.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


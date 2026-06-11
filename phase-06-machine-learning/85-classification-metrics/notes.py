# ======================================================================
# 85 — Classification Metrics  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: Confusion matrix and metrics from scratch
# ----------------------------------------------------------------------
print("\n--- Example 1: Confusion matrix and metrics from scratch ---")
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

# ----------------------------------------------------------------------
# Example 2: Why accuracy misleads on imbalanced data
# ----------------------------------------------------------------------
print("\n--- Example 2: Why accuracy misleads on imbalanced data ---")
# 95 negatives, 5 positives. A lazy model predicts ALL negative.
y_true = [0] * 95 + [1] * 5
y_pred = [0] * 100                       # never predicts positive

accuracy = sum(1 for t, p in zip(y_true, y_pred) if t == p) / len(y_true)
TP = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
FN = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
recall = TP / (TP + FN)

print(f"accuracy: {accuracy:.0%}  <- looks great!")
print(f"recall  : {recall:.0%}  <- but it catches ZERO positives")
print("Lesson: on imbalanced data, track precision/recall, not just accuracy.")

# ----------------------------------------------------------------------
# Example 3: Metrics with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: Metrics with scikit-learn ---")
try:
    from sklearn.metrics import (confusion_matrix, classification_report,
                                 accuracy_score, roc_auc_score)
    y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
    y_scores = [.9, .1, .8, .4, .2, .7, .6, .3, .95, .15]   # probabilities

    print("confusion matrix:\n", confusion_matrix(y_true, y_pred))
    print("accuracy:", round(accuracy_score(y_true, y_pred), 3))
    print("ROC-AUC :", round(roc_auc_score(y_true, y_scores), 3))
    print("\nreport:\n", classification_report(y_true, y_pred, zero_division=0))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")

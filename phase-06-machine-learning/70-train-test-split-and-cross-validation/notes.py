# ======================================================================
# 70 — Train/Test Split and Cross-Validation  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: Manual train/test split with shuffling
# ----------------------------------------------------------------------
print("\n--- Example 1: Manual train/test split with shuffling ---")
import random

data = list(range(1, 11))          # 10 samples
random.seed(42)
random.shuffle(data)               # shuffle so the split isn't biased

split = int(0.8 * len(data))       # 80% train
train, test = data[:split], data[split:]
print("train:", train)             # 8 items
print("test :", test)              # 2 items
print(f"{len(train)} train / {len(test)} test")

# ----------------------------------------------------------------------
# Example 2: K-fold cross-validation indices (pure Python)
# ----------------------------------------------------------------------
print("\n--- Example 2: K-fold cross-validation indices (pure Python) ---")
def k_fold_indices(n, k):
    fold_size = n // k
    indices = list(range(n))
    folds = []
    for i in range(k):
        start = i * fold_size
        # last fold absorbs the remainder
        end = n if i == k - 1 else start + fold_size
        test_idx = indices[start:end]
        train_idx = indices[:start] + indices[end:]
        folds.append((train_idx, test_idx))
    return folds

for fold, (tr, te) in enumerate(k_fold_indices(10, 5), 1):
    print(f"fold {fold}: test={te}, train has {len(tr)} samples")

# Simulate scoring each fold and averaging
scores = [0.80, 0.85, 0.78, 0.82, 0.88]
print("\nCV mean:", round(sum(scores) / len(scores), 3))

# ----------------------------------------------------------------------
# Example 3: scikit-learn split and cross_val_score
# ----------------------------------------------------------------------
print("\n--- Example 3: scikit-learn split and cross_val_score ---")
try:
    from sklearn.model_selection import train_test_split, cross_val_score, KFold
    from sklearn.linear_model import LogisticRegression
    from sklearn.datasets import make_classification

    X, y = make_classification(n_samples=100, n_features=4, random_state=0)

    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.2, random_state=0, stratify=y)
    print("train size:", len(X_tr), "test size:", len(X_te))

    model = LogisticRegression(max_iter=1000)
    model.fit(X_tr, y_tr)
    print("test accuracy:", round(model.score(X_te, y_te), 3))

    # 5-fold cross-validation
    cv = cross_val_score(model, X, y, cv=KFold(5, shuffle=True, random_state=0))
    print("CV scores:", cv.round(3).tolist())
    print("CV mean:", round(cv.mean(), 3), "+/-", round(cv.std(), 3))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")

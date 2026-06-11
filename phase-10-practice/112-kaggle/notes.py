# ======================================================================
# 112 — Kaggle  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: pandas, scikit-learn
# Install:  pip install pandas scikit-learn

# ----------------------------------------------------------------------
# Example 1: The Kaggle workflow
# ----------------------------------------------------------------------
print("\n--- Example 1: The Kaggle workflow ---")
steps = [
    "1. Understand the problem and the evaluation metric",
    "2. EDA: explore distributions, missing values, correlations",
    "3. Build a BASELINE (e.g. predict the mean / a simple model)",
    "4. Set up cross-validation you trust",
    "5. Feature engineering + better models",
    "6. Tune hyperparameters; try ensembling",
    "7. Generate predictions on the test set",
    "8. Write submission.csv and submit",
]
for s in steps:
    print(s)
print("\nGolden rule: trust your local CV score over the public leaderboard.")

# ----------------------------------------------------------------------
# Example 2: A baseline pipeline on toy data (pure Python)
# ----------------------------------------------------------------------
print("\n--- Example 2: A baseline pipeline on toy data (pure Python) ---")
# Toy 'competition': predict pass(1)/fail(0) from hours studied.
train = [(1, 0), (2, 0), (3, 0), (5, 1), (6, 1), (7, 1), (2.5, 0), (5.5, 1)]
test_ids_features = [(101, 1.5), (102, 4.0), (103, 6.5)]   # no labels

# Baseline: a single threshold learned from the class means
pass_hours = [h for h, y in train if y == 1]
fail_hours = [h for h, y in train if y == 0]
threshold = (sum(pass_hours) / len(pass_hours) +
             sum(fail_hours) / len(fail_hours)) / 2
print("learned threshold:", round(threshold, 2))

# Validate on the training data (a real comp uses a held-out split/CV)
acc = sum(1 for h, y in train if (h >= threshold) == y) / len(train)
print("train accuracy:", round(acc, 3))

# Generate a submission file (id,prediction)
print("\nsubmission.csv:")
print("id,passed")
for id_, hours in test_ids_features:
    print(f"{id_},{int(hours >= threshold)}")

# ----------------------------------------------------------------------
# Example 3: A real pipeline with pandas + scikit-learn (template)
# ----------------------------------------------------------------------
print("\n--- Example 3: A real pipeline with pandas + scikit-learn (template) ---")
try:
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import cross_val_score

    # In a real comp: train = pd.read_csv("train.csv"); test = pd.read_csv("test.csv")
    train = pd.DataFrame({
        "feature1": [1, 2, 3, 4, 5, 6, 7, 8],
        "feature2": [2, 1, 4, 3, 6, 5, 8, 7],
        "target":   [0, 0, 0, 0, 1, 1, 1, 1],
    })
    X = train[["feature1", "feature2"]]
    y = train["target"]

    model = RandomForestClassifier(n_estimators=50, random_state=0)
    scores = cross_val_score(model, X, y, cv=4)
    print("CV accuracy:", round(scores.mean(), 3), "+/-", round(scores.std(), 3))

    model.fit(X, y)                       # fit on all training data
    # submission = pd.DataFrame({"id": test.id, "target": model.predict(X_test)})
    # submission.to_csv("submission.csv", index=False)
    print("model trained — ready to predict and write submission.csv")
except ImportError:
    print("pandas/sklearn not installed — run: pip install pandas scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")

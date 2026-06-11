# ======================================================================
# 113 — End-to-End Projects  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: The ML project lifecycle
# ----------------------------------------------------------------------
print("\n--- Example 1: The ML project lifecycle ---")
lifecycle = [
    ("Problem",   "Predict if a student passes from hours studied; metric = accuracy"),
    ("Data",      "Collect (hours, passed) records; clean and split"),
    ("EDA",       "Check ranges, balance, correlation of hours vs outcome"),
    ("Features",  "Maybe add hours^2, sleep, attendance"),
    ("Model",     "Baseline threshold -> logistic regression"),
    ("Evaluate",  "Accuracy on a held-out test set; inspect errors"),
    ("Deploy",    "Save params, wrap predict() in an API"),
    ("Monitor",   "Watch for drift; retrain as new data arrives"),
]
for stage, detail in lifecycle:
    print(f"{stage:9}: {detail}")

# ----------------------------------------------------------------------
# Example 2: A COMPLETE mini-project (data -> train -> save -> predict)
# ----------------------------------------------------------------------
print("\n--- Example 2: A COMPLETE mini-project (data -> train -> save -> predict) ---")
import json, tempfile, os, math

# 1. DATA: (hours studied, passed)
data = [(1, 0), (2, 0), (3, 0), (4, 1), (5, 1), (6, 1), (2.5, 0), (4.5, 1)]

# 2. SPLIT into train / test
train, test = data[:6], data[6:]

# 3. TRAIN a logistic regression with gradient descent
def sigmoid(z): return 1 / (1 + math.exp(-z))
w, b, lr = 0.0, 0.0, 0.3
for _ in range(5000):
    gw = gb = 0.0
    for x, y in train:
        p = sigmoid(w * x + b)
        gw += (p - y) * x; gb += (p - y)
    w -= lr * gw / len(train); b -= lr * gb / len(train)

# 4. EVALUATE on held-out test data
acc = sum(1 for x, y in test if (sigmoid(w * x + b) >= 0.5) == y) / len(test)
print(f"trained model: w={w:.3f}, b={b:.3f}")
print("test accuracy:", acc)

# 5. SAVE the model artifact
path = os.path.join(tempfile.gettempdir(), "study_model.json")
with open(path, "w") as f:
    json.dump({"w": w, "b": b}, f)

# 6. LOAD + PREDICT (what a deployed service does)
with open(path) as f:
    m = json.load(f)
def predict(hours):
    return "pass" if sigmoid(m["w"] * hours + m["b"]) >= 0.5 else "fail"
print("predict 3.5 hrs ->", predict(3.5))
print("predict 5.0 hrs ->", predict(5.0))

# ----------------------------------------------------------------------
# Example 3: A clean project structure and reproducibility
# ----------------------------------------------------------------------
print("\n--- Example 3: A clean project structure and reproducibility ---")
structure = """\
my-ml-project/
|-- README.md              # problem, results, how to run
|-- requirements.txt       # pinned dependencies
|-- data/
|   |-- raw/               # original, never edited
|   |-- processed/         # cleaned, model-ready
|-- notebooks/
|   |-- 01-eda.ipynb
|-- src/
|   |-- data.py            # load & clean
|   |-- features.py        # feature engineering
|   |-- train.py           # train & save model
|   |-- predict.py         # load model & serve
|-- models/                # saved artifacts
|-- tests/
"""
print(structure)
print("Reproducibility checklist:")
for item in ["Fix random seeds", "Pin dependency versions",
             "Version data + code together", "Document run steps in README",
             "Separate raw vs processed data"]:
    print("  [x]", item)

print("\nDone! Tip: change values above and run again to learn by experiment.")

# ======================================================================
# 65 — Data Preprocessing  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: Min-max scaling and standardization (pure Python)
# ----------------------------------------------------------------------
print("\n--- Example 1: Min-max scaling and standardization (pure Python) ---")
import statistics as st

data = [10, 20, 30, 40, 50]

# Min-max scaling to [0, 1]
lo, hi = min(data), max(data)
minmax = [(x - lo) / (hi - lo) for x in data]
print("min-max     :", minmax)            # [0.0, 0.25, 0.5, 0.75, 1.0]

# Standardization (z-scores): mean 0, std 1
mu = st.mean(data)
sigma = st.pstdev(data)                    # population std
standardized = [(x - mu) / sigma for x in data]
print("standardized:", [round(z, 3) for z in standardized])
print("new mean ~", round(st.mean(standardized), 6))   # ~0

# ----------------------------------------------------------------------
# Example 2: Label and one-hot encoding (pure Python)
# ----------------------------------------------------------------------
print("\n--- Example 2: Label and one-hot encoding (pure Python) ---")
colors = ["red", "green", "blue", "green", "red"]

# Label encoding: category -> integer
categories = sorted(set(colors))           # ['blue', 'green', 'red']
label_map = {c: i for i, c in enumerate(categories)}
labels = [label_map[c] for c in colors]
print("label map :", label_map)
print("encoded   :", labels)               # [2, 1, 0, 1, 2]

# One-hot encoding: each category -> its own 0/1 column
def one_hot(value):
    return [1 if value == c else 0 for c in categories]

print("one-hot 'red'  :", one_hot("red"))    # [0, 0, 1]
print("one-hot 'blue' :", one_hot("blue"))   # [1, 0, 0]
for c in colors:
    print(f"  {c:6} -> {one_hot(c)}")

# ----------------------------------------------------------------------
# Example 3: The same with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: The same with scikit-learn ---")
try:
    from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
    from sklearn.model_selection import train_test_split

    X = [[10], [20], [30], [40], [50]]

    scaler = StandardScaler().fit(X)       # learn mean/std
    print("standardized:\n", scaler.transform(X).ravel().round(3))

    mm = MinMaxScaler().fit(X)
    print("min-max     :", mm.transform(X).ravel())

    le = LabelEncoder()
    print("labels      :", le.fit_transform(["red", "green", "blue", "red"]))

    # Train/test split (fit scalers on train only!)
    data = list(range(10))
    train, test = train_test_split(data, test_size=0.3, random_state=0)
    print("train:", sorted(train), "test:", sorted(test))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")

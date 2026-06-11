# ======================================================================
# 66 — Exploratory Data Analysis (EDA)  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: pandas
# Install:  pip install pandas

# ----------------------------------------------------------------------
# Example 1: Summary statistics in pure Python
# ----------------------------------------------------------------------
print("\n--- Example 1: Summary statistics in pure Python ---")
import statistics as st

ages = [23, 25, 31, 35, 41, 22, 29, 33, 60, 27]

print("count :", len(ages))
print("mean  :", round(st.mean(ages), 2))
print("median:", st.median(ages))
print("stdev :", round(st.stdev(ages), 2))
print("min   :", min(ages), " max:", max(ages))

# Quartiles (Q1, Q2, Q3)
q1, q2, q3 = st.quantiles(ages, n=4)
print(f"quartiles: Q1={q1}, Q2={q2}, Q3={q3}")
print("range :", max(ages) - min(ages))

# ----------------------------------------------------------------------
# Example 2: Frequency counts and a text histogram
# ----------------------------------------------------------------------
print("\n--- Example 2: Frequency counts and a text histogram ---")
from collections import Counter

grades = ["A", "B", "A", "C", "B", "A", "B", "D", "A", "C"]

# Value counts (cardinality + distribution of a categorical)
counts = Counter(grades)
print("counts:", dict(counts))
print("unique:", len(counts), "| most common:", counts.most_common(1)[0])

# Text histogram of a numeric column
scores = [55, 62, 71, 73, 78, 81, 85, 88, 91, 95]
print("\nscore histogram:")
for lo in range(50, 100, 10):
    n = sum(1 for s in scores if lo <= s < lo + 10)
    print(f"  {lo}-{lo+9}: {'#' * n} ({n})")

# ----------------------------------------------------------------------
# Example 3: EDA with pandas: describe, info, correlations
# ----------------------------------------------------------------------
print("\n--- Example 3: EDA with pandas: describe, info, correlations ---")
try:
    import pandas as pd

    df = pd.DataFrame({
        "age":    [25, 30, 35, 40, 45, 50],
        "income": [30, 45, 50, 65, 70, 90],   # in thousands
        "city":   ["NYC", "LA", "NYC", "SF", "LA", "SF"],
    })
    print("shape:", df.shape)
    print("\ndescribe:\n", df.describe())            # numeric summary
    print("\nmissing per column:\n", df.isna().sum())
    print("\ncity value counts:\n", df["city"].value_counts())
    print("\ncorrelation:\n", df.corr(numeric_only=True).round(3))
except ImportError:
    print("pandas not installed — run: pip install pandas")

print("\nDone! Tip: change values above and run again to learn by experiment.")

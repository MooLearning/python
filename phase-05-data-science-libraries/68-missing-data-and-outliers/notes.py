# ======================================================================
# 68 — Missing Data and Outliers  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: pandas
# Install:  pip install pandas

# ----------------------------------------------------------------------
# Example 1: Detecting and imputing missing values (pure Python)
# ----------------------------------------------------------------------
print("\n--- Example 1: Detecting and imputing missing values (pure Python) ---")
import statistics as st

data = [10, 20, None, 40, None, 60]

# Detect
missing = [i for i, x in enumerate(data) if x is None]
print("missing at indices:", missing)        # [2, 4]

present = [x for x in data if x is not None]

# Impute with the mean
mean_val = st.mean(present)
mean_filled = [mean_val if x is None else x for x in data]
print("mean-imputed  :", mean_filled)

# Impute with the median (robust to outliers)
median_val = st.median(present)
median_filled = [median_val if x is None else x for x in data]
print("median-imputed:", median_filled)

# ----------------------------------------------------------------------
# Example 2: Outlier detection with the IQR rule
# ----------------------------------------------------------------------
print("\n--- Example 2: Outlier detection with the IQR rule ---")
import statistics as st

data = [10, 12, 12, 13, 12, 11, 14, 13, 100]   # 100 is suspicious

q1, q2, q3 = st.quantiles(data, n=4)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print(f"Q1={q1}, Q3={q3}, IQR={iqr}")
print(f"normal range: [{lower}, {upper}]")

outliers = [x for x in data if x < lower or x > upper]
clean = [x for x in data if lower <= x <= upper]
print("outliers:", outliers)                  # [100]
print("clean   :", clean)

# ----------------------------------------------------------------------
# Example 3: Z-score outliers and capping; pandas version
# ----------------------------------------------------------------------
print("\n--- Example 3: Z-score outliers and capping; pandas version ---")
import statistics as st

data = [50, 52, 49, 51, 53, 120]
mu, sigma = st.mean(data), st.pstdev(data)

# Z-score rule: |z| > 2 flagged here (use 3 for larger data)
z_outliers = [x for x in data if abs((x - mu) / sigma) > 2]
print("z-score outliers:", z_outliers)        # [120]

# Capping (winsorize) to the 5th/95th percentile-ish bounds
lo, hi = min(data[:-1]), 60
capped = [min(max(x, lo), hi) for x in data]
print("capped:", capped)

try:
    import pandas as pd
    import numpy as np
    s = pd.Series([1, 2, np.nan, 4])
    print("\npandas missing count:", int(s.isna().sum()))
    print("filled with mean:\n", s.fillna(s.mean()).tolist())
except ImportError:
    print("pandas not installed — run: pip install pandas")

print("\nDone! Tip: change values above and run again to learn by experiment.")

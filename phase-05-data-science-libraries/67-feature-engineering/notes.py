# ======================================================================
# 67 — Feature Engineering  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: Deriving and transforming features (pure Python)
# ----------------------------------------------------------------------
print("\n--- Example 1: Deriving and transforming features (pure Python) ---")
import math

houses = [
    {"price": 300_000, "area": 1500, "rooms": 3},
    {"price": 500_000, "area": 2000, "rooms": 4},
    {"price": 250_000, "area": 1000, "rooms": 2},
]

for h in houses:
    h["price_per_sqft"] = round(h["price"] / h["area"], 2)   # ratio feature
    h["area_per_room"] = round(h["area"] / h["rooms"], 1)
    h["log_price"] = round(math.log(h["price"]), 3)          # tame skew

for h in houses:
    print(h)

# ----------------------------------------------------------------------
# Example 2: Binning and date features
# ----------------------------------------------------------------------
print("\n--- Example 2: Binning and date features ---")
from datetime import date

# Binning ages into categories
def age_bucket(age):
    if age < 18:  return "minor"
    if age < 65:  return "adult"
    return "senior"

for a in [10, 25, 40, 70]:
    print(f"age {a:2} -> {age_bucket(a)}")

# Date-derived features
events = [date(2026, 1, 1), date(2026, 7, 4), date(2026, 12, 25)]
for d in events:
    print(f"{d}: month={d.month}, weekday={d.strftime('%A')}, "
          f"is_weekend={d.weekday() >= 5}")

# ----------------------------------------------------------------------
# Example 3: Polynomial features and scaling with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: Polynomial features and scaling with scikit-learn ---")
try:
    from sklearn.preprocessing import PolynomialFeatures, StandardScaler
    from sklearn.pipeline import make_pipeline

    X = [[2], [3], [4]]

    # Expand x into [1, x, x^2]
    poly = PolynomialFeatures(degree=2)
    print("polynomial features:\n", poly.fit_transform(X))

    # Chain transforms in a pipeline (kept consistent on new data)
    pipe = make_pipeline(PolynomialFeatures(2), StandardScaler())
    out = pipe.fit_transform(X)
    print("\npoly + standardized:\n", out.round(3))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")

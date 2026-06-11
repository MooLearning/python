# ======================================================================
# 86 — Regression Metrics  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: MAE, MSE, RMSE, R² from scratch
# ----------------------------------------------------------------------
print("\n--- Example 1: MAE, MSE, RMSE, R² from scratch ---")
import math

y_true = [3.0, -0.5, 2.0, 7.0, 4.2]
y_pred = [2.5,  0.0, 2.0, 8.0, 4.0]
n = len(y_true)

mae = sum(abs(t - p) for t, p in zip(y_true, y_pred)) / n
mse = sum((t - p) ** 2 for t, p in zip(y_true, y_pred)) / n
rmse = math.sqrt(mse)

mean_y = sum(y_true) / n
ss_res = sum((t - p) ** 2 for t, p in zip(y_true, y_pred))
ss_tot = sum((t - mean_y) ** 2 for t in y_true)
r2 = 1 - ss_res / ss_tot

print(f"MAE : {mae:.4f}")
print(f"MSE : {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R^2 : {r2:.4f}")

# ----------------------------------------------------------------------
# Example 2: Why RMSE punishes outliers more than MAE
# ----------------------------------------------------------------------
print("\n--- Example 2: Why RMSE punishes outliers more than MAE ---")
# Same predictions except one big miss in the second set.
truth = [10, 20, 30, 40]
good = [11, 19, 31, 39]            # all off by ~1
one_big = [11, 19, 31, 80]         # last one off by 40

def mae(t, p): return sum(abs(a-b) for a, b in zip(t, p)) / len(t)
def rmse(t, p):
    return (sum((a-b)**2 for a, b in zip(t, p)) / len(t)) ** 0.5

print("evenly small errors:  MAE=%.2f RMSE=%.2f" % (mae(truth, good), rmse(truth, good)))
print("one large error:      MAE=%.2f RMSE=%.2f" % (mae(truth, one_big), rmse(truth, one_big)))
print("-> RMSE jumps much more, because squaring magnifies the big miss.")

# ----------------------------------------------------------------------
# Example 3: Regression metrics with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: Regression metrics with scikit-learn ---")
try:
    from sklearn.metrics import (mean_absolute_error, mean_squared_error,
                                 r2_score)
    import math
    y_true = [3.0, -0.5, 2.0, 7.0, 4.2]
    y_pred = [2.5, 0.0, 2.0, 8.0, 4.0]

    print("MAE :", round(mean_absolute_error(y_true, y_pred), 4))
    mse = mean_squared_error(y_true, y_pred)
    print("MSE :", round(mse, 4))
    print("RMSE:", round(math.sqrt(mse), 4))
    print("R^2 :", round(r2_score(y_true, y_pred), 4))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")

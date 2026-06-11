# ======================================================================
# 72 — Linear Regression  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: Simple linear regression in closed form
# ----------------------------------------------------------------------
print("\n--- Example 1: Simple linear regression in closed form ---")
# Hours studied vs exam score
xs = [1, 2, 3, 4, 5]
ys = [52, 60, 67, 75, 81]

n = len(xs)
x_bar = sum(xs) / n
y_bar = sum(ys) / n

# slope = sum((xi-x̄)(yi-ȳ)) / sum((xi-x̄)^2)
num = sum((x - x_bar) * (y - y_bar) for x, y in zip(xs, ys))
den = sum((x - x_bar) ** 2 for x in xs)
slope = num / den
intercept = y_bar - slope * x_bar
print(f"y = {slope:.2f} * x + {intercept:.2f}")

def predict(x):
    return slope * x + intercept

# R^2 = 1 - SS_res / SS_tot
ss_res = sum((y - predict(x)) ** 2 for x, y in zip(xs, ys))
ss_tot = sum((y - y_bar) ** 2 for y in ys)
print("R^2:", round(1 - ss_res / ss_tot, 4))
print("predict 6 hrs ->", round(predict(6), 1))

# ----------------------------------------------------------------------
# Example 2: Linear regression via gradient descent
# ----------------------------------------------------------------------
print("\n--- Example 2: Linear regression via gradient descent ---")
xs = [1, 2, 3, 4, 5]
ys = [52, 60, 67, 75, 81]
n = len(xs)

w, b = 0.0, 0.0
lr = 0.01
for epoch in range(2000):
    # predictions and errors
    preds = [w * x + b for x in xs]
    errors = [p - y for p, y in zip(preds, ys)]
    # gradients of MSE
    grad_w = (2 / n) * sum(e * x for e, x in zip(errors, xs))
    grad_b = (2 / n) * sum(errors)
    w -= lr * grad_w
    b -= lr * grad_b

print(f"learned: y = {w:.2f} * x + {b:.2f}")
print("predict 6 ->", round(w * 6 + b, 1))   # close to closed-form answer

# ----------------------------------------------------------------------
# Example 3: Multi-feature regression with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: Multi-feature regression with scikit-learn ---")
try:
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score

    # features: [area(100s sqft), bedrooms]; target: price (10k)
    X = [[15, 3], [20, 4], [10, 2], [25, 5], [18, 3]]
    y = [30, 45, 22, 58, 38]

    model = LinearRegression().fit(X, y)
    print("coefficients:", model.coef_.round(3).tolist())
    print("intercept   :", round(model.intercept_, 3))

    preds = model.predict(X)
    print("R^2:", round(r2_score(y, preds), 4))
    print("predict [22, 4] ->", round(model.predict([[22, 4]])[0], 2))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")

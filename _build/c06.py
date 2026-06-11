# -*- coding: utf-8 -*-
"""Phase 6 — Machine Learning.

Each topic pairs a from-scratch pure-Python implementation (always runs) with a
guarded scikit-learn example (real API, prints an install hint if missing).
"""

CONTENT = {}

CONTENT["ml-overview"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**Machine learning** is getting computers to learn patterns from data instead of being "
        "explicitly programmed with rules. The main families are **supervised** (learn from labeled "
        "examples to predict — classification & regression), **unsupervised** (find structure in "
        "unlabeled data — clustering, dimensionality reduction), and **reinforcement** (learn by "
        "trial and reward). The workflow: data → features → train a model → evaluate → predict."
    ),
    "why": (
        "ML powers recommendations, fraud detection, language models, vision, and forecasting. "
        "Knowing the categories and the train/evaluate/predict loop frames every later topic and "
        "helps you pick the right tool for a problem."
    ),
    "concepts": [
        ("Supervised", "Labeled data; predict a target (classification/regression)."),
        ("Unsupervised", "No labels; find groups or structure (clustering, PCA)."),
        ("Reinforcement", "Learn actions from rewards via trial and error."),
        ("Features & labels", "Inputs (X) and the answer to predict (y)."),
        ("Train vs predict", "Fit parameters on training data, then predict on new data."),
        ("Generalization", "Doing well on UNSEEN data, not just memorizing training data."),
    ],
    "examples": [
        ("A tiny supervised classifier learned from data", r'''
# Learn a threshold to classify animals as 'cat' or 'dog' by weight (kg).
train = [(4, "cat"), (5, "cat"), (3.5, "cat"), (20, "dog"), (25, "dog"), (18, "dog")]

# 'Training' = compute the midpoint between class averages
cats = [w for w, label in train if label == "cat"]
dogs = [w for w, label in train if label == "dog"]
threshold = (sum(cats) / len(cats) + sum(dogs) / len(dogs)) / 2
print("learned threshold:", round(threshold, 2), "kg")

def predict(weight):
    return "dog" if weight > threshold else "cat"

# Predict on NEW, unseen examples
for w in [6, 15, 22]:
    print(f"{w} kg -> {predict(w)}")
'''),
        ("The train / evaluate / predict loop", r'''
# Toy regression: learn that y ~ 2*x from examples, then evaluate.
train = [(1, 2), (2, 4), (3, 6), (4, 8)]

# 'Fit': estimate the slope as average(y/x)
slope = sum(y / x for x, y in train) / len(train)
print("learned slope:", slope)            # ~2.0

def model(x):
    return slope * x

# Evaluate on held-out data with mean absolute error
test = [(5, 10), (6, 12)]
mae = sum(abs(model(x) - y) for x, y in test) / len(test)
print("test MAE:", round(mae, 4))         # ~0 (great fit)
print("predict x=10 ->", model(10))       # ~20
'''),
        ("Supervised vs unsupervised with scikit-learn", r'''
try:
    from sklearn.linear_model import LinearRegression   # supervised
    from sklearn.cluster import KMeans                   # unsupervised

    # Supervised: learn y = 3x from labeled data
    X = [[1], [2], [3], [4]]
    y = [3, 6, 9, 12]
    reg = LinearRegression().fit(X, y)
    print("supervised slope ~", round(reg.coef_[0], 2))   # ~3
    print("predict 5 ->", round(reg.predict([[5]])[0], 2))

    # Unsupervised: group points with NO labels
    points = [[1], [1.5], [8], [8.5]]
    km = KMeans(n_clusters=2, n_init=10, random_state=0).fit(points)
    print("cluster labels:", km.labels_.tolist())
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "More data and better features usually beat a fancier algorithm — start simple.",
        "Evaluate on data the model never saw; training accuracy alone is misleading.",
        "Garbage labels = garbage model; supervised learning is only as good as its labels.",
        "Not every problem is ML — if simple rules work, use them; ML adds complexity.",
        "Correlation learned by a model isn't causation — be careful about deployment decisions.",
    ],
    "exercises": [
        ("Classify by threshold: predict 'big' if x>10 else 'small' for x=7.", "Compare to threshold.",
         r'''def predict(x):
    return "big" if x > 10 else "small"
print(predict(7))  # small'''),
        ("Is spam detection supervised or unsupervised? Why?", "Labeled emails.",
         r'''#md
**Supervised** — you train on emails already **labeled** spam/not-spam, then predict
labels for new emails. (Grouping unlabeled emails into themes would be unsupervised.)'''),
        ("Compute MAE between predictions [2,4] and truth [3,5].", "Mean abs error.",
         r'''pred, true = [2, 4], [3, 5]
print(sum(abs(p - t) for p, t in zip(pred, true)) / len(true))  # 1.0'''),
        ("Learn a slope from [(1,3),(2,6)] as avg(y/x).", "Average the ratios.",
         r'''data = [(1, 3), (2, 6)]
print(sum(y / x for x, y in data) / len(data))  # 3.0'''),
        ("Name the target (label) vs features for predicting house price from area, rooms.", "y vs X.",
         r'''#md
**Label (y):** house price. **Features (X):** area, number of rooms. The model
learns a mapping X → y from past sales.'''),
        ("Decide: clustering customers by behavior is which ML type?", "No labels.",
         r'''#md
**Unsupervised learning** (clustering) — there are no predefined labels; the
algorithm discovers groups from the data itself.'''),
        ("Predict with model y=2x+1 at x=4.", "Plug in.",
         r'''def model(x): return 2 * x + 1
print(model(4))  # 9'''),
        ("Why split data into train and test sets?", "Measure generalization.",
         r'''#md
To estimate how the model performs on **unseen** data. Testing on training data
rewards memorization; a held-out test set measures real **generalization**.'''),
    ],
}

CONTENT["train-test-split-and-cross-validation"] = {
    "deps": ["scikit-learn"],
    "what": (
        "To estimate how a model generalizes, you **hold out** data it never trains on. A "
        "**train/test split** (e.g. 80/20) trains on one part and evaluates on the other. "
        "**K-fold cross-validation** does this k times — each fold is the test set once — and "
        "averages the scores, giving a more reliable estimate that uses all the data for both "
        "training and validation."
    ),
    "why": (
        "Evaluating on training data overstates performance (memorization). Splits and "
        "cross-validation give honest estimates, reduce the luck of a single split, and are the "
        "basis for comparing models and tuning hyperparameters."
    ),
    "concepts": [
        ("Train/test split", "Hold out a fraction (e.g. 20%) for final evaluation."),
        ("Shuffle + seed", "Randomize order; fix a seed for reproducibility."),
        ("K-fold CV", "Split into k folds; each is the validation set once."),
        ("Stratified", "Keep class proportions balanced across folds."),
        ("Validation set", "A third split for tuning, separate from the final test."),
        ("Average score", "CV reports mean ± std across folds, not one number."),
    ],
    "examples": [
        ("Manual train/test split with shuffling", r'''
import random

data = list(range(1, 11))          # 10 samples
random.seed(42)
random.shuffle(data)               # shuffle so the split isn't biased

split = int(0.8 * len(data))       # 80% train
train, test = data[:split], data[split:]
print("train:", train)             # 8 items
print("test :", test)              # 2 items
print(f"{len(train)} train / {len(test)} test")
'''),
        ("K-fold cross-validation indices (pure Python)", r'''
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
'''),
        ("scikit-learn split and cross_val_score", r'''
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
'''),
    ],
    "gotchas": [
        "Always shuffle before splitting (unless it's time series) — ordered data biases the split.",
        "Fit preprocessing on the TRAIN fold only inside CV, or you leak test info.",
        "Use stratified splits for imbalanced classes so each fold has all classes.",
        "Never tune on the final test set — use a validation set or CV, then test once at the end.",
        "For time series, use forward-chaining splits — random shuffling leaks the future.",
    ],
    "exercises": [
        ("Split [1..10] into 70% train / 30% test by slicing.", "int(0.7*n).",
         r'''data = list(range(1, 11))
s = int(0.7 * len(data))
print(data[:s], data[s:])'''),
        ("Shuffle [1,2,3,4,5] reproducibly with seed 0.", "random.seed + shuffle.",
         r'''import random
random.seed(0)
d = [1, 2, 3, 4, 5]; random.shuffle(d)
print(d)'''),
        ("How many samples per fold for n=20, k=5?", "n // k.",
         r'''print(20 // 5)  # 4'''),
        ("Average the CV scores [0.8,0.9,0.85].", "Mean.",
         r'''s = [0.8, 0.9, 0.85]
print(round(sum(s) / len(s), 3))  # 0.85'''),
        ("Why use cross-validation over a single split?", "Reliability.",
         r'''#md
A single split's score depends on luck (which rows landed in test). **K-fold CV**
averages over k different splits, giving a more **stable, reliable** estimate and
using every sample for both training and validation.'''),
        ("Generate 3-fold test index ranges for n=9.", "Equal thirds.",
         r'''n, k = 9, 3
size = n // k
print([list(range(i * size, (i + 1) * size)) for i in range(k)])'''),
        ("What is stratified splitting?", "Preserve class ratios.",
         r'''#md
**Stratified** splitting keeps the **proportion of each class** the same in every
fold/split as in the full dataset — crucial for imbalanced data so a fold isn't
missing a rare class.'''),
        ("Compute the std of CV scores [0.8,0.82,0.78].", "statistics.pstdev.",
         r'''import statistics as st
print(round(st.pstdev([0.8, 0.82, 0.78]), 4))'''),
    ],
}

CONTENT["bias-variance-tradeoff"] = {
    "deps": ["scikit-learn"],
    "what": (
        "Prediction error splits into **bias** (error from overly simple assumptions — "
        "**underfitting**), **variance** (sensitivity to the training sample — **overfitting**), and "
        "irreducible noise. Simple models have high bias/low variance; complex models have low "
        "bias/high variance. The **tradeoff** is finding the sweet-spot complexity that minimizes "
        "total error on unseen data."
    ),
    "why": (
        "Diagnosing whether a model underfits or overfits tells you what to do next (more features/"
        "complexity vs more data/regularization). It's the central tension in all of ML."
    ),
    "concepts": [
        ("Bias", "Error from wrong assumptions; underfitting (too simple)."),
        ("Variance", "Error from sensitivity to training data; overfitting (too complex)."),
        ("Underfitting", "High train AND test error — model too weak."),
        ("Overfitting", "Low train but high test error — memorized noise."),
        ("Sweet spot", "Complexity that minimizes test/validation error."),
        ("Fixes", "Underfit → add complexity/features; overfit → more data/regularize."),
    ],
    "examples": [
        ("Underfitting: a too-simple model has high error everywhere", r'''
# True relationship: y = 2x. A high-bias model predicts the global mean.
train = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10)]
mean_y = sum(y for _, y in train) / len(train)     # constant predictor

def underfit(x):
    return mean_y                                  # ignores x entirely!

train_err = sum((underfit(x) - y) ** 2 for x, y in train) / len(train)
test = [(6, 12), (7, 14)]
test_err = sum((underfit(x) - y) ** 2 for x, y in test) / len(test)
print("constant prediction:", mean_y)
print("train MSE:", round(train_err, 2), "(high)")
print("test  MSE:", round(test_err, 2), "(high) -> UNDERFIT / high bias")
'''),
        ("Overfitting: memorizing train gives 0 train error, bad test error", r'''
train = [(1, 2), (2, 4), (3, 5), (4, 8)]

# A model that memorizes exact training points (a lookup table)
memory = {x: y for x, y in train}

def overfit(x):
    return memory.get(x, 0)        # perfect on train, clueless on new x

train_err = sum((overfit(x) - y) ** 2 for x, y in train) / len(train)
test = [(5, 10), (6, 12)]
test_err = sum((overfit(x) - y) ** 2 for x, y in test) / len(test)
print("train MSE:", train_err, "(zero -> looks perfect!)")
print("test  MSE:", round(test_err, 1), "(terrible) -> OVERFIT / high variance")
'''),
        ("Polynomial degree vs error with scikit-learn", r'''
try:
    import numpy as np
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.linear_model import LinearRegression
    from sklearn.pipeline import make_pipeline
    from sklearn.model_selection import train_test_split

    rng = np.random.RandomState(0)
    X = np.linspace(-3, 3, 60).reshape(-1, 1)
    y = X.ravel() ** 2 + rng.normal(0, 1.5, 60)    # true: quadratic + noise

    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=0)
    for degree in [1, 2, 10]:
        m = make_pipeline(PolynomialFeatures(degree), LinearRegression())
        m.fit(X_tr, y_tr)
        tr = m.score(X_tr, y_tr); te = m.score(X_te, y_te)
        tag = "underfit" if degree == 1 else ("good" if degree == 2 else "overfit")
        print(f"degree {degree:2}: train R2={tr:.2f}, test R2={te:.2f} -> {tag}")
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn numpy")
'''),
    ],
    "gotchas": [
        "Low training error alone means nothing — a memorizing model has zero train error.",
        "A big gap between train and test performance signals overfitting (high variance).",
        "High error on BOTH train and test signals underfitting (high bias).",
        "Adding data helps variance/overfitting, but rarely fixes bias/underfitting.",
        "More complexity isn't free — it needs more data to avoid overfitting.",
    ],
    "exercises": [
        ("Train error 0.01, test error 5.0 — over or underfit?", "Big gap.",
         r'''#md
**Overfitting** (high variance): tiny training error but large test error means the
model memorized the training data and fails to generalize.'''),
        ("Train error 4.5, test error 4.7 — over or underfit?", "Both high.",
         r'''#md
**Underfitting** (high bias): error is high on both sets, so the model is too simple
to capture the pattern.'''),
        ("Compute MSE of constant predictor 5 for truths [2,8].", "Mean sq error.",
         r'''true = [2, 8]
print(sum((5 - t) ** 2 for t in true) / len(true))  # 9.0'''),
        ("Fix for overfitting: name two options.", "Data/regularize.",
         r'''#md
1) Get **more training data**. 2) **Regularize** / reduce model complexity (fewer
features, smaller degree, L1/L2 penalties, dropout).'''),
        ("Fix for underfitting: name two options.", "Complexity/features.",
         r'''#md
1) Use a **more complex model** (higher degree, more layers). 2) Add **better
features** so the signal is learnable.'''),
        ("Which has higher variance: degree-1 line or degree-15 polynomial?", "Complex = variance.",
         r'''#md
The **degree-15 polynomial** — high complexity makes it wiggle to fit noise, so it
varies a lot with the training sample (high variance).'''),
        ("Compute the train-test error gap for 0.9 vs 0.6 accuracy.", "Subtract.",
         r'''print(0.9 - 0.6)  # 0.30 -> large gap, likely overfit'''),
        ("As model complexity rises, what happens to bias and variance?", "Opposite directions.",
         r'''#md
**Bias decreases** (model fits training data better) while **variance increases**
(more sensitive to the specific training sample). Total error is U-shaped.'''),
    ],
}

CONTENT["linear-regression"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**Linear regression** fits a straight line (or hyperplane) `y = w·x + b` to predict a "
        "continuous target by minimizing the **mean squared error**. With one feature it has a "
        "closed-form solution (least squares: slope and intercept from the data); with many features "
        "you solve the normal equations or use **gradient descent**. It's the simplest, most "
        "interpretable regression model."
    ),
    "why": (
        "It's the entry point to predictive modeling: fast, interpretable (each weight is a feature's "
        "effect), and the foundation for logistic regression, regularization, and neural networks. "
        "Many real relationships are approximately linear."
    ),
    "concepts": [
        ("Line equation", "y = w·x + b: weight (slope) and bias (intercept)."),
        ("Least squares", "Choose w, b to minimize summed squared errors."),
        ("Closed form", "slope = cov(x,y)/var(x); intercept = ȳ − slope·x̄."),
        ("Gradient descent", "Iteratively step weights downhill on the MSE."),
        ("R² score", "Fraction of variance explained (1 = perfect, 0 = mean)."),
        ("Residuals", "Actual − predicted; should look like random noise."),
    ],
    "examples": [
        ("Simple linear regression in closed form", r'''
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
'''),
        ("Linear regression via gradient descent", r'''
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
'''),
        ("Multi-feature regression with scikit-learn", r'''
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
'''),
    ],
    "gotchas": [
        "Linear regression assumes a roughly linear relationship — check residual plots.",
        "Outliers heavily distort least squares (squared errors punish big misses).",
        "Highly correlated features (multicollinearity) make coefficients unstable.",
        "Gradient descent needs a sensible learning rate and scaled features to converge.",
        "Extrapolating far outside the training range is unreliable — the line keeps going forever.",
    ],
    "exercises": [
        ("Fit a line to (1,2),(2,4),(3,6): find the slope.", "Closed form.",
         r'''xs, ys = [1, 2, 3], [2, 4, 6]
n = len(xs); xb = sum(xs) / n; yb = sum(ys) / n
num = sum((x - xb) * (y - yb) for x, y in zip(xs, ys))
den = sum((x - xb) ** 2 for x in xs)
print(num / den)  # 2.0'''),
        ("Predict y at x=10 for y=3x+1.", "Plug in.",
         r'''print(3 * 10 + 1)  # 31'''),
        ("Compute the mean squared error of preds [2,4] vs [3,5].", "Mean of squares.",
         r'''pred, true = [2, 4], [3, 5]
print(sum((p - t) ** 2 for p, t in zip(pred, true)) / len(true))  # 1.0'''),
        ("Compute R^2 when SS_res=2 and SS_tot=10.", "1 - res/tot.",
         r'''print(1 - 2 / 10)  # 0.8'''),
        ("Find the intercept given slope=2, x̄=3, ȳ=8.", "ȳ - slope*x̄.",
         r'''print(8 - 2 * 3)  # 2'''),
        ("One gradient-descent step for w on MSE: w=0,lr=0.1,grad=-4.", "w -= lr*grad.",
         r'''w, lr, grad = 0, 0.1, -4
print(w - lr * grad)  # 0.4'''),
        ("What does an R^2 of 1.0 mean?", "Perfect fit.",
         r'''#md
The model explains **100% of the variance** in the target — predictions match the
actual values exactly (perfect fit on this data).'''),
        ("Why are outliers dangerous for least squares?", "Squared penalty.",
         r'''#md
Least squares minimizes **squared** errors, so a single far-off point contributes a
huge penalty and can drag the whole line toward it, hurting all other predictions.'''),
    ],
}

CONTENT["logistic-regression"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**Logistic regression** is a **classification** model (despite the name). It computes a "
        "linear score `w·x + b`, then squashes it through the **sigmoid** into a probability between "
        "0 and 1. Predict class 1 if the probability exceeds a threshold (usually 0.5). It's trained "
        "by minimizing **log loss** (cross-entropy) via gradient descent."
    ),
    "why": (
        "It's the default baseline for binary classification: fast, interpretable (weights = log-"
        "odds effects), and outputs calibrated probabilities. It underlies neural-network output "
        "layers and many real systems (spam, churn, click prediction)."
    ),
    "concepts": [
        ("Sigmoid", "σ(z) = 1/(1+e^−z) maps any score to (0, 1)."),
        ("Decision boundary", "Predict 1 when probability ≥ 0.5 (score ≥ 0)."),
        ("Log loss", "Cross-entropy penalizes confident wrong predictions heavily."),
        ("Probabilities", "Output is a probability, not just a hard label."),
        ("Linear in features", "The boundary is a line/hyperplane in feature space."),
        ("Threshold tuning", "Move 0.5 to trade precision vs recall."),
    ],
    "examples": [
        ("The sigmoid function and probabilities", r'''
import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

for z in [-4, -1, 0, 1, 4]:
    print(f"sigmoid({z:2}) = {sigmoid(z):.4f}")
# sigmoid(0) = 0.5  -> the decision boundary
# large positive z -> ~1 (class 1), large negative -> ~0 (class 0)
'''),
        ("Logistic regression from scratch (gradient descent)", r'''
import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# 1 feature: hours studied -> pass(1)/fail(0)
xs = [1, 2, 3, 4, 5, 6]
ys = [0, 0, 0, 1, 1, 1]
n = len(xs)

w, b = 0.0, 0.0
lr = 0.3
for epoch in range(3000):
    grad_w = grad_b = 0.0
    for x, y in zip(xs, ys):
        p = sigmoid(w * x + b)
        grad_w += (p - y) * x          # gradient of log loss
        grad_b += (p - y)
    w -= lr * grad_w / n
    b -= lr * grad_b / n

def predict_proba(x):
    return sigmoid(w * x + b)

print(f"weights: w={w:.3f}, b={b:.3f}")
for x in [2, 3.5, 5]:
    p = predict_proba(x)
    print(f"x={x}: P(pass)={p:.3f} -> {'pass' if p >= 0.5 else 'fail'}")
'''),
        ("Logistic regression with scikit-learn", r'''
try:
    from sklearn.linear_model import LogisticRegression
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    X, y = make_classification(n_samples=200, n_features=4,
                               n_informative=3, random_state=0)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)

    clf = LogisticRegression(max_iter=1000).fit(X_tr, y_tr)
    preds = clf.predict(X_te)
    print("accuracy:", round(accuracy_score(y_te, preds), 3))

    # Predicted probabilities for the first 3 test samples
    probs = clf.predict_proba(X_te[:3])[:, 1]
    print("P(class 1):", probs.round(3).tolist())
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "It outputs PROBABILITIES — threshold them (default 0.5) to get class labels.",
        "The decision boundary is linear; for curved boundaries add features or use another model.",
        "Imbalanced classes bias it toward the majority — use class weights or resampling.",
        "Scale/standardize features so gradient descent converges and weights are comparable.",
        "Perfectly separable data makes weights blow up — regularization keeps them finite.",
    ],
    "exercises": [
        ("Compute sigmoid(0).", "1/(1+e^0).",
         r'''import math
print(1 / (1 + math.exp(-0)))  # 0.5'''),
        ("Classify probability 0.7 with threshold 0.5.", "Compare.",
         r'''p = 0.7
print(1 if p >= 0.5 else 0)  # 1'''),
        ("Compute sigmoid(2) rounded to 3 dp.", "Formula.",
         r'''import math
print(round(1 / (1 + math.exp(-2)), 3))  # 0.881'''),
        ("Why is it called regression but used for classification?", "Linear score.",
         r'''#md
It performs linear **regression on the log-odds** (a continuous score), then maps
that score to a probability with the sigmoid. The continuous-score fitting is the
'regression'; thresholding the probability gives a class.'''),
        ("Compute the linear score w*x+b for w=2,x=3,b=-5.", "Dot + bias.",
         r'''print(2 * 3 + (-5))  # 1'''),
        ("At what score z does sigmoid output exactly 0.5?", "z=0.",
         r'''#md
At **z = 0**, sigmoid(0) = 0.5 — that's the decision boundary where the model is
maximally uncertain.'''),
        ("Predicted 0.9 for true label 1 — is log loss small or large?", "Confident correct.",
         r'''#md
**Small.** The model was confident and correct, so cross-entropy
(-log 0.9 ≈ 0.105) is low. Confident *wrong* predictions get large loss.'''),
        ("Move the threshold to 0.3: does recall go up or down?", "Lower bar.",
         r'''#md
**Recall goes up** (and precision usually down): a lower threshold labels more
samples positive, catching more true positives but also more false positives.'''),
    ],
}

CONTENT["knn"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**K-Nearest Neighbors (KNN)** is a simple, **instance-based** algorithm: to classify a new "
        "point, find the **k** closest training points (by a distance like Euclidean) and take a "
        "**majority vote** (or average, for regression). There's no real 'training' — it just stores "
        "the data and computes distances at prediction time (a 'lazy learner')."
    ),
    "why": (
        "KNN is intuitive, needs no training, and works as a strong baseline. It teaches the "
        "importance of distance metrics, feature scaling, and the choice of k — concepts that recur "
        "throughout ML."
    ),
    "concepts": [
        ("Distance", "Euclidean (or Manhattan/cosine) measures closeness."),
        ("k neighbors", "How many nearest points vote; odd k avoids ties."),
        ("Majority vote", "Classification: most common label among neighbors."),
        ("Averaging", "Regression: mean of neighbors' target values."),
        ("Lazy learning", "No model is fit; all work happens at prediction time."),
        ("Scaling matters", "Features must be scaled or large-range ones dominate distance."),
    ],
    "examples": [
        ("KNN classifier from scratch", r'''
import math
from collections import Counter

# training points: (features, label)
train = [
    ((1, 1), "A"), ((1, 2), "A"), ((2, 1), "A"),
    ((6, 6), "B"), ((7, 7), "B"), ((6, 7), "B"),
]

def euclidean(p, q):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p, q)))

def knn_predict(point, k=3):
    # sort training points by distance to the query point
    distances = sorted(train, key=lambda item: euclidean(point, item[0]))
    neighbors = [label for _, label in distances[:k]]
    return Counter(neighbors).most_common(1)[0][0]

print("(2,2) ->", knn_predict((2, 2)))    # A (near the A cluster)
print("(6,5) ->", knn_predict((6, 5)))    # B (near the B cluster)
print("(4,4) ->", knn_predict((4, 4)))    # depends on k / ties
'''),
        ("How k changes the prediction; KNN regression", r'''
import math
from collections import Counter

train = [((1,), "low"), ((2,), "low"), ((3,), "low"),
         ((4,), "high"), ((5,), "high"), ((3.2,), "high")]

def knn(point, k):
    dist = sorted(train, key=lambda it: abs(point[0] - it[0][0]))
    labels = [lab for _, lab in dist[:k]]
    return Counter(labels).most_common(1)[0][0]

for k in [1, 3, 5]:
    print(f"k={k}: (3.1,) -> {knn((3.1,), k)}")

# KNN regression: average the neighbors' values
reg_train = [(1, 10), (2, 20), (3, 30), (4, 40)]
def knn_reg(x, k=2):
    nearest = sorted(reg_train, key=lambda it: abs(x - it[0]))[:k]
    return sum(v for _, v in nearest) / k
print("regress x=2.5 ->", knn_reg(2.5))   # (20+30)/2 = 25
'''),
        ("KNN with scikit-learn (and why scaling matters)", r'''
try:
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import make_pipeline

    X, y = load_iris(return_X_y=True)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)

    # scale features, then KNN — chained so test data is scaled the same way
    model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
    model.fit(X_tr, y_tr)
    print("accuracy:", round(model.score(X_te, y_te), 3))
    print("predict first 5:", model.predict(X_te[:5]).tolist())
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "Unscaled features wreck KNN — a feature in thousands dominates one in fractions. Scale first.",
        "Small k overfits (sensitive to noise); large k oversmooths. Tune it (often odd).",
        "Prediction is O(n) per query — slow on big datasets (no precomputed model).",
        "The curse of dimensionality: distances become meaningless with many features.",
        "Ties in voting need a rule (reduce k, weight by distance, or pick lowest label).",
    ],
    "exercises": [
        ("Compute Euclidean distance between (0,0) and (3,4).", "sqrt of sum of squares.",
         r'''import math
print(math.sqrt((3 - 0) ** 2 + (4 - 0) ** 2))  # 5.0'''),
        ("Majority vote of ['A','B','A'].", "Counter.",
         r'''from collections import Counter
print(Counter(["A", "B", "A"]).most_common(1)[0][0])  # A'''),
        ("Find the 1 nearest of [1,5,9] to the query 4.", "min by distance.",
         r'''pts = [1, 5, 9]
print(min(pts, key=lambda p: abs(p - 4)))  # 5'''),
        ("KNN-regress: average the 2 nearest values to x=3 in [(1,10),(2,20),(5,50)].", "Mean of 2.",
         r'''data = [(1, 10), (2, 20), (5, 50)]
near = sorted(data, key=lambda it: abs(3 - it[0]))[:2]
print(sum(v for _, v in near) / 2)  # 15.0'''),
        ("Why scale features before KNN?", "Distance fairness.",
         r'''#md
KNN uses distances, so a feature with a large numeric range (e.g. salary in the
thousands) dominates one with a small range (e.g. age). **Scaling** puts all
features on comparable footing so each contributes fairly.'''),
        ("With k=1, what is the training accuracy usually?", "Memorization.",
         r'''#md
Usually **100%** — each training point's nearest neighbor is itself. That's a sign
k=1 can overfit; evaluate on a separate test set.'''),
        ("Compute Manhattan distance between (1,2) and (4,6).", "Sum of abs diffs.",
         r'''print(abs(1 - 4) + abs(2 - 6))  # 7'''),
        ("Is KNN a lazy or eager learner? Why?", "No training phase.",
         r'''#md
**Lazy.** It does no real training — it just stores the data and defers all
computation (distance + vote) to **prediction time**.'''),
    ],
}

CONTENT["svm"] = {
    "deps": ["scikit-learn"],
    "what": (
        "A **Support Vector Machine (SVM)** finds the **decision boundary** (hyperplane) that "
        "separates classes with the **widest margin** — the largest gap to the nearest points "
        "(the **support vectors**). For non-linear data, the **kernel trick** (e.g. RBF) implicitly "
        "maps features into a higher-dimensional space where a linear separator exists."
    ),
    "why": (
        "SVMs are powerful, work well in high dimensions, and were state-of-the-art for many tasks "
        "before deep learning. The margin idea and kernels are important concepts; SVMs remain "
        "strong for small/medium structured datasets and text."
    ),
    "concepts": [
        ("Hyperplane", "The linear boundary w·x + b = 0 separating classes."),
        ("Margin", "Distance from the boundary to the nearest points; SVM maximizes it."),
        ("Support vectors", "The closest points that define the margin."),
        ("Kernel trick", "Implicitly map to higher dimensions (linear, poly, RBF)."),
        ("C parameter", "Trades margin width vs misclassification (regularization)."),
        ("gamma (RBF)", "How far each point's influence reaches; controls flexibility."),
    ],
    "examples": [
        ("A linear separator: classify by the sign of w·x + b", r'''
# A hand-chosen boundary: x + y - 5 = 0. Sign tells the side/class.
def classify(point, w=(1, 1), b=-5):
    score = sum(wi * xi for wi, xi in zip(w, point)) + b
    return 1 if score >= 0 else 0, round(score, 2)

for p in [(1, 1), (4, 4), (3, 2), (5, 5)]:
    label, score = classify(p)
    print(f"{p}: score={score:5} -> class {label}")
# The 'margin' is how far points sit from score == 0.
'''),
        ("A perceptron learns a separating line (pure Python)", r'''
# Linearly separable data: class -1 (lower-left) vs +1 (upper-right)
data = [((1, 1), -1), ((2, 1), -1), ((1, 2), -1),
        ((5, 5),  1), ((6, 5),  1), ((5, 6),  1)]

w = [0.0, 0.0]
b = 0.0
lr = 0.1
for epoch in range(20):
    errors = 0
    for (x1, x2), y in data:
        score = w[0] * x1 + w[1] * x2 + b
        pred = 1 if score >= 0 else -1
        if pred != y:                       # update on mistakes
            w[0] += lr * y * x1
            w[1] += lr * y * x2
            b += lr * y
            errors += 1
    if errors == 0:                         # converged: perfectly separated
        print(f"converged at epoch {epoch}")
        break

print("weights:", [round(v, 2) for v in w], "bias:", round(b, 2))
test = (4, 4)
print(f"{test} ->", 1 if w[0]*4 + w[1]*4 + b >= 0 else -1)
'''),
        ("SVM with scikit-learn: linear vs RBF kernel", r'''
try:
    from sklearn.svm import SVC
    from sklearn.datasets import make_circles, make_classification
    from sklearn.model_selection import train_test_split

    # Linearly separable-ish data
    X, y = make_classification(n_samples=200, n_features=2, n_redundant=0,
                               n_informative=2, random_state=1)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=0)
    lin = SVC(kernel="linear", C=1.0).fit(X_tr, y_tr)
    print("linear kernel acc:", round(lin.score(X_te, y_te), 3))
    print("support vectors:", lin.n_support_.tolist())

    # Concentric circles: NOT linearly separable -> RBF wins
    Xc, yc = make_circles(n_samples=200, noise=0.1, factor=0.4, random_state=0)
    Xc_tr, Xc_te, yc_tr, yc_te = train_test_split(Xc, yc, test_size=0.3, random_state=0)
    print("RBF on circles  :", round(SVC(kernel="rbf").fit(Xc_tr, yc_tr).score(Xc_te, yc_te), 3))
    print("linear on circles:", round(SVC(kernel="linear").fit(Xc_tr, yc_tr).score(Xc_te, yc_te), 3))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "Scale features before an SVM — like KNN, it's distance/margin based.",
        "The RBF kernel needs tuning of C and gamma; bad values badly under/overfit.",
        "SVMs don't output probabilities by default (enable `probability=True`, which is slower).",
        "They scale poorly to very large datasets (training is roughly quadratic).",
        "A linear kernel can't separate non-linear data (e.g. concentric circles) — use RBF/poly.",
    ],
    "exercises": [
        ("Classify (3,3) with boundary x+y-5: which side?", "Sign of score.",
         r'''score = 3 + 3 - 5
print(1 if score >= 0 else 0, score)  # 1 1'''),
        ("What are support vectors?", "Closest points.",
         r'''#md
The training points **closest to the decision boundary** — they 'support' (define)
the margin. Moving or removing them changes the boundary; other points don't.'''),
        ("Compute the score w·x+b for w=(2,-1), x=(3,4), b=1.", "Dot + bias.",
         r'''w, x, b = (2, -1), (3, 4), 1
print(sum(wi * xi for wi, xi in zip(w, x)) + b)  # 3'''),
        ("Why use the RBF kernel?", "Non-linear data.",
         r'''#md
The **RBF kernel** maps data into a higher-dimensional space where **non-linearly
separable** classes (like concentric circles) become separable by a hyperplane.'''),
        ("A perceptron update: w=[0,0], y=1, x=(2,3), lr=0.1. New w?", "w += lr*y*x.",
         r'''w = [0.0, 0.0]; y, x, lr = 1, (2, 3), 0.1
w = [w[i] + lr * y * x[i] for i in range(2)]
print(w)  # [0.2, 0.3]'''),
        ("What does a large C do in an SVM?", "Less regularization.",
         r'''#md
A **large C** penalizes misclassifications heavily, producing a **narrower margin**
that fits training data more tightly (less regularization, more overfitting risk).
Small C allows a wider margin with some errors.'''),
        ("Is the margin wider with C small or large?", "Tradeoff.",
         r'''#md
**Smaller C** → wider margin (more tolerance for misclassified points). Larger C →
narrower margin that classifies training points more strictly.'''),
        ("Predict class of (1,1) with perceptron w=[0.2,0.3], b=-1.", "Sign.",
         r'''w, b = [0.2, 0.3], -1
print(1 if w[0]*1 + w[1]*1 + b >= 0 else -1)  # -1'''),
    ],
}

CONTENT["decision-trees"] = {
    "deps": ["scikit-learn"],
    "what": (
        "A **decision tree** classifies (or regresses) by asking a sequence of yes/no questions "
        "about features, splitting the data at each **node** to make child groups as **pure** as "
        "possible. Purity is measured by **Gini impurity** or **entropy**. Splitting continues until "
        "leaves are pure or a depth limit is hit. The result is a flowchart you can read and explain."
    ),
    "why": (
        "Trees are highly interpretable, need no feature scaling, handle non-linear relationships and "
        "mixed data types, and are the building block of random forests and gradient boosting — among "
        "the most effective models on tabular data."
    ),
    "concepts": [
        ("Node / split", "A question on one feature that divides the data."),
        ("Gini impurity", "1 − Σp²; 0 means a pure node (one class)."),
        ("Entropy / info gain", "Alternative purity measure based on information."),
        ("Leaf", "A terminal node giving the prediction (majority class)."),
        ("Max depth", "Limits tree size to prevent overfitting."),
        ("Greedy", "Picks the locally best split at each node."),
    ],
    "examples": [
        ("Gini impurity and finding the best split", r'''
from collections import Counter

def gini(labels):
    if not labels:
        return 0.0
    n = len(labels)
    return 1 - sum((c / n) ** 2 for c in Counter(labels).values())

print("gini pure   [A,A,A]:", gini(["A", "A", "A"]))      # 0.0
print("gini mixed  [A,B]  :", gini(["A", "B"]))           # 0.5
print("gini  [A,A,B,B,B]  :", round(gini(["A","A","B","B","B"]), 3))

# Best threshold split on a 1-feature dataset (minimize weighted Gini)
rows = [(1, "A"), (2, "A"), (3, "A"), (6, "B"), (7, "B"), (8, "B")]
def best_threshold(rows):
    best = None
    vals = sorted(set(x for x, _ in rows))
    for i in range(len(vals) - 1):
        t = (vals[i] + vals[i + 1]) / 2
        left = [l for x, l in rows if x <= t]
        right = [l for x, l in rows if x > t]
        weighted = (len(left) * gini(left) + len(right) * gini(right)) / len(rows)
        if best is None or weighted < best[0]:
            best = (weighted, t)
    return best
print("best split:", best_threshold(rows))   # (0.0, 4.5) -> perfectly pure
'''),
        ("Build a small decision tree from scratch", r'''
from collections import Counter

def gini(labels):
    n = len(labels)
    return 1 - sum((c / n) ** 2 for c in Counter(labels).values()) if n else 0

def best_split(rows):
    best = None
    n_features = len(rows[0][0])
    for f in range(n_features):
        for t in sorted(set(r[0][f] for r in rows)):
            left = [r for r in rows if r[0][f] <= t]
            right = [r for r in rows if r[0][f] > t]
            if not left or not right:
                continue
            g = (len(left) * gini([r[1] for r in left]) +
                 len(right) * gini([r[1] for r in right])) / len(rows)
            if best is None or g < best[0]:
                best = (g, f, t, left, right)
    return best

def build(rows, depth=0, max_depth=3):
    labels = [r[1] for r in rows]
    if len(set(labels)) == 1 or depth >= max_depth:
        return Counter(labels).most_common(1)[0][0]
    split = best_split(rows)
    if not split:
        return Counter(labels).most_common(1)[0][0]
    _, f, t, left, right = split
    return {"f": f, "t": t, "L": build(left, depth+1, max_depth),
            "R": build(right, depth+1, max_depth)}

def predict(tree, x):
    while isinstance(tree, dict):
        tree = tree["L"] if x[tree["f"]] <= tree["t"] else tree["R"]
    return tree

data = [((2, 1), 0), ((1, 1), 0), ((2, 2), 0),
        ((6, 5), 1), ((7, 4), 1), ((6, 6), 1)]
tree = build(data)
print("tree:", tree)
print("predict (2,2) ->", predict(tree, (2, 2)))   # 0
print("predict (6,5) ->", predict(tree, (6, 5)))   # 1
'''),
        ("Decision tree with scikit-learn", r'''
try:
    from sklearn.tree import DecisionTreeClassifier, export_text
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split

    X, y = load_iris(return_X_y=True)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)

    clf = DecisionTreeClassifier(max_depth=3, random_state=0).fit(X_tr, y_tr)
    print("accuracy:", round(clf.score(X_te, y_te), 3))
    print("feature importances:", clf.feature_importances_.round(3).tolist())
    print("\ntree rules:\n", export_text(clf, max_depth=2))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "Unpruned trees overfit badly (pure leaves memorize) — limit depth or min_samples_leaf.",
        "Greedy splitting isn't globally optimal; a slightly worse split now can be better overall.",
        "Small data changes can flip splits — trees are high-variance (random forests fix this).",
        "They can't extrapolate beyond the training range; predictions are piecewise-constant.",
        "Biased toward features with many distinct values when using naive impurity gains.",
    ],
    "exercises": [
        ("Compute the Gini impurity of [A,A,B,B].", "1 - sum p^2.",
         r'''from collections import Counter
labels = ["A", "A", "B", "B"]
n = len(labels)
print(1 - sum((c / n) ** 2 for c in Counter(labels).values()))  # 0.5'''),
        ("What Gini value means a perfectly pure node?", "Single class.",
         r'''#md
**0.0** — all samples belong to one class, so there is no impurity.'''),
        ("Split [1,2,3,9,10] at threshold 5: list the two groups.", "<= vs >.",
         r'''data = [1, 2, 3, 9, 10]
print([x for x in data if x <= 5], [x for x in data if x > 5])'''),
        ("Predict with leaf rule: x[0]<=4 -> 'cat' else 'dog' for x=(6,).", "Compare.",
         r'''x = (6,)
print("cat" if x[0] <= 4 else "dog")  # dog'''),
        ("Why limit max_depth?", "Prevent overfitting.",
         r'''#md
Deep trees keep splitting until leaves are pure, memorizing noise (**overfitting**).
Limiting depth keeps the tree simpler so it **generalizes** to new data.'''),
        ("Compute weighted Gini: left [A,A] (gini0), right [A,B] (gini0.5), sizes 2 and 2.", "Weighted avg.",
         r'''print((2 * 0.0 + 2 * 0.5) / 4)  # 0.25'''),
        ("Do decision trees need feature scaling?", "Threshold-based.",
         r'''#md
**No.** Splits compare a feature to a threshold, which is unaffected by monotonic
scaling — so standardization/normalization is unnecessary for trees.'''),
        ("Majority class of leaf labels [1,1,1,0].", "Most common.",
         r'''from collections import Counter
print(Counter([1, 1, 1, 0]).most_common(1)[0][0])  # 1'''),
    ],
}

CONTENT["random-forests"] = {
    "deps": ["scikit-learn"],
    "what": (
        "A **random forest** is an **ensemble** of many decision trees whose predictions are "
        "combined (majority vote for classification, average for regression). Each tree trains on a "
        "**bootstrap sample** (random rows with replacement) and considers a **random subset of "
        "features** at each split. This **bagging** + feature randomness decorrelates the trees, "
        "slashing variance and overfitting while keeping low bias."
    ),
    "why": (
        "Random forests are one of the best out-of-the-box models for tabular data: accurate, robust "
        "to outliers and noise, need little tuning, and provide feature-importance estimates. They "
        "fix the high variance of single trees."
    ),
    "concepts": [
        ("Ensemble", "Combine many models for a better, more stable prediction."),
        ("Bagging", "Bootstrap Aggregating: train each tree on a resample of the data."),
        ("Bootstrap sample", "Random rows drawn WITH replacement (~63% unique)."),
        ("Feature randomness", "Each split considers a random feature subset."),
        ("Voting / averaging", "Aggregate tree outputs into one prediction."),
        ("Feature importance", "How much each feature reduces impurity across trees."),
    ],
    "examples": [
        ("Bootstrap sampling (the heart of bagging)", r'''
import random
random.seed(0)

data = [10, 20, 30, 40, 50]

# A bootstrap sample: draw len(data) items WITH replacement
def bootstrap(data):
    return [random.choice(data) for _ in range(len(data))]

for i in range(3):
    sample = bootstrap(data)
    unique = len(set(sample))
    print(f"sample {i}: {sample}  ({unique}/{len(data)} unique)")
# On average ~63% of rows appear; the rest are 'out-of-bag'.
'''),
        ("A tiny forest of stumps with majority voting", r'''
import random
from collections import Counter
random.seed(1)

# 1-feature data: small x -> 0, large x -> 1 (with a little noise)
data = [(1, 0), (2, 0), (3, 0), (3, 1), (6, 1), (7, 1), (8, 1), (2, 0)]

def gini(labels):
    n = len(labels)
    return 1 - sum((c / n) ** 2 for c in Counter(labels).values()) if n else 0

def train_stump(rows):
    best = None
    for t in sorted(set(x for x, _ in rows)):
        left = [l for x, l in rows if x <= t]
        right = [l for x, l in rows if x > t]
        if not left or not right:
            continue
        g = (len(left)*gini(left) + len(right)*gini(right)) / len(rows)
        if best is None or g < best[0]:
            lbl_L = Counter(left).most_common(1)[0][0]
            lbl_R = Counter(right).most_common(1)[0][0]
            best = (g, t, lbl_L, lbl_R)
    return best        # (gini, threshold, left_label, right_label)

# Train a forest: each stump on its own bootstrap sample
forest = []
for _ in range(11):
    sample = [random.choice(data) for _ in range(len(data))]
    forest.append(train_stump(sample))

def forest_predict(x):
    votes = [lblL if x <= t else lblR for _, t, lblL, lblR in forest]
    return Counter(votes).most_common(1)[0][0]

for x in [2, 5, 8]:
    print(f"x={x} -> class {forest_predict(x)}")
'''),
        ("Random forest with scikit-learn", r'''
try:
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.datasets import load_wine
    from sklearn.model_selection import train_test_split

    X, y = load_wine(return_X_y=True)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)

    rf = RandomForestClassifier(n_estimators=100, random_state=0).fit(X_tr, y_tr)
    print("accuracy:", round(rf.score(X_te, y_te), 3))

    # Top-3 most important features
    importances = list(enumerate(rf.feature_importances_))
    top = sorted(importances, key=lambda x: -x[1])[:3]
    print("top features (index, importance):",
          [(i, round(v, 3)) for i, v in top])
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "More trees never hurt accuracy but cost time/memory — there are diminishing returns.",
        "A forest is less interpretable than one tree; use feature importances / SHAP to explain.",
        "Importances are biased toward high-cardinality features — interpret with care.",
        "If all trees see the same features/data they correlate; randomness is what makes it work.",
        "Forests can still overfit noisy data; tune depth, min_samples_leaf, and max_features.",
    ],
    "exercises": [
        ("Draw a bootstrap sample of [1,2,3] (with replacement) using seed 0.", "random.choice x3.",
         r'''import random
random.seed(0)
data = [1, 2, 3]
print([random.choice(data) for _ in range(3)])'''),
        ("Majority-vote the predictions [1,1,0,1,0].", "Counter.",
         r'''from collections import Counter
print(Counter([1, 1, 0, 1, 0]).most_common(1)[0][0])  # 1'''),
        ("What fraction of rows appear in a bootstrap sample on average?", "~63%.",
         r'''#md
About **63.2%** (1 − 1/e). The remaining ~37% are 'out-of-bag' and can be used for
free validation.'''),
        ("Average the regression predictions [2.0,3.0,4.0].", "Mean.",
         r'''preds = [2.0, 3.0, 4.0]
print(sum(preds) / len(preds))  # 3.0'''),
        ("Why does a forest reduce variance vs a single tree?", "Decorrelation.",
         r'''#md
Averaging many **decorrelated** trees (each on different rows/features) cancels out
their individual errors/noise, so the ensemble is far more **stable** (lower
variance) than any single high-variance tree.'''),
        ("How many trees in RandomForestClassifier(n_estimators=50)?", "Read the param.",
         r'''#md
**50** trees — `n_estimators` sets the number of trees in the forest.'''),
        ("Combine 3 trees voting [A,B,A] — final class?", "Majority.",
         r'''from collections import Counter
print(Counter(["A", "B", "A"]).most_common(1)[0][0])  # A'''),
        ("Name one advantage of random forests over a single decision tree.", "Stability.",
         r'''#md
Lower **variance / overfitting** (more accurate and stable), thanks to averaging
many decorrelated trees — at the cost of interpretability.'''),
    ],
}

CONTENT["naive-bayes"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**Naive Bayes** classifiers apply **Bayes' theorem** with a 'naive' assumption: features "
        "are **conditionally independent** given the class. They estimate P(class) and P(feature|"
        "class) from training data, then pick the class with the highest posterior. Variants: "
        "**Gaussian** (continuous features), **Multinomial** (counts, e.g. word frequencies), and "
        "**Bernoulli** (binary features)."
    ),
    "why": (
        "Despite the simplistic independence assumption, Naive Bayes is fast, needs little data, and "
        "works remarkably well for text (spam filtering, sentiment). It's a classic strong baseline "
        "for high-dimensional sparse data."
    ),
    "concepts": [
        ("Bayes' theorem", "P(class|x) ∝ P(x|class)·P(class)."),
        ("Conditional independence", "Assume features don't interact given the class."),
        ("Prior", "Base rate of each class P(class)."),
        ("Likelihood", "P(feature|class), modeled by Gaussian/Multinomial/Bernoulli."),
        ("Laplace smoothing", "Add 1 to counts so unseen features don't zero out."),
        ("Log probabilities", "Sum logs instead of multiplying to avoid underflow."),
    ],
    "examples": [
        ("Gaussian Naive Bayes from scratch", r'''
import math
import statistics as st

# features: (height_ft, weight_lb) -> class
train = [((5.0, 100), "cat"), ((5.5, 110), "cat"), ((4.8, 95), "cat"),
         ((6.5, 200), "dog"), ((7.0, 220), "dog"), ((6.8, 210), "dog")]

classes = set(label for _, label in train)
priors, stats = {}, {}
for c in classes:
    feats = [f for f, label in train if label == c]
    priors[c] = len(feats) / len(train)
    # mean and variance of each feature column for this class
    stats[c] = [(st.mean(col), st.pvariance(col) or 1e-6) for col in zip(*feats)]

def gaussian(x, mean, var):
    return math.exp(-(x - mean) ** 2 / (2 * var)) / math.sqrt(2 * math.pi * var)

def predict(x):
    best_c, best_p = None, -1.0
    for c in classes:
        p = priors[c]
        for xi, (m, v) in zip(x, stats[c]):
            p *= gaussian(xi, m, v)
        if p > best_p:
            best_c, best_p = c, p
    return best_c

print("(5.2, 105) ->", predict((5.2, 105)))   # cat
print("(6.9, 205) ->", predict((6.9, 205)))   # dog
'''),
        ("Multinomial Naive Bayes for spam (text)", r'''
import math
from collections import Counter

train = [("buy cheap meds now", "spam"), ("cheap meds buy", "spam"),
         ("limited offer buy now", "spam"), ("meeting tomorrow team", "ham"),
         ("project deadline tomorrow", "ham"), ("lunch meeting now", "ham")]

vocab = set()
word_counts = {"spam": Counter(), "ham": Counter()}
doc_counts = Counter()
for text, label in train:
    doc_counts[label] += 1
    for w in text.split():
        word_counts[label][w] += 1
        vocab.add(w)

def predict(text):
    total_docs = sum(doc_counts.values())
    best_c, best_score = None, float("-inf")
    for c in word_counts:
        score = math.log(doc_counts[c] / total_docs)          # log prior
        total_words = sum(word_counts[c].values())
        for w in text.split():
            # Laplace-smoothed likelihood
            score += math.log((word_counts[c][w] + 1) /
                              (total_words + len(vocab)))
        if score > best_score:
            best_c, best_score = c, score
    return best_c

print("'cheap buy now'      ->", predict("cheap buy now"))      # spam
print("'project meeting'    ->", predict("project meeting"))    # ham
'''),
        ("Naive Bayes with scikit-learn", r'''
try:
    from sklearn.naive_bayes import GaussianNB
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split

    X, y = load_iris(return_X_y=True)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)

    nb = GaussianNB().fit(X_tr, y_tr)
    print("accuracy:", round(nb.score(X_te, y_te), 3))
    print("class priors:", nb.class_prior_.round(3).tolist())
    print("predict first 5:", nb.predict(X_te[:5]).tolist())
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "Without smoothing, an unseen feature gives probability 0 and zeros the whole product.",
        "Multiply many small probabilities → underflow; sum LOG-probabilities instead.",
        "The independence assumption is usually false, but the classifier is still useful.",
        "Use the RIGHT variant: Gaussian for continuous, Multinomial for counts, Bernoulli for binary.",
        "Probabilities are often poorly calibrated (too extreme) — trust the ranking, not the value.",
    ],
    "exercises": [
        ("Apply Bayes: P(A|B)=P(B|A)P(A)/P(B) with P(B|A)=0.8,P(A)=0.25,P(B)=0.4.", "Plug in.",
         r'''print(0.8 * 0.25 / 0.4)  # 0.5'''),
        ("Why add 1 in Laplace smoothing?", "Avoid zero probability.",
         r'''#md
So a feature never seen with a class doesn't make its likelihood **0** (which would
zero out the entire product). Adding 1 to every count keeps all probabilities
positive.'''),
        ("Compute a Gaussian likelihood at x=mean (peak).", "Max density.",
         r'''import math
var = 4.0
print(round(1 / math.sqrt(2 * math.pi * var), 4))  # peak density'''),
        ("Sum log-probs log(0.5)+log(0.25).", "Logs add.",
         r'''import math
print(round(math.log(0.5) + math.log(0.25), 4))'''),
        ("Which NB variant for word-count features?", "Counts.",
         r'''#md
**Multinomial** Naive Bayes — designed for discrete **count** features such as word
frequencies in text.'''),
        ("Compute the prior P(spam) from 3 spam / 5 total docs.", "count/total.",
         r'''print(3 / 5)  # 0.6'''),
        ("Why use logs instead of multiplying probabilities?", "Underflow.",
         r'''#md
Multiplying many small probabilities **underflows** to 0 in floating point. Summing
their **logarithms** is numerically stable and monotonic (preserves the ranking).'''),
        ("Pick the class with higher score: spam=-5.2, ham=-6.1.", "Max (least negative).",
         r'''scores = {"spam": -5.2, "ham": -6.1}
print(max(scores, key=scores.get))  # spam'''),
    ],
}

CONTENT["gradient-boosting"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**Gradient boosting** builds an ensemble **sequentially**: each new weak learner (usually a "
        "shallow tree) is trained to correct the **residual errors** of the current ensemble. "
        "Predictions are added together, scaled by a **learning rate**. Unlike random forests "
        "(parallel, independent trees), boosting is additive and focuses on the mistakes — "
        "powering XGBoost, LightGBM, and CatBoost."
    ),
    "why": (
        "Gradient-boosted trees are the dominant approach for tabular ML competitions and many "
        "production systems — typically the most accurate off-the-shelf model. Understanding the "
        "residual-fitting idea demystifies them."
    ),
    "concepts": [
        ("Weak learner", "A simple model (shallow tree/stump) slightly better than chance."),
        ("Residuals", "The errors (actual − predicted) the next learner targets."),
        ("Additive model", "Final prediction = sum of all learners' outputs."),
        ("Learning rate", "Shrinks each learner's contribution to avoid overfitting."),
        ("Sequential", "Each tree depends on the ones before it."),
        ("vs bagging", "Boosting reduces bias by focusing on errors; bagging reduces variance."),
    ],
    "examples": [
        ("Boosting residuals with stumps (1-D regression)", r'''
data = [(1, 1.0), (2, 1.5), (3, 3.5), (4, 4.2), (5, 6.0)]
xs = [x for x, _ in data]
ys = [y for _, y in data]

def best_stump(xs, residuals):
    # threshold that best predicts residuals by side means (min SSE)
    best = None
    for t in sorted(set(xs)):
        left = [r for x, r in zip(xs, residuals) if x <= t]
        right = [r for x, r in zip(xs, residuals) if x > t]
        if not left or not right:
            continue
        lm, rm = sum(left) / len(left), sum(right) / len(right)
        sse = sum((r - lm) ** 2 for r in left) + sum((r - rm) ** 2 for r in right)
        if best is None or sse < best[0]:
            best = (sse, t, lm, rm)
    return best

pred = [sum(ys) / len(ys)] * len(ys)     # start from the mean
lr = 0.5
for rnd in range(6):
    residuals = [y - p for y, p in zip(ys, pred)]
    _, t, lm, rm = best_stump(xs, residuals)
    pred = [p + lr * (lm if x <= t else rm) for x, p in zip(xs, pred)]
    mse = sum((y - p) ** 2 for y, p in zip(ys, pred)) / len(ys)
    print(f"round {rnd}: split@{t}, MSE={mse:.4f}")
print("final preds:", [round(p, 2) for p in pred])
'''),
        ("Why the learning rate matters", r'''
# Same idea, compare a small vs large learning rate over a few rounds.
ys = [10, 12, 14, 16]
def boost(lr, rounds=5):
    pred = [sum(ys) / len(ys)] * len(ys)
    for _ in range(rounds):
        residuals = [y - p for y, p in zip(ys, pred)]
        # one global stump: just add the mean residual (toy weak learner)
        step = sum(residuals) / len(residuals)
        pred = [p + lr * step for p in pred]
    return sum((y - p) ** 2 for y, p in zip(ys, pred)) / len(ys)

for lr in [0.1, 0.5, 1.0]:
    print(f"lr={lr}: final MSE after 5 rounds = {boost(lr):.4f}")
# Smaller lr learns slower but is more robust; larger lr can overshoot.
'''),
        ("Gradient boosting with scikit-learn", r'''
try:
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.datasets import load_breast_cancer
    from sklearn.model_selection import train_test_split

    X, y = load_breast_cancer(return_X_y=True)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)

    gb = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1,
                                    max_depth=3, random_state=0).fit(X_tr, y_tr)
    print("accuracy:", round(gb.score(X_te, y_te), 3))
    print("n_estimators:", gb.n_estimators_, "| lr:", gb.learning_rate)
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "Boosting trains sequentially — it can't parallelize across trees like a random forest.",
        "Too many rounds or too-high learning rate overfits; tune n_estimators with early stopping.",
        "Sensitive to noisy data and outliers because it keeps chasing residuals.",
        "Use SHALLOW trees (stumps to depth ~3) as weak learners; deep trees defeat the purpose.",
        "Lower learning rate usually needs more trees — they trade off (lr × n_estimators).",
    ],
    "exercises": [
        ("Compute residuals of preds [2,4,6] vs truth [3,5,5].", "actual - predicted.",
         r'''pred, true = [2, 4, 6], [3, 5, 5]
print([t - p for p, t in zip(pred, true)])  # [1, 1, -1]'''),
        ("Update a prediction p=5 by lr=0.1 times step=4.", "p += lr*step.",
         r'''p, lr, step = 5, 0.1, 4
print(p + lr * step)  # 5.4'''),
        ("How does boosting differ from bagging (one line)?", "Sequential vs parallel.",
         r'''#md
**Boosting** trains learners **sequentially**, each fixing the previous errors
(reduces bias). **Bagging** trains learners **independently in parallel** and
averages them (reduces variance).'''),
        ("Final prediction = sum of [3.0, 0.5, -0.2]. Compute it.", "Additive model.",
         r'''print(sum([3.0, 0.5, -0.2]))  # 3.3'''),
        ("Why use a small learning rate?", "Robustness.",
         r'''#md
A small learning rate makes each tree contribute a little, so the ensemble learns
**gradually and robustly**, reducing overfitting — at the cost of needing more
trees.'''),
        ("What kind of trees are used as weak learners?", "Shallow.",
         r'''#md
**Shallow** trees (often stumps, or depth ≤ ~3). Each only needs to be slightly
better than chance; depth comes from combining many of them.'''),
        ("Mean residual of [2,-1,2,-3]?", "Average.",
         r'''r = [2, -1, 2, -3]
print(sum(r) / len(r))  # 0.0'''),
        ("If lr=0.1 and you want similar power to lr=0.5 with 100 trees, more or fewer trees?", "Tradeoff.",
         r'''#md
**More** trees. Lower learning rate means each step is smaller, so you need
proportionally **more estimators** to reach the same total fit.'''),
    ],
}

CONTENT["kmeans-clustering"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**K-Means** is an **unsupervised** algorithm that partitions data into **k clusters**. It "
        "alternates two steps until stable: **assign** each point to the nearest **centroid**, then "
        "**update** each centroid to the mean of its assigned points. It minimizes within-cluster "
        "variance (**inertia**). You choose k (e.g. via the **elbow method**)."
    ),
    "why": (
        "Clustering finds natural groups without labels — customer segmentation, image color "
        "quantization, anomaly grouping, document topics. K-Means is the fast, simple default and "
        "teaches the assign/update (EM-style) pattern."
    ),
    "concepts": [
        ("Centroid", "The mean point of a cluster."),
        ("Assignment step", "Put each point in the nearest centroid's cluster."),
        ("Update step", "Move each centroid to its cluster's mean."),
        ("Inertia (WCSS)", "Sum of squared distances to centroids — lower is tighter."),
        ("Elbow method", "Plot inertia vs k; the 'elbow' suggests a good k."),
        ("k-means++", "Smart centroid initialization for better, faster convergence."),
    ],
    "examples": [
        ("K-Means from scratch", r'''
import random, math
random.seed(0)

points = [(1, 1), (1.5, 2), (1, 0.5),
          (8, 8), (9, 8), (8.5, 9),
          (1, 8), (1.5, 8.5)]

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def kmeans(points, k, iterations=20):
    centroids = random.sample(points, k)         # random init
    for _ in range(iterations):
        # ASSIGN each point to its nearest centroid
        clusters = [[] for _ in range(k)]
        for p in points:
            nearest = min(range(k), key=lambda i: dist(p, centroids[i]))
            clusters[nearest].append(p)
        # UPDATE centroids to cluster means
        new = []
        for i, cluster in enumerate(clusters):
            if cluster:
                cx = sum(p[0] for p in cluster) / len(cluster)
                cy = sum(p[1] for p in cluster) / len(cluster)
                new.append((cx, cy))
            else:
                new.append(centroids[i])
        if new == centroids:                     # converged
            break
        centroids = new
    return centroids, clusters

centroids, clusters = kmeans(points, k=3)
for i, (c, cl) in enumerate(zip(centroids, clusters)):
    print(f"cluster {i}: centroid={tuple(round(v,2) for v in c)}, points={cl}")
'''),
        ("Inertia and the elbow method", r'''
import random, math
random.seed(0)
points = [(1, 1), (1.5, 2), (1, 0.5), (8, 8), (9, 8), (8.5, 9)]

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def kmeans_inertia(points, k, iters=20):
    centroids = random.sample(points, k)
    clusters = [[] for _ in range(k)]
    for _ in range(iters):
        clusters = [[] for _ in range(k)]
        for p in points:
            i = min(range(k), key=lambda j: dist(p, centroids[j]))
            clusters[i].append(p)
        centroids = [(sum(q[0] for q in c)/len(c), sum(q[1] for q in c)/len(c))
                     if c else centroids[i] for i, c in enumerate(clusters)]
    inertia = sum(dist(p, centroids[i]) ** 2
                  for i, c in enumerate(clusters) for p in c)
    return inertia

for k in range(1, 5):
    print(f"k={k}: inertia={kmeans_inertia(points, k):.2f}")
# Inertia drops sharply then levels off — the 'elbow' hints at the best k (2 here).
'''),
        ("K-Means with scikit-learn", r'''
try:
    from sklearn.cluster import KMeans
    from sklearn.datasets import make_blobs

    X, _ = make_blobs(n_samples=150, centers=3, random_state=0)
    km = KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)
    print("inertia:", round(km.inertia_, 2))
    print("centroids:\n", km.cluster_centers_.round(2))
    print("first 10 labels:", km.labels_[:10].tolist())
    print("predict new point:", km.predict([[0, 0]]).tolist())
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "You must choose k in advance; the elbow/silhouette methods help estimate it.",
        "Results depend on random init — run multiple times (k-means++ / n_init) and keep the best.",
        "K-Means assumes spherical, similar-size clusters; it fails on elongated/odd shapes.",
        "Unscaled features distort distances — standardize first.",
        "Outliers pull centroids; consider removing them or using k-medoids.",
    ],
    "exercises": [
        ("Compute the centroid (mean) of points [(0,0),(2,2),(4,4)].", "Average coords.",
         r'''pts = [(0, 0), (2, 2), (4, 4)]
cx = sum(p[0] for p in pts) / len(pts)
cy = sum(p[1] for p in pts) / len(pts)
print((cx, cy))  # (2.0, 2.0)'''),
        ("Assign point (1,1) to the nearer of centroids (0,0),(5,5).", "Min distance.",
         r'''import math
def d(a, b): return math.dist(a, b)
p = (1, 1); cents = [(0, 0), (5, 5)]
print(min(range(2), key=lambda i: d(p, cents[i])))  # 0'''),
        ("Compute inertia for points [(0,0),(2,0)] around centroid (1,0).", "Sum sq dist.",
         r'''import math
c = (1, 0)
print(sum(math.dist(p, c) ** 2 for p in [(0, 0), (2, 0)]))  # 2.0'''),
        ("What does the elbow method help choose?", "Number of clusters.",
         r'''#md
The value of **k** (number of clusters). You plot inertia vs k and pick the 'elbow'
where adding more clusters stops sharply reducing inertia.'''),
        ("Why scale features before K-Means?", "Distance fairness.",
         r'''#md
K-Means uses Euclidean distance, so a large-range feature dominates the clustering.
**Standardizing** gives each feature comparable influence.'''),
        ("Move centroid to the mean of assigned [(1,2),(3,4),(5,0)].", "Mean.",
         r'''pts = [(1, 2), (3, 4), (5, 0)]
print((sum(p[0] for p in pts)/3, sum(p[1] for p in pts)/3))  # (3.0, 2.0)'''),
        ("Why run K-Means multiple times?", "Random init.",
         r'''#md
Because the result depends on the **random initial centroids**, different runs can
converge to different (worse) solutions. Running several times (n_init) and keeping
the lowest-inertia result avoids bad local minima.'''),
        ("Name the two alternating steps of K-Means.", "Assign/update.",
         r'''#md
1) **Assignment** — assign each point to its nearest centroid. 2) **Update** — move
each centroid to the mean of its assigned points. Repeat until stable.'''),
    ],
}

CONTENT["hierarchical-clustering"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**Hierarchical clustering** builds a tree of clusters (a **dendrogram**). The common "
        "**agglomerative** approach starts with each point as its own cluster and repeatedly "
        "**merges the two closest clusters** until one remains. 'Closest' depends on a **linkage**: "
        "single (min distance), complete (max), or average. You cut the dendrogram at a height to "
        "get any number of clusters — no need to pre-specify k."
    ),
    "why": (
        "It reveals nested structure and relationships at multiple scales, doesn't require choosing k "
        "up front, and the dendrogram is a great visualization. Used in genomics, document "
        "organization, and taxonomy."
    ),
    "concepts": [
        ("Agglomerative", "Bottom-up: start with singletons, merge upward."),
        ("Linkage", "How to measure cluster distance: single/complete/average/ward."),
        ("Dendrogram", "Tree diagram of the merge order and heights."),
        ("Cut height", "Slice the tree to choose the number of clusters."),
        ("No preset k", "Decide clusters after seeing the structure."),
        ("Distance matrix", "Pairwise distances drive the merges."),
    ],
    "examples": [
        ("Agglomerative single-linkage from scratch", r'''
import math

pts = {"A": (1, 1), "B": (1.5, 1.5), "C": (5, 5), "D": (5.5, 5), "E": (9, 9)}

def dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

def single_linkage(c1, c2):
    return min(dist(pts[a], pts[b]) for a in c1 for b in c2)

clusters = [[name] for name in pts]      # each point starts alone
while len(clusters) > 1:
    # find the two closest clusters
    best = None
    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            d = single_linkage(clusters[i], clusters[j])
            if best is None or d < best[0]:
                best = (d, i, j)
    d, i, j = best
    print(f"merge {clusters[i]} + {clusters[j]}  (distance {d:.2f})")
    clusters[i] = clusters[i] + clusters[j]
    del clusters[j]
'''),
        ("Cutting the tree to get k clusters", r'''
import math

pts = {"A": (1, 1), "B": (1.5, 1.5), "C": (5, 5), "D": (5.5, 5), "E": (9, 9)}
def dist(a, b): return math.sqrt(sum((x-y)**2 for x, y in zip(a, b)))
def linkage(c1, c2): return min(dist(pts[a], pts[b]) for a in c1 for b in c2)

def cluster_until(k):
    clusters = [[n] for n in pts]
    while len(clusters) > k:              # stop once we have k clusters
        best = None
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                d = linkage(clusters[i], clusters[j])
                if best is None or d < best[0]:
                    best = (d, i, j)
        _, i, j = best
        clusters[i] += clusters[j]
        del clusters[j]
    return clusters

print("2 clusters:", cluster_until(2))
print("3 clusters:", cluster_until(3))
'''),
        ("Hierarchical clustering with scikit-learn / SciPy", r'''
try:
    from sklearn.cluster import AgglomerativeClustering
    X = [[1, 1], [1.5, 1.5], [5, 5], [5.5, 5], [9, 9]]
    model = AgglomerativeClustering(n_clusters=2, linkage="single").fit(X)
    print("sklearn labels:", model.labels_.tolist())

    try:
        from scipy.cluster.hierarchy import linkage, fcluster
        Z = linkage(X, method="single")       # the linkage matrix
        print("scipy 2-cluster labels:", fcluster(Z, t=2, criterion="maxclust").tolist())
    except ImportError:
        print("scipy not installed — pip install scipy for dendrograms")
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn scipy")
'''),
    ],
    "gotchas": [
        "Naive agglomerative clustering is O(n³)/O(n²) — too slow for very large datasets.",
        "Linkage choice changes results: single linkage 'chains', complete makes compact clusters.",
        "Scale features first — distances drive every merge.",
        "Once merged, clusters can't be split — early mistakes propagate (greedy).",
        "Reading a dendrogram: the merge HEIGHT is the distance, not the horizontal position.",
    ],
    "exercises": [
        ("Compute the distance between (0,0) and (3,4).", "Euclidean.",
         r'''import math
print(math.dist((0, 0), (3, 4)))  # 5.0'''),
        ("Single-linkage distance between {A,B} and {C}: min of AC,BC = min(4,3).", "Take min.",
         r'''print(min(4, 3))  # 3'''),
        ("Complete-linkage distance for the same: max(4,3).", "Take max.",
         r'''print(max(4, 3))  # 4'''),
        ("Do you need to choose k before hierarchical clustering?", "Cut later.",
         r'''#md
**No.** You build the full dendrogram first, then **cut it at a chosen height** to
get however many clusters you want — k is decided after seeing the structure.'''),
        ("Start with 5 points: how many merges to reach 1 cluster?", "n-1.",
         r'''print(5 - 1)  # 4'''),
        ("What does the height of a merge in a dendrogram represent?", "Distance.",
         r'''#md
The **distance** (dissimilarity) at which the two clusters were merged. Merges low
on the tree are very similar; high merges join dissimilar groups.'''),
        ("Average-linkage of distances [2,4,6] between cluster members.", "Mean.",
         r'''d = [2, 4, 6]
print(sum(d) / len(d))  # 4.0'''),
        ("Single linkage tends to produce what artifact?", "Chaining.",
         r'''#md
**Chaining** — clusters can stretch into long thin chains because only the single
closest pair is needed to merge, linking far-apart points through intermediates.'''),
    ],
}

CONTENT["dbscan"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) groups points that "
        "are **densely packed** and labels sparse points as **noise**. Two parameters: **eps** (the "
        "neighborhood radius) and **min_pts** (how many neighbors make a **core point**). It finds "
        "**arbitrarily shaped** clusters and the number of clusters **automatically** — unlike "
        "K-Means."
    ),
    "why": (
        "DBSCAN handles non-spherical clusters, doesn't need k, and explicitly detects outliers — "
        "ideal for spatial data, anomaly detection, and messy real-world data where K-Means fails."
    ),
    "concepts": [
        ("eps", "Radius defining a point's neighborhood."),
        ("min_pts", "Minimum neighbors (incl. self) to be a core point."),
        ("Core point", "Has ≥ min_pts neighbors within eps."),
        ("Border point", "Within eps of a core point but not core itself."),
        ("Noise", "Neither core nor border — an outlier."),
        ("No preset k", "Cluster count emerges from the density structure."),
    ],
    "examples": [
        ("DBSCAN from scratch", r'''
import math

points = [(1, 1), (1.2, 1.1), (0.8, 1.0),      # dense cluster 0
          (8, 8), (8.1, 8.2),                   # dense cluster 1
          (5, 5)]                               # lone noise point
eps, min_pts = 1.0, 2

def neighbors(i):
    return [j for j in range(len(points)) if math.dist(points[i], points[j]) <= eps]

labels = [None] * len(points)     # None=unvisited, -1=noise, >=0 cluster id
cluster_id = 0
for i in range(len(points)):
    if labels[i] is not None:
        continue
    nbrs = neighbors(i)
    if len(nbrs) < min_pts:
        labels[i] = -1            # provisionally noise
        continue
    labels[i] = cluster_id        # start a new cluster
    seeds = list(nbrs)
    k = 0
    while k < len(seeds):
        j = seeds[k]
        if labels[j] == -1:
            labels[j] = cluster_id            # border point
        elif labels[j] is None:
            labels[j] = cluster_id
            j_nbrs = neighbors(j)
            if len(j_nbrs) >= min_pts:         # j is core -> expand
                seeds += j_nbrs
        k += 1
    cluster_id += 1

for p, lab in zip(points, labels):
    kind = "noise" if lab == -1 else f"cluster {lab}"
    print(f"{p} -> {kind}")
'''),
        ("Classifying core / border / noise points", r'''
import math

points = [(0, 0), (0.5, 0), (1, 0), (5, 5)]
eps, min_pts = 1.0, 3

def neighbor_count(i):
    return sum(1 for j in range(len(points)) if math.dist(points[i], points[j]) <= eps)

for i, p in enumerate(points):
    c = neighbor_count(i)
    role = "core" if c >= min_pts else "non-core"
    print(f"{p}: {c} neighbors -> {role}")
# Non-core points near a core become 'border'; isolated ones are 'noise'.
'''),
        ("DBSCAN with scikit-learn", r'''
try:
    from sklearn.cluster import DBSCAN
    from sklearn.datasets import make_moons

    X, _ = make_moons(n_samples=150, noise=0.06, random_state=0)
    db = DBSCAN(eps=0.2, min_samples=5).fit(X)
    labels = db.labels_
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise = list(labels).count(-1)
    print("clusters found:", n_clusters)      # ~2 crescent shapes
    print("noise points  :", n_noise)
    print("first 10 labels:", labels[:10].tolist())
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "DBSCAN is very sensitive to eps — too small = all noise, too big = one blob.",
        "It struggles when clusters have very different densities (one eps can't fit all).",
        "Distance-based, so scale features first; high dimensions weaken density estimates.",
        "Border points can be assigned to whichever core reaches them first (order-dependent).",
        "Pick min_pts ≈ dimensions + 1 (or more); eps via a k-distance plot.",
    ],
    "exercises": [
        ("Count neighbors of (0,0) within eps=1 among [(0,0),(0.5,0),(2,0)].", "Distance <= eps.",
         r'''import math
pts = [(0, 0), (0.5, 0), (2, 0)]
print(sum(1 for p in pts if math.dist((0, 0), p) <= 1))  # 2'''),
        ("Is a point with 4 neighbors a core point if min_pts=3?", "Compare.",
         r'''print(4 >= 3)  # True -> core'''),
        ("What label does DBSCAN give an isolated outlier?", "Noise.",
         r'''#md
**Noise** (typically labeled **-1**) — it is neither a core point nor within eps of
one.'''),
        ("Does DBSCAN need the number of clusters in advance?", "Density-driven.",
         r'''#md
**No.** The number of clusters emerges from the density structure (eps + min_pts);
you don't specify k.'''),
        ("Classify: 1 neighbor, min_pts=3 — core or not?", "Below threshold.",
         r'''print("core" if 1 >= 3 else "not core")  # not core'''),
        ("Why scale features before DBSCAN?", "Distance based.",
         r'''#md
DBSCAN measures density via Euclidean distance, so unscaled features with large
ranges dominate. **Standardizing** makes eps meaningful across all features.'''),
        ("Name the two DBSCAN parameters.", "eps, min_pts.",
         r'''#md
**eps** (neighborhood radius) and **min_samples / min_pts** (minimum neighbors for
a core point).'''),
        ("If eps is too large, what happens?", "Over-merge.",
         r'''#md
Everything falls within everyone's neighborhood, so distinct clusters **merge into
one giant blob** (and almost nothing is labeled noise).'''),
    ],
}

CONTENT["pca"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**Principal Component Analysis (PCA)** reduces dimensionality by finding new axes "
        "(**principal components**) along which the data varies most. PC1 captures the most "
        "variance, PC2 the next (orthogonal to PC1), and so on. Projecting onto the top few "
        "components compresses the data while keeping most of its structure. Mechanically: center "
        "the data, compute the **covariance matrix**, and take its top **eigenvectors**."
    ),
    "why": (
        "PCA fights the curse of dimensionality, speeds up models, removes correlated/redundant "
        "features, and enables 2-D visualization of high-dimensional data — a standard preprocessing "
        "and exploration tool."
    ),
    "concepts": [
        ("Principal component", "A direction of maximum variance in the data."),
        ("Center the data", "Subtract the mean so PCA measures variance about 0."),
        ("Covariance matrix", "Captures how features vary together."),
        ("Eigenvectors/values", "Directions (components) and how much variance each holds."),
        ("Explained variance", "Fraction of total variance kept by each component."),
        ("Projection", "Map points onto the chosen components (the new coordinates)."),
    ],
    "examples": [
        ("PCA on 2-D data from scratch", r'''
import math

# Data that mostly varies along the diagonal (x ~ y)
data = [(2, 2.1), (3, 2.9), (4, 4.2), (5, 4.8), (6, 6.1), (1, 1.1)]

n = len(data)
mx = sum(p[0] for p in data) / n
my = sum(p[1] for p in data) / n
centered = [(x - mx, y - my) for x, y in data]      # center

# Covariance matrix [[a, b], [b, d]] (population)
a = sum(x * x for x, y in centered) / n
d = sum(y * y for x, y in centered) / n
b = sum(x * y for x, y in centered) / n

# Eigenvalues of a symmetric 2x2 matrix
tr, det = a + d, a * d - b * b
disc = math.sqrt((tr / 2) ** 2 - det)
l1, l2 = tr / 2 + disc, tr / 2 - disc

# Top eigenvector (principal component) for l1: v = (b, l1 - a), normalized
vx, vy = b, l1 - a
norm = math.hypot(vx, vy)
pc1 = (vx / norm, vy / norm)
print("PC1 direction:", tuple(round(v, 3) for v in pc1))   # ~(0.707, 0.707)
print("explained variance ratio:", round(l1 / (l1 + l2), 4))

# Project the centered points onto PC1 (the 1-D compressed coordinate)
proj = [round(x * pc1[0] + y * pc1[1], 3) for x, y in centered]
print("projected (1-D):", proj)
'''),
        ("Explained variance across components", r'''
# Suppose eigenvalues (variances) of components came out as:
eigenvalues = [4.0, 1.0, 0.4, 0.1]
total = sum(eigenvalues)

print("explained variance ratios:")
cumulative = 0.0
for i, ev in enumerate(eigenvalues, 1):
    ratio = ev / total
    cumulative += ratio
    print(f"  PC{i}: {ratio:.1%}  (cumulative {cumulative:.1%})")

# Keep enough components to reach 90% of the variance
keep = 0
cumulative = 0.0
for ev in eigenvalues:
    keep += 1
    cumulative += ev / total
    if cumulative >= 0.90:
        break
print(f"-> keep {keep} components to retain >=90% variance")
'''),
        ("PCA with scikit-learn", r'''
try:
    from sklearn.decomposition import PCA
    from sklearn.datasets import load_iris
    from sklearn.preprocessing import StandardScaler

    X, y = load_iris(return_X_y=True)
    X_scaled = StandardScaler().fit_transform(X)    # scale before PCA

    pca = PCA(n_components=2).fit(X_scaled)
    X_2d = pca.transform(X_scaled)
    print("original shape:", X.shape, "-> reduced:", X_2d.shape)
    print("explained variance ratio:", pca.explained_variance_ratio_.round(3).tolist())
    print("total kept:", round(pca.explained_variance_ratio_.sum(), 3))
    print("first point in 2-D:", X_2d[0].round(3).tolist())
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "Always standardize features first — PCA chases variance, so large-scale features dominate.",
        "PCA components are linear combinations — they lose direct interpretability.",
        "It only captures LINEAR structure; use t-SNE/UMAP/kernel PCA for non-linear manifolds.",
        "Don't fit PCA on test data — fit on train, then transform test with the same components.",
        "Reducing too aggressively discards useful signal; check cumulative explained variance.",
    ],
    "exercises": [
        ("Center the data [2,4,6] (subtract the mean).", "x - mean.",
         r'''d = [2, 4, 6]
m = sum(d) / len(d)
print([x - m for x in d])  # [-2.0, 0.0, 2.0]'''),
        ("Compute the variance of centered [-2,0,2].", "Mean of squares.",
         r'''c = [-2, 0, 2]
print(sum(x ** 2 for x in c) / len(c))  # 2.666...'''),
        ("Explained variance ratio for eigenvalues [3,1].", "ev/total.",
         r'''ev = [3, 1]
print(ev[0] / sum(ev))  # 0.75'''),
        ("How many components to keep 90% with ratios [0.8,0.15,0.05]?", "Cumulate.",
         r'''ratios = [0.8, 0.15, 0.05]
c = 0; n = 0
for r in ratios:
    n += 1; c += r
    if c >= 0.9: break
print(n)  # 2'''),
        ("Why standardize before PCA?", "Variance fairness.",
         r'''#md
PCA maximizes variance, so a feature measured in large units (e.g. salary) would
dominate the components purely due to scale. **Standardizing** gives each feature
equal footing.'''),
        ("Project point (1,1) onto direction (0.707,0.707).", "Dot product.",
         r'''print(round(1 * 0.707 + 1 * 0.707, 3))  # 1.414'''),
        ("Trace (sum of variances) of covariance [[4,0],[0,1]].", "a + d.",
         r'''print(4 + 1)  # 5'''),
        ("Is PCA supervised or unsupervised?", "Uses labels?",
         r'''#md
**Unsupervised** — PCA uses only the feature matrix X (its variance/covariance
structure); it never looks at labels y.'''),
    ],
}

CONTENT["dimensionality-reduction"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**Dimensionality reduction** compresses many features into fewer while preserving "
        "structure. **PCA** does this linearly (max variance). **t-SNE** and **UMAP** are non-linear "
        "techniques tuned for **visualization**: they place similar points near each other in 2-D/"
        "3-D, revealing clusters. Simpler approaches include **feature selection** (drop "
        "low-variance or redundant features)."
    ),
    "why": (
        "Fewer dimensions mean faster training, less overfitting, smaller storage, and — crucially — "
        "the ability to SEE high-dimensional data in a 2-D scatter, which is invaluable for "
        "understanding clusters and class separation."
    ),
    "concepts": [
        ("Curse of dimensionality", "Distances blur and data sparsifies as dimensions grow."),
        ("Feature selection", "Keep a subset of original features (e.g. by variance)."),
        ("Feature extraction", "Build new combined features (PCA components)."),
        ("t-SNE / UMAP", "Non-linear methods that preserve local neighborhoods for plots."),
        ("Linear vs non-linear", "PCA = linear; t-SNE/UMAP capture curved manifolds."),
        ("For viz, not modeling", "t-SNE coordinates aren't meant as model features."),
    ],
    "examples": [
        ("Variance-threshold feature selection (pure Python)", r'''
import statistics as st

# 4 features across 5 samples; feature 2 (index 2) barely varies
samples = [
    [1.0, 5.0, 3.0, 100],
    [2.0, 6.0, 3.0, 220],
    [3.0, 4.0, 3.0, 150],
    [4.0, 7.0, 3.1, 300],
    [5.0, 5.0, 3.0, 180],
]
cols = list(zip(*samples))
variances = [st.pvariance(c) for c in cols]
print("variances:", [round(v, 3) for v in variances])

threshold = 0.1
keep = [i for i, v in enumerate(variances) if v > threshold]
print("keep feature indices:", keep)       # drops the near-constant feature 2
reduced = [[row[i] for i in keep] for row in samples]
print("reduced first row:", reduced[0])
'''),
        ("Simple linear projection to fewer dimensions", r'''
# Keep the two highest-variance features as a crude 4-D -> 2-D reduction
import statistics as st

samples = [[1, 9, 2, 8], [2, 1, 2, 7], [3, 8, 2, 9], [4, 2, 2, 6]]
cols = list(zip(*samples))
variances = [(i, st.pvariance(c)) for i, c in enumerate(cols)]
top2 = [i for i, _ in sorted(variances, key=lambda t: -t[1])[:2]]
print("top-2 variance feature indices:", sorted(top2))

projected = [[row[i] for i in sorted(top2)] for row in samples]
print("projected to 2-D:")
for p in projected:
    print(" ", p)
'''),
        ("t-SNE and PCA with scikit-learn", r'''
try:
    from sklearn.datasets import load_digits
    from sklearn.decomposition import PCA
    from sklearn.manifold import TSNE

    X, y = load_digits(return_X_y=True)       # 64-dimensional (8x8 images)
    print("original dimensions:", X.shape[1])

    # PCA: fast linear reduction to 2-D
    X_pca = PCA(n_components=2, random_state=0).fit_transform(X)
    print("PCA 2-D first point:", X_pca[0].round(2).tolist())

    # t-SNE: slower, non-linear, great for visualization (subset for speed)
    X_tsne = TSNE(n_components=2, perplexity=30,
                  init="pca", random_state=0).fit_transform(X[:300])
    print("t-SNE 2-D first point:", X_tsne[0].round(2).tolist())
    print("reduced to 2-D for plotting clusters of digits 0-9")
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "t-SNE is for VISUALIZATION — don't feed its 2-D output into a model as features.",
        "t-SNE distances/cluster sizes aren't meaningful globally; only local neighborhoods are.",
        "t-SNE is sensitive to 'perplexity' and random seed — try a few settings.",
        "Reduce after scaling, and fit the reducer on train only to avoid leakage.",
        "Aggressive reduction can destroy signal — validate that downstream accuracy holds.",
    ],
    "exercises": [
        ("Compute the variance of each column of [[1,3],[2,3],[3,3]].", "Per-column.",
         r'''import statistics as st
cols = list(zip(*[[1, 3], [2, 3], [3, 3]]))
print([st.pvariance(c) for c in cols])  # [0.66.., 0.0]'''),
        ("Drop columns with zero variance from that data.", "Keep var>0.",
         r'''import statistics as st
data = [[1, 3], [2, 3], [3, 3]]
cols = list(zip(*data))
keep = [i for i, c in enumerate(cols) if st.pvariance(c) > 0]
print(keep)  # [0]'''),
        ("Why is high dimensionality a problem (one line)?", "Curse.",
         r'''#md
The **curse of dimensionality**: as features grow, data becomes sparse and
distances between points become similar, so models need exponentially more data and
distance-based methods degrade.'''),
        ("Is t-SNE output suitable as model features?", "Viz only.",
         r'''#md
**No** — t-SNE is for **visualization** only. Its coordinates are non-deterministic
and don't preserve global structure, so they shouldn't be used as model inputs.'''),
        ("Pick the 2 highest-variance feature indices given vars [0.1,5,0.2,3].", "Sort desc.",
         r'''vars = [0.1, 5, 0.2, 3]
idx = sorted(range(4), key=lambda i: -vars[i])[:2]
print(sorted(idx))  # [1, 3]'''),
        ("PCA vs t-SNE: which is linear?", "Recall definitions.",
         r'''#md
**PCA** is linear (projection onto variance-maximizing axes). **t-SNE** is
non-linear, modeling local neighborhood probabilities.'''),
        ("Reduce [5,2,9,1] keeping the 2 largest values' positions.", "Top-2 indices.",
         r'''vals = [5, 2, 9, 1]
print(sorted(sorted(range(4), key=lambda i: -vals[i])[:2]))  # [0, 2]'''),
        ("Name one benefit of dimensionality reduction.", "Any valid.",
         r'''#md
Any of: faster training, less overfitting, lower storage, removing redundant/
correlated features, or enabling 2-D **visualization** of the data.'''),
    ],
}

CONTENT["classification-metrics"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**Classification metrics** judge how well a classifier labels data. From the **confusion "
        "matrix** (TP, FP, TN, FN) come **accuracy** (overall correct), **precision** (of predicted "
        "positives, how many are right), **recall/sensitivity** (of actual positives, how many were "
        "caught), and **F1** (their harmonic mean). **ROC-AUC** summarizes the precision/recall "
        "trade-off across thresholds."
    ),
    "why": (
        "Accuracy alone lies on imbalanced data (99% accuracy by always predicting the majority). "
        "Precision vs recall captures the cost of false positives vs false negatives — central to "
        "medical, fraud, and safety decisions."
    ),
    "concepts": [
        ("Confusion matrix", "Counts of TP, FP, TN, FN."),
        ("Accuracy", "(TP+TN)/all — fraction correct."),
        ("Precision", "TP/(TP+FP) — correctness of positive predictions."),
        ("Recall", "TP/(TP+FN) — coverage of actual positives."),
        ("F1 score", "Harmonic mean of precision and recall."),
        ("ROC-AUC", "Ranking quality across all thresholds (0.5 = random, 1 = perfect)."),
    ],
    "examples": [
        ("Confusion matrix and metrics from scratch", r'''
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
'''),
        ("Why accuracy misleads on imbalanced data", r'''
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
'''),
        ("Metrics with scikit-learn", r'''
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
'''),
    ],
    "gotchas": [
        "Accuracy is misleading on imbalanced classes — a constant predictor can score high.",
        "Precision and recall trade off; lowering the threshold raises recall but lowers precision.",
        "F1 balances precision/recall but ignores true negatives — not always what you want.",
        "Pick the metric by cost: false negatives in cancer screening matter more than false positives.",
        "ROC-AUC needs scores/probabilities, not hard labels; PR-AUC is better for heavy imbalance.",
    ],
    "exercises": [
        ("Compute accuracy: 8 correct of 10.", "correct/total.",
         r'''print(8 / 10)  # 0.8'''),
        ("Compute precision with TP=5, FP=5.", "TP/(TP+FP).",
         r'''print(5 / (5 + 5))  # 0.5'''),
        ("Compute recall with TP=5, FN=15.", "TP/(TP+FN).",
         r'''print(5 / (5 + 15))  # 0.25'''),
        ("Compute F1 with precision=0.5, recall=0.25.", "Harmonic mean.",
         r'''p, r = 0.5, 0.25
print(round(2 * p * r / (p + r), 3))  # 0.333'''),
        ("Count TP in true=[1,0,1], pred=[1,1,1].", "Both 1.",
         r'''t, p = [1, 0, 1], [1, 1, 1]
print(sum(1 for a, b in zip(t, p) if a == 1 and b == 1))  # 2'''),
        ("Why is accuracy bad for 99% negative data?", "Majority predictor.",
         r'''#md
Always predicting the majority class scores **99% accuracy** while catching **none**
of the rare positives. Accuracy hides this failure — precision/recall expose it.'''),
        ("Which metric matters most for cancer screening?", "Cost of FN.",
         r'''#md
**Recall (sensitivity)** — missing a real case (false negative) is dangerous, so you
want to catch as many true positives as possible, even at some precision cost.'''),
        ("What ROC-AUC value means random guessing?", "Baseline.",
         r'''#md
**0.5** — equivalent to a coin flip. 1.0 is a perfect ranker; below 0.5 is worse
than random (predictions inverted).'''),
    ],
}

CONTENT["regression-metrics"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**Regression metrics** measure how far predictions fall from continuous targets. **MAE** "
        "(mean absolute error) averages |error|; **MSE** averages squared error (punishing big "
        "misses); **RMSE** is its square root (same units as the target); **R²** reports the "
        "fraction of variance explained (1 = perfect, 0 = no better than the mean, negative = "
        "worse)."
    ),
    "why": (
        "Choosing the right error metric shapes what the model optimizes and how you judge it. RMSE "
        "vs MAE encodes how much you care about large errors; R² gives an intuitive 'how much "
        "variance is explained' score for stakeholders."
    ),
    "concepts": [
        ("MAE", "Average absolute error; robust, same units as target."),
        ("MSE", "Average squared error; penalizes large errors heavily."),
        ("RMSE", "√MSE; interpretable in the target's units."),
        ("R²", "1 − SS_res/SS_tot; variance explained."),
        ("MAPE", "Mean absolute PERCENTAGE error; scale-free but breaks near zero."),
        ("Metric choice", "Outliers → MAE; penalize big misses → RMSE."),
    ],
    "examples": [
        ("MAE, MSE, RMSE, R² from scratch", r'''
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
'''),
        ("Why RMSE punishes outliers more than MAE", r'''
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
'''),
        ("Regression metrics with scikit-learn", r'''
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
'''),
    ],
    "gotchas": [
        "RMSE and MSE are dominated by outliers; use MAE if large errors shouldn't be over-weighted.",
        "R² can be NEGATIVE when the model is worse than predicting the mean.",
        "A high R² doesn't mean the model is good or causal — check residuals and context.",
        "MAPE explodes when true values are near zero — avoid it for targets that cross 0.",
        "Compare RMSE only on the same target scale; it's not comparable across different units.",
    ],
    "exercises": [
        ("Compute MAE for preds [2,4] vs truth [3,5].", "Mean abs error.",
         r'''t, p = [3, 5], [2, 4]
print(sum(abs(a - b) for a, b in zip(t, p)) / len(t))  # 1.0'''),
        ("Compute MSE for the same.", "Mean sq error.",
         r'''t, p = [3, 5], [2, 4]
print(sum((a - b) ** 2 for a, b in zip(t, p)) / len(t))  # 1.0'''),
        ("Compute RMSE when MSE=9.", "sqrt.",
         r'''print(9 ** 0.5)  # 3.0'''),
        ("Compute R^2 when SS_res=2, SS_tot=8.", "1 - res/tot.",
         r'''print(1 - 2 / 8)  # 0.75'''),
        ("Which metric is most robust to outliers?", "Linear penalty.",
         r'''#md
**MAE** — it weights errors linearly, so a single huge error doesn't dominate like
it does in MSE/RMSE (which square the error).'''),
        ("What does a negative R^2 indicate?", "Worse than mean.",
         r'''#md
The model predicts **worse than simply using the mean** of the target. SS_res >
SS_tot, so 1 − SS_res/SS_tot < 0.'''),
        ("Compute MAPE for true=[100,200], pred=[110,180].", "Mean abs % error.",
         r'''t, p = [100, 200], [110, 180]
print(sum(abs(a - b) / a for a, b in zip(t, p)) / len(t))  # 0.1'''),
        ("Why prefer RMSE over MSE for reporting?", "Units.",
         r'''#md
**RMSE is in the same units as the target** (MSE is squared units), so it's directly
interpretable — e.g. 'off by ~3 dollars' rather than '9 dollars-squared'.'''),
    ],
}

CONTENT["hyperparameter-tuning"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**Hyperparameters** are settings you choose BEFORE training (e.g. k in KNN, tree depth, "
        "learning rate, regularization strength) — distinct from parameters the model learns. "
        "**Tuning** searches for the combination that generalizes best, evaluated with "
        "**cross-validation**. Strategies: **grid search** (try every combo), **random search** "
        "(sample combos), and smarter Bayesian optimization."
    ),
    "why": (
        "The right hyperparameters can be the difference between a mediocre and a great model. "
        "Systematic tuning with proper validation prevents both underfitting and overfitting and is "
        "a standard step in any serious ML pipeline."
    ),
    "concepts": [
        ("Hyperparameter", "Set before training (k, depth, lr); not learned from data."),
        ("Grid search", "Exhaustively try all combinations in a grid."),
        ("Random search", "Sample random combinations — efficient for big spaces."),
        ("Validation score", "Use CV, not the test set, to compare settings."),
        ("Search space", "The ranges/values of each hyperparameter to try."),
        ("Overfitting the search", "Tuning too hard on validation leaks — keep a final test set."),
    ],
    "examples": [
        ("Grid search from scratch (tune k for KNN)", r'''
import math
from collections import Counter

train = [((1,), "A"), ((2,), "A"), ((3,), "A"),
         ((6,), "B"), ((7,), "B"), ((8,), "B")]
val =   [((2.5,), "A"), ((6.5,), "B"), ((1.5,), "A"), ((7.5,), "B")]

def knn_predict(x, k):
    nearest = sorted(train, key=lambda it: abs(x[0] - it[0][0]))[:k]
    return Counter(lab for _, lab in nearest).most_common(1)[0][0]

def accuracy(k):
    correct = sum(1 for x, y in val if knn_predict(x, k) == y)
    return correct / len(val)

# Grid search over candidate k values
best_k, best_acc = None, -1
for k in [1, 2, 3, 4, 5]:
    acc = accuracy(k)
    print(f"k={k}: validation accuracy = {acc:.2f}")
    if acc > best_acc:
        best_k, best_acc = k, acc
print(f"-> best k = {best_k} (acc {best_acc:.2f})")
'''),
        ("Grid vs random search size", r'''
import random
random.seed(0)

# A 2-hyperparameter grid
learning_rates = [0.001, 0.01, 0.1, 1.0]
depths = [2, 3, 5, 10]

grid = [(lr, d) for lr in learning_rates for d in depths]
print("grid search tries:", len(grid), "combinations")   # 4*4 = 16

# Random search: sample a few combos instead of all
random_combos = [(random.choice(learning_rates), random.choice(depths))
                 for _ in range(5)]
print("random search tries:", len(random_combos), "->", random_combos)
print("Random search scales better when there are many hyperparameters.")
'''),
        ("GridSearchCV with scikit-learn", r'''
try:
    from sklearn.model_selection import GridSearchCV
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.datasets import load_iris

    X, y = load_iris(return_X_y=True)
    param_grid = {"n_estimators": [10, 50], "max_depth": [2, 3, None]}

    search = GridSearchCV(RandomForestClassifier(random_state=0),
                          param_grid, cv=5)
    search.fit(X, y)
    print("best params:", search.best_params_)
    print("best CV score:", round(search.best_score_, 3))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "Tune using cross-validation, never the final test set — that leaks and inflates results.",
        "Grid search explodes combinatorially; random/Bayesian search scales to many hyperparameters.",
        "Scale features when tuning distance/gradient models, or the search chases artifacts.",
        "Re-fit preprocessing inside CV folds (use pipelines) so each fold is independent.",
        "After choosing hyperparameters, evaluate ONCE on the held-out test set for an honest number.",
    ],
    "exercises": [
        ("Is tree max_depth a parameter or hyperparameter?", "Set before training.",
         r'''#md
A **hyperparameter** — you set it before training. The split thresholds the tree
learns from data are its parameters.'''),
        ("How many combos in a 3x4 grid?", "Multiply.",
         r'''print(3 * 4)  # 12'''),
        ("Pick the best k by accuracy {1:0.6,3:0.8,5:0.7}.", "Max by value.",
         r'''scores = {1: 0.6, 3: 0.8, 5: 0.7}
print(max(scores, key=scores.get))  # 3'''),
        ("Why not tune on the test set?", "Leakage.",
         r'''#md
Tuning on the test set **leaks** its information into model selection, so the test
score no longer reflects true generalization. Use cross-validation for tuning and
reserve the test set for one final evaluation.'''),
        ("Grid has 5 lrs and 4 depths and 3-fold CV: how many fits?", "lr*depth*folds.",
         r'''print(5 * 4 * 3)  # 60'''),
        ("When does random search beat grid search?", "Many params.",
         r'''#md
When the search space is **large/high-dimensional**. Random search samples the space
more efficiently and often finds good configs with far fewer trials than exhaustive
grid search.'''),
        ("Sample one random (lr, depth) from lrs [0.1,1], depths [2,5] with seed 0.", "random.choice.",
         r'''import random
random.seed(0)
print((random.choice([0.1, 1]), random.choice([2, 5])))'''),
        ("After tuning, how many times evaluate on the test set?", "Once.",
         r'''#md
**Exactly once**, at the very end, to get an unbiased estimate of generalization.
Repeated peeking turns the test set into a validation set.'''),
    ],
}

CONTENT["regularization"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**Regularization** discourages overly complex models by adding a penalty on the size of the "
        "weights to the loss. **L2 (Ridge)** penalizes the sum of squared weights — shrinking them "
        "smoothly toward zero. **L1 (Lasso)** penalizes the sum of absolute weights — driving some "
        "exactly to zero (automatic **feature selection**). A strength **λ (alpha)** controls how "
        "hard you penalize."
    ),
    "why": (
        "Regularization is the primary cure for overfitting in linear models and neural networks. "
        "L1 also yields sparse, interpretable models by zeroing out useless features. It's everywhere "
        "— Ridge/Lasso, weight decay, dropout."
    ),
    "concepts": [
        ("Penalty term", "Added to the loss to punish large weights."),
        ("L2 / Ridge", "Σwᵢ² penalty; shrinks weights smoothly, keeps all features."),
        ("L1 / Lasso", "Σ|wᵢ| penalty; zeros out some weights → sparsity."),
        ("Lambda / alpha", "Regularization strength; bigger = simpler model."),
        ("Bias-variance", "Regularization adds bias to cut variance/overfitting."),
        ("Elastic Net", "Combines L1 and L2 penalties."),
    ],
    "examples": [
        ("L2 regularization shrinks weights (gradient descent)", r'''
# Target depends only on feature 1; feature 2 is irrelevant noise.
data = [([1, 2], 2.0), ([2, 1], 4.0), ([3, 0], 6.0),
        ([4, 3], 8.0), ([5, 1], 10.0)]

def train(lam, epochs=2000, lr=0.01):
    w = [0.0, 0.0]
    for _ in range(epochs):
        gw = [0.0, 0.0]
        for x, y in data:
            pred = w[0] * x[0] + w[1] * x[1]
            err = pred - y
            for j in range(2):
                gw[j] += 2 * err * x[j]
        # add the L2 penalty gradient: d/dw (lam * w^2) = 2*lam*w
        for j in range(2):
            gw[j] = gw[j] / len(data) + 2 * lam * w[j]
            w[j] -= lr * gw[j]
    return w

for lam in [0.0, 0.1, 1.0, 5.0]:
    w = train(lam)
    print(f"lambda={lam:4}: weights = [{w[0]:.3f}, {w[1]:.3f}]")
# As lambda grows, BOTH weights shrink toward 0 (especially the noise feature).
'''),
        ("L1 vs L2: sparsity via soft-thresholding", r'''
# L1's effect on a single weight is 'soft-thresholding': small weights -> 0.
def soft_threshold(w, lam):
    if w > lam:   return w - lam
    if w < -lam:  return w + lam
    return 0.0                       # |w| <= lam gets zeroed (sparsity!)

for w in [-2.0, -0.3, 0.0, 0.4, 1.5]:
    print(f"w={w:5} -> L1(lam=0.5) -> {soft_threshold(w, 0.5)}")
print("Small weights snap to exactly 0 -> L1 selects features.")
print("L2 would only shrink them proportionally, never exactly to 0.")
'''),
        ("Ridge and Lasso with scikit-learn", r'''
try:
    from sklearn.linear_model import Ridge, Lasso, LinearRegression
    from sklearn.datasets import make_regression

    X, y = make_regression(n_samples=80, n_features=8, n_informative=3,
                           noise=10, random_state=0)

    lr = LinearRegression().fit(X, y)
    ridge = Ridge(alpha=10).fit(X, y)
    lasso = Lasso(alpha=10).fit(X, y)

    print("plain coef (abs sum):", round(sum(abs(c) for c in lr.coef_), 1))
    print("ridge coef (abs sum):", round(sum(abs(c) for c in ridge.coef_), 1))
    print("lasso zeros          :", int(sum(1 for c in lasso.coef_ if abs(c) < 1e-6)),
          "of", len(lasso.coef_), "features set to 0")
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "Standardize features first — penalties depend on weight scale, so unscaled features are penalized unfairly.",
        "Too much regularization (huge λ) underfits — weights shrink so much the model ignores signal.",
        "L1 yields sparsity (feature selection); L2 keeps all features but small — pick by goal.",
        "Don't usually regularize the bias/intercept term.",
        "λ is a hyperparameter — tune it with cross-validation, don't guess.",
    ],
    "exercises": [
        ("Compute the L2 penalty Σw² for w=[3,4].", "Sum of squares.",
         r'''w = [3, 4]
print(sum(wi ** 2 for wi in w))  # 25'''),
        ("Compute the L1 penalty Σ|w| for w=[-3,4].", "Sum of abs.",
         r'''w = [-3, 4]
print(sum(abs(wi) for wi in w))  # 7'''),
        ("Soft-threshold w=0.3 with lambda=0.5.", "Within band -> 0.",
         r'''def st(w, lam):
    return w - lam if w > lam else (w + lam if w < -lam else 0.0)
print(st(0.3, 0.5))  # 0.0'''),
        ("Which penalty produces sparse models?", "Zeros weights.",
         r'''#md
**L1 (Lasso)** — its constant-magnitude gradient drives small weights exactly to
**zero**, performing automatic feature selection. L2 only shrinks them.'''),
        ("As lambda increases, do weights grow or shrink?", "Penalty effect.",
         r'''#md
**Shrink** toward zero — a larger penalty makes large weights more costly, producing
a simpler, more biased (but lower-variance) model.'''),
        ("Add L2 gradient 2*lambda*w for lambda=0.5, w=4.", "Compute.",
         r'''print(2 * 0.5 * 4)  # 4.0'''),
        ("Why standardize before regularizing?", "Fair penalty.",
         r'''#md
The penalty acts on weight magnitudes, which depend on feature scale. Without
standardizing, features with small ranges get large weights and are penalized
disproportionately. Scaling makes the penalty fair across features.'''),
        ("What does Elastic Net combine?", "L1 + L2.",
         r'''#md
**Both L1 and L2** penalties — getting Lasso's sparsity plus Ridge's stability
(handles correlated features better than pure L1).'''),
    ],
}

CONTENT["ensemble-methods"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**Ensemble methods** combine multiple models into one stronger predictor. **Voting/"
        "averaging** blends diverse models (hard vote = majority label, soft vote = average "
        "probabilities). **Bagging** trains the same model on bootstrap samples to cut variance "
        "(random forests). **Boosting** trains models sequentially to fix errors and cut bias "
        "(gradient boosting). **Stacking** trains a meta-model on base models' outputs."
    ),
    "why": (
        "Ensembles almost always beat single models — they win Kaggle competitions and power "
        "production systems — by exploiting model diversity so individual errors cancel out. "
        "Understanding the four patterns lets you mix models effectively."
    ),
    "concepts": [
        ("Voting", "Combine different models: majority (hard) or averaged probs (soft)."),
        ("Bagging", "Same model on bootstrap samples; reduces variance."),
        ("Boosting", "Sequential models that fix predecessors; reduces bias."),
        ("Stacking", "A meta-model learns to combine base models' predictions."),
        ("Diversity", "Ensembles help most when members make different errors."),
        ("Wisdom of crowds", "Averaging many decent, diverse models beats one."),
    ],
    "examples": [
        ("Hard voting from scratch", r'''
from collections import Counter

# Three simple 'models' each return a class label for an input.
def model_a(x): return "spam" if x > 5 else "ham"
def model_b(x): return "spam" if x > 3 else "ham"
def model_c(x): return "spam" if x > 7 else "ham"

def hard_vote(x):
    votes = [model_a(x), model_b(x), model_c(x)]
    return Counter(votes).most_common(1)[0][0], votes

for x in [2, 6, 8]:
    decision, votes = hard_vote(x)
    print(f"x={x}: votes={votes} -> {decision}")
'''),
        ("Soft voting (average probabilities)", r'''
# Each model outputs P(class=1). Soft voting averages them.
def model_a(x): return min(1.0, x / 10)        # probability-like score
def model_b(x): return min(1.0, x / 8)
def model_c(x): return min(1.0, (x - 1) / 9)

def soft_vote(x, threshold=0.5):
    probs = [model_a(x), model_b(x), model_c(x)]
    avg = sum(probs) / len(probs)
    label = 1 if avg >= threshold else 0
    return label, round(avg, 3), [round(p, 2) for p in probs]

for x in [3, 5, 8]:
    label, avg, probs = soft_vote(x)
    print(f"x={x}: probs={probs}, avg={avg} -> class {label}")
'''),
        ("Voting and Stacking with scikit-learn", r'''
try:
    from sklearn.ensemble import VotingClassifier, StackingClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.datasets import load_iris
    from sklearn.model_selection import cross_val_score

    X, y = load_iris(return_X_y=True)
    estimators = [
        ("lr", LogisticRegression(max_iter=1000)),
        ("dt", DecisionTreeClassifier(max_depth=3, random_state=0)),
        ("knn", KNeighborsClassifier()),
    ]
    voting = VotingClassifier(estimators, voting="hard")
    print("voting CV acc :", round(cross_val_score(voting, X, y, cv=5).mean(), 3))

    stacking = StackingClassifier(estimators,
                                  final_estimator=LogisticRegression(max_iter=1000))
    print("stacking CV acc:", round(cross_val_score(stacking, X, y, cv=5).mean(), 3))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "Ensembles help only if members are DIVERSE — combining identical models gains nothing.",
        "Soft voting needs well-calibrated probabilities; otherwise hard voting can be safer.",
        "Stacking can overfit if the meta-model sees the same data base models trained on — use CV folds.",
        "Ensembles cost more compute/memory and are harder to interpret and deploy.",
        "A bad model can drag down a vote — weight or drop weak members.",
    ],
    "exercises": [
        ("Majority-vote the labels ['spam','ham','spam'].", "Counter.",
         r'''from collections import Counter
print(Counter(["spam", "ham", "spam"]).most_common(1)[0][0])  # spam'''),
        ("Average the probabilities [0.6,0.8,0.4] and threshold at 0.5.", "Mean + compare.",
         r'''probs = [0.6, 0.8, 0.4]
avg = sum(probs) / len(probs)
print(avg, 1 if avg >= 0.5 else 0)  # 0.6 1'''),
        ("Which ensemble reduces variance: bagging or boosting?", "Recall.",
         r'''#md
**Bagging** reduces variance (averaging independent models). Boosting primarily
reduces **bias** by sequentially correcting errors.'''),
        ("Which reduces bias: bagging or boosting?", "Recall.",
         r'''#md
**Boosting** — each model focuses on the previous models' mistakes, reducing bias
(at some risk of higher variance/overfitting).'''),
        ("What does a stacking meta-model take as input?", "Base predictions.",
         r'''#md
The **predictions (outputs) of the base models** — the meta-model learns how best to
combine them into a final prediction.'''),
        ("Why must ensemble members be diverse?", "Errors cancel.",
         r'''#md
If models make **different errors**, averaging/voting cancels them out. Identical
models make identical mistakes, so combining them adds nothing.'''),
        ("Tie-break a vote ['A','B'] — what's a simple rule?", "Any deterministic rule.",
         r'''#md
Use a deterministic tie-break: e.g. pick the class with higher prior, the
alphabetically first label, or fall back to the single most accurate base model.'''),
        ("3 models with 70% accuracy and independent errors: is the vote usually higher?", "Wisdom of crowds.",
         r'''#md
**Yes** — if their errors are independent, majority voting corrects cases where only
one model is wrong, pushing combined accuracy **above 70%** (wisdom of crowds).'''),
    ],
}

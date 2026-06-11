# ======================================================================
# 78 — Naive Bayes  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: Gaussian Naive Bayes from scratch
# ----------------------------------------------------------------------
print("\n--- Example 1: Gaussian Naive Bayes from scratch ---")
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

# ----------------------------------------------------------------------
# Example 2: Multinomial Naive Bayes for spam (text)
# ----------------------------------------------------------------------
print("\n--- Example 2: Multinomial Naive Bayes for spam (text) ---")
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

# ----------------------------------------------------------------------
# Example 3: Naive Bayes with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: Naive Bayes with scikit-learn ---")
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

print("\nDone! Tip: change values above and run again to learn by experiment.")

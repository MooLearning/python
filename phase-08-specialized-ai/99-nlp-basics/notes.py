# ======================================================================
# 99 — NLP Basics  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: scikit-learn
# Install:  pip install scikit-learn

# ----------------------------------------------------------------------
# Example 1: Tokenize, normalize, remove stopwords
# ----------------------------------------------------------------------
print("\n--- Example 1: Tokenize, normalize, remove stopwords ---")
import re

text = "The quick brown Fox jumps over the LAZY dog!"
stopwords = {"the", "over", "a", "an", "is", "of"}

# lowercase + keep only word characters
tokens = re.findall(r"[a-z]+", text.lower())
print("tokens   :", tokens)

filtered = [t for t in tokens if t not in stopwords]
print("no stops :", filtered)

# A naive stemmer: chop common suffixes
def stem(word):
    for suf in ("ing", "ed", "s"):
        if word.endswith(suf) and len(word) - len(suf) >= 3:
            return word[:-len(suf)]
    return word
print("stemmed  :", [stem(t) for t in filtered])

# ----------------------------------------------------------------------
# Example 2: Bag-of-words and TF-IDF from scratch
# ----------------------------------------------------------------------
print("\n--- Example 2: Bag-of-words and TF-IDF from scratch ---")
import math

docs = ["the cat sat", "the dog sat", "the cat ran fast"]
tokenized = [d.split() for d in docs]
vocab = sorted({w for doc in tokenized for w in doc})
print("vocab:", vocab)

# Bag-of-words: count vector per document
print("\nbag-of-words:")
for doc in tokenized:
    print(" ", {w: doc.count(w) for w in vocab if doc.count(w)})

# TF-IDF: rare-but-present words score highest
def tf(w, doc):  return doc.count(w) / len(doc)
def idf(w):
    containing = sum(1 for doc in tokenized if w in doc)
    return math.log(len(docs) / (1 + containing)) + 1

print("\nTF-IDF for doc 0 ('the cat sat'):")
for w in tokenized[0]:
    print(f"  {w:5}: {tf(w, tokenized[0]) * idf(w):.3f}")
# 'the' appears everywhere -> low idf -> low weight; 'cat'/'sat' score higher.

# ----------------------------------------------------------------------
# Example 3: n-grams and vectorizing with scikit-learn
# ----------------------------------------------------------------------
print("\n--- Example 3: n-grams and vectorizing with scikit-learn ---")
text = "machine learning is fun".split()

# Bigrams (pairs of consecutive words)
bigrams = list(zip(text, text[1:]))
print("bigrams:", bigrams)

try:
    from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
    docs = ["the cat sat", "the dog sat", "the cat ran"]

    cv = CountVectorizer()
    counts = cv.fit_transform(docs)
    print("\nvocabulary:", cv.get_feature_names_out().tolist())
    print("count matrix:\n", counts.toarray())

    tfidf = TfidfVectorizer()
    print("\nTF-IDF matrix (rounded):\n", tfidf.fit_transform(docs).toarray().round(2))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")

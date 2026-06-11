# 99 — NLP Basics

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Natural Language Processing (NLP)** turns text into something models can use. The basic pipeline: **tokenize** (split into words), **normalize** (lowercase, remove punctuation/**stopwords**, optionally **stem/lemmatize**), then **vectorize** — **bag-of-words** (counts) or **TF-IDF** (weighting words by how distinctive they are). **n-grams** capture short word sequences.

## Why it matters

Text is unstructured; these steps convert it to numbers for classification, search, and clustering. TF-IDF and bag-of-words still power strong baselines, and tokenization concepts carry straight into transformers and LLMs.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install scikit-learn
```

## Key concepts

- **Tokenization** — Split text into tokens (words/subwords).
- **Normalization** — Lowercase, strip punctuation, remove stopwords.
- **Stemming/lemmatization** — Reduce words to a root form (running→run).
- **Bag-of-words** — Represent a doc by word counts, ignoring order.
- **TF-IDF** — Weight = term frequency × inverse document frequency.
- **n-grams** — Contiguous word sequences (bigrams, trigrams) for context.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Tokenizing on spaces alone mishandles punctuation/contractions — use regex or a real tokenizer.
- ⚠️ Removing stopwords can hurt tasks where they matter (sentiment, negation).
- ⚠️ Bag-of-words ignores word ORDER — 'dog bites man' == 'man bites dog'.
- ⚠️ TF-IDF vectors are sparse and high-dimensional; store them sparsely.
- ⚠️ Stemming is crude (can mangle words); lemmatization is more accurate but needs a dictionary.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


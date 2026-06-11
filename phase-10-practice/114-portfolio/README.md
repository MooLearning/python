# 114 — Portfolio

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **portfolio** is your public proof of skill: a small set of well-documented projects (usually on GitHub) plus clear write-ups. For ML, strong portfolios show the **whole process** — problem framing, EDA, modeling decisions, evaluation, and (ideally) a live demo — not just a final accuracy number. A great README and clean, reproducible code matter as much as the model.

## Why it matters

Hiring managers skim portfolios to see if you can deliver real, communicated work. A few polished, end-to-end projects beat dozens of half-finished notebooks and often matter more than a resume line.

## Key concepts

- **Quality over quantity** — 3–5 polished projects beat 20 sloppy ones.
- **Show the process** — EDA, decisions, trade-offs — not just the result.
- **Great README** — Problem, approach, results, how to run, demo link.
- **Reproducibility** — Anyone can clone and run it.
- **Live demo** — A Streamlit/HF Space app makes it tangible.
- **Range** — Cover different skills: viz, ML, DL, deployment.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
readme = """\
# Student Pass Predictor

Predicts whether a student passes based on study habits.
**Demo:** https://your-app.streamlit.app  |  **Accuracy:** 89% (held-out test)

## Problem
Given hours studied, sleep, and attendance, predict pass/fail so tutors can
flag at-risk students early.

## Data
1,200 anonymized records. See `data/README.md` for the schema and source.

## Approach
- EDA: study hours strongly correlate with passing (see notebooks/01-eda.ipynb)
- Model: logistic regression baseline -> gradient boosting (best CV)
- Validation: 5-fold cross-validation, accuracy + F1

## Results
| model               | CV accuracy |
|---------------------|-------------|
| baseline (majority) | 0.61        |
| logistic regression | 0.84        |
| gradient boosting   | 0.89        |

## Run it
```bash
pip install -r requirements.txt
python src/train.py
streamlit run app.py
```
"""
print(readme)
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Quality over quantity — a few polished projects beat many abandoned notebooks.
- ⚠️ A missing/weak README kills a good project; recruiters skim, so lead with results.
- ⚠️ If it isn't reproducible (no requirements, hard-coded paths), people can't run it.
- ⚠️ Don't just paste accuracy — explain the problem, decisions, and limitations.
- ⚠️ Avoid only toy datasets everyone uses; a unique/real dataset stands out.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


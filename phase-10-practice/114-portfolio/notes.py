# ======================================================================
# 114 — Portfolio  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: A README template that sells a project
# ----------------------------------------------------------------------
print("\n--- Example 1: A README template that sells a project ---")
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

# ----------------------------------------------------------------------
# Example 2: A portfolio project checklist
# ----------------------------------------------------------------------
print("\n--- Example 2: A portfolio project checklist ---")
checklist = [
    "Clear problem statement (why it matters)",
    "Clean, commented, reproducible code",
    "README with results table + how-to-run",
    "EDA and decisions shown, not hidden",
    "Honest evaluation on held-out data",
    "Pinned requirements.txt",
    "A live demo or screenshots/GIF",
    "Reflection: what worked, what you'd improve",
]
print("Make each project tick these boxes:")
for item in checklist:
    print("  [ ]", item)

score = sum(1 for _ in checklist)        # all 8 = portfolio-ready
print(f"\n{score}/8 -> a project that stands out")

# ----------------------------------------------------------------------
# Example 3: Suggested projects by skill level
# ----------------------------------------------------------------------
print("\n--- Example 3: Suggested projects by skill level ---")
projects = {
    "Beginner": [
        "Exploratory analysis of a public dataset (clear viz + insights)",
        "Classification (Titanic / Iris) with a clean pipeline",
    ],
    "Intermediate": [
        "End-to-end model with a Streamlit demo",
        "NLP sentiment analysis on real reviews",
        "Time-series forecast with proper backtesting",
    ],
    "Advanced": [
        "Fine-tune a transformer and deploy it",
        "Computer-vision app (detection/segmentation)",
        "Full MLOps: API + Docker + CI/CD + monitoring",
    ],
}
for level, ideas in projects.items():
    print(f"\n{level}:")
    for idea in ideas:
        print("  -", idea)

print("\nDone! Tip: change values above and run again to learn by experiment.")

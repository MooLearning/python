# -*- coding: utf-8 -*-
"""Phase 10 — Practice (DSA practice, Kaggle, end-to-end projects, portfolio).

Capstone phase: worked interview problems, a baseline Kaggle pipeline, a complete
mini ML project, and portfolio guidance — all pure-Python and runnable.
"""

CONTENT = {}

CONTENT["dsa-practice"] = {
    "what": (
        "**DSA practice** is the deliberate, repeated solving of data-structure and algorithm "
        "problems (LeetCode/HackerRank style) to build pattern recognition and interview fluency. "
        "The skill isn't memorizing solutions — it's recognizing which **pattern** a problem fits "
        "(two pointers, sliding window, hashing, BFS/DFS, DP) and reasoning about **time/space "
        "complexity** out loud."
    ),
    "why": (
        "Coding interviews at most companies are DSA-based, and the problem-solving muscle transfers "
        "to writing efficient real code. Consistent practice with reflection beats cramming."
    ),
    "concepts": [
        ("Pattern recognition", "Map a new problem to a known technique."),
        ("Brute force first", "Get a correct solution, THEN optimize."),
        ("Complexity analysis", "State time/space Big-O for every solution."),
        ("Edge cases", "Empty input, one element, duplicates, negatives."),
        ("Spaced repetition", "Re-solve missed problems after a few days."),
        ("Think aloud", "Communicate your approach — interviews test reasoning."),
    ],
    "examples": [
        ("A problem-solving framework on Two Sum", r'''
# Problem: return indices of two numbers that add up to target.
nums, target = [2, 7, 11, 15], 9

# Step 1 - BRUTE FORCE: check all pairs -> O(n^2)
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
print("brute force:", two_sum_brute(nums, target))

# Step 2 - OPTIMIZE with a hash map -> O(n)
def two_sum_fast(nums, target):
    seen = {}                          # value -> index
    for i, n in enumerate(nums):
        if target - n in seen:
            return (seen[target - n], i)
        seen[n] = i
print("optimized :", two_sum_fast(nums, target))
print("complexity: brute O(n^2) -> hashmap O(n) time, O(n) space")
'''),
        ("Recognizing patterns: window, two-pointer, hashing", r'''
# SLIDING WINDOW: max sum of k consecutive elements
def max_window(a, k):
    window = sum(a[:k]); best = window
    for i in range(k, len(a)):
        window += a[i] - a[i - k]
        best = max(best, window)
    return best
print("window  :", max_window([1, 4, 2, 10, 2, 3], 3))   # 16

# TWO POINTERS: pair summing to target in a sorted array
def pair_sum(a, t):
    i, j = 0, len(a) - 1
    while i < j:
        s = a[i] + a[j]
        if s == t: return (a[i], a[j])
        i, j = (i + 1, j) if s < t else (i, j - 1)
print("2-pointer:", pair_sum([1, 2, 4, 7, 11], 9))        # (2, 7)

# HASHING: first non-repeating character
from collections import Counter
def first_unique(s):
    c = Counter(s)
    return next((ch for ch in s if c[ch] == 1), None)
print("hashing :", first_unique("aabbcde"))               # c
'''),
        ("A study plan and worked complexity analysis", r'''
# Worked example: valid parentheses (stack) — O(n) time, O(n) space
def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif not stack or stack.pop() != pairs[ch]:
            return False
    return not stack

for test in ["()[]{}", "(]", "([{}])"]:
    print(f"{test:8} -> {is_valid(test)}")

print("\nSuggested 8-week plan (1-2 problems/day):")
plan = ["Arrays & Hashing", "Two Pointers & Sliding Window", "Stack & Queue",
        "Binary Search", "Linked Lists", "Trees & BFS/DFS",
        "Backtracking & Recursion", "Dynamic Programming"]
for week, topic in enumerate(plan, 1):
    print(f"  week {week}: {topic}")
'''),
    ],
    "gotchas": [
        "Don't memorize solutions — practice RECOGNIZING the pattern, or new problems stump you.",
        "Always analyze time/space complexity; a working but O(n²) answer may not pass.",
        "Test edge cases (empty, single, duplicates, negatives) before declaring it done.",
        "Re-solve problems you missed a few days later — spaced repetition cements them.",
        "In interviews, explain your thinking out loud; silence reads as being stuck.",
    ],
    "exercises": [
        ("Solve FizzBuzz for 1..15.", "Modulo checks.",
         r'''for n in range(1, 16):
    print("FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0
          else "Buzz" if n % 5 == 0 else n)'''),
        ("Reverse the string 'hello' without slicing.", "Build backward.",
         r'''s = "hello"; out = ""
for c in s: out = c + out
print(out)  # olleh'''),
        ("Check if 'listen'/'silent' are anagrams.", "Counter compare.",
         r'''from collections import Counter
print(Counter("listen") == Counter("silent"))  # True'''),
        ("Find the max subarray sum of [-2,1,-3,4,-1,2,1,-5,4].", "Kadane.",
         r'''def kadane(a):
    best = cur = a[0]
    for x in a[1:]:
        cur = max(x, cur + x); best = max(best, cur)
    return best
print(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6'''),
        ("Return True if [1,2,3,1] contains a duplicate.", "Set length.",
         r'''a = [1, 2, 3, 1]
print(len(set(a)) != len(a))  # True'''),
        ("Compute fibonacci(10) iteratively.", "Two vars.",
         r'''a, b = 0, 1
for _ in range(10): a, b = b, a + b
print(a)  # 55'''),
        ("Find the missing number in [0,1,3] (range 0..3).", "Sum formula.",
         r'''a = [0, 1, 3]; n = 3
print(n * (n + 1) // 2 - sum(a))  # 2'''),
        ("Merge sorted [1,3,5] and [2,4] into one sorted list.", "Two pointers.",
         r'''def merge(a, b):
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: out.append(a[i]); i += 1
        else: out.append(b[j]); j += 1
    return out + a[i:] + b[j:]
print(merge([1, 3, 5], [2, 4]))  # [1,2,3,4,5]'''),
    ],
}

CONTENT["kaggle"] = {
    "deps": ["pandas", "scikit-learn"],
    "what": (
        "**Kaggle** is a platform for data-science competitions, datasets, notebooks, and learning. "
        "A competition gives you a **training set** (with labels) and a **test set** (without); you "
        "build a model and submit predictions, scored on a hidden leaderboard. The standard loop: "
        "EDA → baseline model → **cross-validation** → feature engineering → ensembling → submit. "
        "It's the best place to practice end-to-end ML on real data."
    ),
    "why": (
        "Kaggle gives real datasets, public baselines, and instant feedback. Competing (or just "
        "completing) builds practical skills — data cleaning, validation discipline, and feature "
        "engineering — far faster than tutorials alone."
    ),
    "concepts": [
        ("Train/test split", "Labeled train; unlabeled test you predict on."),
        ("Baseline first", "A simple model to beat before getting fancy."),
        ("Cross-validation", "Trust local CV over leaderboard to avoid overfitting it."),
        ("Feature engineering", "Often the biggest source of score gains."),
        ("Submission file", "Usually a CSV of id,prediction rows."),
        ("Leaderboard", "Public (partial) vs private (final) — don't overfit public."),
    ],
    "examples": [
        ("The Kaggle workflow", r'''
steps = [
    "1. Understand the problem and the evaluation metric",
    "2. EDA: explore distributions, missing values, correlations",
    "3. Build a BASELINE (e.g. predict the mean / a simple model)",
    "4. Set up cross-validation you trust",
    "5. Feature engineering + better models",
    "6. Tune hyperparameters; try ensembling",
    "7. Generate predictions on the test set",
    "8. Write submission.csv and submit",
]
for s in steps:
    print(s)
print("\nGolden rule: trust your local CV score over the public leaderboard.")
'''),
        ("A baseline pipeline on toy data (pure Python)", r'''
# Toy 'competition': predict pass(1)/fail(0) from hours studied.
train = [(1, 0), (2, 0), (3, 0), (5, 1), (6, 1), (7, 1), (2.5, 0), (5.5, 1)]
test_ids_features = [(101, 1.5), (102, 4.0), (103, 6.5)]   # no labels

# Baseline: a single threshold learned from the class means
pass_hours = [h for h, y in train if y == 1]
fail_hours = [h for h, y in train if y == 0]
threshold = (sum(pass_hours) / len(pass_hours) +
             sum(fail_hours) / len(fail_hours)) / 2
print("learned threshold:", round(threshold, 2))

# Validate on the training data (a real comp uses a held-out split/CV)
acc = sum(1 for h, y in train if (h >= threshold) == y) / len(train)
print("train accuracy:", round(acc, 3))

# Generate a submission file (id,prediction)
print("\nsubmission.csv:")
print("id,passed")
for id_, hours in test_ids_features:
    print(f"{id_},{int(hours >= threshold)}")
'''),
        ("A real pipeline with pandas + scikit-learn (template)", r'''
try:
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import cross_val_score

    # In a real comp: train = pd.read_csv("train.csv"); test = pd.read_csv("test.csv")
    train = pd.DataFrame({
        "feature1": [1, 2, 3, 4, 5, 6, 7, 8],
        "feature2": [2, 1, 4, 3, 6, 5, 8, 7],
        "target":   [0, 0, 0, 0, 1, 1, 1, 1],
    })
    X = train[["feature1", "feature2"]]
    y = train["target"]

    model = RandomForestClassifier(n_estimators=50, random_state=0)
    scores = cross_val_score(model, X, y, cv=4)
    print("CV accuracy:", round(scores.mean(), 3), "+/-", round(scores.std(), 3))

    model.fit(X, y)                       # fit on all training data
    # submission = pd.DataFrame({"id": test.id, "target": model.predict(X_test)})
    # submission.to_csv("submission.csv", index=False)
    print("model trained — ready to predict and write submission.csv")
except ImportError:
    print("pandas/sklearn not installed — run: pip install pandas scikit-learn")
'''),
    ],
    "gotchas": [
        "Don't overfit the PUBLIC leaderboard — the private split decides final rank.",
        "Build robust cross-validation early and trust it over leaderboard noise.",
        "Avoid leakage: never fit preprocessing on test data or use future/target info.",
        "A strong baseline beats a fancy model with bugs — get end-to-end working first.",
        "Match the EXACT submission format (column names, id order) or it's rejected.",
    ],
    "exercises": [
        ("Compute accuracy of preds [1,0,1] vs truth [1,1,1].", "Mean correct.",
         r'''pred, true = [1, 0, 1], [1, 1, 1]
print(sum(p == t for p, t in zip(pred, true)) / len(true))  # 0.666'''),
        ("Make a baseline that predicts the majority class of [0,0,1].", "Most common.",
         r'''from collections import Counter
print(Counter([0, 0, 1]).most_common(1)[0][0])  # 0'''),
        ("Format a submission row id=5, pred=1 as CSV.", "Join.",
         r'''print(f"{5},{1}")  # 5,1'''),
        ("Why trust local CV over the public leaderboard?", "Overfitting.",
         r'''#md
The public leaderboard is a **small, fixed slice** you can accidentally overfit by
tuning to it. Robust **cross-validation** estimates generalization better and tracks
the hidden private score.'''),
        ("What is the first model you should build?", "Baseline.",
         r'''#md
A **simple baseline** (e.g. predict the mean/majority, or a basic model) to
establish a score to beat and verify the end-to-end pipeline works.'''),
        ("Predict with threshold 4.0: is 6.5 hours a pass?", "Compare.",
         r'''print(int(6.5 >= 4.0))  # 1'''),
        ("Name one cause of data leakage.", "Any valid.",
         r'''#md
Fitting a scaler/encoder on test data, including a feature derived from the target,
or using future information — all leak info and inflate validation scores.'''),
        ("Compute mean CV score of [0.81,0.79,0.83].", "Mean.",
         r'''s = [0.81, 0.79, 0.83]
print(round(sum(s) / len(s), 3))  # 0.81'''),
    ],
}

CONTENT["end-to-end-projects"] = {
    "what": (
        "An **end-to-end ML project** runs the full lifecycle: define the **problem** → collect/clean "
        "**data** → **EDA** → engineer features → **train** and validate models → **evaluate** → "
        "**deploy** → **monitor**. The model is a small slice; most effort is data work, validation "
        "discipline, and packaging. Doing complete projects (not just model snippets) is what turns "
        "knowledge into real-world skill."
    ),
    "why": (
        "Employers and real impact come from shipping working solutions, not isolated accuracy "
        "numbers. End-to-end projects integrate everything from earlier phases and produce portfolio "
        "pieces that prove you can deliver."
    ),
    "concepts": [
        ("Problem definition", "What are you predicting, and what metric matters?"),
        ("Data pipeline", "Collect, clean, split — reproducibly."),
        ("Modeling", "Baseline → iterate with validation."),
        ("Evaluation", "Right metric on held-out data; understand errors."),
        ("Deployment", "Save the model, wrap it in an API/app."),
        ("Reproducibility", "Seeds, versioned data/code, a clear README."),
    ],
    "examples": [
        ("The ML project lifecycle", r'''
lifecycle = [
    ("Problem",   "Predict if a student passes from hours studied; metric = accuracy"),
    ("Data",      "Collect (hours, passed) records; clean and split"),
    ("EDA",       "Check ranges, balance, correlation of hours vs outcome"),
    ("Features",  "Maybe add hours^2, sleep, attendance"),
    ("Model",     "Baseline threshold -> logistic regression"),
    ("Evaluate",  "Accuracy on a held-out test set; inspect errors"),
    ("Deploy",    "Save params, wrap predict() in an API"),
    ("Monitor",   "Watch for drift; retrain as new data arrives"),
]
for stage, detail in lifecycle:
    print(f"{stage:9}: {detail}")
'''),
        ("A COMPLETE mini-project (data -> train -> save -> predict)", r'''
import json, tempfile, os, math

# 1. DATA: (hours studied, passed)
data = [(1, 0), (2, 0), (3, 0), (4, 1), (5, 1), (6, 1), (2.5, 0), (4.5, 1)]

# 2. SPLIT into train / test
train, test = data[:6], data[6:]

# 3. TRAIN a logistic regression with gradient descent
def sigmoid(z): return 1 / (1 + math.exp(-z))
w, b, lr = 0.0, 0.0, 0.3
for _ in range(5000):
    gw = gb = 0.0
    for x, y in train:
        p = sigmoid(w * x + b)
        gw += (p - y) * x; gb += (p - y)
    w -= lr * gw / len(train); b -= lr * gb / len(train)

# 4. EVALUATE on held-out test data
acc = sum(1 for x, y in test if (sigmoid(w * x + b) >= 0.5) == y) / len(test)
print(f"trained model: w={w:.3f}, b={b:.3f}")
print("test accuracy:", acc)

# 5. SAVE the model artifact
path = os.path.join(tempfile.gettempdir(), "study_model.json")
with open(path, "w") as f:
    json.dump({"w": w, "b": b}, f)

# 6. LOAD + PREDICT (what a deployed service does)
with open(path) as f:
    m = json.load(f)
def predict(hours):
    return "pass" if sigmoid(m["w"] * hours + m["b"]) >= 0.5 else "fail"
print("predict 3.5 hrs ->", predict(3.5))
print("predict 5.0 hrs ->", predict(5.0))
'''),
        ("A clean project structure and reproducibility", r'''
structure = """\
my-ml-project/
|-- README.md              # problem, results, how to run
|-- requirements.txt       # pinned dependencies
|-- data/
|   |-- raw/               # original, never edited
|   |-- processed/         # cleaned, model-ready
|-- notebooks/
|   |-- 01-eda.ipynb
|-- src/
|   |-- data.py            # load & clean
|   |-- features.py        # feature engineering
|   |-- train.py           # train & save model
|   |-- predict.py         # load model & serve
|-- models/                # saved artifacts
|-- tests/
"""
print(structure)
print("Reproducibility checklist:")
for item in ["Fix random seeds", "Pin dependency versions",
             "Version data + code together", "Document run steps in README",
             "Separate raw vs processed data"]:
    print("  [x]", item)
'''),
    ],
    "gotchas": [
        "Most of the work is data cleaning/validation, not the model — budget time accordingly.",
        "Define the success metric BEFORE modeling, tied to the real goal.",
        "Keep raw data immutable; do all cleaning into a separate processed copy.",
        "Set seeds and pin versions, or 'it worked yesterday' becomes unreproducible.",
        "Ship something deployable (save + a predict function); accuracy in a notebook isn't a product.",
    ],
    "exercises": [
        ("Order the lifecycle: model, data, deploy, problem.", "Sequence.",
         r'''#md
**Problem → Data → Model → Deploy.** Define what you're solving, get/clean the data,
build and validate the model, then deploy and monitor it.'''),
        ("Split [1..10] into 80% train / 20% test sizes.", "int(0.8*n).",
         r'''n = 10; s = int(0.8 * n)
print("train", s, "test", n - s)  # train 8 test 2'''),
        ("Save {'w':1.5} as a model artifact (JSON string).", "json.dumps.",
         r'''import json
print(json.dumps({"w": 1.5}))'''),
        ("Why keep raw data immutable?", "Reproducibility.",
         r'''#md
So you can always **reproduce** the cleaning pipeline from the original source and
recover from mistakes. Edit a separate processed copy, never the raw data.'''),
        ("Predict pass/fail with sigmoid(w*x+b)>=0.5 for w=1,x=5,b=-3.", "Threshold.",
         r'''import math
z = 1 * 5 + (-3)
print("pass" if 1 / (1 + math.exp(-z)) >= 0.5 else "fail")  # pass'''),
        ("Name two things a project README should contain.", "Any valid.",
         r'''#md
For example: the **problem statement & results**, and **how to install/run** it
(setup, commands). Also useful: data source, approach, and limitations.'''),
        ("Why define the metric before modeling?", "Alignment.",
         r'''#md
So the model optimizes the **right objective** tied to the real goal. Choosing the
metric afterward risks optimizing the wrong thing (e.g. accuracy on imbalanced
data).'''),
        ("Compute test accuracy: 3 correct of 4.", "correct/total.",
         r'''print(3 / 4)  # 0.75'''),
    ],
}

CONTENT["portfolio"] = {
    "what": (
        "A **portfolio** is your public proof of skill: a small set of well-documented projects "
        "(usually on GitHub) plus clear write-ups. For ML, strong portfolios show the **whole "
        "process** — problem framing, EDA, modeling decisions, evaluation, and (ideally) a live "
        "demo — not just a final accuracy number. A great README and clean, reproducible code "
        "matter as much as the model."
    ),
    "why": (
        "Hiring managers skim portfolios to see if you can deliver real, communicated work. A few "
        "polished, end-to-end projects beat dozens of half-finished notebooks and often matter more "
        "than a resume line."
    ),
    "concepts": [
        ("Quality over quantity", "3–5 polished projects beat 20 sloppy ones."),
        ("Show the process", "EDA, decisions, trade-offs — not just the result."),
        ("Great README", "Problem, approach, results, how to run, demo link."),
        ("Reproducibility", "Anyone can clone and run it."),
        ("Live demo", "A Streamlit/HF Space app makes it tangible."),
        ("Range", "Cover different skills: viz, ML, DL, deployment."),
    ],
    "examples": [
        ("A README template that sells a project", r'''
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
'''),
        ("A portfolio project checklist", r'''
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
'''),
        ("Suggested projects by skill level", r'''
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
'''),
    ],
    "gotchas": [
        "Quality over quantity — a few polished projects beat many abandoned notebooks.",
        "A missing/weak README kills a good project; recruiters skim, so lead with results.",
        "If it isn't reproducible (no requirements, hard-coded paths), people can't run it.",
        "Don't just paste accuracy — explain the problem, decisions, and limitations.",
        "Avoid only toy datasets everyone uses; a unique/real dataset stands out.",
    ],
    "exercises": [
        ("How many polished projects are usually enough?", "Quality.",
         r'''#md
About **3–5 polished, end-to-end projects** — depth and clarity beat a large number
of unfinished ones.'''),
        ("Name three sections a good README needs.", "Any valid.",
         r'''#md
For example: **Problem**, **Approach/Results**, and **How to run** (setup +
commands). A demo link and data description strengthen it further.'''),
        ("Why include a live demo?", "Tangibility.",
         r'''#md
It makes the project **tangible and interactive** for reviewers who won't run your
code — they can try it instantly (e.g. a Streamlit app or HF Space).'''),
        ("What proves reproducibility in a repo?", "Any valid.",
         r'''#md
A pinned **requirements.txt**, clear **run instructions**, fixed seeds, and no
hard-coded local paths — so anyone can clone and reproduce your results.'''),
        ("Quality or quantity for a portfolio?", "Recall.",
         r'''#md
**Quality.** A few well-documented, working projects communicate competence far
better than many sloppy or unfinished ones.'''),
        ("Pick a good beginner project idea.", "Any valid.",
         r'''#md
For example: an **EDA of a public dataset** with clear visualizations and insights,
or a **clean classification pipeline** (Titanic/Iris) with proper validation.'''),
        ("Why show EDA and decisions, not just accuracy?", "Process.",
         r'''#md
It demonstrates your **reasoning and process** — how you understood the data and
made trade-offs — which is what employers actually evaluate, not just a number.'''),
        ("Where do most people host portfolios?", "Recall.",
         r'''#md
**GitHub** (code + READMEs), often paired with live demos on **Streamlit Cloud /
Hugging Face Spaces** and a short write-up or blog post.'''),
    ],
}

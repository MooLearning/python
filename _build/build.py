#!/usr/bin/env python3
"""Generator for the Python + DSA + AI/ML learning workspace.

Run from anywhere:  python3 _build/build.py
It writes folders/files into the REPO ROOT (parent of this _build/ dir).

Content lives in c01.py .. c10.py (one module per phase), each exposing a
CONTENT dict mapping topic-slug -> meta dict with keys:
    what      : str   (paragraph, beginner-friendly)
    why       : str   (paragraph)
    concepts  : list[(term, description)]
    examples  : list[(title, code)]     # code must be runnable; first reused in README
    gotchas   : list[str]               (3-5)
    exercises : list[(problem, hint, solution)]  # 8-10, easy->hard
    deps      : list[str] (optional)    # pip packages used by examples
A solution string starting with "#md" is rendered as markdown (not a code block).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)  # repo root
sys.path.insert(0, HERE)

# --------------------------------------------------------------------------
# Curriculum structure: (phase_slug, phase_title, [(num, slug, title), ...])
# --------------------------------------------------------------------------
STRUCTURE = [
    ("phase-01-python-fundamentals", "Phase 1 — Python Fundamentals", [
        (1, "installation-and-setup", "Installation and Setup"),
        (2, "variables-and-data-types", "Variables and Data Types"),
        (3, "operators", "Operators"),
        (4, "input-output-and-type-casting", "Input, Output and Type Casting"),
        (5, "strings-and-methods", "Strings and Methods"),
        (6, "conditional-statements", "Conditional Statements"),
        (7, "loops", "Loops"),
        (8, "lists-tuples-sets-dictionaries", "Lists, Tuples, Sets and Dictionaries"),
        (9, "comprehensions", "Comprehensions"),
        (10, "functions", "Functions"),
        (11, "lambda-map-filter-reduce", "Lambda, Map, Filter and Reduce"),
        (12, "scope", "Scope (local, global, nonlocal)"),
        (13, "recursion-basics", "Recursion Basics"),
        (14, "exception-handling", "Exception Handling"),
        (15, "file-handling", "File Handling"),
        (16, "modules-and-packages", "Modules and Packages"),
        (17, "virtual-environments", "Virtual Environments"),
    ]),
    ("phase-02-intermediate-python", "Phase 2 — Intermediate Python", [
        (18, "oop-classes-and-objects", "OOP: Classes and Objects"),
        (19, "inheritance-polymorphism-encapsulation", "Inheritance, Polymorphism and Encapsulation"),
        (20, "dunder-methods", "Dunder (Magic) Methods"),
        (21, "decorators", "Decorators"),
        (22, "generators-and-iterators", "Generators and Iterators"),
        (23, "closures", "Closures"),
        (24, "context-managers", "Context Managers"),
        (25, "regular-expressions", "Regular Expressions"),
        (26, "datetime", "Datetime"),
        (27, "json-and-csv", "JSON and CSV"),
        (28, "apis-with-requests", "APIs with Requests"),
        (29, "multithreading-and-multiprocessing", "Multithreading and Multiprocessing"),
        (30, "logging", "Logging"),
    ]),
    ("phase-03-data-structures-and-algorithms", "Phase 3 — Data Structures & Algorithms", [
        (31, "big-o-notation", "Big-O Notation"),
        (32, "arrays", "Arrays and Dynamic Arrays"),
        (33, "string-algorithms", "String Algorithms"),
        (34, "linked-lists", "Linked Lists"),
        (35, "stacks", "Stacks"),
        (36, "queues", "Queues"),
        (37, "hashing-and-hash-tables", "Hashing and Hash Tables"),
        (38, "linear-and-binary-search", "Linear and Binary Search"),
        (39, "basic-sorts", "Basic Sorts (Bubble, Selection, Insertion)"),
        (40, "merge-sort", "Merge Sort"),
        (41, "quick-sort", "Quick Sort"),
        (42, "heap-counting-radix-sort", "Heap, Counting and Radix Sort"),
        (43, "trees-and-bst", "Trees and BST"),
        (44, "tree-traversals", "Tree Traversals"),
        (45, "avl-and-balanced-trees", "AVL and Balanced Trees"),
        (46, "heaps", "Heaps"),
        (47, "tries", "Tries"),
        (48, "graphs", "Graphs"),
        (49, "bfs-and-dfs", "BFS and DFS"),
        (50, "recursion-and-backtracking", "Recursion and Backtracking"),
        (51, "two-pointers-and-sliding-window", "Two Pointers and Sliding Window"),
        (52, "greedy-algorithms", "Greedy Algorithms"),
        (53, "divide-and-conquer", "Divide and Conquer"),
        (54, "dynamic-programming", "Dynamic Programming"),
        (55, "graph-algorithms", "Graph Algorithms"),
        (56, "bit-manipulation", "Bit Manipulation"),
    ]),
    ("phase-04-math-for-ml", "Phase 4 — Math for ML", [
        (57, "linear-algebra", "Linear Algebra"),
        (58, "calculus-basics", "Calculus Basics"),
        (59, "probability-and-statistics", "Probability and Statistics"),
        (60, "distributions", "Distributions"),
    ]),
    ("phase-05-data-science-libraries", "Phase 5 — Data Science Libraries", [
        (61, "numpy", "NumPy"),
        (62, "pandas", "pandas"),
        (63, "matplotlib", "Matplotlib"),
        (64, "seaborn", "Seaborn"),
        (65, "data-preprocessing", "Data Preprocessing"),
        (66, "exploratory-data-analysis", "Exploratory Data Analysis (EDA)"),
        (67, "feature-engineering", "Feature Engineering"),
        (68, "missing-data-and-outliers", "Missing Data and Outliers"),
    ]),
    ("phase-06-machine-learning", "Phase 6 — Machine Learning", [
        (69, "ml-overview", "ML Overview"),
        (70, "train-test-split-and-cross-validation", "Train/Test Split and Cross-Validation"),
        (71, "bias-variance-tradeoff", "Bias-Variance Tradeoff"),
        (72, "linear-regression", "Linear Regression"),
        (73, "logistic-regression", "Logistic Regression"),
        (74, "knn", "K-Nearest Neighbors (KNN)"),
        (75, "svm", "Support Vector Machines (SVM)"),
        (76, "decision-trees", "Decision Trees"),
        (77, "random-forests", "Random Forests"),
        (78, "naive-bayes", "Naive Bayes"),
        (79, "gradient-boosting", "Gradient Boosting"),
        (80, "kmeans-clustering", "K-Means Clustering"),
        (81, "hierarchical-clustering", "Hierarchical Clustering"),
        (82, "dbscan", "DBSCAN"),
        (83, "pca", "Principal Component Analysis (PCA)"),
        (84, "dimensionality-reduction", "Dimensionality Reduction (t-SNE)"),
        (85, "classification-metrics", "Classification Metrics"),
        (86, "regression-metrics", "Regression Metrics"),
        (87, "hyperparameter-tuning", "Hyperparameter Tuning"),
        (88, "regularization", "Regularization (L1, L2)"),
        (89, "ensemble-methods", "Ensemble Methods"),
    ]),
    ("phase-07-deep-learning", "Phase 7 — Deep Learning", [
        (90, "neural-network-fundamentals", "Neural Network Fundamentals"),
        (91, "forward-and-backpropagation", "Forward and Backpropagation"),
        (92, "gradient-descent-and-optimizers", "Gradient Descent and Optimizers"),
        (93, "tensorflow-keras-pytorch", "TensorFlow, Keras and PyTorch"),
        (94, "building-anns", "Building ANNs"),
        (95, "cnn", "Convolutional Neural Networks (CNN)"),
        (96, "rnn-lstm-gru", "RNN, LSTM and GRU"),
        (97, "dropout-and-batchnorm", "Dropout and Batch Normalization"),
        (98, "transfer-learning", "Transfer Learning"),
    ]),
    ("phase-08-specialized-ai", "Phase 8 — Specialized AI", [
        (99, "nlp-basics", "NLP Basics"),
        (100, "transformers-and-attention", "Transformers and Attention"),
        (101, "llm-basics", "LLM Basics"),
        (102, "computer-vision-opencv", "Computer Vision with OpenCV"),
        (103, "reinforcement-learning-basics", "Reinforcement Learning Basics"),
    ]),
    ("phase-09-deployment-and-mlops", "Phase 9 — Deployment & MLOps", [
        (104, "model-saving-and-loading", "Model Saving and Loading"),
        (105, "flask-fastapi-serving", "Flask and FastAPI Serving"),
        (106, "streamlit-apps", "Streamlit Apps"),
        (107, "docker-basics", "Docker Basics"),
        (108, "cloud-deployment", "Cloud Deployment"),
        (109, "mlops-and-monitoring", "MLOps and Monitoring"),
        (110, "git-and-version-control", "Git and Version Control"),
    ]),
    ("phase-10-practice", "Phase 10 — Practice", [
        (111, "dsa-practice", "DSA Practice"),
        (112, "kaggle", "Kaggle"),
        (113, "end-to-end-projects", "End-to-End Projects"),
        (114, "portfolio", "Portfolio"),
    ]),
]

# --------------------------------------------------------------------------
# Load per-phase content modules (c01..c10). Missing modules are tolerated.
# --------------------------------------------------------------------------
CONTENT = {}
for i in range(1, 11):
    mod_name = "c%02d" % i
    try:
        mod = __import__(mod_name)
    except ImportError:
        continue
    CONTENT.update(getattr(mod, "CONTENT", {}))


def normalize(meta, title):
    """Fill any missing keys so rendering never crashes."""
    m = dict(meta)
    m.setdefault("what", "%s is a key topic in this curriculum." % title)
    m.setdefault("why", "Understanding %s strengthens your foundation for later phases." % title)
    m.setdefault("concepts", [])
    m.setdefault("gotchas", [])
    m.setdefault("exercises", [])
    m.setdefault("deps", [])
    if not m.get("examples"):
        m["examples"] = [("Hello", 'print("Study %s — examples coming. Edit me!")' % title)]
    return m


def fallback_meta(title):
    return normalize({}, title)


# --------------------------------------------------------------------------
# Renderers
# --------------------------------------------------------------------------
def render_readme(num, slug, title, m):
    p = []
    p.append("# %02d — %s\n" % (num, title))
    p.append("> Part of the **Python + DSA + AI/ML** learning workspace.  "
             "Learning loop: **README → notes.py → practice.md**\n")
    p.append("## What is it?\n")
    p.append(m["what"].strip() + "\n")
    p.append("## Why it matters\n")
    p.append(m["why"].strip() + "\n")
    if m.get("deps"):
        p.append("## Setup\n")
        p.append("This topic uses external libraries. Install them with:\n")
        p.append("```bash\npip install %s\n```\n" % " ".join(m["deps"]))
    if m.get("concepts"):
        p.append("## Key concepts\n")
        for term, desc in m["concepts"]:
            p.append("- **%s** — %s" % (term, desc))
        p.append("")
    p.append("## Code example\n")
    p.append("A fully commented, runnable example (see `notes.py` for more):\n")
    _, code = m["examples"][0]
    p.append("```python\n" + code.strip() + "\n```\n")
    p.append("Run every example in this topic with:\n")
    p.append("```bash\npython notes.py\n```\n")
    if m.get("gotchas"):
        p.append("## Common mistakes & gotchas\n")
        for g in m["gotchas"]:
            p.append("- ⚠️ %s" % g)
        p.append("")
    p.append("## Practice\n")
    p.append("Open [`practice.md`](practice.md) and solve the exercises (easy → hard). "
             "Try each one before revealing the solution.\n")
    return "\n".join(p) + "\n"


def render_notes(num, slug, title, m):
    L = []
    bar = "=" * 70
    L.append("# " + bar)
    L.append("# %02d — %s  |  notes.py" % (num, title))
    L.append("# Run:  python notes.py")
    L.append("# Heavily commented, runnable examples. Edit freely and re-run!")
    L.append("# " + bar)
    L.append("")
    if m.get("deps"):
        L.append("# Requires: %s" % ", ".join(m["deps"]))
        L.append("# Install:  pip install %s" % " ".join(m["deps"]))
        L.append("")
    for i, (etitle, code) in enumerate(m["examples"], 1):
        safe = etitle.replace('"', "'")
        L.append("# " + "-" * 70)
        L.append("# Example %d: %s" % (i, etitle))
        L.append("# " + "-" * 70)
        L.append('print("\\n--- Example %d: %s ---")' % (i, safe))
        L.append(code.strip())
        L.append("")
    L.append('print("\\nDone! Tip: change values above and run again to learn by experiment.")')
    return "\n".join(L) + "\n"


def render_practice(num, slug, title, m):
    p = []
    p.append("# %02d — %s: Practice\n" % (num, title))
    p.append("Solve top to bottom (easy → hard). Attempt each problem yourself, "
             "then expand **Solution** to check.\n")
    if not m.get("exercises"):
        p.append("_Exercises coming soon for this topic._\n")
        return "\n".join(p) + "\n"
    for i, (problem, hint, sol) in enumerate(m["exercises"], 1):
        p.append("## Exercise %d\n" % i)
        p.append(problem.strip() + "\n")
        if hint:
            p.append("*Hint: %s*\n" % hint)
        p.append("<details>\n<summary>✅ Solution</summary>\n")
        if sol.strip().startswith("#md"):
            p.append(sol.strip()[3:].strip() + "\n")
        else:
            p.append("```python\n" + sol.strip() + "\n```\n")
        p.append("</details>\n")
    return "\n".join(p) + "\n"


def render_master_readme(folders, files):
    p = []
    p.append("# 🐍 Python + DSA + AI/ML — Learning Workspace\n")
    p.append("A complete, hands-on roadmap from Python basics to AI/ML, organized into "
             "**10 phases** and **114 topics**. Every topic folder contains three files "
             "designed to be worked in order.\n")
    p.append("## How to use this repo\n")
    p.append("For **each topic**, follow this 3-step learning loop:\n")
    p.append("1. **`README.md`** — Read first. Plain-English explanation of *what* the "
             "topic is, *why* it matters, the key ideas, a commented runnable example, "
             "and common gotchas.")
    p.append("2. **`notes.py`** — Run and tinker. Multiple commented, runnable examples. "
             "Execute with `python notes.py`, then change things and re-run to build intuition.")
    p.append("3. **`practice.md`** — Test yourself. 8–10 exercises (easy → hard). Try each "
             "before expanding the collapsible solution.\n")
    p.append("> **Tip:** Don't just read — *run the code and break it*. The fastest way to "
             "learn is to change a line, predict what happens, and check.\n")
    p.append("### Suggested path\n")
    p.append("- Finish **Phase 1–2** (Python) before anything else.\n"
             "- Then **Phase 3 (DSA)** and **Phases 4–6 (Math + Data + ML)** can run in parallel.\n"
             "- **Phases 7–9** build on ML. **Phase 10** is continuous practice — start it early.\n")
    p.append("### Requirements\n")
    p.append("- Python 3.10+ for Phases 1–3 (standard library only).\n"
             "- Later phases use libraries; install per-topic with the `pip install` line in each README, "
             "or all at once:\n")
    p.append("```bash\npip install numpy pandas matplotlib seaborn scikit-learn "
             "requests flask fastapi uvicorn streamlit\n```\n")
    p.append("---\n")
    p.append("## Roadmap & progress\n")
    p.append("Check topics off as you complete them.\n")
    for phase_slug, phase_title, topics in STRUCTURE:
        p.append("### %s\n" % phase_title)
        for num, slug, title in topics:
            link = "%s/%02d-%s/" % (phase_slug, num, slug)
            p.append("- [ ] [%02d — %s](%s)" % (num, title, link))
        p.append("")
    p.append("---\n")
    p.append("_Generated by `_build/build.py` — %d folders, %d files. "
             "Re-run `python3 _build/build.py` to regenerate._\n" % (folders, files))
    return "\n".join(p) + "\n"


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------
def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    folders = 0
    files = 0
    authored = 0
    total_topics = 0
    for phase_slug, phase_title, topics in STRUCTURE:
        phase_dir = os.path.join(BASE, phase_slug)
        os.makedirs(phase_dir, exist_ok=True)
        folders += 1
        for num, slug, title in topics:
            total_topics += 1
            tdir = os.path.join(phase_dir, "%02d-%s" % (num, slug))
            os.makedirs(tdir, exist_ok=True)
            folders += 1
            if slug in CONTENT:
                authored += 1
                m = normalize(CONTENT[slug], title)
            else:
                m = fallback_meta(title)
            write_file(os.path.join(tdir, "README.md"), render_readme(num, slug, title, m))
            write_file(os.path.join(tdir, "notes.py"), render_notes(num, slug, title, m))
            write_file(os.path.join(tdir, "practice.md"), render_practice(num, slug, title, m))
            files += 3

    # master README (count it in files)
    files += 1
    write_file(os.path.join(BASE, "README.md"), render_master_readme(folders, files))

    print("=" * 60)
    print("BUILD COMPLETE")
    print("=" * 60)
    print("Phases           :", len(STRUCTURE))
    print("Topics           :", total_topics)
    print("Topics authored  :", authored, "/", total_topics)
    print("Folders created  :", folders)
    print("Files created    :", files)
    print("Output root      :", BASE)


if __name__ == "__main__":
    main()

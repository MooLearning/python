# 106 — Streamlit Apps

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Streamlit** turns a Python script into an interactive web app with almost no web code. You write top-to-bottom Python using `st.` widgets (`st.slider`, `st.button`, `st.file_uploader`) and display calls (`st.write`, `st.dataframe`, `st.pyplot`). On every interaction Streamlit **re-runs the whole script**, recomputing the UI. It's the fastest way to build ML demos and dashboards.

## Why it matters

Streamlit lets data scientists ship interactive demos, prototypes, and internal tools in minutes — no HTML/JS/CSS — perfect for showcasing models to non-technical stakeholders.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install streamlit
```

## Key concepts

- **Script = app** — The whole script defines the UI, top to bottom.
- **Re-run model** — Any widget change re-executes the script.
- **Widgets** — st.slider/selectbox/button capture user input.
- **Display** — st.write/dataframe/line_chart render outputs.
- **Caching** — @st.cache_data avoids recomputing expensive steps.
- **Session state** — st.session_state persists values across re-runs.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import statistics as st_

# In Streamlit this data would come from st.file_uploader / a widget
data = [23, 45, 12, 67, 34, 89, 21, 55]

# Compute the same summary a dashboard would display
summary = {
    "count": len(data),
    "mean": round(st_.mean(data), 2),
    "median": st_.median(data),
    "min": min(data),
    "max": max(data),
}
print("Dashboard summary:")
for k, v in summary.items():
    print(f"  {k:7}: {v}")

# A simulated 'slider' filter: keep values above a threshold
threshold = 40                       # would be st.slider("min", 0, 100)
filtered = [x for x in data if x >= threshold]
print(f"\nvalues >= {threshold}: {filtered}")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ The ENTIRE script re-runs on every interaction — cache expensive work with @st.cache_data.
- ⚠️ Run apps with `streamlit run app.py`, not `python app.py` (the latter won't start the server).
- ⚠️ Use st.session_state to keep values across re-runs; plain variables reset each run.
- ⚠️ Heavy computations in the script make the UI feel sluggish — cache or precompute.
- ⚠️ Widget order in the script = layout order; structure the script as you want the page.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


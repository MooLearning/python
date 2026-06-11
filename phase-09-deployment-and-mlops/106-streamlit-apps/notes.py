# ======================================================================
# 106 — Streamlit Apps  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: streamlit
# Install:  pip install streamlit

# ----------------------------------------------------------------------
# Example 1: The logic behind a dashboard (runs as plain Python)
# ----------------------------------------------------------------------
print("\n--- Example 1: The logic behind a dashboard (runs as plain Python) ---")
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

# ----------------------------------------------------------------------
# Example 2: A Streamlit app (template)
# ----------------------------------------------------------------------
print("\n--- Example 2: A Streamlit app (template) ---")
try:
    import streamlit as st

    st.title("Model Demo")                       # page title
    st.write("Adjust the inputs and see the prediction update.")

    # Widgets capture user input; the script re-runs on every change
    x1 = st.slider("Feature 1", 0.0, 10.0, 5.0)
    x2 = st.slider("Feature 2", 0.0, 10.0, 3.0)

    weights, bias = [0.5, -0.3], 0.1
    score = weights[0] * x1 + weights[1] * x2 + bias
    label = "positive" if score >= 0 else "negative"

    st.metric("Score", round(score, 3))
    st.write("Prediction:", label)

    print("Streamlit app defined. Run with:  streamlit run app.py")
except ImportError:
    print("Streamlit not installed — run: pip install streamlit")

# ----------------------------------------------------------------------
# Example 3: Caching and charts in Streamlit (template)
# ----------------------------------------------------------------------
print("\n--- Example 3: Caching and charts in Streamlit (template) ---")
try:
    import streamlit as st

    @st.cache_data                      # cache: expensive load runs once
    def load_data():
        return [10, 20, 15, 30, 25, 40]

    data = load_data()
    st.line_chart(data)                 # built-in chart
    st.bar_chart(data)

    if st.button("Show stats"):         # button returns True on click
        st.write("Mean:", sum(data) / len(data))

    # Persist a counter across re-runs with session state
    if "clicks" not in st.session_state:
        st.session_state.clicks = 0
    print("Streamlit caching + charts demo ready.")
except ImportError:
    print("Streamlit not installed — run: pip install streamlit")

print("\nDone! Tip: change values above and run again to learn by experiment.")

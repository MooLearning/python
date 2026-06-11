# ======================================================================
# 62 — pandas  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: pandas
# Install:  pip install pandas

# ----------------------------------------------------------------------
# Example 1: Building a DataFrame and inspecting it
# ----------------------------------------------------------------------
print("\n--- Example 1: Building a DataFrame and inspecting it ---")
try:
    import pandas as pd

    df = pd.DataFrame({
        "name": ["Ada", "Bob", "Cy", "Dee"],
        "age": [30, 25, 35, 28],
        "city": ["NYC", "LA", "NYC", "LA"],
    })
    print(df)
    print("\nshape   :", df.shape)        # (4, 3)
    print("columns :", list(df.columns))
    print("\ndescribe (numeric):")
    print(df["age"].describe())
except ImportError:
    print("pandas not installed — run: pip install pandas")

# ----------------------------------------------------------------------
# Example 2: Selecting, filtering, and adding columns
# ----------------------------------------------------------------------
print("\n--- Example 2: Selecting, filtering, and adding columns ---")
try:
    import pandas as pd

    df = pd.DataFrame({
        "name": ["Ada", "Bob", "Cy", "Dee"],
        "age": [30, 25, 35, 28],
        "salary": [90, 60, 120, 75],
    })
    print("ages column:\n", df["age"].tolist())
    print("\nover 28:\n", df[df["age"] > 28][["name", "age"]])

    # Add a computed column
    df["bonus"] = df["salary"] * 0.10
    print("\nwith bonus:\n", df[["name", "salary", "bonus"]])

    # iloc by position, loc by label
    print("\nfirst row:\n", df.iloc[0])
except ImportError:
    print("pandas not installed — run: pip install pandas")

# ----------------------------------------------------------------------
# Example 3: groupby aggregation and sorting
# ----------------------------------------------------------------------
print("\n--- Example 3: groupby aggregation and sorting ---")
try:
    import pandas as pd

    df = pd.DataFrame({
        "dept": ["eng", "eng", "sales", "sales", "eng"],
        "name": ["A", "B", "C", "D", "E"],
        "salary": [100, 120, 80, 90, 110],
    })
    # Average salary per department
    avg = df.groupby("dept")["salary"].mean()
    print("avg salary by dept:\n", avg)

    # Multiple aggregations at once
    stats = df.groupby("dept")["salary"].agg(["count", "mean", "max"])
    print("\nstats:\n", stats)

    # Sort the whole frame by salary, descending
    print("\ntop earners:\n", df.sort_values("salary", ascending=False).head(3))
except ImportError:
    print("pandas not installed — run: pip install pandas")

print("\nDone! Tip: change values above and run again to learn by experiment.")

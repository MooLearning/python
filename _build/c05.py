# -*- coding: utf-8 -*-
"""Phase 5 — Data Science Libraries.

Library examples are guarded with try/except ImportError so every notes.py runs
(printing an install hint) even when the library isn't installed. Where useful,
a pure-Python example demonstrates the concept and always runs.
"""

CONTENT = {}

CONTENT["numpy"] = {
    "deps": ["numpy"],
    "what": (
        "**NumPy** is the foundation of scientific Python. Its core object is the **ndarray**: a "
        "fast, fixed-type N-dimensional array. NumPy runs **vectorized** operations in compiled C, "
        "so `arr * 2` transforms a million numbers without a Python loop. It adds **broadcasting** "
        "(operating on different-shaped arrays), powerful **slicing/masking**, and a huge library of "
        "math, linear-algebra, and random functions."
    ),
    "why": (
        "Pandas, scikit-learn, matplotlib, TensorFlow, and PyTorch all build on NumPy arrays. "
        "Vectorization makes numeric code 10–100× faster and far shorter than pure-Python loops — "
        "it's the workhorse of all data science and ML."
    ),
    "concepts": [
        ("ndarray", "A fixed-type, N-dimensional array; the central NumPy object."),
        ("Vectorization", "Elementwise ops over whole arrays with no Python loop."),
        ("Broadcasting", "Auto-expanding shapes so arrays of different sizes combine."),
        ("Slicing & masking", "`a[1:3]`, `a[a > 0]` select sub-arrays (views, not copies)."),
        ("Axis", "Aggregate along rows (axis=1) or columns (axis=0)."),
        ("dtype & shape", "Every array has a data type and a shape tuple."),
    ],
    "examples": [
        ("Creating arrays and vectorized math", r'''
try:
    import numpy as np

    a = np.array([1, 2, 3, 4, 5])
    print("array :", a, "| shape", a.shape, "| dtype", a.dtype)
    print("a * 2 :", a * 2)            # vectorized: [ 2  4  6  8 10]
    print("a + 10:", a + 10)           # broadcast a scalar
    print("a ** 2:", a ** 2)           # [ 1  4  9 16 25]
    print("sum   :", a.sum(), "mean", a.mean(), "std", round(float(a.std()), 3))

    # Handy constructors
    print("zeros :", np.zeros(3))
    print("range :", np.arange(0, 10, 2))      # [0 2 4 6 8]
    print("linsp :", np.linspace(0, 1, 5))     # 5 evenly spaced points
except ImportError:
    print("NumPy not installed — run: pip install numpy")
'''),
        ("Indexing, slicing, boolean masks, 2D arrays", r'''
try:
    import numpy as np

    a = np.array([10, 20, 30, 40, 50])
    print("a[1:4]    :", a[1:4])        # [20 30 40]
    print("a[a > 25] :", a[a > 25])     # boolean mask -> [30 40 50]
    a[a > 25] = 0                       # assign through a mask
    print("masked    :", a)             # [10 20  0  0  0]

    # 2D array: shape (2, 3)
    m = np.array([[1, 2, 3],
                  [4, 5, 6]])
    print("m shape   :", m.shape)
    print("row 0     :", m[0])          # [1 2 3]
    print("col 1     :", m[:, 1])       # [2 5]
    print("m[1, 2]   :", m[1, 2])       # 6
except ImportError:
    print("NumPy not installed — run: pip install numpy")
'''),
        ("Aggregations, axes, broadcasting, reshape", r'''
try:
    import numpy as np

    m = np.array([[1, 2, 3],
                  [4, 5, 6]])
    print("sum all   :", m.sum())          # 21
    print("sum cols  :", m.sum(axis=0))    # [5 7 9]  (down columns)
    print("sum rows  :", m.sum(axis=1))    # [ 6 15]  (across rows)
    print("max each col:", m.max(axis=0))  # [4 5 6]

    # Broadcasting: add a row vector to every row
    bias = np.array([10, 20, 30])
    print("m + bias  :\n", m + bias)

    # Reshape and dot product
    print("reshaped  :\n", np.arange(6).reshape(2, 3))
    print("dot       :", np.dot([1, 2, 3], [4, 5, 6]))   # 32
except ImportError:
    print("NumPy not installed — run: pip install numpy")
'''),
    ],
    "gotchas": [
        "Array slices are VIEWS, not copies — modifying a slice changes the original. Use `.copy()`.",
        "NumPy arrays are fixed-dtype; mixing types silently up-casts (ints become floats).",
        "`*` is ELEMENTWISE multiply; use `@` or `np.dot` for matrix multiplication.",
        "Broadcasting only works when trailing dimensions match (or are 1) — otherwise it errors.",
        "Integer arrays overflow silently in some dtypes; watch for unexpected negatives.",
    ],
    "exercises": [
        ("Create an array [1,2,3] and multiply every element by 10.", "Vectorized.",
         r'''try:
    import numpy as np
    print(np.array([1, 2, 3]) * 10)  # [10 20 30]
except ImportError:
    print("pip install numpy")'''),
        ("Make a 3x3 array of zeros.", "np.zeros with a shape tuple.",
         r'''try:
    import numpy as np
    print(np.zeros((3, 3)))
except ImportError:
    print("pip install numpy")'''),
        ("Select all elements > 3 from [1,4,2,5,3].", "Boolean mask.",
         r'''try:
    import numpy as np
    a = np.array([1, 4, 2, 5, 3])
    print(a[a > 3])  # [4 5]
except ImportError:
    print("pip install numpy")'''),
        ("Compute the mean of each column of [[1,2],[3,4]].", "axis=0.",
         r'''try:
    import numpy as np
    print(np.array([[1, 2], [3, 4]]).mean(axis=0))  # [2. 3.]
except ImportError:
    print("pip install numpy")'''),
        ("Reshape np.arange(6) into 2 rows, 3 cols.", "reshape(2,3).",
         r'''try:
    import numpy as np
    print(np.arange(6).reshape(2, 3))
except ImportError:
    print("pip install numpy")'''),
        ("Create 5 evenly spaced numbers from 0 to 1.", "linspace.",
         r'''try:
    import numpy as np
    print(np.linspace(0, 1, 5))
except ImportError:
    print("pip install numpy")'''),
        ("Add the vector [1,0,1] to every row of a 2x3 ones array.", "Broadcasting.",
         r'''try:
    import numpy as np
    print(np.ones((2, 3)) + np.array([1, 0, 1]))
except ImportError:
    print("pip install numpy")'''),
        ("Compute the dot product of [1,2] and [3,4].", "np.dot.",
         r'''try:
    import numpy as np
    print(np.dot([1, 2], [3, 4]))  # 11
except ImportError:
    print("pip install numpy")'''),
    ],
}

CONTENT["pandas"] = {
    "deps": ["pandas"],
    "what": (
        "**pandas** is the go-to library for tabular data. Its two structures are the **Series** "
        "(a labeled 1-D array) and the **DataFrame** (a labeled 2-D table, like a spreadsheet). "
        "pandas makes loading (CSV/Excel/SQL), cleaning, filtering, transforming, **grouping**, and "
        "summarizing data concise and fast. It's where most real data analysis starts."
    ),
    "why": (
        "Real datasets are tables, and pandas is the standard tool to wrangle them: select columns, "
        "filter rows, handle missing values, join tables, and compute group statistics — the daily "
        "work of data science before any model is trained."
    ),
    "concepts": [
        ("Series", "A labeled 1-D column of values."),
        ("DataFrame", "A labeled 2-D table of rows and columns."),
        ("Selection", "`df['col']`, `df.loc[label]`, `df.iloc[pos]`."),
        ("Boolean filtering", "`df[df['age'] > 30]` keeps matching rows."),
        ("groupby", "Split-apply-combine: group rows and aggregate."),
        ("Missing data", "`isna()`, `fillna()`, `dropna()` handle NaNs."),
    ],
    "examples": [
        ("Building a DataFrame and inspecting it", r'''
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
'''),
        ("Selecting, filtering, and adding columns", r'''
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
'''),
        ("groupby aggregation and sorting", r'''
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
'''),
    ],
    "gotchas": [
        "`df['col']` returns a Series; `df[['col']]` (double brackets) returns a DataFrame.",
        "Chained indexing like `df[df.a>0]['b'] = 1` may not assign — use `.loc[mask, 'b']`.",
        "Operations return NEW frames by default; assign the result or use `inplace=`/reassign.",
        "Missing values are NaN (a float) — they propagate; handle with fillna/dropna before math.",
        "`groupby` skips NaN keys by default and returns a grouped object — you must aggregate it.",
    ],
    "exercises": [
        ("Create a DataFrame with columns 'x'=[1,2,3] and 'y'=[4,5,6].", "Dict of lists.",
         r'''try:
    import pandas as pd
    print(pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]}))
except ImportError:
    print("pip install pandas")'''),
        ("Select only the 'x' column from that frame.", "df['x'].",
         r'''try:
    import pandas as pd
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    print(df["x"].tolist())  # [1, 2, 3]
except ImportError:
    print("pip install pandas")'''),
        ("Filter rows where x > 1.", "Boolean mask.",
         r'''try:
    import pandas as pd
    df = pd.DataFrame({"x": [1, 2, 3]})
    print(df[df["x"] > 1])
except ImportError:
    print("pip install pandas")'''),
        ("Add a column z = x + y.", "Vectorized column math.",
         r'''try:
    import pandas as pd
    df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
    df["z"] = df["x"] + df["y"]
    print(df)
except ImportError:
    print("pip install pandas")'''),
        ("Compute the mean of column 'age'=[20,30,40].", "Series.mean.",
         r'''try:
    import pandas as pd
    print(pd.Series([20, 30, 40]).mean())  # 30.0
except ImportError:
    print("pip install pandas")'''),
        ("Group [('a',1),('a',2),('b',3)] by letter and sum values.", "groupby.sum.",
         r'''try:
    import pandas as pd
    df = pd.DataFrame({"k": ["a", "a", "b"], "v": [1, 2, 3]})
    print(df.groupby("k")["v"].sum())
except ImportError:
    print("pip install pandas")'''),
        ("Sort a frame by 'score' descending.", "sort_values.",
         r'''try:
    import pandas as pd
    df = pd.DataFrame({"score": [3, 1, 2]})
    print(df.sort_values("score", ascending=False))
except ImportError:
    print("pip install pandas")'''),
        ("Count missing values per column in a frame with a NaN.", "isna().sum().",
         r'''try:
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a": [1, np.nan, 3]})
    print(df.isna().sum())
except ImportError:
    print("pip install pandas numpy")'''),
    ],
}

CONTENT["matplotlib"] = {
    "deps": ["matplotlib"],
    "what": (
        "**Matplotlib** is the foundational plotting library for Python. Its `pyplot` interface "
        "draws line plots, bar charts, scatter plots, histograms, and more. You build a figure, add "
        "data and labels, then show or save it. Almost every other Python viz tool (including "
        "seaborn and pandas `.plot`) sits on top of matplotlib."
    ),
    "why": (
        "Visualization is how you understand data and communicate results. A quick plot reveals "
        "trends, outliers, and distributions that raw numbers hide — an essential step in EDA and "
        "model evaluation."
    ),
    "concepts": [
        ("Figure & Axes", "The canvas (figure) holds one or more plots (axes)."),
        ("plot / scatter / bar / hist", "The common chart types."),
        ("Labels & title", "xlabel, ylabel, title, legend make plots readable."),
        ("savefig vs show", "Save to a file (headless) or display interactively."),
        ("Backends", "Use the 'Agg' backend to render without a screen."),
        ("Subplots", "Multiple axes in one figure with plt.subplots."),
    ],
    "examples": [
        ("A line plot saved to a file (headless-safe)", r'''
try:
    import matplotlib
    matplotlib.use("Agg")                 # render without a display
    import matplotlib.pyplot as plt
    import tempfile, os

    x = [0, 1, 2, 3, 4, 5]
    y = [v ** 2 for v in x]               # y = x^2

    plt.figure(figsize=(5, 3))
    plt.plot(x, y, marker="o", label="y = x^2")
    plt.title("Line Plot")
    plt.xlabel("x"); plt.ylabel("y")
    plt.legend(); plt.grid(True)

    out = os.path.join(tempfile.gettempdir(), "line_plot.png")
    plt.savefig(out, dpi=80); plt.close()
    print("saved line plot ->", out)
except ImportError:
    print("matplotlib not installed — run: pip install matplotlib")
'''),
        ("Bar chart and scatter plot", r'''
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import tempfile, os

    # Bar chart
    fruits = ["apple", "banana", "cherry"]
    counts = [12, 7, 19]
    plt.figure(figsize=(5, 3))
    plt.bar(fruits, counts, color=["red", "gold", "crimson"])
    plt.title("Fruit Counts"); plt.ylabel("count")
    bar = os.path.join(tempfile.gettempdir(), "bar.png")
    plt.savefig(bar, dpi=80); plt.close()
    print("saved bar chart ->", bar)

    # Scatter plot
    xs = [1, 2, 3, 4, 5]; ys = [2, 4, 5, 4, 6]
    plt.figure(figsize=(5, 3))
    plt.scatter(xs, ys)
    plt.title("Scatter"); plt.xlabel("x"); plt.ylabel("y")
    sca = os.path.join(tempfile.gettempdir(), "scatter.png")
    plt.savefig(sca, dpi=80); plt.close()
    print("saved scatter ->", sca)
except ImportError:
    print("matplotlib not installed — run: pip install matplotlib")
'''),
        ("Histogram and subplots", r'''
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import tempfile, os, random

    random.seed(0)
    data = [random.gauss(50, 10) for _ in range(1000)]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))
    ax1.hist(data, bins=20, color="steelblue", edgecolor="white")
    ax1.set_title("Histogram")
    ax2.plot(sorted(data))
    ax2.set_title("Sorted values")

    out = os.path.join(tempfile.gettempdir(), "subplots.png")
    fig.tight_layout(); fig.savefig(out, dpi=80); plt.close(fig)
    print("saved subplots ->", out)
except ImportError:
    print("matplotlib not installed — run: pip install matplotlib")
'''),
    ],
    "gotchas": [
        "On a headless server, set `matplotlib.use('Agg')` BEFORE importing pyplot, or it may error.",
        "Call `plt.close()` after saving in loops, or figures pile up and leak memory.",
        "`plt.show()` blocks until you close the window; use `savefig` in scripts/notebooks.",
        "Re-plotting onto the same figure overlays data — start a new `plt.figure()` each chart.",
        "Set labels/titles BEFORE savefig/show; adding them after rendering has no effect.",
    ],
    "exercises": [
        ("Plot y=[1,4,9] vs x=[1,2,3] and save it.", "plt.plot + savefig.",
         r'''try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, tempfile, os
    plt.plot([1, 2, 3], [1, 4, 9])
    p = os.path.join(tempfile.gettempdir(), "ex.png")
    plt.savefig(p); plt.close(); print("saved", p)
except ImportError:
    print("pip install matplotlib")'''),
        ("Make a bar chart of {'a':3,'b':5}.", "plt.bar.",
         r'''try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, tempfile, os
    plt.bar(["a", "b"], [3, 5])
    p = os.path.join(tempfile.gettempdir(), "bar.png")
    plt.savefig(p); plt.close(); print("saved", p)
except ImportError:
    print("pip install matplotlib")'''),
        ("Add an x-axis label 'time' to a plot.", "plt.xlabel.",
         r'''try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, tempfile, os
    plt.plot([1, 2], [3, 4]); plt.xlabel("time")
    p = os.path.join(tempfile.gettempdir(), "lab.png")
    plt.savefig(p); plt.close(); print("labeled & saved")
except ImportError:
    print("pip install matplotlib")'''),
        ("Plot a histogram of [1,1,2,3,3,3].", "plt.hist.",
         r'''try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, tempfile, os
    plt.hist([1, 1, 2, 3, 3, 3], bins=3)
    p = os.path.join(tempfile.gettempdir(), "h.png")
    plt.savefig(p); plt.close(); print("saved hist")
except ImportError:
    print("pip install matplotlib")'''),
        ("Why call matplotlib.use('Agg')? Explain in one line.", "Headless rendering.",
         r'''#md
The **'Agg'** backend renders plots to image files **without needing a display/GUI**
— essential on servers, CI, and scripts. Set it *before* importing pyplot.'''),
        ("Create a scatter of x=[1,2,3], y=[3,2,1].", "plt.scatter.",
         r'''try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, tempfile, os
    plt.scatter([1, 2, 3], [3, 2, 1])
    p = os.path.join(tempfile.gettempdir(), "s.png")
    plt.savefig(p); plt.close(); print("saved scatter")
except ImportError:
    print("pip install matplotlib")'''),
        ("Add a title 'Sales' to a plot.", "plt.title.",
         r'''try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, tempfile, os
    plt.plot([1, 2, 3]); plt.title("Sales")
    p = os.path.join(tempfile.gettempdir(), "t.png")
    plt.savefig(p); plt.close(); print("titled & saved")
except ImportError:
    print("pip install matplotlib")'''),
        ("Make two side-by-side subplots.", "plt.subplots(1,2).",
         r'''try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, tempfile, os
    fig, (a, b) = plt.subplots(1, 2)
    a.plot([1, 2, 3]); b.bar(["x", "y"], [1, 2])
    p = os.path.join(tempfile.gettempdir(), "sub.png")
    fig.savefig(p); plt.close(fig); print("saved subplots")
except ImportError:
    print("pip install matplotlib")'''),
    ],
}

CONTENT["seaborn"] = {
    "deps": ["seaborn"],
    "what": (
        "**Seaborn** is a high-level statistical visualization library built on matplotlib. It makes "
        "attractive, informative plots with one line — histograms with KDE, box/violin plots, "
        "scatter plots with regression lines, and **correlation heatmaps** — and works directly with "
        "pandas DataFrames. It handles styling and color palettes for you."
    ),
    "why": (
        "Seaborn turns common statistical charts into one-liners and looks great by default, so it's "
        "the fastest way to explore relationships and distributions during EDA without fiddling with "
        "matplotlib boilerplate."
    ),
    "concepts": [
        ("Built on matplotlib", "Returns matplotlib Axes you can further tweak."),
        ("DataFrame-aware", "Pass `data=df` and column names to x/y/hue."),
        ("histplot / kdeplot", "Distribution of a single variable."),
        ("boxplot / violinplot", "Compare distributions across categories."),
        ("scatterplot / regplot", "Relationships, optionally with a fitted line."),
        ("heatmap", "Visualize a matrix (e.g. correlations) with color."),
    ],
    "examples": [
        ("Distribution plot (histogram + KDE)", r'''
try:
    import matplotlib
    matplotlib.use("Agg")
    import seaborn as sns
    import matplotlib.pyplot as plt
    import tempfile, os, random

    random.seed(0)
    data = [random.gauss(0, 1) for _ in range(500)]

    sns.set_theme()                       # apply seaborn styling
    ax = sns.histplot(data, kde=True, bins=20)
    ax.set_title("Distribution with KDE")
    out = os.path.join(tempfile.gettempdir(), "sns_dist.png")
    plt.savefig(out, dpi=80); plt.close()
    print("saved distribution plot ->", out)
except ImportError:
    print("seaborn not installed — run: pip install seaborn")
'''),
        ("Boxplot comparing categories (with a DataFrame)", r'''
try:
    import matplotlib
    matplotlib.use("Agg")
    import seaborn as sns
    import pandas as pd
    import matplotlib.pyplot as plt
    import tempfile, os

    df = pd.DataFrame({
        "group": ["A"] * 5 + ["B"] * 5,
        "value": [1, 2, 2, 3, 4, 5, 6, 6, 7, 9],
    })
    ax = sns.boxplot(data=df, x="group", y="value")
    ax.set_title("Value by Group")
    out = os.path.join(tempfile.gettempdir(), "sns_box.png")
    plt.savefig(out, dpi=80); plt.close()
    print("saved boxplot ->", out)
except ImportError:
    print("seaborn/pandas not installed — run: pip install seaborn pandas")
'''),
        ("Correlation heatmap", r'''
try:
    import matplotlib
    matplotlib.use("Agg")
    import seaborn as sns
    import pandas as pd
    import matplotlib.pyplot as plt
    import tempfile, os

    df = pd.DataFrame({
        "height": [150, 160, 170, 180, 190],
        "weight": [50, 60, 65, 80, 90],
        "age":    [20, 25, 30, 35, 40],
    })
    corr = df.corr()                      # correlation matrix
    print("correlation matrix:\n", corr.round(2))

    ax = sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_title("Correlation Heatmap")
    out = os.path.join(tempfile.gettempdir(), "sns_heat.png")
    plt.savefig(out, dpi=80); plt.close()
    print("saved heatmap ->", out)
except ImportError:
    print("seaborn/pandas not installed — run: pip install seaborn pandas")
'''),
    ],
    "gotchas": [
        "Seaborn needs matplotlib; on headless systems set the 'Agg' backend before importing pyplot.",
        "Pass tidy/long-form DataFrames (one observation per row) for most seaborn functions.",
        "Seaborn functions return a matplotlib Axes — save/show with plt, not a seaborn call.",
        "`sns.set_theme()` changes global matplotlib styling for the rest of the session.",
        "Heatmaps need numeric matrices; call `df.corr()` (numeric columns only) first.",
    ],
    "exercises": [
        ("Plot a seaborn histogram of [1,2,2,3,3,3].", "sns.histplot.",
         r'''try:
    import matplotlib; matplotlib.use("Agg")
    import seaborn as sns, matplotlib.pyplot as plt, tempfile, os
    sns.histplot([1, 2, 2, 3, 3, 3])
    p = os.path.join(tempfile.gettempdir(), "sh.png")
    plt.savefig(p); plt.close(); print("saved")
except ImportError:
    print("pip install seaborn")'''),
        ("Apply seaborn's default theme.", "set_theme.",
         r'''try:
    import seaborn as sns
    sns.set_theme()
    print("theme applied")
except ImportError:
    print("pip install seaborn")'''),
        ("Make a boxplot of values by group from a DataFrame.", "sns.boxplot.",
         r'''try:
    import matplotlib; matplotlib.use("Agg")
    import seaborn as sns, pandas as pd, matplotlib.pyplot as plt, tempfile, os
    df = pd.DataFrame({"g": ["a", "a", "b"], "v": [1, 2, 3]})
    sns.boxplot(data=df, x="g", y="v")
    p = os.path.join(tempfile.gettempdir(), "b.png")
    plt.savefig(p); plt.close(); print("saved")
except ImportError:
    print("pip install seaborn pandas")'''),
        ("Compute a correlation matrix with pandas .corr().", "df.corr().",
         r'''try:
    import pandas as pd
    df = pd.DataFrame({"a": [1, 2, 3], "b": [2, 4, 6]})
    print(df.corr())
except ImportError:
    print("pip install pandas")'''),
        ("Draw a seaborn scatterplot of x vs y.", "sns.scatterplot.",
         r'''try:
    import matplotlib; matplotlib.use("Agg")
    import seaborn as sns, matplotlib.pyplot as plt, tempfile, os
    sns.scatterplot(x=[1, 2, 3], y=[3, 1, 2])
    p = os.path.join(tempfile.gettempdir(), "sc.png")
    plt.savefig(p); plt.close(); print("saved")
except ImportError:
    print("pip install seaborn")'''),
        ("Why does seaborn pair well with pandas? One line.", "DataFrame-aware.",
         r'''#md
Seaborn is **DataFrame-aware**: you pass `data=df` plus column names for x, y, and
hue, so it reads tidy pandas tables directly — no manual array wrangling.'''),
        ("Make a heatmap of [[1,0],[0,1]] with annotations.", "sns.heatmap(annot=True).",
         r'''try:
    import matplotlib; matplotlib.use("Agg")
    import seaborn as sns, matplotlib.pyplot as plt, tempfile, os
    sns.heatmap([[1, 0], [0, 1]], annot=True)
    p = os.path.join(tempfile.gettempdir(), "hm.png")
    plt.savefig(p); plt.close(); print("saved")
except ImportError:
    print("pip install seaborn")'''),
        ("Add a KDE curve to a seaborn histogram.", "kde=True.",
         r'''try:
    import matplotlib; matplotlib.use("Agg")
    import seaborn as sns, matplotlib.pyplot as plt, tempfile, os
    sns.histplot([1, 2, 3, 4, 5], kde=True)
    p = os.path.join(tempfile.gettempdir(), "k.png")
    plt.savefig(p); plt.close(); print("saved with kde")
except ImportError:
    print("pip install seaborn")'''),
    ],
}

CONTENT["data-preprocessing"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**Data preprocessing** transforms raw data into a clean, numeric form models can use: "
        "**scaling** features to comparable ranges (min-max or standardization), **encoding** "
        "categorical text into numbers (label or one-hot), and splitting data. Models like KNN, SVM, "
        "and neural nets are sensitive to feature scale, so preprocessing often decides whether they "
        "work at all."
    ),
    "why": (
        "'Garbage in, garbage out.' Most ML effort is data prep. Correct scaling and encoding "
        "prevent features with big numbers from dominating and let algorithms converge — frequently "
        "more impactful than the model choice."
    ),
    "concepts": [
        ("Min-max scaling", "Rescale to [0, 1]: (x − min)/(max − min)."),
        ("Standardization", "Center & scale to mean 0, std 1: (x − μ)/σ."),
        ("Label encoding", "Map categories to integers (for ordinal data/trees)."),
        ("One-hot encoding", "Each category becomes its own 0/1 column."),
        ("Fit on train only", "Learn scaling params from training data, then apply to test."),
        ("Pipelines", "Chain preprocessing + model so steps stay consistent."),
    ],
    "examples": [
        ("Min-max scaling and standardization (pure Python)", r'''
import statistics as st

data = [10, 20, 30, 40, 50]

# Min-max scaling to [0, 1]
lo, hi = min(data), max(data)
minmax = [(x - lo) / (hi - lo) for x in data]
print("min-max     :", minmax)            # [0.0, 0.25, 0.5, 0.75, 1.0]

# Standardization (z-scores): mean 0, std 1
mu = st.mean(data)
sigma = st.pstdev(data)                    # population std
standardized = [(x - mu) / sigma for x in data]
print("standardized:", [round(z, 3) for z in standardized])
print("new mean ~", round(st.mean(standardized), 6))   # ~0
'''),
        ("Label and one-hot encoding (pure Python)", r'''
colors = ["red", "green", "blue", "green", "red"]

# Label encoding: category -> integer
categories = sorted(set(colors))           # ['blue', 'green', 'red']
label_map = {c: i for i, c in enumerate(categories)}
labels = [label_map[c] for c in colors]
print("label map :", label_map)
print("encoded   :", labels)               # [2, 1, 0, 1, 2]

# One-hot encoding: each category -> its own 0/1 column
def one_hot(value):
    return [1 if value == c else 0 for c in categories]

print("one-hot 'red'  :", one_hot("red"))    # [0, 0, 1]
print("one-hot 'blue' :", one_hot("blue"))   # [1, 0, 0]
for c in colors:
    print(f"  {c:6} -> {one_hot(c)}")
'''),
        ("The same with scikit-learn", r'''
try:
    from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
    from sklearn.model_selection import train_test_split

    X = [[10], [20], [30], [40], [50]]

    scaler = StandardScaler().fit(X)       # learn mean/std
    print("standardized:\n", scaler.transform(X).ravel().round(3))

    mm = MinMaxScaler().fit(X)
    print("min-max     :", mm.transform(X).ravel())

    le = LabelEncoder()
    print("labels      :", le.fit_transform(["red", "green", "blue", "red"]))

    # Train/test split (fit scalers on train only!)
    data = list(range(10))
    train, test = train_test_split(data, test_size=0.3, random_state=0)
    print("train:", sorted(train), "test:", sorted(test))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "Fit scalers/encoders on the TRAINING set only, then transform test — fitting on all data leaks.",
        "One-hot encoding high-cardinality columns explodes dimensions; group rare categories first.",
        "Label encoding implies an ORDER (0<1<2); don't use it for unordered categories in linear models.",
        "Standardize for distance/gradient models (KNN, SVM, NN); tree models barely care about scale.",
        "Apply the SAME fitted transform to new data — re-fitting on test changes the scale.",
    ],
    "exercises": [
        ("Min-max scale [2,4,6,8] to [0,1].", "(x-min)/(max-min).",
         r'''data = [2, 4, 6, 8]
lo, hi = min(data), max(data)
print([(x - lo) / (hi - lo) for x in data])  # [0.0,0.33,0.67,1.0]'''),
        ("Standardize [1,2,3] (mean 0, std 1).", "z-score.",
         r'''import statistics as st
data = [1, 2, 3]
mu, sd = st.mean(data), st.pstdev(data)
print([round((x - mu) / sd, 3) for x in data])'''),
        ("Label-encode ['cat','dog','cat'].", "Map to ints.",
         r'''colors = ["cat", "dog", "cat"]
cats = sorted(set(colors))
m = {c: i for i, c in enumerate(cats)}
print([m[c] for c in colors])  # [0, 1, 0]'''),
        ("One-hot encode 'green' given categories [red,green,blue].", "0/1 vector.",
         r'''cats = ["red", "green", "blue"]
print([1 if "green" == c else 0 for c in cats])  # [0, 1, 0]'''),
        ("Why fit a scaler on training data only?", "Avoid leakage.",
         r'''#md
Fitting on the test set leaks information about it into training (**data leakage**),
giving over-optimistic results. Learn min/max/mean/std from **train**, then apply
the same transform to test — mimicking real deployment on unseen data.'''),
        ("Scale a new value 25 using train min=10,max=50.", "Apply learned params.",
         r'''lo, hi = 10, 50
print((25 - lo) / (hi - lo))  # 0.375'''),
        ("Split [0..9] into 70% train / 30% test sizes (counts).", "len math.",
         r'''n = 10
train = int(n * 0.7)
print("train", train, "test", n - train)  # train 7 test 3'''),
        ("Standardize, then verify the mean is ~0 for [5,10,15].", "Compute mean after.",
         r'''import statistics as st
d = [5, 10, 15]
mu, sd = st.mean(d), st.pstdev(d)
z = [(x - mu) / sd for x in d]
print(round(st.mean(z), 6))  # 0.0'''),
    ],
}

CONTENT["exploratory-data-analysis"] = {
    "deps": ["pandas"],
    "what": (
        "**Exploratory Data Analysis (EDA)** is the first look at a dataset: compute summary "
        "statistics (count, mean, min/max, quartiles), check distributions, spot missing values and "
        "outliers, and examine relationships between variables (correlation). The goal is to "
        "**understand** the data and form hypotheses before modeling."
    ),
    "why": (
        "EDA catches data-quality problems, surprising distributions, and leakage early — saving you "
        "from training models on broken data. It guides which features to engineer and which models "
        "are appropriate."
    ),
    "concepts": [
        ("Summary statistics", "count, mean, std, min, quartiles, max per column."),
        ("Distribution shape", "Symmetric, skewed, multimodal? Histograms reveal it."),
        ("Missing values", "How many, and where? Decide impute vs drop."),
        ("Outliers", "Extreme values that distort means and models."),
        ("Correlation", "Which features move together (and with the target)."),
        ("Cardinality", "How many distinct values a categorical column has."),
    ],
    "examples": [
        ("Summary statistics in pure Python", r'''
import statistics as st

ages = [23, 25, 31, 35, 41, 22, 29, 33, 60, 27]

print("count :", len(ages))
print("mean  :", round(st.mean(ages), 2))
print("median:", st.median(ages))
print("stdev :", round(st.stdev(ages), 2))
print("min   :", min(ages), " max:", max(ages))

# Quartiles (Q1, Q2, Q3)
q1, q2, q3 = st.quantiles(ages, n=4)
print(f"quartiles: Q1={q1}, Q2={q2}, Q3={q3}")
print("range :", max(ages) - min(ages))
'''),
        ("Frequency counts and a text histogram", r'''
from collections import Counter

grades = ["A", "B", "A", "C", "B", "A", "B", "D", "A", "C"]

# Value counts (cardinality + distribution of a categorical)
counts = Counter(grades)
print("counts:", dict(counts))
print("unique:", len(counts), "| most common:", counts.most_common(1)[0])

# Text histogram of a numeric column
scores = [55, 62, 71, 73, 78, 81, 85, 88, 91, 95]
print("\nscore histogram:")
for lo in range(50, 100, 10):
    n = sum(1 for s in scores if lo <= s < lo + 10)
    print(f"  {lo}-{lo+9}: {'#' * n} ({n})")
'''),
        ("EDA with pandas: describe, info, correlations", r'''
try:
    import pandas as pd

    df = pd.DataFrame({
        "age":    [25, 30, 35, 40, 45, 50],
        "income": [30, 45, 50, 65, 70, 90],   # in thousands
        "city":   ["NYC", "LA", "NYC", "SF", "LA", "SF"],
    })
    print("shape:", df.shape)
    print("\ndescribe:\n", df.describe())            # numeric summary
    print("\nmissing per column:\n", df.isna().sum())
    print("\ncity value counts:\n", df["city"].value_counts())
    print("\ncorrelation:\n", df.corr(numeric_only=True).round(3))
except ImportError:
    print("pandas not installed — run: pip install pandas")
'''),
    ],
    "gotchas": [
        "The mean hides skew and outliers — always look at median and a histogram too.",
        "Correlation only captures LINEAR relationships; a 0 correlation can still hide a curve.",
        "Don't impute or drop missing values before understanding WHY they're missing.",
        "High-cardinality categoricals (IDs, names) usually aren't useful features as-is.",
        "Quantile methods differ (inclusive vs exclusive) — small datasets give slightly different quartiles.",
    ],
    "exercises": [
        ("Compute mean, median, min, max of [4,8,6,2,10].", "statistics + builtins.",
         r'''import statistics as st
d = [4, 8, 6, 2, 10]
print(st.mean(d), st.median(d), min(d), max(d))'''),
        ("Find the range (max-min) of [12,5,9,20,3].", "max - min.",
         r'''d = [12, 5, 9, 20, 3]
print(max(d) - min(d))  # 17'''),
        ("Count the distinct values in ['x','y','x','z'].", "set length.",
         r'''print(len(set(["x", "y", "x", "z"])))  # 3'''),
        ("Compute the quartiles of [1,2,3,4,5,6,7,8].", "statistics.quantiles.",
         r'''import statistics as st
print(st.quantiles([1, 2, 3, 4, 5, 6, 7, 8], n=4))'''),
        ("Get value counts of ['a','b','a','a','b'].", "Counter.",
         r'''from collections import Counter
print(dict(Counter(["a", "b", "a", "a", "b"])))  # {'a':3,'b':2}'''),
        ("Find the most common grade in ['A','B','A','C','A'].", "most_common.",
         r'''from collections import Counter
print(Counter(["A", "B", "A", "C", "A"]).most_common(1)[0][0])  # A'''),
        ("Compute the standard deviation of [2,4,4,4,5,5,7,9].", "pstdev.",
         r'''import statistics as st
print(st.pstdev([2, 4, 4, 4, 5, 5, 7, 9]))  # 2.0'''),
        ("Why look at the median in addition to the mean?", "Robustness.",
         r'''#md
The **median** is robust to outliers and skew, while the **mean** gets dragged
toward extreme values. Comparing them reveals skew: if mean >> median, the data
has a long right tail (a few large values).'''),
    ],
}

CONTENT["feature-engineering"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**Feature engineering** creates better input variables from raw data so models can learn "
        "more easily: deriving new columns (ratios, differences, date parts), **binning** continuous "
        "values, **polynomial/interaction** terms, encoding categoricals, and transforming skewed "
        "features (log). Good features often beat fancier algorithms."
    ),
    "why": (
        "Models can only use the signal you expose. Thoughtful features (e.g. 'price per square "
        "foot' instead of price and area separately) inject domain knowledge and frequently produce "
        "the biggest accuracy gains in practical ML."
    ),
    "concepts": [
        ("Derived features", "Combine columns: ratios, sums, differences, rates."),
        ("Date/time parts", "Extract year, month, day-of-week, is_weekend."),
        ("Binning", "Bucket a continuous variable into ranges/categories."),
        ("Polynomial & interaction", "x², x·y capture non-linear effects."),
        ("Log transform", "Compress skewed/heavy-tailed features."),
        ("Aggregations", "Group-level stats (mean per category) as features."),
    ],
    "examples": [
        ("Deriving and transforming features (pure Python)", r'''
import math

houses = [
    {"price": 300_000, "area": 1500, "rooms": 3},
    {"price": 500_000, "area": 2000, "rooms": 4},
    {"price": 250_000, "area": 1000, "rooms": 2},
]

for h in houses:
    h["price_per_sqft"] = round(h["price"] / h["area"], 2)   # ratio feature
    h["area_per_room"] = round(h["area"] / h["rooms"], 1)
    h["log_price"] = round(math.log(h["price"]), 3)          # tame skew

for h in houses:
    print(h)
'''),
        ("Binning and date features", r'''
from datetime import date

# Binning ages into categories
def age_bucket(age):
    if age < 18:  return "minor"
    if age < 65:  return "adult"
    return "senior"

for a in [10, 25, 40, 70]:
    print(f"age {a:2} -> {age_bucket(a)}")

# Date-derived features
events = [date(2026, 1, 1), date(2026, 7, 4), date(2026, 12, 25)]
for d in events:
    print(f"{d}: month={d.month}, weekday={d.strftime('%A')}, "
          f"is_weekend={d.weekday() >= 5}")
'''),
        ("Polynomial features and scaling with scikit-learn", r'''
try:
    from sklearn.preprocessing import PolynomialFeatures, StandardScaler
    from sklearn.pipeline import make_pipeline

    X = [[2], [3], [4]]

    # Expand x into [1, x, x^2]
    poly = PolynomialFeatures(degree=2)
    print("polynomial features:\n", poly.fit_transform(X))

    # Chain transforms in a pipeline (kept consistent on new data)
    pipe = make_pipeline(PolynomialFeatures(2), StandardScaler())
    out = pipe.fit_transform(X)
    print("\npoly + standardized:\n", out.round(3))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "Don't engineer features using the target in a leaky way (e.g. target mean of the same row).",
        "Compute group aggregates on TRAIN folds only, or you leak test information.",
        "Polynomial expansion explodes dimensions fast — degree 3 on many features is huge.",
        "Log transforms need positive values; shift by a constant if zeros/negatives appear.",
        "More features isn't always better — irrelevant ones add noise and overfitting risk.",
    ],
    "exercises": [
        ("Create a 'bmi' feature from weight=70kg, height=1.75m.", "weight / height^2.",
         r'''weight, height = 70, 1.75
print(round(weight / height ** 2, 2))  # 22.86'''),
        ("Compute price_per_unit for price=120, units=4.", "Ratio.",
         r'''print(120 / 4)  # 30.0'''),
        ("Bin score 85 into 'low'(<60),'mid'(<80),'high'.", "If/elif.",
         r'''def bucket(s):
    return "low" if s < 60 else "mid" if s < 80 else "high"
print(bucket(85))  # high'''),
        ("Extract the weekday name from date(2026,6,9).", "strftime.",
         r'''from datetime import date
print(date(2026, 6, 9).strftime("%A"))  # Tuesday'''),
        ("Log-transform the value 1000.", "math.log.",
         r'''import math
print(round(math.log(1000), 3))  # 6.908'''),
        ("Create an interaction feature x*y for x=3,y=4.", "Multiply.",
         r'''x, y = 3, 4
print(x * y)  # 12'''),
        ("Make an is_weekend flag for date(2026,6,13) (a Saturday).", "weekday()>=5.",
         r'''from datetime import date
print(date(2026, 6, 13).weekday() >= 5)  # True'''),
        ("Square the feature 5 to capture a non-linear effect.", "x**2.",
         r'''print(5 ** 2)  # 25'''),
    ],
}

CONTENT["missing-data-and-outliers"] = {
    "deps": ["pandas"],
    "what": (
        "Real data has holes and extremes. **Missing data** (NaN/None) must be handled by "
        "**dropping** rows/columns or **imputing** (filling with mean/median/mode or a model). "
        "**Outliers** are values far from the rest; detect them with the **IQR rule** (outside "
        "Q1−1.5·IQR or Q3+1.5·IQR) or **z-scores** (|z| > 3), then decide to keep, cap, or remove."
    ),
    "why": (
        "Missing values crash many algorithms, and outliers distort means, scaling, and model fits. "
        "Handling them well is essential to trustworthy analysis — and how you handle them can change "
        "your conclusions."
    ),
    "concepts": [
        ("Detect missing", "Find None/NaN before doing math on a column."),
        ("Drop", "Remove rows/columns with missing values (simple, can lose data)."),
        ("Impute", "Fill missing with mean/median/mode or a predicted value."),
        ("IQR rule", "Outlier if below Q1−1.5·IQR or above Q3+1.5·IQR."),
        ("Z-score rule", "Outlier if |(x−μ)/σ| exceeds ~3."),
        ("Cap (winsorize)", "Clip extremes to a threshold instead of deleting."),
    ],
    "examples": [
        ("Detecting and imputing missing values (pure Python)", r'''
import statistics as st

data = [10, 20, None, 40, None, 60]

# Detect
missing = [i for i, x in enumerate(data) if x is None]
print("missing at indices:", missing)        # [2, 4]

present = [x for x in data if x is not None]

# Impute with the mean
mean_val = st.mean(present)
mean_filled = [mean_val if x is None else x for x in data]
print("mean-imputed  :", mean_filled)

# Impute with the median (robust to outliers)
median_val = st.median(present)
median_filled = [median_val if x is None else x for x in data]
print("median-imputed:", median_filled)
'''),
        ("Outlier detection with the IQR rule", r'''
import statistics as st

data = [10, 12, 12, 13, 12, 11, 14, 13, 100]   # 100 is suspicious

q1, q2, q3 = st.quantiles(data, n=4)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print(f"Q1={q1}, Q3={q3}, IQR={iqr}")
print(f"normal range: [{lower}, {upper}]")

outliers = [x for x in data if x < lower or x > upper]
clean = [x for x in data if lower <= x <= upper]
print("outliers:", outliers)                  # [100]
print("clean   :", clean)
'''),
        ("Z-score outliers and capping; pandas version", r'''
import statistics as st

data = [50, 52, 49, 51, 53, 120]
mu, sigma = st.mean(data), st.pstdev(data)

# Z-score rule: |z| > 2 flagged here (use 3 for larger data)
z_outliers = [x for x in data if abs((x - mu) / sigma) > 2]
print("z-score outliers:", z_outliers)        # [120]

# Capping (winsorize) to the 5th/95th percentile-ish bounds
lo, hi = min(data[:-1]), 60
capped = [min(max(x, lo), hi) for x in data]
print("capped:", capped)

try:
    import pandas as pd
    import numpy as np
    s = pd.Series([1, 2, np.nan, 4])
    print("\npandas missing count:", int(s.isna().sum()))
    print("filled with mean:\n", s.fillna(s.mean()).tolist())
except ImportError:
    print("pandas not installed — run: pip install pandas")
'''),
    ],
    "gotchas": [
        "Imputing with the MEAN is skewed by outliers — the median is usually safer.",
        "Dropping rows with any NaN can throw away most of your data; check how much you lose.",
        "Not every outlier is an error — some are the most important signal (fraud, failures).",
        "Impute using TRAINING statistics only; using test stats leaks information.",
        "NaN != NaN in floats; test with `math.isnan`/`pd.isna`, not `== None`, for float columns.",
    ],
    "exercises": [
        ("Count the missing (None) values in [1,None,3,None,5].", "Sum a condition.",
         r'''data = [1, None, 3, None, 5]
print(sum(1 for x in data if x is None))  # 2'''),
        ("Impute missing with the mean of present values in [2,None,4].", "Mean of [2,4].",
         r'''import statistics as st
data = [2, None, 4]
present = [x for x in data if x is not None]
m = st.mean(present)
print([m if x is None else x for x in data])  # [2, 3, 4]'''),
        ("Compute the IQR of [1,2,3,4,5,6,7,8].", "Q3 - Q1.",
         r'''import statistics as st
q1, _, q3 = st.quantiles([1, 2, 3, 4, 5, 6, 7, 8], n=4)
print(q3 - q1)'''),
        ("Flag outliers in [10,11,12,13,90] with the IQR rule.", "Outside fences.",
         r'''import statistics as st
d = [10, 11, 12, 13, 90]
q1, _, q3 = st.quantiles(d, n=4); iqr = q3 - q1
lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print([x for x in d if x < lo or x > hi])  # [90]'''),
        ("Impute with the median of [5,None,7,9].", "Robust fill.",
         r'''import statistics as st
data = [5, None, 7, 9]
present = [x for x in data if x is not None]
med = st.median(present)
print([med if x is None else x for x in data])'''),
        ("Cap the value 150 to a max of 100.", "min(x, cap).",
         r'''print(min(150, 100))  # 100'''),
        ("Compute the z-score of 90 in data mean=50,std=20.", "(x-mu)/sigma.",
         r'''print((90 - 50) / 20)  # 2.0'''),
        ("Drop all None values from [1,None,2,None,3].", "List comprehension.",
         r'''data = [1, None, 2, None, 3]
print([x for x in data if x is not None])  # [1, 2, 3]'''),
    ],
}

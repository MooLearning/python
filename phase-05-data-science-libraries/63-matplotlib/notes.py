# ======================================================================
# 63 — Matplotlib  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: matplotlib
# Install:  pip install matplotlib

# ----------------------------------------------------------------------
# Example 1: A line plot saved to a file (headless-safe)
# ----------------------------------------------------------------------
print("\n--- Example 1: A line plot saved to a file (headless-safe) ---")
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

# ----------------------------------------------------------------------
# Example 2: Bar chart and scatter plot
# ----------------------------------------------------------------------
print("\n--- Example 2: Bar chart and scatter plot ---")
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

# ----------------------------------------------------------------------
# Example 3: Histogram and subplots
# ----------------------------------------------------------------------
print("\n--- Example 3: Histogram and subplots ---")
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

print("\nDone! Tip: change values above and run again to learn by experiment.")

# ======================================================================
# 64 — Seaborn  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: seaborn
# Install:  pip install seaborn

# ----------------------------------------------------------------------
# Example 1: Distribution plot (histogram + KDE)
# ----------------------------------------------------------------------
print("\n--- Example 1: Distribution plot (histogram + KDE) ---")
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

# ----------------------------------------------------------------------
# Example 2: Boxplot comparing categories (with a DataFrame)
# ----------------------------------------------------------------------
print("\n--- Example 2: Boxplot comparing categories (with a DataFrame) ---")
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

# ----------------------------------------------------------------------
# Example 3: Correlation heatmap
# ----------------------------------------------------------------------
print("\n--- Example 3: Correlation heatmap ---")
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

print("\nDone! Tip: change values above and run again to learn by experiment.")

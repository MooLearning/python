# 64 — Seaborn: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Plot a seaborn histogram of [1,2,2,3,3,3].

*Hint: sns.histplot.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import matplotlib; matplotlib.use("Agg")
    import seaborn as sns, matplotlib.pyplot as plt, tempfile, os
    sns.histplot([1, 2, 2, 3, 3, 3])
    p = os.path.join(tempfile.gettempdir(), "sh.png")
    plt.savefig(p); plt.close(); print("saved")
except ImportError:
    print("pip install seaborn")
```

</details>

## Exercise 2

Apply seaborn's default theme.

*Hint: set_theme.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import seaborn as sns
    sns.set_theme()
    print("theme applied")
except ImportError:
    print("pip install seaborn")
```

</details>

## Exercise 3

Make a boxplot of values by group from a DataFrame.

*Hint: sns.boxplot.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import matplotlib; matplotlib.use("Agg")
    import seaborn as sns, pandas as pd, matplotlib.pyplot as plt, tempfile, os
    df = pd.DataFrame({"g": ["a", "a", "b"], "v": [1, 2, 3]})
    sns.boxplot(data=df, x="g", y="v")
    p = os.path.join(tempfile.gettempdir(), "b.png")
    plt.savefig(p); plt.close(); print("saved")
except ImportError:
    print("pip install seaborn pandas")
```

</details>

## Exercise 4

Compute a correlation matrix with pandas .corr().

*Hint: df.corr().*

<details>
<summary>✅ Solution</summary>

```python
try:
    import pandas as pd
    df = pd.DataFrame({"a": [1, 2, 3], "b": [2, 4, 6]})
    print(df.corr())
except ImportError:
    print("pip install pandas")
```

</details>

## Exercise 5

Draw a seaborn scatterplot of x vs y.

*Hint: sns.scatterplot.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import matplotlib; matplotlib.use("Agg")
    import seaborn as sns, matplotlib.pyplot as plt, tempfile, os
    sns.scatterplot(x=[1, 2, 3], y=[3, 1, 2])
    p = os.path.join(tempfile.gettempdir(), "sc.png")
    plt.savefig(p); plt.close(); print("saved")
except ImportError:
    print("pip install seaborn")
```

</details>

## Exercise 6

Why does seaborn pair well with pandas? One line.

*Hint: DataFrame-aware.*

<details>
<summary>✅ Solution</summary>

Seaborn is **DataFrame-aware**: you pass `data=df` plus column names for x, y, and
hue, so it reads tidy pandas tables directly — no manual array wrangling.

</details>

## Exercise 7

Make a heatmap of [[1,0],[0,1]] with annotations.

*Hint: sns.heatmap(annot=True).*

<details>
<summary>✅ Solution</summary>

```python
try:
    import matplotlib; matplotlib.use("Agg")
    import seaborn as sns, matplotlib.pyplot as plt, tempfile, os
    sns.heatmap([[1, 0], [0, 1]], annot=True)
    p = os.path.join(tempfile.gettempdir(), "hm.png")
    plt.savefig(p); plt.close(); print("saved")
except ImportError:
    print("pip install seaborn")
```

</details>

## Exercise 8

Add a KDE curve to a seaborn histogram.

*Hint: kde=True.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import matplotlib; matplotlib.use("Agg")
    import seaborn as sns, matplotlib.pyplot as plt, tempfile, os
    sns.histplot([1, 2, 3, 4, 5], kde=True)
    p = os.path.join(tempfile.gettempdir(), "k.png")
    plt.savefig(p); plt.close(); print("saved with kde")
except ImportError:
    print("pip install seaborn")
```

</details>


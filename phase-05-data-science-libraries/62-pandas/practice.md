# 62 — pandas: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Create a DataFrame with columns 'x'=[1,2,3] and 'y'=[4,5,6].

*Hint: Dict of lists.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import pandas as pd
    print(pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]}))
except ImportError:
    print("pip install pandas")
```

</details>

## Exercise 2

Select only the 'x' column from that frame.

*Hint: df['x'].*

<details>
<summary>✅ Solution</summary>

```python
try:
    import pandas as pd
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    print(df["x"].tolist())  # [1, 2, 3]
except ImportError:
    print("pip install pandas")
```

</details>

## Exercise 3

Filter rows where x > 1.

*Hint: Boolean mask.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import pandas as pd
    df = pd.DataFrame({"x": [1, 2, 3]})
    print(df[df["x"] > 1])
except ImportError:
    print("pip install pandas")
```

</details>

## Exercise 4

Add a column z = x + y.

*Hint: Vectorized column math.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import pandas as pd
    df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
    df["z"] = df["x"] + df["y"]
    print(df)
except ImportError:
    print("pip install pandas")
```

</details>

## Exercise 5

Compute the mean of column 'age'=[20,30,40].

*Hint: Series.mean.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import pandas as pd
    print(pd.Series([20, 30, 40]).mean())  # 30.0
except ImportError:
    print("pip install pandas")
```

</details>

## Exercise 6

Group [('a',1),('a',2),('b',3)] by letter and sum values.

*Hint: groupby.sum.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import pandas as pd
    df = pd.DataFrame({"k": ["a", "a", "b"], "v": [1, 2, 3]})
    print(df.groupby("k")["v"].sum())
except ImportError:
    print("pip install pandas")
```

</details>

## Exercise 7

Sort a frame by 'score' descending.

*Hint: sort_values.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import pandas as pd
    df = pd.DataFrame({"score": [3, 1, 2]})
    print(df.sort_values("score", ascending=False))
except ImportError:
    print("pip install pandas")
```

</details>

## Exercise 8

Count missing values per column in a frame with a NaN.

*Hint: isna().sum().*

<details>
<summary>✅ Solution</summary>

```python
try:
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a": [1, np.nan, 3]})
    print(df.isna().sum())
except ImportError:
    print("pip install pandas numpy")
```

</details>


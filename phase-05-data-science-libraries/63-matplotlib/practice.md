# 63 — Matplotlib: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Plot y=[1,4,9] vs x=[1,2,3] and save it.

*Hint: plt.plot + savefig.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, tempfile, os
    plt.plot([1, 2, 3], [1, 4, 9])
    p = os.path.join(tempfile.gettempdir(), "ex.png")
    plt.savefig(p); plt.close(); print("saved", p)
except ImportError:
    print("pip install matplotlib")
```

</details>

## Exercise 2

Make a bar chart of {'a':3,'b':5}.

*Hint: plt.bar.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, tempfile, os
    plt.bar(["a", "b"], [3, 5])
    p = os.path.join(tempfile.gettempdir(), "bar.png")
    plt.savefig(p); plt.close(); print("saved", p)
except ImportError:
    print("pip install matplotlib")
```

</details>

## Exercise 3

Add an x-axis label 'time' to a plot.

*Hint: plt.xlabel.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, tempfile, os
    plt.plot([1, 2], [3, 4]); plt.xlabel("time")
    p = os.path.join(tempfile.gettempdir(), "lab.png")
    plt.savefig(p); plt.close(); print("labeled & saved")
except ImportError:
    print("pip install matplotlib")
```

</details>

## Exercise 4

Plot a histogram of [1,1,2,3,3,3].

*Hint: plt.hist.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, tempfile, os
    plt.hist([1, 1, 2, 3, 3, 3], bins=3)
    p = os.path.join(tempfile.gettempdir(), "h.png")
    plt.savefig(p); plt.close(); print("saved hist")
except ImportError:
    print("pip install matplotlib")
```

</details>

## Exercise 5

Why call matplotlib.use('Agg')? Explain in one line.

*Hint: Headless rendering.*

<details>
<summary>✅ Solution</summary>

The **'Agg'** backend renders plots to image files **without needing a display/GUI**
— essential on servers, CI, and scripts. Set it *before* importing pyplot.

</details>

## Exercise 6

Create a scatter of x=[1,2,3], y=[3,2,1].

*Hint: plt.scatter.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, tempfile, os
    plt.scatter([1, 2, 3], [3, 2, 1])
    p = os.path.join(tempfile.gettempdir(), "s.png")
    plt.savefig(p); plt.close(); print("saved scatter")
except ImportError:
    print("pip install matplotlib")
```

</details>

## Exercise 7

Add a title 'Sales' to a plot.

*Hint: plt.title.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, tempfile, os
    plt.plot([1, 2, 3]); plt.title("Sales")
    p = os.path.join(tempfile.gettempdir(), "t.png")
    plt.savefig(p); plt.close(); print("titled & saved")
except ImportError:
    print("pip install matplotlib")
```

</details>

## Exercise 8

Make two side-by-side subplots.

*Hint: plt.subplots(1,2).*

<details>
<summary>✅ Solution</summary>

```python
try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt, tempfile, os
    fig, (a, b) = plt.subplots(1, 2)
    a.plot([1, 2, 3]); b.bar(["x", "y"], [1, 2])
    p = os.path.join(tempfile.gettempdir(), "sub.png")
    fig.savefig(p); plt.close(fig); print("saved subplots")
except ImportError:
    print("pip install matplotlib")
```

</details>


# 61 — NumPy: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Create an array [1,2,3] and multiply every element by 10.

*Hint: Vectorized.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import numpy as np
    print(np.array([1, 2, 3]) * 10)  # [10 20 30]
except ImportError:
    print("pip install numpy")
```

</details>

## Exercise 2

Make a 3x3 array of zeros.

*Hint: np.zeros with a shape tuple.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import numpy as np
    print(np.zeros((3, 3)))
except ImportError:
    print("pip install numpy")
```

</details>

## Exercise 3

Select all elements > 3 from [1,4,2,5,3].

*Hint: Boolean mask.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import numpy as np
    a = np.array([1, 4, 2, 5, 3])
    print(a[a > 3])  # [4 5]
except ImportError:
    print("pip install numpy")
```

</details>

## Exercise 4

Compute the mean of each column of [[1,2],[3,4]].

*Hint: axis=0.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import numpy as np
    print(np.array([[1, 2], [3, 4]]).mean(axis=0))  # [2. 3.]
except ImportError:
    print("pip install numpy")
```

</details>

## Exercise 5

Reshape np.arange(6) into 2 rows, 3 cols.

*Hint: reshape(2,3).*

<details>
<summary>✅ Solution</summary>

```python
try:
    import numpy as np
    print(np.arange(6).reshape(2, 3))
except ImportError:
    print("pip install numpy")
```

</details>

## Exercise 6

Create 5 evenly spaced numbers from 0 to 1.

*Hint: linspace.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import numpy as np
    print(np.linspace(0, 1, 5))
except ImportError:
    print("pip install numpy")
```

</details>

## Exercise 7

Add the vector [1,0,1] to every row of a 2x3 ones array.

*Hint: Broadcasting.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import numpy as np
    print(np.ones((2, 3)) + np.array([1, 0, 1]))
except ImportError:
    print("pip install numpy")
```

</details>

## Exercise 8

Compute the dot product of [1,2] and [3,4].

*Hint: np.dot.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import numpy as np
    print(np.dot([1, 2], [3, 4]))  # 11
except ImportError:
    print("pip install numpy")
```

</details>


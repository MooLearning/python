# ======================================================================
# 61 — NumPy  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: numpy
# Install:  pip install numpy

# ----------------------------------------------------------------------
# Example 1: Creating arrays and vectorized math
# ----------------------------------------------------------------------
print("\n--- Example 1: Creating arrays and vectorized math ---")
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

# ----------------------------------------------------------------------
# Example 2: Indexing, slicing, boolean masks, 2D arrays
# ----------------------------------------------------------------------
print("\n--- Example 2: Indexing, slicing, boolean masks, 2D arrays ---")
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

# ----------------------------------------------------------------------
# Example 3: Aggregations, axes, broadcasting, reshape
# ----------------------------------------------------------------------
print("\n--- Example 3: Aggregations, axes, broadcasting, reshape ---")
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

print("\nDone! Tip: change values above and run again to learn by experiment.")

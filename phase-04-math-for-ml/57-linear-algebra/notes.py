# ======================================================================
# 57 — Linear Algebra  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Vectors: add, scale, dot product, magnitude
# ----------------------------------------------------------------------
print("\n--- Example 1: Vectors: add, scale, dot product, magnitude ---")
import math

def add(u, v):       return [a + b for a, b in zip(u, v)]
def scale(k, v):     return [k * x for x in v]
def dot(u, v):       return sum(a * b for a, b in zip(u, v))
def magnitude(v):    return math.sqrt(dot(v, v))

u = [1, 2, 3]
v = [4, 5, 6]
print("u + v   :", add(u, v))        # [5, 7, 9]
print("3 * u   :", scale(3, u))      # [3, 6, 9]
print("u . v   :", dot(u, v))        # 32  (1*4 + 2*5 + 3*6)
print("|u|     :", round(magnitude(u), 4))   # 3.7417

# Cosine similarity = dot / (|u| * |v|)  -> how aligned two vectors are
cos_sim = dot(u, v) / (magnitude(u) * magnitude(v))
print("cos_sim :", round(cos_sim, 4))        # 0.9746

# ----------------------------------------------------------------------
# Example 2: Matrices: transpose and multiply (pure Python)
# ----------------------------------------------------------------------
print("\n--- Example 2: Matrices: transpose and multiply (pure Python) ---")
def transpose(M):
    # swap rows and columns
    return [[M[r][c] for r in range(len(M))] for c in range(len(M[0]))]

def matmul(A, B):
    # A is (m x n), B is (n x p) -> result is (m x p)
    n = len(B)
    assert len(A[0]) == n, "inner dimensions must match"
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(len(B[0]))]
            for i in range(len(A))]

A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]
print("A^T   :", transpose(A))   # [[1, 3], [2, 4]]
print("A x B :", matmul(A, B))   # [[19, 22], [43, 50]]

# Matrix-vector product: treat the vector as a column
v = [[1], [1]]
print("A x v :", matmul(A, v))   # [[3], [7]]

# ----------------------------------------------------------------------
# Example 3: The same with NumPy (if installed)
# ----------------------------------------------------------------------
print("\n--- Example 3: The same with NumPy (if installed) ---")
try:
    import numpy as np
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print("shapes:", A.shape, B.shape)
    print("A @ B =\n", A @ B)              # matrix multiply
    print("A.T   =\n", A.T)                # transpose
    print("dot   :", np.dot([1, 2, 3], [4, 5, 6]))   # 32

    # Solve a linear system  A x = b
    Acoef = np.array([[2.0, 1.0], [1.0, 3.0]])
    b = np.array([5.0, 10.0])
    x = np.linalg.solve(Acoef, b)
    print("solution x:", np.round(x, 3))   # [1. 3.]
except ImportError:
    print("NumPy not installed — run: pip install numpy")
    print("(the pure-Python examples above already show the same math)")

print("\nDone! Tip: change values above and run again to learn by experiment.")

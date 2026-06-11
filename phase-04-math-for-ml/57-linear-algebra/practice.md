# 57 — Linear Algebra: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute the dot product of [1,2,3] and [4,5,6].

*Hint: Sum of products.*

<details>
<summary>✅ Solution</summary>

```python
def dot(u, v):
    return sum(a * b for a, b in zip(u, v))
print(dot([1, 2, 3], [4, 5, 6]))  # 32
```

</details>

## Exercise 2

Add the vectors [1,1] and [2,3].

*Hint: Elementwise.*

<details>
<summary>✅ Solution</summary>

```python
def add(u, v):
    return [a + b for a, b in zip(u, v)]
print(add([1, 1], [2, 3]))  # [3, 4]
```

</details>

## Exercise 3

Find the magnitude (length) of [3,4].

*Hint: sqrt of sum of squares.*

<details>
<summary>✅ Solution</summary>

```python
import math
v = [3, 4]
print(math.sqrt(sum(x * x for x in v)))  # 5.0
```

</details>

## Exercise 4

Transpose the matrix [[1,2,3],[4,5,6]].

*Hint: Rows become columns.*

<details>
<summary>✅ Solution</summary>

```python
M = [[1, 2, 3], [4, 5, 6]]
T = [[M[r][c] for r in range(len(M))] for c in range(len(M[0]))]
print(T)  # [[1,4],[2,5],[3,6]]
```

</details>

## Exercise 5

Multiply [[1,0],[0,1]] (identity) by [[5,6],[7,8]].

*Hint: Identity returns the matrix.*

<details>
<summary>✅ Solution</summary>

```python
def matmul(A, B):
    n = len(B)
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(len(B[0]))] for i in range(len(A))]
print(matmul([[1, 0], [0, 1]], [[5, 6], [7, 8]]))  # [[5,6],[7,8]]
```

</details>

## Exercise 6

Scale the vector [1,2,3] by 0.5.

*Hint: Multiply each element.*

<details>
<summary>✅ Solution</summary>

```python
v = [1, 2, 3]
print([0.5 * x for x in v])  # [0.5, 1.0, 1.5]
```

</details>

## Exercise 7

Compute cosine similarity between [1,0] and [0,1].

*Hint: Orthogonal -> 0.*

<details>
<summary>✅ Solution</summary>

```python
import math
def dot(u, v): return sum(a * b for a, b in zip(u, v))
def mag(v): return math.sqrt(dot(v, v))
u, v = [1, 0], [0, 1]
print(dot(u, v) / (mag(u) * mag(v)))  # 0.0
```

</details>

## Exercise 8

Multiply matrix [[1,2],[3,4]] by column vector [[1],[1]].

*Hint: (2x2)x(2x1)->(2x1).*

<details>
<summary>✅ Solution</summary>

```python
def matmul(A, B):
    n = len(B)
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(len(B[0]))] for i in range(len(A))]
print(matmul([[1, 2], [3, 4]], [[1], [1]]))  # [[3],[7]]
```

</details>


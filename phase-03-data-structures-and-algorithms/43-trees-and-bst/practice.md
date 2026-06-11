# 43 — Trees and BST: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Create a TreeNode class and build root=10 with children 5 and 15.

*Hint: left/right attrs.*

<details>
<summary>✅ Solution</summary>

```python
class TreeNode:
    def __init__(self, v): self.value = v; self.left = None; self.right = None
root = TreeNode(10)
root.left = TreeNode(5); root.right = TreeNode(15)
print(root.left.value, root.right.value)  # 5 15
```

</details>

## Exercise 2

Insert [4,2,6,1,3] into a BST and search for 3.

*Hint: Recursive insert.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def insert(root, v):
    if not root: return N(v)
    if v < root.value: root.left = insert(root.left, v)
    else: root.right = insert(root.right, v)
    return root
def search(root, v):
    while root:
        if root.value == v: return True
        root = root.left if v < root.value else root.right
    return False
r = None
for v in [4, 2, 6, 1, 3]: r = insert(r, v)
print(search(r, 3))  # True
```

</details>

## Exercise 3

Count the nodes in a binary tree recursively.

*Hint: 1 + left + right.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def count(n):
    return 0 if n is None else 1 + count(n.left) + count(n.right)
root = N(1); root.left = N(2); root.right = N(3)
print(count(root))  # 3
```

</details>

## Exercise 4

Find the height of a tree (edges on the longest root-to-leaf path).

*Hint: 1 + max(children).*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def height(n):
    return -1 if n is None else 1 + max(height(n.left), height(n.right))
root = N(1); root.left = N(2); root.left.left = N(3)
print(height(root))  # 2
```

</details>

## Exercise 5

Find the minimum value in a BST.

*Hint: Go left until None.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def insert(r, v):
    if not r: return N(v)
    if v < r.value: r.left = insert(r.left, v)
    else: r.right = insert(r.right, v)
    return r
def find_min(r):
    while r.left: r = r.left
    return r.value
r = None
for v in [5, 3, 8, 1]: r = insert(r, v)
print(find_min(r))  # 1
```

</details>

## Exercise 6

Sum all values in a binary tree.

*Hint: Recursive sum.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def tree_sum(n):
    return 0 if n is None else n.value + tree_sum(n.left) + tree_sum(n.right)
root = N(1); root.left = N(2); root.right = N(3)
print(tree_sum(root))  # 6
```

</details>

## Exercise 7

Validate whether a tree is a BST.

*Hint: Pass min/max bounds down.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def is_bst(n, lo=float("-inf"), hi=float("inf")):
    if n is None: return True
    if not (lo < n.value < hi): return False
    return is_bst(n.left, lo, n.value) and is_bst(n.right, n.value, hi)
root = N(2); root.left = N(1); root.right = N(3)
print(is_bst(root))  # True
```

</details>

## Exercise 8

Find the lowest common ancestor of 1 and 4 in a BST.

*Hint: Use the ordering.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def insert(r, v):
    if not r: return N(v)
    if v < r.value: r.left = insert(r.left, v)
    else: r.right = insert(r.right, v)
    return r
def lca(root, a, b):
    while root:
        if a < root.value and b < root.value: root = root.left
        elif a > root.value and b > root.value: root = root.right
        else: return root.value
r = None
for v in [5, 3, 8, 1, 4]: r = insert(r, v)
print(lca(r, 1, 4))  # 3
```

</details>


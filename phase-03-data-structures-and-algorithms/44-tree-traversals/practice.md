# 44 — Tree Traversals: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Pre-order traverse a tree root=1,left=2,right=3.

*Hint: Node, left, right.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
root = N(1); root.left = N(2); root.right = N(3)
def pre(n, out):
    if n: out.append(n.value); pre(n.left, out); pre(n.right, out)
o = []; pre(root, o); print(o)  # [1, 2, 3]
```

</details>

## Exercise 2

In-order traverse the same tree.

*Hint: Left, node, right.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
root = N(2); root.left = N(1); root.right = N(3)
def ino(n, out):
    if n: ino(n.left, out); out.append(n.value); ino(n.right, out)
o = []; ino(root, o); print(o)  # [1, 2, 3]
```

</details>

## Exercise 3

Post-order traverse a tree.

*Hint: Left, right, node.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
root = N(1); root.left = N(2); root.right = N(3)
def post(n, out):
    if n: post(n.left, out); post(n.right, out); out.append(n.value)
o = []; post(root, o); print(o)  # [2, 3, 1]
```

</details>

## Exercise 4

Level-order traverse into a flat list.

*Hint: Queue + popleft.*

<details>
<summary>✅ Solution</summary>

```python
from collections import deque
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
root = N(1); root.left = N(2); root.right = N(3)
def bfs(r):
    out, q = [], deque([r])
    while q:
        n = q.popleft(); out.append(n.value)
        if n.left: q.append(n.left)
        if n.right: q.append(n.right)
    return out
print(bfs(root))  # [1, 2, 3]
```

</details>

## Exercise 5

Count leaf nodes (no children) in a tree.

*Hint: Both children None.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def leaves(n):
    if n is None: return 0
    if not n.left and not n.right: return 1
    return leaves(n.left) + leaves(n.right)
root = N(1); root.left = N(2); root.right = N(3)
print(leaves(root))  # 2
```

</details>

## Exercise 6

Find the maximum depth (number of levels) of a tree.

*Hint: 1 + max child depth.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def depth(n):
    return 0 if n is None else 1 + max(depth(n.left), depth(n.right))
root = N(1); root.left = N(2); root.left.left = N(3)
print(depth(root))  # 3
```

</details>

## Exercise 7

Return the right-side view (rightmost node per level).

*Hint: BFS, take last per level.*

<details>
<summary>✅ Solution</summary>

```python
from collections import deque
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def right_view(root):
    if not root: return []
    out, q = [], deque([root])
    while q:
        n = len(q)
        for i in range(n):
            node = q.popleft()
            if i == n - 1: out.append(node.value)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return out
r = N(1); r.left = N(2); r.right = N(3); r.left.left = N(4)
print(right_view(r))  # [1, 3, 4]
```

</details>

## Exercise 8

Reconstruct in-order WITHOUT recursion using a stack.

*Hint: Push lefts, pop, go right.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def inorder_iter(root):
    out, stack, cur = [], [], root
    while stack or cur:
        while cur:
            stack.append(cur); cur = cur.left
        cur = stack.pop(); out.append(cur.value); cur = cur.right
    return out
r = N(2); r.left = N(1); r.right = N(3)
print(inorder_iter(r))  # [1, 2, 3]
```

</details>


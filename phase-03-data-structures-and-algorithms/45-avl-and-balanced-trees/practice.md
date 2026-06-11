# 45 — AVL and Balanced Trees: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute the balance factor of a node given left height 2, right height 0.

*Hint: left - right.*

<details>
<summary>✅ Solution</summary>

```python
left_h, right_h = 2, 0
print(left_h - right_h)  # 2  -> unbalanced (needs rotation)
```

</details>

## Exercise 2

Show a skewed BST's height for sorted inserts [1,2,3,4].

*Hint: Each goes right.*

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
def height(n):
    return -1 if n is None else 1 + max(height(n.left), height(n.right))
r = None
for v in [1, 2, 3, 4]: r = insert(r, v)
print(height(r))  # 3 (a stick)
```

</details>

## Exercise 3

Implement a right rotation on three nodes.

*Hint: Promote the left child.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def rotate_right(y):
    x = y.left; y.left = x.right; x.right = y
    return x
y = N(3); y.left = N(2); y.left.left = N(1)
new_root = rotate_right(y)
print(new_root.value)  # 2
```

</details>

## Exercise 4

Implement a left rotation on three nodes.

*Hint: Promote the right child.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def rotate_left(x):
    y = x.right; x.right = y.left; y.left = x
    return y
x = N(1); x.right = N(2); x.right.right = N(3)
new_root = rotate_left(x)
print(new_root.value)  # 2
```

</details>

## Exercise 5

Decide which rotation an LL imbalance needs.

*Hint: Heavy on left-left.*

<details>
<summary>✅ Solution</summary>

An **LL** case (inserted into the left subtree's left side) is fixed with a single
**right rotation** at the unbalanced node.

</details>

## Exercise 6

Check if a tree is height-balanced (|bf| ≤ 1 everywhere).

*Hint: Recurse heights.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v): self.value = v; self.left = self.right = None
def check(n):
    if n is None: return 0, True
    lh, lb = check(n.left); rh, rb = check(n.right)
    bal = lb and rb and abs(lh - rh) <= 1
    return 1 + max(lh, rh), bal
root = N(1); root.left = N(2); root.left.left = N(3)
print(check(root)[1])  # False
```

</details>

## Exercise 7

Identify the case (LL/RR/LR/RL) when bf=-2 and the new value went left of the right child.

*Hint: Zig-zag.*

<details>
<summary>✅ Solution</summary>

bf = −2 means **right-heavy**; the value landing on the right child's **left** side
is the **RL** case → fix with a **right rotation on the right child, then a left
rotation** on the node.

</details>

## Exercise 8

Insert [10,20,30] into an AVL tree and report the new root.

*Hint: RR triggers left rotation.*

<details>
<summary>✅ Solution</summary>

```python
class N:
    def __init__(self, v):
        self.value = v; self.left = self.right = None; self.height = 1
def h(n): return n.height if n else 0
def upd(n): n.height = 1 + max(h(n.left), h(n.right))
def bf(n): return h(n.left) - h(n.right) if n else 0
def rl(x):
    y = x.right; x.right = y.left; y.left = x; upd(x); upd(y); return y
def insert(n, v):
    if not n: return N(v)
    if v < n.value: n.left = insert(n.left, v)
    else: n.right = insert(n.right, v)
    upd(n)
    if bf(n) < -1 and v > n.right.value: return rl(n)
    return n
r = None
for v in [10, 20, 30]: r = insert(r, v)
print(r.value)  # 20
```

</details>


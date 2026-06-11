# ======================================================================
# 45 — AVL and Balanced Trees  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Why an unbalanced BST is bad
# ----------------------------------------------------------------------
print("\n--- Example 1: Why an unbalanced BST is bad ---")
class N:
    def __init__(self, v): self.value = v; self.left = None; self.right = None

def insert(root, v):
    if root is None: return N(v)
    if v < root.value: root.left = insert(root.left, v)
    else: root.right = insert(root.right, v)
    return root

def height(n):
    return -1 if n is None else 1 + max(height(n.left), height(n.right))

# Inserting SORTED data makes a right-leaning 'stick'
root = None
for v in [1, 2, 3, 4, 5]:
    root = insert(root, v)
print("height of skewed tree:", height(root))   # 4 -> O(n), not O(log n)!
# A balanced tree of 5 nodes would have height 2.

# ----------------------------------------------------------------------
# Example 2: A self-balancing AVL tree
# ----------------------------------------------------------------------
print("\n--- Example 2: A self-balancing AVL tree ---")
class N:
    def __init__(self, v):
        self.value = v; self.left = None; self.right = None; self.height = 1

def h(n):       return n.height if n else 0
def balance(n): return h(n.left) - h(n.right) if n else 0
def update(n):  n.height = 1 + max(h(n.left), h(n.right))

def rotate_right(y):
    x = y.left; y.left = x.right; x.right = y
    update(y); update(x)
    return x

def rotate_left(x):
    y = x.right; x.right = y.left; y.left = x
    update(x); update(y)
    return y

def insert(node, v):
    if node is None:
        return N(v)
    if v < node.value: node.left = insert(node.left, v)
    else:              node.right = insert(node.right, v)
    update(node)
    bf = balance(node)
    if bf > 1 and v < node.left.value:                 # LL
        return rotate_right(node)
    if bf < -1 and v > node.right.value:               # RR
        return rotate_left(node)
    if bf > 1 and v > node.left.value:                 # LR
        node.left = rotate_left(node.left); return rotate_right(node)
    if bf < -1 and v < node.right.value:               # RL
        node.right = rotate_right(node.right); return rotate_left(node)
    return node

root = None
for v in [1, 2, 3, 4, 5]:        # same sorted data as before
    root = insert(root, v)
print("AVL root:", root.value)   # 2  (rebalanced!)
print("AVL height:", root.height)   # 3 levels -> stays ~log n

# ----------------------------------------------------------------------
# Example 3: Verify the tree stays balanced
# ----------------------------------------------------------------------
print("\n--- Example 3: Verify the tree stays balanced ---")
class N:
    def __init__(self, v):
        self.value = v; self.left = None; self.right = None; self.height = 1

def h(n): return n.height if n else 0
def update(n): n.height = 1 + max(h(n.left), h(n.right))
def balance(n): return h(n.left) - h(n.right) if n else 0

def rot_r(y):
    x = y.left; y.left = x.right; x.right = y; update(y); update(x); return x
def rot_l(x):
    y = x.right; x.right = y.left; y.left = x; update(x); update(y); return y

def insert(node, v):
    if node is None: return N(v)
    if v < node.value: node.left = insert(node.left, v)
    else: node.right = insert(node.right, v)
    update(node); bf = balance(node)
    if bf > 1 and v < node.left.value: return rot_r(node)
    if bf < -1 and v > node.right.value: return rot_l(node)
    if bf > 1 and v > node.left.value:
        node.left = rot_l(node.left); return rot_r(node)
    if bf < -1 and v < node.right.value:
        node.right = rot_r(node.right); return rot_l(node)
    return node

def is_balanced(n):
    if n is None: return True
    return abs(balance(n)) <= 1 and is_balanced(n.left) and is_balanced(n.right)

root = None
for v in range(1, 16):          # 15 sorted inserts
    root = insert(root, v)
print("balanced?", is_balanced(root))   # True
print("height   :", h(root))            # 4 (log2(15) ~ 3.9)

print("\nDone! Tip: change values above and run again to learn by experiment.")

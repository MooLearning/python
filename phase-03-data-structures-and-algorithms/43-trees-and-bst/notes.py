# ======================================================================
# 43 — Trees and BST  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: A BST with insert and search
# ----------------------------------------------------------------------
print("\n--- Example 1: A BST with insert and search ---")
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)        # found the spot
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node                       # duplicates ignored

    def search(self, value):
        node = self.root
        while node:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False

bst = BST()
for v in [5, 3, 8, 1, 4, 7, 9]:
    bst.insert(v)
print(bst.search(7))    # True
print(bst.search(6))    # False

# ----------------------------------------------------------------------
# Example 2: In-order traversal of a BST yields sorted order
# ----------------------------------------------------------------------
print("\n--- Example 2: In-order traversal of a BST yields sorted order ---")
class TreeNode:
    def __init__(self, v): self.value = v; self.left = None; self.right = None

def insert(root, v):
    if root is None: return TreeNode(v)
    if v < root.value: root.left = insert(root.left, v)
    else: root.right = insert(root.right, v)
    return root

def in_order(node, out):
    if node:
        in_order(node.left, out)    # left
        out.append(node.value)      # node
        in_order(node.right, out)   # right

root = None
for v in [5, 3, 8, 1, 4, 7, 9]:
    root = insert(root, v)
result = []
in_order(root, result)
print(result)   # [1, 3, 4, 5, 7, 8, 9] -> SORTED!

# ----------------------------------------------------------------------
# Example 3: Height, node count, and min/max of a BST
# ----------------------------------------------------------------------
print("\n--- Example 3: Height, node count, and min/max of a BST ---")
class TreeNode:
    def __init__(self, v): self.value = v; self.left = None; self.right = None

def insert(root, v):
    if root is None: return TreeNode(v)
    if v < root.value: root.left = insert(root.left, v)
    else: root.right = insert(root.right, v)
    return root

def height(node):
    if node is None:
        return -1                       # empty tree has height -1
    return 1 + max(height(node.left), height(node.right))

def count(node):
    if node is None:
        return 0
    return 1 + count(node.left) + count(node.right)

def find_min(node):
    while node.left:                    # smallest is leftmost
        node = node.left
    return node.value

root = None
for v in [5, 3, 8, 1, 4, 7, 9]:
    root = insert(root, v)
print("height:", height(root))   # 2
print("nodes :", count(root))    # 7
print("min   :", find_min(root)) # 1

print("\nDone! Tip: change values above and run again to learn by experiment.")

# ======================================================================
# 34 — Linked Lists  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: A singly linked list class
# ----------------------------------------------------------------------
print("\n--- Example 1: A singly linked list class ---")
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):           # add to the end -> O(n)
        node = Node(value)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def to_list(self):                 # for easy printing
        out, cur = [], self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out

ll = LinkedList()
for x in [1, 2, 3]:
    ll.append(x)
print(ll.to_list())     # [1, 2, 3]

# ----------------------------------------------------------------------
# Example 2: Prepend, search, and delete by value
# ----------------------------------------------------------------------
print("\n--- Example 2: Prepend, search, and delete by value ---")
class Node:
    def __init__(self, v): self.value = v; self.next = None

class LinkedList:
    def __init__(self): self.head = None
    def prepend(self, v):              # add to front -> O(1)
        node = Node(v); node.next = self.head; self.head = node
    def find(self, v):                 # O(n) search
        cur = self.head
        while cur:
            if cur.value == v: return True
            cur = cur.next
        return False
    def delete(self, v):               # remove first node with value v
        if self.head and self.head.value == v:
            self.head = self.head.next; return
        cur = self.head
        while cur and cur.next:
            if cur.next.value == v:
                cur.next = cur.next.next; return
            cur = cur.next
    def to_list(self):
        out, cur = [], self.head
        while cur: out.append(cur.value); cur = cur.next
        return out

ll = LinkedList()
for x in [3, 2, 1]: ll.prepend(x)
print(ll.to_list())     # [1, 2, 3]
print(ll.find(2))       # True
ll.delete(2)
print(ll.to_list())     # [1, 3]

# ----------------------------------------------------------------------
# Example 3: Reverse a linked list and detect a cycle
# ----------------------------------------------------------------------
print("\n--- Example 3: Reverse a linked list and detect a cycle ---")
class Node:
    def __init__(self, v): self.value = v; self.next = None

def build(values):
    head = None
    for v in reversed(values):
        n = Node(v); n.next = head; head = n
    return head

def reverse(head):
    prev = None
    while head:
        nxt = head.next     # save next
        head.next = prev    # flip the pointer
        prev = head         # advance prev
        head = nxt          # advance head
    return prev

def to_list(head):
    out = []
    while head: out.append(head.value); head = head.next
    return out

h = build([1, 2, 3, 4])
print(to_list(reverse(h)))   # [4, 3, 2, 1]

def has_cycle(head):         # Floyd's tortoise and hare
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

a = Node(1); b = Node(2); c = Node(3)
a.next = b; b.next = c; c.next = b   # cycle!
print(has_cycle(a))          # True

print("\nDone! Tip: change values above and run again to learn by experiment.")

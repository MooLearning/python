# 34 — Linked Lists: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Build a Node class and link three nodes 1->2->3, then print all values.

*Hint: node.next chaining.*

<details>
<summary>✅ Solution</summary>

```python
class Node:
    def __init__(self, v): self.value = v; self.next = None
a = Node(1); a.next = Node(2); a.next.next = Node(3)
cur = a
while cur: print(cur.value, end=" "); cur = cur.next
print()
```

</details>

## Exercise 2

Count the number of nodes in a linked list.

*Hint: Traverse and tally.*

<details>
<summary>✅ Solution</summary>

```python
class Node:
    def __init__(self, v): self.value = v; self.next = None
def length(head):
    n = 0
    while head: n += 1; head = head.next
    return n
a = Node(1); a.next = Node(2)
print(length(a))  # 2
```

</details>

## Exercise 3

Find the maximum value in a linked list.

*Hint: Traverse tracking max.*

<details>
<summary>✅ Solution</summary>

```python
class Node:
    def __init__(self, v): self.value = v; self.next = None
def max_val(head):
    best = head.value
    while head:
        best = max(best, head.value); head = head.next
    return best
a = Node(3); a.next = Node(9); a.next.next = Node(1)
print(max_val(a))  # 9
```

</details>

## Exercise 4

Reverse a linked list iteratively.

*Hint: Three pointers.*

<details>
<summary>✅ Solution</summary>

```python
class Node:
    def __init__(self, v): self.value = v; self.next = None
def reverse(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev
a = Node(1); a.next = Node(2); a.next.next = Node(3)
r = reverse(a)
while r: print(r.value, end=" "); r = r.next
print()  # 3 2 1
```

</details>

## Exercise 5

Find the middle node using fast/slow pointers (return its value).

*Hint: Hare moves twice as fast.*

<details>
<summary>✅ Solution</summary>

```python
class Node:
    def __init__(self, v): self.value = v; self.next = None
def middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next; fast = fast.next.next
    return slow.value
h = Node(1); h.next = Node(2); h.next.next = Node(3)
print(middle(h))  # 2
```

</details>

## Exercise 6

Detect whether a linked list has a cycle.

*Hint: Floyd's algorithm.*

<details>
<summary>✅ Solution</summary>

```python
class Node:
    def __init__(self, v): self.value = v; self.next = None
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast: return True
    return False
a = Node(1); b = Node(2); a.next = b; b.next = a
print(has_cycle(a))  # True
```

</details>

## Exercise 7

Get the nth value from the end (n=1 is last).

*Hint: Two pointers k apart.*

<details>
<summary>✅ Solution</summary>

```python
class Node:
    def __init__(self, v): self.value = v; self.next = None
def nth_from_end(head, n):
    lead = head
    for _ in range(n): lead = lead.next
    while lead:
        lead = lead.next; head = head.next
    return head.value
h = Node(1); h.next = Node(2); h.next.next = Node(3)
print(nth_from_end(h, 1))  # 3
```

</details>

## Exercise 8

Merge two sorted linked lists into one sorted list (return values).

*Hint: Compare heads.*

<details>
<summary>✅ Solution</summary>

```python
class Node:
    def __init__(self, v): self.value = v; self.next = None
def build(vals):
    head = None
    for v in reversed(vals):
        n = Node(v); n.next = head; head = n
    return head
def merge(a, b):
    dummy = tail = Node(0)
    while a and b:
        if a.value <= b.value: tail.next, a = a, a.next
        else: tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    out = []
    cur = dummy.next
    while cur: out.append(cur.value); cur = cur.next
    return out
print(merge(build([1, 3, 5]), build([2, 4])))  # [1,2,3,4,5]
```

</details>


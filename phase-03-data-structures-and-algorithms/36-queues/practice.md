# 36 — Queues: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Create a queue with deque, enqueue 1,2,3, then dequeue once.

*Hint: append + popleft.*

<details>
<summary>✅ Solution</summary>

```python
from collections import deque
q = deque([1, 2, 3])
print(q.popleft())  # 1
print(list(q))      # [2, 3]
```

</details>

## Exercise 2

Why is list.pop(0) a bad queue? State the complexity.

*Hint: Front removal shifts.*

<details>
<summary>✅ Solution</summary>

`list.pop(0)` is **O(n)** because every remaining element shifts left one slot.
`deque.popleft()` is **O(1)**.

</details>

## Exercise 3

Use a deque as a double-ended queue: add to both ends.

*Hint: appendleft/append.*

<details>
<summary>✅ Solution</summary>

```python
from collections import deque
d = deque([1])
d.appendleft(0)   # front
d.append(2)       # rear
print(list(d))    # [0, 1, 2]
```

</details>

## Exercise 4

Reverse the first k=2 elements of a queue [1,2,3,4].

*Hint: Stack + queue.*

<details>
<summary>✅ Solution</summary>

```python
from collections import deque
def reverse_first_k(q, k):
    stack = [q.popleft() for _ in range(k)]
    for _ in range(k): q.appendleft(stack[_])  # noqa
    return q
q = deque([1, 2, 3, 4])
print(list(reverse_first_k(q, 2)))  # [2, 1, 3, 4]
```

</details>

## Exercise 5

Implement a queue using two stacks.

*Hint: Amortized O(1) dequeue.*

<details>
<summary>✅ Solution</summary>

```python
class QueueTwoStacks:
    def __init__(self):
        self.inb = []; self.out = []
    def enqueue(self, x):
        self.inb.append(x)
    def dequeue(self):
        if not self.out:
            while self.inb:
                self.out.append(self.inb.pop())
        return self.out.pop()
q = QueueTwoStacks()
q.enqueue(1); q.enqueue(2); q.enqueue(3)
print(q.dequeue(), q.dequeue())  # 1 2
```

</details>

## Exercise 6

Generate binary numbers 1..5 as strings using a queue.

*Hint: BFS-style generation.*

<details>
<summary>✅ Solution</summary>

```python
from collections import deque
def binaries(n):
    out, q = [], deque(["1"])
    for _ in range(n):
        cur = q.popleft()
        out.append(cur)
        q.append(cur + "0"); q.append(cur + "1")
    return out
print(binaries(5))  # ['1','10','11','100','101']
```

</details>

## Exercise 7

Find the first non-repeating char in a stream 'aabc' at each step.

*Hint: Queue of candidates.*

<details>
<summary>✅ Solution</summary>

```python
from collections import deque, Counter
def stream_first_unique(s):
    counts = Counter(); q = deque(); res = []
    for ch in s:
        counts[ch] += 1; q.append(ch)
        while q and counts[q[0]] > 1:
            q.popleft()
        res.append(q[0] if q else "#")
    return res
print(stream_first_unique("aabc"))  # ['a','#','b','b']
```

</details>

## Exercise 8

Simulate a circular queue of capacity 3: enqueue 1,2,3,4 (4 should fail).

*Hint: Track size vs capacity.*

<details>
<summary>✅ Solution</summary>

```python
from collections import deque
class CircularQueue:
    def __init__(self, cap):
        self.q = deque(); self.cap = cap
    def enqueue(self, x):
        if len(self.q) >= self.cap: return False
        self.q.append(x); return True
cq = CircularQueue(3)
print([cq.enqueue(x) for x in [1, 2, 3, 4]])  # [True, True, True, False]
```

</details>


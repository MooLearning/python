# 24 — Context Managers: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Use 'with' to write 'hello' to a file and confirm it is closed afterward.

*Hint: f.closed.*

<details>
<summary>✅ Solution</summary>

```python
import os
with open("h.txt", "w", encoding="utf-8") as f:
    f.write("hello")
print(f.closed)  # True
os.remove("h.txt")
```

</details>

## Exercise 2

Write a context manager class that prints 'enter' and 'exit' around a block.

*Hint: __enter__/__exit__.*

<details>
<summary>✅ Solution</summary>

```python
class CM:
    def __enter__(self): print("enter"); return self
    def __exit__(self, *a): print("exit")
with CM():
    print("inside")
```

</details>

## Exercise 3

Use @contextmanager to make a manager that yields the string 'resource'.

*Hint: yield value.*

<details>
<summary>✅ Solution</summary>

```python
from contextlib import contextmanager
@contextmanager
def res():
    yield "resource"
with res() as r:
    print(r)  # resource
```

</details>

## Exercise 4

Make a Timer context manager that prints elapsed time for a block.

*Hint: time.perf_counter.*

<details>
<summary>✅ Solution</summary>

```python
import time
from contextlib import contextmanager
@contextmanager
def timer():
    s = time.perf_counter()
    yield
    print(f"{(time.perf_counter()-s)*1000:.1f} ms")
with timer():
    sum(range(100000))
```

</details>

## Exercise 5

Ensure cleanup runs even if the block raises (use try/finally in @contextmanager).

*Hint: finally.*

<details>
<summary>✅ Solution</summary>

```python
from contextlib import contextmanager
@contextmanager
def guard():
    try:
        yield
    finally:
        print("cleanup")
try:
    with guard():
        raise ValueError("boom")
except ValueError:
    print("caught")
```

</details>

## Exercise 6

Use contextlib.suppress to ignore a FileNotFoundError.

*Hint: suppress.*

<details>
<summary>✅ Solution</summary>

```python
from contextlib import suppress
import os
with suppress(FileNotFoundError):
    os.remove("not_here.txt")
print("done")
```

</details>

## Exercise 7

Open two files in a single with statement.

*Hint: with a, b:.*

<details>
<summary>✅ Solution</summary>

```python
import os
with open("a.txt", "w") as a, open("b.txt", "w") as b:
    a.write("A"); b.write("B")
print("written")
os.remove("a.txt"); os.remove("b.txt")
```

</details>

## Exercise 8

Write a manager that temporarily appends to a list and removes the item on exit.

*Hint: Mutate then undo.*

<details>
<summary>✅ Solution</summary>

```python
from contextlib import contextmanager
@contextmanager
def temp_item(lst, item):
    lst.append(item)
    try:
        yield lst
    finally:
        lst.remove(item)
data = [1, 2]
with temp_item(data, 99) as d:
    print(d)  # [1, 2, 99]
print(data)   # [1, 2]
```

</details>


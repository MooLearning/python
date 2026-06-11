# 29 — Multithreading and Multiprocessing: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Use ThreadPoolExecutor.map to square [1,2,3,4] concurrently.

*Hint: pool.map.*

<details>
<summary>✅ Solution</summary>

```python
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor() as p:
    print(list(p.map(lambda x: x * x, [1, 2, 3, 4])))  # [1,4,9,16]
```

</details>

## Exercise 2

Run a function in a single thread and join it.

*Hint: threading.Thread.*

<details>
<summary>✅ Solution</summary>

```python
import threading
def task(): print("working")
t = threading.Thread(target=task)
t.start(); t.join()
```

</details>

## Exercise 3

Decide: would you use threads or processes for downloading 50 files? Why?

<details>
<summary>✅ Solution</summary>

**Threads.** Downloading is **I/O-bound** (mostly waiting on the network), so the
GIL is released during the wait and many threads overlap their waiting. Processes
would add overhead for no benefit here.

</details>

## Exercise 4

Decide: threads or processes for multiplying huge matrices? Why?

<details>
<summary>✅ Solution</summary>

**Processes.** That's **CPU-bound** work. The GIL prevents threads from running
Python bytecode in parallel, so only processes (separate interpreters) use
multiple cores.

</details>

## Exercise 5

Protect a shared counter with a Lock across two threads.

*Hint: with lock.*

<details>
<summary>✅ Solution</summary>

```python
import threading
n, lock = 0, threading.Lock()
def add():
    global n
    for _ in range(10000):
        with lock: n += 1
ts = [threading.Thread(target=add) for _ in range(2)]
[t.start() for t in ts]; [t.join() for t in ts]
print(n)  # 20000
```

</details>

## Exercise 6

Use ProcessPoolExecutor to compute squares of [1,2,3] (guard with __main__).

*Hint: ProcessPool.*

<details>
<summary>✅ Solution</summary>

```python
from concurrent.futures import ProcessPoolExecutor
def sq(x): return x * x
if __name__ == "__main__":
    with ProcessPoolExecutor() as p:
        print(list(p.map(sq, [1, 2, 3])))  # [1, 4, 9]
```

</details>

## Exercise 7

Submit a single task with executor.submit and get its result via future.result().

*Hint: submit.*

<details>
<summary>✅ Solution</summary>

```python
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor() as p:
    fut = p.submit(pow, 2, 10)
    print(fut.result())  # 1024
```

</details>

## Exercise 8

Time how much faster 4 concurrent 0.1s sleeps are vs sequential.

*Hint: Compare timings.*

<details>
<summary>✅ Solution</summary>

```python
import time
from concurrent.futures import ThreadPoolExecutor
def wait(_): time.sleep(0.1)
s = time.perf_counter()
with ThreadPoolExecutor(4) as p: list(p.map(wait, range(4)))
print(f"~{time.perf_counter()-s:.2f}s (≈0.1, not 0.4)")
```

</details>


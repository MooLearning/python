# ======================================================================
# 29 — Multithreading and Multiprocessing  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Threads for I/O-bound work (ThreadPoolExecutor)
# ----------------------------------------------------------------------
print("\n--- Example 1: Threads for I/O-bound work (ThreadPoolExecutor) ---")
import time
from concurrent.futures import ThreadPoolExecutor

def fake_download(url):
    time.sleep(0.2)                 # pretend we're waiting on the network
    return f"{url} -> 200"

urls = [f"site{i}.com" for i in range(5)]

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(fake_download, urls))   # run concurrently
print(results)
print(f"threaded: {time.perf_counter() - start:.2f}s (≈0.2s, not 1.0s)")

# ----------------------------------------------------------------------
# Example 2: Processes for CPU-bound work (ProcessPoolExecutor)
# ----------------------------------------------------------------------
print("\n--- Example 2: Processes for CPU-bound work (ProcessPoolExecutor) ---")
from concurrent.futures import ProcessPoolExecutor

def heavy(n):
    return sum(i * i for i in range(n))   # pure CPU work

if __name__ == "__main__":          # required guard for multiprocessing
    tasks = [200_000, 200_000, 200_000, 200_000]
    with ProcessPoolExecutor() as pool:
        results = list(pool.map(heavy, tasks))
    print("sums:", results[0], "(x4)")
    print("Processes use multiple CPU cores, sidestepping the GIL.")

# ----------------------------------------------------------------------
# Example 3: Threads + a Lock to avoid race conditions
# ----------------------------------------------------------------------
print("\n--- Example 3: Threads + a Lock to avoid race conditions ---")
import threading

counter = 0
lock = threading.Lock()

def increment_many():
    global counter
    for _ in range(100_000):
        with lock:                  # only one thread updates at a time
            counter += 1

threads = [threading.Thread(target=increment_many) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()          # wait for all to finish
print("counter:", counter)          # 400000 (correct, thanks to the lock)

print("\nDone! Tip: change values above and run again to learn by experiment.")

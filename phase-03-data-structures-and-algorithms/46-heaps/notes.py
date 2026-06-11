# ======================================================================
# 46 — Heaps  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: heapq basics: push, pop, peek, heapify
# ----------------------------------------------------------------------
print("\n--- Example 1: heapq basics: push, pop, peek, heapify ---")
import heapq

h = []
for x in [5, 3, 8, 1, 9, 2]:
    heapq.heappush(h, x)         # O(log n) each
print("min (peek):", h[0])       # 1  -> root is always the smallest
print("pop:", heapq.heappop(h))  # 1
print("pop:", heapq.heappop(h))  # 2

# Build a heap from a list in O(n)
data = [9, 4, 7, 1, 2, 6]
heapq.heapify(data)
print("heapified:", data)        # [1, 2, 6, 9, 4, 7] (heap order)
print("3 smallest:", heapq.nsmallest(3, [9, 4, 7, 1, 2, 6]))   # [1, 2, 4]
print("3 largest :", heapq.nlargest(3, [9, 4, 7, 1, 2, 6]))    # [9, 7, 6]

# ----------------------------------------------------------------------
# Example 2: Priority queue with (priority, task) tuples
# ----------------------------------------------------------------------
print("\n--- Example 2: Priority queue with (priority, task) tuples ---")
import heapq

pq = []
heapq.heappush(pq, (2, "write tests"))
heapq.heappush(pq, (1, "fix bug"))        # lower number = higher priority
heapq.heappush(pq, (3, "deploy"))
heapq.heappush(pq, (1, "security patch"))

while pq:
    priority, task = heapq.heappop(pq)
    print(f"[p{priority}] {task}")
# fix bug, security patch (both p1, tie-broken by text), then p2, p3

# ----------------------------------------------------------------------
# Example 3: Max-heap and k-th largest
# ----------------------------------------------------------------------
print("\n--- Example 3: Max-heap and k-th largest ---")
import heapq

# Python only has a MIN-heap; negate values for a max-heap
nums = [5, 3, 8, 1, 9, 2]
max_heap = [-x for x in nums]
heapq.heapify(max_heap)
print("max:", -heapq.heappop(max_heap))   # 9

# k-th largest using a size-k min-heap (efficient, O(n log k))
def kth_largest(arr, k):
    h = arr[:k]
    heapq.heapify(h)
    for x in arr[k:]:
        if x > h[0]:                # bigger than the smallest of our top-k
            heapq.heapreplace(h, x) # pop smallest, push x
    return h[0]

print("2nd largest:", kth_largest([3, 2, 1, 5, 6, 4], 2))   # 5

print("\nDone! Tip: change values above and run again to learn by experiment.")

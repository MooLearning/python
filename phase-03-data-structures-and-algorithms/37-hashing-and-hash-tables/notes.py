# ======================================================================
# 37 — Hashing and Hash Tables  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: dict and set as hash tables
# ----------------------------------------------------------------------
print("\n--- Example 1: dict and set as hash tables ---")
# dict: O(1) average insert, lookup, delete
phone = {"alice": 123, "bob": 456}
phone["carol"] = 789
print(phone["bob"])          # 456  -> O(1)
print("alice" in phone)      # True -> O(1) key check
print(phone.get("dave", -1)) # -1   -> default if missing

# set: membership in O(1) (vs O(n) for a list)
seen = set()
for x in [1, 2, 2, 3, 1]:
    if x in seen:
        print("duplicate:", x)
    seen.add(x)
print("unique:", seen)       # {1, 2, 3}

# ----------------------------------------------------------------------
# Example 2: Build a hash table from scratch (chaining)
# ----------------------------------------------------------------------
print("\n--- Example 2: Build a hash table from scratch (chaining) ---")
class HashTable:
    def __init__(self, size=8):
        self.size = size
        self.buckets = [[] for _ in range(size)]   # each bucket is a list

    def _index(self, key):
        return hash(key) % self.size               # hash -> bucket index

    def put(self, key, value):
        bucket = self.buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:                           # update existing
                bucket[i] = (key, value)
                return
        bucket.append((key, value))                # insert new

    def get(self, key, default=None):
        for k, v in self.buckets[self._index(key)]:
            if k == key:
                return v
        return default

ht = HashTable()
ht.put("apple", 3)
ht.put("banana", 5)
ht.put("apple", 9)            # updates
print(ht.get("apple"))       # 9
print(ht.get("banana"))      # 5
print(ht.get("cherry", 0))   # 0

# ----------------------------------------------------------------------
# Example 3: Counting and grouping with hashing
# ----------------------------------------------------------------------
print("\n--- Example 3: Counting and grouping with hashing ---")
from collections import Counter, defaultdict

words = "the cat sat on the mat the cat".split()

# Count frequencies in O(n)
print(Counter(words))        # {'the': 3, 'cat': 2, ...}

# Group words by their length using a dict of lists
groups = defaultdict(list)
for w in words:
    groups[len(w)].append(w)
print(dict(groups))          # {3: ['the','cat','sat',...]}

# Two-sum: find indices that add to target — O(n) with a hash map
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return (seen[target - n], i)
        seen[n] = i
    return None
print(two_sum([2, 7, 11, 15], 9))   # (0, 1)

print("\nDone! Tip: change values above and run again to learn by experiment.")

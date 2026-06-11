# 37 — Hashing and Hash Tables: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Count how many times each char appears in 'banana' using a dict.

*Hint: get with default.*

<details>
<summary>✅ Solution</summary>

```python
counts = {}
for c in "banana":
    counts[c] = counts.get(c, 0) + 1
print(counts)  # {'b':1,'a':3,'n':2}
```

</details>

## Exercise 2

Use a set to remove duplicates from [1,2,2,3,3,3].

*Hint: set() then list.*

<details>
<summary>✅ Solution</summary>

```python
print(sorted(set([1, 2, 2, 3, 3, 3])))  # [1, 2, 3]
```

</details>

## Exercise 3

Check if two strings are anagrams using a frequency dict.

*Hint: Compare counts.*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
print(Counter("listen") == Counter("silent"))  # True
```

</details>

## Exercise 4

Find the first repeated element in [3,1,4,1,5].

*Hint: Track seen in a set.*

<details>
<summary>✅ Solution</summary>

```python
def first_repeat(a):
    seen = set()
    for x in a:
        if x in seen: return x
        seen.add(x)
    return None
print(first_repeat([3, 1, 4, 1, 5]))  # 1
```

</details>

## Exercise 5

Implement two-sum: return indices summing to 6 in [1,4,5,2].

*Hint: Complement in a map.*

<details>
<summary>✅ Solution</summary>

```python
def two_sum(a, t):
    seen = {}
    for i, x in enumerate(a):
        if t - x in seen: return (seen[t - x], i)
        seen[x] = i
print(two_sum([1, 4, 5, 2], 6))  # (1, 4)? -> (1, 2)
```

</details>

## Exercise 6

Group ['eat','tea','tan','ate'] into anagram groups.

*Hint: Sorted word as key.*

<details>
<summary>✅ Solution</summary>

```python
from collections import defaultdict
def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups["".join(sorted(w))].append(w)
    return list(groups.values())
print(group_anagrams(["eat", "tea", "tan", "ate"]))
# [['eat','tea','ate'], ['tan']]
```

</details>

## Exercise 7

Find the element appearing more than n/2 times in [2,2,1,2,3].

*Hint: Count then check.*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
def majority(a):
    c = Counter(a)
    for k, v in c.items():
        if v > len(a) // 2: return k
print(majority([2, 2, 1, 2, 3]))  # 2
```

</details>

## Exercise 8

Build a tiny LRU-ish cache: keep only the last 2 distinct keys inserted.

*Hint: dict order.*

<details>
<summary>✅ Solution</summary>

```python
def make_cache(limit=2):
    store = {}
    def put(k, v):
        if k in store: del store[k]
        store[k] = v
        while len(store) > limit:
            oldest = next(iter(store))
            del store[oldest]
    return store, put
store, put = make_cache()
for k, v in [("a",1),("b",2),("c",3)]: put(k, v)
print(list(store))  # ['b', 'c']
```

</details>


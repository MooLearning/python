# 33 — String Algorithms: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Reverse the string 'algorithms' without slicing.

*Hint: Build from the end.*

<details>
<summary>✅ Solution</summary>

```python
def rev(s):
    out = []
    for c in s:
        out.insert(0, c)
    return "".join(out)
print(rev("algorithms"))  # smhtirogla
```

</details>

## Exercise 2

Count vowels in 'Encyclopedia'.

*Hint: Membership in 'aeiou'.*

<details>
<summary>✅ Solution</summary>

```python
s = "Encyclopedia"
print(sum(1 for c in s.lower() if c in "aeiou"))  # 5
```

</details>

## Exercise 3

Check if 'Dormitory' and 'Dirty Room' are anagrams (ignore case/space).

*Hint: Counter.*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
def anag(a, b):
    norm = lambda x: Counter(x.replace(" ", "").lower())
    return norm(a) == norm(b)
print(anag("Dormitory", "Dirty Room"))  # True
```

</details>

## Exercise 4

Return the most frequent character in 'mississippi'.

*Hint: Counter.most_common.*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
print(Counter("mississippi").most_common(1)[0][0])  # i or s -> 's'? -> 'i
```

</details>

## Exercise 5

Find all starting indices of 'ana' in 'banana'.

*Hint: Naive scan.*

<details>
<summary>✅ Solution</summary>

```python
def find(t, p):
    return [i for i in range(len(t) - len(p) + 1) if t[i:i+len(p)] == p]
print(find("banana", "ana"))  # [1, 3]
```

</details>

## Exercise 6

Compress 'aaabbc' to 'a3b2c1' (run-length encoding).

*Hint: Count consecutive runs.*

<details>
<summary>✅ Solution</summary>

```python
def rle(s):
    out, i = [], 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        out.append(f"{s[i]}{j - i}")
        i = j
    return "".join(out)
print(rle("aaabbc"))  # a3b2c1
```

</details>

## Exercise 7

Check if 'abc' is a subsequence of 'aXbYcZ'.

*Hint: Two pointers.*

<details>
<summary>✅ Solution</summary>

```python
def is_subseq(sub, s):
    it = iter(s)
    return all(c in it for c in sub)
print(is_subseq("abc", "aXbYcZ"))  # True
```

</details>

## Exercise 8

Find the longest substring without repeating characters in 'abcabcbb'.

*Hint: Sliding window.*

<details>
<summary>✅ Solution</summary>

```python
def longest_unique(s):
    seen = {}; start = best = 0
    for i, c in enumerate(s):
        if c in seen and seen[c] >= start:
            start = seen[c] + 1
        seen[c] = i
        best = max(best, i - start + 1)
    return best
print(longest_unique("abcabcbb"))  # 3
```

</details>


# 111 — DSA Practice: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Solve FizzBuzz for 1..15.

*Hint: Modulo checks.*

<details>
<summary>✅ Solution</summary>

```python
for n in range(1, 16):
    print("FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0
          else "Buzz" if n % 5 == 0 else n)
```

</details>

## Exercise 2

Reverse the string 'hello' without slicing.

*Hint: Build backward.*

<details>
<summary>✅ Solution</summary>

```python
s = "hello"; out = ""
for c in s: out = c + out
print(out)  # olleh
```

</details>

## Exercise 3

Check if 'listen'/'silent' are anagrams.

*Hint: Counter compare.*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
print(Counter("listen") == Counter("silent"))  # True
```

</details>

## Exercise 4

Find the max subarray sum of [-2,1,-3,4,-1,2,1,-5,4].

*Hint: Kadane.*

<details>
<summary>✅ Solution</summary>

```python
def kadane(a):
    best = cur = a[0]
    for x in a[1:]:
        cur = max(x, cur + x); best = max(best, cur)
    return best
print(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
```

</details>

## Exercise 5

Return True if [1,2,3,1] contains a duplicate.

*Hint: Set length.*

<details>
<summary>✅ Solution</summary>

```python
a = [1, 2, 3, 1]
print(len(set(a)) != len(a))  # True
```

</details>

## Exercise 6

Compute fibonacci(10) iteratively.

*Hint: Two vars.*

<details>
<summary>✅ Solution</summary>

```python
a, b = 0, 1
for _ in range(10): a, b = b, a + b
print(a)  # 55
```

</details>

## Exercise 7

Find the missing number in [0,1,3] (range 0..3).

*Hint: Sum formula.*

<details>
<summary>✅ Solution</summary>

```python
a = [0, 1, 3]; n = 3
print(n * (n + 1) // 2 - sum(a))  # 2
```

</details>

## Exercise 8

Merge sorted [1,3,5] and [2,4] into one sorted list.

*Hint: Two pointers.*

<details>
<summary>✅ Solution</summary>

```python
def merge(a, b):
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: out.append(a[i]); i += 1
        else: out.append(b[j]); j += 1
    return out + a[i:] + b[j:]
print(merge([1, 3, 5], [2, 4]))  # [1,2,3,4,5]
```

</details>


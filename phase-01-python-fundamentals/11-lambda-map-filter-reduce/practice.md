# 11 — Lambda, Map, Filter and Reduce: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Use map to triple every number in [1,2,3,4].

*Hint: list(map(lambda x: x*3, ...)).*

<details>
<summary>✅ Solution</summary>

```python
print(list(map(lambda x: x * 3, [1, 2, 3, 4])))  # [3, 6, 9, 12]
```

</details>

## Exercise 2

Use filter to keep words longer than 3 letters from ['hi','tree','no','code'].

*Hint: len > 3.*

<details>
<summary>✅ Solution</summary>

```python
words = ["hi", "tree", "no", "code"]
print(list(filter(lambda w: len(w) > 3, words)))  # ['tree', 'code']
```

</details>

## Exercise 3

Sort ['bb','a','ccc'] by length using sorted with a key.

*Hint: key=len.*

<details>
<summary>✅ Solution</summary>

```python
print(sorted(["bb", "a", "ccc"], key=len))  # ['a', 'bb', 'ccc']
```

</details>

## Exercise 4

Use reduce to compute the product of [2,3,4].

*Hint: functools.reduce.*

<details>
<summary>✅ Solution</summary>

```python
from functools import reduce
print(reduce(lambda a, x: a * x, [2, 3, 4]))  # 24
```

</details>

## Exercise 5

Find the person with the max age from [('A',30),('B',45)] using max and a key.

*Hint: key=lambda p: p[1].*

<details>
<summary>✅ Solution</summary>

```python
people = [("A", 30), ("B", 45)]
print(max(people, key=lambda p: p[1]))  # ('B', 45)
```

</details>

## Exercise 6

Use map to convert ['1','2','3'] to integers and sum them.

*Hint: map(int, ...).*

<details>
<summary>✅ Solution</summary>

```python
print(sum(map(int, ["1", "2", "3"])))  # 6
```

</details>

## Exercise 7

Rewrite list(map(lambda x: x+1, nums)) as a list comprehension.

*Hint: [x+1 for x in nums].*

<details>
<summary>✅ Solution</summary>

```python
nums = [10, 20, 30]
print([x + 1 for x in nums])  # [11, 21, 31]
```

</details>

## Exercise 8

Sort a list of dicts [{'n':'A','s':3},{'n':'B','s':9}] by 's' descending.

*Hint: key + reverse=True.*

<details>
<summary>✅ Solution</summary>

```python
data = [{"n": "A", "s": 3}, {"n": "B", "s": 9}]
print(sorted(data, key=lambda d: d["s"], reverse=True))
```

</details>


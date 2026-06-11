# 39 — Basic Sorts (Bubble, Selection, Insertion): Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Sort [3,1,2] with bubble sort and print it.

*Hint: Swap adjacent pairs.*

<details>
<summary>✅ Solution</summary>

```python
def bubble(a):
    a = a[:]
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
print(bubble([3, 1, 2]))  # [1, 2, 3]
```

</details>

## Exercise 2

Sort [5,3,8,1] in DESCENDING order with selection sort.

*Hint: Find the max instead.*

<details>
<summary>✅ Solution</summary>

```python
def sel_desc(a):
    a = a[:]
    for i in range(len(a)):
        mx = i
        for j in range(i + 1, len(a)):
            if a[j] > a[mx]: mx = j
        a[i], a[mx] = a[mx], a[i]
    return a
print(sel_desc([5, 3, 8, 1]))  # [8, 5, 3, 1]
```

</details>

## Exercise 3

Use insertion sort to sort ['pear','fig','apple'] alphabetically.

*Hint: Same logic, string compare.*

<details>
<summary>✅ Solution</summary>

```python
def insert_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        key = a[i]; j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]; j -= 1
        a[j + 1] = key
    return a
print(insert_sort(["pear", "fig", "apple"]))  # ['apple','fig','pear']
```

</details>

## Exercise 4

Count the number of swaps bubble sort makes on [2,1,3,1].

*Hint: Increment on each swap.*

<details>
<summary>✅ Solution</summary>

```python
def count_swaps(a):
    a = a[:]; swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]; swaps += 1
    return swaps
print(count_swaps([2, 1, 3, 1]))  # 2
```

</details>

## Exercise 5

Make insertion sort return early-sorted detection (was it already sorted?).

*Hint: Track any shift.*

<details>
<summary>✅ Solution</summary>

```python
def insert_sorted_flag(a):
    a = a[:]; moved = False
    for i in range(1, len(a)):
        key = a[i]; j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]; j -= 1; moved = True
        a[j + 1] = key
    return a, (not moved)
print(insert_sorted_flag([1, 2, 3]))  # ([1,2,3], True)
```

</details>

## Exercise 6

Sort a list of (name, age) tuples by age using insertion sort.

*Hint: Compare the second item.*

<details>
<summary>✅ Solution</summary>

```python
def by_age(people):
    a = people[:]
    for i in range(1, len(a)):
        key = a[i]; j = i - 1
        while j >= 0 and a[j][1] > key[1]:
            a[j + 1] = a[j]; j -= 1
        a[j + 1] = key
    return a
print(by_age([("ann", 30), ("bo", 20), ("cy", 25)]))
# [('bo',20),('cy',25),('ann',30)]
```

</details>

## Exercise 7

Demonstrate that selection sort is unstable with [(1,'a'),(1,'b'),(0,'c')].

*Hint: Watch equal keys.*

<details>
<summary>✅ Solution</summary>

Sorting by the first element, selection sort may swap the two `1`s out of their
original `a`,`b` order because it swaps the found minimum into place regardless of
ties — so the result can be `[(0,'c'),(1,'b'),(1,'a')]`. A **stable** sort would
keep `(1,'a')` before `(1,'b')`.

</details>

## Exercise 8

Implement a 'cocktail' (bidirectional bubble) sort on [3,1,2,5,4].

*Hint: Bubble both directions.*

<details>
<summary>✅ Solution</summary>

```python
def cocktail(a):
    a = a[:]; lo, hi = 0, len(a) - 1
    while lo < hi:
        for j in range(lo, hi):
            if a[j] > a[j + 1]: a[j], a[j + 1] = a[j + 1], a[j]
        hi -= 1
        for j in range(hi, lo, -1):
            if a[j] < a[j - 1]: a[j], a[j - 1] = a[j - 1], a[j]
        lo += 1
    return a
print(cocktail([3, 1, 2, 5, 4]))  # [1, 2, 3, 4, 5]
```

</details>


# 81 — Hierarchical Clustering: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute the distance between (0,0) and (3,4).

*Hint: Euclidean.*

<details>
<summary>✅ Solution</summary>

```python
import math
print(math.dist((0, 0), (3, 4)))  # 5.0
```

</details>

## Exercise 2

Single-linkage distance between {A,B} and {C}: min of AC,BC = min(4,3).

*Hint: Take min.*

<details>
<summary>✅ Solution</summary>

```python
print(min(4, 3))  # 3
```

</details>

## Exercise 3

Complete-linkage distance for the same: max(4,3).

*Hint: Take max.*

<details>
<summary>✅ Solution</summary>

```python
print(max(4, 3))  # 4
```

</details>

## Exercise 4

Do you need to choose k before hierarchical clustering?

*Hint: Cut later.*

<details>
<summary>✅ Solution</summary>

**No.** You build the full dendrogram first, then **cut it at a chosen height** to
get however many clusters you want — k is decided after seeing the structure.

</details>

## Exercise 5

Start with 5 points: how many merges to reach 1 cluster?

*Hint: n-1.*

<details>
<summary>✅ Solution</summary>

```python
print(5 - 1)  # 4
```

</details>

## Exercise 6

What does the height of a merge in a dendrogram represent?

*Hint: Distance.*

<details>
<summary>✅ Solution</summary>

The **distance** (dissimilarity) at which the two clusters were merged. Merges low
on the tree are very similar; high merges join dissimilar groups.

</details>

## Exercise 7

Average-linkage of distances [2,4,6] between cluster members.

*Hint: Mean.*

<details>
<summary>✅ Solution</summary>

```python
d = [2, 4, 6]
print(sum(d) / len(d))  # 4.0
```

</details>

## Exercise 8

Single linkage tends to produce what artifact?

*Hint: Chaining.*

<details>
<summary>✅ Solution</summary>

**Chaining** — clusters can stretch into long thin chains because only the single
closest pair is needed to merge, linking far-apart points through intermediates.

</details>


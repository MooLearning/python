# 65 — Data Preprocessing: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Min-max scale [2,4,6,8] to [0,1].

*Hint: (x-min)/(max-min).*

<details>
<summary>✅ Solution</summary>

```python
data = [2, 4, 6, 8]
lo, hi = min(data), max(data)
print([(x - lo) / (hi - lo) for x in data])  # [0.0,0.33,0.67,1.0]
```

</details>

## Exercise 2

Standardize [1,2,3] (mean 0, std 1).

*Hint: z-score.*

<details>
<summary>✅ Solution</summary>

```python
import statistics as st
data = [1, 2, 3]
mu, sd = st.mean(data), st.pstdev(data)
print([round((x - mu) / sd, 3) for x in data])
```

</details>

## Exercise 3

Label-encode ['cat','dog','cat'].

*Hint: Map to ints.*

<details>
<summary>✅ Solution</summary>

```python
colors = ["cat", "dog", "cat"]
cats = sorted(set(colors))
m = {c: i for i, c in enumerate(cats)}
print([m[c] for c in colors])  # [0, 1, 0]
```

</details>

## Exercise 4

One-hot encode 'green' given categories [red,green,blue].

*Hint: 0/1 vector.*

<details>
<summary>✅ Solution</summary>

```python
cats = ["red", "green", "blue"]
print([1 if "green" == c else 0 for c in cats])  # [0, 1, 0]
```

</details>

## Exercise 5

Why fit a scaler on training data only?

*Hint: Avoid leakage.*

<details>
<summary>✅ Solution</summary>

Fitting on the test set leaks information about it into training (**data leakage**),
giving over-optimistic results. Learn min/max/mean/std from **train**, then apply
the same transform to test — mimicking real deployment on unseen data.

</details>

## Exercise 6

Scale a new value 25 using train min=10,max=50.

*Hint: Apply learned params.*

<details>
<summary>✅ Solution</summary>

```python
lo, hi = 10, 50
print((25 - lo) / (hi - lo))  # 0.375
```

</details>

## Exercise 7

Split [0..9] into 70% train / 30% test sizes (counts).

*Hint: len math.*

<details>
<summary>✅ Solution</summary>

```python
n = 10
train = int(n * 0.7)
print("train", train, "test", n - train)  # train 7 test 3
```

</details>

## Exercise 8

Standardize, then verify the mean is ~0 for [5,10,15].

*Hint: Compute mean after.*

<details>
<summary>✅ Solution</summary>

```python
import statistics as st
d = [5, 10, 15]
mu, sd = st.mean(d), st.pstdev(d)
z = [(x - mu) / sd for x in d]
print(round(st.mean(z), 6))  # 0.0
```

</details>


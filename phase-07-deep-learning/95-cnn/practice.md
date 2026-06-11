# 95 — Convolutional Neural Networks (CNN): Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Output size of a 5x5 image with a 3x3 kernel (no padding)?

*Hint: in-k+1.*

<details>
<summary>✅ Solution</summary>

```python
print(5 - 3 + 1)  # 3
```

</details>

## Exercise 2

Convolve [1,2,3,4] (1-D) with kernel [1,-1]: first output.

*Hint: Dot product.*

<details>
<summary>✅ Solution</summary>

```python
img, k = [1, 2, 3, 4], [1, -1]
print(img[0] * k[0] + img[1] * k[1])  # -1
```

</details>

## Exercise 3

2x2 max-pool the block [[1,4],[3,2]].

*Hint: Take max.*

<details>
<summary>✅ Solution</summary>

```python
block = [[1, 4], [3, 2]]
print(max(v for row in block for v in row))  # 4
```

</details>

## Exercise 4

Why do CNNs use weight sharing?

*Hint: Efficiency.*

<details>
<summary>✅ Solution</summary>

The same kernel is applied across the whole image, so the network learns
**position-independent** features with **far fewer parameters** than a fully
connected layer (and gains translation invariance).

</details>

## Exercise 5

What does a pooling layer do?

*Hint: Downsample.*

<details>
<summary>✅ Solution</summary>

**Downsamples** feature maps (e.g. 2×2 max pooling), reducing spatial size and
computation while adding small-shift invariance.

</details>

## Exercise 6

Output size of 28x28 image with 3x3 kernel, padding='same'?

*Hint: Same.*

<details>
<summary>✅ Solution</summary>

**28×28** — 'same' padding adds a border so the output keeps the input's spatial
dimensions.

</details>

## Exercise 7

What do early conv layers typically detect?

*Hint: Low-level.*

<details>
<summary>✅ Solution</summary>

Low-level features like **edges, corners, and simple textures**. Deeper layers
combine these into shapes and eventually whole objects.

</details>

## Exercise 8

Flatten a 2x2 feature map [[1,2],[3,4]] to a vector.

*Hint: Row-major.*

<details>
<summary>✅ Solution</summary>

```python
m = [[1, 2], [3, 4]]
print([v for row in m for v in row])  # [1, 2, 3, 4]
```

</details>


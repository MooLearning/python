# 100 — Transformers and Attention: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute the dot-product score of [1,0] and [1,1].

*Hint: Dot.*

<details>
<summary>✅ Solution</summary>

```python
print(sum(a * b for a, b in zip([1, 0], [1, 1])))  # 1
```

</details>

## Exercise 2

Softmax the scores [1,2,3] (return rounded).

*Hint: exp/sum.*

<details>
<summary>✅ Solution</summary>

```python
import math
z = [1, 2, 3]; e = [math.exp(v) for v in z]; s = sum(e)
print([round(v / s, 3) for v in e])
```

</details>

## Exercise 3

Why divide scores by sqrt(d)?

*Hint: Stability.*

<details>
<summary>✅ Solution</summary>

To **scale down** large dot products (which grow with dimension d). Without it,
softmax saturates and gradients vanish, hurting training.

</details>

## Exercise 4

What do Q, K, V stand for?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Query, Key, Value** — each token is projected into these three vectors;
attention compares queries to keys to weight the values.

</details>

## Exercise 5

Why add positional encodings?

*Hint: Order.*

<details>
<summary>✅ Solution</summary>

Self-attention treats the input as a **set** (order-agnostic). Positional encodings
inject **word-order** information so the model knows token positions.

</details>

## Exercise 6

What is the complexity of attention in sequence length n?

*Hint: Pairwise.*

<details>
<summary>✅ Solution</summary>

**O(n²)** — every token attends to every other token, so cost grows quadratically
with sequence length.

</details>

## Exercise 7

What does multi-head attention add?

*Hint: Multiple views.*

<details>
<summary>✅ Solution</summary>

Several attention heads run in **parallel**, each learning to focus on different
relationships/positions; their outputs are concatenated for a richer
representation.

</details>

## Exercise 8

In a decoder, why mask future tokens?

*Hint: No peeking.*

<details>
<summary>✅ Solution</summary>

So each position can only attend to **earlier** tokens — preventing the model from
'cheating' by seeing the future words it's supposed to predict.

</details>


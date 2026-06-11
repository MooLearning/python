# 93 — TensorFlow, Keras and PyTorch: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

What is a tensor (one line)?

*Hint: Definition.*

<details>
<summary>✅ Solution</summary>

An **N-dimensional array** (scalar=0-D, vector=1-D, matrix=2-D, …) that frameworks
can run on a GPU and differentiate through.

</details>

## Exercise 2

What does autograd remove the need for?

*Hint: Manual backprop.*

<details>
<summary>✅ Solution</summary>

**Hand-coding backpropagation** — autograd records operations and computes gradients
automatically when you call backward().

</details>

## Exercise 3

Give the shape of [[1,2,3],[4,5,6]].

*Hint: rows x cols.*

<details>
<summary>✅ Solution</summary>

```python
m = [[1, 2, 3], [4, 5, 6]]
print((len(m), len(m[0])))  # (2, 3)
```

</details>

## Exercise 4

Which framework uses nn.Module?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**PyTorch** — custom models subclass `torch.nn.Module` (or use `nn.Sequential`).

</details>

## Exercise 5

Which Keras API stacks layers in a list?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**`keras.Sequential`** — pass a list of layers to build a simple feed-forward
stack.

</details>

## Exercise 6

Count params of a Dense layer: 4 inputs -> 3 units (with bias).

*Hint: in*out+out.*

<details>
<summary>✅ Solution</summary>

```python
print(4 * 3 + 3)  # 15
```

</details>

## Exercise 7

Why keep tensors on the same device?

*Hint: Compatibility.*

<details>
<summary>✅ Solution</summary>

Operations require all tensors on the **same device** (all CPU or all the same GPU);
mixing CPU and GPU tensors raises a runtime error.

</details>

## Exercise 8

In PyTorch, what call computes gradients?

*Hint: API.*

<details>
<summary>✅ Solution</summary>

**`loss.backward()`** — it backpropagates and populates each parameter's `.grad`,
which the optimizer then uses in `optimizer.step()`.

</details>


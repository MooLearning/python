# 90 — Neural Network Fundamentals: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute a neuron's output: inputs [1,2], weights [0.5,0.5], bias 0, sigmoid.

*Hint: Weighted sum.*

<details>
<summary>✅ Solution</summary>

```python
import math
z = 1 * 0.5 + 2 * 0.5 + 0
print(round(1 / (1 + math.exp(-z)), 3))  # 0.818
```

</details>

## Exercise 2

Compute ReLU(-3) and ReLU(4).

*Hint: max(0,z).*

<details>
<summary>✅ Solution</summary>

```python
print(max(0, -3), max(0, 4))  # 0 4
```

</details>

## Exercise 3

Compute tanh(0).

*Hint: math.tanh.*

<details>
<summary>✅ Solution</summary>

```python
import math
print(math.tanh(0))  # 0.0
```

</details>

## Exercise 4

Why is a non-linear activation needed?

*Hint: Depth.*

<details>
<summary>✅ Solution</summary>

Without non-linearity, stacking layers just composes linear maps into **one linear
map**, so the network can't represent curves/XOR. Activations give it the power to
approximate complex functions.

</details>

## Exercise 5

Weighted sum of inputs [2,3,1] with weights [1,0,-1], bias 0.5.

*Hint: Dot + bias.*

<details>
<summary>✅ Solution</summary>

```python
inp, w = [2, 3, 1], [1, 0, -1]
print(sum(i * j for i, j in zip(inp, w)) + 0.5)  # 1.5
```

</details>

## Exercise 6

What does sigmoid output approach for large positive z?

*Hint: Saturation.*

<details>
<summary>✅ Solution</summary>

It approaches **1** (and approaches 0 for large negative z). In the saturated
region the gradient is ~0, which can slow learning (vanishing gradients).

</details>

## Exercise 7

Why not initialize all weights to zero?

*Hint: Symmetry.*

<details>
<summary>✅ Solution</summary>

All neurons would compute the same thing and receive identical gradients, so they'd
stay identical forever (**symmetry**). Random init breaks this symmetry.

</details>

## Exercise 8

Apply ReLU elementwise to [-1, 2, -3, 4].

*Hint: Map max(0,x).*

<details>
<summary>✅ Solution</summary>

```python
print([max(0, x) for x in [-1, 2, -3, 4]])  # [0, 2, 0, 4]
```

</details>


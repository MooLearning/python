# 91 — Forward and Backpropagation: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute the MSE loss 0.5*(pred-target)^2 for pred=0.8, target=1.

*Hint: Plug in.*

<details>
<summary>✅ Solution</summary>

```python
pred, target = 0.8, 1
print(0.5 * (pred - target) ** 2)  # 0.02
```

</details>

## Exercise 2

Compute the sigmoid derivative a*(1-a) at a=0.5.

*Hint: Derivative.*

<details>
<summary>✅ Solution</summary>

```python
a = 0.5
print(a * (1 - a))  # 0.25
```

</details>

## Exercise 3

Output error d_out=(out-y)*a(1-a) for out=0.6,y=0.

*Hint: Compute.*

<details>
<summary>✅ Solution</summary>

```python
out, y = 0.6, 0
print(round((out - y) * out * (1 - out), 4))  # 0.144
```

</details>

## Exercise 4

Update w=0.5 with lr=0.1, grad=0.2.

*Hint: w -= lr*grad.*

<details>
<summary>✅ Solution</summary>

```python
w, lr, grad = 0.5, 0.1, 0.2
print(w - lr * grad)  # 0.48
```

</details>

## Exercise 5

What rule does backprop use to compute gradients?

*Hint: Calculus.*

<details>
<summary>✅ Solution</summary>

The **chain rule** of calculus — it decomposes the loss gradient through each
composed layer, multiplying local derivatives from output back to input.

</details>

## Exercise 6

Why cache forward activations?

*Hint: Needed in backward.*

<details>
<summary>✅ Solution</summary>

The backward pass needs each layer's activation (and its derivative) to compute
gradients via the chain rule, so they must be **stored during the forward pass**.

</details>

## Exercise 7

What is one epoch?

*Hint: Definition.*

<details>
<summary>✅ Solution</summary>

**One full pass over the entire training dataset** (forward + backprop + update for
all samples).

</details>

## Exercise 8

Propagate gradient to hidden: d_h = d_out*w2*a(1-a), d_out=0.1,w2=0.4,a=0.5.

*Hint: Chain.*

<details>
<summary>✅ Solution</summary>

```python
d_out, w2, a = 0.1, 0.4, 0.5
print(round(d_out * w2 * a * (1 - a), 5))  # 0.01
```

</details>


# 94 — Building ANNs: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

What output layer for binary classification?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**One neuron with a sigmoid** activation, paired with binary cross-entropy loss.

</details>

## Exercise 2

What output activation for 5-class classification?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Softmax** over **5 neurons** (one per class), with categorical cross-entropy.

</details>

## Exercise 3

What loss for a regression ANN?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Mean Squared Error (MSE)** (or MAE) — the output layer is a single linear
neuron.

</details>

## Exercise 4

Apply softmax to logits [1,2,3] (compute the max-prob class index).

*Hint: Argmax.*

<details>
<summary>✅ Solution</summary>

```python
import math
z = [1, 2, 3]; e = [math.exp(v) for v in z]; s = sum(e)
probs = [v / s for v in e]
print(probs.index(max(probs)))  # 2
```

</details>

## Exercise 5

Compute ReLU of hidden pre-activations [-0.5, 0.3, 2].

*Hint: max(0,z).*

<details>
<summary>✅ Solution</summary>

```python
print([max(0, z) for z in [-0.5, 0.3, 2]])  # [0, 0.3, 2]
```

</details>

## Exercise 6

Sign of overfitting in train/val accuracy?

*Hint: Gap.*

<details>
<summary>✅ Solution</summary>

**Training accuracy much higher than validation accuracy** (a large gap) signals the
model is memorizing training data rather than generalizing.

</details>

## Exercise 7

How many weights in Dense(8) fed by 4 inputs (no bias)?

*Hint: in*out.*

<details>
<summary>✅ Solution</summary>

```python
print(4 * 8)  # 32
```

</details>

## Exercise 8

Integer labels: which loss in Keras?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**sparse_categorical_crossentropy** — it accepts integer class labels directly (no
one-hot encoding needed).

</details>


# 96 — RNN, LSTM and GRU: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute one RNN step h=tanh(0.5*x+0.8*h) for x=1,h=0.

*Hint: Plug in.*

<details>
<summary>✅ Solution</summary>

```python
import math
print(round(math.tanh(0.5 * 1 + 0.8 * 0), 4))  # 0.4621
```

</details>

## Exercise 2

What problem do LSTMs solve vs plain RNNs?

*Hint: Long memory.*

<details>
<summary>✅ Solution</summary>

**Vanishing gradients / short memory.** LSTM gates and a cell state let gradients
flow over many steps, capturing **long-range dependencies** plain RNNs lose.

</details>

## Exercise 3

Name the three LSTM gates.

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Forget**, **input**, and **output** gates (operating on a cell state).

</details>

## Exercise 4

Which is simpler/lighter: LSTM or GRU?

*Hint: Param count.*

<details>
<summary>✅ Solution</summary>

**GRU** — it merges gates (reset/update, no separate cell state), so it has fewer
parameters and trains faster, often with comparable accuracy.

</details>

## Exercise 5

What input shape does a Keras LSTM expect?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**(batch, timesteps, features)** — a 3-D tensor where each sample is a sequence of
feature vectors.

</details>

## Exercise 6

Compute a forget gate sigmoid(0.5*2+0.1*0).

*Hint: Sigmoid.*

<details>
<summary>✅ Solution</summary>

```python
import math
print(round(1 / (1 + math.exp(-(0.5 * 2 + 0.1 * 0))), 4))  # 0.7311
```

</details>

## Exercise 7

Many-to-one RNN: give an example task.

*Hint: Sequence in, label out.*

<details>
<summary>✅ Solution</summary>

**Sentiment classification** (read a sentence → output positive/negative), or any
task that consumes a whole sequence and emits a single label/value.

</details>

## Exercise 8

Why pad sequences in a batch?

*Hint: Equal length.*

<details>
<summary>✅ Solution</summary>

Tensors must be rectangular, so variable-length sequences are **padded to the same
length** (with a mask so the model ignores the padding).

</details>


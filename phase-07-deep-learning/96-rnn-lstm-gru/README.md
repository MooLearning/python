# 96 — RNN, LSTM and GRU

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Recurrent Neural Networks (RNNs)** process **sequences** (text, time series, audio) by maintaining a **hidden state** that carries information from previous steps: hₜ = tanh(Wₓxₜ + Wₕhₜ₋₁ + b). Plain RNNs forget long-range context (vanishing gradients). **LSTM** and **GRU** add **gates** that learn what to keep, forget, and output — capturing long-term dependencies.

## Why it matters

Sequence data is everywhere — language, stock prices, sensor streams. RNNs/LSTMs were the backbone of NLP and forecasting before transformers, and the gated-memory idea is fundamental to understanding sequence modeling.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install tensorflow
```

## Key concepts

- **Hidden state** — Memory passed from one time step to the next.
- **Recurrence** — Same weights applied at every step of the sequence.
- **Vanishing gradient** — Plain RNNs lose long-range signal during backprop.
- **LSTM gates** — Forget/input/output gates manage a cell state.
- **GRU** — Simpler gating (reset/update) — fewer params than LSTM.
- **Sequence I/O** — Many-to-one (classify), many-to-many (translate).

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import math

# h_t = tanh(Wx * x_t + Wh * h_{t-1} + b)
Wx, Wh, b = 0.6, 0.8, 0.0
h = 0.0
sequence = [1.0, 0.5, -1.0, 2.0]

print("step | input |  hidden state")
for t, x in enumerate(sequence):
    h = math.tanh(Wx * x + Wh * h + b)        # carries memory forward
    print(f"  {t}  |  {x:4} |  {h:.4f}")
print("\nThe hidden state depends on ALL previous inputs (memory).")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Plain RNNs suffer vanishing/exploding gradients on long sequences — use LSTM/GRU.
- ⚠️ Sequences in a batch must be padded to equal length (and masked) — don't ignore padding.
- ⚠️ LSTMs are slow to train (sequential, can't fully parallelize over time).
- ⚠️ Watch input shape: Keras RNNs expect (batch, timesteps, features).
- ⚠️ For very long-range dependencies, transformers usually beat RNNs now.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


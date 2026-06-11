# 100 — Transformers and Attention

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Transformers** process sequences using **self-attention** instead of recurrence. Attention lets each token look at every other token and weight their relevance: scores = softmax(Q·Kᵀ/√d), output = scores·V. **Multi-head attention** runs several attentions in parallel; **positional encodings** inject word order. Because attention is parallel (not sequential), transformers train fast on huge data — powering BERT, GPT, etc.

## Why it matters

Transformers are the architecture behind virtually all modern AI (LLMs, translation, vision transformers). Understanding self-attention — the core operation — is the key to understanding today's models.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install transformers
```

## Key concepts

- **Self-attention** — Each token attends to all tokens, weighting by relevance.
- **Q, K, V** — Query, Key, Value projections of each token.
- **Scaled dot-product** — softmax(QKᵀ/√d)·V computes the attention output.
- **Multi-head** — Several attention heads capture different relationships.
- **Positional encoding** — Adds order information (attention itself is order-agnostic).
- **Parallelism** — All positions processed at once — unlike sequential RNNs.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import math

def softmax(xs):
    m = max(xs)
    exps = [math.exp(x - m) for x in xs]
    s = sum(exps)
    return [e / s for e in exps]

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

# 3 tokens, each a 2-D embedding. Use them directly as Q=K=V (self-attention).
tokens = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
d = len(tokens[0])

for i, q in enumerate(tokens):
    scores = [dot(q, k) / math.sqrt(d) for k in tokens]   # similarity to each token
    weights = softmax(scores)                              # attention distribution
    output = [sum(weights[j] * tokens[j][c] for j in range(len(tokens)))
              for c in range(d)]
    print(f"token {i}: weights={[round(w, 3) for w in weights]} "
          f"-> context={[round(o, 3) for o in output]}")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Self-attention is O(n²) in sequence length — long sequences are expensive.
- ⚠️ Attention alone ignores order; you MUST add positional encodings.
- ⚠️ Don't forget the 1/√d scaling — large dot products make softmax gradients vanish.
- ⚠️ Q, K, V come from LEARNED projections in real models, not the raw embeddings.
- ⚠️ Causal (decoder) attention must mask future tokens so the model can't peek ahead.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


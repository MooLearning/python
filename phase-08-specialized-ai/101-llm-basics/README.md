# 101 — LLM Basics

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Large Language Models (LLMs)** are huge transformers trained on massive text to predict the **next token**. From that single objective emerge translation, summarization, coding, and reasoning. Key ideas: **tokenization** (text → subword IDs), **autoregressive generation** (sample tokens one at a time), **temperature** (randomness of sampling), and **prompting/context windows**. Fine-tuning and RLHF align them to instructions.

## Why it matters

LLMs (GPT, Claude, Llama) are reshaping software. Understanding next-token prediction, tokens, temperature, and context windows lets you use and build on them effectively — prompting, RAG, and agents all rest on these basics.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install transformers
```

## Key concepts

- **Next-token prediction** — The core training objective: predict the following token.
- **Tokenization** — Text is split into subword tokens with integer IDs.
- **Autoregressive** — Generate one token, append it, repeat.
- **Temperature** — Scales randomness: low = focused, high = creative.
- **Context window** — Max tokens the model can attend to at once.
- **Prompting** — The input text that steers the model's output.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import random
from collections import defaultdict, Counter
random.seed(0)

corpus = ("the cat sat on the mat the cat ran the dog sat on the log "
          "the dog ran the cat sat").split()

# Learn P(next word | current word) from counts
model = defaultdict(Counter)
for a, b in zip(corpus, corpus[1:]):
    model[a][b] += 1

def predict_next(word):
    if word not in model:
        return random.choice(corpus)
    options = model[word]
    return options.most_common(1)[0][0]      # greedy: most likely next word

# Generate text autoregressively
word = "the"
out = [word]
for _ in range(8):
    word = predict_next(word)
    out.append(word)
print("generated:", " ".join(out))
print("P(* | 'cat'):", dict(model["cat"]))
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ LLMs predict plausible text, not truth — they can 'hallucinate' confident wrong answers.
- ⚠️ Everything is tokens (subwords), not words — token limits and costs are per-token.
- ⚠️ Temperature 0 is (near) deterministic/greedy; high temperature can become incoherent.
- ⚠️ Context windows are finite — text beyond the limit is truncated/forgotten.
- ⚠️ Output is sensitive to prompt wording; small changes can change results a lot.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


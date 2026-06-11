# 98 — Transfer Learning

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Transfer learning** reuses a model **pretrained** on a huge dataset (e.g. ImageNet, or a language corpus) for a new, related task with little data. You keep the pretrained **feature extractor** (often **frozen**) and train a small new **head** on top. **Fine-tuning** then optionally unfreezes some upper layers and trains them at a low learning rate.

## Why it matters

Training big models from scratch needs massive data and compute. Transfer learning gives state-of-the-art results with a few hundred examples and minutes of training — the default approach for most real vision and NLP tasks today.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install tensorflow
```

## Key concepts

- **Pretrained model** — Weights learned on a large general dataset.
- **Feature extractor** — Reuse the pretrained body that produces rich features.
- **Freezing** — Mark layers non-trainable so their weights don't update.
- **New head** — A fresh small classifier trained for your task.
- **Fine-tuning** — Unfreeze upper layers and train at a low learning rate.
- **Data efficiency** — Great results from little task-specific data.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
# A pretrained base is frozen; a small head is trained on top.
layers = [
    {"name": "pretrained_conv_base", "params": 14_000_000, "trainable": False},
    {"name": "new_dense_head",       "params": 50_000,     "trainable": True},
]
trainable = sum(l["params"] for l in layers if l["trainable"])
frozen = sum(l["params"] for l in layers if not l["trainable"])
print(f"frozen (reused) params : {frozen:,}")
print(f"trainable (new) params : {trainable:,}")
print(f"-> training only {trainable / (trainable + frozen):.1%} of the weights")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Freeze the base FIRST and train the head; only then fine-tune upper layers (low LR).
- ⚠️ Use the SAME preprocessing the base model was trained with (resize, normalization).
- ⚠️ Fine-tuning with a high learning rate destroys pretrained weights — use a small one.
- ⚠️ If your task is very different from the pretraining data, transfer helps less.
- ⚠️ Match input size/channels to what the pretrained model expects.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


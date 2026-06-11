# 98 — Transfer Learning: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

If base has 14M frozen params and head 50k trainable, how many train?

*Hint: Only head.*

<details>
<summary>✅ Solution</summary>

```python
print(50_000)  # only the head's params update
```

</details>

## Exercise 2

What does 'freezing' a layer mean?

*Hint: No updates.*

<details>
<summary>✅ Solution</summary>

Marking it **non-trainable** so its weights are **not updated** during
backpropagation — the pretrained features are reused as-is.

</details>

## Exercise 3

Why use a pretrained model?

*Hint: Data/compute.*

<details>
<summary>✅ Solution</summary>

It already learned general features from a huge dataset, so you get strong results
with **little task data and compute** instead of training from scratch.

</details>

## Exercise 4

Order: freeze-then-finetune or finetune-then-freeze?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Freeze first** (train the new head on frozen features), **then optionally
fine-tune** some upper layers at a low learning rate.

</details>

## Exercise 5

Why a LOW learning rate when fine-tuning?

*Hint: Preserve weights.*

<details>
<summary>✅ Solution</summary>

To make small adjustments that **preserve the valuable pretrained weights**; a high
LR would overwrite them and destroy the learned features.

</details>

## Exercise 6

Compute the trainable fraction: 50k of 14.05M total.

*Hint: Ratio.*

<details>
<summary>✅ Solution</summary>

```python
print(round(50_000 / 14_050_000, 4))  # ~0.0036
```

</details>

## Exercise 7

Must input preprocessing match the pretrained model?

*Hint: Yes.*

<details>
<summary>✅ Solution</summary>

**Yes** — use the same resizing and normalization the base model was trained with,
or the features will be meaningless.

</details>

## Exercise 8

Name a domain where transfer learning is standard.

*Hint: Vision/NLP.*

<details>
<summary>✅ Solution</summary>

**Computer vision** (ImageNet-pretrained CNNs) and **NLP** (pretrained transformers
like BERT/GPT) — both routinely fine-tune large pretrained models.

</details>


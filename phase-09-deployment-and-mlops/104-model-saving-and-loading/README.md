# 104 — Model Saving and Loading

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A trained model must be **persisted** (serialized to disk) so you can reuse it without retraining. Python's **pickle** serializes arbitrary objects; **joblib** is faster for big NumPy arrays (the scikit-learn standard). For portability you can also save just the **parameters** (weights, config) as **JSON**. Frameworks have their own formats (Keras `.keras`, PyTorch `state_dict`).

## Why it matters

You train once and serve many times. Saving/loading models is the bridge from a notebook experiment to a deployable artifact — the first step of putting ML into production.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install joblib
```

## Key concepts

- **Serialization** — Convert an in-memory object to bytes on disk.
- **pickle** — Built-in; serializes most Python objects.
- **joblib** — Efficient for large NumPy arrays; sklearn's choice.
- **JSON params** — Portable, human-readable weights/config (no code).
- **Framework formats** — Keras `.keras`, PyTorch `state_dict`.
- **Versioning** — Save the model version + training metadata alongside it.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import pickle, tempfile, os

class LinearModel:
    def __init__(self, w, b):
        self.w, self.b = w, b
    def predict(self, x):
        return self.w * x + self.b

model = LinearModel(2.0, 1.0)               # a 'trained' model
path = os.path.join(tempfile.gettempdir(), "model.pkl")

with open(path, "wb") as f:                 # SAVE
    pickle.dump(model, f)

with open(path, "rb") as f:                 # LOAD (e.g. in a server later)
    loaded = pickle.load(f)

print("loaded model predicts:", loaded.predict(5))   # 11.0
print("saved to:", path)
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ NEVER unpickle files from untrusted sources — pickle can execute arbitrary code.
- ⚠️ Pickled models are tied to library versions; loading with a different sklearn can break.
- ⚠️ Pickle needs the model's CLASS available at load time — keep the code importable.
- ⚠️ Save preprocessing (scalers/encoders) WITH the model, or predictions will be wrong.
- ⚠️ Record the model version and training data/metadata for reproducibility.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


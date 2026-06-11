# ======================================================================
# 98 — Transfer Learning  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: tensorflow
# Install:  pip install tensorflow

# ----------------------------------------------------------------------
# Example 1: Freezing: only the new head is trainable
# ----------------------------------------------------------------------
print("\n--- Example 1: Freezing: only the new head is trainable ---")
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

# ----------------------------------------------------------------------
# Example 2: Transfer learning concretely: frozen extractor + trained head
# ----------------------------------------------------------------------
print("\n--- Example 2: Transfer learning concretely: frozen extractor + trained head ---")
import math
def sigmoid(z): return 1 / (1 + math.exp(-z))

# A FROZEN 'pretrained' feature extractor (fixed weights, never updated)
def extract_features(x):
    return [math.sin(x), x * 0.1, 1.0]        # 3 reusable features

data = [(1.0, 0), (2.0, 0), (8.0, 1), (9.0, 1)]   # small task dataset

# Train ONLY a small head (3 weights) on the frozen features
w = [0.0, 0.0, 0.0]
lr = 0.1
for _ in range(800):
    for x, y in data:
        f = extract_features(x)
        p = sigmoid(sum(wi * fi for wi, fi in zip(w, f)))
        for j in range(3):
            w[j] -= lr * (p - y) * f[j]        # update head only

print("trained head predictions:")
for x, y in data:
    f = extract_features(x)
    p = sigmoid(sum(wi * fi for wi, fi in zip(w, f)))
    print(f"  x={x} -> {p:.3f} (target {y})")

# ----------------------------------------------------------------------
# Example 3: Transfer learning with Keras (frozen base + new head)
# ----------------------------------------------------------------------
print("\n--- Example 3: Transfer learning with Keras (frozen base + new head) ---")
try:
    from tensorflow import keras

    # Load a model pretrained on ImageNet, WITHOUT its classifier head
    base = keras.applications.MobileNetV2(
        input_shape=(96, 96, 3), include_top=False, weights="imagenet")
    base.trainable = False                       # freeze the feature extractor

    model = keras.Sequential([
        base,
        keras.layers.GlobalAveragePooling2D(),
        keras.layers.Dense(2, activation="softmax"),   # new task: 2 classes
    ])
    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    trainable = sum(keras.backend.count_params(w) for w in model.trainable_weights)
    print("trainable params (just the head):", trainable)
except ImportError:
    print("TensorFlow not installed — run: pip install tensorflow")

print("\nDone! Tip: change values above and run again to learn by experiment.")

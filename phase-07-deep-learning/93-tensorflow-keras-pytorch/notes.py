# ======================================================================
# 93 — TensorFlow, Keras and PyTorch  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: tensorflow, torch
# Install:  pip install tensorflow torch

# ----------------------------------------------------------------------
# Example 1: Tensors are like nested lists / NumPy arrays (concept)
# ----------------------------------------------------------------------
print("\n--- Example 1: Tensors are like nested lists / NumPy arrays (concept) ---")
# A 'tensor' is just an n-dimensional array. Pure-Python stand-ins:
scalar = 3.14                       # 0-D
vector = [1, 2, 3]                  # 1-D
matrix = [[1, 2], [3, 4]]           # 2-D
tensor3d = [[[1], [2]], [[3], [4]]] # 3-D

def shape(x):
    s = []
    while isinstance(x, list):
        s.append(len(x)); x = x[0]
    return tuple(s)

print("scalar shape :", shape(scalar) or "()")
print("vector shape :", shape(vector))     # (3,)
print("matrix shape :", shape(matrix))     # (2, 2)
print("tensor shape :", shape(tensor3d))   # (2, 2, 1)

# ----------------------------------------------------------------------
# Example 2: Build a model in Keras
# ----------------------------------------------------------------------
print("\n--- Example 2: Build a model in Keras ---")
try:
    import tensorflow as tf
    from tensorflow import keras

    model = keras.Sequential([
        keras.layers.Input(shape=(4,)),
        keras.layers.Dense(16, activation="relu"),
        keras.layers.Dense(3, activation="softmax"),
    ])
    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])
    print("total params:", model.count_params())
    model.summary()
except ImportError:
    print("TensorFlow not installed — run: pip install tensorflow")

# ----------------------------------------------------------------------
# Example 3: Build the same model in PyTorch
# ----------------------------------------------------------------------
print("\n--- Example 3: Build the same model in PyTorch ---")
try:
    import torch
    import torch.nn as nn

    model = nn.Sequential(
        nn.Linear(4, 16),
        nn.ReLU(),
        nn.Linear(16, 3),
    )
    x = torch.randn(2, 4)             # a batch of 2 samples
    out = model(x)                    # forward pass (autograd tracks it)
    print("output shape:", tuple(out.shape))         # (2, 3)
    n_params = sum(p.numel() for p in model.parameters())
    print("total params:", n_params)
except ImportError:
    print("PyTorch not installed — run: pip install torch")

print("\nDone! Tip: change values above and run again to learn by experiment.")

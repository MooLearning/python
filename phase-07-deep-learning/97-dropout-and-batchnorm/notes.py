# ======================================================================
# 97 — Dropout and Batch Normalization  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: tensorflow
# Install:  pip install tensorflow

# ----------------------------------------------------------------------
# Example 1: Dropout (inverted) in train vs eval mode
# ----------------------------------------------------------------------
print("\n--- Example 1: Dropout (inverted) in train vs eval mode ---")
import random
random.seed(0)

def dropout(activations, p=0.5, training=True):
    if not training:
        return activations[:]                 # inference: use everything
    out = []
    for a in activations:
        keep = random.random() >= p
        out.append(a / (1 - p) if keep else 0.0)   # scale survivors
    return out

acts = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
print("train (some zeroed, rest scaled):", [round(v, 2) for v in dropout(acts, 0.5)])
print("eval  (all kept)               :", dropout(acts, 0.5, training=False))

# ----------------------------------------------------------------------
# Example 2: Batch normalization of a layer's activations
# ----------------------------------------------------------------------
print("\n--- Example 2: Batch normalization of a layer's activations ---")
import statistics as st

def batch_norm(batch, gamma=1.0, beta=0.0, eps=1e-5):
    mean = st.mean(batch)
    var = st.pvariance(batch)
    # normalize to mean 0 / var 1, then scale (gamma) and shift (beta)
    return [gamma * ((x - mean) / ((var + eps) ** 0.5)) + beta for x in batch]

activations = [10.0, 12.0, 14.0, 16.0, 18.0]
normed = batch_norm(activations)
print("before:", activations)
print("after :", [round(v, 3) for v in normed])
print("new mean ~", round(st.mean(normed), 6), "| new std ~",
      round(st.pstdev(normed), 4))            # ~0 mean, ~1 std

# ----------------------------------------------------------------------
# Example 3: Dropout and BatchNorm layers in Keras
# ----------------------------------------------------------------------
print("\n--- Example 3: Dropout and BatchNorm layers in Keras ---")
try:
    from tensorflow import keras

    model = keras.Sequential([
        keras.layers.Input(shape=(20,)),
        keras.layers.Dense(64),
        keras.layers.BatchNormalization(),       # normalize activations
        keras.layers.Activation("relu"),
        keras.layers.Dropout(0.5),               # drop 50% during training
        keras.layers.Dense(1, activation="sigmoid"),
    ])
    model.compile(optimizer="adam", loss="binary_crossentropy")
    print("params:", model.count_params())
    # Keras automatically disables dropout / uses running stats at inference.
    model.summary()
except ImportError:
    print("TensorFlow not installed — run: pip install tensorflow")

print("\nDone! Tip: change values above and run again to learn by experiment.")

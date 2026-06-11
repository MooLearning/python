# ======================================================================
# 94 — Building ANNs  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: tensorflow
# Install:  pip install tensorflow

# ----------------------------------------------------------------------
# Example 1: A minimal multilayer perceptron forward pass (pure Python)
# ----------------------------------------------------------------------
print("\n--- Example 1: A minimal multilayer perceptron forward pass (pure Python) ---")
import math
def relu(z):    return max(0.0, z)
def softmax(zs):
    m = max(zs)
    exps = [math.exp(z - m) for z in zs]
    s = sum(exps)
    return [e / s for e in exps]

def dense(inputs, weights, biases, act):
    outs = []
    for j in range(len(biases)):
        z = sum(i * w for i, w in zip(inputs, weights[j])) + biases[j]
        outs.append(z if act is None else act(z))
    return outs

x = [0.5, -1.0, 2.0]
W1 = [[0.1, 0.2, -0.1], [0.0, 0.3, 0.2]]     # hidden: 2 ReLU units
b1 = [0.0, 0.1]
W2 = [[0.5, -0.2], [0.1, 0.4], [-0.3, 0.2]]  # output: 3 classes
b2 = [0.0, 0.0, 0.0]

hidden = dense(x, W1, b1, relu)
logits = dense(hidden, W2, b2, None)
probs = softmax(logits)
print("hidden       :", [round(h, 3) for h in hidden])
print("class probs  :", [round(p, 3) for p in probs])
print("predicted    :", probs.index(max(probs)))

# ----------------------------------------------------------------------
# Example 2: Choosing output layer and loss by task
# ----------------------------------------------------------------------
print("\n--- Example 2: Choosing output layer and loss by task ---")
tasks = [
    ("binary classification", "1 neuron, sigmoid", "binary_crossentropy"),
    ("multiclass (3 classes)", "3 neurons, softmax", "categorical_crossentropy"),
    ("regression",            "1 neuron, linear",  "mse"),
]
print(f"{'task':24} | {'output layer':22} | loss")
print("-" * 70)
for task, out, loss in tasks:
    print(f"{task:24} | {out:22} | {loss}")

# ----------------------------------------------------------------------
# Example 3: Build and train an ANN with Keras
# ----------------------------------------------------------------------
print("\n--- Example 3: Build and train an ANN with Keras ---")
try:
    import numpy as np
    from tensorflow import keras
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split

    X, y = load_iris(return_X_y=True)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=0)

    model = keras.Sequential([
        keras.layers.Input(shape=(4,)),
        keras.layers.Dense(16, activation="relu"),
        keras.layers.Dense(3, activation="softmax"),
    ])
    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit(X_tr, y_tr, epochs=30, batch_size=8, verbose=0)
    loss, acc = model.evaluate(X_te, y_te, verbose=0)
    print("test accuracy:", round(acc, 3))
except ImportError:
    print("TensorFlow/sklearn not installed — run: pip install tensorflow scikit-learn")

print("\nDone! Tip: change values above and run again to learn by experiment.")

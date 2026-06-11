# ======================================================================
# 90 — Neural Network Fundamentals  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: tensorflow
# Install:  pip install tensorflow

# ----------------------------------------------------------------------
# Example 1: A single neuron
# ----------------------------------------------------------------------
print("\n--- Example 1: A single neuron ---")
import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def neuron(inputs, weights, bias, activation=sigmoid):
    z = sum(i * w for i, w in zip(inputs, weights)) + bias   # weighted sum
    return activation(z)

# An OR-like neuron
inputs_list = [[0, 0], [0, 1], [1, 0], [1, 1]]
weights = [10, 10]      # large weights -> sharp decision
bias = -5
for x in inputs_list:
    out = neuron(x, weights, bias)
    print(f"{x} -> {out:.3f} -> {round(out)}")   # behaves like logical OR

# ----------------------------------------------------------------------
# Example 2: Activation functions and why non-linearity matters
# ----------------------------------------------------------------------
print("\n--- Example 2: Activation functions and why non-linearity matters ---")
import math

def sigmoid(z): return 1 / (1 + math.exp(-z))
def relu(z):    return max(0.0, z)
def tanh(z):    return math.tanh(z)

print(f"{'z':>5} | {'sigmoid':>8} | {'relu':>5} | {'tanh':>6}")
for z in [-2, -0.5, 0, 0.5, 2]:
    print(f"{z:5} | {sigmoid(z):8.3f} | {relu(z):5.1f} | {tanh(z):6.3f}")

# Two stacked LINEAR layers collapse into one linear layer:
def linear(x, w, b): return w * x + b
combined = linear(linear(3, 2, 1), 4, 0)        # 4*(2*3+1) = 28
direct   = (4 * 2) * 3 + (4 * 1)                # 8*3 + 4 = 28  -> same!
print("\nstacked linear =", combined, "== single linear =", direct)
print("-> need a non-linear activation to gain real depth")

# ----------------------------------------------------------------------
# Example 3: A 2-layer forward pass (pure Python) and Keras
# ----------------------------------------------------------------------
print("\n--- Example 3: A 2-layer forward pass (pure Python) and Keras ---")
import math
def sigmoid(z): return 1 / (1 + math.exp(-z))

def layer(inputs, weights, biases, act=sigmoid):
    # weights[j] are the weights for neuron j
    return [act(sum(i * w for i, w in zip(inputs, weights[j])) + biases[j])
            for j in range(len(biases))]

x = [1.0, 0.5]
W1 = [[0.2, 0.8], [0.6, -0.4]]      # hidden layer: 2 neurons
b1 = [0.0, 0.1]
W2 = [[0.5, -0.3]]                  # output layer: 1 neuron
b2 = [0.2]

hidden = layer(x, W1, b1)
output = layer(hidden, W2, b2)
print("hidden:", [round(h, 3) for h in hidden])
print("output:", [round(o, 3) for o in output])

try:
    from tensorflow import keras
    model = keras.Sequential([
        keras.layers.Input(shape=(2,)),
        keras.layers.Dense(2, activation="sigmoid"),
        keras.layers.Dense(1, activation="sigmoid"),
    ])
    print("Keras params:", model.count_params())
except ImportError:
    print("TensorFlow not installed — run: pip install tensorflow")

print("\nDone! Tip: change values above and run again to learn by experiment.")

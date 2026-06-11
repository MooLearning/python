# ======================================================================
# 96 — RNN, LSTM and GRU  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: tensorflow
# Install:  pip install tensorflow

# ----------------------------------------------------------------------
# Example 1: A simple RNN cell processing a sequence (pure Python)
# ----------------------------------------------------------------------
print("\n--- Example 1: A simple RNN cell processing a sequence (pure Python) ---")
import math

# h_t = tanh(Wx * x_t + Wh * h_{t-1} + b)
Wx, Wh, b = 0.6, 0.8, 0.0
h = 0.0
sequence = [1.0, 0.5, -1.0, 2.0]

print("step | input |  hidden state")
for t, x in enumerate(sequence):
    h = math.tanh(Wx * x + Wh * h + b)        # carries memory forward
    print(f"  {t}  |  {x:4} |  {h:.4f}")
print("\nThe hidden state depends on ALL previous inputs (memory).")

# ----------------------------------------------------------------------
# Example 2: A scalar LSTM cell with gates (pure Python)
# ----------------------------------------------------------------------
print("\n--- Example 2: A scalar LSTM cell with gates (pure Python) ---")
import math
def sigmoid(z): return 1 / (1 + math.exp(-z))

# Preset weights for illustration. Gates decide what to keep/forget/output.
h, c = 0.0, 0.0          # hidden state, cell state
for t, x in enumerate([1.0, 0.5, 2.0]):
    f = sigmoid(0.5 * x + 0.1 * h)      # FORGET gate (keep old cell?)
    i = sigmoid(0.6 * x + 0.2 * h)      # INPUT gate (write new info?)
    o = sigmoid(0.4 * x + 0.3 * h)      # OUTPUT gate (expose cell?)
    g = math.tanh(0.7 * x + 0.1 * h)    # candidate cell value
    c = f * c + i * g                   # update cell state
    h = o * math.tanh(c)                # new hidden state
    print(f"t={t}: forget={f:.2f} input={i:.2f} output={o:.2f} -> h={h:.4f}")

# ----------------------------------------------------------------------
# Example 3: LSTM/GRU with Keras
# ----------------------------------------------------------------------
print("\n--- Example 3: LSTM/GRU with Keras ---")
try:
    from tensorflow import keras

    # Many-to-one: read a sequence, output a class (e.g. sentiment)
    model = keras.Sequential([
        keras.layers.Input(shape=(20, 8)),       # 20 timesteps, 8 features
        keras.layers.LSTM(32),                   # try GRU(32) for fewer params
        keras.layers.Dense(1, activation="sigmoid"),
    ])
    model.compile(optimizer="adam", loss="binary_crossentropy",
                  metrics=["accuracy"])
    print("LSTM model params:", model.count_params())

    gru = keras.Sequential([
        keras.layers.Input(shape=(20, 8)),
        keras.layers.GRU(32),
        keras.layers.Dense(1, activation="sigmoid"),
    ])
    print("GRU  model params:", gru.count_params(), "(fewer than LSTM)")
except ImportError:
    print("TensorFlow not installed — run: pip install tensorflow")

print("\nDone! Tip: change values above and run again to learn by experiment.")

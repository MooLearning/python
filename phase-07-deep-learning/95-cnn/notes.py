# ======================================================================
# 95 — Convolutional Neural Networks (CNN)  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: tensorflow
# Install:  pip install tensorflow

# ----------------------------------------------------------------------
# Example 1: 2-D convolution from scratch (edge detection)
# ----------------------------------------------------------------------
print("\n--- Example 1: 2-D convolution from scratch (edge detection) ---")
def conv2d(image, kernel):
    ih, iw = len(image), len(image[0])
    kh, kw = len(kernel), len(kernel[0])
    out = [[0.0] * (iw - kw + 1) for _ in range(ih - kh + 1)]
    for i in range(len(out)):
        for j in range(len(out[0])):
            out[i][j] = sum(image[i + a][j + b] * kernel[a][b]
                            for a in range(kh) for b in range(kw))
    return out

# image: dark left half, bright right half -> a vertical edge in the middle
image = [[0, 0, 0, 9, 9, 9] for _ in range(5)]
edge_kernel = [[-1, 0, 1],            # vertical-edge (Prewitt) filter
               [-1, 0, 1],
               [-1, 0, 1]]
feature_map = conv2d(image, edge_kernel)
print("feature map (high values mark the edge):")
for row in feature_map:
    print(" ", [round(v) for v in row])     # the edge column lights up

# ----------------------------------------------------------------------
# Example 2: Max pooling downsamples a feature map
# ----------------------------------------------------------------------
print("\n--- Example 2: Max pooling downsamples a feature map ---")
def max_pool(image, size=2):
    oh, ow = len(image) // size, len(image[0]) // size
    out = [[0] * ow for _ in range(oh)]
    for i in range(oh):
        for j in range(ow):
            out[i][j] = max(image[i*size + a][j*size + b]
                            for a in range(size) for b in range(size))
    return out

fmap = [[1, 3, 2, 4],
        [5, 6, 1, 2],
        [7, 2, 3, 0],
        [1, 2, 8, 4]]
pooled = max_pool(fmap, size=2)
print("2x2 max pooled:")
for row in pooled:
    print(" ", row)            # [[6, 4], [7, 8]] -> keeps the strongest signals
print("shape:", len(fmap), "x", len(fmap[0]), "->",
      len(pooled), "x", len(pooled[0]))

# ----------------------------------------------------------------------
# Example 3: A CNN with Keras
# ----------------------------------------------------------------------
print("\n--- Example 3: A CNN with Keras ---")
try:
    from tensorflow import keras

    model = keras.Sequential([
        keras.layers.Input(shape=(28, 28, 1)),           # grayscale image
        keras.layers.Conv2D(32, (3, 3), activation="relu"),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation="relu"),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Flatten(),
        keras.layers.Dense(64, activation="relu"),
        keras.layers.Dense(10, activation="softmax"),    # 10 digit classes
    ])
    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    print("total params:", model.count_params())
    model.summary()
except ImportError:
    print("TensorFlow not installed — run: pip install tensorflow")

print("\nDone! Tip: change values above and run again to learn by experiment.")

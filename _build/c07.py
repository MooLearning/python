# -*- coding: utf-8 -*-
"""Phase 7 — Deep Learning.

Core neural-network mechanics are implemented in pure Python (and actually learn,
e.g. XOR via backprop). Framework examples (TensorFlow/Keras, PyTorch) are guarded
with try/except so each notes.py runs even without the libraries installed.
"""

CONTENT = {}

CONTENT["neural-network-fundamentals"] = {
    "deps": ["tensorflow"],
    "what": (
        "A **neural network** is layers of **neurons**. Each neuron computes a **weighted sum** of "
        "its inputs plus a **bias**, then applies a non-linear **activation function** (sigmoid, "
        "ReLU, tanh). Stacking layers (**input → hidden → output**) lets the network approximate "
        "complex, non-linear functions. The activation's non-linearity is essential — without it, "
        "any depth collapses to a single linear map."
    ),
    "why": (
        "Neural networks are the foundation of deep learning, powering vision, language, and speech. "
        "Understanding the neuron, weights, bias, and activations demystifies everything that "
        "follows — backprop, CNNs, transformers."
    ),
    "concepts": [
        ("Neuron", "Weighted sum of inputs + bias, then an activation."),
        ("Weights & bias", "Learnable parameters; weights scale inputs, bias shifts."),
        ("Activation", "Non-linearity (ReLU/sigmoid/tanh) enabling complex functions."),
        ("Layer", "A group of neurons; networks stack input/hidden/output layers."),
        ("Forward pass", "Data flows input → output to produce a prediction."),
        ("Why non-linear", "Without it, stacked layers reduce to one linear layer."),
    ],
    "examples": [
        ("A single neuron", r'''
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
'''),
        ("Activation functions and why non-linearity matters", r'''
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
'''),
        ("A 2-layer forward pass (pure Python) and Keras", r'''
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
'''),
    ],
    "gotchas": [
        "Without a non-linear activation, any number of layers equals a single linear layer.",
        "Sigmoid/tanh saturate for large |z| (tiny gradients) — ReLU avoids this in hidden layers.",
        "Initialize weights randomly (not all zeros), or every neuron learns the same thing.",
        "ReLU neurons can 'die' (always output 0) if learning rate is too high — try leaky ReLU.",
        "Bias terms matter — without them a neuron's boundary must pass through the origin.",
    ],
    "exercises": [
        ("Compute a neuron's output: inputs [1,2], weights [0.5,0.5], bias 0, sigmoid.", "Weighted sum.",
         r'''import math
z = 1 * 0.5 + 2 * 0.5 + 0
print(round(1 / (1 + math.exp(-z)), 3))  # 0.818'''),
        ("Compute ReLU(-3) and ReLU(4).", "max(0,z).",
         r'''print(max(0, -3), max(0, 4))  # 0 4'''),
        ("Compute tanh(0).", "math.tanh.",
         r'''import math
print(math.tanh(0))  # 0.0'''),
        ("Why is a non-linear activation needed?", "Depth.",
         r'''#md
Without non-linearity, stacking layers just composes linear maps into **one linear
map**, so the network can't represent curves/XOR. Activations give it the power to
approximate complex functions.'''),
        ("Weighted sum of inputs [2,3,1] with weights [1,0,-1], bias 0.5.", "Dot + bias.",
         r'''inp, w = [2, 3, 1], [1, 0, -1]
print(sum(i * j for i, j in zip(inp, w)) + 0.5)  # 1.5'''),
        ("What does sigmoid output approach for large positive z?", "Saturation.",
         r'''#md
It approaches **1** (and approaches 0 for large negative z). In the saturated
region the gradient is ~0, which can slow learning (vanishing gradients).'''),
        ("Why not initialize all weights to zero?", "Symmetry.",
         r'''#md
All neurons would compute the same thing and receive identical gradients, so they'd
stay identical forever (**symmetry**). Random init breaks this symmetry.'''),
        ("Apply ReLU elementwise to [-1, 2, -3, 4].", "Map max(0,x).",
         r'''print([max(0, x) for x in [-1, 2, -3, 4]])  # [0, 2, 0, 4]'''),
    ],
}

CONTENT["forward-and-backpropagation"] = {
    "deps": ["torch"],
    "what": (
        "**Forward propagation** runs inputs through the network to produce a prediction and a "
        "**loss**. **Backpropagation** then applies the **chain rule** to compute the gradient of "
        "the loss with respect to every weight — flowing errors backward layer by layer. Gradient "
        "descent uses those gradients to nudge the weights. Repeating forward + backprop + update is "
        "how networks **learn**."
    ),
    "why": (
        "Backpropagation is THE algorithm that makes deep learning possible — efficiently computing "
        "millions of gradients. Implementing it once (even for XOR) turns neural nets from magic into "
        "understandable calculus."
    ),
    "concepts": [
        ("Forward pass", "Compute activations layer by layer → prediction → loss."),
        ("Loss", "How wrong the prediction is (e.g. MSE, cross-entropy)."),
        ("Chain rule", "Decompose the gradient through composed functions."),
        ("Backward pass", "Propagate error gradients from output back to inputs."),
        ("Weight update", "w ← w − lr · ∂loss/∂w."),
        ("Epoch", "One full pass over the training data."),
    ],
    "examples": [
        ("Train a network to learn XOR with backprop (pure Python)", r'''
import math, random
random.seed(1)

def sigmoid(z): return 1 / (1 + math.exp(-z))
def dsig(a):    return a * (1 - a)           # derivative via the activation

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [0, 1, 1, 0]                              # XOR: not linearly separable

r = lambda: random.uniform(-1, 1)
W1 = [[r(), r()], [r(), r()]]                 # 2 hidden neurons
b1 = [r(), r()]
W2 = [r(), r()]                               # 1 output neuron
b2 = r()
lr = 0.5

for epoch in range(10000):
    for x, y in zip(X, Y):
        # ---- forward ----
        h = [sigmoid(W1[j][0]*x[0] + W1[j][1]*x[1] + b1[j]) for j in range(2)]
        out = sigmoid(W2[0]*h[0] + W2[1]*h[1] + b2)
        # ---- backward (chain rule) ----
        d_out = (out - y) * dsig(out)         # dLoss/dz at output
        d_h = [d_out * W2[j] * dsig(h[j]) for j in range(2)]
        # ---- update ----
        W2[0] -= lr * d_out * h[0]; W2[1] -= lr * d_out * h[1]; b2 -= lr * d_out
        for j in range(2):
            W1[j][0] -= lr * d_h[j] * x[0]
            W1[j][1] -= lr * d_h[j] * x[1]
            b1[j] -= lr * d_h[j]

print("XOR predictions after training:")
for x, y in zip(X, Y):
    h = [sigmoid(W1[j][0]*x[0] + W1[j][1]*x[1] + b1[j]) for j in range(2)]
    out = sigmoid(W2[0]*h[0] + W2[1]*h[1] + b2)
    print(f"  {x} -> {out:.3f}  (target {y})")
'''),
        ("One forward + backward step, gradients shown", r'''
import math
def sigmoid(z): return 1 / (1 + math.exp(-z))
def dsig(a):    return a * (1 - a)

# tiny 1-1-1 network
w1, b1, w2, b2 = 0.5, 0.0, 0.4, 0.0
x, y = 1.0, 0.0          # input, target

# forward
h = sigmoid(w1 * x + b1)
out = sigmoid(w2 * h + b2)
loss = 0.5 * (out - y) ** 2
print(f"forward: h={h:.4f}, out={out:.4f}, loss={loss:.4f}")

# backward (chain rule)
d_out = (out - y) * dsig(out)            # dL/d(out_pre)
grad_w2 = d_out * h                       # dL/dw2
d_h = d_out * w2 * dsig(h)                # propagate to hidden
grad_w1 = d_h * x                         # dL/dw1
print(f"grad w2={grad_w2:.5f}, grad w1={grad_w1:.5f}")

# update
lr = 0.1
w2 -= lr * grad_w2; w1 -= lr * grad_w1
print(f"updated w1={w1:.5f}, w2={w2:.5f}")
'''),
        ("Autograd with PyTorch", r'''
try:
    import torch

    # PyTorch computes gradients automatically (autograd)
    x = torch.tensor([2.0], requires_grad=True)
    w = torch.tensor([3.0], requires_grad=True)
    b = torch.tensor([1.0], requires_grad=True)

    y = w * x + b          # forward
    loss = (y - 10) ** 2   # target 10
    loss.backward()        # backprop: fills .grad

    print("y    :", y.item())
    print("loss :", loss.item())
    print("dL/dw:", w.grad.item())   # gradient w.r.t. w
    print("dL/db:", b.grad.item())
except ImportError:
    print("PyTorch not installed — run: pip install torch")
'''),
    ],
    "gotchas": [
        "Forgetting to ZERO gradients between steps (in frameworks) accumulates them — wrong updates.",
        "Sigmoid/tanh in deep nets cause VANISHING gradients; use ReLU and good initialization.",
        "Too-large learning rates make gradients explode and loss go to NaN.",
        "Backprop needs the forward activations cached — you can't discard them before the backward pass.",
        "A wrong derivative (e.g. sigmoid') silently breaks learning — verify gradients numerically.",
    ],
    "exercises": [
        ("Compute the MSE loss 0.5*(pred-target)^2 for pred=0.8, target=1.", "Plug in.",
         r'''pred, target = 0.8, 1
print(0.5 * (pred - target) ** 2)  # 0.02'''),
        ("Compute the sigmoid derivative a*(1-a) at a=0.5.", "Derivative.",
         r'''a = 0.5
print(a * (1 - a))  # 0.25'''),
        ("Output error d_out=(out-y)*a(1-a) for out=0.6,y=0.", "Compute.",
         r'''out, y = 0.6, 0
print(round((out - y) * out * (1 - out), 4))  # 0.144'''),
        ("Update w=0.5 with lr=0.1, grad=0.2.", "w -= lr*grad.",
         r'''w, lr, grad = 0.5, 0.1, 0.2
print(w - lr * grad)  # 0.48'''),
        ("What rule does backprop use to compute gradients?", "Calculus.",
         r'''#md
The **chain rule** of calculus — it decomposes the loss gradient through each
composed layer, multiplying local derivatives from output back to input.'''),
        ("Why cache forward activations?", "Needed in backward.",
         r'''#md
The backward pass needs each layer's activation (and its derivative) to compute
gradients via the chain rule, so they must be **stored during the forward pass**.'''),
        ("What is one epoch?", "Definition.",
         r'''#md
**One full pass over the entire training dataset** (forward + backprop + update for
all samples).'''),
        ("Propagate gradient to hidden: d_h = d_out*w2*a(1-a), d_out=0.1,w2=0.4,a=0.5.", "Chain.",
         r'''d_out, w2, a = 0.1, 0.4, 0.5
print(round(d_out * w2 * a * (1 - a), 5))  # 0.01'''),
    ],
}

CONTENT["gradient-descent-and-optimizers"] = {
    "deps": ["torch"],
    "what": (
        "**Gradient descent** minimizes the loss by repeatedly stepping weights opposite the "
        "gradient. Variants differ by how much data each step uses: **batch** (all data), "
        "**stochastic/SGD** (one sample), **mini-batch** (a small group). **Optimizers** improve "
        "plain SGD: **momentum** accelerates consistent directions, **RMSProp** adapts per-parameter "
        "step sizes, and **Adam** combines both — the popular default."
    ),
    "why": (
        "Optimization is how networks actually learn. The optimizer and learning rate dramatically "
        "affect whether training converges, how fast, and how well — among the most important "
        "practical choices in deep learning."
    ),
    "concepts": [
        ("Batch vs SGD", "All data per step (stable, slow) vs one sample (noisy, fast)."),
        ("Mini-batch", "A small batch — the practical sweet spot."),
        ("Learning rate", "Step size; the single most important hyperparameter."),
        ("Momentum", "Accumulate velocity to roll through small bumps and speed up."),
        ("Adam", "Adaptive per-parameter rates + momentum; strong default."),
        ("Convergence", "Loss decreasing and settling near a minimum."),
    ],
    "examples": [
        ("Plain gradient descent vs momentum", r'''
def f(x):    return x ** 2          # minimize -> minimum at x=0
def grad(x): return 2 * x

def descend(lr, momentum=0.0, steps=15):
    x, v = 10.0, 0.0
    for _ in range(steps):
        g = grad(x)
        v = momentum * v - lr * g    # velocity (0 momentum = plain GD)
        x += v
    return x

print("plain GD   (lr=0.1):", round(descend(0.1), 5))
print("with momentum 0.9  :", round(descend(0.1, momentum=0.9), 5))
# Momentum reaches the minimum faster by building up velocity.
'''),
        ("Learning rate: too small, good, too big", r'''
def grad(x): return 2 * x

def run(lr, steps=20):
    x = 10.0
    for _ in range(steps):
        x -= lr * grad(x)
        if abs(x) > 1e6:             # diverged
            return "DIVERGED"
    return round(x, 4)

for lr in [0.001, 0.1, 0.9, 1.01]:
    print(f"lr={lr:5}: x after 20 steps = {run(lr)}")
# tiny lr crawls; good lr converges; lr>=1 here overshoots/diverges.
'''),
        ("Adam from scratch, and framework optimizers", r'''
import math

def grad(x): return 2 * x

# Adam: adaptive moments (m = momentum, v = squared-grad average)
x, m, v = 10.0, 0.0, 0.0
lr, b1, b2, eps = 0.5, 0.9, 0.999, 1e-8
for t in range(1, 21):
    g = grad(x)
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * g * g
    m_hat = m / (1 - b1 ** t)          # bias correction
    v_hat = v / (1 - b2 ** t)
    x -= lr * m_hat / (math.sqrt(v_hat) + eps)
print("Adam result:", round(x, 4))

try:
    import torch
    w = torch.tensor([10.0], requires_grad=True)
    opt = torch.optim.Adam([w], lr=0.5)
    for _ in range(20):
        opt.zero_grad()
        loss = (w ** 2).sum()
        loss.backward()
        opt.step()
    print("torch Adam result:", round(w.item(), 4))
except ImportError:
    print("PyTorch not installed — run: pip install torch")
'''),
    ],
    "gotchas": [
        "Learning rate too high → divergence/NaN; too low → painfully slow or stuck.",
        "Always SHUFFLE data for SGD/mini-batch, or ordered batches bias the gradient.",
        "Adam is a great default but can generalize slightly worse than tuned SGD+momentum.",
        "Remember to zero gradients each step in frameworks, or they accumulate.",
        "Constant LR can stall near minima — learning-rate schedules/decay often help.",
    ],
    "exercises": [
        ("One GD step on f(x)=x^2 from x=5, lr=0.1.", "x -= lr*2x.",
         r'''x, lr = 5, 0.1
print(x - lr * 2 * x)  # 4.0'''),
        ("What does momentum add to GD?", "Velocity.",
         r'''#md
A **velocity** term that accumulates past gradients, so the optimizer accelerates in
consistent directions and rolls through small bumps/plateaus — faster convergence.'''),
        ("Batch vs stochastic GD: which uses one sample per step?", "Definition.",
         r'''#md
**Stochastic gradient descent (SGD)** uses **one sample** per update (noisy but
fast). Batch GD uses the whole dataset per step.'''),
        ("If lr=1.01 on f(x)=x^2, does it converge?", "Overshoot.",
         r'''#md
**No** — the step overshoots the minimum and grows each iteration (|x| increases),
so it **diverges**. The update needs lr < 1 here for stability.'''),
        ("Compute velocity v = 0.9*v - 0.1*g for v=0,g=4.", "Plug in.",
         r'''v, g = 0, 4
print(0.9 * v - 0.1 * g)  # -0.4'''),
        ("Which optimizer combines momentum and adaptive rates?", "Name it.",
         r'''#md
**Adam** — it keeps a momentum estimate (first moment) and a per-parameter adaptive
scale from squared gradients (second moment).'''),
        ("Why shuffle data for mini-batch GD?", "Avoid bias.",
         r'''#md
So consecutive batches aren't correlated/ordered (e.g. sorted by class), which would
bias each gradient estimate. Shuffling makes batches representative.'''),
        ("What's the most important hyperparameter in training?", "LR.",
         r'''#md
The **learning rate** — it controls step size and most directly determines whether
training converges, how fast, and how well.'''),
    ],
}

CONTENT["tensorflow-keras-pytorch"] = {
    "deps": ["tensorflow", "torch"],
    "what": (
        "**TensorFlow/Keras** and **PyTorch** are the two dominant deep-learning frameworks. They "
        "provide **tensors** (GPU-accelerated arrays), **automatic differentiation** (autograd, so "
        "you never hand-code backprop), prebuilt **layers/optimizers/losses**, and training "
        "utilities. **Keras** offers a simple high-level API; **PyTorch** is Pythonic and flexible "
        "(the research favorite)."
    ),
    "why": (
        "You won't implement backprop by hand in practice — frameworks make building, training, and "
        "deploying networks fast and GPU-accelerated. Knowing both (and their tensor/autograd model) "
        "is essential for real deep learning."
    ),
    "concepts": [
        ("Tensor", "An N-dimensional array (like NumPy) that can live on a GPU."),
        ("Autograd", "Automatic gradient computation — no manual backprop."),
        ("Keras Sequential", "Stack layers in a list for a quick model."),
        ("nn.Module", "PyTorch's base class for custom models."),
        ("Optimizer & loss", "Prebuilt SGD/Adam and MSE/cross-entropy."),
        ("GPU acceleration", "Move tensors/models to a GPU for speed."),
    ],
    "examples": [
        ("Tensors are like nested lists / NumPy arrays (concept)", r'''
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
'''),
        ("Build a model in Keras", r'''
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
'''),
        ("Build the same model in PyTorch", r'''
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
'''),
    ],
    "gotchas": [
        "Don't mix framework tensors with NumPy mid-graph — convert explicitly and watch the device.",
        "Keep tensors on the SAME device (CPU/GPU); mismatches raise runtime errors.",
        "PyTorch: call `optimizer.zero_grad()` before `backward()` each step.",
        "Keras expects the right input shape; the first layer needs `input_shape`/`Input`.",
        "Framework version differences (TF1 vs TF2, torch APIs) break old tutorials — check versions.",
    ],
    "exercises": [
        ("What is a tensor (one line)?", "Definition.",
         r'''#md
An **N-dimensional array** (scalar=0-D, vector=1-D, matrix=2-D, …) that frameworks
can run on a GPU and differentiate through.'''),
        ("What does autograd remove the need for?", "Manual backprop.",
         r'''#md
**Hand-coding backpropagation** — autograd records operations and computes gradients
automatically when you call backward().'''),
        ("Give the shape of [[1,2,3],[4,5,6]].", "rows x cols.",
         r'''m = [[1, 2, 3], [4, 5, 6]]
print((len(m), len(m[0])))  # (2, 3)'''),
        ("Which framework uses nn.Module?", "Recall.",
         r'''#md
**PyTorch** — custom models subclass `torch.nn.Module` (or use `nn.Sequential`).'''),
        ("Which Keras API stacks layers in a list?", "Recall.",
         r'''#md
**`keras.Sequential`** — pass a list of layers to build a simple feed-forward
stack.'''),
        ("Count params of a Dense layer: 4 inputs -> 3 units (with bias).", "in*out+out.",
         r'''print(4 * 3 + 3)  # 15'''),
        ("Why keep tensors on the same device?", "Compatibility.",
         r'''#md
Operations require all tensors on the **same device** (all CPU or all the same GPU);
mixing CPU and GPU tensors raises a runtime error.'''),
        ("In PyTorch, what call computes gradients?", "API.",
         r'''#md
**`loss.backward()`** — it backpropagates and populates each parameter's `.grad`,
which the optimizer then uses in `optimizer.step()`.'''),
    ],
}

CONTENT["building-anns"] = {
    "deps": ["tensorflow"],
    "what": (
        "An **Artificial Neural Network (ANN)** for tabular/structured data is a stack of fully "
        "connected (**Dense**) layers. The recipe: choose an architecture (layer sizes, "
        "activations), pick a **loss** and **optimizer**, then `fit` on training data and `evaluate` "
        "on test data. Output layer/activation depends on the task: 1 sigmoid (binary), softmax "
        "(multiclass), or linear (regression)."
    ),
    "why": (
        "ANNs are the entry point to building real models in a framework — turning the theory "
        "(neurons, activations, backprop, optimizers) into a working classifier/regressor with a few "
        "lines of Keras/PyTorch."
    ),
    "concepts": [
        ("Architecture", "Number of layers and neurons; the model's capacity."),
        ("Output layer", "sigmoid (binary), softmax (multiclass), linear (regression)."),
        ("Loss function", "binary/categorical cross-entropy or MSE — match the task."),
        ("fit / evaluate", "Train on data, then measure on held-out test data."),
        ("Epochs & batch size", "How many passes and how many samples per update."),
        ("Overfitting signs", "Train accuracy ≫ validation accuracy."),
    ],
    "examples": [
        ("A minimal multilayer perceptron forward pass (pure Python)", r'''
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
'''),
        ("Choosing output layer and loss by task", r'''
tasks = [
    ("binary classification", "1 neuron, sigmoid", "binary_crossentropy"),
    ("multiclass (3 classes)", "3 neurons, softmax", "categorical_crossentropy"),
    ("regression",            "1 neuron, linear",  "mse"),
]
print(f"{'task':24} | {'output layer':22} | loss")
print("-" * 70)
for task, out, loss in tasks:
    print(f"{task:24} | {out:22} | {loss}")
'''),
        ("Build and train an ANN with Keras", r'''
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
'''),
    ],
    "gotchas": [
        "Match output activation + loss to the task — softmax with MSE won't train well.",
        "Scale/normalize inputs; unscaled features slow or break training.",
        "Too many epochs overfits — watch validation loss and use early stopping.",
        "Use sparse_categorical_crossentropy for integer labels, categorical for one-hot.",
        "Start small — a giant network on little data just memorizes.",
    ],
    "exercises": [
        ("What output layer for binary classification?", "Recall.",
         r'''#md
**One neuron with a sigmoid** activation, paired with binary cross-entropy loss.'''),
        ("What output activation for 5-class classification?", "Recall.",
         r'''#md
**Softmax** over **5 neurons** (one per class), with categorical cross-entropy.'''),
        ("What loss for a regression ANN?", "Recall.",
         r'''#md
**Mean Squared Error (MSE)** (or MAE) — the output layer is a single linear
neuron.'''),
        ("Apply softmax to logits [1,2,3] (compute the max-prob class index).", "Argmax.",
         r'''import math
z = [1, 2, 3]; e = [math.exp(v) for v in z]; s = sum(e)
probs = [v / s for v in e]
print(probs.index(max(probs)))  # 2'''),
        ("Compute ReLU of hidden pre-activations [-0.5, 0.3, 2].", "max(0,z).",
         r'''print([max(0, z) for z in [-0.5, 0.3, 2]])  # [0, 0.3, 2]'''),
        ("Sign of overfitting in train/val accuracy?", "Gap.",
         r'''#md
**Training accuracy much higher than validation accuracy** (a large gap) signals the
model is memorizing training data rather than generalizing.'''),
        ("How many weights in Dense(8) fed by 4 inputs (no bias)?", "in*out.",
         r'''print(4 * 8)  # 32'''),
        ("Integer labels: which loss in Keras?", "Recall.",
         r'''#md
**sparse_categorical_crossentropy** — it accepts integer class labels directly (no
one-hot encoding needed).'''),
    ],
}

CONTENT["cnn"] = {
    "deps": ["tensorflow"],
    "what": (
        "A **Convolutional Neural Network (CNN)** is built for images. Instead of connecting every "
        "pixel to every neuron, it slides small **filters (kernels)** across the image to detect "
        "local patterns (edges, textures), producing **feature maps**. **Pooling** layers downsample "
        "to shrink size and add invariance. Stacked conv+pool layers learn a hierarchy: edges → "
        "shapes → objects, with far fewer parameters than a dense net."
    ),
    "why": (
        "CNNs revolutionized computer vision (classification, detection, segmentation, medical "
        "imaging). Weight sharing and locality make them efficient and translation-invariant — the "
        "right inductive bias for images."
    ),
    "concepts": [
        ("Convolution", "Slide a kernel over the image; each position is a dot product."),
        ("Kernel/filter", "Small weight grid that detects a local pattern."),
        ("Feature map", "The output of applying a filter across the image."),
        ("Pooling", "Downsample (max/avg) to reduce size and add invariance."),
        ("Weight sharing", "The same kernel is reused everywhere — few parameters."),
        ("Hierarchy", "Early layers find edges; deeper layers find objects."),
    ],
    "examples": [
        ("2-D convolution from scratch (edge detection)", r'''
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
'''),
        ("Max pooling downsamples a feature map", r'''
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
'''),
        ("A CNN with Keras", r'''
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
'''),
    ],
    "gotchas": [
        "Convolution shrinks the image (output = input − kernel + 1); use padding='same' to preserve size.",
        "Feed images with a channel dimension (H×W×C); forgetting it causes shape errors.",
        "Normalize pixel values (e.g. /255) — raw 0–255 inputs slow training.",
        "Too many conv filters/dense units overfit small datasets — use dropout/augmentation.",
        "Pooling loses spatial precision; for segmentation you need it back (upsampling/U-Net).",
    ],
    "exercises": [
        ("Output size of a 5x5 image with a 3x3 kernel (no padding)?", "in-k+1.",
         r'''print(5 - 3 + 1)  # 3'''),
        ("Convolve [1,2,3,4] (1-D) with kernel [1,-1]: first output.", "Dot product.",
         r'''img, k = [1, 2, 3, 4], [1, -1]
print(img[0] * k[0] + img[1] * k[1])  # -1'''),
        ("2x2 max-pool the block [[1,4],[3,2]].", "Take max.",
         r'''block = [[1, 4], [3, 2]]
print(max(v for row in block for v in row))  # 4'''),
        ("Why do CNNs use weight sharing?", "Efficiency.",
         r'''#md
The same kernel is applied across the whole image, so the network learns
**position-independent** features with **far fewer parameters** than a fully
connected layer (and gains translation invariance).'''),
        ("What does a pooling layer do?", "Downsample.",
         r'''#md
**Downsamples** feature maps (e.g. 2×2 max pooling), reducing spatial size and
computation while adding small-shift invariance.'''),
        ("Output size of 28x28 image with 3x3 kernel, padding='same'?", "Same.",
         r'''#md
**28×28** — 'same' padding adds a border so the output keeps the input's spatial
dimensions.'''),
        ("What do early conv layers typically detect?", "Low-level.",
         r'''#md
Low-level features like **edges, corners, and simple textures**. Deeper layers
combine these into shapes and eventually whole objects.'''),
        ("Flatten a 2x2 feature map [[1,2],[3,4]] to a vector.", "Row-major.",
         r'''m = [[1, 2], [3, 4]]
print([v for row in m for v in row])  # [1, 2, 3, 4]'''),
    ],
}

CONTENT["rnn-lstm-gru"] = {
    "deps": ["tensorflow"],
    "what": (
        "**Recurrent Neural Networks (RNNs)** process **sequences** (text, time series, audio) by "
        "maintaining a **hidden state** that carries information from previous steps: hₜ = "
        "tanh(Wₓxₜ + Wₕhₜ₋₁ + b). Plain RNNs forget long-range context (vanishing gradients). "
        "**LSTM** and **GRU** add **gates** that learn what to keep, forget, and output — capturing "
        "long-term dependencies."
    ),
    "why": (
        "Sequence data is everywhere — language, stock prices, sensor streams. RNNs/LSTMs were the "
        "backbone of NLP and forecasting before transformers, and the gated-memory idea is "
        "fundamental to understanding sequence modeling."
    ),
    "concepts": [
        ("Hidden state", "Memory passed from one time step to the next."),
        ("Recurrence", "Same weights applied at every step of the sequence."),
        ("Vanishing gradient", "Plain RNNs lose long-range signal during backprop."),
        ("LSTM gates", "Forget/input/output gates manage a cell state."),
        ("GRU", "Simpler gating (reset/update) — fewer params than LSTM."),
        ("Sequence I/O", "Many-to-one (classify), many-to-many (translate)."),
    ],
    "examples": [
        ("A simple RNN cell processing a sequence (pure Python)", r'''
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
'''),
        ("A scalar LSTM cell with gates (pure Python)", r'''
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
'''),
        ("LSTM/GRU with Keras", r'''
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
'''),
    ],
    "gotchas": [
        "Plain RNNs suffer vanishing/exploding gradients on long sequences — use LSTM/GRU.",
        "Sequences in a batch must be padded to equal length (and masked) — don't ignore padding.",
        "LSTMs are slow to train (sequential, can't fully parallelize over time).",
        "Watch input shape: Keras RNNs expect (batch, timesteps, features).",
        "For very long-range dependencies, transformers usually beat RNNs now.",
    ],
    "exercises": [
        ("Compute one RNN step h=tanh(0.5*x+0.8*h) for x=1,h=0.", "Plug in.",
         r'''import math
print(round(math.tanh(0.5 * 1 + 0.8 * 0), 4))  # 0.4621'''),
        ("What problem do LSTMs solve vs plain RNNs?", "Long memory.",
         r'''#md
**Vanishing gradients / short memory.** LSTM gates and a cell state let gradients
flow over many steps, capturing **long-range dependencies** plain RNNs lose.'''),
        ("Name the three LSTM gates.", "Recall.",
         r'''#md
**Forget**, **input**, and **output** gates (operating on a cell state).'''),
        ("Which is simpler/lighter: LSTM or GRU?", "Param count.",
         r'''#md
**GRU** — it merges gates (reset/update, no separate cell state), so it has fewer
parameters and trains faster, often with comparable accuracy.'''),
        ("What input shape does a Keras LSTM expect?", "Recall.",
         r'''#md
**(batch, timesteps, features)** — a 3-D tensor where each sample is a sequence of
feature vectors.'''),
        ("Compute a forget gate sigmoid(0.5*2+0.1*0).", "Sigmoid.",
         r'''import math
print(round(1 / (1 + math.exp(-(0.5 * 2 + 0.1 * 0))), 4))  # 0.7311'''),
        ("Many-to-one RNN: give an example task.", "Sequence in, label out.",
         r'''#md
**Sentiment classification** (read a sentence → output positive/negative), or any
task that consumes a whole sequence and emits a single label/value.'''),
        ("Why pad sequences in a batch?", "Equal length.",
         r'''#md
Tensors must be rectangular, so variable-length sequences are **padded to the same
length** (with a mask so the model ignores the padding).'''),
    ],
}

CONTENT["dropout-and-batchnorm"] = {
    "deps": ["tensorflow"],
    "what": (
        "**Dropout** randomly 'drops' (zeros) a fraction of neurons during training, forcing the "
        "network to not rely on any single unit — a powerful **regularizer** against overfitting. "
        "**Batch Normalization** normalizes each layer's inputs to zero mean/unit variance per "
        "mini-batch (then rescales with learnable γ, β), which **stabilizes and speeds up** "
        "training and allows higher learning rates."
    ),
    "why": (
        "These two layers are standard tools for training deep networks reliably: dropout combats "
        "overfitting, batch norm smooths the loss landscape so training converges faster and is less "
        "sensitive to initialization."
    ),
    "concepts": [
        ("Dropout", "Randomly zero neurons during training; keep all at inference."),
        ("Inverted dropout", "Scale survivors by 1/(1−p) so the expected value is unchanged."),
        ("Train vs eval mode", "Dropout/BN behave differently in training vs inference."),
        ("Batch norm", "Normalize layer inputs over the batch, then scale/shift."),
        ("Internal covariate shift", "BN reduces shifting input distributions across layers."),
        ("Regularization", "Dropout (and BN slightly) reduce overfitting."),
    ],
    "examples": [
        ("Dropout (inverted) in train vs eval mode", r'''
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
'''),
        ("Batch normalization of a layer's activations", r'''
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
'''),
        ("Dropout and BatchNorm layers in Keras", r'''
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
'''),
    ],
    "gotchas": [
        "Dropout is ON only during training — it must be OFF at inference (frameworks handle this).",
        "Use inverted dropout (scale by 1/(1−p)) so activations have the same expected scale.",
        "Batch norm behaves differently in train (batch stats) vs eval (running averages).",
        "Very small batch sizes make batch-norm statistics noisy — consider LayerNorm/GroupNorm.",
        "Too-high dropout (e.g. 0.8) can underfit — 0.2–0.5 is typical.",
    ],
    "exercises": [
        ("With dropout p=0.5 inverted, scale a surviving activation of 3.", "/ (1-p).",
         r'''p = 0.5
print(3 / (1 - p))  # 6.0'''),
        ("Is dropout active during inference?", "Recall.",
         r'''#md
**No.** Dropout is applied only during **training**; at inference all neurons are
used (the framework switches it off automatically).'''),
        ("Normalize [2,4,6] to zero mean (subtract mean).", "x - mean.",
         r'''d = [2, 4, 6]
m = sum(d) / len(d)
print([x - m for x in d])  # [-2, 0, 2]'''),
        ("After batch norm, what are the mean and variance (before scale/shift)?", "Recall.",
         r'''#md
**Mean 0 and variance 1** — batch norm standardizes the activations, then applies
learnable scale (γ) and shift (β).'''),
        ("What does dropout help prevent?", "Overfitting.",
         r'''#md
**Overfitting** — by randomly dropping units it stops the network from co-adapting/
relying on specific neurons, acting as a regularizer.'''),
        ("Compute batch variance of [1,3] (population).", "pvariance.",
         r'''import statistics as st
print(st.pvariance([1, 3]))  # 1.0'''),
        ("Why does batch norm allow higher learning rates?", "Stability.",
         r'''#md
By keeping each layer's input distribution stable (mean 0 / var 1), BN **smooths the
loss landscape**, reducing the risk of exploding activations — so larger, faster
learning-rate steps stay stable.'''),
        ("Typical dropout rate range?", "Recall.",
         r'''#md
Commonly **0.2 to 0.5**. Too high (e.g. 0.8) removes so much signal it can cause
underfitting.'''),
    ],
}

CONTENT["transfer-learning"] = {
    "deps": ["tensorflow"],
    "what": (
        "**Transfer learning** reuses a model **pretrained** on a huge dataset (e.g. ImageNet, or a "
        "language corpus) for a new, related task with little data. You keep the pretrained **feature "
        "extractor** (often **frozen**) and train a small new **head** on top. **Fine-tuning** then "
        "optionally unfreezes some upper layers and trains them at a low learning rate."
    ),
    "why": (
        "Training big models from scratch needs massive data and compute. Transfer learning gives "
        "state-of-the-art results with a few hundred examples and minutes of training — the default "
        "approach for most real vision and NLP tasks today."
    ),
    "concepts": [
        ("Pretrained model", "Weights learned on a large general dataset."),
        ("Feature extractor", "Reuse the pretrained body that produces rich features."),
        ("Freezing", "Mark layers non-trainable so their weights don't update."),
        ("New head", "A fresh small classifier trained for your task."),
        ("Fine-tuning", "Unfreeze upper layers and train at a low learning rate."),
        ("Data efficiency", "Great results from little task-specific data."),
    ],
    "examples": [
        ("Freezing: only the new head is trainable", r'''
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
'''),
        ("Transfer learning concretely: frozen extractor + trained head", r'''
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
'''),
        ("Transfer learning with Keras (frozen base + new head)", r'''
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
'''),
    ],
    "gotchas": [
        "Freeze the base FIRST and train the head; only then fine-tune upper layers (low LR).",
        "Use the SAME preprocessing the base model was trained with (resize, normalization).",
        "Fine-tuning with a high learning rate destroys pretrained weights — use a small one.",
        "If your task is very different from the pretraining data, transfer helps less.",
        "Match input size/channels to what the pretrained model expects.",
    ],
    "exercises": [
        ("If base has 14M frozen params and head 50k trainable, how many train?", "Only head.",
         r'''print(50_000)  # only the head's params update'''),
        ("What does 'freezing' a layer mean?", "No updates.",
         r'''#md
Marking it **non-trainable** so its weights are **not updated** during
backpropagation — the pretrained features are reused as-is.'''),
        ("Why use a pretrained model?", "Data/compute.",
         r'''#md
It already learned general features from a huge dataset, so you get strong results
with **little task data and compute** instead of training from scratch.'''),
        ("Order: freeze-then-finetune or finetune-then-freeze?", "Recall.",
         r'''#md
**Freeze first** (train the new head on frozen features), **then optionally
fine-tune** some upper layers at a low learning rate.'''),
        ("Why a LOW learning rate when fine-tuning?", "Preserve weights.",
         r'''#md
To make small adjustments that **preserve the valuable pretrained weights**; a high
LR would overwrite them and destroy the learned features.'''),
        ("Compute the trainable fraction: 50k of 14.05M total.", "Ratio.",
         r'''print(round(50_000 / 14_050_000, 4))  # ~0.0036'''),
        ("Must input preprocessing match the pretrained model?", "Yes.",
         r'''#md
**Yes** — use the same resizing and normalization the base model was trained with,
or the features will be meaningless.'''),
        ("Name a domain where transfer learning is standard.", "Vision/NLP.",
         r'''#md
**Computer vision** (ImageNet-pretrained CNNs) and **NLP** (pretrained transformers
like BERT/GPT) — both routinely fine-tune large pretrained models.'''),
    ],
}


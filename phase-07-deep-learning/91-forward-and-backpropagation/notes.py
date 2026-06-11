# ======================================================================
# 91 — Forward and Backpropagation  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: torch
# Install:  pip install torch

# ----------------------------------------------------------------------
# Example 1: Train a network to learn XOR with backprop (pure Python)
# ----------------------------------------------------------------------
print("\n--- Example 1: Train a network to learn XOR with backprop (pure Python) ---")
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

# ----------------------------------------------------------------------
# Example 2: One forward + backward step, gradients shown
# ----------------------------------------------------------------------
print("\n--- Example 2: One forward + backward step, gradients shown ---")
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

# ----------------------------------------------------------------------
# Example 3: Autograd with PyTorch
# ----------------------------------------------------------------------
print("\n--- Example 3: Autograd with PyTorch ---")
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

print("\nDone! Tip: change values above and run again to learn by experiment.")

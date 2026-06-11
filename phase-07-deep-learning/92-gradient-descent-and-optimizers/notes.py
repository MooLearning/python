# ======================================================================
# 92 — Gradient Descent and Optimizers  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: torch
# Install:  pip install torch

# ----------------------------------------------------------------------
# Example 1: Plain gradient descent vs momentum
# ----------------------------------------------------------------------
print("\n--- Example 1: Plain gradient descent vs momentum ---")
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

# ----------------------------------------------------------------------
# Example 2: Learning rate: too small, good, too big
# ----------------------------------------------------------------------
print("\n--- Example 2: Learning rate: too small, good, too big ---")
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

# ----------------------------------------------------------------------
# Example 3: Adam from scratch, and framework optimizers
# ----------------------------------------------------------------------
print("\n--- Example 3: Adam from scratch, and framework optimizers ---")
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

print("\nDone! Tip: change values above and run again to learn by experiment.")

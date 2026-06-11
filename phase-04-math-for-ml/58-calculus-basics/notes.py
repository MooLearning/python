# ======================================================================
# 58 — Calculus Basics  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Numerical derivative (slope) via finite differences
# ----------------------------------------------------------------------
print("\n--- Example 1: Numerical derivative (slope) via finite differences ---")
def derivative(f, x, h=1e-6):
    # central difference: more accurate than (f(x+h)-f(x))/h
    return (f(x + h) - f(x - h)) / (2 * h)

f = lambda x: x ** 2          # f'(x) = 2x
print("f'(3)  ~", round(derivative(f, 3), 4))   # 6.0
print("f'(0)  ~", round(derivative(f, 0), 4))   # 0.0

g = lambda x: x ** 3          # g'(x) = 3x^2
print("g'(2)  ~", round(derivative(g, 2), 4))   # 12.0

# ----------------------------------------------------------------------
# Example 2: Numerical integration (area under the curve)
# ----------------------------------------------------------------------
print("\n--- Example 2: Numerical integration (area under the curve) ---")
def integrate(f, a, b, n=10000):
    # trapezoidal rule: split [a,b] into n strips
    h = (b - a) / n
    total = (f(a) + f(b)) / 2
    for i in range(1, n):
        total += f(a + i * h)
    return total * h

f = lambda x: x ** 2          # integral of x^2 from 0..1 = 1/3
print("area x^2 [0,1] ~", round(integrate(f, 0, 1), 5))   # 0.33333

import math
print("area sin [0,pi] ~", round(integrate(math.sin, 0, math.pi), 5))  # 2.0

# ----------------------------------------------------------------------
# Example 3: Gradient descent: minimize f(x) = (x - 3)^2
# ----------------------------------------------------------------------
print("\n--- Example 3: Gradient descent: minimize f(x) = (x - 3)^2 ---")
def f(x):       return (x - 3) ** 2
def grad(x):    return 2 * (x - 3)        # derivative

x = 0.0            # starting guess
lr = 0.1           # learning rate
for step in range(50):
    x = x - lr * grad(x)                  # step downhill
    if step % 10 == 0:
        print(f"step {step:2d}: x={x:.4f}, f(x)={f(x):.4f}")

print("minimum near x =", round(x, 4))    # ~3.0 (the true minimum)

print("\nDone! Tip: change values above and run again to learn by experiment.")

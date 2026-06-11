# 58 — Calculus Basics

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Calculus** studies change. The **derivative** measures the instantaneous rate of change (the slope) of a function; the **integral** measures accumulated area under a curve. In ML the key idea is the **gradient** (the vector of partial derivatives), which points uphill — so stepping in the OPPOSITE direction (**gradient descent**) minimizes a loss function. That single idea trains almost every model.

## Why it matters

Training a model = minimizing a loss, and we minimize by following negative gradients. Understanding derivatives, the chain rule, and gradient descent demystifies how neural networks actually learn.

## Key concepts

- **Derivative** — Slope/rate of change of f at a point: f'(x).
- **Finite difference** — Estimate a derivative numerically: (f(x+h)−f(x−h))/2h.
- **Integral** — Accumulated area under f; estimate with Riemann/trapezoid sums.
- **Gradient** — Vector of partial derivatives for a multivariable function.
- **Gradient descent** — Step x ← x − lr·f'(x) to move toward a minimum.
- **Learning rate** — Step size; too big overshoots, too small crawls.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
def derivative(f, x, h=1e-6):
    # central difference: more accurate than (f(x+h)-f(x))/h
    return (f(x + h) - f(x - h)) / (2 * h)

f = lambda x: x ** 2          # f'(x) = 2x
print("f'(3)  ~", round(derivative(f, 3), 4))   # 6.0
print("f'(0)  ~", round(derivative(f, 0), 4))   # 0.0

g = lambda x: x ** 3          # g'(x) = 3x^2
print("g'(2)  ~", round(derivative(g, 2), 4))   # 12.0
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Finite-difference h too small → floating-point noise; too large → inaccurate. 1e-6 is a good default.
- ⚠️ Gradient descent with too large a learning rate DIVERGES (values blow up).
- ⚠️ Following the POSITIVE gradient climbs (maximizes); subtract it to minimize.
- ⚠️ A non-convex loss can trap gradient descent in a local minimum, not the global one.
- ⚠️ Forgetting the chain rule when composing functions gives wrong derivatives.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


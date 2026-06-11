# -*- coding: utf-8 -*-
"""Phase 4 — Math for ML content.

Core examples use only the standard library (math, statistics, random) so every
notes.py runs with no installs. NumPy demos are guarded with try/except.
"""

CONTENT = {}

CONTENT["linear-algebra"] = {
    "what": (
        "**Linear algebra** is the math of **vectors** (ordered lists of numbers) and **matrices** "
        "(grids of numbers). Core operations are vector addition, **dot products**, **matrix "
        "multiplication**, and **transpose**. Machine learning represents data as vectors/matrices "
        "and expresses models (a linear layer, a rotation, a projection) as matrix operations — so "
        "this is the language ML is written in."
    ),
    "why": (
        "Every dataset is a matrix (rows = samples, columns = features); every neural-network layer "
        "is a matrix multiply. Understanding dot products, shapes, and matrix multiply makes ML "
        "math (and NumPy/PyTorch code) click instead of feeling like magic."
    ),
    "concepts": [
        ("Vector", "An ordered list of numbers; a point/arrow in n-D space."),
        ("Dot product", "Sum of elementwise products; measures alignment/similarity."),
        ("Matrix", "A 2-D grid; shape (rows, cols)."),
        ("Matrix multiply", "(m×n)·(n×p) → (m×p); inner dimensions must match."),
        ("Transpose", "Flip rows and columns: shape (m,n) → (n,m)."),
        ("Magnitude (norm)", "Length of a vector: sqrt(sum of squares)."),
    ],
    "examples": [
        ("Vectors: add, scale, dot product, magnitude", r'''
import math

def add(u, v):       return [a + b for a, b in zip(u, v)]
def scale(k, v):     return [k * x for x in v]
def dot(u, v):       return sum(a * b for a, b in zip(u, v))
def magnitude(v):    return math.sqrt(dot(v, v))

u = [1, 2, 3]
v = [4, 5, 6]
print("u + v   :", add(u, v))        # [5, 7, 9]
print("3 * u   :", scale(3, u))      # [3, 6, 9]
print("u . v   :", dot(u, v))        # 32  (1*4 + 2*5 + 3*6)
print("|u|     :", round(magnitude(u), 4))   # 3.7417

# Cosine similarity = dot / (|u| * |v|)  -> how aligned two vectors are
cos_sim = dot(u, v) / (magnitude(u) * magnitude(v))
print("cos_sim :", round(cos_sim, 4))        # 0.9746
'''),
        ("Matrices: transpose and multiply (pure Python)", r'''
def transpose(M):
    # swap rows and columns
    return [[M[r][c] for r in range(len(M))] for c in range(len(M[0]))]

def matmul(A, B):
    # A is (m x n), B is (n x p) -> result is (m x p)
    n = len(B)
    assert len(A[0]) == n, "inner dimensions must match"
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(len(B[0]))]
            for i in range(len(A))]

A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]
print("A^T   :", transpose(A))   # [[1, 3], [2, 4]]
print("A x B :", matmul(A, B))   # [[19, 22], [43, 50]]

# Matrix-vector product: treat the vector as a column
v = [[1], [1]]
print("A x v :", matmul(A, v))   # [[3], [7]]
'''),
        ("The same with NumPy (if installed)", r'''
try:
    import numpy as np
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print("shapes:", A.shape, B.shape)
    print("A @ B =\n", A @ B)              # matrix multiply
    print("A.T   =\n", A.T)                # transpose
    print("dot   :", np.dot([1, 2, 3], [4, 5, 6]))   # 32

    # Solve a linear system  A x = b
    Acoef = np.array([[2.0, 1.0], [1.0, 3.0]])
    b = np.array([5.0, 10.0])
    x = np.linalg.solve(Acoef, b)
    print("solution x:", np.round(x, 3))   # [1. 3.]
except ImportError:
    print("NumPy not installed — run: pip install numpy")
    print("(the pure-Python examples above already show the same math)")
'''),
    ],
    "gotchas": [
        "Matrix multiply needs matching INNER dimensions: (m×n)·(n×p). Mismatched shapes error.",
        "Matrix multiplication is NOT commutative: A·B ≠ B·A in general.",
        "The dot product needs equal-length vectors — zip silently stops at the shorter one!",
        "`*` on NumPy arrays is ELEMENTWISE; matrix multiply is `@` or `np.dot`.",
        "Mixing row vectors and column vectors causes shape bugs — track shapes deliberately.",
    ],
    "exercises": [
        ("Compute the dot product of [1,2,3] and [4,5,6].", "Sum of products.",
         r'''def dot(u, v):
    return sum(a * b for a, b in zip(u, v))
print(dot([1, 2, 3], [4, 5, 6]))  # 32'''),
        ("Add the vectors [1,1] and [2,3].", "Elementwise.",
         r'''def add(u, v):
    return [a + b for a, b in zip(u, v)]
print(add([1, 1], [2, 3]))  # [3, 4]'''),
        ("Find the magnitude (length) of [3,4].", "sqrt of sum of squares.",
         r'''import math
v = [3, 4]
print(math.sqrt(sum(x * x for x in v)))  # 5.0'''),
        ("Transpose the matrix [[1,2,3],[4,5,6]].", "Rows become columns.",
         r'''M = [[1, 2, 3], [4, 5, 6]]
T = [[M[r][c] for r in range(len(M))] for c in range(len(M[0]))]
print(T)  # [[1,4],[2,5],[3,6]]'''),
        ("Multiply [[1,0],[0,1]] (identity) by [[5,6],[7,8]].", "Identity returns the matrix.",
         r'''def matmul(A, B):
    n = len(B)
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(len(B[0]))] for i in range(len(A))]
print(matmul([[1, 0], [0, 1]], [[5, 6], [7, 8]]))  # [[5,6],[7,8]]'''),
        ("Scale the vector [1,2,3] by 0.5.", "Multiply each element.",
         r'''v = [1, 2, 3]
print([0.5 * x for x in v])  # [0.5, 1.0, 1.5]'''),
        ("Compute cosine similarity between [1,0] and [0,1].", "Orthogonal -> 0.",
         r'''import math
def dot(u, v): return sum(a * b for a, b in zip(u, v))
def mag(v): return math.sqrt(dot(v, v))
u, v = [1, 0], [0, 1]
print(dot(u, v) / (mag(u) * mag(v)))  # 0.0'''),
        ("Multiply matrix [[1,2],[3,4]] by column vector [[1],[1]].", "(2x2)x(2x1)->(2x1).",
         r'''def matmul(A, B):
    n = len(B)
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(len(B[0]))] for i in range(len(A))]
print(matmul([[1, 2], [3, 4]], [[1], [1]]))  # [[3],[7]]'''),
    ],
}

CONTENT["calculus-basics"] = {
    "what": (
        "**Calculus** studies change. The **derivative** measures the instantaneous rate of change "
        "(the slope) of a function; the **integral** measures accumulated area under a curve. In ML "
        "the key idea is the **gradient** (the vector of partial derivatives), which points uphill — "
        "so stepping in the OPPOSITE direction (**gradient descent**) minimizes a loss function. "
        "That single idea trains almost every model."
    ),
    "why": (
        "Training a model = minimizing a loss, and we minimize by following negative gradients. "
        "Understanding derivatives, the chain rule, and gradient descent demystifies how neural "
        "networks actually learn."
    ),
    "concepts": [
        ("Derivative", "Slope/rate of change of f at a point: f'(x)."),
        ("Finite difference", "Estimate a derivative numerically: (f(x+h)−f(x−h))/2h."),
        ("Integral", "Accumulated area under f; estimate with Riemann/trapezoid sums."),
        ("Gradient", "Vector of partial derivatives for a multivariable function."),
        ("Gradient descent", "Step x ← x − lr·f'(x) to move toward a minimum."),
        ("Learning rate", "Step size; too big overshoots, too small crawls."),
    ],
    "examples": [
        ("Numerical derivative (slope) via finite differences", r'''
def derivative(f, x, h=1e-6):
    # central difference: more accurate than (f(x+h)-f(x))/h
    return (f(x + h) - f(x - h)) / (2 * h)

f = lambda x: x ** 2          # f'(x) = 2x
print("f'(3)  ~", round(derivative(f, 3), 4))   # 6.0
print("f'(0)  ~", round(derivative(f, 0), 4))   # 0.0

g = lambda x: x ** 3          # g'(x) = 3x^2
print("g'(2)  ~", round(derivative(g, 2), 4))   # 12.0
'''),
        ("Numerical integration (area under the curve)", r'''
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
'''),
        ("Gradient descent: minimize f(x) = (x - 3)^2", r'''
def f(x):       return (x - 3) ** 2
def grad(x):    return 2 * (x - 3)        # derivative

x = 0.0            # starting guess
lr = 0.1           # learning rate
for step in range(50):
    x = x - lr * grad(x)                  # step downhill
    if step % 10 == 0:
        print(f"step {step:2d}: x={x:.4f}, f(x)={f(x):.4f}")

print("minimum near x =", round(x, 4))    # ~3.0 (the true minimum)
'''),
    ],
    "gotchas": [
        "Finite-difference h too small → floating-point noise; too large → inaccurate. 1e-6 is a good default.",
        "Gradient descent with too large a learning rate DIVERGES (values blow up).",
        "Following the POSITIVE gradient climbs (maximizes); subtract it to minimize.",
        "A non-convex loss can trap gradient descent in a local minimum, not the global one.",
        "Forgetting the chain rule when composing functions gives wrong derivatives.",
    ],
    "exercises": [
        ("Estimate the derivative of x^2 at x=5.", "Central difference.",
         r'''def deriv(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)
print(round(deriv(lambda x: x ** 2, 5)))  # 10'''),
        ("Estimate the derivative of x^3 at x=1.", "Should be 3.",
         r'''def deriv(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)
print(round(deriv(lambda x: x ** 3, 1)))  # 3'''),
        ("Approximate the area under x from 0 to 2.", "Triangle area = 2.",
         r'''def integrate(f, a, b, n=1000):
    h = (b - a) / n
    return h * (f(a)/2 + f(b)/2 + sum(f(a + i*h) for i in range(1, n)))
print(round(integrate(lambda x: x, 0, 2)))  # 2'''),
        ("Do one gradient-descent step on f(x)=(x-3)^2 from x=0, lr=0.1.", "x -= lr*2(x-3).",
         r'''x = 0.0; lr = 0.1
x = x - lr * 2 * (x - 3)
print(x)  # 0.6'''),
        ("What learning rate behavior causes divergence? Explain briefly.", "Too large.",
         r'''#md
A learning rate that is **too large** makes each step overshoot the minimum and
land farther away, so |x| grows every step and f(x) blows up — **divergence**. A
smaller learning rate converges (just more slowly).'''),
        ("Find the minimum of f(x)=x^2+4x+4 with gradient descent.", "Derivative 2x+4.",
         r'''def grad(x): return 2 * x + 4
x = 0.0
for _ in range(100):
    x -= 0.1 * grad(x)
print(round(x))  # -2'''),
        ("Numerically check that the derivative of sin at 0 is 1.", "cos(0)=1.",
         r'''import math
def deriv(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)
print(round(deriv(math.sin, 0)))  # 1'''),
        ("Minimize f(x,y)=x^2+y^2 with gradient descent (start (3,4)).", "Grad=(2x,2y).",
         r'''x, y = 3.0, 4.0
for _ in range(100):
    x -= 0.1 * 2 * x
    y -= 0.1 * 2 * y
print(round(x, 2), round(y, 2))  # 0.0 0.0'''),
    ],
}

CONTENT["probability-and-statistics"] = {
    "what": (
        "**Statistics** summarizes data (mean, median, variance, standard deviation, correlation); "
        "**probability** quantifies uncertainty (the chance of events between 0 and 1). Together "
        "they let us describe datasets, reason about randomness, and judge whether a pattern is real "
        "or noise. Python's `statistics` module and `random` module cover the basics with no "
        "installs."
    ),
    "why": (
        "ML is applied statistics: we estimate parameters from samples, measure spread and "
        "relationships, and quantify confidence. Mean/variance/correlation and basic probability "
        "(including Bayes' theorem) underpin metrics, feature analysis, and model evaluation."
    ),
    "concepts": [
        ("Mean / median / mode", "Center of data: average, middle value, most frequent."),
        ("Variance / std dev", "Spread: average squared distance from the mean (and its root)."),
        ("Probability", "Chance of an event in [0, 1]; complement is 1 − P."),
        ("Combinations", "Count ways to choose k of n (order ignored): n!/(k!(n−k)!)."),
        ("Correlation", "How two variables move together, from −1 to +1."),
        ("Bayes' theorem", "Update a probability given new evidence."),
    ],
    "examples": [
        ("Descriptive statistics with the statistics module", r'''
import statistics as st

data = [4, 8, 15, 16, 23, 42]
print("mean    :", st.mean(data))                 # 18
print("median  :", st.median(data))               # 15.5
print("stdev   :", round(st.stdev(data), 3))      # sample std dev
print("variance:", round(st.variance(data), 3))   # sample variance

scores = [90, 85, 85, 70, 95, 85]
print("mode    :", st.mode(scores))               # 85 (most frequent)

# Compute the mean and variance by hand to see the formula
n = len(data)
mean = sum(data) / n
var = sum((x - mean) ** 2 for x in data) / n      # population variance
print("by hand : mean =", mean, " pop_var =", round(var, 3))
'''),
        ("Probability: simulation, combinations, complement", r'''
import random
from math import comb

random.seed(42)                       # reproducible results

# Simulate rolling a die 10,000 times; estimate P(roll >= 5)
rolls = [random.randint(1, 6) for _ in range(10_000)]
p_ge_5 = sum(1 for r in rolls if r >= 5) / len(rolls)
print("P(roll >= 5) ~", round(p_ge_5, 3), " (theory 0.333)")

# Combinations: how many 2-card hands from 5 cards?
print("C(5, 2) =", comb(5, 2))        # 10

# Probability of at least one head in 3 coin flips = 1 - P(no heads)
p_no_heads = (1 / 2) ** 3
print("P(>=1 head in 3) =", 1 - p_no_heads)   # 0.875
'''),
        ("Correlation, covariance, and Bayes' theorem", r'''
import statistics as st

hours = [1, 2, 3, 4, 5]
scores = [52, 60, 67, 75, 81]         # study hours vs test score

# Pearson correlation (built in since Python 3.10)
print("correlation:", round(st.correlation(hours, scores), 4))   # ~0.999
print("covariance :", round(st.covariance(hours, scores), 4))

# Bayes' theorem: P(disease | positive test)
# Given: prevalence, test sensitivity, false-positive rate
p_disease = 0.01
p_pos_given_disease = 0.99            # sensitivity
p_pos_given_healthy = 0.05           # false positive rate
p_pos = (p_pos_given_disease * p_disease +
         p_pos_given_healthy * (1 - p_disease))
p_disease_given_pos = (p_pos_given_disease * p_disease) / p_pos
print("P(disease | +test) =", round(p_disease_given_pos, 4))   # ~0.1667
'''),
    ],
    "gotchas": [
        "Sample variance divides by (n−1); population variance divides by n — know which you need.",
        "The mean is sensitive to outliers; the median is robust — report both for skewed data.",
        "Correlation is NOT causation — a strong correlation can be coincidental or confounded.",
        "Probabilities must lie in [0, 1] and a full set of outcomes must sum to 1.",
        "Bayes surprises people: a 99%-accurate test can still mostly flag healthy people if the disease is rare.",
    ],
    "exercises": [
        ("Compute the mean of [2,4,6,8].", "Sum / count.",
         r'''data = [2, 4, 6, 8]
print(sum(data) / len(data))  # 5.0'''),
        ("Find the median of [7,1,3,9,5].", "Sort, take middle.",
         r'''import statistics as st
print(st.median([7, 1, 3, 9, 5]))  # 5'''),
        ("Compute the population variance of [1,2,3,4,5].", "Mean squared deviation.",
         r'''data = [1, 2, 3, 4, 5]
m = sum(data) / len(data)
print(sum((x - m) ** 2 for x in data) / len(data))  # 2.0'''),
        ("What is P(even) when rolling a fair die?", "3 of 6 outcomes.",
         r'''print(3 / 6)  # 0.5'''),
        ("How many ways to choose 3 from 6 (combinations)?", "math.comb.",
         r'''from math import comb
print(comb(6, 3))  # 20'''),
        ("Find the mode of [1,2,2,3,3,3,4].", "Most frequent.",
         r'''import statistics as st
print(st.mode([1, 2, 2, 3, 3, 3, 4]))  # 3'''),
        ("Compute P(at least one 6 in two rolls).", "1 - P(no 6).",
         r'''p_no_six = (5 / 6) ** 2
print(round(1 - p_no_six, 4))  # 0.3056'''),
        ("Estimate P(heads) from 10000 simulated coin flips.", "random + count.",
         r'''import random
random.seed(0)
flips = [random.choice("HT") for _ in range(10000)]
print(round(flips.count("H") / len(flips), 2))  # ~0.5'''),
    ],
}

CONTENT["distributions"] = {
    "what": (
        "A **probability distribution** describes how likely each outcome is. **Discrete** "
        "distributions (Bernoulli, **binomial**, Poisson) assign probabilities to countable "
        "outcomes; **continuous** ones (**uniform**, **normal/Gaussian**) describe densities over a "
        "range. The **normal distribution** — the bell curve — is central to ML because of the "
        "Central Limit Theorem and the 68–95–99.7 rule."
    ),
    "why": (
        "Models assume distributions (Naive Bayes assumes Gaussian features; errors are often "
        "assumed normal). Knowing distributions helps you simulate data, standardize features "
        "(z-scores), spot outliers, and understand sampling and confidence."
    ),
    "concepts": [
        ("Uniform", "Every value in a range equally likely."),
        ("Bernoulli / Binomial", "One trial / number of successes in n independent trials."),
        ("Poisson", "Count of rare events in a fixed interval."),
        ("Normal (Gaussian)", "Symmetric bell curve defined by mean μ and std σ."),
        ("68–95–99.7 rule", "Fraction of normal data within 1, 2, 3 std devs."),
        ("Z-score", "(x − μ)/σ: how many std devs from the mean a value sits."),
    ],
    "examples": [
        ("Sampling uniform and normal distributions", r'''
import random
import statistics as st

random.seed(0)

# Uniform: every value in [0, 1) equally likely
uniform_sample = [random.random() for _ in range(10_000)]
print("uniform mean ~", round(st.mean(uniform_sample), 3))   # ~0.5

# Normal (Gaussian): bell curve with mean=50, std=10
normal_sample = [random.gauss(50, 10) for _ in range(10_000)]
print("normal mean ~", round(st.mean(normal_sample), 2))     # ~50
print("normal std  ~", round(st.stdev(normal_sample), 2))    # ~10

# A quick text histogram of the normal sample
buckets = {}
for x in normal_sample:
    b = int(x // 10) * 10
    buckets[b] = buckets.get(b, 0) + 1
for b in sorted(buckets):
    print(f"{b:3d}-{b+9:3d} | {'#' * (buckets[b] // 100)}")
'''),
        ("Binomial and Poisson probability mass functions", r'''
from math import comb, exp, factorial

# Binomial PMF: P(k successes in n trials), success prob p
def binomial_pmf(k, n, p):
    return comb(n, k) * p ** k * (1 - p) ** (n - k)

# Flip a fair coin 5 times: probability of exactly 3 heads
print("P(3 heads in 5) =", round(binomial_pmf(3, 5, 0.5), 4))   # 0.3125

# Full distribution sums to 1
total = sum(binomial_pmf(k, 5, 0.5) for k in range(6))
print("sum of PMF =", round(total, 6))                          # 1.0

# Poisson PMF: P(k events) given average rate lambda
def poisson_pmf(k, lam):
    return exp(-lam) * lam ** k / factorial(k)

# Average 2 calls/min: probability of exactly 3 calls
print("P(3 calls | lam=2) =", round(poisson_pmf(3, 2), 4))      # 0.1804
'''),
        ("Normal distribution: PDF, z-scores, 68-95-99.7", r'''
import math
import random
import statistics as st

# Normal probability DENSITY function
def normal_pdf(x, mu=0, sigma=1):
    coef = 1 / (sigma * math.sqrt(2 * math.pi))
    return coef * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

print("peak density at mean:", round(normal_pdf(0), 4))   # 0.3989

# Z-score: how many std devs from the mean
def z_score(x, mu, sigma):
    return (x - mu) / sigma

print("z of 80 (mu=70,sd=5):", z_score(80, 70, 5))        # 2.0

# Verify the 68-95-99.7 rule by simulation
random.seed(1)
sample = [random.gauss(0, 1) for _ in range(100_000)]
within1 = sum(1 for x in sample if abs(x) <= 1) / len(sample)
within2 = sum(1 for x in sample if abs(x) <= 2) / len(sample)
within3 = sum(1 for x in sample if abs(x) <= 3) / len(sample)
print(f"within 1 std: {within1:.1%}  (~68%)")
print(f"within 2 std: {within2:.1%}  (~95%)")
print(f"within 3 std: {within3:.1%}  (~99.7%)")
'''),
    ],
    "gotchas": [
        "A continuous PDF gives DENSITY, not probability — P(X = exact value) is 0; use ranges/areas.",
        "Binomial assumes independent trials with a CONSTANT success probability.",
        "`random.gauss(mu, sigma)` takes the standard deviation, not the variance.",
        "Real data is often skewed or heavy-tailed — don't assume normal without checking.",
        "Z-scores need the population/sample mean and std; computing them on tiny samples is unreliable.",
    ],
    "exercises": [
        ("Sample 1000 values from a uniform [0,1) and print the mean.", "random.random.",
         r'''import random, statistics as st
random.seed(0)
print(round(st.mean([random.random() for _ in range(1000)]), 1))  # ~0.5'''),
        ("Sample from a normal(mean=100, std=15) and print one value.", "random.gauss.",
         r'''import random
random.seed(0)
print(round(random.gauss(100, 15), 2))'''),
        ("Compute the binomial probability of exactly 2 heads in 4 flips.", "comb * p^k * q^(n-k).",
         r'''from math import comb
print(round(comb(4, 2) * 0.5 ** 4, 4))  # 0.375'''),
        ("Compute the z-score of 85 given mean 75, std 5.", "(x-mu)/sigma.",
         r'''print((85 - 75) / 5)  # 2.0'''),
        ("Compute the Poisson probability of 0 events when lambda=3.", "e^-lambda.",
         r'''from math import exp
print(round(exp(-3), 4))  # 0.0498'''),
        ("Verify a binomial(n=3,p=0.5) PMF sums to 1.", "Sum over k.",
         r'''from math import comb
print(round(sum(comb(3, k) * 0.5 ** 3 for k in range(4)), 6))  # 1.0'''),
        ("Evaluate the standard normal density at x=0.", "1/sqrt(2pi).",
         r'''import math
print(round(1 / math.sqrt(2 * math.pi), 4))  # 0.3989'''),
        ("Estimate P(|z|<=1) for a standard normal by simulation.", "Count within 1 std.",
         r'''import random
random.seed(1)
s = [random.gauss(0, 1) for _ in range(50000)]
print(round(sum(1 for x in s if abs(x) <= 1) / len(s), 2))  # ~0.68'''),
    ],
}

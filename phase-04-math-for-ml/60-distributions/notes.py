# ======================================================================
# 60 — Distributions  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Sampling uniform and normal distributions
# ----------------------------------------------------------------------
print("\n--- Example 1: Sampling uniform and normal distributions ---")
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

# ----------------------------------------------------------------------
# Example 2: Binomial and Poisson probability mass functions
# ----------------------------------------------------------------------
print("\n--- Example 2: Binomial and Poisson probability mass functions ---")
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

# ----------------------------------------------------------------------
# Example 3: Normal distribution: PDF, z-scores, 68-95-99.7
# ----------------------------------------------------------------------
print("\n--- Example 3: Normal distribution: PDF, z-scores, 68-95-99.7 ---")
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

print("\nDone! Tip: change values above and run again to learn by experiment.")

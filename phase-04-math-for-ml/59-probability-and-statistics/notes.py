# ======================================================================
# 59 — Probability and Statistics  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Descriptive statistics with the statistics module
# ----------------------------------------------------------------------
print("\n--- Example 1: Descriptive statistics with the statistics module ---")
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

# ----------------------------------------------------------------------
# Example 2: Probability: simulation, combinations, complement
# ----------------------------------------------------------------------
print("\n--- Example 2: Probability: simulation, combinations, complement ---")
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

# ----------------------------------------------------------------------
# Example 3: Correlation, covariance, and Bayes' theorem
# ----------------------------------------------------------------------
print("\n--- Example 3: Correlation, covariance, and Bayes' theorem ---")
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

print("\nDone! Tip: change values above and run again to learn by experiment.")

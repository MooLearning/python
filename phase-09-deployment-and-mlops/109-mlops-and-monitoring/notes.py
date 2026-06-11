# ======================================================================
# 109 — MLOps and Monitoring  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: Detecting data drift by comparing distributions (runs)
# ----------------------------------------------------------------------
print("\n--- Example 1: Detecting data drift by comparing distributions (runs) ---")
import statistics as st

# Feature stats at TRAINING time vs what we see in PRODUCTION now
train = [5.0, 5.2, 4.8, 5.1, 4.9, 5.0, 5.3, 4.7]
prod  = [6.1, 6.3, 5.9, 6.2, 6.0, 6.4, 5.8, 6.1]   # shifted upward!

train_mean, train_std = st.mean(train), st.pstdev(train)
prod_mean = st.mean(prod)

# How many training-std-devs has the production mean moved?
z_shift = abs(prod_mean - train_mean) / train_std
print(f"train mean={train_mean:.2f}, prod mean={prod_mean:.2f}")
print(f"drift (in std devs): {z_shift:.2f}")
print("DRIFT DETECTED -> retrain" if z_shift > 2 else "stable")

# ----------------------------------------------------------------------
# Example 2: Population Stability Index (PSI) for drift
# ----------------------------------------------------------------------
print("\n--- Example 2: Population Stability Index (PSI) for drift ---")
import math

# Fraction of data falling in each bin: expected (training) vs actual (production)
expected = [0.25, 0.25, 0.25, 0.25]
actual   = [0.10, 0.20, 0.30, 0.40]

def psi(expected, actual, eps=1e-6):
    total = 0.0
    for e, a in zip(expected, actual):
        e, a = max(e, eps), max(a, eps)
        total += (a - e) * math.log(a / e)
    return total

score = psi(expected, actual)
print(f"PSI = {score:.4f}")
# Rule of thumb: <0.1 stable, 0.1-0.25 moderate shift, >0.25 significant drift
verdict = ("stable" if score < 0.1 else
           "moderate drift" if score < 0.25 else "significant drift")
print("verdict:", verdict)

# ----------------------------------------------------------------------
# Example 3: Monitoring metrics: log predictions and summarize
# ----------------------------------------------------------------------
print("\n--- Example 3: Monitoring metrics: log predictions and summarize ---")
import time, random
random.seed(0)

# Simulate a stream of served predictions with latencies
logs = []
for _ in range(200):
    latency_ms = random.gauss(40, 8)
    pred = random.choice([0, 1])
    logs.append({"latency_ms": max(1, latency_ms), "prediction": pred})

# Summarize what a monitoring dashboard would track
latencies = sorted(l["latency_ms"] for l in logs)
p50 = latencies[len(latencies) // 2]
p95 = latencies[int(len(latencies) * 0.95)]
positive_rate = sum(l["prediction"] for l in logs) / len(logs)

print(f"requests       : {len(logs)}")
print(f"latency p50    : {p50:.1f} ms")
print(f"latency p95    : {p95:.1f} ms")
print(f"positive rate  : {positive_rate:.1%}")
print("Alert if p95 latency or positive-rate drifts from the baseline.")

print("\nDone! Tip: change values above and run again to learn by experiment.")

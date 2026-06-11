# 109 — MLOps and Monitoring

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**MLOps** applies DevOps practices to machine learning: versioning data/models, automated **CI/CD** for training and deployment, a **model registry**, and ongoing **monitoring**. Unlike regular software, models **decay** as the world changes — **data drift** (inputs shift) and **concept drift** (input→output relationship shifts) degrade accuracy silently. Monitoring catches drift and performance drops so you can retrain.

## Why it matters

A model that was 95% accurate at launch can quietly rot. MLOps and monitoring turn ML from a one-off experiment into a reliable, maintainable production system with feedback loops and automated retraining.

## Key concepts

- **CI/CD for ML** — Automate testing, training, and deployment.
- **Model registry** — Versioned store of models with metadata/stages.
- **Data drift** — Input distribution changes over time.
- **Concept drift** — The input→output relationship changes.
- **Monitoring** — Track accuracy, latency, throughput, inputs in production.
- **Retraining trigger** — Drift/perf drop kicks off a retrain pipeline.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Models decay — monitor in production; accuracy at launch isn't accuracy next quarter.
- ⚠️ Ground-truth labels often arrive late, so monitor input drift as an early proxy.
- ⚠️ Version DATA and CODE together with the model, or you can't reproduce/debug.
- ⚠️ Alert thresholds need tuning — too sensitive = noise, too loose = silent failures.
- ⚠️ A retraining pipeline must be tested too; auto-retraining on bad data makes things worse.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


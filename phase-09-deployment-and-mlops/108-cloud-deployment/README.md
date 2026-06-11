# 108 — Cloud Deployment

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Cloud deployment** runs your model/service on managed infrastructure (AWS, GCP, Azure) instead of your laptop. Options range from **VMs** (full control) to **containers** (ECS/Cloud Run/Kubernetes) to **serverless** functions (Lambda/Cloud Functions — scale to zero, pay per call) to **managed ML platforms** (SageMaker, Vertex AI). Config comes from **environment variables**; you add health checks, autoscaling, and logging.

## Why it matters

The cloud gives scalability, reliability, and global reach without owning hardware. Knowing the deployment options and 12-factor practices lets you ship models that handle real traffic and recover from failures.

## Key concepts

- **VM / container / serverless** — A spectrum of control vs convenience.
- **Serverless** — Run code per request; auto-scales, scales to zero.
- **Managed ML platform** — SageMaker/Vertex handle training+serving.
- **Env-var config** — 12-factor: configuration via environment, not code.
- **Health checks** — Endpoints the platform pings to know you're alive.
- **Autoscaling** — Add/remove instances based on load.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import os

# Read configuration from the environment with sensible defaults.
# In the cloud these are set by the platform (never hard-coded!).
config = {
    "MODEL_PATH": os.environ.get("MODEL_PATH", "/models/model.pkl"),
    "PORT": int(os.environ.get("PORT", "8000")),
    "LOG_LEVEL": os.environ.get("LOG_LEVEL", "INFO"),
    "MAX_BATCH": int(os.environ.get("MAX_BATCH", "32")),
}
print("loaded config:")
for k, v in config.items():
    print(f"  {k:10} = {v!r}")

# Secrets (API keys, DB passwords) also come from env vars, never the code:
api_key = os.environ.get("API_KEY", "<not set>")
print("API key present:", api_key != "<not set>")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Never hard-code secrets/keys — inject them via env vars or a secrets manager.
- ⚠️ Serverless has COLD STARTS; big ML models may be too slow/large for it.
- ⚠️ Log to stdout/stderr — cloud platforms capture those, not local files.
- ⚠️ Set resource limits and autoscaling, or you get throttled or a surprise bill.
- ⚠️ Provide a health/readiness endpoint, or the load balancer can't route correctly.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


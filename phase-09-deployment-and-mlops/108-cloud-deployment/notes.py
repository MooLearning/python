# ======================================================================
# 108 — Cloud Deployment  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# ----------------------------------------------------------------------
# Example 1: 12-factor config via environment variables (runs)
# ----------------------------------------------------------------------
print("\n--- Example 1: 12-factor config via environment variables (runs) ---")
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

# ----------------------------------------------------------------------
# Example 2: Choosing a deployment option
# ----------------------------------------------------------------------
print("\n--- Example 2: Choosing a deployment option ---")
options = [
    ("VM (EC2/Compute Engine)", "full control",   "you manage OS, scaling, patching"),
    ("Container (Cloud Run/ECS)", "balanced",      "ship a Docker image, auto-scales"),
    ("Serverless (Lambda/Functions)", "least ops", "per-request, scales to zero, cold starts"),
    ("Managed ML (SageMaker/Vertex)", "ML-native", "training+serving+monitoring built in"),
]
print(f"{'option':32} | {'control':10} | notes")
print("-" * 78)
for name, control, notes in options:
    print(f"{name:32} | {control:10} | {notes}")

# ----------------------------------------------------------------------
# Example 3: A health-check endpoint and deployment checklist
# ----------------------------------------------------------------------
print("\n--- Example 3: A health-check endpoint and deployment checklist ---")
# Cloud platforms ping a health endpoint to decide if traffic should be routed.
def health_check(model_loaded, db_connected):
    healthy = model_loaded and db_connected
    return {"status": "ok" if healthy else "unhealthy",
            "model": model_loaded, "db": db_connected}

print("healthy :", health_check(True, True))
print("degraded:", health_check(True, False))

checklist = [
    "Container builds and runs locally",
    "Config & secrets via environment variables",
    "/health endpoint returns 200 when ready",
    "Logging to stdout (the platform collects it)",
    "Autoscaling min/max instances set",
    "Resource limits (CPU/RAM) defined",
]
print("\nDeployment checklist:")
for item in checklist:
    print("  [ ]", item)

print("\nDone! Tip: change values above and run again to learn by experiment.")

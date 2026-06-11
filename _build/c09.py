# -*- coding: utf-8 -*-
"""Phase 9 — Deployment & MLOps.

Uses the standard library where possible (pickle, json, os, subprocess) so the
core examples run. Framework/tool examples (joblib, Flask, FastAPI, Streamlit,
Docker) are guarded or shown as runnable templates that print real configs.
"""

CONTENT = {}

CONTENT["model-saving-and-loading"] = {
    "deps": ["joblib"],
    "what": (
        "A trained model must be **persisted** (serialized to disk) so you can reuse it without "
        "retraining. Python's **pickle** serializes arbitrary objects; **joblib** is faster for big "
        "NumPy arrays (the scikit-learn standard). For portability you can also save just the "
        "**parameters** (weights, config) as **JSON**. Frameworks have their own formats (Keras "
        "`.keras`, PyTorch `state_dict`)."
    ),
    "why": (
        "You train once and serve many times. Saving/loading models is the bridge from a notebook "
        "experiment to a deployable artifact — the first step of putting ML into production."
    ),
    "concepts": [
        ("Serialization", "Convert an in-memory object to bytes on disk."),
        ("pickle", "Built-in; serializes most Python objects."),
        ("joblib", "Efficient for large NumPy arrays; sklearn's choice."),
        ("JSON params", "Portable, human-readable weights/config (no code)."),
        ("Framework formats", "Keras `.keras`, PyTorch `state_dict`."),
        ("Versioning", "Save the model version + training metadata alongside it."),
    ],
    "examples": [
        ("Save and load a model with pickle (stdlib)", r'''
import pickle, tempfile, os

class LinearModel:
    def __init__(self, w, b):
        self.w, self.b = w, b
    def predict(self, x):
        return self.w * x + self.b

model = LinearModel(2.0, 1.0)               # a 'trained' model
path = os.path.join(tempfile.gettempdir(), "model.pkl")

with open(path, "wb") as f:                 # SAVE
    pickle.dump(model, f)

with open(path, "rb") as f:                 # LOAD (e.g. in a server later)
    loaded = pickle.load(f)

print("loaded model predicts:", loaded.predict(5))   # 11.0
print("saved to:", path)
'''),
        ("Save parameters as portable JSON", r'''
import json, tempfile, os

# Save just the learned numbers + metadata (portable, language-agnostic)
artifact = {
    "model_type": "logistic_regression",
    "weights": [0.5, -0.3, 1.2],
    "bias": 0.1,
    "version": "1.0.0",
    "trained_on": "2026-01-15",
}
path = os.path.join(tempfile.gettempdir(), "params.json")
with open(path, "w") as f:
    json.dump(artifact, f, indent=2)

with open(path) as f:
    loaded = json.load(f)
print("model type:", loaded["model_type"], "| version:", loaded["version"])
print("weights:", loaded["weights"])

def predict(features, p):                   # reconstruct the model from params
    z = sum(w * x for w, x in zip(p["weights"], features)) + p["bias"]
    return 1 if z >= 0 else 0
print("predict [1,0,1]:", predict([1, 0, 1], loaded))
'''),
        ("joblib with scikit-learn (and framework notes)", r'''
try:
    import joblib, tempfile, os
    from sklearn.linear_model import LinearRegression

    model = LinearRegression().fit([[1], [2], [3]], [2, 4, 6])
    path = os.path.join(tempfile.gettempdir(), "sklearn_model.joblib")
    joblib.dump(model, path)                 # SAVE
    loaded = joblib.load(path)               # LOAD
    print("joblib model predicts 5 ->", round(loaded.predict([[5]])[0], 2))
except ImportError:
    print("joblib/sklearn not installed — run: pip install joblib scikit-learn")

print("\nFramework save formats:")
print("  Keras   : model.save('m.keras');  keras.models.load_model('m.keras')")
print("  PyTorch : torch.save(model.state_dict(), 'm.pt'); model.load_state_dict(...)")
'''),
    ],
    "gotchas": [
        "NEVER unpickle files from untrusted sources — pickle can execute arbitrary code.",
        "Pickled models are tied to library versions; loading with a different sklearn can break.",
        "Pickle needs the model's CLASS available at load time — keep the code importable.",
        "Save preprocessing (scalers/encoders) WITH the model, or predictions will be wrong.",
        "Record the model version and training data/metadata for reproducibility.",
    ],
    "exercises": [
        ("Pickle the dict {'w':2} to bytes and load it back.", "pickle.dumps/loads.",
         r'''import pickle
data = pickle.dumps({"w": 2})
print(pickle.loads(data))  # {'w': 2}'''),
        ("Save params {'bias':0.5} to JSON string and reload.", "json.dumps/loads.",
         r'''import json
s = json.dumps({"bias": 0.5})
print(json.loads(s))  # {'bias': 0.5}'''),
        ("Why is unpickling untrusted files dangerous?", "Security.",
         r'''#md
Unpickling can **execute arbitrary code** embedded in the file, so a malicious
pickle can run anything. Only load pickles from sources you trust (or use safer
formats like JSON for plain data).'''),
        ("Which library is preferred for large NumPy models?", "Recall.",
         r'''#md
**joblib** — it serializes large NumPy arrays more efficiently than pickle and is
the scikit-learn standard.'''),
        ("Reconstruct a linear model: predict w·x+b for w=[1,2],x=[3,4],b=1.", "Dot+bias.",
         r'''w, x, b = [1, 2], [3, 4], 1
print(sum(a * c for a, c in zip(w, x)) + b)  # 12'''),
        ("Why save the scaler with the model?", "Consistent preprocessing.",
         r'''#md
Predictions require the **same preprocessing** used in training. If the scaler/
encoder isn't saved and reused, inputs are transformed differently and outputs
become wrong.'''),
        ("What does PyTorch's state_dict contain?", "Recall.",
         r'''#md
The model's **learned parameters** (weights and biases) as a dictionary — saved/
loaded separately from the model code/architecture.'''),
        ("Name one reason to version your saved models.", "Reproducibility.",
         r'''#md
To **reproduce results, roll back** to a known-good model, and track which model
produced which predictions (auditing/debugging in production).'''),
    ],
}

CONTENT["flask-fastapi-serving"] = {
    "deps": ["fastapi", "flask", "uvicorn"],
    "what": (
        "To use a model in an app, you wrap it in a **web API**: a server exposes an HTTP endpoint "
        "(e.g. `POST /predict`) that accepts input JSON and returns predictions. **Flask** is a "
        "simple, mature micro-framework; **FastAPI** is modern, async, and auto-generates docs with "
        "data **validation** (Pydantic). You load the model once at startup and serve many requests."
    ),
    "why": (
        "An API turns a model into a service any client (web, mobile, another microservice) can call "
        "over the network. REST/JSON serving is the most common way models reach production."
    ),
    "concepts": [
        ("REST endpoint", "A URL + method (POST /predict) clients call."),
        ("Request/response", "JSON in, JSON out over HTTP."),
        ("Load once", "Load the model at startup, not per request."),
        ("Flask", "Minimal, synchronous, battle-tested."),
        ("FastAPI", "Async, typed, auto docs + validation."),
        ("Status codes", "200 OK, 400 bad input, 500 server error."),
    ],
    "examples": [
        ("The core: a predict function + simulated request (runs)", r'''
import json

# The model logic (loaded once in a real server)
WEIGHTS, BIAS = [0.5, -0.2, 0.8], 0.1
def predict(features):
    z = sum(w * x for w, x in zip(WEIGHTS, features)) + BIAS
    label = 1 if z >= 0 else 0
    return {"score": round(z, 3), "label": label}

# Simulate an incoming HTTP request body (JSON string)
request_body = '{"features": [1.0, 2.0, 0.5]}'
data = json.loads(request_body)                 # parse JSON
result = predict(data["features"])              # run the model
response = json.dumps(result)                    # serialize JSON response
print("request :", request_body)
print("response:", response)                     # {"score": ..., "label": 1}
'''),
        ("A Flask prediction server (template)", r'''
try:
    from flask import Flask, request, jsonify

    app = Flask(__name__)
    WEIGHTS, BIAS = [0.5, -0.2, 0.8], 0.1

    @app.route("/predict", methods=["POST"])
    def predict():
        data = request.get_json()
        feats = data["features"]
        z = sum(w * x for w, x in zip(WEIGHTS, feats)) + BIAS
        return jsonify({"label": int(z >= 0), "score": round(z, 3)})

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})

    print("Flask app ready. Run with:  flask run")
    print("Test:  curl -X POST localhost:5000/predict -d '{\"features\":[1,2,0.5]}'")
    # app.run()  # <- uncomment to actually start the server
except ImportError:
    print("Flask not installed — run: pip install flask")
'''),
        ("A FastAPI server with validation (template)", r'''
try:
    from fastapi import FastAPI
    from pydantic import BaseModel

    app = FastAPI()
    WEIGHTS, BIAS = [0.5, -0.2, 0.8], 0.1

    class Features(BaseModel):       # automatic validation of input shape/types
        features: list[float]

    @app.post("/predict")
    def predict(item: Features):
        z = sum(w * x for w, x in zip(WEIGHTS, item.features)) + BIAS
        return {"label": int(z >= 0), "score": round(z, 3)}

    print("FastAPI app ready. Run with:  uvicorn app:app --reload")
    print("Interactive docs auto-generated at:  http://localhost:8000/docs")
except ImportError:
    print("FastAPI not installed — run: pip install fastapi uvicorn pydantic")
'''),
    ],
    "gotchas": [
        "Load the model ONCE at startup (module/global), not inside the request handler.",
        "Validate and sanitize inputs — bad/missing fields should return 400, not crash (500).",
        "Flask's dev server isn't for production — use gunicorn/uvicorn workers behind a proxy.",
        "Heavy models block requests — use async/batching/queues for throughput.",
        "Return clear JSON errors and proper status codes; don't leak stack traces to clients.",
    ],
    "exercises": [
        ("Parse the JSON '{\"x\": 5}' and read x.", "json.loads.",
         r'''import json
print(json.loads('{"x": 5}')["x"])  # 5'''),
        ("Serialize {'label':1} to a JSON string.", "json.dumps.",
         r'''import json
print(json.dumps({"label": 1}))  # {"label": 1}'''),
        ("Which HTTP method submits data for a prediction?", "Recall.",
         r'''#md
**POST** — it carries the input data in the request body (GET is for retrieval and
shouldn't carry a prediction payload).'''),
        ("Compute a prediction z=w·x+b for w=[1,1],x=[2,3],b=0.", "Dot+bias.",
         r'''w, x, b = [1, 1], [2, 3], 0
print(sum(a * c for a, c in zip(w, x)) + b)  # 5'''),
        ("What status code means a bad client request?", "Recall.",
         r'''#md
**400 (Bad Request)** — the input was malformed/invalid. (200 = OK, 500 = server
error.)'''),
        ("Why load the model at startup, not per request?", "Performance.",
         r'''#md
Loading is slow; doing it **once at startup** (kept in memory) lets every request
reuse it, instead of re-loading from disk on every call (huge latency).'''),
        ("What does FastAPI auto-generate that Flask doesn't?", "Recall.",
         r'''#md
**Interactive API docs** (Swagger/OpenAPI at /docs) and automatic **request
validation** via Pydantic type hints.'''),
        ("Return label 1 if score>=0 for score=-0.5.", "Threshold.",
         r'''score = -0.5
print(int(score >= 0))  # 0'''),
    ],
}

CONTENT["streamlit-apps"] = {
    "deps": ["streamlit"],
    "what": (
        "**Streamlit** turns a Python script into an interactive web app with almost no web code. "
        "You write top-to-bottom Python using `st.` widgets (`st.slider`, `st.button`, "
        "`st.file_uploader`) and display calls (`st.write`, `st.dataframe`, `st.pyplot`). On every "
        "interaction Streamlit **re-runs the whole script**, recomputing the UI. It's the fastest "
        "way to build ML demos and dashboards."
    ),
    "why": (
        "Streamlit lets data scientists ship interactive demos, prototypes, and internal tools in "
        "minutes — no HTML/JS/CSS — perfect for showcasing models to non-technical stakeholders."
    ),
    "concepts": [
        ("Script = app", "The whole script defines the UI, top to bottom."),
        ("Re-run model", "Any widget change re-executes the script."),
        ("Widgets", "st.slider/selectbox/button capture user input."),
        ("Display", "st.write/dataframe/line_chart render outputs."),
        ("Caching", "@st.cache_data avoids recomputing expensive steps."),
        ("Session state", "st.session_state persists values across re-runs."),
    ],
    "examples": [
        ("The logic behind a dashboard (runs as plain Python)", r'''
import statistics as st_

# In Streamlit this data would come from st.file_uploader / a widget
data = [23, 45, 12, 67, 34, 89, 21, 55]

# Compute the same summary a dashboard would display
summary = {
    "count": len(data),
    "mean": round(st_.mean(data), 2),
    "median": st_.median(data),
    "min": min(data),
    "max": max(data),
}
print("Dashboard summary:")
for k, v in summary.items():
    print(f"  {k:7}: {v}")

# A simulated 'slider' filter: keep values above a threshold
threshold = 40                       # would be st.slider("min", 0, 100)
filtered = [x for x in data if x >= threshold]
print(f"\nvalues >= {threshold}: {filtered}")
'''),
        ("A Streamlit app (template)", r'''
try:
    import streamlit as st

    st.title("Model Demo")                       # page title
    st.write("Adjust the inputs and see the prediction update.")

    # Widgets capture user input; the script re-runs on every change
    x1 = st.slider("Feature 1", 0.0, 10.0, 5.0)
    x2 = st.slider("Feature 2", 0.0, 10.0, 3.0)

    weights, bias = [0.5, -0.3], 0.1
    score = weights[0] * x1 + weights[1] * x2 + bias
    label = "positive" if score >= 0 else "negative"

    st.metric("Score", round(score, 3))
    st.write("Prediction:", label)

    print("Streamlit app defined. Run with:  streamlit run app.py")
except ImportError:
    print("Streamlit not installed — run: pip install streamlit")
'''),
        ("Caching and charts in Streamlit (template)", r'''
try:
    import streamlit as st

    @st.cache_data                      # cache: expensive load runs once
    def load_data():
        return [10, 20, 15, 30, 25, 40]

    data = load_data()
    st.line_chart(data)                 # built-in chart
    st.bar_chart(data)

    if st.button("Show stats"):         # button returns True on click
        st.write("Mean:", sum(data) / len(data))

    # Persist a counter across re-runs with session state
    if "clicks" not in st.session_state:
        st.session_state.clicks = 0
    print("Streamlit caching + charts demo ready.")
except ImportError:
    print("Streamlit not installed — run: pip install streamlit")
'''),
    ],
    "gotchas": [
        "The ENTIRE script re-runs on every interaction — cache expensive work with @st.cache_data.",
        "Run apps with `streamlit run app.py`, not `python app.py` (the latter won't start the server).",
        "Use st.session_state to keep values across re-runs; plain variables reset each run.",
        "Heavy computations in the script make the UI feel sluggish — cache or precompute.",
        "Widget order in the script = layout order; structure the script as you want the page.",
    ],
    "exercises": [
        ("Compute a dashboard mean of [10,20,30].", "Mean.",
         r'''data = [10, 20, 30]
print(sum(data) / len(data))  # 20.0'''),
        ("Filter [5,15,25] keeping values >= 10 (a slider filter).", "Comprehension.",
         r'''print([x for x in [5, 15, 25] if x >= 10])  # [15, 25]'''),
        ("How do you run a Streamlit app file app.py?", "Recall.",
         r'''#md
**`streamlit run app.py`** — not `python app.py`. The Streamlit CLI starts the web
server and watches the script.'''),
        ("What happens when a user moves a slider?", "Recall.",
         r'''#md
Streamlit **re-runs the entire script** top to bottom with the new widget value,
recomputing and re-rendering the page.'''),
        ("Why use @st.cache_data?", "Avoid recompute.",
         r'''#md
Because the whole script re-runs on every interaction, caching prevents repeating
**expensive work** (loading data, training) — it runs once and reuses the result.'''),
        ("Keep a counter across re-runs: which feature?", "Recall.",
         r'''#md
**st.session_state** — a dict-like store that **persists** values across script
re-runs (ordinary variables reset each run).'''),
        ("Pick the max of dashboard data [3,9,2].", "max.",
         r'''print(max([3, 9, 2]))  # 9'''),
        ("Name one reason data scientists like Streamlit.", "Any valid.",
         r'''#md
You build interactive web apps with **pure Python** (no HTML/JS/CSS), shipping ML
demos and dashboards in minutes.'''),
    ],
}

CONTENT["docker-basics"] = {
    "what": (
        "**Docker** packages your app and ALL its dependencies into a **container** — a lightweight, "
        "isolated, reproducible unit that runs identically anywhere. A **Dockerfile** is the recipe "
        "(base image, copy code, install deps, run command); building it produces an **image**; "
        "running the image creates a **container**. This solves 'works on my machine' and is the "
        "standard way to ship ML services."
    ),
    "why": (
        "Containers guarantee the same environment in dev, test, and production — crucial for ML "
        "where library versions matter. They're the unit of deployment for cloud, Kubernetes, and "
        "CI/CD pipelines."
    ),
    "concepts": [
        ("Image", "A read-only template (base + your app + deps)."),
        ("Container", "A running instance of an image."),
        ("Dockerfile", "The build recipe, one instruction per layer."),
        ("Layers", "Each instruction caches a layer; order them for cache reuse."),
        ("Ports & volumes", "Expose ports and mount data into the container."),
        (".dockerignore", "Exclude files (venv, data) from the build context."),
    ],
    "examples": [
        ("A Dockerfile for a Python ML service (template)", r'''
dockerfile = """\
# Start from a small official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy and install dependencies FIRST (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Document the port the app listens on
EXPOSE 8000

# Command to run when the container starts
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
"""
print(dockerfile)
print("Build:  docker build -t my-model-api .")
print("Run  :  docker run -p 8000:8000 my-model-api")
'''),
        ("Common Docker commands", r'''
commands = [
    ("docker build -t name:tag .", "Build an image from the Dockerfile here"),
    ("docker run -p 8000:8000 name", "Run a container, mapping host:container ports"),
    ("docker run -d name", "Run detached (in the background)"),
    ("docker ps", "List running containers"),
    ("docker images", "List local images"),
    ("docker logs <id>", "View a container's logs"),
    ("docker exec -it <id> bash", "Open a shell inside a running container"),
    ("docker stop <id>", "Stop a running container"),
    ("docker push name:tag", "Upload an image to a registry"),
]
for cmd, desc in commands:
    print(f"{cmd:34} # {desc}")
'''),
        ("Layer caching and .dockerignore", r'''
# Why copy requirements.txt before the code:
print("Layer caching tip:")
print("  COPY requirements.txt + RUN pip install   <- cached unless deps change")
print("  COPY . .                                  <- re-runs when code changes")
print("  => dependencies aren't reinstalled on every code edit.\n")

dockerignore = """\
__pycache__/
*.pyc
.venv/
venv/
data/
*.csv
.git/
.env
"""
print(".dockerignore (keep the image small & secrets out):")
print(dockerignore)
'''),
    ],
    "gotchas": [
        "Bind to 0.0.0.0 inside the container, not 127.0.0.1, or it's unreachable from the host.",
        "Copy requirements.txt and install BEFORE copying code, so deps stay cached across edits.",
        "Use slim/specific base tags (python:3.11-slim), not 'latest' — reproducibility.",
        "Never bake secrets into the image — pass them as env vars/secrets at runtime.",
        "Add a .dockerignore (venv, data, .git) or images balloon and may leak files.",
    ],
    "exercises": [
        ("What's the difference between an image and a container?", "Recall.",
         r'''#md
An **image** is a static, read-only template; a **container** is a **running
instance** of that image (you can run many containers from one image).'''),
        ("Which Dockerfile instruction sets the startup command?", "Recall.",
         r'''#md
**CMD** (or ENTRYPOINT) — it defines the process that runs when the container
starts.'''),
        ("Why copy requirements.txt before the app code?", "Caching.",
         r'''#md
So the dependency-install layer is **cached** and reused; it only re-runs when
requirements change, not on every code edit — much faster rebuilds.'''),
        ("Map host port 5000 to container port 8000: which flag?", "Recall.",
         r'''#md
**`-p 5000:8000`** (host:container) on `docker run` — host port 5000 forwards to
the container's 8000.'''),
        ("What address should a containerized server bind to?", "Recall.",
         r'''#md
**0.0.0.0** (all interfaces) — binding to 127.0.0.1 makes it reachable only inside
the container, not from the host.'''),
        ("Name one thing to put in .dockerignore.", "Any valid.",
         r'''#md
Things like **.venv/, __pycache__/, data/, .git/, .env** — they bloat the image
and may leak secrets; excluding them keeps builds small and safe.'''),
        ("Why pin a base image tag instead of 'latest'?", "Reproducibility.",
         r'''#md
'latest' changes over time, so builds aren't **reproducible**. Pinning (e.g.
python:3.11-slim) guarantees the same base every build.'''),
        ("Which command lists running containers?", "Recall.",
         r'''#md
**`docker ps`** (add `-a` to also show stopped containers).'''),
    ],
}

CONTENT["cloud-deployment"] = {
    "what": (
        "**Cloud deployment** runs your model/service on managed infrastructure (AWS, GCP, Azure) "
        "instead of your laptop. Options range from **VMs** (full control) to **containers** "
        "(ECS/Cloud Run/Kubernetes) to **serverless** functions (Lambda/Cloud Functions — scale to "
        "zero, pay per call) to **managed ML platforms** (SageMaker, Vertex AI). Config comes from "
        "**environment variables**; you add health checks, autoscaling, and logging."
    ),
    "why": (
        "The cloud gives scalability, reliability, and global reach without owning hardware. Knowing "
        "the deployment options and 12-factor practices lets you ship models that handle real "
        "traffic and recover from failures."
    ),
    "concepts": [
        ("VM / container / serverless", "A spectrum of control vs convenience."),
        ("Serverless", "Run code per request; auto-scales, scales to zero."),
        ("Managed ML platform", "SageMaker/Vertex handle training+serving."),
        ("Env-var config", "12-factor: configuration via environment, not code."),
        ("Health checks", "Endpoints the platform pings to know you're alive."),
        ("Autoscaling", "Add/remove instances based on load."),
    ],
    "examples": [
        ("12-factor config via environment variables (runs)", r'''
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
'''),
        ("Choosing a deployment option", r'''
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
'''),
        ("A health-check endpoint and deployment checklist", r'''
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
'''),
    ],
    "gotchas": [
        "Never hard-code secrets/keys — inject them via env vars or a secrets manager.",
        "Serverless has COLD STARTS; big ML models may be too slow/large for it.",
        "Log to stdout/stderr — cloud platforms capture those, not local files.",
        "Set resource limits and autoscaling, or you get throttled or a surprise bill.",
        "Provide a health/readiness endpoint, or the load balancer can't route correctly.",
    ],
    "exercises": [
        ("Read an env var PORT with default 8000.", "os.environ.get.",
         r'''import os
print(int(os.environ.get("PORT", "8000")))  # 8000 if unset'''),
        ("Which option scales to zero between requests?", "Recall.",
         r'''#md
**Serverless** (Lambda / Cloud Functions) — it runs only per request and scales
down to **zero** instances when idle (you pay per invocation).'''),
        ("Where should secrets like API keys come from?", "Recall.",
         r'''#md
**Environment variables or a secrets manager** — never hard-coded in source or
baked into the image.'''),
        ("Why log to stdout in the cloud?", "Collection.",
         r'''#md
Cloud platforms automatically **collect stdout/stderr** into their logging systems.
Writing to local files inside an ephemeral container loses the logs.'''),
        ("What does a health-check endpoint do?", "Recall.",
         r'''#md
It lets the platform/load balancer **check if the service is ready** to receive
traffic (returns 200 when healthy), and restart/replace it if not.'''),
        ("A serverless downside for big models?", "Recall.",
         r'''#md
**Cold starts** (and size/time limits) — loading a large model on a fresh instance
adds latency, and serverless caps memory/runtime.'''),
        ("Build a config dict from env with default LOG_LEVEL=INFO.", "get default.",
         r'''import os
print(os.environ.get("LOG_LEVEL", "INFO"))  # INFO'''),
        ("Name the control trade-off: VM vs serverless.", "Recall.",
         r'''#md
**VM = maximum control** but you manage OS/scaling/patching. **Serverless = minimal
ops** but least control (limits, cold starts). Containers sit in between.'''),
    ],
}

CONTENT["mlops-and-monitoring"] = {
    "what": (
        "**MLOps** applies DevOps practices to machine learning: versioning data/models, automated "
        "**CI/CD** for training and deployment, a **model registry**, and ongoing **monitoring**. "
        "Unlike regular software, models **decay** as the world changes — **data drift** (inputs "
        "shift) and **concept drift** (input→output relationship shifts) degrade accuracy silently. "
        "Monitoring catches drift and performance drops so you can retrain."
    ),
    "why": (
        "A model that was 95% accurate at launch can quietly rot. MLOps and monitoring turn ML from "
        "a one-off experiment into a reliable, maintainable production system with feedback loops "
        "and automated retraining."
    ),
    "concepts": [
        ("CI/CD for ML", "Automate testing, training, and deployment."),
        ("Model registry", "Versioned store of models with metadata/stages."),
        ("Data drift", "Input distribution changes over time."),
        ("Concept drift", "The input→output relationship changes."),
        ("Monitoring", "Track accuracy, latency, throughput, inputs in production."),
        ("Retraining trigger", "Drift/perf drop kicks off a retrain pipeline."),
    ],
    "examples": [
        ("Detecting data drift by comparing distributions (runs)", r'''
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
'''),
        ("Population Stability Index (PSI) for drift", r'''
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
'''),
        ("Monitoring metrics: log predictions and summarize", r'''
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
'''),
    ],
    "gotchas": [
        "Models decay — monitor in production; accuracy at launch isn't accuracy next quarter.",
        "Ground-truth labels often arrive late, so monitor input drift as an early proxy.",
        "Version DATA and CODE together with the model, or you can't reproduce/debug.",
        "Alert thresholds need tuning — too sensitive = noise, too loose = silent failures.",
        "A retraining pipeline must be tested too; auto-retraining on bad data makes things worse.",
    ],
    "exercises": [
        ("Compute the mean shift in std devs: train mean 5 std 1, prod mean 7.", "z = |diff|/std.",
         r'''print(abs(7 - 5) / 1)  # 2.0'''),
        ("Data drift vs concept drift: which changes inputs only?", "Recall.",
         r'''#md
**Data drift** — the input distribution changes while the input→output relationship
may stay the same. **Concept drift** is when that relationship itself changes.'''),
        ("PSI term for one bin: (a-e)*ln(a/e), a=0.4,e=0.25.", "Plug in.",
         r'''import math
a, e = 0.4, 0.25
print(round((a - e) * math.log(a / e), 4))'''),
        ("Compute the p50 (median) latency of [10,20,30].", "Median.",
         r'''import statistics as st
print(st.median([10, 20, 30]))  # 20'''),
        ("What does a model registry store?", "Recall.",
         r'''#md
**Versioned models with metadata** (metrics, training data/version, stage like
staging/production) — enabling rollback, auditing, and controlled promotion.'''),
        ("PSI of 0.3 means what?", "Recall.",
         r'''#md
**Significant drift** (rule of thumb PSI > 0.25). The production distribution has
shifted enough from training that you should investigate/retrain.'''),
        ("Why monitor input drift when labels are delayed?", "Early signal.",
         r'''#md
True accuracy needs ground-truth labels, which often arrive late. **Input drift** is
an **early proxy** — if inputs shift, performance is likely degrading before labels
confirm it.'''),
        ("Compute positive rate of predictions [1,0,1,1].", "Mean.",
         r'''p = [1, 0, 1, 1]
print(sum(p) / len(p))  # 0.75'''),
    ],
}

CONTENT["git-and-version-control"] = {
    "what": (
        "**Git** is a distributed **version control** system that tracks every change to your code, "
        "lets you **branch** to work in isolation, **merge** work together, and collaborate via "
        "remotes (GitHub/GitLab). The core loop: edit files → **stage** (`git add`) → **commit** "
        "(`git commit`) a snapshot → **push** to a remote. Branches enable parallel work and pull "
        "requests enable review."
    ),
    "why": (
        "Git is non-negotiable in software and ML: it's your undo history, collaboration backbone, "
        "and the basis of CI/CD. Versioning code (and, with tools like DVC, data/models) makes work "
        "reproducible and team-friendly."
    ),
    "concepts": [
        ("Repository", "A project tracked by Git (its full history)."),
        ("Stage & commit", "git add selects changes; git commit snapshots them."),
        ("Branch", "An independent line of work; merge it back when ready."),
        ("Remote", "A hosted copy (origin) you push to / pull from."),
        ("Merge / pull request", "Combine branches; PRs add review."),
        (".gitignore", "Patterns of files Git should not track."),
    ],
    "examples": [
        ("The core Git workflow (commands)", r'''
workflow = [
    ("git init", "Start tracking a new project"),
    ("git clone <url>", "Copy an existing remote repo"),
    ("git status", "See what's changed / staged"),
    ("git add file.py", "Stage a change for the next commit"),
    ("git add .", "Stage ALL changes"),
    ("git commit -m 'msg'", "Snapshot staged changes with a message"),
    ("git push", "Upload commits to the remote"),
    ("git pull", "Download + merge remote changes"),
    ("git log --oneline", "View commit history compactly"),
]
for cmd, desc in workflow:
    print(f"{cmd:22} # {desc}")
'''),
        ("Branching and merging", r'''
branching = [
    ("git branch", "List branches"),
    ("git checkout -b feature", "Create AND switch to a new branch"),
    ("git switch main", "Switch back to main"),
    ("git merge feature", "Merge 'feature' into the current branch"),
    ("git branch -d feature", "Delete a merged branch"),
]
for cmd, desc in branching:
    print(f"{cmd:26} # {desc}")

print("\nTypical feature workflow:")
for step in ["git checkout -b add-model", "  ...edit & commit...",
             "git push -u origin add-model", "open a Pull Request -> review -> merge"]:
    print("  " + step)
'''),
        ("A .gitignore for ML projects, and checking git", r'''
import subprocess

gitignore = """\
__pycache__/
*.pyc
.venv/
venv/
.env                 # secrets
data/                # large datasets (use DVC/cloud storage)
*.csv
models/*.pkl         # large model binaries
.ipynb_checkpoints/
"""
print(".gitignore for an ML project:")
print(gitignore)

try:
    version = subprocess.run(["git", "--version"],
                             capture_output=True, text=True, timeout=5)
    print("git available:", version.stdout.strip() or "yes")
except (FileNotFoundError, subprocess.SubprocessError):
    print("git not found — install it from https://git-scm.com")
'''),
    ],
    "gotchas": [
        "Don't commit secrets (.env, keys) or large data/models — add them to .gitignore.",
        "Write clear, present-tense commit messages ('Add X', not 'added stuff').",
        "Commit small and often; giant commits are hard to review and revert.",
        "`git push --force` can overwrite teammates' work — avoid it on shared branches.",
        "Pull/merge frequently to avoid painful conflicts from long-lived branches.",
    ],
    "exercises": [
        ("Which command stages all changes?", "Recall.",
         r'''#md
**`git add .`** stages every modified/new file in the current directory tree for the
next commit.'''),
        ("Create and switch to a branch 'dev' in one command.", "checkout -b.",
         r'''#md
**`git checkout -b dev`** (or the newer `git switch -c dev`).'''),
        ("What does git commit do?", "Recall.",
         r'''#md
Records a **snapshot** of the currently **staged** changes into the repository
history, with a message describing them.'''),
        ("Name two things to put in .gitignore for ML.", "Any valid.",
         r'''#md
For example **.env (secrets)** and **data/ or *.pkl (large datasets/models)** —
plus __pycache__/, .venv/, .ipynb_checkpoints/.'''),
        ("What's the command to upload commits to the remote?", "Recall.",
         r'''#md
**`git push`** — sends your local commits to the remote (e.g. origin/GitHub).'''),
        ("Why avoid git push --force on shared branches?", "Overwrites.",
         r'''#md
It can **overwrite/rewrite history** that teammates already based work on, causing
lost commits and conflicts. Use it only on your own private branches.'''),
        ("Combine branch 'feature' into the current branch.", "merge.",
         r'''#md
**`git merge feature`** — integrates the commits from `feature` into the branch
you currently have checked out.'''),
        ("Write a good commit message style for adding a function.", "Imperative.",
         r'''#md
Imperative, present tense and specific — e.g. **"Add predict() endpoint to API"**,
not "added stuff" or "fixes".'''),
    ],
}

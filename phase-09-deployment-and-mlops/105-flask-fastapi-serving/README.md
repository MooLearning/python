# 105 — Flask and FastAPI Serving

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

To use a model in an app, you wrap it in a **web API**: a server exposes an HTTP endpoint (e.g. `POST /predict`) that accepts input JSON and returns predictions. **Flask** is a simple, mature micro-framework; **FastAPI** is modern, async, and auto-generates docs with data **validation** (Pydantic). You load the model once at startup and serve many requests.

## Why it matters

An API turns a model into a service any client (web, mobile, another microservice) can call over the network. REST/JSON serving is the most common way models reach production.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install fastapi flask uvicorn
```

## Key concepts

- **REST endpoint** — A URL + method (POST /predict) clients call.
- **Request/response** — JSON in, JSON out over HTTP.
- **Load once** — Load the model at startup, not per request.
- **Flask** — Minimal, synchronous, battle-tested.
- **FastAPI** — Async, typed, auto docs + validation.
- **Status codes** — 200 OK, 400 bad input, 500 server error.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
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
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Load the model ONCE at startup (module/global), not inside the request handler.
- ⚠️ Validate and sanitize inputs — bad/missing fields should return 400, not crash (500).
- ⚠️ Flask's dev server isn't for production — use gunicorn/uvicorn workers behind a proxy.
- ⚠️ Heavy models block requests — use async/batching/queues for throughput.
- ⚠️ Return clear JSON errors and proper status codes; don't leak stack traces to clients.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


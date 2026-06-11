# ======================================================================
# 105 — Flask and FastAPI Serving  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: fastapi, flask, uvicorn
# Install:  pip install fastapi flask uvicorn

# ----------------------------------------------------------------------
# Example 1: The core: a predict function + simulated request (runs)
# ----------------------------------------------------------------------
print("\n--- Example 1: The core: a predict function + simulated request (runs) ---")
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

# ----------------------------------------------------------------------
# Example 2: A Flask prediction server (template)
# ----------------------------------------------------------------------
print("\n--- Example 2: A Flask prediction server (template) ---")
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

# ----------------------------------------------------------------------
# Example 3: A FastAPI server with validation (template)
# ----------------------------------------------------------------------
print("\n--- Example 3: A FastAPI server with validation (template) ---")
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

print("\nDone! Tip: change values above and run again to learn by experiment.")

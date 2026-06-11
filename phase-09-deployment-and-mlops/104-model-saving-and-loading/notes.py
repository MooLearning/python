# ======================================================================
# 104 — Model Saving and Loading  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: joblib
# Install:  pip install joblib

# ----------------------------------------------------------------------
# Example 1: Save and load a model with pickle (stdlib)
# ----------------------------------------------------------------------
print("\n--- Example 1: Save and load a model with pickle (stdlib) ---")
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

# ----------------------------------------------------------------------
# Example 2: Save parameters as portable JSON
# ----------------------------------------------------------------------
print("\n--- Example 2: Save parameters as portable JSON ---")
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

# ----------------------------------------------------------------------
# Example 3: joblib with scikit-learn (and framework notes)
# ----------------------------------------------------------------------
print("\n--- Example 3: joblib with scikit-learn (and framework notes) ---")
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

print("\nDone! Tip: change values above and run again to learn by experiment.")

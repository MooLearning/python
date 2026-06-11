# ======================================================================
# 100 — Transformers and Attention  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: transformers
# Install:  pip install transformers

# ----------------------------------------------------------------------
# Example 1: Scaled dot-product self-attention from scratch
# ----------------------------------------------------------------------
print("\n--- Example 1: Scaled dot-product self-attention from scratch ---")
import math

def softmax(xs):
    m = max(xs)
    exps = [math.exp(x - m) for x in xs]
    s = sum(exps)
    return [e / s for e in exps]

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

# 3 tokens, each a 2-D embedding. Use them directly as Q=K=V (self-attention).
tokens = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
d = len(tokens[0])

for i, q in enumerate(tokens):
    scores = [dot(q, k) / math.sqrt(d) for k in tokens]   # similarity to each token
    weights = softmax(scores)                              # attention distribution
    output = [sum(weights[j] * tokens[j][c] for j in range(len(tokens)))
              for c in range(d)]
    print(f"token {i}: weights={[round(w, 3) for w in weights]} "
          f"-> context={[round(o, 3) for o in output]}")

# ----------------------------------------------------------------------
# Example 2: Positional encoding (sinusoidal)
# ----------------------------------------------------------------------
print("\n--- Example 2: Positional encoding (sinusoidal) ---")
import math

def positional_encoding(position, d_model):
    pe = []
    for i in range(d_model):
        angle = position / (10000 ** (2 * (i // 2) / d_model))
        pe.append(math.sin(angle) if i % 2 == 0 else math.cos(angle))
    return pe

# Each position gets a unique vector added to its token embedding
for pos in range(4):
    enc = positional_encoding(pos, 4)
    print(f"pos {pos}: {[round(v, 3) for v in enc]}")
print("-> attention is order-agnostic, so we ADD these to encode word order.")

# ----------------------------------------------------------------------
# Example 3: Using a pretrained transformer (Hugging Face)
# ----------------------------------------------------------------------
print("\n--- Example 3: Using a pretrained transformer (Hugging Face) ---")
try:
    from transformers import pipeline

    # Sentiment analysis with a pretrained transformer model
    classifier = pipeline("sentiment-analysis")
    for text in ["I love this!", "This is terrible."]:
        result = classifier(text)[0]
        print(f"{text!r} -> {result['label']} ({result['score']:.2f})")
except ImportError:
    print("transformers not installed — run: pip install transformers torch")
except Exception as e:
    # model download/runtime issues shouldn't crash the lesson
    print("transformers present but model unavailable offline:", type(e).__name__)

print("\nDone! Tip: change values above and run again to learn by experiment.")

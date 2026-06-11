# ======================================================================
# 101 — LLM Basics  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: transformers
# Install:  pip install transformers

# ----------------------------------------------------------------------
# Example 1: A tiny bigram language model (next-token prediction)
# ----------------------------------------------------------------------
print("\n--- Example 1: A tiny bigram language model (next-token prediction) ---")
import random
from collections import defaultdict, Counter
random.seed(0)

corpus = ("the cat sat on the mat the cat ran the dog sat on the log "
          "the dog ran the cat sat").split()

# Learn P(next word | current word) from counts
model = defaultdict(Counter)
for a, b in zip(corpus, corpus[1:]):
    model[a][b] += 1

def predict_next(word):
    if word not in model:
        return random.choice(corpus)
    options = model[word]
    return options.most_common(1)[0][0]      # greedy: most likely next word

# Generate text autoregressively
word = "the"
out = [word]
for _ in range(8):
    word = predict_next(word)
    out.append(word)
print("generated:", " ".join(out))
print("P(* | 'cat'):", dict(model["cat"]))

# ----------------------------------------------------------------------
# Example 2: Temperature sampling: focused vs creative
# ----------------------------------------------------------------------
print("\n--- Example 2: Temperature sampling: focused vs creative ---")
import random, math
random.seed(1)

# A probability distribution over next tokens
logits = {"cat": 3.0, "dog": 2.0, "bird": 1.0, "fish": 0.5}

def sample(logits, temperature):
    # scale logits by temperature, then softmax + sample
    scaled = {w: v / temperature for w, v in logits.items()}
    m = max(scaled.values())
    exps = {w: math.exp(v - m) for w, v in scaled.items()}
    total = sum(exps.values())
    probs = {w: e / total for w, e in exps.items()}
    r = random.random(); cum = 0.0
    for w, p in probs.items():
        cum += p
        if r <= cum:
            return w, probs
    return w, probs

for temp in [0.2, 1.0, 2.0]:
    _, probs = sample(logits, temp)
    print(f"T={temp}: {({w: round(p, 2) for w, p in probs.items()})}")
print("Low T -> sharper (picks 'cat'); high T -> flatter (more random).")

# ----------------------------------------------------------------------
# Example 3: Tokenization and generation with Hugging Face
# ----------------------------------------------------------------------
print("\n--- Example 3: Tokenization and generation with Hugging Face ---")
try:
    from transformers import pipeline
    generator = pipeline("text-generation", model="distilgpt2")
    out = generator("The future of AI is", max_new_tokens=20,
                    temperature=0.7, do_sample=True)
    print(out[0]["generated_text"])
except ImportError:
    print("transformers not installed — run: pip install transformers torch")
except Exception as e:
    print("transformers present but model unavailable offline:", type(e).__name__)
    # Concept: tokenization splits text into subword IDs the model predicts over.
    text = "unbelievable"
    print("subword-style split example:", ["un", "bel", "iev", "able"])

print("\nDone! Tip: change values above and run again to learn by experiment.")

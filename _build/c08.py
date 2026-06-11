# -*- coding: utf-8 -*-
"""Phase 8 — Specialized AI (NLP, Transformers, LLMs, Computer Vision, RL).

Core mechanics (attention, TF-IDF, a bigram LM, image ops, Q-learning) are pure
Python and run. Library examples (transformers, OpenCV, gymnasium) are guarded.
"""

CONTENT = {}

CONTENT["nlp-basics"] = {
    "deps": ["scikit-learn"],
    "what": (
        "**Natural Language Processing (NLP)** turns text into something models can use. The basic "
        "pipeline: **tokenize** (split into words), **normalize** (lowercase, remove punctuation/"
        "**stopwords**, optionally **stem/lemmatize**), then **vectorize** — **bag-of-words** "
        "(counts) or **TF-IDF** (weighting words by how distinctive they are). **n-grams** capture "
        "short word sequences."
    ),
    "why": (
        "Text is unstructured; these steps convert it to numbers for classification, search, and "
        "clustering. TF-IDF and bag-of-words still power strong baselines, and tokenization concepts "
        "carry straight into transformers and LLMs."
    ),
    "concepts": [
        ("Tokenization", "Split text into tokens (words/subwords)."),
        ("Normalization", "Lowercase, strip punctuation, remove stopwords."),
        ("Stemming/lemmatization", "Reduce words to a root form (running→run)."),
        ("Bag-of-words", "Represent a doc by word counts, ignoring order."),
        ("TF-IDF", "Weight = term frequency × inverse document frequency."),
        ("n-grams", "Contiguous word sequences (bigrams, trigrams) for context."),
    ],
    "examples": [
        ("Tokenize, normalize, remove stopwords", r'''
import re

text = "The quick brown Fox jumps over the LAZY dog!"
stopwords = {"the", "over", "a", "an", "is", "of"}

# lowercase + keep only word characters
tokens = re.findall(r"[a-z]+", text.lower())
print("tokens   :", tokens)

filtered = [t for t in tokens if t not in stopwords]
print("no stops :", filtered)

# A naive stemmer: chop common suffixes
def stem(word):
    for suf in ("ing", "ed", "s"):
        if word.endswith(suf) and len(word) - len(suf) >= 3:
            return word[:-len(suf)]
    return word
print("stemmed  :", [stem(t) for t in filtered])
'''),
        ("Bag-of-words and TF-IDF from scratch", r'''
import math

docs = ["the cat sat", "the dog sat", "the cat ran fast"]
tokenized = [d.split() for d in docs]
vocab = sorted({w for doc in tokenized for w in doc})
print("vocab:", vocab)

# Bag-of-words: count vector per document
print("\nbag-of-words:")
for doc in tokenized:
    print(" ", {w: doc.count(w) for w in vocab if doc.count(w)})

# TF-IDF: rare-but-present words score highest
def tf(w, doc):  return doc.count(w) / len(doc)
def idf(w):
    containing = sum(1 for doc in tokenized if w in doc)
    return math.log(len(docs) / (1 + containing)) + 1

print("\nTF-IDF for doc 0 ('the cat sat'):")
for w in tokenized[0]:
    print(f"  {w:5}: {tf(w, tokenized[0]) * idf(w):.3f}")
# 'the' appears everywhere -> low idf -> low weight; 'cat'/'sat' score higher.
'''),
        ("n-grams and vectorizing with scikit-learn", r'''
text = "machine learning is fun".split()

# Bigrams (pairs of consecutive words)
bigrams = list(zip(text, text[1:]))
print("bigrams:", bigrams)

try:
    from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
    docs = ["the cat sat", "the dog sat", "the cat ran"]

    cv = CountVectorizer()
    counts = cv.fit_transform(docs)
    print("\nvocabulary:", cv.get_feature_names_out().tolist())
    print("count matrix:\n", counts.toarray())

    tfidf = TfidfVectorizer()
    print("\nTF-IDF matrix (rounded):\n", tfidf.fit_transform(docs).toarray().round(2))
except ImportError:
    print("scikit-learn not installed — run: pip install scikit-learn")
'''),
    ],
    "gotchas": [
        "Tokenizing on spaces alone mishandles punctuation/contractions — use regex or a real tokenizer.",
        "Removing stopwords can hurt tasks where they matter (sentiment, negation).",
        "Bag-of-words ignores word ORDER — 'dog bites man' == 'man bites dog'.",
        "TF-IDF vectors are sparse and high-dimensional; store them sparsely.",
        "Stemming is crude (can mangle words); lemmatization is more accurate but needs a dictionary.",
    ],
    "exercises": [
        ("Tokenize 'Hello, World!' into lowercase words.", "regex.",
         r'''import re
print(re.findall(r"[a-z]+", "Hello, World!".lower()))  # ['hello', 'world']'''),
        ("Remove stopwords {'the','a'} from ['the','cat','a','dog'].", "Filter.",
         r'''stop = {"the", "a"}
print([w for w in ["the", "cat", "a", "dog"] if w not in stop])  # ['cat','dog']'''),
        ("Build a bag-of-words count for 'cat cat dog'.", "Counter.",
         r'''from collections import Counter
print(dict(Counter("cat cat dog".split())))  # {'cat':2,'dog':1}'''),
        ("Compute term frequency of 'cat' in 'cat dog cat'.", "count/len.",
         r'''doc = "cat dog cat".split()
print(doc.count("cat") / len(doc))  # 0.666...'''),
        ("Generate bigrams of 'a b c'.", "zip with shift.",
         r'''t = "a b c".split()
print(list(zip(t, t[1:])))  # [('a','b'),('b','c')]'''),
        ("Why does 'the' get a low TF-IDF weight?", "Common everywhere.",
         r'''#md
Because it appears in (almost) **every document**, its inverse-document-frequency
(IDF) is low, so TF-IDF down-weights it as non-distinctive.'''),
        ("Stem 'running' by chopping 'ing'.", "Suffix strip.",
         r'''w = "running"
print(w[:-3] if w.endswith("ing") else w)  # runn'''),
        ("Does bag-of-words keep word order?", "Recall.",
         r'''#md
**No.** It only records word counts, discarding order — so 'dog bites man' and 'man
bites dog' get identical representations.'''),
    ],
}

CONTENT["transformers-and-attention"] = {
    "deps": ["transformers"],
    "what": (
        "**Transformers** process sequences using **self-attention** instead of recurrence. "
        "Attention lets each token look at every other token and weight their relevance: "
        "scores = softmax(Q·Kᵀ/√d), output = scores·V. **Multi-head attention** runs several "
        "attentions in parallel; **positional encodings** inject word order. Because attention is "
        "parallel (not sequential), transformers train fast on huge data — powering BERT, GPT, etc."
    ),
    "why": (
        "Transformers are the architecture behind virtually all modern AI (LLMs, translation, vision "
        "transformers). Understanding self-attention — the core operation — is the key to "
        "understanding today's models."
    ),
    "concepts": [
        ("Self-attention", "Each token attends to all tokens, weighting by relevance."),
        ("Q, K, V", "Query, Key, Value projections of each token."),
        ("Scaled dot-product", "softmax(QKᵀ/√d)·V computes the attention output."),
        ("Multi-head", "Several attention heads capture different relationships."),
        ("Positional encoding", "Adds order information (attention itself is order-agnostic)."),
        ("Parallelism", "All positions processed at once — unlike sequential RNNs."),
    ],
    "examples": [
        ("Scaled dot-product self-attention from scratch", r'''
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
'''),
        ("Positional encoding (sinusoidal)", r'''
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
'''),
        ("Using a pretrained transformer (Hugging Face)", r'''
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
'''),
    ],
    "gotchas": [
        "Self-attention is O(n²) in sequence length — long sequences are expensive.",
        "Attention alone ignores order; you MUST add positional encodings.",
        "Don't forget the 1/√d scaling — large dot products make softmax gradients vanish.",
        "Q, K, V come from LEARNED projections in real models, not the raw embeddings.",
        "Causal (decoder) attention must mask future tokens so the model can't peek ahead.",
    ],
    "exercises": [
        ("Compute the dot-product score of [1,0] and [1,1].", "Dot.",
         r'''print(sum(a * b for a, b in zip([1, 0], [1, 1])))  # 1'''),
        ("Softmax the scores [1,2,3] (return rounded).", "exp/sum.",
         r'''import math
z = [1, 2, 3]; e = [math.exp(v) for v in z]; s = sum(e)
print([round(v / s, 3) for v in e])'''),
        ("Why divide scores by sqrt(d)?", "Stability.",
         r'''#md
To **scale down** large dot products (which grow with dimension d). Without it,
softmax saturates and gradients vanish, hurting training.'''),
        ("What do Q, K, V stand for?", "Recall.",
         r'''#md
**Query, Key, Value** — each token is projected into these three vectors;
attention compares queries to keys to weight the values.'''),
        ("Why add positional encodings?", "Order.",
         r'''#md
Self-attention treats the input as a **set** (order-agnostic). Positional encodings
inject **word-order** information so the model knows token positions.'''),
        ("What is the complexity of attention in sequence length n?", "Pairwise.",
         r'''#md
**O(n²)** — every token attends to every other token, so cost grows quadratically
with sequence length.'''),
        ("What does multi-head attention add?", "Multiple views.",
         r'''#md
Several attention heads run in **parallel**, each learning to focus on different
relationships/positions; their outputs are concatenated for a richer
representation.'''),
        ("In a decoder, why mask future tokens?", "No peeking.",
         r'''#md
So each position can only attend to **earlier** tokens — preventing the model from
'cheating' by seeing the future words it's supposed to predict.'''),
    ],
}

CONTENT["llm-basics"] = {
    "deps": ["transformers"],
    "what": (
        "**Large Language Models (LLMs)** are huge transformers trained on massive text to predict "
        "the **next token**. From that single objective emerge translation, summarization, coding, "
        "and reasoning. Key ideas: **tokenization** (text → subword IDs), **autoregressive "
        "generation** (sample tokens one at a time), **temperature** (randomness of sampling), and "
        "**prompting/context windows**. Fine-tuning and RLHF align them to instructions."
    ),
    "why": (
        "LLMs (GPT, Claude, Llama) are reshaping software. Understanding next-token prediction, "
        "tokens, temperature, and context windows lets you use and build on them effectively — "
        "prompting, RAG, and agents all rest on these basics."
    ),
    "concepts": [
        ("Next-token prediction", "The core training objective: predict the following token."),
        ("Tokenization", "Text is split into subword tokens with integer IDs."),
        ("Autoregressive", "Generate one token, append it, repeat."),
        ("Temperature", "Scales randomness: low = focused, high = creative."),
        ("Context window", "Max tokens the model can attend to at once."),
        ("Prompting", "The input text that steers the model's output."),
    ],
    "examples": [
        ("A tiny bigram language model (next-token prediction)", r'''
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
'''),
        ("Temperature sampling: focused vs creative", r'''
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
'''),
        ("Tokenization and generation with Hugging Face", r'''
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
'''),
    ],
    "gotchas": [
        "LLMs predict plausible text, not truth — they can 'hallucinate' confident wrong answers.",
        "Everything is tokens (subwords), not words — token limits and costs are per-token.",
        "Temperature 0 is (near) deterministic/greedy; high temperature can become incoherent.",
        "Context windows are finite — text beyond the limit is truncated/forgotten.",
        "Output is sensitive to prompt wording; small changes can change results a lot.",
    ],
    "exercises": [
        ("What is an LLM's core training objective?", "Recall.",
         r'''#md
**Next-token prediction** — given the preceding tokens, predict the probability of
the next token. Everything else emerges from scaling this objective.'''),
        ("Greedy-predict the next word after 'cat' given counts {'sat':3,'ran':1}.", "Argmax.",
         r'''from collections import Counter
print(Counter({"sat": 3, "ran": 1}).most_common(1)[0][0])  # sat'''),
        ("Does low temperature make output more or less random?", "Recall.",
         r'''#md
**Less random** — low temperature sharpens the distribution toward the most likely
tokens (more focused/deterministic). High temperature flattens it (more diverse).'''),
        ("Build a bigram count for 'a b a b a'.", "Pairs.",
         r'''from collections import defaultdict, Counter
words = "a b a b a".split()
m = defaultdict(Counter)
for x, y in zip(words, words[1:]): m[x][y] += 1
print(dict(m["a"]))  # {'b': 2}'''),
        ("Why can't an LLM remember a 1M-word document at once?", "Context limit.",
         r'''#md
The **context window** is finite (a fixed max number of tokens). Text beyond that
limit is truncated, so the model can't attend to all of a very long document at
once.'''),
        ("Softmax-scale logit 4 by temperature 2 (just the division).", "logit/T.",
         r'''print(4 / 2)  # 2.0'''),
        ("True or false: tokens are always whole words.", "Subwords.",
         r'''#md
**False.** Modern LLMs use **subword** tokens (e.g. 'unbelievable' → un/believ/
able), so one word can be several tokens and rare words split into pieces.'''),
        ("What does 'autoregressive generation' mean?", "Recall.",
         r'''#md
Generating **one token at a time**, appending each output back to the input and
predicting the next — building the sequence left to right.'''),
    ],
}

CONTENT["computer-vision-opencv"] = {
    "deps": ["opencv-python"],
    "what": (
        "**Computer vision** processes images, which are just grids of pixel values (grayscale = one "
        "number 0–255; color = three R/G/B channels). Basic operations: convert to **grayscale**, "
        "adjust brightness/contrast, **threshold** to binary, **blur** (smooth), detect **edges**, "
        "resize, and flip. **OpenCV** (`cv2`) is the standard library for reading images and running "
        "these operations fast."
    ),
    "why": (
        "Vision powers face detection, OCR, medical imaging, self-driving, and AR. Understanding "
        "pixels and core operations (filters, thresholds, edges) is the foundation for CNNs and "
        "real-world image pipelines."
    ),
    "concepts": [
        ("Pixel grid", "An image is a 2-D (gray) or 3-D (color) array of intensities."),
        ("Grayscale", "Collapse RGB to one luminosity channel."),
        ("Thresholding", "Turn a gray image into black/white by a cutoff."),
        ("Blur / smoothing", "Average neighboring pixels to reduce noise."),
        ("Edge detection", "Find intensity changes (Sobel/Canny)."),
        ("Channels", "Color images have R, G, B (OpenCV uses BGR order)."),
    ],
    "examples": [
        ("Represent an image and convert to grayscale (pure Python)", r'''
# A 2x3 RGB image as nested lists: each pixel is [R, G, B]
image = [
    [[255, 0, 0],   [0, 255, 0],   [0, 0, 255]],     # red, green, blue
    [[255, 255, 0], [0, 0, 0],     [255, 255, 255]], # yellow, black, white
]

def to_grayscale(img):
    # luminosity formula: 0.299R + 0.587G + 0.114B
    return [[round(0.299*p[0] + 0.587*p[1] + 0.114*p[2]) for p in row]
            for row in img]

gray = to_grayscale(image)
print("grayscale values:")
for row in gray:
    print(" ", row)
'''),
        ("Thresholding, brightness, and flip", r'''
gray = [[50, 120, 200],
        [30, 128, 255],
        [90, 60, 180]]

# Threshold: pixels >= 128 become white (255), else black (0)
def threshold(img, t=128):
    return [[255 if v >= t else 0 for v in row] for row in img]
print("thresholded:")
for row in threshold(gray):
    print(" ", row)

# Increase brightness by 40 (clamped to 255)
def brighten(img, amount):
    return [[min(255, v + amount) for v in row] for row in img]
print("brighter:", brighten(gray, 40)[0])

# Flip horizontally (mirror each row)
print("flipped:", [row[::-1] for row in gray][0])
'''),
        ("Box blur (smoothing) and OpenCV", r'''
def box_blur(img):
    # average each pixel with its 8 neighbors (interior pixels only)
    h, w = len(img), len(img[0])
    out = [row[:] for row in img]
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            total = sum(img[i+di][j+dj] for di in (-1, 0, 1) for dj in (-1, 0, 1))
            out[i][j] = total // 9
    return out

img = [[10, 10, 10, 10, 10],
       [10, 90, 90, 90, 10],
       [10, 90, 90, 90, 10],
       [10, 90, 90, 90, 10],
       [10, 10, 10, 10, 10]]
print("blurred center row:", box_blur(img)[2])

try:
    import cv2
    import numpy as np
    arr = np.array(img, dtype="uint8")
    print("cv2 Gaussian blur center:", cv2.GaussianBlur(arr, (3, 3), 0)[2].tolist())
    print("cv2 Canny edges shape:", cv2.Canny(arr, 50, 150).shape)
except ImportError:
    print("OpenCV not installed — run: pip install opencv-python")
'''),
    ],
    "gotchas": [
        "OpenCV loads color as BGR, not RGB — convert before showing with matplotlib.",
        "Pixel values are 0–255 (uint8); arithmetic can overflow/wrap — clamp or use a wider dtype.",
        "Image arrays are indexed [row, col] = [y, x], which trips people up.",
        "Blurring/edge kernels can't fully process border pixels — handle padding.",
        "Resizing changes aspect ratio if you don't keep it; interpolation choice affects quality.",
    ],
    "exercises": [
        ("Convert RGB [100,150,200] to grayscale (luminosity).", "Weighted sum.",
         r'''p = [100, 150, 200]
print(round(0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2]))  # 142'''),
        ("Threshold [50,130,200] at 128 to binary.", "Compare.",
         r'''print([255 if v >= 128 else 0 for v in [50, 130, 200]])  # [0,255,255]'''),
        ("Brighten [200,250,100] by 30, clamped to 255.", "min(255, v+30).",
         r'''print([min(255, v + 30) for v in [200, 250, 100]])  # [230,255,130]'''),
        ("Flip the row [1,2,3,4] horizontally.", "Reverse.",
         r'''print([1, 2, 3, 4][::-1])  # [4, 3, 2, 1]'''),
        ("What color order does OpenCV use?", "Recall.",
         r'''#md
**BGR** (Blue, Green, Red) — not RGB. Convert with `cv2.cvtColor(img,
cv2.COLOR_BGR2RGB)` before displaying with RGB-based tools.'''),
        ("Average the 3 values [60,90,120] (1-D blur).", "Mean.",
         r'''print(sum([60, 90, 120]) // 3)  # 90'''),
        ("How is a grayscale image indexed: [x,y] or [row,col]?", "Recall.",
         r'''#md
**[row, col]** = **[y, x]** — the first index is the row (vertical), the second is
the column (horizontal).'''),
        ("Invert a pixel value 200 (255 - v).", "Negative.",
         r'''print(255 - 200)  # 55'''),
    ],
}

CONTENT["reinforcement-learning-basics"] = {
    "deps": ["gymnasium"],
    "what": (
        "**Reinforcement Learning (RL)** trains an **agent** to act in an **environment** to "
        "maximize cumulative **reward**. At each step the agent observes a **state**, picks an "
        "**action**, and receives a reward and a new state. **Q-learning** learns a table Q(state, "
        "action) estimating future reward, updated by the **Bellman equation**. The "
        "**exploration/exploitation** trade-off (ε-greedy) balances trying new actions vs using "
        "known-good ones."
    ),
    "why": (
        "RL powers game-playing AI (AlphaGo), robotics, recommendation, and RLHF (aligning LLMs). "
        "It's the framework for sequential decision-making under reward — a fundamentally different "
        "paradigm from supervised learning."
    ),
    "concepts": [
        ("Agent & environment", "The learner and the world it acts in."),
        ("State / action / reward", "Observation, choice, and feedback signal."),
        ("Policy", "The strategy mapping states to actions."),
        ("Q-value", "Expected future reward of an action in a state."),
        ("Bellman update", "Q(s,a) ← Q(s,a) + α[r + γ·maxQ(s') − Q(s,a)]."),
        ("Exploration vs exploitation", "ε-greedy: sometimes explore, mostly exploit."),
    ],
    "examples": [
        ("Q-learning on a line world (the agent learns to reach the goal)", r'''
import random
random.seed(0)

N = 5                       # states 0..4; goal is state 4
GOAL = 4
ACTIONS = [-1, +1]          # 0 = left, 1 = right
Q = [[0.0, 0.0] for _ in range(N)]
alpha, gamma, epsilon = 0.1, 0.9, 0.2

def step(s, a):
    ns = max(0, min(N - 1, s + ACTIONS[a]))
    reward = 1.0 if ns == GOAL else 0.0
    return ns, reward, ns == GOAL

for episode in range(500):
    s = 0
    for _ in range(50):
        # epsilon-greedy action selection
        if random.random() < epsilon:
            a = random.randint(0, 1)            # explore
        else:
            a = 0 if Q[s][0] >= Q[s][1] else 1  # exploit
        ns, r, done = step(s, a)
        # Bellman update
        Q[s][a] += alpha * (r + gamma * max(Q[ns]) - Q[s][a])
        s = ns
        if done:
            break

print("learned policy:")
for s in range(N):
    action = "right ->" if Q[s][1] >= Q[s][0] else "<- left"
    print(f"  state {s}: Q={[round(q, 2) for q in Q[s]]} -> {action}")
'''),
        ("The exploration/exploitation trade-off", r'''
import random
random.seed(0)

# Three slot machines (bandits) with unknown win rates
true_rates = [0.2, 0.5, 0.75]
counts = [0, 0, 0]
values = [0.0, 0.0, 0.0]          # estimated value per machine
epsilon = 0.1

def pull(machine):
    return 1.0 if random.random() < true_rates[machine] else 0.0

for t in range(2000):
    if random.random() < epsilon:
        m = random.randint(0, 2)            # explore a random machine
    else:
        m = values.index(max(values))       # exploit the best so far
    reward = pull(m)
    counts[m] += 1
    values[m] += (reward - values[m]) / counts[m]   # incremental average

print("estimated win rates:", [round(v, 3) for v in values])
print("true win rates     :", true_rates)
print("most-played machine:", counts.index(max(counts)), "(should be #2)")
'''),
        ("RL environments with Gymnasium", r'''
try:
    import gymnasium as gym

    env = gym.make("FrozenLake-v1", is_slippery=False)
    state, _ = env.reset(seed=0)
    print("observation space:", env.observation_space)
    print("action space     :", env.action_space)

    total_reward = 0
    for _ in range(20):
        action = env.action_space.sample()      # random policy
        state, reward, terminated, truncated, _ = env.step(action)
        total_reward += reward
        if terminated or truncated:
            break
    print("random-policy episode reward:", total_reward)
    env.close()
except ImportError:
    print("gymnasium not installed — run: pip install gymnasium")
'''),
    ],
    "gotchas": [
        "Without exploration (ε=0) the agent gets stuck exploiting a suboptimal policy.",
        "γ (discount) near 1 values the far future; near 0 is myopic — tune it to the task.",
        "Sparse rewards make learning slow — the agent rarely sees a signal.",
        "Q-learning needs many episodes; it's sample-inefficient vs supervised learning.",
        "Plain Q-tables don't scale to large/continuous states — that's where deep RL (DQN) comes in.",
    ],
    "exercises": [
        ("Bellman update: Q=0, r=1, gamma=0.9, maxQ'=0, alpha=0.1. New Q?", "Plug in.",
         r'''Q, r, gamma, maxQ, alpha = 0, 1, 0.9, 0, 0.1
print(Q + alpha * (r + gamma * maxQ - Q))  # 0.1'''),
        ("Epsilon-greedy with epsilon=0: explore or exploit?", "Recall.",
         r'''#md
**Always exploit** — with ε=0 the agent never takes a random action, always
choosing the current best-known one (no exploration).'''),
        ("Pick the greedy action from Q-values [0.3, 0.7].", "Argmax.",
         r'''Q = [0.3, 0.7]
print(Q.index(max(Q)))  # 1'''),
        ("What does the discount factor gamma control?", "Recall.",
         r'''#md
How much **future rewards** are valued relative to immediate ones. γ near 1 makes
the agent far-sighted; γ near 0 makes it greedy for immediate reward.'''),
        ("Incremental average: value 0.5 after 2 pulls, new reward 1. Update (3rd pull).", "Mean update.",
         r'''value, count, reward = 0.5, 2, 1
count += 1
print(value + (reward - value) / count)  # 0.666...'''),
        ("Name the 4 core RL elements.", "Recall.",
         r'''#md
**State, action, reward, and policy** (within an agent–environment loop). The agent
observes a state, takes an action per its policy, and receives a reward.'''),
        ("Why explore instead of always exploiting?", "Find better.",
         r'''#md
To **discover better actions/states** the current estimates don't yet know about.
Pure exploitation can lock onto a suboptimal choice forever.'''),
        ("Does Q-learning need labeled data?", "Recall.",
         r'''#md
**No.** It learns from **rewards** gathered by interacting with the environment, not
from labeled input/output pairs — it's not supervised learning.'''),
    ],
}

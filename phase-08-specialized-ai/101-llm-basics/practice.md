# 101 — LLM Basics: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

What is an LLM's core training objective?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Next-token prediction** — given the preceding tokens, predict the probability of
the next token. Everything else emerges from scaling this objective.

</details>

## Exercise 2

Greedy-predict the next word after 'cat' given counts {'sat':3,'ran':1}.

*Hint: Argmax.*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
print(Counter({"sat": 3, "ran": 1}).most_common(1)[0][0])  # sat
```

</details>

## Exercise 3

Does low temperature make output more or less random?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Less random** — low temperature sharpens the distribution toward the most likely
tokens (more focused/deterministic). High temperature flattens it (more diverse).

</details>

## Exercise 4

Build a bigram count for 'a b a b a'.

*Hint: Pairs.*

<details>
<summary>✅ Solution</summary>

```python
from collections import defaultdict, Counter
words = "a b a b a".split()
m = defaultdict(Counter)
for x, y in zip(words, words[1:]): m[x][y] += 1
print(dict(m["a"]))  # {'b': 2}
```

</details>

## Exercise 5

Why can't an LLM remember a 1M-word document at once?

*Hint: Context limit.*

<details>
<summary>✅ Solution</summary>

The **context window** is finite (a fixed max number of tokens). Text beyond that
limit is truncated, so the model can't attend to all of a very long document at
once.

</details>

## Exercise 6

Softmax-scale logit 4 by temperature 2 (just the division).

*Hint: logit/T.*

<details>
<summary>✅ Solution</summary>

```python
print(4 / 2)  # 2.0
```

</details>

## Exercise 7

True or false: tokens are always whole words.

*Hint: Subwords.*

<details>
<summary>✅ Solution</summary>

**False.** Modern LLMs use **subword** tokens (e.g. 'unbelievable' → un/believ/
able), so one word can be several tokens and rare words split into pieces.

</details>

## Exercise 8

What does 'autoregressive generation' mean?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

Generating **one token at a time**, appending each output back to the input and
predicting the next — building the sequence left to right.

</details>


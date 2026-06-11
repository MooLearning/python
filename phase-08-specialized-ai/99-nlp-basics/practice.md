# 99 — NLP Basics: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Tokenize 'Hello, World!' into lowercase words.

*Hint: regex.*

<details>
<summary>✅ Solution</summary>

```python
import re
print(re.findall(r"[a-z]+", "Hello, World!".lower()))  # ['hello', 'world']
```

</details>

## Exercise 2

Remove stopwords {'the','a'} from ['the','cat','a','dog'].

*Hint: Filter.*

<details>
<summary>✅ Solution</summary>

```python
stop = {"the", "a"}
print([w for w in ["the", "cat", "a", "dog"] if w not in stop])  # ['cat','dog']
```

</details>

## Exercise 3

Build a bag-of-words count for 'cat cat dog'.

*Hint: Counter.*

<details>
<summary>✅ Solution</summary>

```python
from collections import Counter
print(dict(Counter("cat cat dog".split())))  # {'cat':2,'dog':1}
```

</details>

## Exercise 4

Compute term frequency of 'cat' in 'cat dog cat'.

*Hint: count/len.*

<details>
<summary>✅ Solution</summary>

```python
doc = "cat dog cat".split()
print(doc.count("cat") / len(doc))  # 0.666...
```

</details>

## Exercise 5

Generate bigrams of 'a b c'.

*Hint: zip with shift.*

<details>
<summary>✅ Solution</summary>

```python
t = "a b c".split()
print(list(zip(t, t[1:])))  # [('a','b'),('b','c')]
```

</details>

## Exercise 6

Why does 'the' get a low TF-IDF weight?

*Hint: Common everywhere.*

<details>
<summary>✅ Solution</summary>

Because it appears in (almost) **every document**, its inverse-document-frequency
(IDF) is low, so TF-IDF down-weights it as non-distinctive.

</details>

## Exercise 7

Stem 'running' by chopping 'ing'.

*Hint: Suffix strip.*

<details>
<summary>✅ Solution</summary>

```python
w = "running"
print(w[:-3] if w.endswith("ing") else w)  # runn
```

</details>

## Exercise 8

Does bag-of-words keep word order?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**No.** It only records word counts, discarding order — so 'dog bites man' and 'man
bites dog' get identical representations.

</details>


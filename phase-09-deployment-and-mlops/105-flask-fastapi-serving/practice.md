# 105 — Flask and FastAPI Serving: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Parse the JSON '{"x": 5}' and read x.

*Hint: json.loads.*

<details>
<summary>✅ Solution</summary>

```python
import json
print(json.loads('{"x": 5}')["x"])  # 5
```

</details>

## Exercise 2

Serialize {'label':1} to a JSON string.

*Hint: json.dumps.*

<details>
<summary>✅ Solution</summary>

```python
import json
print(json.dumps({"label": 1}))  # {"label": 1}
```

</details>

## Exercise 3

Which HTTP method submits data for a prediction?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**POST** — it carries the input data in the request body (GET is for retrieval and
shouldn't carry a prediction payload).

</details>

## Exercise 4

Compute a prediction z=w·x+b for w=[1,1],x=[2,3],b=0.

*Hint: Dot+bias.*

<details>
<summary>✅ Solution</summary>

```python
w, x, b = [1, 1], [2, 3], 0
print(sum(a * c for a, c in zip(w, x)) + b)  # 5
```

</details>

## Exercise 5

What status code means a bad client request?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**400 (Bad Request)** — the input was malformed/invalid. (200 = OK, 500 = server
error.)

</details>

## Exercise 6

Why load the model at startup, not per request?

*Hint: Performance.*

<details>
<summary>✅ Solution</summary>

Loading is slow; doing it **once at startup** (kept in memory) lets every request
reuse it, instead of re-loading from disk on every call (huge latency).

</details>

## Exercise 7

What does FastAPI auto-generate that Flask doesn't?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Interactive API docs** (Swagger/OpenAPI at /docs) and automatic **request
validation** via Pydantic type hints.

</details>

## Exercise 8

Return label 1 if score>=0 for score=-0.5.

*Hint: Threshold.*

<details>
<summary>✅ Solution</summary>

```python
score = -0.5
print(int(score >= 0))  # 0
```

</details>


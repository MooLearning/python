# 28 — APIs with Requests: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Build the query string for params {'q':'cats','limit':5} using urllib.

*Hint: urlencode.*

<details>
<summary>✅ Solution</summary>

```python
from urllib.parse import urlencode
print(urlencode({"q": "cats", "limit": 5}))  # q=cats&limit=5
```

</details>

## Exercise 2

Write a function that returns 'ok' for status 200 and 'error' otherwise.

*Hint: Compare to 200.*

<details>
<summary>✅ Solution</summary>

```python
def check(status):
    return "ok" if status == 200 else "error"
print(check(200), check(404))  # ok error
```

</details>

## Exercise 3

Parse this API JSON string and print the user's name: '{"user":{"name":"Ada"}}'.

*Hint: json.loads.*

<details>
<summary>✅ Solution</summary>

```python
import json
data = json.loads('{"user": {"name": "Ada"}}')
print(data["user"]["name"])  # Ada
```

</details>

## Exercise 4

Categorize a status code into a class (2xx/3xx/4xx/5xx). Test 404.

*Hint: code // 100.*

<details>
<summary>✅ Solution</summary>

```python
def klass(code):
    return f"{code // 100}xx"
print(klass(404))  # 4xx
```

</details>

## Exercise 5

Write fetch that returns {'error': ...} instead of raising on failure.

*Hint: try/except.*

<details>
<summary>✅ Solution</summary>

```python
def fetch(fn):
    try:
        return fn()
    except Exception as e:
        return {"error": str(e)}
print(fetch(lambda: 1 / 0))
```

</details>

## Exercise 6

Read an API key from the environment variable API_KEY (default 'missing').

*Hint: os.environ.get.*

<details>
<summary>✅ Solution</summary>

```python
import os
print(os.environ.get("API_KEY", "missing"))
```

</details>

## Exercise 7

Given a dict response, safely get response['data']['items'] or [].

*Hint: Nested get.*

<details>
<summary>✅ Solution</summary>

```python
resp = {"data": {}}
print(resp.get("data", {}).get("items", []))  # []
```

</details>

## Exercise 8

Make a real GET request if requests is installed and network is up; else print a message.

*Hint: Guarded.*

<details>
<summary>✅ Solution</summary>

```python
try:
    import requests
    r = requests.get("https://httpbin.org/get", timeout=5)
    print("status:", r.status_code)
except Exception as e:
    print("skipped:", type(e).__name__)
```

</details>


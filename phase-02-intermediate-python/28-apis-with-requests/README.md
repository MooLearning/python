# 28 — APIs with Requests

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

Web **APIs** let your program talk to services over HTTP. You send a **request** (usually GET to read or POST to send data) to a URL and get back a **response** (often JSON). The `requests` library is the most popular way to do this; Python's built-in `urllib` works too. Key ideas: status codes, query parameters, headers, and JSON bodies.

## Why it matters

Almost every real app integrates with APIs: weather, payments, maps, LLMs, databases. Knowing how to call them, pass parameters, handle errors, and parse JSON responses is a core practical skill.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install requests
```

## Key concepts

- **HTTP methods** — GET (read), POST (create/send), PUT/PATCH (update), DELETE (remove).
- **Status codes** — 2xx success, 3xx redirect, 4xx your fault, 5xx server's fault. 200 = OK, 404 = not found.
- **Query parameters** — `?key=value` extras; pass as `params={...}`.
- **Headers** — Metadata like auth tokens and content type.
- **JSON body** — `response.json()` parses the response; `json=...` sends a JSON body.
- **Error handling** — Check `response.status_code` or call `raise_for_status()`; handle timeouts.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
# The SHAPE of a typical requests call (no network needed to learn it).
# When online with `pip install requests`, you would write:
#
#   import requests
#   resp = requests.get("https://api.github.com", timeout=10)
#   print(resp.status_code)          # 200 if OK
#   print(resp.headers["content-type"])
#   data = resp.json()               # parse JSON body into a dict
#   print(data["current_user_url"])
#
# Every API call has these parts:
for part in ["URL", "method (GET/POST)", "status code", "JSON body"]:
    print("part:", part)
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ ALWAYS pass a `timeout=` — without it a hung server freezes your program forever.
- ⚠️ A 200 response can still contain an error payload; check the body, not just the status code.
- ⚠️ `response.json()` raises if the body isn't valid JSON — wrap it or check the content-type.
- ⚠️ Don't hardcode API keys in code you share; load them from environment variables.
- ⚠️ Respect rate limits and add retries/backoff for production calls; hammering an API gets you blocked.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


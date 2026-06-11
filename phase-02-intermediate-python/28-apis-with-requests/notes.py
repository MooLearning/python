# ======================================================================
# 28 — APIs with Requests  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: requests
# Install:  pip install requests

# ----------------------------------------------------------------------
# Example 1: Anatomy of an API call (offline-safe demo)
# ----------------------------------------------------------------------
print("\n--- Example 1: Anatomy of an API call (offline-safe demo) ---")
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

# ----------------------------------------------------------------------
# Example 2: Make a real request if possible, else explain (fully runnable)
# ----------------------------------------------------------------------
print("\n--- Example 2: Make a real request if possible, else explain (fully runnable) ---")
import json

def fetch_json(url, timeout=10):
    """Try requests; fall back to urllib; never crash if offline."""
    try:
        try:
            import requests
            r = requests.get(url, timeout=timeout)
            r.raise_for_status()       # raise on 4xx/5xx
            return r.json()
        except ImportError:
            # requests not installed -> use the standard library
            from urllib.request import urlopen
            with urlopen(url, timeout=timeout) as resp:
                return json.loads(resp.read().decode())
    except Exception as e:
        return {"error": type(e).__name__}   # offline / blocked / bad URL / not JSON

result = fetch_json("https://httpbin.org/json")
print(type(result).__name__)
print(list(result)[:3] if isinstance(result, dict) else result)

# ----------------------------------------------------------------------
# Example 3: Sending parameters, headers, and POST bodies (shown as data)
# ----------------------------------------------------------------------
print("\n--- Example 3: Sending parameters, headers, and POST bodies (shown as data) ---")
# Building the pieces of a request (no network needed to learn the structure):
params = {"q": "python", "page": 2}        # -> ?q=python&page=2
headers = {"Authorization": "Bearer TOKEN", "Accept": "application/json"}
payload = {"title": "hello", "done": False}

from urllib.parse import urlencode
print("query string:", urlencode(params))   # q=python&page=2
print("headers:", headers)
print("json body:", payload)

# With requests you would write:
#   requests.get(url, params=params, headers=headers, timeout=10)
#   requests.post(url, json=payload, headers=headers, timeout=10)
print("Remember: always pass timeout=, and check status_code / raise_for_status().")

print("\nDone! Tip: change values above and run again to learn by experiment.")

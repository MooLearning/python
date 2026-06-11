# 106 — Streamlit Apps: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute a dashboard mean of [10,20,30].

*Hint: Mean.*

<details>
<summary>✅ Solution</summary>

```python
data = [10, 20, 30]
print(sum(data) / len(data))  # 20.0
```

</details>

## Exercise 2

Filter [5,15,25] keeping values >= 10 (a slider filter).

*Hint: Comprehension.*

<details>
<summary>✅ Solution</summary>

```python
print([x for x in [5, 15, 25] if x >= 10])  # [15, 25]
```

</details>

## Exercise 3

How do you run a Streamlit app file app.py?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**`streamlit run app.py`** — not `python app.py`. The Streamlit CLI starts the web
server and watches the script.

</details>

## Exercise 4

What happens when a user moves a slider?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

Streamlit **re-runs the entire script** top to bottom with the new widget value,
recomputing and re-rendering the page.

</details>

## Exercise 5

Why use @st.cache_data?

*Hint: Avoid recompute.*

<details>
<summary>✅ Solution</summary>

Because the whole script re-runs on every interaction, caching prevents repeating
**expensive work** (loading data, training) — it runs once and reuses the result.

</details>

## Exercise 6

Keep a counter across re-runs: which feature?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**st.session_state** — a dict-like store that **persists** values across script
re-runs (ordinary variables reset each run).

</details>

## Exercise 7

Pick the max of dashboard data [3,9,2].

*Hint: max.*

<details>
<summary>✅ Solution</summary>

```python
print(max([3, 9, 2]))  # 9
```

</details>

## Exercise 8

Name one reason data scientists like Streamlit.

*Hint: Any valid.*

<details>
<summary>✅ Solution</summary>

You build interactive web apps with **pure Python** (no HTML/JS/CSS), shipping ML
demos and dashboards in minutes.

</details>


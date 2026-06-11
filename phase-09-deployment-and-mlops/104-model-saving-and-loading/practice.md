# 104 — Model Saving and Loading: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Pickle the dict {'w':2} to bytes and load it back.

*Hint: pickle.dumps/loads.*

<details>
<summary>✅ Solution</summary>

```python
import pickle
data = pickle.dumps({"w": 2})
print(pickle.loads(data))  # {'w': 2}
```

</details>

## Exercise 2

Save params {'bias':0.5} to JSON string and reload.

*Hint: json.dumps/loads.*

<details>
<summary>✅ Solution</summary>

```python
import json
s = json.dumps({"bias": 0.5})
print(json.loads(s))  # {'bias': 0.5}
```

</details>

## Exercise 3

Why is unpickling untrusted files dangerous?

*Hint: Security.*

<details>
<summary>✅ Solution</summary>

Unpickling can **execute arbitrary code** embedded in the file, so a malicious
pickle can run anything. Only load pickles from sources you trust (or use safer
formats like JSON for plain data).

</details>

## Exercise 4

Which library is preferred for large NumPy models?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**joblib** — it serializes large NumPy arrays more efficiently than pickle and is
the scikit-learn standard.

</details>

## Exercise 5

Reconstruct a linear model: predict w·x+b for w=[1,2],x=[3,4],b=1.

*Hint: Dot+bias.*

<details>
<summary>✅ Solution</summary>

```python
w, x, b = [1, 2], [3, 4], 1
print(sum(a * c for a, c in zip(w, x)) + b)  # 12
```

</details>

## Exercise 6

Why save the scaler with the model?

*Hint: Consistent preprocessing.*

<details>
<summary>✅ Solution</summary>

Predictions require the **same preprocessing** used in training. If the scaler/
encoder isn't saved and reused, inputs are transformed differently and outputs
become wrong.

</details>

## Exercise 7

What does PyTorch's state_dict contain?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

The model's **learned parameters** (weights and biases) as a dictionary — saved/
loaded separately from the model code/architecture.

</details>

## Exercise 8

Name one reason to version your saved models.

*Hint: Reproducibility.*

<details>
<summary>✅ Solution</summary>

To **reproduce results, roll back** to a known-good model, and track which model
produced which predictions (auditing/debugging in production).

</details>


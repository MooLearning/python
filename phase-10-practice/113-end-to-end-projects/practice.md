# 113 — End-to-End Projects: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Order the lifecycle: model, data, deploy, problem.

*Hint: Sequence.*

<details>
<summary>✅ Solution</summary>

**Problem → Data → Model → Deploy.** Define what you're solving, get/clean the data,
build and validate the model, then deploy and monitor it.

</details>

## Exercise 2

Split [1..10] into 80% train / 20% test sizes.

*Hint: int(0.8*n).*

<details>
<summary>✅ Solution</summary>

```python
n = 10; s = int(0.8 * n)
print("train", s, "test", n - s)  # train 8 test 2
```

</details>

## Exercise 3

Save {'w':1.5} as a model artifact (JSON string).

*Hint: json.dumps.*

<details>
<summary>✅ Solution</summary>

```python
import json
print(json.dumps({"w": 1.5}))
```

</details>

## Exercise 4

Why keep raw data immutable?

*Hint: Reproducibility.*

<details>
<summary>✅ Solution</summary>

So you can always **reproduce** the cleaning pipeline from the original source and
recover from mistakes. Edit a separate processed copy, never the raw data.

</details>

## Exercise 5

Predict pass/fail with sigmoid(w*x+b)>=0.5 for w=1,x=5,b=-3.

*Hint: Threshold.*

<details>
<summary>✅ Solution</summary>

```python
import math
z = 1 * 5 + (-3)
print("pass" if 1 / (1 + math.exp(-z)) >= 0.5 else "fail")  # pass
```

</details>

## Exercise 6

Name two things a project README should contain.

*Hint: Any valid.*

<details>
<summary>✅ Solution</summary>

For example: the **problem statement & results**, and **how to install/run** it
(setup, commands). Also useful: data source, approach, and limitations.

</details>

## Exercise 7

Why define the metric before modeling?

*Hint: Alignment.*

<details>
<summary>✅ Solution</summary>

So the model optimizes the **right objective** tied to the real goal. Choosing the
metric afterward risks optimizing the wrong thing (e.g. accuracy on imbalanced
data).

</details>

## Exercise 8

Compute test accuracy: 3 correct of 4.

*Hint: correct/total.*

<details>
<summary>✅ Solution</summary>

```python
print(3 / 4)  # 0.75
```

</details>


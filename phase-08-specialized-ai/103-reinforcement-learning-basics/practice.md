# 103 — Reinforcement Learning Basics: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Bellman update: Q=0, r=1, gamma=0.9, maxQ'=0, alpha=0.1. New Q?

*Hint: Plug in.*

<details>
<summary>✅ Solution</summary>

```python
Q, r, gamma, maxQ, alpha = 0, 1, 0.9, 0, 0.1
print(Q + alpha * (r + gamma * maxQ - Q))  # 0.1
```

</details>

## Exercise 2

Epsilon-greedy with epsilon=0: explore or exploit?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**Always exploit** — with ε=0 the agent never takes a random action, always
choosing the current best-known one (no exploration).

</details>

## Exercise 3

Pick the greedy action from Q-values [0.3, 0.7].

*Hint: Argmax.*

<details>
<summary>✅ Solution</summary>

```python
Q = [0.3, 0.7]
print(Q.index(max(Q)))  # 1
```

</details>

## Exercise 4

What does the discount factor gamma control?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

How much **future rewards** are valued relative to immediate ones. γ near 1 makes
the agent far-sighted; γ near 0 makes it greedy for immediate reward.

</details>

## Exercise 5

Incremental average: value 0.5 after 2 pulls, new reward 1. Update (3rd pull).

*Hint: Mean update.*

<details>
<summary>✅ Solution</summary>

```python
value, count, reward = 0.5, 2, 1
count += 1
print(value + (reward - value) / count)  # 0.666...
```

</details>

## Exercise 6

Name the 4 core RL elements.

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**State, action, reward, and policy** (within an agent–environment loop). The agent
observes a state, takes an action per its policy, and receives a reward.

</details>

## Exercise 7

Why explore instead of always exploiting?

*Hint: Find better.*

<details>
<summary>✅ Solution</summary>

To **discover better actions/states** the current estimates don't yet know about.
Pure exploitation can lock onto a suboptimal choice forever.

</details>

## Exercise 8

Does Q-learning need labeled data?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**No.** It learns from **rewards** gathered by interacting with the environment, not
from labeled input/output pairs — it's not supervised learning.

</details>


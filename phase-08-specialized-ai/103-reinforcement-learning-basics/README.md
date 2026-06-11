# 103 — Reinforcement Learning Basics

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Reinforcement Learning (RL)** trains an **agent** to act in an **environment** to maximize cumulative **reward**. At each step the agent observes a **state**, picks an **action**, and receives a reward and a new state. **Q-learning** learns a table Q(state, action) estimating future reward, updated by the **Bellman equation**. The **exploration/exploitation** trade-off (ε-greedy) balances trying new actions vs using known-good ones.

## Why it matters

RL powers game-playing AI (AlphaGo), robotics, recommendation, and RLHF (aligning LLMs). It's the framework for sequential decision-making under reward — a fundamentally different paradigm from supervised learning.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install gymnasium
```

## Key concepts

- **Agent & environment** — The learner and the world it acts in.
- **State / action / reward** — Observation, choice, and feedback signal.
- **Policy** — The strategy mapping states to actions.
- **Q-value** — Expected future reward of an action in a state.
- **Bellman update** — Q(s,a) ← Q(s,a) + α[r + γ·maxQ(s') − Q(s,a)].
- **Exploration vs exploitation** — ε-greedy: sometimes explore, mostly exploit.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
import random
random.seed(0)

N = 5                       # states 0..4; goal is state 4
GOAL = 4
ACTIONS = [-1, +1]          # 0 = left, 1 = right
Q = [[0.0, 0.0] for _ in range(N)]
alpha, gamma, epsilon = 0.1, 0.9, 0.2

def step(s, a):
    ns = max(0, min(N - 1, s + ACTIONS[a]))
    reward = 1.0 if ns == GOAL else 0.0
    return ns, reward, ns == GOAL

for episode in range(500):
    s = 0
    for _ in range(50):
        # epsilon-greedy action selection
        if random.random() < epsilon:
            a = random.randint(0, 1)            # explore
        else:
            a = 0 if Q[s][0] >= Q[s][1] else 1  # exploit
        ns, r, done = step(s, a)
        # Bellman update
        Q[s][a] += alpha * (r + gamma * max(Q[ns]) - Q[s][a])
        s = ns
        if done:
            break

print("learned policy:")
for s in range(N):
    action = "right ->" if Q[s][1] >= Q[s][0] else "<- left"
    print(f"  state {s}: Q={[round(q, 2) for q in Q[s]]} -> {action}")
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Without exploration (ε=0) the agent gets stuck exploiting a suboptimal policy.
- ⚠️ γ (discount) near 1 values the far future; near 0 is myopic — tune it to the task.
- ⚠️ Sparse rewards make learning slow — the agent rarely sees a signal.
- ⚠️ Q-learning needs many episodes; it's sample-inefficient vs supervised learning.
- ⚠️ Plain Q-tables don't scale to large/continuous states — that's where deep RL (DQN) comes in.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.


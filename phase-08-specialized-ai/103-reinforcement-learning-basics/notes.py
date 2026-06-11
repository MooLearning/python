# ======================================================================
# 103 — Reinforcement Learning Basics  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: gymnasium
# Install:  pip install gymnasium

# ----------------------------------------------------------------------
# Example 1: Q-learning on a line world (the agent learns to reach the goal)
# ----------------------------------------------------------------------
print("\n--- Example 1: Q-learning on a line world (the agent learns to reach the goal) ---")
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

# ----------------------------------------------------------------------
# Example 2: The exploration/exploitation trade-off
# ----------------------------------------------------------------------
print("\n--- Example 2: The exploration/exploitation trade-off ---")
import random
random.seed(0)

# Three slot machines (bandits) with unknown win rates
true_rates = [0.2, 0.5, 0.75]
counts = [0, 0, 0]
values = [0.0, 0.0, 0.0]          # estimated value per machine
epsilon = 0.1

def pull(machine):
    return 1.0 if random.random() < true_rates[machine] else 0.0

for t in range(2000):
    if random.random() < epsilon:
        m = random.randint(0, 2)            # explore a random machine
    else:
        m = values.index(max(values))       # exploit the best so far
    reward = pull(m)
    counts[m] += 1
    values[m] += (reward - values[m]) / counts[m]   # incremental average

print("estimated win rates:", [round(v, 3) for v in values])
print("true win rates     :", true_rates)
print("most-played machine:", counts.index(max(counts)), "(should be #2)")

# ----------------------------------------------------------------------
# Example 3: RL environments with Gymnasium
# ----------------------------------------------------------------------
print("\n--- Example 3: RL environments with Gymnasium ---")
try:
    import gymnasium as gym

    env = gym.make("FrozenLake-v1", is_slippery=False)
    state, _ = env.reset(seed=0)
    print("observation space:", env.observation_space)
    print("action space     :", env.action_space)

    total_reward = 0
    for _ in range(20):
        action = env.action_space.sample()      # random policy
        state, reward, terminated, truncated, _ = env.step(action)
        total_reward += reward
        if terminated or truncated:
            break
    print("random-policy episode reward:", total_reward)
    env.close()
except ImportError:
    print("gymnasium not installed — run: pip install gymnasium")

print("\nDone! Tip: change values above and run again to learn by experiment.")

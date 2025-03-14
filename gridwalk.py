import numpy as np

# Initialize grid size and rewards
N = 4
rewards = -1 * np.ones((N, N))
rewards[N-1, N-1] = 0  # Terminal state reward

# Initialize value function
V = np.zeros((N, N))

# Set discount factor and convergence threshold
gamma = 0.7
theta = 1e-5

# Define possible actions: up, down, left, right
actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid_state(x, y):
    return 0 <= x < N and 0 <= y < N

def value_iteration(V, rewards, gamma, theta):
    while True:
        delta = 0
        V_new = np.copy(V)
        for i in range(N):
            for j in range(N):
                if (i, j) == (N-1, N-1):
                    continue
                v = V[i, j]
                new_values = []
                for action in actions:
                    ni, nj = i + action[0], j + action[1]
                    if is_valid_state(ni, nj):
                        new_values.append(rewards[i, j] + gamma * V[ni, nj])
                    else:
                        new_values.append(rewards[i, j] + gamma * V[i, j])
                V_new[i, j] = max(new_values)
                delta = max(delta, abs(v - V_new[i, j]))
        V = V_new
        if delta < theta:
            break
    return V

# Perform value iteration
V = value_iteration(V, rewards, gamma, theta)

# Print the final value function
print(V)

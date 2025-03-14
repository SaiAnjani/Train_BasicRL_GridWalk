# Gridworld Value Iteration

## Overview

`gridwalk.py` is a Python script that implements the Value Iteration algorithm for solving the Gridworld problem. The Gridworld problem is a common example in reinforcement learning where an agent navigates a grid to reach a goal while maximizing the cumulative reward.

## Code Explanation

The script performs the following steps:

1. **Initialization**: Define the grid, rewards, and transition probabilities.
2. **Value Iteration**: Iteratively update the value of each state based on the expected rewards and the values of neighboring states.
3. **Policy Extraction**: Derive the optimal policy from the computed state values.

### Key Components

- **Grid Definition**: The grid is defined with states, rewards, and terminal states.
- **Value Function**: A function that assigns a value to each state, representing the expected cumulative reward.
- **Bellman Update**: The core of the Value Iteration algorithm, updating state values based on neighboring states and rewards.
- **Policy**: A mapping from states to actions that maximizes the expected reward.

## Pseudocode

The pseudocode for the Value Iteration algorithm is as follows:

1. Initialize the value function for all states to zero.
2. Repeat until convergence:
   - For each state:
     - Compute the value for each action using the Bellman equation.
     - Update the state's value to the maximum value computed.
3. Extract the policy:
   - For each state:
     - Choose the action that maximizes the value.

```plaintext
Initialize V(s) = 0 for all states s
Repeat until convergence:
    For each state s:
        V(s) = max_a Σ P(s'|s,a) [R(s,a,s') + γV(s')]
Extract policy π:
    For each state s:
        π(s) = argmax_a Σ P(s'|s,a) [R(s,a,s') + γV(s')]
```

## Usage

To run the script, execute the following command:

```sh
python gridwalk.py
```

Ensure you have the necessary dependencies installed.

## Example

An example grid and the resulting optimal policy will be displayed after running the script.

```plaintext
Grid:
S  .  .  G
.  #  .  .
.  .  .  .

Optimal Policy:
→  →  →  G
↓  #  ↓  ↓
→  →  →  ↑
```

In this example, `S` is the start state, `G` is the goal state, `.` represents empty cells, and `#` represents obstacles. The arrows indicate the optimal policy for the agent to follow.


## Result

[[-2.94117 -2.7731  -2.533   -2.19   ]
 [-2.7731  -2.533   -2.19    -1.7    ]
 [-2.533   -2.19    -1.7     -1.     ]
 [-2.19    -1.7     -1.       0.     ]]

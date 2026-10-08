# Capacities of the two jugs
CAP_A = 4
CAP_B = 3

# goal amount
GOAL = 2

# Function to print the state
def print_state(state):
    print("Jug A:", state[0], "liters")
    print("Jug B:", state[1], "liters")
    print()

# generate all possible moves
def get_neighbors(state):
    neighbors = []
    a, b = state

    # 1. Fill Jug A
    if a < CAP_A:
        neighbors.append(((CAP_A, b), "Fill Jug A"))

    # 2. Fill Jug B
    if b < CAP_B:
        neighbors.append(((a, CAP_B), "Fill Jug B"))

    # 3. Empty Jug A
    if a > 0:
        neighbors.append(((0, b), "Empty Jug A"))

    # 4. Empty Jug B
    if b > 0:
        neighbors.append(((a, 0), "Empty Jug B"))

    # 5. pour jug A -> B
    amount = min(a, CAP_B - b)
    if amount > 0:
        neighbors.append(((a - amount, b + amount), "pour Jug A -> Jug B"))
    
    # 6. pour jug B -> A
    amount = min(b, CAP_A - a)
    if amount > 0:
        neighbors.append(((a + amount, b - amount), "pour Jug B -> Jug A"))

    return neighbors

# DFS Algorithm (Iterative using a Stack)
def dfs(start):

    stack = [(start, [])]
    visited = set()

    while stack:

        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)
        

        if state[0] == GOAL or state[1] == GOAL:
            return path
            
        # Generate neighbors
        for neighbor, action in reversed (get_neighbors(state)):
            if neighbor not in visited:

                stack.append((neighbor, path + [(neighbor, action)]))
    return None

# starting state
start = (0, 0)

# run DFS
solution = dfs(start)

# print solution
if solution:
    print("Solution found in", len(solution), "moves:\n")

    print("Initial state:")
    print_state(start)

    for state, action in solution:
        print(f"Action: {action}")
        print_state(state)
else:
    print("No solution found.")

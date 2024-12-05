from collections import deque

# Define the initial state and goal state
initial_state = (
    0,  # Elevator position
    (
        ('HM', 'LM'),       # Floor 1: Hydrogen Microchip, Lithium Microchip
        ('HG',),            # Floor 2: Hydrogen Generator
        ('LG',),            # Floor 3: Lithium Generator
        ()                  # Floor 4: Empty
    )
)

# Goal state is all items on the fourth floor
def is_goal(state):
    _, floors = state
    return len(floors[3]) == 4

# Check if a floor is valid (no unpowered microchip in the presence of another generator)
def is_valid_floor(floor):
    chips = {item[0] for item in floor if item.endswith('M')}
    generators = {item[0] for item in floor if item.endswith('G')}
    # Chips are safe if no generators, or every chip has its generator
    return not chips or chips.issubset(generators)

# Generate possible next states
def get_neighbors(state):
    elevator, floors = state
    current_floor = set(floors[elevator])
    floors = [set(f) for f in floors]
    neighbors = []

    # Possible moves: take 1 or 2 items from the current floor
    for move in [[item] for item in current_floor] + [[a, b] for a in current_floor for b in current_floor if a != b]:
        for direction in [-1, 1]:  # Move elevator up or down
            new_elevator = elevator + direction
            if 0 <= new_elevator < 4:  # Ensure valid floor
                # Remove items from current floor and add them to the target floor
                new_floors = [set(f) for f in floors]
                new_floors[elevator] -= set(move)
                new_floors[new_elevator] |= set(move)

                # Check if both floors are valid
                if is_valid_floor(new_floors[elevator]) and is_valid_floor(new_floors[new_elevator]):
                    # Convert back to tuples for immutability
                    neighbors.append((
                        new_elevator,
                        tuple(tuple(sorted(f)) for f in new_floors)
                    ))
    return neighbors

# Perform BFS to find the shortest path to the goal
def bfs(initial_state):
    queue = deque([(initial_state, 0)])  # (state, steps)
    visited = set()
    visited.add(initial_state)

    while queue:
        state, steps = queue.popleft()

        if is_goal(state):
            return steps

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))

    return -1  # If no solution found (should not happen for valid input)

# Solve the problem
steps = bfs(initial_state)
print(f"Minimum number of steps required: {steps}")

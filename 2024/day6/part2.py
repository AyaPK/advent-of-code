area = [[i for i in x.strip()] for x in open("input.txt").readlines()]

pos = next((x, y) for y, row in enumerate(area) for x, char in enumerate(row) if char == '^')
direction = "up"

turn = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up"
}

look = {
    "up": (0, -1),
    "down": (0, 1),
    "right": (1, 0),
    "left": (-1, 0)
}

def tup_add(tup, to_add):
    a = tup[0] + to_add[0]
    b = tup[1] + to_add[1]
    return (a, b)

candidates = [
    (x, y)
    for y, row in enumerate(area)
    for x, char in enumerate(row)
    if char == '.' and (x, y) != pos
]


def causes_loop(obstruction):
    area[obstruction[1]][obstruction[0]] = "#"
    visited_states = set()
    current_pos = pos
    current_dir = direction

    while True:
        state = (current_pos, current_dir)
        if state in visited_states:
            area[obstruction[1]][obstruction[0]] = "."  # Restore the map
            return True
        visited_states.add(state)

        next_pos = tup_add(current_pos, look[current_dir])

        if 0 <= next_pos[0] < len(area[0]) and 0 <= next_pos[1] < len(area):
            if area[next_pos[1]][next_pos[0]] != "#":
                current_pos = next_pos
            else:
                current_dir = turn[current_dir]
        else:
            break
    area[obstruction[1]][obstruction[0]] = "."
    return False


loop_causing_positions = [pos for pos in candidates if causes_loop(pos)]
print(len(loop_causing_positions))

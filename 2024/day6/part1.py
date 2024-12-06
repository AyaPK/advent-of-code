map = [[i for i in x.strip()] for x in open("input.txt").readlines()]

pos = next((x, y) for y, row in enumerate(map) for x, char in enumerate(row) if char == '^')

def tup_add(tup, to_add):
    a = tup[0] + to_add[0]
    b = tup[1] + to_add[1]
    return (a, b)

dir = "up"

turn = {
    "up": "right",
    "down": "left",
    "right": "down",
    "left": "up"
}

look = {
    "up": (0, -1),
    "down": (0, 1),
    "right": (1, 0),
    "left": (-1, 0)
}

visited = set()

while True:
    if pos[0] >= 0 and pos[0] < len(map) and pos[1] >= 0 and pos[1] < len(map[0]):
        ahead = tuple(tup_add(pos, look[dir]))
        object = map[ahead[1]][ahead[0]]
        if object != "#":
            pos = ahead
        else:
            dir = turn[dir]
        visited.add(pos)
    else:
        break
print(len(visited))
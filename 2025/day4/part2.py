with open("input.txt") as f:
    grid = [list(line.strip()) for line in f]

ROWS = len(grid)
COLS = len(grid[0])

NEIGHBORS = [
    (dx, dy)
    for dx in (-1, 0, 1)
    for dy in (-1, 0, 1)
    if not (dx == 0 and dy == 0)
]

def neighbors(x, y):
    for dx, dy in NEIGHBORS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < ROWS and 0 <= ny < COLS:
            yield nx, ny

def count_adjacent(x, y, char="@"):
    return sum(1 for nx, ny in neighbors(x, y) if grid[nx][ny] == char)

removed = 0

while True:
    to_remove = []

    for x in range(ROWS):
        for y in range(COLS):
            if grid[x][y] == "@":
                count = count_adjacent(x, y, "@")
                if count < 4:
                    removed += 1
                    to_remove.append((x, y))
    if not to_remove:
        break

    for x, y in to_remove:
        grid[x][y] = "."

print(removed)
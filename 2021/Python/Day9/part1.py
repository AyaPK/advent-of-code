grid = [[y for y in x.strip()] for x in open("input.txt").readlines()]

def get_adjacent(x, y):
    adjacent = []
    if x > 0:
        adjacent.append(grid[x-1][y])
    if x < len(grid) - 1:
        adjacent.append(grid[x+1][y])
    if y > 0:
        adjacent.append(grid[x][y-1])
    if y < len(grid[0]) - 1:
        adjacent.append(grid[x][y+1])
    return adjacent

for x in range(len(grid)):
    for y in range(len(grid[0])):
        grid[x][y] = int(grid[x][y])
risk_level = 0

for x in range(len(grid)):
    for y in range(len(grid[0])):
        current = grid[x][y]
        adjacent = get_adjacent(x, y)
        if all(current < adj for adj in adjacent):
            risk_level += current + 1
print(risk_level)
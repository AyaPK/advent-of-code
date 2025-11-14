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
basin_sizes = []
visited = set()
def dfs(x, y):
    if (x, y) in visited or grid[x][y] == 9:
        return 0
    visited.add((x, y))
    size = 1
    if x > 0:
        size += dfs(x-1, y)
    if x < len(grid) - 1:
        size += dfs(x+1, y)
    if y > 0:
        size += dfs(x, y-1)
    if y < len(grid[0]) - 1:
        size += dfs(x, y+1)
    return size
for x in range(len(grid)):
    for y in range(len(grid[0])):
        current = grid[x][y]
        adjacent = get_adjacent(x, y)
        if all(current < adj for adj in adjacent):
            basin_size = dfs(x, y)
            basin_sizes.append(basin_size)
basin_sizes.sort(reverse=True)
result = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
print(result)
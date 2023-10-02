grid = [y for y in [x.strip() for x in open("input.txt").readlines()]]
final_grid = []
for row in grid:
    final_grid.append([x for x in row])


def show_grid(grid):
    print("===" * 10)
    for row in grid:
        print("".join(row))
    print("===" * 10)


def check_neighbours(i, j):
    on = 0
    for y in range(i-1, i+2):
        for x in range(j-1, j+2):
            if x < 0 or y < 0:
                continue
            if i == y and x == j:
                continue
            try:
                neighbour = final_grid[y][x]
                if final_grid[y][x] == "#":
                    on += 1
            except:
                pass
    return on

indexes_to_turn_on = []
indexes_to_turn_off = []

for _ in range(100):
    for i, row in enumerate(final_grid):
        for j, col in enumerate(row):
            if check_neighbours(i,j) in [2, 3] and final_grid[i][j] == "#":
                indexes_to_turn_on.append((i,j))
            elif check_neighbours(i,j) == 3 and final_grid[i][j] == ".":
                indexes_to_turn_on.append((i,j))
            else:
                indexes_to_turn_off.append((i,j))

    for change in indexes_to_turn_on:
        final_grid[change[0]][change[1]] = "#"
    for change in indexes_to_turn_off:
        final_grid[change[0]][change[1]] = "."

    indexes_to_turn_on = []
    indexes_to_turn_off = []

lights = 0
for row in final_grid:
    for item in row:
        if item == "#":
            lights += 1
print(lights)
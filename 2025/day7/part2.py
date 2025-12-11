# Load grid
with open("input.txt") as f:
    grid = [list(line.rstrip("\n")) for line in f]

H = len(grid)
W = len(grid[0])

timelines = [[0] * W for _ in range(H)]

for y in range(H):
    for x in range(W):
        if grid[y][x] == "S":
            timelines[y][x] = 1
            start = (x, y)
            break

ended = 0

for y in range(H):
    for x in range(W):
        flow = timelines[y][x]
        if flow == 0:
            continue

        if grid[y][x] in (".", "S"):
            ny, nx = y + 1, x
            if ny < H:
                timelines[ny][nx] += flow
            else:
                ended += flow

        elif grid[y][x] == "|":
            ny, nx = y + 1, x
            if ny < H:
                timelines[ny][nx] += flow
            else:
                ended += flow

        elif grid[y][x] == "^":
            # Split left
            ny, nx = y + 1, x - 1
            if ny < H and 0 <= nx < W:
                timelines[ny][nx] += flow
            else:
                ended += flow

            # Split right
            ny, nx = y + 1, x + 1
            if ny < H and 0 <= nx < W:
                timelines[ny][nx] += flow
            else:
                ended += flow

        else:
            ended += flow

print(ended)

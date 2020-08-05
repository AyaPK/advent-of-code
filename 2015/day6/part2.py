import json
# process data before anything else
with open("input.txt", "r") as f:
    data = f.readlines()
    for x in range(len(data)):
        data[x] = data[x].replace("\n", "").replace("turn ", "")

# build grid
grid = []
for x in range(1000):
    toappend = []
    for y in range(1000):
        toappend.append(0)
    grid.append(toappend)


def change_bulb(x, y, c):
    if c == "off":
        grid[y][x] -= 1
    elif c == "on":
        grid[y][x] += 1
    elif c == "toggle":
        grid[y][x] += 2
    if grid[y][x] < 0:
        grid[y][x] = 0

def execute(start, end, c):
    for y in range(start[0], end[0]+1):
        for x in range(start[1], end[1]+1):
            change_bulb(x, y, c)
    pass

for i in data:
    command = i.split(" ")[0]
    start = (int(i.split(" ")[1].split(",")[0]),int(i.split(" ")[1].split(",")[1]))
    end = (int(i.split(" ")[3].split(",")[0]),int(i.split(" ")[3].split(",")[1]))
    execute(start, end, command)


brightness = 0
for col in grid:
    for light in col:
        brightness += light
print(brightness)
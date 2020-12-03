areaMap = [x.replace("\n", "") for x in open("input.txt", "r").readlines()]

x, y, = 0, 0
goal = len(areaMap)
trees = 0
while y < goal:
    if areaMap[y][x] == "#":
        trees += 1
    x += 3
    y += 1

    if x >= len(areaMap[0]):
        x -= len(areaMap[0])

print(trees)


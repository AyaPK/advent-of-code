areaMap = [x.replace("\n", "") for x in open("input.txt", "r").readlines()]

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
goal = len(areaMap)
collisions = []
for slope in slopes:
    h = slope[0]
    v = slope[1]
    trees = 0
    x, y, = 0, 0
    while y < goal:
        if areaMap[y][x] == "#":
            trees += 1
        x += h
        y += v

        if x >= len(areaMap[0]):
            x -= len(areaMap[0])

    collisions.append(trees)

output = 1
for i in collisions:
    output = output*i
print(output)


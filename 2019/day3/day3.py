set1 = set()
set2 = set()
stepdict = {}
stepcount = 0

x, y = 0, 0


def findclosest(a):
    return abs(a[0]) + abs(a[1])


with open("input.txt", "r") as f:
    instruct = f.read().split(",")

for a in range(len(instruct)):
    for b in range(int(instruct[a][1:])):
        dir = instruct[a][0]
        if dir == "R":
            x += 1
        elif dir == "L":
            x -= 1
        elif dir == "U":
            y -= 1
        elif dir == "D":
            y += 1
        set1.add((x, y))

x, y = 0, 0
with open("input2.txt", "r") as f:
    instruct = f.read().split(",")

for a in range(len(instruct)):
    for b in range(int(instruct[a][1:])):
        dir = instruct[a][0]
        if dir == "R":
            x += 1
        elif dir == "L":
            x -= 1
        elif dir == "U":
            y -= 1
        elif dir == "D":
            y += 1
        set2.add((x, y))

nodes = set1.intersection(set2)

print(min(findclosest(a) for a in nodes))

set1 = set()
set2 = set()
stepdictx = {}
stepdicty = {}
stepcount = 0

x, y = 0, 0

def findclosest(a):
    return abs(a[0])+abs(a[1])

def findclosesttwo(a):
    return stepdictx[a]+stepdicty[a]

with open("input.txt", "r") as f:
    instruct = f.read().split(",")

for a in range(len(instruct)):
    for b in range(int(instruct[a][1:])):
        dir = instruct[a][0]
        stepcount += 1
        if dir == "R":
            x += 1
            stepdictx[(x,y)] = stepcount
        elif dir == "L":
            x -= 1
            stepdictx[(x, y)] = stepcount
        elif dir == "U":
            y -= 1
            stepdictx[(x, y)] = stepcount
        elif dir == "D":
            y += 1
            stepdictx[(x, y)] = stepcount
            set1.add((x, y))

with open("input2.txt", "r") as f:
    instruct = f.read().split(",")

x, y = 0, 0
stepcount = 0
for a in range(len(instruct)):
    for b in range(int(instruct[a][1:])):
        dir = instruct[a][0]
        stepcount += 1
        if dir == "R":
            x += 1
            stepdicty[(x, y)] = stepcount
        elif dir == "L":
            x -= 1
            stepdicty[(x, y)] = stepcount
        elif dir == "U":
            y -= 1
            stepdicty[(x, y)] = stepcount
        elif dir == "D":
            y += 1
            stepdicty[(x, y)] = stepcount
        set2.add((x, y))

nodes = set1.intersection(set2)


print("CLOSEST BY STEP MANHATTAN: ",min(findclosest(a) for a in nodes))
print("CLOSEST BY STEP COUNT: ",min(findclosesttwo(a) for a in nodes))
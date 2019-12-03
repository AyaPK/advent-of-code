from PIL import Image

arr = []
arr2 = []

x, y = 0, 0

def plotpoints(inst, tomod):
    global x, y
    if inst[0] == "R":
        for x in range(0, int(inst[1:])):
            x += 1
            tomod.append([x, y])
    if inst[0] == "L":
        for x in range(0, int(inst[1:])):
            x -= 1
            tomod.append([x, y])
    if inst[0] == "U":
        for x in range(0, int(inst[1:])):
            y -= 1
            tomod.append([x, y])
    if inst[0] == "D":
        for x in range(0, int(inst[1:])):
            y += 1
            tomod.append([x, y])

with open("input.txt", "r") as f:
    ins = f.read().split(",")
for inst in ins:
    plotpoints(inst, arr)

x, y = 0, 0

with open("input2.txt", "r") as f:
    ins = f.read().split(",")
for inst in ins:
    plotpoints(inst, arr2)

print(arr)
print(arr2)

matches = []

iterations = 0
for a in arr:
    if a not in (matches):
        for b in arr2:
            if b not in (matches):
                if a == b:
                    matches.append(a)
                    iterations += 1
                    print(iterations)
print(matches)
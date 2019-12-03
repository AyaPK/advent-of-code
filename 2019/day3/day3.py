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


print(len(arr))
print(len(arr2))

matches = []

iterations = 0

for a in range(0, len(arr)):
    for b in range(0, len(arr2)):
        if arr[a] == arr2[b]:
            print(arr2[b])


print(matches)
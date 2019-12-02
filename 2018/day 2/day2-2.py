import string
arr = []
two = 0
three = 0
flags = []


def compare(a, b):
    global flags
    matchcount = 0
    for z in range(0, len(a)-1):
        if a[z] == b[z]:
            matchcount += 1
    if matchcount == 24:
        for z in range(0, len(a) - 1):
            if a[z] != b[z]:
                flags.append(z+1)
                print(a[z])

        print(a, b, flags)

with open("input.txt", "r") as f:
    data = f.readlines()
    for x in data:
        arr.append(x.replace("\n", ""))

for x in range(0, len(arr)):
    for y in range(0, len(arr)):
        compare(arr[x], arr[y])
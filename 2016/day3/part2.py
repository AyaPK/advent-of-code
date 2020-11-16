
with open("input.txt", "r") as f:
    data = f.readlines()

def testSides(first, second, third):
    return int(first) + int(second) > int(third)
count = 0

newarray = []
triarray = []
for i in data:
    i = i.strip()
    i = i.split(" ")
    while True:
        try:
            i.remove("")
        except ValueError:
            break
    newarray.append(i)

for x in range(0, len(newarray)-1, 3):
    triarray.append([])
    triarray.append([])
    triarray.append([])
    triarray[x].append(newarray[x][0])
    triarray[x].append(newarray[x+1][0])
    triarray[x].append(newarray[x+2][0])
    triarray[x+1].append(newarray[x][1])
    triarray[x+1].append(newarray[x + 1][1])
    triarray[x+1].append(newarray[x + 2][1])
    triarray[x+2].append(newarray[x][2])
    triarray[x+2].append(newarray[x + 1][2])
    triarray[x+2].append(newarray[x + 2][2])

for i in triarray:
    case1 = testSides(i[0], i[1], i[2])
    case2 = testSides(i[1], i[2], i[0])
    case3 = testSides(i[0], i[2], i[1])

    if case1 and case2 and case3:
        count+=1
print(count)

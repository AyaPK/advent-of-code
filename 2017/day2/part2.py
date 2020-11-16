with open("input.txt", "r") as f:
    data = f.readlines()
    for x in range(len(data)):
        data[x] = data[x].replace("\t", " ")

arr = []

for l in data:
    found = False
    line = l.replace("\n", "").split(" ")
    for x in range(len(line)):
        line[x] = int(line[x])
    for x in range(len(line)):
        for y in range(len(line)):
            ay = line[y]
            ax = line[x]
            if x != y:
                if (line[x]%line[y]) == 0:
                    if not found:
                        arr.append(line[x]/line[y])
                    found = True





print(sum(arr))
with open("input.txt", "r") as f:
    data = f.readlines()
    for x in range(len(data)):
        data[x] = data[x].replace("\t", " ")

arr = []
for l in data:
    line = l.replace("\n", "").split(" ")
    for x in range(len(line)):
        line[x] = int(line[x])
    line.sort()
    arr.append(abs(line[len(line)-1] - line[0]))

print(sum(arr))
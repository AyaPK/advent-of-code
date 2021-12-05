data = [x.strip() for x in open("input.txt", "r").readlines()]
mostCommon = ""

for x in range(len(data[0])):
    numbers = []
    if len(data) == 1:
        break
    for line in data:
        numbers.append(line[x])
    if numbers.count("1") > numbers.count("0"):
        data = [i for i in data if i[x] == "1"]
    elif numbers.count("1") < numbers.count("0"):
        data = [i for i in data if i[x] == "0"]
    else:
        data = [i for i in data if i[x] == "1"]

xxx = data[0]

data = [x.strip() for x in open("input.txt", "r").readlines()]
mostCommon = ""

for x in range(len(data[0])):
    numbers = []
    if len(data) == 1:
        break
    for line in data:
        numbers.append(line[x])
    if numbers.count("1") < numbers.count("0"):
        data = [i for i in data if i[x] == "1"]
    elif numbers.count("1") > numbers.count("0"):
        data = [i for i in data if i[x] == "0"]
    else:
        data = [i for i in data if i[x] == "0"]

yyy = data[0]


print(int(xxx, 2) * int(yyy, 2))
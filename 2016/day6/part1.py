import collections

with open("input.txt", "r") as f:
    data = f.readlines()

columns = [""]*len(data[0])
print(columns)

for line in data:
    for x in range(len(line)):
        columns[x] = columns[x]+line[x]

for line in columns:
    count = collections.Counter(line)
    print(count)

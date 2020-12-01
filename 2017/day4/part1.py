with open("input.txt", "r") as f:
    data = f.readlines()
    for x in range(len(data)):
        data[x] = data[x].replace("\n", "")

output = 0

for line in data:
    words = line.split(" ")
    for x in range(len(words)):
        words[x] = "".join(sorted(words[x]))
    if len(words) == len(set(words)):
        output+=1

print(output)
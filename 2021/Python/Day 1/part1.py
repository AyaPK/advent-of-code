data = [int(x.strip()) for x in open("input.txt", "r").readlines()]

output = 0

for x in range(1,len(data)):
    if data[x] > data[x-1]:
        output += 1

print(output)
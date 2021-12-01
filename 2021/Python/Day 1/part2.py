data = [int(x.strip()) for x in open("input.txt", "r").readlines()]

output = 0

for x in range(3,len(data)):
    if data[x]+data[x-1]+data[x-2] > data[x-1]+data[x-2]+data[x-3]:
        output += 1

print(output)
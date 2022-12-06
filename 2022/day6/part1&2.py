data = [x.strip() for x in open("input.txt").readlines()][0]

print([x+4 for x in range(len(data)-3) if len(set(data[x:x+4])) == 4])
print([x+14 for x in range(len(data)-13) if len(set(data[x:x+14])) == 14][0])

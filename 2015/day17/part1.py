from itertools import combinations

jars = [int(x.strip()) for x in open("input.txt").readlines()]

out = 0

length = len(jars)

for i in range(1,len(jars)):
    for x in combinations(jars,i):
        if sum(x) == 150:
            out += 1
            if len(x) < length:
                length = len(x)
print(f"Part 1: {out}")
print(f"Part 2: {length}")
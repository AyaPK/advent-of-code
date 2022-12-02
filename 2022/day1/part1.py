input = [x.strip() for x in open("input.txt", "r").readlines()]
elves, current = [], 0
for x in input:
    if x == "":
        elves.append(current)
        current = 0
    else:
        current += int(x)
elves.append(current)
print(sum(sorted(elves, reverse=True)[:3]))
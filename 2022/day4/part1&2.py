data = [x.strip() for x in open("input.txt").readlines()]

part1 = 0
part2 = 0
for line in data:
    elf1 = [x for x in range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1])+1)]
    elf2 = [x for x in range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1])+1)]
    part1 += (all(b in elf1 for b in elf2) or all(b in elf2 for b in elf1))
    part2 += (not set(elf1).isdisjoint(elf2))

print(part1)
print(part2)

import string

data = [x.strip() for x in open("input.txt").readlines()]

part1 = sum(string.ascii_letters.index("".join(set(x[:int(len(x)/2)]).intersection(x[int(len(x)/2):])))+1 for x in [x.strip() for x in open("input.txt").readlines()])
part2 = sum(string.ascii_letters.index("".join(set(data[x]).intersection(data[x+1]).intersection(data[x+2])))+1 for x in range(0,len(data),3))

print(f"Part 1: {part1}\nPart 2: {part2}")
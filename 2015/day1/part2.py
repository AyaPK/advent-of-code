def floor(inp):
    floor = 0
    count = 0
    for x in inp:
        if x == "(":
            floor += 1
            count += 1
        else:
            floor -= 1
            count += 1
        if floor == -1:
            return count


with open("input.txt", "r") as f:
    input = f.read()
print(floor(input))

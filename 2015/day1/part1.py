def floor(inp):
    return sum(1 for x in inp if x == "(")-sum(1 for x in inp if x == ")")

with open("input.txt", "r") as f:
    input = f.read()
print(floor(input))

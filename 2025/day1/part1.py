def parse(line):
    line = line.strip()
    return int(line[1:]) * (-1 if line[0] == "L" else 1)

moves = [parse(x) for x in open("input.txt")]

pos = 50
count = sum((pos := (pos + m) % 100) == 0 for m in moves)

print(count)

def parse(line):
    line = line.strip()
    return int(line[1:]) * (-1 if line[0] == "L" else 1)

moves = [parse(x) for x in open("input.txt")]

pos = 50
count = 0

for move in moves:
    if move > 0:
        for x in range(pos, pos + move):
            pos += 1
            if pos > 99:
                pos = 0
            if pos == 0:
                count += 1
    elif move < 0:
        for x in range(pos, pos + move, -1):
            pos -= 1
            if pos < 0:
                pos = 99
            if pos == 0:
                count += 1

print(count)
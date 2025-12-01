def parse(line):
    sign = -1 if line[0] == "L" else 1
    return sign * int(line[1:])

moves = [parse(x) for x in open("input.txt")]

pos = 50
count = 0

for m in moves:
    step = 1 if m > 0 else -1
    for x in range(abs(m)):
        pos = (pos + step) % 100
        if pos == 0:
            count += 1

print(count)

instructions = [x.replace("\n", "") for x in open("input.txt", "r").readlines()]

xpos, ypos = 0, 0
direction = "E"
r = {"N":"E", "E":"S", "S":"W", "W":"N"}
l = {"N":"W", "W":"S", "S":"E", "E":"N"}

def rotate_ship(d, n):
    global direction
    num = int(n/90)
    for x in range(num):
        if d == "R":
            direction = r[direction]
        elif d == "L":
            direction = l[direction]


for row in instructions:
    instruction = row[0]
    number = int(row[1:])
    if instruction == "N":
        ypos += number
    elif instruction == "S":
        ypos -= number
    elif instruction == "E":
        xpos += number
    elif instruction == "W":
        xpos -= number
    elif instruction == "F":
        if direction == "N":
            ypos += number
        elif direction == "S":
            ypos -= number
        elif direction == "E":
            xpos += number
        elif direction == "W":
            xpos -= number
    elif instruction in ["R", "L"]:
        rotate_ship(instruction, number)

print(abs(xpos)+abs(ypos))

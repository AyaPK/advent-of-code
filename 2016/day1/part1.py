dir = "North"
blocks = 0

with open ("input.txt", "r") as f:
    data = f.read()
    data = data.split(",")

for i in data:
    i = i.strip()
    direction = i[0]
    num = i[1:]
    if direction == "L":
        if dir == "North": dir = "West"
        elif dir == "West": dir = "South"
        elif dir == "South": dir = "East"
        elif dir == "East": dir = "North"
    elif direction == "R":
        if dir == "North": dir = "East"
        elif dir == "West": dir = "North"
        elif dir == "South": dir = "West"
        elif dir == "East": dir = "South"
    if dir == "North" or dir == "East":
        blocks += int(num)
    else:
        blocks -= int(num)
print(abs(blocks))
dir = "North"
blocks = 0
posx, posy = 0,0
visited = []
found = False
with open("input.txt", "r") as f:
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
    num = int(num)
    if dir == "North":
        for x in range(1, num+1):
            blocks += 1
            posy += 1
            if (posx, posy) not in visited:
                visited.append((posx, posy))
            else:
                print(abs(blocks))
                found = True
    elif dir == "South":
        for x in range(1, num + 1):
            blocks -= 1
            posy -= 1
            if (posx, posy) not in visited:
                visited.append((posx, posy))
            else:
                print(abs(blocks))
                found = True
    elif dir == "East":
        for x in range(1, num + 1):
            blocks += 1
            posx += 1
            if (posx, posy) not in visited:
                visited.append((posx, posy))
            else:
                print(abs(blocks))
                found = True
    else:
        for x in range(1, num + 1):
            blocks -= 1
            posx -= 1
            if (posx, posy) not in visited:
                visited.append((posx, posy))
            else:
                print(abs(blocks))
                found = True
    if found:
        break
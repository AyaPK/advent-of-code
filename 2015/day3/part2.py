def deliver(inp):
    sx, sy = 0, 0
    rx, ry = 0, 0
    arr = [(0, 0)]
    turn = "robo"
    for dir in inp:
        if dir == "^":
            if turn == "santa":
                sx -= 1
            else:
                rx -= 1
        elif dir == "v":
            if turn == "santa":
                sx += 1
            else:
                rx += 1
        elif dir == ">":
            if turn == "santa":
                sy += 1
            else:
                ry += 1
        else:
            if turn == "santa":
                sy -= 1
            else:
                ry -= 1

        if turn == "robo":
            arr.append((rx, ry))
            turn = "santa"
        else:
            arr.append((sx, sy))
            turn = "robo"
    return len(set(arr))

with open("input.txt", "r") as f:
    data = f.read()

print(deliver(data))
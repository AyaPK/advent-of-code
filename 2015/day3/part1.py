def deliver(inp):
    x, y = 0, 0
    arr = [(0, 0)]
    for dir in inp:
        if dir == "^":
            x -= 1
        elif dir == "v":
            x += 1
        elif dir == ">":
            y += 1
        else:
            y -= 1
        arr.append((x, y))
    return len(set(arr))

with open("input.txt", "r") as f:
    data = f.read()

print(deliver(data))
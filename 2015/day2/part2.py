def wrapping_paper(inp):
    total = 0
    ribbon = 0
    for box in inp:
        sides = box.split("x")
        l = int(sides[0])
        w = int(sides[1])
        h = int(sides[2])
        arr = []
        arr.append(2*l*w)
        arr.append(2*w*h)
        arr.append(2*h*l)
        arr.sort()
        total += sum(arr)+(arr[0]/2)

        sides.sort(key=int)
        ribbon += (int(sides[0])*2)+(int(sides[1])*2)
        ribbon += l*w*h
    return [int(total), ribbon]

with open("input.txt", "r") as f:
    data = f.readlines()
    for x in range(len(data)):
        data[x] = data[x].replace("\n", "")

out = wrapping_paper(data)
print("Paper needed: "+str(out[0]))
print("Ribbon needed: "+str(out[1]))

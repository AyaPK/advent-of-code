def wrapping_paper(inp):
    total = 0
    for box in inp:
        l = int(box.split("x")[0])
        w = int(box.split("x")[1])
        h = int(box.split("x")[2])
        arr = []
        arr.append(2*l*w)
        arr.append(2*w*h)
        arr.append(2*h*l)
        arr.sort()
        total += sum(arr)+(arr[0]/2)
    return int(total)

with open("input.txt", "r") as f:
    data = f.readlines()
    for x in range(len(data)):
        data[x] = data[x].replace("\n", "")

print(wrapping_paper(data))
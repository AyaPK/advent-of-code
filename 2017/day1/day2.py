data = open("input.txt", "r").read()

arr = []
half = int(len(data)/2)
for x in range(len(data)):
    new = half+x
    while new > len(data)-1:
        new -= len(data)
    if data[x] == data[int(new)]:
        arr.append(int(data[new]))
print(sum(arr))

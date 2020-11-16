data = open("input.txt", "r").read()

arr = []
for x in range(len(data)):
    try:
        if data[x] == data[x+1]:
            arr.append(int(data[x]))
    except:
        if data[x] == data[0]:
            arr.append(int(data[x]))
print(sum(arr))

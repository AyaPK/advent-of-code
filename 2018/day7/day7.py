firstarr = []
secondarr = []

with open("input.txt", "r") as f:
    data = f.readlines()

for a in data:
        firstarr.append(a.split(" ")[1])
for a in data:
        secondarr.append(a.split(" ")[7])

for x in firstarr:
    if x not in secondarr:
        print(x)
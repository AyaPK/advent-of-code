plot = {}
arr = {}

for x in range(-200, 500):
    for y in range(-200, 500):
        plot[(x, y)] = "-"

with open("input.txt", "r") as f:
    data = f.readlines()
    for d in data:
        num1 = int(d.replace("/n", "").split(",")[0])
        num2 = int(d.replace("/n", "").split(",")[1])
        arr[(num1, num2)] = 0
x = 1
for node in arr:
    plot[node] = x
    x += 1



def findclosesthome(a):
    print(min((node[0]+node[1])-(a[0]+a[1]) for node in arr))

findclosesthome((193,201))

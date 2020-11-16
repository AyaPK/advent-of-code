
with open("input.txt", "r") as f:
    data = f.readlines()

def testSides(first, second, third):
    return int(first) + int(second) > int(third)
count = 0
for i in data:
    i = i.strip()
    i = i.split(" ")
    while True:
        try:
            i.remove("")
        except ValueError:
            break

    case1 = testSides(i[0], i[1], i[2])
    case2 = testSides(i[1], i[2], i[0])
    case3 = testSides(i[0], i[2], i[1])

    if case1 and case2 and case3:
        count+=1
print(count)

import string
arr = []
two = 0
three = 0

def calc(id):
    global two
    global three
    twofound = False
    threefound = False
    for x in string.ascii_letters:
        if id.count(x) == 3:
            threefound = True
        elif id.count(x) == 2:
            twofound = True
    if threefound:
        three += 1
    if twofound:
        two += 1
    print(f"{id} : {threefound} {twofound}")

with open("input.txt", "r") as f:
    data = f.readlines()
    for x in data:
        arr.append(x.replace("\n", ""))

for y in arr:
    calc(y)

print(two)
print(three)
print(two*three)
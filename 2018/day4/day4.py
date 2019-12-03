from statistics import mode

def mostcommon(input):
    counter = 0
    out = input[0]
    for x in input:
        freq = input.count(x)
        if int(freq) > counter:
            counter = freq
            out = x
    return out, counter

arr = []
sch = {}
guardtouse = ""
tempsleep = 0
with open("input.txt", "r") as f:
    data = f.readlines()
    for x in data:
        arr.append(x.replace("\n", ""))

for x in range(0, len(arr)-1):
    if arr[x].split(" ")[2] == "Guard":
        guardtouse = arr[x].split(" ")[3]
        if guardtouse not in sch:
            sch[guardtouse] = 0
    elif arr[x].split(" ")[2] == "falls":
        tempsleep = int(arr[x].split(" ")[1][0:5].replace(":",""))
    elif arr[x].split(" ")[2] == "wakes":
        sch[guardtouse] = (sch[guardtouse])+((int(arr[x].split(" ")[1][0:5].replace(":",""))) - tempsleep)

print(sch)

array = []
for guard in sch:
    sleep907 = []
    using = False
    tempsleep = 0
    for x in range(0, len(arr)):
        if arr[x].split(" ")[2] == "Guard":
            if arr[x].split(" ")[3] == guard:
                using = True
            else:
                using = False
        elif arr[x].split(" ")[2] == "falls" and using:
            tempsleep = int(arr[x].split(" ")[1][0:5].replace(":",""))
        elif arr[x].split(" ")[2] == "wakes" and using:
            for y in range(tempsleep, int(arr[x].split(" ")[1][0:5].replace(":", ""))):
                sleep907.append(y)
    print(guard, len(sleep907))
    try:
        print(mode(sleep907))
    except:
        print("More than one mode")
    try:
        print(sleep907.count(mode(sleep907)))
        array.append([guard, mode(sleep907), sleep907.count(mode(sleep907))])
    except:
        pass
for thing in array:
    print(thing)
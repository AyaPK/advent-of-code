arr = []
with open("input.txt", "r") as f:
    data = f.read().split(",")
    for d in data:
        arr.append(int(d))

input = int(input("> "))

def calc():
    global input
    global arr
    x = 0
    while True:
        if len(str(arr[x])) <= 2:
            if str(arr[x]) == "3":
                step = 2
                dir = arr[x+1]
                arr[dir] = input
                x += step
            elif str(arr[x]) == "4":
                step = 2
                dir = arr[x+1]
                print("diagnostic ",arr[dir])
                x += step
            elif str(arr[x]) == "1":
                step = 4
                dir1 = arr[x + 1]
                dir2 = arr[x + 2]
                outdir = arr[x + 3]
                arr[outdir] = arr[dir1] + arr[dir2]

                x += step
            elif arr[x] == 2:
                step = 4
                dir1 = arr[x + 1]
                dir2 = arr[x + 2]
                outdir = arr[x + 3]
                arr[outdir] = arr[dir1] * arr[dir2]

                x += step
            elif arr[x] == 99:
                if arr[0] == 19690720:
                    print("found")
                break

        elif len(str(arr[x]))> 2:
            step = 4
            code = str(arr[x])
            opcode = int(code[-2:])
            inst1 = int(code[-3:-2])
            if inst1 == 0:
                inst1 = arr[x+1]
                inst1 = arr[inst1]
            else:
                inst1 = arr[x+1]
            if len(str(code)) > 3:
                inst2 = int(code[-4:-3])
                if inst2 == 0:
                    inst2 = arr[x+2]
                    inst2 = arr[inst2]
                else:
                    inst2 = arr[x + 2]
                outdir = arr[x+3]
            else:
                inst2 = arr[x + 2]
                outdir = arr[x + 3]
                try:
                    inst2 = arr[inst2]
                except:
                    pass

            if opcode == 1:
                step = 4
                arr[outdir] = inst1+inst2
                x += step
            if opcode == 2:
                step = 4
                arr[outdir] = inst1*inst2
                x += step
            if opcode == 4:
                step = 2
                print("diagnostic ",arr[x+1])
                x += step
        else:
            break
calc()
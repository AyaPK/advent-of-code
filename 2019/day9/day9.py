arr = {}
with open("input.txt", "r") as f:
    data = f.read().split(",")
    xy = 0
    for d in data:
        arr[xy] = int(d)
        xy += 1

print(len(arr))
input = int(input("> "))
relativebase = 0
def calc():
    global input
    global arr
    global relativebase
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
            elif str(arr[x]) == "5":
                dir1, dir2 = arr[x+1], arr[x+2]
                if arr[dir1] != 0:
                    x = arr[dir2]
                else:
                    x += 3
            elif str(arr[x]) == "6":
                dir1, dir2 = arr[x + 1], arr[x + 2]
                if arr[dir1] == 0:
                    x = arr[dir2]
                else:
                    x += 3
            elif str(arr[x]) == "7":
                dir1, dir2, dir3 = arr[x + 1], arr[x + 2], arr[x + 3]
                if arr[dir1] < arr[dir2]:
                    arr[dir3] = 1
                else:
                    arr[dir3] = 0
                x += 4
            elif str(arr[x]) == "8":
                dir1, dir2, dir3 = arr[x + 1], arr[x + 2], arr[x + 3]
                if arr[dir1] == arr[dir2]:
                    arr[dir3] = 1
                else:
                    arr[dir3] = 0
                x += 4
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
            elif arr[x] == 9:
                relativebase += arr[x+1]
                x += 2
            elif arr[x] == 99:
                if arr[0] == 19690720:
                    print("found")
                break

        elif len(str(arr[x]))> 2:
            step = 4
            code = str(arr[x])
            opcode = int(code[-2:])
            inst1 = int(code[-3:-2])
            if inst1 == 2:
                inst1 = arr[inst1+relativebase]
            elif inst1 == 0:
                inst1 = arr[x+1]
                inst1 = arr[inst1]
            else:
                inst1 = arr[x+1]
            if len(str(code)) > 3:
                inst2 = int(code[-4:-3])
                if inst2 == 2:
                    inst1 = arr[inst2 + relativebase]
                elif inst2 == 0:
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
                arr[outdir] = int(inst1)*int(inst2)
                x += step
            if opcode == 4:
                step = 2
                print("diagnostic ",arr[x+1])
                x += step
            if opcode == 5:
                if inst1 != 0:
                    x = inst2
                else:
                    x += 3
            if opcode == 6:
                if inst1 == 0:
                    x = inst2
                else:
                    x += 3
            if opcode == 7:
                if inst1 < inst2:
                    arr[outdir] = 1
                else:
                    arr[outdir] = 0
                x += 4
            if opcode == 8:
                if inst1 == inst2:
                    arr[outdir] = 1
                else:
                    arr[outdir] = 0
                x += 4
            if opcode == 9:
                relativebase = arr[inst1]
                x += 2
        else:
            break
calc()
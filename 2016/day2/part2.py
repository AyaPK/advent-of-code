from copy import deepcopy
pointer = (0,2)

with open("input.txt") as f:
    data = f.readlines()

keypad = [
    ["X", "X", "1", "X", "X"],
    ["X", "2", "3", "4", "X"],
    ["5", "6", "7", "8", "9"],
    ["X", "A", "B", "C", "X"],
    ["X", "X", "D", "X", "X"]
]
projection = [
    ["X", "X", "1", "X", "X"],
    ["X", "2", "3", "4", "X"],
    ["5", "6", "7", "8", "9"],
    ["X", "A", "B", "C", "D"],
    ["X", "X", "D", "X", "X"]
]
code = ""
for line in data:
    line = line.replace("\n", "")
    for i in line:
        currentpos = (pointer[0], pointer[1])
        if i == "U": pointer = (pointer[0], pointer[1] - 1)
        elif i == "D": pointer = (pointer[0], pointer[1] + 1)
        elif i == "L": pointer = (pointer[0] - 1, pointer[1])
        elif i == "R": pointer = (pointer[0] + 1, pointer[1])

        try:
            if keypad[pointer[1]][pointer[0]] == "X" or pointer[0] < 0 or pointer[0] > 4 or pointer[1] < 0 or pointer[1] > 4:
                pointer = currentpos
        except:
            pointer = currentpos
        projection = deepcopy(keypad)
        projection[pointer[1]][pointer[0]] = "(" + projection[pointer[1]][pointer[0]] + ")"
        print('\n'*80)
        for line in projection:
            print(line)
    code = code+keypad[pointer[1]][pointer[0]]




print(code)
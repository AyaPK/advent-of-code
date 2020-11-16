
pointer = (1,1)

with open("input.txt") as f:
    data =  f.readlines()

keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
code = ""
for line in data:
    for i in line:
        if i == "U": pointer = (pointer[0], pointer[1] - 1)
        elif i == "D": pointer = (pointer[0], pointer[1] + 1)
        elif i == "L": pointer = (pointer[0] - 1, pointer[1])
        elif i == "R": pointer = (pointer[0] + 1, pointer[1])

        if pointer[0] < 0: pointer = (0, pointer[1])
        if pointer[0] > 2: pointer = (2, pointer[1])
        if pointer[1] < 0: pointer = (pointer[0], 0)
        if pointer[1] > 2: pointer = (pointer[0], 2)

    code = code+str(keypad[pointer[1]][pointer[0]])
print(code)
code = [x.replace("\n", "") for x in open("input.txt", "r").readlines()]

visited = []
acc = 0
pointer = 0
while True:
    command = code[pointer].split(" ")[0]
    num = int(code[pointer].split(" ")[1])
    if pointer in visited:
        break
    visited.append(pointer)
    if command == "acc":
        acc += num
        pointer += 1
    elif command == "jmp":
        pointer += num
    else:
        pointer += 1
print(acc)
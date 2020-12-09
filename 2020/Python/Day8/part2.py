import cProfile

def f():
    tochange = 0
    while True:
        code = [x.replace("\n", "") for x in open("input.txt", "r").readlines()]
        if code[tochange].split(" ")[0] == "jmp":
            code[tochange] = " ".join(["nop", code[tochange].split(" ")[1]])
        elif code[tochange].split(" ")[0] == "nop":
            code[tochange] = " ".join(["jmp", code[tochange].split(" ")[1]])
        else:
            tochange += 1
            continue
        visited = []
        acc = 0
        pointer = 0
        breakfound = False
        while True:
            try:
                command = code[pointer].split(" ")[0]
                num = int(code[pointer].split(" ")[1])
                if pointer in visited:
                    breakfound = True
                    break
                elif pointer == len(code)+1:
                    break
                visited.append(pointer)
                if command == "acc":
                    acc += num
                    pointer += 1
                elif command == "jmp":
                    pointer += num
                else:
                    pointer += 1
            except:
                print(acc)
                break
        if breakfound:
            tochange += 1
        else:
            break

cProfile.run("f()")
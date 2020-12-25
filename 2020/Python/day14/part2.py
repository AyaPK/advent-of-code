import itertools
instructions = [x.replace("\n", "") for x in open("input.txt", "r").readlines()]
memory = {}
mask = "X"*32


for i in instructions:
    if i.split(" ")[0] == "mask":
        mask = i.split("=")[1].strip()
    else:
        address = int(i.split("[")[1].split("]")[0])
        value_to_write = int(i.split("=")[1].strip())

        add_bin = str(bin(address)).split("b")[1]
        while len(add_bin) < len(mask):
            add_bin = "0"+add_bin
        addresses = []
        fi = []
        newadd = ""
        for x in range(len(add_bin)):
            if mask[x] == "1":
                newadd = newadd+"1"
            elif mask[x] == "X":
                newadd = newadd+"F"
                fi.append(x)
            else:
                newadd = newadd+add_bin[x]
        fuzzies = newadd.count("F")
        binary = list(itertools.product(["0", "1"], repeat=int(fuzzies)))
        for b in binary:
            changed = [x for x in newadd]
            for x in range(len(b)):
                changed[fi[x]] = b[x]
            new_add = int("".join(changed).replace("X", ""), 2)
            addresses.append(new_add)
        for a in addresses:
            memory[a] = value_to_write
output = 0
for x in memory:
    #print(f"{x} : {memory[x]}")
    output += memory[x]
print(output)


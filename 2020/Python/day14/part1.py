instructions = [x.replace("\n", "") for x in open("input.txt", "r").readlines()]
memory = [0]*1000000
mask = "X"*32


for i in instructions:
    if i.split(" ")[0] == "mask":
        mask = i.split("=")[1].strip()
    else:
        address = int(i.split("[")[1].split("]")[0])
        value_to_write = int(i.split("=")[1].strip())

        val_bin = str(bin(value_to_write)).split("b")[1]
        while len(val_bin) < len(mask):
            val_bin = "0"+val_bin
        val_bin = [x for x in val_bin]
        for x in range(len(val_bin)):
            if mask[x] != "X":
                val_bin[x] = mask[x]
        val_bin = "".join(val_bin)
        memory[address] = int(val_bin, 2)
print(sum(memory))


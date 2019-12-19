import intcode

memory1 = intcode.compute(1, "input.txt")
memory2 = intcode.computewithgivenmemory(memory1[0], memory1[1], memory1[2])
memory3 = intcode.computewithgivenmemory(memory2[0], memory2[1], memory2[2])
print(memory1)
print(memory2)
print(memory3)

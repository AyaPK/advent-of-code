"""
To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to
allocate to these operations. For example, in the above instructions, the highest value ever held was 10
(in register c after the third instruction was evaluated).
"""

import operator as op

ins = [x.strip() for x in open("input.txt").readlines()]

memory = {}

comparators = {
    ">": op.gt,
    "<": op.lt,
    ">=": op.ge,
    "<=": op.le,
    "==": op.eq,
    "!=": op.ne,
}

values = []

for i in ins:
    left = i.split(" ")[0]
    is_inc = i.split(" ")[1] == "inc"
    amt = int(i.split(" ")[2])
    right = i.split(" ")[4]
    comparator = i.split(" ")[5]
    compare_value = int(i.split(" ")[6])

    if left not in memory:
        memory[left] = 0

    if right not in memory:
        memory[right] = 0

    if comparators[comparator](memory[right], compare_value):
        if is_inc:
            memory[left] += amt
        else:
            memory[left] -= amt
    values.append(max(memory.values()))

print(max(memory.values()))
print(max(values))
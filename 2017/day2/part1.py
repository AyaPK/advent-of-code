data = [
    [int(x) for x in row.strip().split()]
    for row in open("input.txt")
]

print(sum(max(x)-min(x) for x in data))

import itertools as ite

out = sum(
    pair[0] // pair[1]
    for x in data
    for pair in ite.permutations(x, 2)
    if pair[0] % pair[1] == 0
)
print(int(out))
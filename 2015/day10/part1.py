from itertools import groupby

# Part 1
num = "1113122113"
for x in range(40):
    res = ["".join(group) for ele, group in groupby(num)]
    num = "".join(f"{len(x)}{x[0]}" for x in res)
print(len(num))

# Part 2
num = "1113122113"
for x in range(50):
    res = ["".join(group) for ele, group in groupby(num)]
    num = "".join(f"{len(x)}{x[0]}" for x in res)

print(len(num))
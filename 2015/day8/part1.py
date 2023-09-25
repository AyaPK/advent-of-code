import ast
total = 0
out = []
for x in open("input.txt", "r").readlines():
    total += len(x.strip())
    out.append(f"{ast.literal_eval(x.strip())}")
print(total - len("".join(out)))

import re

code = open("input.txt").read()

mul = r"mul\((\d+),(\d+)\)"
control = r"do\(\)|don't\(\)"

enabled = True
total = 0

matches = re.finditer(fr"{control}|{mul}", code)

for match in matches:
    if match.group().startswith("do()"):
        enabled = True
    elif match.group().startswith("don't()"):
        enabled = False
    elif enabled and match.group().startswith("mul"):
        a, b = map(int, match.groups())
        total += a * b

print(total)
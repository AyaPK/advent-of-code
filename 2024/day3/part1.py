import re

code = open("input.txt").read()
commands = re.findall(r"mul\((\d+),(\d+)\)", code)
total = sum(int(a) * int(b) for a, b in commands)

print(total)
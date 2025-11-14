displays = [x.strip() for x in open("input.txt").readlines()]

print(displays)

out = sum(1 for display in displays for digit in display.split(" | ")[1].split() if len(digit) in [2, 3, 4, 7])
print(out)
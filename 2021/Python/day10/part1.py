lines = [x.strip() for x in open("input.txt").readlines()]

points = {")": 3, "]": 57, "}": 1197, ">": 25137}

total = 0

for line in lines:
    stack = ""
    for char in line:
        if char in "([{<":
            stack += char
        else:
            if char == ")" and stack[-1] == "(":
                stack = stack[:-1]
            elif char == "]" and stack[-1] == "[":
                stack = stack[:-1]
            elif char == "}" and stack[-1] == "{":
                stack = stack[:-1]
            elif char == ">" and stack[-1] == "<":
                stack = stack[:-1]
            else:
                total += points[char]
                break
print(total)
lines = [x.strip() for x in open("input.txt").readlines()]

points = {")": 3, "]": 57, "}": 1197, ">": 25137}

total = 0
to_remove = []

for x in range(len(lines)):
    line = lines[x]
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
                to_remove.append(x)
                break
for index in reversed(to_remove):
    lines.pop(index)

completion_points = {")": 1, "]": 2, "}": 3, ">": 4}
scores = []
for line in lines:
    stack = ""
    for char in line:
        if char in "([{<":
            stack += char
        else:
            stack = stack[:-1]
    completion_string = ""
    for char in reversed(stack):
        if char == "(":
            completion_string += ")"
        elif char == "[":
            completion_string += "]"
        elif char == "{":
            completion_string += "}"
        elif char == "<":
            completion_string += ">"
    score = 0
    for char in completion_string:
        score = score * 5 + completion_points[char]
    scores.append(score)
scores.sort()
print(scores[len(scores)//2])

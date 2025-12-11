with open("input.txt") as f:
    table = [list(line.strip()) for line in f]
splitcount = 0
for y in range(len(table)):
    row = table[y]
    for x in range(len(row)):
        character = row[x]
        try:
            if character == "." or character == "^":
                pass
            elif character == "S" or character == "|":
                if table[y+1][x] == "^":
                    table[y+1][x-1] = "|"
                    table[y+1][x+1] = "|"
                    splitcount += 1
                else:
                    table[y+1][x] = "|"
        except IndexError:
            pass

print(splitcount)

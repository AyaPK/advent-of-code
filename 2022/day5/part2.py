import string
data = [x for x in open("input.txt").readlines()]

# parsing the input
end_of_stack_index = 0
for x, row in enumerate(data):
    if row.replace(" ", "")[0] in string.digits:
        end_of_stack_index = x
        break
stack_lines = []
for x in range(end_of_stack_index-1, -1, -1):
    stack_lines.append(data[x].replace("\n",""))
data = [x.strip() for x in data[end_of_stack_index+2:]]
rows = {}
for row in stack_lines:
    for i, letter in enumerate(row):
        if letter not in "[ ]":
            try:
                rows[str((i+3)//4)] += letter
            except:
                rows[str((i+3)//4)] = letter

# Actually solving the puzzle
for move in data:
    amount = int(move.split("from")[0].split(" ")[1])
    origin = move.split("from")[1].split(" ")[1]
    destination = move.split("from")[1].split(" ")[3]
    letter_to_move = rows[origin][len(rows[origin])-(amount):len(rows[origin])]
    rows[destination] += rows[origin][len(rows[origin])-(amount):len(rows[origin])]
    rows[origin] = rows[origin][:len(rows[origin])-(amount)]
print("".join(rows[x][-1] for x in rows))

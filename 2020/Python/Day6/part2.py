
data = [x.replace("\n", "") for x in open("input.txt", "r").readlines()]
forms = []
string = []
for line in data:
    if line != "":
        string.append(line)
    else:
        forms.append(",".join(string))
        string = []
forms.append(",".join(string))

output = 0
for form in forms:
    all_yes = []
    for person in form.split(","):
        for answer in person:
            if answer not in all_yes and form.count(answer) == len(form.split(",")):
                all_yes.append(answer)
    output += len(all_yes)

print(output)
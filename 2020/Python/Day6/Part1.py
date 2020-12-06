data = [x.replace("\n", "") for x in open("input.txt", "r").readlines()]
forms = []
string = ""
for line in data:
    if line != "":
        string = string+line
    else:
        forms.append(string)
        string = ""
forms.append(string)

yes_answer_counts = []
for form in forms:
    yes_answer_counts.append(len(set(form)))
print(sum(yes_answer_counts))

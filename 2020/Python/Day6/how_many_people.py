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

print(sum(len(x.split(",")) for x in forms))


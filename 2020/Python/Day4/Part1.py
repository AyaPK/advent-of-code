data = open("input.txt", "r").readlines()

passports = []
passport = {}

for line in data:
    if line != "\n":
        for pair in line.split(" "):
            k = pair.split(":")[0]
            v = pair.split(":")[1].replace("\n", "")
            passport[k] = v
    else:
        passports.append(passport)
        passport = {}
passports.append(passport)
passport = {}

print(sum(1 for p in passports if len(p) == 8 or (len(p) == 7 and "cid" not in p)))
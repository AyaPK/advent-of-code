inp = [x.strip() for x in open("input.txt", "r").readlines()]
out = [x.strip() for x in open("output.txt", "r").readlines()]

aunts = []

results = {}
for item in out:
    i = item.split(":")[0]
    count = item.split(":")[1].strip()
    results[i] = int(count)

for aunt in inp:
    owned = {}
    items = [x.split(":") for x in "".join(aunt.split(" ")[2:]).split(",")]
    for item in items:
        owned[item[0]] = int(item[1])
    aunts.append(owned)

def is_it_aunt():
    for item in aunt:
        if aunt[item] != results[item]:
            return False
    return True

found = False
for i, aunt in enumerate(aunts):
    if is_it_aunt():
        print(aunt)
        print(i+1)

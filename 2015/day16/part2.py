"""
As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many
(due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and
goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?
"""

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

def is_it_aunt(x):
    higher_items = ["cats", "trees"]
    lower_items = ["pomeranians", "goldfish"]
    for item in aunt:
        # print(f"ID: {x+1} | item: {item} - Aunt count: {aunt[item]} - Result: {results[item]}")
        if aunt[item] != results[item] and item not in higher_items+lower_items:
            return False
        elif item in higher_items:
            if aunt[item] <= results[item]:
                return False
        elif item in lower_items:
            if aunt[item] >= results[item]:
                return False
    return True

found = False
for i, aunt in enumerate(aunts):
    if is_it_aunt(i):
        print(aunt)
        print(i+1)

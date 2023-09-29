from itertools import permutations

details = [x.strip() for x in open("input.txt", "r").readlines()]
relationships = {}
people = set()
people.add("Me")


def is_positive(kind, amount):
    return -int(amount) if kind == "lose" else int(amount)


for detail in details:
    person = detail.split(" ")[0]
    friend = detail.split(" ")[-1].replace(".", "")
    kind = detail.split(" ")[2]
    amount = is_positive(kind, detail.split(" ")[3])
    people.add(person)
    if person not in relationships:
        relationships[person] = {}
    relationships[person][friend] = amount

relationships["Me"] = {}
for person in people:
    relationships["Me"][person] = 0
    relationships[person]["Me"] = 0

orders = [x for x in permutations(relationships)]

final_counts = []
for order in orders:
    order_change = 0
    for i, person in enumerate(order):
        order_change += (relationships[person][order[i - 1]] + relationships[order[i - 1]][person])
    final_counts.append(order_change)

print(max(final_counts))

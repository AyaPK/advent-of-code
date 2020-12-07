data = open("input.txt", "r").readlines()
data = [x.replace("\n", "") for x in data]
rules = {}
for rule in data:
    container = " ".join(rule.split(" ")[:2])
    bags = []
    for bag in rule.split("contain")[1].split(","):
        bags.append(" ".join(bag.split(" ")[1:4]))
    rules[container] = bags
for rule in rules:
    if rules[rule] == ["other bags."]:
        rules[rule] = None


bags_inside = ["shiny gold"]
def get_bags_inside(outer):
    try:
        for bag in rules[outer]:
            count = int(bag.split(" ")[0])
            for x in range(count):
                bags_inside.append(" ".join(bag.split(" ")[1:]))
    except:
        pass #Found a bag with no required children

for bag in bags_inside:
        get_bags_inside(bag)
print(len(bags_inside)-1)



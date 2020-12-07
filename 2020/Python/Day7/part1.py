data = open("input.txt", "r").readlines()
data = [x.replace("\n", "") for x in data]
rules = {}
for rule in data:
    container = " ".join(rule.split(" ")[:2])
    bags = []
    for bag in rule.split("contain")[1].split(","):
        bags.append(" ".join(bag.split(" ")[2:4]))
    rules[container] = bags
for rule in rules:
    if rules[rule] == ["other bags."]:
        rules[rule] = None

shiny_gold_parents = []
found = True
def find_containers(bag):
    global found
    global shiny_gold_parents
    rule_found = False
    for rule in rules:
        try:
            if bag in rules[rule] and rule not in shiny_gold_parents:
                shiny_gold_parents.append(rule)
                rule_found = True
        except:
            pass
    if not rule_found:
        found = False

find_containers("shiny gold")
while found:
    for x in shiny_gold_parents:
        find_containers(x)
print(len(shiny_gold_parents))
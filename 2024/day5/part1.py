input = [x.strip() for x in open("input.txt").readlines()]
rules_in, updates = input[:input.index("")], input[input.index("")+1:]

rules = {}
for before, after in (rule.split("|") for rule in rules_in):
    rules[before] = rules.get(before, []) + [after]

bads = {
    update
    for update in updates
    for i, page in enumerate(update.split(","))
    if i + 1 < len(update.split(",")) and update.split(",")[i + 1] in rules and page in rules[update.split(",")[i + 1]]
}

goods = [x for x in updates if x not in bads]
middle_sum = sum(int(s.split(',')[len(s.split(',')) // 2]) for s in goods)
print(middle_sum)
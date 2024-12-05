input = [x.strip() for x in open("input.txt").readlines()]
rules_in, updates = input[:input.index("")], input[input.index("")+1:]

rules = {}
for before, after in (rule.split("|") for rule in rules_in):
    rules[before] = rules.get(before, []) + [after]
print(rules)

bads = {
    update
    for update in updates
    for i, page in enumerate(update.split(","))
    if i + 1 < len(update.split(",")) and update.split(",")[i + 1] in rules and page in rules[update.split(",")[i + 1]]
}

goods = [x for x in updates if x not in bads]
middle_sum = sum(int(s.split(',')[len(s.split(',')) // 2]) for s in goods)

corrected_bads = [
    ",".join(sorted(update.split(","), key=lambda p: sum(1 for r in rules.get(p, []) if r in update.split(",")), reverse=True))
    for update in bads
]

corrected_middle_sum = sum(int(s.split(',')[len(s.split(',')) // 2]) for s in corrected_bads)
print(corrected_middle_sum)
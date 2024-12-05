from collections import defaultdict
import re

robots = defaultdict(list)
outputs = defaultdict(list)

with open('input.txt') as file:
    lines = file.read().splitlines()

rules = {}
for instruction in lines:
    if instruction.startswith('value'):
        value, robot_id = map(int, re.findall(r'\d+', instruction))
        robots[robot_id].append(value)
    elif instruction.startswith('bot'):
        numbers = list(map(int, re.findall(r'\d+', instruction)))
        source, low_id, high_id = numbers[0], numbers[1], numbers[2]
        targets = re.findall(r'(bot|output)', instruction)
        low_target, high_target = targets[0], targets[1]
        rules[source] = ((low_target, low_id), (high_target, high_id))

while any(len(chips) >= 2 for chips in robots.values()):
    for robot_id, chips in list(robots.items()):
        if len(chips) >= 2:
            low_chip, high_chip = sorted(chips)
            robots[robot_id] = []

            if low_chip == 17 and high_chip == 61:
                print(robot_id)

            (low_target, low_id), (high_target, high_id) = rules[robot_id]

            if low_target == 'bot':
                robots[low_id].append(low_chip)
            else:
                outputs[low_id].append(low_chip)

            if high_target == 'bot':
                robots[high_id].append(high_chip)
            else:
                outputs[high_id].append(high_chip)

product = 1
for index in [0, 1, 2]:
    product *= outputs[index][0]

print(product)
from itertools import product
from operator import add, mul

equations = [x.strip() for x in open("input.txt").readlines()]

def calculate_all_results(numbers):
    operators = {'+': add, '*': mul}
    operator_symbols = list(operators.keys())
    combinations = product(operator_symbols, repeat=len(numbers) - 1)
    results = []

    for combo in combinations:
        current_result = numbers[0]
        expression = str(numbers[0])
        for i, operator in enumerate(combo):
            current_result = operators[operator](current_result, numbers[i + 1])
            expression += f" {operator} {numbers[i + 1]}"
        results.append((expression, current_result))

    return results

found = 0
found_good = set()

for equation in equations:
    numbers = equation.split(":")[1].strip().split(" ")
    numbers = [int(x) for x in numbers]
    results = calculate_all_results(numbers)
    for result in results:
        if result[1] == int(equation.split(":")[0]):
            found_good.add(result[1])

print(sum(found_good))
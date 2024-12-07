from itertools import product
from operator import add, mul


def concat(x, y):
    return int(f"{x}{y}")


equations = [x.strip() for x in open("input.txt").readlines()]


def calculate_all_results(numbers):
    operators = {'+': add, '*': mul, '||': concat}
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


found_good = set()

for equation in equations:
    target = int(equation.split(":")[0])
    numbers = list(map(int, equation.split(":")[1].strip().split(" ")))

    results = calculate_all_results(numbers)

    for result in results:
        if result[1] == target:
            found_good.add(result[1])

print(sum(found_good))

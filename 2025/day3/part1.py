batteries = [x.strip() for x in open("input.txt").readlines()]

def highest_joltage(s: str, k: int) -> int:
    digits = list(map(int, s))
    n = len(digits)
    result = []

    start = 0
    for remaining in range(k, 0, -1):
        end = n - remaining
        max_digit = -1
        max_index = start
        for i in range(start, end + 1):
            if digits[i] > max_digit:
                max_digit = digits[i]
                max_index = i
        result.append(str(max_digit))
        start = max_index + 1
    return int("".join(result))

joltage = 0
for bank in batteries:
    joltage += highest_joltage(bank, 2)
print(f"Part 1: {joltage}")

joltage = 0
for bank in batteries:
    joltage += highest_joltage(bank, 12)
print(f"Part 2: {joltage}")
import itertools

data = [int(x.replace("\n","")) for x in open("input.txt", "r").readlines()]

preamble_length = 25
numbers = data[:preamble_length]
pointer = preamble_length+0

while True:
    couples = itertools.combinations(numbers, 2)
    sums = [sum(x) for x in couples]
    if data[pointer] not in sums:
        print(data[pointer])
        break
    else:
        numbers = numbers[1:]
        numbers.append(data[pointer])
        pointer += 1



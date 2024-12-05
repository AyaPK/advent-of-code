with open('input.txt') as file:
    data = file.read().strip()

is_part2 = False

def calculate_decompression_length(sequence):
    total_length = 0
    while '(' in sequence:
        prefix, sequence = sequence.split('(', 1)
        total_length += len(prefix)
        marker, sequence = sequence.split(')', 1)
        length, repeat = map(int, marker.split('x'))
        segment = sequence[:length]
        sequence = sequence[length:]
        if is_part2:
            total_length += calculate_decompression_length(segment) * repeat
        else:
            total_length += len(segment) * repeat
    total_length += len(sequence)
    return total_length

print(calculate_decompression_length(data))
is_part2 = True
print(calculate_decompression_length(data))

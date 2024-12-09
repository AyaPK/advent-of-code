def check_if_done(a, b, disk):
    if a == b:
        print(sum(i * n for i, n in enumerate(disk[:a])))
        quit()


def prepare_disk(input_line):
    disk = []
    for i in range(len(input_line) // 2):
        count_ones = int(input_line[i * 2])
        count_negatives = int(input_line[i * 2 + 1])
        disk.extend([i] * count_ones)
        disk.extend([-1] * count_negatives)
    return disk


input_line = open("input.txt").read().strip() + '0'
disk = prepare_disk(input_line)

a, b = 0, len(disk) - 1

while True:
    while disk[a] != -1:
        a += 1
        check_if_done(a, b, disk)

    while disk[b] == -1:
        b -= 1
        check_if_done(a, b, disk)

    disk[a], disk[b] = disk[b], -1

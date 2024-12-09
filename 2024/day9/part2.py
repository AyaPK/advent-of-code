input_data = open("input.txt").read().strip() + '0'

disk = []
free_spaces = []
files = []

for i in range(len(input_data) // 2):
    n, m = int(input_data[i * 2]), int(input_data[i * 2 + 1])
    files.append((len(disk), n))
    if m > 0:
        free_spaces.append([len(disk) + n, m])

    disk.extend([i for x in range(n)])
    disk.extend([-1 for x in range(m)])

for file_start, file_length in reversed(files):
    for free_space in free_spaces:
        if free_space[0] >= file_start:
            break
        if file_length <= free_space[1]:
            for i in range(file_length):
                disk[free_space[0] + i], disk[file_start + i] = disk[file_start + i], -1
            free_space[0] += file_length
            free_space[1] -= file_length
            break

result = sum(i * n for i, n in enumerate(disk) if n > 0)
print(result)
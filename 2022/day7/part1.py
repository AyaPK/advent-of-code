import string
commands = [x.strip() for x in open("input.txt").readlines()]

commands = [x.split(' ') for x in commands]
data_system = {}
directory = []

for row in commands:
    if row[0] == '$' and row[1] == 'cd':
        if row[2] == '/':
            directory = ['//']
            data_system['//'] = 0
        elif row[2] == '..':
            directory.pop()
        else:
            cursor = '/'.join(directory) + '/' + row[2]
            directory.append(cursor)
            if not data_system.get(cursor):
                data_system[cursor] = 0
    elif str(row[0])[0] in string.digits:
        for dir in directory:
            data_system[dir] += int(row[0])

output = [x for x in data_system.values() if x <= 100000]
print(sum(output))

output = [x for x in data_system.values() if x > data_system['//'] - 40000000]
print(min(output))

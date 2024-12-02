import time
st = time.time()

with open("input.txt", "r") as file:
    data = file.readlines()

seeds = [int(i) for i in data[0].strip().split(": ")[1].split(" ")]
mappings = []
for line in data[2:]:
    line = line.strip()
    if line.endswith(":"):
        mappings.append([])
    elif len(line) > 0:
        mappings[-1].append([int(i) for i in line.split(" ")])

[m.sort(key=lambda x: x[1]) for m in mappings]

res = 2**32
for x in seeds:
    for typemappings in mappings:
        for mapping in typemappings:
            if x >= mapping[1] and x < mapping[1] + mapping[2]:
                x = x - mapping[1] + mapping[0]
                break
    res = min(x, res)
print(res)

with open("input.txt", "r") as file:
    data = file.readlines()

seeds = [int(i) for i in data[0].strip().split(": ")[1].split(" ")]
mappings = []
for line in data[2:]:
    line = line.strip()
    if line.endswith(":"):
        mappings.append([])
    elif len(line) > 0:
        mappings[-1].append([int(i) for i in line.split(" ")])

res = 2**64
for s, o in zip(seeds[::2], seeds[1::2]):
    ranges = [(s, s + o - 1)]
    for typemappings in mappings:
        newranges = []
        for l, h in ranges:
            found = False
            for md, ms, mo in typemappings:
                if l >= ms and h < ms + mo:
                    newranges.append((l - ms + md, h - ms + md))
                    found = True
                elif l < ms and h >= ms and h < ms + mo:
                    ranges.append((l, ms - 1))
                    newranges.append((md, md + h - ms))
                    found = True
                elif l < ms + mo and h >= ms + mo and l >= ms:
                    ranges.append((ms + mo, h))
                    newranges.append((md + l - ms, md + mo - 1))
                    found = True
                elif l < ms and h >= ms + mo:
                    ranges.append((l, ms - 1))
                    newranges.append((md, md + mo - 1))
                    ranges.append((ms + mo, h))
                    found = True
                if found == True:
                    break
            if found == False:
                newranges.append((l, h))
        ranges = newranges.copy()
    res = min(res, min(ranges)[0])
print(res)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
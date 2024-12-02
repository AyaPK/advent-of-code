import re


def searchAdjacents(engine):
    parts = []
    for j in range(len(engine)):
        # search all integers in current engine line useing re.finditer()
        # to account for duplicates and get position in string
        for p in re.finditer(r'\d+', engine[j]):
            pn = p.group(0)  # matched integer
            ps = p.start()  # start position in string
            pe = p.end()  # end position in string
            # search for symbol around part number
            s = []
            for Y in range(max(j - 1, 0), min(j + 2, len(engine))):
                for X in range(max(ps - 1, 0), min(pe + 1, len(engine[j]))):
                    if not engine[Y][X].isdigit() and engine[Y][X] != ".":
                        s.append((engine[Y][X], (X, Y)))
            if len(s):
                parts.append((int(pn), s[0]))
    return parts


from collections import defaultdict


def part1(infile):
    with open(infile) as f:
        engine = f.read().split()
        adj = searchAdjacents(engine)
        return sum([n for n, p in adj])


print("Part 1:", part1("input.txt"))

def part2(infile):
    with open(infile) as f:
        engine = f.read().split()
        adj = searchAdjacents(engine)
        gears = defaultdict(list)
        for n,(g,X) in adj:
            if g=="*":
                gears[X].append(n)
        return sum([ v[0]*v[1] for X,v in gears.items() if len(v)==2 ])

print("Part 2:",part2("input.txt"))

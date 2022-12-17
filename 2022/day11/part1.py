class Monkey:
    def __init__(self, inv, op, v, test, t, f):
        self.inv = inv
        self.op = op
        self.v = v
        self.test = test
        self.t = t
        self.f = f
        self.inspected = 0


monkeys = [
    Monkey([92, 73, 86, 83, 65, 51, 55, 93], "*", 5, 11, 3, 4),
    Monkey([99, 67, 62, 61, 59, 98], "*", "o", 2, 6, 7),
    Monkey([81, 89, 56, 61, 99], "*", 7, 5, 1, 5),
    Monkey([97, 74, 68], "+", 1, 17, 2, 5),
    Monkey([78, 73], "+", 3, 19, 2, 3),
    Monkey([50], "+", 5, 7, 1, 6),
    Monkey([95, 88, 53, 75], "+", 8, 3, 0, 7),
    Monkey([50, 77, 98, 85, 94, 56, 89], "+", 2, 13, 4, 0)
]

for _ in range(20):
    for m in monkeys:
        for x in range(len(m.inv)):
            item = m.inv[0]
            if m.v == "o":
                v = item
            else:
                v = m.v
            m.inv[0] = (eval(str(item)+m.op+str(v)) // 3)
            if m.inv[0]%m.test == 0:
                monkeys[m.t].inv.append(m.inv.pop(0))
            else:
                monkeys[m.f].inv.append(m.inv.pop(0))
            m.inspected += 1
counts = [x.inspected for x in monkeys]
counts.sort(reverse=True)
print(counts[0]*counts[1])
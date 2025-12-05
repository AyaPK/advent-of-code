from bisect import bisect_right

inp = [l.strip() for l in open("input.txt")]
split = inp.index("")

ranges = sorted(tuple(map(int, r.split("-"))) for r in inp[:split])

merged = []
for s, e in ranges:
    if merged and s <= merged[-1][1] + 1:
        a, b = merged[-1]
        merged[-1] = (a, e if e > b else b)
    else:
        merged.append((s, e))

starts = [s for s, _ in merged]
ids = [int(x) for x in inp[split+1:] if x]

def fresh(x):
    i = bisect_right(starts, x) - 1
    return i >= 0 and merged[i][0] <= x <= merged[i][1]

print(sum(fresh(x) for x in ids))
print(sum(e - s + 1 for s, e in merged))

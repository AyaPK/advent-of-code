data = [int(x.replace("\n", "")) for x in open("input.txt", "r")]
data = sorted(data) + [max(data) + 3]

diffs = [b - a for a, b in zip([0] + data, data)]
print(diffs.count(1) * diffs.count(3))


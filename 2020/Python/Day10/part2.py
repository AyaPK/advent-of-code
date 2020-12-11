from collections import Counter

data = [int(x.replace("\n", "")) for x in open("input.txt")]
data = [0]+sorted(data)
counter = Counter({0: 1})

for x in data:
    i = x
    c1 = counter[x+1]
    c2 = counter[x+2]
    c3 = counter[x+3]
    cx = counter[x]
    counter[x+1] += counter[x]
    counter[x+2] += counter[x]
    counter[x+3] += counter[x]

print(counter[max(data)+3])


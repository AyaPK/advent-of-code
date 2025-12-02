ranges = [x.strip() for x in open("input.txt").readlines()[0].split(",")]

count  = 0
for r in ranges:
    lower = r.split("-")[0]
    upper = r.split("-")[1]
    for x in range(int(lower), int(upper) + 1):
        s = str(x)
        mid = len(s) // 2

        left = s[:mid]
        right = s[mid:]

        if left == right:
            count += x
print(count)

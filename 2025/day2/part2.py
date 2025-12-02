ranges = [x.strip() for x in open("input.txt").readlines()[0].split(",")]

def is_repeated_pattern(s: str) -> bool:
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            base = s[:i]
            if base * (n // i) == s:
                return True
    return False

count = 0
for r in ranges:
    lower, upper = r.split("-")
    for x in range(int(lower), int(upper) + 1):
        if is_repeated_pattern(str(x)):
            count += x

print(count)

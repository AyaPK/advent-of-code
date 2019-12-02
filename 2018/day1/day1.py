arr = []
output = 0
found = False
results = [0]
checks = 0

def calc(a, b):
    global output
    global found
    global checks
    if a == "+":
        output = output + b
    else:
        output = output - b

    if output in results:
        print(f"found {output}")
        found = True

    results.append(output)


with open("input.txt", "r") as f:
    data = f.readlines()
    for x in data:
        arr.append(x.replace("\n", ""))

while not found:
    for x in arr:
        calc(x[0], int(x[1:]))
    checks += 1
    if checks % 25 == 0:
        print(results)
    print(checks)

print(output)
print(results)
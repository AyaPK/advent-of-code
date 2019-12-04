pwlist = set()
ascension = []
for x in range(359282, 820401):
    pwlist.add(str(x))

for pas in pwlist:
    checkdec = True
    doublecheck = False
    doubles = []
    for x in range(1, 6, 1):
        if pas[x-1] > pas[x]:
            checkdec = False
            break
        if pas[x-1] == pas[x]:
            doublecheck = True
            doubles.append(pas[x])
    tripcheck = False
    for x in doubles:
        if doubles.count(x) == 1:
            tripcheck = True
    if checkdec and doublecheck and tripcheck:
        ascension.append(pas)
print((ascension))
print(len(ascension))

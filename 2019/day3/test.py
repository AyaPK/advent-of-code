tup1 = [[1, 2], [3, 4]]
tup2 = [[1, 4], [1, 2]]

for a in tup1:
    for b in tup2:
        if a == b:
            print("yes")
        else:
            print("no")
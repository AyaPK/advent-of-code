import itertools
import cProfile
def myFunc():
    data = open("input.txt", "r").readlines()
    for x in range(len(data)):
        data[x] = int(data[x])
    triplets = itertools.combinations(data, 3)
    for t in triplets:
        if sum(t) == 2020:
            print(t[0]*t[1]*t[2])
cProfile.run('myFunc()')
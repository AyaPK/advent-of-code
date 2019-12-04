# a more compact way to do task 1 of day 1

import math
with open("input.txt", "r") as f:
    print(sum((math.floor(int(module)/3))-2 for module in f.readlines()))


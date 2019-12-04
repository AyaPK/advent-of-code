# a more compact way to do task 1 of day 1
import math

def calc(fuel):
    output = 0
    while fuel > 0:
        fuel = (math.floor(fuel/3))-2
        output = output+fuel
    return output

with open("input.txt", "r") as f:
    print(sum(calc(int(module)) for module in f.readlines()))
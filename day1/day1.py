import math
inputs = []
outputs = []

def calc(arg1):
    temparray = []
    fuel = arg1
    while fuel > 0:
        fuel = (math.floor(fuel/3))-2
        if fuel > 0:
            temparray.append(fuel)
    return sum(temparray)

with open("input.txt", "r") as f:
    input = f.readlines()
    for x in input:
        out = x.replace("\n", "")
        inputs.append(out)

for x in inputs:
    outputs.append(calc(int(x)))

print(sum(outputs))
data = [x.replace("\n", "") for x in open("input.txt", "r").readlines()]

arrival = int(data[0])
buses = [int(x) for x in data[1].split(",") if x != "x"]
times = {}
for bus in buses:
    time = int(bus)
    while time < arrival:
        time += bus
    times[bus] = time

lowestid = buses[0]
lowesttime = times[buses[0]]

for id in buses:
    if times[id] < lowesttime:
        lowesttime = times[id]
        lowestid = id

print(lowestid*(lowesttime-arrival))
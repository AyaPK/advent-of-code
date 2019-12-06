with open("input.txt", "r") as f:
    planetlist = {planet[4:7]: planet[:3] for planet in f.readlines()}
    orbitcount = 0

for planet in planetlist:
    while planet != "COM":
        orbitcount += 1
        planet = planetlist[planet]

print(orbitcount)
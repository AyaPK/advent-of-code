from itertools import permutations

inp = [x.strip() for x in open("input.txt", "r").readlines()]

locations = set()
distances = {}
loc_perms = list()
routes = []

def process_input(lst):
    global loc_perms
    for distance in lst:
        loc1 = distance.split(" ")[0]
        loc2 = distance.split(" ")[2]
        d = distance.split(" ")[4]

        locations.add(loc1)
        locations.add(loc2)

        if loc1 not in distances:
            distances[loc1] = {}
        distances[loc1][loc2] = d
        if loc2 not in distances:
            distances[loc2] = {}
        distances[loc2][loc1] = int(d)
    loc_perms = list(permutations(locations))

process_input(inp)

for route in loc_perms:
    length = 0
    for i, loc in enumerate(route):
        try:
            length += int(distances[route[i]][route[i+1]])
        except IndexError:
            continue
    routes.append(length)
print(f"shortest trip: {min(routes)}")
print(f"longest trip: {max(routes)}")
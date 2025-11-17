paths = [x.strip() for x in open("input.txt").readlines()]
from collections import defaultdict

graph = defaultdict(list)
for path in paths:
    a, b = path.split("-")
    graph[a].append(b)
    graph[b].append(a)

def is_small_cave(cave):
    return cave.islower()

def dfs(cave, visited):
    if cave == "end":
        return 1
    count = 0
    for neighbor in graph[cave]:
        if is_small_cave(neighbor) and neighbor in visited:
            continue
        new_visited = visited.copy()
        if is_small_cave(neighbor):
            new_visited.add(neighbor)
        count += dfs(neighbor, new_visited)
    return count

result = dfs("start", {"start"})
print(result)
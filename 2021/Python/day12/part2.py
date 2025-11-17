paths = [x.strip() for x in open("input.txt").readlines()]
from collections import defaultdict

graph = defaultdict(list)
for path in paths:
    a, b = path.split("-")
    graph[a].append(b)
    graph[b].append(a)

def is_small_cave(cave):
    return cave.islower()

def dfs(cave, visited, small_cave_visited_twice=False):
    if cave == "end":
        return 1
    total_paths = 0
    for neighbor in graph[cave]:
        if neighbor == "start":
            continue
        if is_small_cave(neighbor):
            if neighbor in visited:
                if not small_cave_visited_twice:
                    total_paths += dfs(neighbor, visited, True)
            else:
                total_paths += dfs(neighbor, visited | {neighbor}, small_cave_visited_twice)
        else:
            total_paths += dfs(neighbor, visited, small_cave_visited_twice)
    return total_paths

result = dfs("start", {"start"})
print(result)


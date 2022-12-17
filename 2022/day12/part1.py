from collections import deque
import string

# I had to go to reddit for inspiration on this one, it was getting late and I was tired
def search(graph, start):
    w = len(graph[0])
    h = len(graph)
    queue = deque([[start]])
    visited = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if graph[y][x] == "E":
            return path
        e_index = string.ascii_lowercase.index(graph[y][x])
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < w and 0 <= y2 < h and (x2, y2) not in visited:
                e_index_2 = string.ascii_lowercase.index(graph[y2][x2]) if graph[y2][x2] != "E" else 26
                if e_index_2 <= e_index + 1:
                    queue.append(path + [(x2, y2)])
                    visited.add((x2, y2))

data = open("input.txt").read().strip()
graph = [[c for c in line] for line in data.split("\n")]
y, x = [(n, r.index("S")) for n, r in enumerate(graph) if "S" in r][0]
y2, x2 = [(n, r.index("E")) for n, r in enumerate(graph) if "E" in r][0]
graph[y][x] = "a"
print(f"Part 1: {len(search(graph, (x, y))) - 1}")
starts = [(c, r) for r in range(len(graph)) for c in range(len(graph[0])) if graph[r][c] == "a"]
p2 = [len(search(graph, pos)) - 1 for pos in starts if search(graph, pos)]
print(f"Part 2: {min(p2)}")
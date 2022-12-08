import numpy as np

data = [x.strip() for x in open("input.txt").readlines()]
data = np.array([[int(x) for x in y] for y in data])


def check_left(tree_y, tree_x):
    tree = data[tree_y, tree_x]
    seen = 0
    for x in range(tree_x - 1, -1, -1):
        if data[tree_y][x] >= tree:
            seen += 1
            return seen
        seen += 1
    return seen

def check_right(tree_y, tree_x):
    tree = data[tree_y, tree_x]
    seen = 0
    for x in range(tree_x + 1, len(data[0])):
        try:
            if data[tree_y][x] >= tree:
                seen += 1
                return seen
        except:
            return seen
        seen += 1
    return seen

def check_up(tree_y, tree_x):
    tree = data[tree_y, tree_x]
    seen = 0
    for y in range(tree_y - 1, -1, -1):
        if data[y][tree_x] >= tree:
            seen += 1
            return seen
        seen += 1
    return seen

def check_down(tree_y, tree_x):
    tree = data[tree_y, tree_x]
    seen = 0
    for y in range(tree_y + 1, len(data)):
        if data[y][tree_x] >= tree:
            seen += 1
            return seen
        seen += 1
    return seen

def check_trees(tree_y, tree_x):
    scenic_score = np.prod([check_left(tree_y, tree_x), check_right(tree_y, tree_x),
                            check_up(tree_y, tree_x), check_down(tree_y, tree_x)])
    return scenic_score

score = 0
for y in range(1, len(data)-1):
    for x in range(1, len(data[0])-1):
        scenic = check_trees(y, x)
        if scenic > score:
            score = scenic
print(score)


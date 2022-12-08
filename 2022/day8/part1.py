import numpy as np

data = [x.strip() for x in open("input.txt").readlines()]
data = np.array([[int(x) for x in y] for y in data])

def check_left(tree_y, tree_x):
    tree = data[tree_y, tree_x]
    for x in range(tree_x):
        if data[tree_y][x] >= tree:
            return False
    return True

def check_right(tree_y, tree_x):
    tree = data[tree_y, tree_x]
    for x in range(len(data[0])-1, tree_x, -1):
        if data[tree_y][x] >= tree:
            return False
    return True

def check_top(tree_y, tree_x):
    tree = data[tree_y, tree_x]
    for y in range(tree_y):
        if data[y][tree_x] >= tree:
            return False
    return True

def check_bottom(tree_y, tree_x):
    tree = data[tree_y, tree_x]
    for y in range(len(data)-1, tree_y, -1):
        if data[y][tree_x] >= tree:
            return False
    return True

def is_visible(tree_y, tree_x):
    tree = data[tree_y, tree_x]

    visible = sum(1 for x in [check_left(tree_y, tree_x),
                              check_right(tree_y, tree_x),
                              check_top(tree_y, tree_x),
                              check_bottom(tree_y, tree_x)] if x)

    return visible > 0

visible = (len(data)*2) + (len(data[0])*2) - 4
for y in range(1, len(data)-1):
    for x in range(1, len(data[0])-1):
        if is_visible(y, x):
            visible += 1

print(visible)



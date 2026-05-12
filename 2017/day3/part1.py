"""
You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward
For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1
(the location of the only access port for this memory system) by programs that can only move up, down, left, or right
They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

Your puzzle input is 265149.
"""

from math import ceil, sqrt
from collections import defaultdict


def spiral_distance(n):
    if n == 1:
        return 0

    k = ceil((sqrt(n) - 1) / 2)
    side = 2 * k
    max_val = (2 * k + 1) ** 2
    mids = [max_val - k - side * i for i in range(4)]
    return k + min(abs(n - m) for m in mids)

def stress_spiral(limit):
    grid = defaultdict(int)
    x = y = 0
    grid[(0,0)] = 1

    directions = [(1,0), (0,-1), (-1,0), (0,1)]
    step = 1

    while True:
        for d in range(4):
            dx, dy = directions[d]

            for _ in range(step):
                x += dx
                y += dy

                val = sum(
                    grid[(x+i, y+j)]
                    for i in (-1,0,1)
                    for j in (-1,0,1)
                    if (i,j) != (0,0)
                )

                grid[(x,y)] = val

                if val > limit:
                    return val

            if d % 2 == 1:
                step += 1

print(spiral_distance(265149))
print(stress_spiral(265149))
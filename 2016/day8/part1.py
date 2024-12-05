import re
import numpy as np

def show(grid):
    for row in grid:
        print(''.join('X' if cell else ' ' for cell in row))

def process_grid(width, height, instructions):
    grid = np.zeros((height, width), dtype=bool)
    for instruction in instructions:
        parts = re.split(r'[ =]', instruction)
        if parts[0] == 'rect':
            cols, rows = map(int, parts[1].split('x'))
            grid[:rows, :cols] = True
        elif parts[0] == 'rotate':
            index, shift = int(parts[3]), int(parts[5])
            if parts[1] == 'row':
                grid[index] = np.roll(grid[index], shift)
            elif parts[1] == 'column':
                grid[:, index] = np.roll(grid[:, index], shift)
    return grid

with open('input.txt') as file:
    instructions = file.read().splitlines()

result_grid = process_grid(50, 6, instructions)
print('Answer #1:', np.sum(result_grid))
print('Answer #2:')
show(result_grid)

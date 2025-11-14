grid = [[x for x in line.strip()] for line in open("input.txt").readlines()]
print(grid)

class Octopus:
    def __init__(self, energy: int) -> None:
        self.energy = energy
        self.flashed = False

    def step(self):
        self.energy += 1
        if self.energy > 9 and not self.flashed:
            self.flashed = True
            return True
        return False

    def reset(self):
        if self.flashed:
            self.energy = 0
            self.flashed = False

    def __str__(self) -> str:
        return str(self.energy)

octopuses = [[Octopus(int(energy)) for energy in line] for line in grid]
total_flashes = 0
step = -1
while True:
    step += 1
    for row in octopuses:
        for octopus in row:
            octopus.energy += 1

    flash_occurred = True
    while flash_occurred:
        flash_occurred = False
        for i in range(len(octopuses)):
            for j in range(len(octopuses[i])):
                octopus = octopuses[i][j]
                if octopus.energy > 9 and not octopus.flashed:
                    octopus.flashed = True
                    flash_occurred = True
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if di == 0 and dj == 0:
                                continue
                            ni, nj = i + di, j + dj
                            if 0 <= ni < len(octopuses) and 0 <= nj < len(octopuses[i]):
                                octopuses[ni][nj].energy += 1
    for row in octopuses:
        for octopus in row:
            if octopus.flashed:
                total_flashes += 1
                octopus.energy = 0
                octopus.flashed = False

    if all(octopus.energy == 0 for row in octopuses for octopus in row):
        print(f"All octopuses flashed simultaneously on step {step + 1}")
        break



print(f"Total flashes after 100 steps: {total_flashes}")

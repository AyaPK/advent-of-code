from enum import Enum

data = [x.strip() for x in open("input.txt").readlines()]

cycle_row = {}

class State(Enum):
    IDLE = 1,
    ADDING = 2


state = State.IDLE
cycle = 1
index = 0
x = 1
interesting = []
screen = [["."] * 40,
          ["."] * 40,
          ["."] * 40,
          ["."] * 40,
          ["."] * 40,
          ["."] * 40]


def draw():
    if cycle <= 40:
        row = 0
    elif cycle <= 80:
        row = 1
    elif cycle <= 120:
        row = 2
    elif cycle <= 160:
        row = 3
    elif cycle <= 200:
        row = 4
    elif cycle <= 240:
        row = 5
    else:
        row = 6

    if row < 6:
        _ = abs(x-((cycle-1)-(row*40)))
        if abs(x-((cycle-1)-(row*40))) <= 1:
            y = cycle-1-(row*40)
            screen[row][cycle-1-(row*40)] = "#"

while True:
    try:
        if state == State.IDLE:
            action = data[index]
            if "noop" in action:
                state = State.IDLE
                index += 1
                draw()
                cycle += 1
            else:
                state = State.ADDING
                draw()
                cycle += 1

        elif state == State.ADDING:
            value = int(data[index].split(" ")[1])
            draw()
            x += value
            cycle += 1
            index += 1
            state = State.IDLE
    except:
        break

for row in screen:
    print("".join(row))

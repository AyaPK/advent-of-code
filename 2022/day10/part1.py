from enum import Enum

data = [x.strip() for x in open("input.txt").readlines()]


class State(Enum):
    IDLE = 1,
    ADDING = 2


state = State.IDLE
cycle = 1
index = 0
x = 1
interesting = []

while True:
    try:
        if state == State.IDLE:
            action = data[index]
            if "noop" in action:
                state = State.IDLE
                index += 1
                cycle += 1
            else:
                state = State.ADDING
                cycle += 1

        elif state == State.ADDING:
            value = int(data[index].split(" ")[1])
            x += value
            cycle += 1
            index += 1
            state = State.IDLE

        if cycle in [20, 60, 100, 140, 180, 220]:
            interesting.append(cycle*x)
    except:
        break

print(sum(interesting))



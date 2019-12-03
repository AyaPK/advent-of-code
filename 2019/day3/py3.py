with open("input.txt", "r") as f:
    def follow():
        start = [0, 0]

        for move in f.readline().split(","):
            instruction = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1)}[move[0]]

            for _ in range(int(move[1:])):
                start[instruction[0]] += instruction[1]
                yield tuple(start)

    plotted = set(follow())
    closest = min(abs(x[0]) + abs(x[1]) for x in follow() if x in plotted)

    print(closest)

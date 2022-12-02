data = [x.strip() for x in open("input.txt", "r").readlines()]
scores = {"R": 1, "P": 2, "S": 3}
points = {"Win": 6, "Draw": 3, "Lose": 0}
actions = {"X": "Lose", "Y": "Draw", "Z": "Win"}
outcomes = {
    "A": {
        "Draw": "R",
        "Win": "P",
        "Lose": "S"
    },
    "B": {
        "Lose": "R",
        "Draw": "P",
        "Win": "S"
    },
    "C": {
        "Win": "R",
        "Lose": "P",
        "Draw": "S",
    }
}
print(sum(points[actions[player]] + scores[outcomes[elf][actions[player]]] for elf, player in [turn.split(" ") for turn in data]))

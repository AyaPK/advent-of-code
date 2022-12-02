data = [x.strip() for x in open("input.txt", "r").readlines()]
scores = {"X": 1, "Y": 2, "Z": 3}
points = {"Win":6, "Draw":3,"Lose":0}
outcomes = {
    "A": {
        "X": "Draw",
        "Y": "Win",
        "Z": "Lose"
    },
    "B": {
        "X": "Lose",
        "Y": "Draw",
        "Z": "Win"
    },
    "C": {
        "X": "Win",
        "Y": "Lose",
        "Z": "Draw",
    }
}
score = sum(points[outcomes[elf][player]]+scores[player] for elf, player in [turn.split(" ") for turn in data])
print(score)
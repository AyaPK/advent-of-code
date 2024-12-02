games = [x.strip() for x in open("input.txt").readlines()]
possible_games = []
colours = {"red": 12, "green": 13, "blue": 14}
for game in games:
    id = int(game.split(":")[0].strip().replace("Game ", "").strip())
    game = game.split(":")[1].strip()
    hands = game.split(";")
    possible = True
    for hand in hands:
        hand = hand.strip()
        things = hand.split(",")
        for thing in things:
            colour = thing.strip().split(" ")[1]
            if int(thing.strip().split(" ")[0]) > colours[colour]:
                possible = False
    if possible:
        possible_games.append(id)
print(sum(possible_games))
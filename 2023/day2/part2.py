games = [x.strip() for x in open("input.txt").readlines()]
powers = []
colours = {"red": 12, "green": 13, "blue": 14}
for game in games:
    lowest_colours = {}
    id = int(game.split(":")[0].strip().replace("Game ", "").strip())
    game = game.split(":")[1].strip()
    hands = game.split(";")
    for hand in hands:
        hand = hand.strip()
        things = hand.split(",")
        for thing in things:
            colour = thing.strip().split(" ")[1]
            num = int(thing.strip().split(" ")[0])
            if colour in lowest_colours:
                if lowest_colours[colour] < num:
                    lowest_colours[colour] = num
            else:
                lowest_colours[colour] = num
    powers.append(lowest_colours["red"]*lowest_colours["blue"]*lowest_colours["green"])

print(sum(powers))
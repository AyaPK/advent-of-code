data = open("input.txt", "r").readlines()
for item_one in data:
    for item_two in data:
        if item_one != item_two and int(item_one) + int(item_two) == 2020:
            print(int(item_one) * int(item_two))

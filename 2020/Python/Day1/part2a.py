
import cProfile
def myFunc():
    data = open("input.txt", "r").readlines()
    found = False
    for item_one in data:
        if not found:
            for item_two in data:
                if not found:
                    for item_three in data:
                        if (item_one != item_two != item_three) and int(item_one) + int(item_two) + int(item_three) == 2020 and not found:
                            print(int(item_one) * int(item_two) * int(item_three))
                            found = True
cProfile.run('myFunc()')
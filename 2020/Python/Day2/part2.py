def myFun():
    data = open("input.txt", "r").readlines()
    data = [x.replace("\n", "") for x in data]

    count = 0

    for p in data:
        lower = int(p.split(" ")[0].split("-")[0])
        upper = int(p.split(" ")[0].split("-")[1])
        char = p.split(" ")[1].replace(":", "")
        word = p.split(" ")[2]

        if (word[lower-1] == char) != (word[upper-1] == char):
            count += 1

    print(count)


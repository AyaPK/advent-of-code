import cProfile

def myFun():
    data = open("input.txt", "r").readlines()
    data = [x.replace("\n", "") for x in data]

    count = 0

    for p in data:
        lower = int(p.split(" ")[0].split("-")[0])
        upper = int(p.split(" ")[0].split("-")[1])
        char = p.split(" ")[1].replace(":", "")
        word = p.split(" ")[2]

        if (word.count(char) >= lower and word.count(char) <= upper):
            count += 1

    print(count)

print(cProfile.run("myFun()"))
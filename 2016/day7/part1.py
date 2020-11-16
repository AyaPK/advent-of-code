
with open("input.txt", "r") as f:
    data = f.readlines()

count = 0
foundIP = []
minus = 0

def checkForAbba(string):
    for x in range(0, len(string)-3):
        test = string[x:x+4]
        if len(set(test)) == 2 and test == test[::-1]:
            print(test)
            return True
    return False

stringpos = 0
for line in data:
    strings = []
    hypernets = []
    toadd = ""
    mode = "string"
    line = line.replace("\n","")
    line = line+"["
    for letter in line:
        if letter not in "[]\n":
            toadd = toadd+letter
        else:
            if mode == "string":
                strings.append(toadd)
                mode = "hypernets"
                toadd = ""
            else:
                hypernets.append(toadd)
                mode = "string"
                toadd = ""
    found = False
    for string in strings:
        if checkForAbba(string) and not found:
            for hypernet in hypernets:
                if not checkForAbba(hypernet) and not found:
                    count += 1
                    found = True
                    foundIP.append(line)
                    print(hypernets)
                    break
                else:
                    minus += 1
                    break
            break

print(count-minus)
# for i in foundIP:
#     print(i)
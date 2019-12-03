indexes = []


def parse(input):
    parsed = 0
    global output
    output = input
    notfound = True
    while notfound:
        for letter in range(0, len(output) - 1):
            notfound = False
            let = output[letter]
            if let.isupper():
                if output[letter + 1] == let.lower():
                    output = output[0:letter] + output[letter + 2:]
                    notfound = True
                    parsed += 1
                    break
            if let.islower():
                if output[letter + 1] == let.upper():
                    output = f"{output[0:letter]}{output[letter + 2:]}"
                    notfound = True
                    parsed += 1
                    break
        print(parsed, letter)
    print(output)
    print(len(output))


with open("input.txt", "r") as f:
    data = f.read()



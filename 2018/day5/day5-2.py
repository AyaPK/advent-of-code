indexes = []
arr = []
import string

def parse(input, rem1, rem2):
    parsed = 0
    global output
    output = input.replace(rem1, "")
    output = output.replace(rem2, "")
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
    print(output)
    print(len(output))
    arr.append([rem2, len(output)])

with open("input.txt", "r") as f:
    data = f.read()

for poly in string.ascii_lowercase:
    parse(data, poly, poly.upper())
    print(arr)
print(arr)
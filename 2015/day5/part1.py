def three_vowels(inp):
    return sum(1 for x in inp if x.lower() in "aeiou") >= 3

def no_bad_strings(inp):
    badstrings = ["ab", "cd", "pq", "xy"]
    for st in badstrings:
        if st in inp.lower():
            return False
    return True

def double_letter(inp):
    for x in range(len(inp)-1):
        if inp[x] == inp[x+1]:
            return True
    return False

def naughty_or_nice(inp):
    return three_vowels(inp) and no_bad_strings(inp) and double_letter(inp)

with open("input.txt", "r") as f:
    data = f.readlines()
    for x in range(len(data)):
        data[x] = data[x].replace("\n", "")
    print(sum(1 for x in data if naughty_or_nice(x)))
data = open("input.txt", "r").readlines()

"""Validates a passport to ensure it meets a criteria

:param p: A dictionary of key:value pairs to be validated
:returns: Boolean confirming the validity of the passport
"""
def check_passport(p):
    if len(p) < 7 or (len(p) == 7 and "cid" in p): return False
    if not 1920 <= int(p["byr"]) <= 2002: return False
    if not 2010 <= int(p["iyr"]) <= 2020: return False
    if not 2020 <= int(p["eyr"]) <= 2030: return False
    if "cm" in p["hgt"] or "in" in p["hgt"]:
        if "cm" in p["hgt"]:
            n = int(p["hgt"].replace("cm", ""))
            if not 150 <= n <= 193: return False
        elif "in" in p["hgt"]:
            n = int(p["hgt"].replace("in", ""))
            if not 59 <= n <= 76: return False
    if p["hcl"][0] == "#":
        for letter in p["hcl"].replace("#", ""):
            if letter not in "abcdefg" and not letter.isnumeric(): return False
    else: return False
    if not p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: return False
    if len(p["pid"]) == 9 and p["pid"].isnumeric():
        if int(p["pid"]) < 100000000:
            if p["pid"][0] != "0": return False
    else: return False
    return True

passports = []
passport = {}

for line in data:
    if line != "\n":
        for pair in line.split(" "):
            k = pair.split(":")[0]
            v = pair.split(":")[1].replace("\n", "")
            passport[k] = v
    else:
        passports.append(passport)
        passport = {}
passports.append(passport)
passport = {}

print(sum(1 for p in passports if check_passport(p)))
import hashlib

doorID = "reyedfim"
code = ["","","","","","","",""]
start = 0
found = 0
while "" in code:
    touse = str(start)
    toTest = doorID+str(start)
    hash = hashlib.md5(toTest.encode())
    out = hash.hexdigest()
    if out[:5] == "00000":
        try:
            if out[5].isnumeric() and code[int(out[5])] == "":
                code[int(out[5])] = str(out[6])
            else:
                start += 1
                continue
        except:
            start += 1
            continue
        found += 1
        print("Found digit")
        print(f"Currently found: {found}")
    start += 1
    if start%100000 == 0:
        print(start)
print("".join(code))
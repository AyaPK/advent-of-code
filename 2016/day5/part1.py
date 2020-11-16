import hashlib

doorID = "reyedfim"
code = ""
start = 0
while len(code) < 8:
    touse = str(start)
    toTest = doorID+str(start)
    hash = hashlib.md5(toTest.encode())
    out = hash.hexdigest()
    if out[:5] == "00000":
        code = code+out[5]
        print("Found digit")
        print(f"Currently found: {len(code)}")
    start += 1
    if start%100000 == 0:
        print(start)
print(code)
import hashlib

hashcode = "yzbqklnj"

def md5(x):
    return hashlib.md5(x).hexdigest()

x = 0
while True:
    test = hashcode+str(x)
    hashed = md5(test.encode())
    if hashed[0:5] == "00000":
        print("found")
        print(str(x))
        break
    else:
        x += 1
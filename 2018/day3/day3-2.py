from PIL import Image

array = []
redcount = 0

img = Image.new('RGB', (1000, 1000), color = 'white')
img.save('base.png')

map = img.load()
# map[2,2] = (0, 255, 0)

def image(x, y, xcount, ycount):
    for a in range(x, x+xcount):
        for b in range(y, y+ycount):
            if map[a, b] != (255, 255, 255):
                map[a, b] = (255, 0, 0)
            else:
                map[a, b] = (0, 255, 255)

def imagecheck(x, y, xcount, ycount, id):
    claimcheck = True
    for ach in range(x, x+xcount):
        for bch in range(y, y+ycount):
            if map[ach, bch] != (0, 255, 255):
                claimcheck = False
    if claimcheck:
        print("found", id)

with open("input.txt", "r") as f:
    data = f.readlines()
    for x in data:
        array.append(x.replace("\n", ""))

for str in array:
    xc = str.split(" ")[2].split(",")[0]
    yc = str.split(" ")[2].split(",")[1].replace(":","")
    xnum = str.split(" ")[3].split("x")[0]
    ynum = str.split(" ")[3].split("x")[1]
    image(int(xc), int(yc), int(xnum), int(ynum))

for a in range(0, 1000):
    for b in range(0, 1000):
        if map[a, b] == (255, 0, 0):
            redcount += 1

for strc in array:
    xc = strc.split(" ")[2].split(",")[0]
    yc = strc.split(" ")[2].split(",")[1].replace(":","")
    xnum = strc.split(" ")[3].split("x")[0]
    ynum = strc.split(" ")[3].split("x")[1]
    idch = strc.split(" ")[0]
    imagecheck(int(xc), int(yc), int(xnum), int(ynum), idch)

img.save('base.png')
print(redcount)
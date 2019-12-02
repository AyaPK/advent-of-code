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


with open("input.txt", "r") as f:
    data = f.readlines()
    for x in data:
        array.append(x.replace("\n", ""))

for str in array:
    xc = str.split(" ")[2].split(",")[0]
    yc = str.split(" ")[2].split(",")[1].replace(":","")
    xnum = str.split(" ")[3].split("x")[0]
    ynum = str.split(" ")[3].split("x")[1]
    print(xc)
    print(yc)
    print(xnum)
    print(ynum)
    image(int(xc), int(yc), int(xnum), int(ynum))

for a in range(0, 1000):
    for b in range(0, 1000):
        if map[a, b] == (255, 0, 0):
            redcount += 1


img.save('base.png')
print(redcount)
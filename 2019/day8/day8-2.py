from PIL import Image

with open("input.txt", "r") as f:
    inp = f.read()

dimenions = 25*6
count = len(inp)
layercount = int(count/dimenions)
pixelsperlayer = int(count/layercount)

pixels = inp
arr = []
while len(pixels) > 0:
    arr.append(pixels[0:150])
    pixels = pixels[150:]
zerocounts = (list(layer.count("0") for layer in arr))

x, y = 25, 6

img = Image.new("RGB",(x,y), color="Red")

map = img.load()

for layer in arr:
    counter = 0
    for a in range(0, y):
        for b in range(0, x):
            if map[b, a] == (255,0,0):
                if layer[counter] == "0":
                    map[b, a] = (0,0,0)
                elif layer[counter] == "1":
                    map[b, a] = (255, 255, 255)
            counter += 1

img.show()

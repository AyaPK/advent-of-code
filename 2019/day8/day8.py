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

for x in arr:
    if x.count("0") == min(zerocounts):
        print(x.count("1")*x.count("2"))

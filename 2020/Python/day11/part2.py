import sys
seats = [list(x.replace("\n", "")) for x in open("input.txt", "r").readlines()]

def count_seats(x, y):
    seat_area = []
    dirs = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]
    #Check up
    for dir in dirs:
        startx = int(x)
        starty = int(y)
        spotted = "."
        while spotted == ".":
            startx += dir[0]
            starty += dir[1]
            if starty >= 0 and startx >= 0 and startx < len(seats[0]) and starty < len(seats):
                spotted = seats[starty][startx]
            else:
                break
        seat_area.append(spotted)
    return [seat_area.count("L"), seat_area.count("#")]

rows = len(seats)
cols = len(seats[0])

changed = True
while changed:
    changed = False
    newmap = [x[:] for x in seats]


    for y in range(rows):
        for x in range(cols):
            try:
                seat = seats[y][x]
            except:
                print(x)
                print(y)
                sys.exit()
            if seat == "L":
                if count_seats(x, y)[1] == 0:
                    changed = True
                    newmap[y][x] = "#"
            elif seat == "#":
                if count_seats(x, y)[1] >= 5:
                    changed = True
                    newmap[y][x] = "L"
            elif seat == ".":
                pass
    seats = [x[:] for x in newmap]
print(sum(x.count("#") for x in seats))

count_seats(3,4)
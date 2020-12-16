import sys
seats = [list(x.replace("\n", "")) for x in open("input.txt", "r").readlines()]

def count_seats(x, y):
    seat_area = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                col = y+i
                row = x+j
                if col >= 0 and row >= 0 and col < len(seats) and row < len(seats[0]) and [i, j] != [0,0]:
                    seat_area.append(seats[col][row])
            except:
                pass
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
                if count_seats(x, y)[1] >= 4:
                    changed = True
                    newmap[y][x] = "L"
            elif seat == ".":
                pass
    seats = [x[:] for x in newmap]
print(sum(x.count("#") for x in seats))

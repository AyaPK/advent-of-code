instructions = [x.replace("\n", "") for x in open("input.txt", "r").readlines()]

rotater = {"N":"E", "E":"S", "S":"W", "W":"N"}
rotatel = {"N":"W", "E":"N", "S":"E", "W":"S"}

waypointx = 10
waypointy = 1

boatx = 0
boaty = 0

def move_to_waypoint():
    global boatx
    global boaty
    boatx += waypointx
    boaty += waypointy

def rotate_waypoint_right(n):
    global waypointx, waypointy
    n = int(n/90)
    for x in range(n):
        oldx = int(waypointx)
        oldy = int(waypointy)
        waypointy = -oldx
        waypointx = oldy

def rotate_waypoint_left(n):
    global waypointx, waypointy
    n = int(n / 90)
    for x in range(n):
        oldx = int(waypointx)
        oldy = int(waypointy)
        waypointy = oldx
        waypointx = -oldy

for row in instructions:
    instruction = row[0]
    number = int(row[1:])
    if instruction == "N":
        waypointy += number
    elif instruction == "S":
        waypointy -= number
    elif instruction == "E":
        waypointx += number
    elif instruction == "W":
        waypointx -= number
    elif instruction == "F":
        for x in range(number):
            move_to_waypoint()
    elif instruction == "R":
        rotate_waypoint_right(number)
    elif instruction == "L":
        rotate_waypoint_left(number)

print(abs(boatx)+abs(boaty))

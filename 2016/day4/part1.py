import collections

with open("input.txt", "r") as f:
    data = f.readlines()

real_room_sectors = []

for line in data:
    #seperate string in to parts: name, sector ID, checksum
    checksum = line.split("[")[1].replace("]", "").strip()
    sector_id = line.split("[")[0].split("-")[len(line.split("-"))-1]
    room_name = "".join(line.split("[")[0].split("-")[:len(line.split("-"))-1])

    #count the letters in the room name
    letters = {}
    room_name = sorted(room_name)
    for letter in room_name:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1

    #Sort counted dict
    letters = {k: v for k, v in sorted(letters.items(), key=lambda item: item[1], reverse=True)}

    #test checksum
    check = []
    for l in letters:
        check.append(l)
    check = "".join(check[:5])

    #if checksum passes, note sector ID

    if checksum == check:
        real_room_sectors.append(int(sector_id))


print(sum(real_room_sectors))
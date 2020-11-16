import collections
import string

with open("input.txt", "r") as f:
    data = f.readlines()

real_room_sectors = []
real_room_names = []

def shift(input, shift_count):
    letters = string.ascii_lowercase
    letter_loc = letters.index(input)
    letter_loc += shift_count
    while letter_loc > 25:
        letter_loc -= 26
    return letters[letter_loc]

for line in data:
    #seperate string in to parts: name, sector ID, checksum
    checksum = line.split("[")[1].replace("]", "").strip()
    sector_id = line.split("[")[0].split("-")[len(line.split("-"))-1]
    room__name = "".join(line.split("[")[0].split("-")[:len(line.split("-"))-1])

    #count the letters in the room name
    letters = {}
    room_name = sorted(room__name)
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
    check_passed = False
    if checksum == check:
        real_room_sectors.append(int(sector_id))
        check_passed = True

    if check_passed:
        unencrypted_name = ""
        for letters in room__name:
            unencrypted_name = unencrypted_name+shift(letters, int(sector_id))
        real_room_names.append(unencrypted_name)
print(real_room_sectors[real_room_names.index("northpoleobjectstorage")])
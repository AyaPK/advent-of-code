wordsearch = [x.strip() for x in open("input.txt").readlines()]
word = "XMAS"
hits = 0

def look_in_direction(length, x, y, dx, dy):
    found_word = []
    for i in range(length):
        if 0 <= y < len(wordsearch) and 0 <= x < len(wordsearch[0]):
            found_word.append(wordsearch[y][x])
        else:
            break
        x += dx
        y += dy
    return "".join(found_word) if len(found_word) == length else ""

DIRECTIONS = [
    (0, -1),  # Vertical up
    (1, 0),   # Horizontal right
    (1, 1),   # Diagonal down-right
    (1, -1),  # Diagonal up-right
]

hits = 0
for y, line in enumerate(wordsearch):
    for x, letter in enumerate(line):
        for dx, dy in DIRECTIONS:
            word_found = look_in_direction(len(word), x, y, dx, dy)
            if word_found == word or word_found[::-1] == word:
                hits += 1
print(hits)
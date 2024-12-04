wordsearch = [x.strip() for x in open("input.txt").readlines()]
hits = 0

def check_xmas(x, y):
    n = len(wordsearch)
    m = len(wordsearch[0])

    if not (0 <= y - 1 < n and 0 <= y + 1 < n and 0 <= x - 1 < m and 0 <= x + 1 < m):
        return 0

    top_left_diag = [wordsearch[y - 1][x - 1], wordsearch[y][x], wordsearch[y + 1][x + 1]]
    top_right_diag = [wordsearch[y - 1][x + 1], wordsearch[y][x], wordsearch[y + 1][x - 1]]

    valid_sequences = {"MAS", "SAM"}

    if "".join(top_left_diag) in valid_sequences and "".join(top_right_diag) in valid_sequences:
        return 1
    return 0

hits = 0
for y in range(len(wordsearch)):
    for x in range(len(wordsearch[0])):
        hits += check_xmas(x, y)

print(hits)

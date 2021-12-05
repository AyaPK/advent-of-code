win_conditions = [
    [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],
    [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4]],
    [[2, 0], [2, 1], [2, 2], [2, 3], [2, 4]],
    [[3, 0], [3, 1], [3, 2], [3, 3], [3, 4]],
    [[4, 0], [4, 1], [4, 2], [4, 3], [4, 4]],
    [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]],
    [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1]],
    [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2]],
    [[0, 3], [1, 3], [2, 3], [3, 3], [4, 3]],
    [[0, 4], [1, 4], [2, 4], [3, 4], [4, 4]],
]


class Board:
    def __init__(self):
        self.rows = []
        self.complete = False

    def add_row(self, numbers_to_add):
        self.rows.append(numbers_to_add.replace("  ", " ").split(" "))

    def mark_number(self, number_to_mark):
        for row in self.rows:
            for x in range(len(row)):
                if row[x] == number_to_mark:
                    row[x] = "x"

    def check_board(self):
        for con in win_conditions:
            bad_board = False
            for check in con:
                if self.rows[check[0]][check[1]] != "x":
                    bad_board = True
                    break
            if not bad_board:
                self.complete = True
                return True

    def calculate_score(self, multiplier):
        ints = []
        for row in self.rows:
            for n in row:
                if n != "x":
                    ints.append(int(n))
        return sum(ints)*int(multiplier)


    def show_board(self):
        print("------------------")
        for d in self.rows:
            print(" ".join(d))
        print("------------------")


data = [x.strip() for x in open("input.txt", "r").readlines()]
numbers = data[0].split(",")
data = data[2:]
boards = []
board = Board()
for d in data:
    if d != "":
        board.add_row(d)
    else:
        boards.append(board)
        board = Board()
boards.append(board)


winning_board = None
final_number = None
complete_boards = []
for number in numbers:
    for b in boards:
        if not b.complete:
            b.mark_number(number)
            if b.check_board():
                winning_board = b
                final_number = number
                complete_boards.append(b)
                pass

print(complete_boards[len(complete_boards)-1].calculate_score(final_number))
import array
import pawn
import tools


class Board:
    def __init__(self, n):
        self.n = n
        self.pawns = []
        self.board_init()
        self.pawn_init()

    def board_init(self):

        rows, cols = self.n, self.n

        for i in range(rows):
            col = []
            for j in range(cols):
                col.append(0)
            self.pawns.append(col)

    def pawn_init(self):

        rows, cols = self.n, self.n
        color = True

        for i in range(0, int((cols - 1) / 2) * 2 + 2, 2):
            p = pawn.Pawn(0, i, color)
            self.pawns[0][i] = p
        for i in range(1, int(cols / 2) * 2, 2):
            p = pawn.Pawn(1, i, color)
            self.pawns[1][i] = p

        color = False

        for i in range(tools.odd_even2(rows), int(cols / 2) * 2, 2):
            p = pawn.Pawn(rows - 2, i, color)
            self.pawns[rows - 2][i] = p
        for i in range(tools.odd_even1(rows), int((cols - 1) / 2) * 2 + 2, 2):
            p = pawn.Pawn(rows - 1, i, color)
            self.pawns[rows - 1][i] = p

    def print_board(self):
        board_str = ""
        for i in range(self.n):
            for j in range(self.n):
                p = self.pawns[i][j]
                if p != 0:
                    if p.color:
                        color = "White"
                    else:
                        color = "Black"
                else:
                    color = "----"

                # s = "(" + str(i + 1) + ", " + chr(j + 97) + ", " + color + ")\t\t"
                s = "(" + str(i) + ", " + str(j) + ", " + color + ")\t\t"

                board_str += s

            board_str += "\n"

        print(board_str)

    def get_color(self, row, col):
        p = self.pawns[row][col]
        if p != 0:
            return p.get_color()
        else:
            return -1

    def remove_pawn(self, row, col):
        self.pawns[row][col] = 0

    def move_pawn(self, row1, col1, row2, col2):

        p = self.pawns[row1][col1]
        if p.can_move(row2, col2):
            p.x = row2
            p.y = col2
            self.pawns[row1][col1] = 0
            self.pawns[row2][col2] = p
            return True

        else:
            print("move is wrong")
            return False

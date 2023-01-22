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

        for i in range(0, rows, 1):
            for j in range(tools.is_even(i), int(cols), 2):
                if i <= 3:
                    p = pawn.Pawn(i, j, True)
                    self.pawns[i][j] = p
                elif i >= (rows - 4):
                    p = pawn.Pawn(i, j, False)
                    self.pawns[i][j] = p

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

                s = "(" + str(i + 1) + ", " + chr(j + 97) + ", " + color + ")\t\t"
                # s = "(" + str(i) + ", " + str(j) + ", " + color + ")\t\t"

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
        if self.get_color(row2, col2) == -1 and p.can_move(row2, col2):
            p.x = row2
            p.y = col2
            self.pawns[row1][col1] = 0
            self.pawns[row2][col2] = p
            return True

        else:
            return False

    def can_eat(self, color, row, col):
        if color:
            row1 = row + 1
            row2 = row + 2
        else:
            row1 = row - 1
            row2 = row - 2

        col_izq = col - 1
        col_der = col + 1

        if self.eats(row1, col_izq, row2, col_izq - 1, self.get_color(row, col)):
            print("You must eat")
            return True
        elif self.eats(row1, col_der, row2, col_der + 1, self.get_color(row, col)):
            print("You must eat")
            return True
        else:
            return False

    def eats(self, row1, col1, row2, col2, color):
        if (0 <= row1 < self.n) and (0 <= col1 < self.n) and (0 <= row2 < self.n) and (0 <= col2 < self.n):
            if self.get_color(row1, col1) != -1:
                if (color != self.get_color(row1, col1)) and (self.get_color(row2, col2) == -1):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def eat_pawn(self, row, row1, row2, col, col1, col2):
        self.remove_pawn(row1, col1)
        self.move_pawn(row, col, row1, col1)
        self.move_pawn(row1, col1, row2, col2)

    def possibles_moves(self, color, row, col):

        if color:
            aux = 1
        else:
            aux = -1

        if 0 <= row + aux < self.n:
            if 0 <= col - 1 < self.n:
                if self.get_color(row + aux, col - 1) == -1:
                    return True

            if 0 <= col + 1 < self.n:
                if self.get_color(row + aux, col + 1) == -1:
                    return True
            return False

        else:
            return False

import board


class Game:
    def __init__(self):
        self.white = None
        self.black = None
        self.n = None
        self.board = None
        self.turn = True  # True is White and False is Black
        self.n_white = None
        self.n_black = None

    def start(self):
        self.white = input("Who is playing white?\n")
        self.black = input("Who is playing black?\n")
        self.n = int(input("Which is the board's size?\n"))
        self.board = board.Board(self.n)
        self.n_white = 2 * self.n
        self.n_black = 2 * self.n

    def try_to_make_move(self, row1, col1, row2, col2):
        pass

    def pick_pawn(self, row, col):
        if (0 <= row <= self.n) and (0 <= col <= self.n):
            if self.board.get_color(row, col) == -1:
                print("No pawn in there")
                return False
            elif self.board.get_color(row, col) != self.turn:
                print("Not your pawn")
                return False
            else:
                return True
        else:
            print("No pawn in there")
            return False

    def move_pawn(self, row1, col1):
        aux = True
        while aux:
            while True:
                    print("Where do you want to move? \n")
                    try:
                        row2 = int(input("Enter row: ")) - 1
                    except ValueError:
                        print("You must enter a valid row")
                        continue
                    try:
                        col2 = ord(input("Enter column: ")[0]) - 97
                    except IndexError:
                        print("You must enter a valid column")
                        continue
                    else:
                        break

            if (0 <= row2 <= self.n) and (0 <= col2 <= self.n):
                if self.board.move_pawn(row1, col1, row2, col2):
                    aux = False
                else:
                    print("Move is wrong")
            else:
                print("Move out of border")

    def eat_pawn(self, row, col):
        aux = True
        while aux:
            while True:
                    print("Which pawn do you want to eat? \n")
                    try:
                        row1 = int(input("Enter row: ")) - 1
                    except ValueError:
                        print("You must enter a valid row")
                        continue
                    try:
                        col1 = ord(input("Enter column: ")[0]) - 97
                    except IndexError:
                        print("You must enter a valid column")
                        continue
                    else:
                        break

            row2 = row1 + (row1 - row)
            col2 = col1 + (col1 - col)

            if self.board.eats(row1, col1, row2, col2, self.turn):
                self.board.eat_pawn(row, row1, row2, col, col1, col2)
                if self.turn == True:
                    self.n_white -= 1
                    if self.n_white == 0:
                        print("GAME OVER: WHITE PAWNS WIN")
                elif self.turn == False:
                    self.n_black -= 1
                    if self.n_black == 0:
                        print("GAME OVER: BLACK PAWNS WIN")
                aux = False
            else:
                print("You can't eat that pawn")

    def play_game(self):
        self.start()

        while True:

            aux = True
            self.board.print_board()

            if self.turn:
                print(self.white, "TURN\n")
            else:
                print(self.black, "TURN\n")

            while aux:
                while True:
                    print("Which pawn do you want to move? \n")
                    try:
                        row = int(input("Enter row: ")) - 1
                    except ValueError:
                        print("You must enter a valid row")
                        continue
                    try:
                        col = ord(input("Enter column: ")[0]) - 97
                    except IndexError:
                        print("You must enter a valid col")
                        continue
                    else:
                        break

                if self.pick_pawn(row, col):
                    if self.board.can_eat(self.turn, row, col):
                        self.eat_pawn(row, col)
                        aux = False
                    elif self.board.possibles_moves(self.turn, row, col):
                        self.move_pawn(row, col)
                        aux = False
                    else:
                        print("You can't move this pawn")
            if self.n_black == 0 or self.n_white == 0:
                break
            self.turn = not self.turn

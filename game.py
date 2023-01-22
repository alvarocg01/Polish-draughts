import board


class Game:
    def __init__(self):
        self.white = None
        self.black = None
        self.n = None
        self.board = None
        self.turn = True  # True is White and False is Black

    def start(self):
        self.white = input("Who is playing white?\n")
        self.black = input("Who is playing black?\n")
        self.n = int(input("Which is the board's size?\n"))
        self.board = board.Board(self.n)

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
            print("Where you want to move? \n")
            row2 = int(input("Enter row: ")) - 1
            col2 = ord(input("Enter column: ")[0]) - 97

            if (0 <= row2 <= self.n) and (0 <= col2 <= self.n):
                if self.board.move_pawn(row1, col1, row2, col2):
                    aux = False
                else:
                    print("move is wrong")
            else:
                print("Move out of border")

    def eat_pawn(self, row, col):
        aux = True
        while aux:
            print("Which pawn you want to eat? \n")
            row1 = int(input("Enter row: ")) - 1
            col1 = ord(input("Enter column: ")[0]) - 97

            row2 = row1 + (row1 - row)
            col2 = col1 + (col1 - col)

            if self.board.eats(row1, col1, row2, col2, self.turn):
                self.board.eat_pawn(row, row1, row2, col, col1, col2)
                aux = False
            else:
                print("you can't eat that pawn")

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
                print("Which pawn you want to move? \n")
                row = int(input("Enter row: ")) - 1
                col = ord(input("Enter column: ")[0]) - 97

                if self.pick_pawn(row, col):
                    if self.board.can_eat(self.turn, row, col):
                        self.eat_pawn(row, col)
                        aux = False
                    elif self.board.possibles_moves(self.turn, row, col):
                        self.move_pawn(row, col)
                        aux = False
                    else:
                        print("You can't move this pawn")

            self.turn = not self.turn

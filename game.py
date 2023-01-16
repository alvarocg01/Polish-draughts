import board


class Game:
    def __init__(self):
        self.white = None
        self.black = None
        self.n = None
        self.board = None
        self.turn = True  # True is White and False is Black

    def start(self):
        self.white = input("Who is playing white?")
        self.black = input("Who is playing black?")
        self.n = int(input("Which is the board's size?"))
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
            print("no pawn in there")
            return False

    def move_pawn(self, row1, col1, row2, col2):
        if (0 <= row2 <= self.n) and (0 <= col2 <= self.n):
            if self.board.move_pawn(row1, col1, row2, col2):
                return True
            else:
                return False
        else:
            print("move out of border")
            return False

    def play_game(self):
        self.start()

        while True:
            aux = True
            aux1 = True

            self.board.print_board()

            if self.turn:
                print(self.white, "turn")
            else:
                print(self.black, "turn")

            while aux:
                print("Which pawn you want to move?")
                row1 = int(input("Enter row")) - 1
                col1 = ord(input("Enter column")[0]) - 97
                if self.board.possibles_moves(self.turn, row1, col1) == False:
                    print("You cannot move this pawn")
                if self.pick_pawn(row1, col1):
                    aux = False

            while aux1:
                print("Where you want to move?")
                row2 = int(input("Enter row")) - 1
                col2 = ord(input("Enter column")[0]) - 97

                if self.move_pawn(row1, col1, row2, col2):
                    aux1 = False

            self.turn = not self.turn

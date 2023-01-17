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
                if(i <= 3):
                    p = pawn.Pawn(i, j, True)
                    self.pawns[i][j] = p
                elif(i >= (rows - 4)):
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
        if p.can_move(row2, col2):
            p.x = row2
            p.y = col2
            self.pawns[row1][col1] = 0
            self.pawns[row2][col2] = p
            return True

        else:
            print("move is wrong")
            return False

    def can_eat(self, row, col):
        p = self.pawns[row][col]
        row_up = row + 1
        row_down = row - 1
        col_izq = col - 1
        col_der = col + 1

        # caso arriba izquierda, compruebo primero si no se sale de los límites en diagonal tanto a la diagonal de la ficha que me quiero comer
        # como la casilla donde me quiero mover despues de comer
        if (0 <= row_up <= self.n) and (0 <= col_izq <= self.n) and (0 <= row_up + 1 <= self.n) and (0 <= col_izq - 1 <= self.n):
            p_izq = self.pawns[row_up][col_izq]
            if(p_izq != 0): #si en la casilla diagonal hay una ficha
                p_izq2 = self.pawns[row_up + 1][col_izq - 1]
                if(p.get_color() != p_izq.get_color()) and (p_izq2 == 0): #compruebo que sea de distinto color y que despues hay hueco para moverme
                    self.remove_pawn(row_up, col_izq) #elimino la ficha comida
                    self.move_pawn(row, col, row_up, col_izq) 
                    self.move_pawn(row_up, col_izq, row_up + 1, col_izq - 1) #muevo la ficha en dos llamadas ya que solo puedo avanzar de 1 en 1
                    return True
        #repito el proceso con la derecha
        elif(0 <= row_up <= self.n) and (0 <= col_der <= self.n) and (0 <= row_up + 1 <= self.n) and (0 <= col_der + 1 <= self.n):
            p_der = self.pawns[row_up][col_der]
            if(p_der != 0):
                p_der2 = self.pawns[row_up + 1][col_der + 1]
                if(p.get_color() != p_der.get_color()) and (p_der2 == 0): 
                    self.remove_pawn(row_up, col_der)
                    self.move_pawn(row, col, row_up, col_der) 
                    self.move_pawn(row_up, col_der, row_up + 1, col_der + 1) 
                    return True
        else: return False

    def possibles_moves(self, color, row, col):

        p_izq = -1
        p_der = -1

        # we checked their moves depends on its color

        if color == True:
            if col == 0: 
                p_der = self.pawns[row + 1][col + 1]
                if(p_der.get_color() == color):
                    return False
                else: return True
            elif col == self.n - 1:
                p_izq = self.pawns[row + 1][col - 1]
                if(p_izq.get_color() == color):
                    return False
                else: return True
            else:
                p_izq = self.pawns[row + 1][col - 1]
                p_der = self.pawns[row + 1][col + 1]
                if (color == p_der.get_color() and color == p_izq.get_color()):
                    return False
                else: return True

        if color == False:
            if col == 0: 
                p_der = self.pawns[row - 1][col + 1]
                if(p_der.get_color() == color):
                    return False
                else: return True
            elif col == self.n - 1:
                p_izq = self.pawns[row - 1][col - 1]
                if(p_izq.get_color() == color):
                    return False
                else: return True
            else:
                p_izq = self.pawns[row - 1][col - 1]
                p_der = self.pawns[row - 1][col + 1]
                if (color == p_der.get_color() and color == p_izq.get_color()):
                    return False
                else: return True
        
        
        


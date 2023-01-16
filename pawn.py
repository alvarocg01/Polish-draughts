class Pawn:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color  # True is White and False is Black

    def get_color(self):
        return self.color

    def can_move(self, x, y):
        if y == (self.y - 1) or y == (self.y + 1):
            if (self.color is True) and (x == (self.x + 1)):
                return True
            elif (self.color is False) and (x == (self.x - 1)):
                return True
        else:
            return False

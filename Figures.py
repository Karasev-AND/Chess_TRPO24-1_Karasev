
PAWN_MOVES = 'pawn_moves'
PAWN_TAKES = 'pawn_takes'


class Piece(object):
    """Basic class for chess pieces/figures initialisation"""
    def __init__(self, img, row, col, side, board):
        """initialisation of Piece with basic characteristics

        Args:
            img(str): a visual in console representation of object
            row(int): a first coordinate used for pieces to determine available moves
            col(int): a second coordinate used for pieces to determine available moves
            side(str): determines a player side of piece
            board(Board): a board object to check if move cell is available/empty

        Attributes:
            is_drop(bool): value that determines if figure is in game or not
            """
        self.img = img
        self.row = row
        self.col = col
        self.side = side
        self.board = board
        self.is_drop = False

    @staticmethod
    def is_vailid_pos(r, c):
        """Function that helps to determine Piece's position by cutting overstepping values

        Args:
            r(int): row coordinate of position
            c(int): column coordinate of position

        Return:
            return type - boolean True if position is available else False"""
        if 0 <= r <= 7 and 0 <= c <= 7:
            return True
        else:
            return False


class King(Piece):
    """Child Class for King Piece"""
    def __init__(self, img, row, col, side, board):
        """Refers to parential class Piece

         Attributes:
             moved(bool): parameter to check if castling is available
             """
        Piece.__init__(self, img, row, col, side, board)
        self.moved = False

    def __str__(self):
        """ 'Magic' method , represents piece on field
        Return:
            returns str value side + image of piece"""
        return self.side + self.img

    def get_moves(self):
        """function to determine available positions for piece

        Return:
            returns list of tuples with two integer coordinates in each tuple"""
        res = []
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1))

        for dir_row, dir_col in directions:
            r1 = dir_row + self.row
            c1 = dir_col + self.col
            if not self.is_vailid_pos(r1, c1):
                continue
            figure = self.board.get_figure(r1, c1)
            if figure is not None:
                if figure.side == self.side:
                    continue
            else:
                res.append((r1, c1))
        return res


class Queen(Piece):
    """Child Class for Queen Piece"""
    def __init__(self, img, row, col, side, board):
        """Refers to parential class Piece """
        Piece.__init__(self, img, row, col, side, board)

    def __str__(self):
        """ 'Magic' method , represents piece on field
        Return:
            returns str value side + image of piece"""
        return self.side + self.img

    def get_moves(self):
        """function to determine available positions for piece

        Return:
            returns list of tuples with two integer coordinates in each tuple"""
        res = []
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1))
        for dir_row, dir_col in directions:
            mul = 0
            while True:
                mul += 1
                r1 = self.row + mul * dir_row
                c1 = self.col + mul * dir_col
                if not self.is_vailid_pos(r1, c1):

                    break
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    if figure.side == self.side:
                        break
                res.append((r1, c1))
                if figure is not None:
                    break

        return res


class Rook(Piece):
    """Child Class for Rook Piece"""
    def __init__(self, img, row, col, side, board):
        """Refers to parential class Piece

        Attributes:
            moved(bool): parameter to check if castling is available
        """
        Piece.__init__(self, img, row, col, side, board)
        self.moved = False

    def __str__(self):
        """ 'Magic' method , represents piece on field
        Return:
            returns str value side + image of piece"""
        return self.side + self.img

    def get_moves(self):
        """function to determine available positions for piece

        Return:
            returns list of tuples with two integer coordinates in each tuple"""
        res = []
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        for dir_row, dir_col in directions:
            mul = 0
            while True:
                mul += 1
                r1 = self.row + mul * dir_row
                c1 = self.col + mul * dir_col
                if not self.is_vailid_pos(r1, c1):
                    break
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    if figure.side == self.side:
                        break
                res.append((r1, c1))
                if figure is not None:
                    break
        return res


class Bishop(Piece):
    """Child Class for Bishop Piece"""
    def __init__(self, img, row, col, side, board):
        """Refers to parential class Piece"""
        Piece.__init__(self, img, row, col, side, board)

    def __str__(self):
        """ 'Magic' method , represents piece on field
        Return:
            returns str value side + image of piece"""
        return self.side + self.img

    def get_moves(self):
        """function to determine available positions for piece

        Return:
            returns list of tuples with two integer coordinates in each tuple"""
        res = []
        directions = ((-1, 1), (1, 1), (1, -1), (-1, -1))

        for dir_row, dir_col in directions:
            mul = 0
            while True:
                mul += 1
                r1 = self.row + mul * dir_row
                c1 = self.col + mul * dir_col
                if not self.is_vailid_pos(r1, c1):
                    break
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    if figure.side == self.side:
                        break
                res.append((r1, c1))
                if figure is not None:
                    break

        return res


class Knight(Piece):
    """Child Class for Knight Piece"""
    def __init__(self, img, row, col, side, board):
        """Refers to parential class Piece"""
        Piece.__init__(self, img, row, col, side, board)

    def __str__(self):
        """ 'Magic' method , represents piece on field
        Return:
            returns str value side + image of piece"""
        return self.side + self.img

    def get_moves(self):
        """function to determine available positions for piece

        Return:
            returns list of tuples with two integer coordinates in each tuple"""
        res = []

        directions = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
        for dir_row, dir_col in directions:
            r1 = self.row + dir_row
            c1 = self.col + dir_col
            if not self.is_vailid_pos(r1, c1):
                continue
            figure = self.board.get_figure(r1, c1)
            if figure is not None:
                if figure.side == self.side:
                    continue
            res.append((r1, c1))
        return res


class Pawn(Piece):
    """Child Class for Pawn Piece"""
    def __init__(self, img, row, col, side, board):
        """Refers to parential class Piece
        
        Attributes:
            direction(int): direction of pawns movement """
        Piece.__init__(self, img, row, col, side, board)

        self.direction = {'w': 1, 'b': -1}[self.side]
        """
        if self.side == 'w':
            self.direction = 1
        if self.row == 'b':
            self.direction = -1
"""
    def __str__(self):
        """ 'Magic' method , represents piece on field
        Return:
            returns str value side + image of piece"""
        return self.side + self.img

    def get_moves(self, *args):
        """function to determine available positions for piece

        Args:
            *args(str):optional value that receives two special markers PAWN_MOVES/TAKES
            to determine possible moves

        Return:
            returns list of tuples with two integer coordinates in each tuple"""
        result = []

        if PAWN_MOVES in args or not args:

            r1 = self.row + self.direction
            c = self.col
            if self.is_vailid_pos(r1, c):
                if self.board.get_figure(r1, c) is None:
                    result.append((r1, c))

            if self.row == 1 or self.row == 6:
                r2 = self.row + 2 * self.direction
                if self.is_vailid_pos(r2, c):
                    if self.board.get_figure(r1, c) is None and self.board.get_figure(r2, c) is None:
                        result.append((r2, c))

        if PAWN_TAKES in args or not args:
            offsets = (-1, 1)
            r1 = self.row + self.direction
            for offset in offsets:
                c1 = self.col + offset
                if not self.is_vailid_pos(r1, c1):
                    continue
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    if figure.side == self.side:
                        continue
                    result.append((r1, c1))

        return result


class Xman(Piece):
    """Child Class for Xman Piece"""
    def __init__(self, img, row, col, side, board):
        """Refers to parential class Piece"""
        Piece.__init__(self, img, row, col, side, board)

    def __str__(self):
        """ 'Magic' method , represents piece on field
        Return:
            returns str value side + image of piece"""
        return self.side + self.img

    def get_moves(self):
        """function to determine available positions for piece

        Return:
            returns list of tuples with two integer coordinates in each tuple"""
        res = []
        directions = ((-1, 1), (1, 1), (1, -1), (-1, -1))

        for dir_row, dir_col in directions:
            for mul in range(1, 4):
                r1 = self.row + mul * dir_row
                c1 = self.col + mul * dir_col
                if not self.is_vailid_pos(r1, c1):
                    break
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    if figure.side == self.side:
                        break
                res.append((r1, c1))
                if figure is not None:
                    break

        return res


class Missile(Piece):
    """Child Class for Missile Piece"""
    def __init__(self, img, row, col, side, board):
        """Refers to parential class Piece
        
        Attributes:
             moved(bool): indicates if figure is able to move forward again on long distance
             direction(int): direction of missile blast
             """
        Piece.__init__(self, img, row, col, side, board)
        self.moved = False

        if self.row == 1:
            self.direction = 1
        if self.row == 6:
            self.direction = -1

    def __str__(self):
        """ 'Magic' method , represents piece on field
        Return:
            returns str value side + image of piece"""
        return self.side + self.img

    def get_moves(self):
        """function to determine available positions for piece

        Return:
            returns list of tuples with two integer coordinates in each tuple"""
        res = []
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        if (self.row == 1 or self.row == 6) and not self.moved:
            r2 = self.row + 5 * self.direction
            c = self.col
            if self.is_vailid_pos(r2, c):
                res.append((r2, c))
        
        for dir_row, dir_col in directions:              
            for mul in range(1, 3): 
                r1 = self.row + mul * dir_row
                c1 = self.col + mul * dir_col
                if not self.is_vailid_pos(r1, c1):
                    break
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    if figure.side == self.side:
                        break
                res.append((r1, c1))
                if figure is not None:
                    break
        return res


class Princess(Piece):
    """Child Class for Princess Piece"""
    def __init__(self, img, row, col, side, board):
        """Refers to parential class Piece """
        Piece.__init__(self, img, row, col, side, board)

    def __str__(self):
        """ 'Magic' method , represents piece on field
        Return:
            returns str value side + image of piece"""
        return self.side + self.img

    def get_moves(self):
        """function to determine available positions for piece

        Return:
            returns list of tuples with two integer coordinates in each tuple"""
        res = []
        directions = ((-2, 0), (0, 2), (2, 0), (0, -2), (-2, 2), (2, 2), (2, -2), (-2, -2))
        for dir_row, dir_col in directions:
            mul = 0
            while True:
                mul += 1
                r1 = self.row + mul * dir_row
                c1 = self.col + mul * dir_col
                if not self.is_vailid_pos(r1, c1):
                    break
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    if figure.side == self.side:
                        break
                res.append((r1, c1))
                if figure is not None:
                    break

        return res


class Checker(Piece):
    """Child Class for Checker Piece for checkers game"""

    def __init__(self, img, row, col, side, board):
        """Refers to parential class Piece """
        Piece.__init__(self, img, row, col, side, board)

    def __str__(self):
        """ 'Magic' method , represents piece on field
        Return:
            returns str value side + image of piece"""
        return self.side + self.img

    def get_moves(self):
        """function to determine available positions for piece

        Return:
            returns list of tuples with two integer coordinates in each tuple"""
        res = []
        directions = ((-1, 1), (1, 1), (1, -1), (-1, -1))

        for dir_row, dir_col in directions:
            r1 = self.row + dir_row
            c1 = self.col + dir_col
            if not self.is_vailid_pos(r1, c1):
                continue
            figure = self.board.get_figure(r1, c1)

            if figure is not None:
                if figure.side == self.side:
                    continue
                if not self.is_vailid_pos(r1 + dir_row, c1 + dir_col):
                    continue
                if self.is_vailid_pos(r1 + dir_row, c1 + dir_col):
                    if self.board.get_figure(r1 + dir_row, c1 + dir_col) is not None:
                        continue
                    else:
                        res.append((r1 + dir_row, c1 + dir_col))

            else:
                res.append((r1, c1))

        return res


class KingChecker(Piece):
    """Child Class for Checker Piece for checkers game"""

    def __init__(self, img, row, col, side, board):
        """Refers to parential class Piece """
        Piece.__init__(self, img, row, col, side, board)

    def __str__(self):
        """ 'Magic' method , represents piece on field
        Return:
            returns str value side + image of piece"""
        return self.side + self.img

    def get_moves(self):
        """function to determine available positions for piece

        Return:
            returns list of tuples with two integer coordinates in each tuple"""
        res = []
        directions = ((-1, 1), (1, 1), (1, -1), (-1, -1))

        for dir_row, dir_col in directions:
            mul = 0
            while True:
                mul += 1
                r1 = self.row + mul * dir_row
                c1 = self.col + mul * dir_col
                if not self.is_vailid_pos(r1, c1):
                    break
                figure = self.board.get_figure(r1, c1)

                if figure is not None:
                    if not self.is_vailid_pos(r1 + dir_row, c1 + dir_col):
                        break
                    else:
                        if not self.is_vailid_pos(r1 + dir_row * mul, c1 + dir_col * mul):
                            if self.board.get_figure(r1 + dir_row * mul, c1 + dir_col * mul) is not None:
                                continue

                else:
                    res.append((r1, c1))

        return res

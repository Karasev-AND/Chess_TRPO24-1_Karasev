from Figures import *

WHITE = 'w'
BLACK = 'b'

side_dct = {0: 'w', 1: 'b'}
opposite = {'w': 'b', 'b': 'w'}


class MoveNotation(object):
    """Move notation class for writing game moves and returning back"""
    def __init__(self):
        """initialisation of notation

        Attributes:
            notation(list): contains list of tuples
            (figure that moved, row, col, :(eated), figure that was eaten or a str cell, new row , new col)"""
        self.notation = []

    def write(self, figure, nr, nc, eaten):
        """Adds notes to notation
        Args:
            figure(Piece, King, Queen ...): figure started move
            nr(int): new row of figure
            nc(int): new col of figure
            eaten(Piece, King, Queen ... , str): piece eaten or cell on new coordinates
            """
        if eaten is not None:
            self.notation.append((figure, figure.row, figure.col, ':', eaten, nr, nc))
        else:
            self.notation.append((figure, figure.row, figure.col, '-', '__', nr, nc))

    def rewind(self, board, steps):
        """Function responsible for getting back in game

         Args:
             board(Board):
             steps(int): the amount of steps to return in notation
             """
        if steps > len(self.notation) or steps <= 0:
            print('Нельзя откатить дальше нуля')
            return None
        for ind in range(steps):
            figure, row, col, blank, eaten, n_row, n_col = self.notation.pop()
            board.cells[row][col] = type(figure)(figure.img, row, col, figure.side, board)
            board.cells[n_row][n_col] = eaten if eaten == '__' else type(eaten)(eaten.img, n_row, n_col, eaten.side, board)
        return None


class Board:
    """Board class for checkers game"""
    def __init__(self):
        """Initialization of Board

            Attributes:
                plw_figures(list):list for access to player figures
                plb_figures(list):list for access to player figures
                cols(list): list for drawing board borders
                rows(list): list for drawing board borders
                cells(list): list of lists - interpretation of game field
        """
        self.plw_figures = []
        self.plb_figures = []
        self.cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.rows = [str(i) + '' for i in range(1, 9)]
        self.figures_dict = {WHITE: self.plw_figures, BLACK: self.plb_figures}
        self.kings_dict = {}
        self.w_king = King('K', 0, 3, WHITE, self)
        self.kings_dict[WHITE] = self.w_king
        self.plw_figures.append(self.w_king)
        self.plw_figures.append(Queen('Q', 0, 4, WHITE, self))
        self.plw_figures.append(Rook('R', 0, 0, WHITE, self))
        self.plw_figures.append(Rook('R', 0, 7, WHITE, self))
        self.plw_figures.append(Knight('N', 0, 1, WHITE, self))
        self.plw_figures.append(Knight('N', 0, 6, WHITE, self))
        self.plw_figures.append(Bishop('B', 0, 2, WHITE, self))
        self.plw_figures.append(Princess('L', 0, 5, WHITE, self))
        self.plw_figures.append(Xman('X', 1, 0, WHITE, self))
        self.plw_figures.append(Missile('M', 1, 7, WHITE, self))
        for i in range(1, 7):
            self.plw_figures.append(Pawn('P', 1, i, WHITE, self))
        self.b_king = King('K', 7, 4, BLACK, self)
        self.kings_dict[BLACK] = self.b_king
        self.plb_figures.append(self.b_king)
        self.plb_figures.append(Queen('Q', 7, 3, BLACK, self))
        self.plb_figures.append(Rook('R', 7, 0, BLACK, self))
        self.plb_figures.append(Rook('R', 7, 7, BLACK, self))
        self.plb_figures.append(Knight('N', 7, 1, BLACK, self))
        self.plb_figures.append(Knight('N', 7, 6, BLACK, self))
        self.plb_figures.append(Bishop('B', 7, 2, BLACK, self))
        self.plb_figures.append(Princess('L', 7, 5, BLACK, self))
        self.plb_figures.append(Missile('M', 6, 0, BLACK, self))
        self.plb_figures.append(Xman('X', 6, 7, BLACK, self))
        for i in range(1, 7):
            self.plb_figures.append(Pawn('P', 6, i, BLACK, self))
        self.cells = []
        for i in range(0, 8):
            self.cells.append(['__'] * 8)
        for figure in (self.plb_figures + self.plw_figures):
            self.cells[figure.row][figure.col] = figure

    def get_figure(self, row, col):
        """retrieves figure from board if figure is there
                Args:
                    row(int):coordinate of position to retrieve
                    col(int):coordinate of position to retrieve
                Return:
                    returns None type value or child class of Piece
        """
        if self.cells[row][col] == '__':
            return None
        else:
            return self.cells[row][col]

    def print_field(self):
        """prints image of field in console
                Return:
                     returns None"""
        print('   ', end='')
        for i in range(8):
            print(self.cols[i], end='    ')
        print('')

        for i in range(8):
            print(self.rows[7 - i], end='  ')
            for j in range(8):
                print(str(self.cells[7 - i][j]), end='   ')
            print(self.rows[7 - i])
        print('   ', end='')

        for i in range(8):
            print(self.cols[i], end='    ')
        print('')

    def print_avl_moves(self, move_list):
        """prints image of field in console with available moves
                Return:
                     returns None"""
        image = [[str(x) for x in self.cells[j]] for j in range(8)]
        for row, col in move_list:
            target = self.get_figure(row, col)
            if not target:
                image[row][col] = '{}'
            else:
                image[row][col] = str(target).lower()
        print('   ', end='')
        for i in range(8):
            print(self.cols[i], end='    ')
        print('')
        for i in range(8):
            print(self.rows[7 - i], end='  ')
            for j in range(8):
                print(str(image[7 - i][j]), end='   ')
            print(self.rows[7 - i])
        print('   ', end='')

        for i in range(8):
            print(self.cols[i], end='    ')
        print('')

    def is_strike_cell(self, row, col, side):
        """Function determines if selected cell is under attack of opponent
        Args:
            row(int): coordinate of attacked cell
            col(int): coordinate of attacked cell
            side(str):'w' or 'b' to determine for which side is under attack
        Return:
            returns True or False value"""
        work_list = self.figures_dict[side]
        for figure in work_list:
            if figure.is_drop:
                continue
            figure_type = type(figure)
            if figure_type == Pawn:
                actions = figure.get_moves(PAWN_TAKES)
            else:
                actions = figure.get_moves()
            for r, c in actions:
                if r == row and c == col:
                    return True
        return False

    def make_move(self, piece, new_r, new_c):
        """Makes moves on game field
                Args:
                    piece(Piece):figure that makes move
                    new_r(int):coordinate of position to move on
                    new_c(int):coordinate of position to move on
                Return:
                    returns None
                    """

        if type(piece) in (Rook, King, Missile):
            piece.moved = True

        self.cells[new_r][new_c] = piece
        self.cells[piece.row][piece.col] = '__'
        piece.row = new_r
        piece.col = new_c



from Figures import *

side_dct = {0: 'w', 1: 'b'}
opposite = {'w': 'b', 'b': 'w'}


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

        for i in range(3):
            for j in range(8):
                if (i + j) % 2 == 0:
                    self.plw_figures.append(Checker('C', i, j, 'w', self))
        for i in range(5, 8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    self.plb_figures.append(Checker('C', i, j, 'b', self))

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

    def make_move(self, piece, new_r, new_c):
        """Makes moves on game field
        Args:
            piece(Piece):figure that makes move
            new_r(int):coordinate of position to move on
            new_c(int):coordinate of position to move on
        Return:
            returns None
            """

        moves = piece.get_moves()
        finish = {'w': 7, 'b': 0}

        if (new_r, new_c) in moves:
            dir_c = (new_r - piece.row) // abs(new_r - piece.row)
            dir_r = (new_c - piece.col) // abs(new_c - piece.col)
            eaten_figs = [self.get_figure(piece.row + dir_r * i, piece.col + dir_c * i) for i \
                          in range(1, min(abs(new_r - piece.row), abs(new_c - piece.col))) if Piece.is_vailid_pos(i, i)]
            eaten = [x for x in eaten_figs if x is not None]
            if eaten:
                for p in eaten:
                    p.is_drop = True
                    self.cells[p.row][p.col] = '__'
                self.cells[piece.row][piece.col] = '__'
                piece.row = new_r
                piece.col = new_c
                self.cells[new_r][new_c] = piece
            else:
                self.cells[piece.row][piece.col] = '__'
                piece.row = new_r
                piece.col = new_c
                self.cells[new_r][new_c] = piece
            if new_r == finish[piece.side]:
                self.cells[new_r][new_c] = KingChecker('D', new_r, new_c, piece.side, self)

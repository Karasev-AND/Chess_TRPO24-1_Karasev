from Checker_field import *

avl_moves = []
step_c = 0

board = Board()


def start():
    global board, step_c, avl_moves
    col_conw = {r: ind for r, ind in zip(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], range(8))}
    row_conw = {c: ind for c, ind in zip([str(i) + '' for i in range(1, 9)], range(8))}
    side_dct = {0: 'w', 1: 'b'}

    while True:
        board.print_field()
        events = input('Введите значение клетки хода или команду quit:')
        if 'quit' in events:
            print('end')
            return None
        else:
            col, row = events.split(' ')
            if row not in row_conw.keys() or col not in col_conw.keys():
                continue
            row = row_conw[row]
            col = col_conw[col]
            figure = board.get_figure(row, col)
            if figure is None:
                print('Вы выбрали пустую клетку')
                continue
            if figure is not None:
                if side_dct[step_c % 2] != figure.side:
                    print('Вы выбрали не свою фигуру и/или сейчас не ваш ход')
                    continue
                avl_moves = figure.get_moves()
                if avl_moves:
                    board.print_avl_moves(avl_moves)
                    step_2 = input('Введите новые координаты:')
                    sel_col, sel_row = step_2.split()
                    sel_row = row_conw[sel_row]
                    sel_col = col_conw[sel_col]
                    if (sel_row, sel_col) in avl_moves:
                        board.make_move(figure, sel_row, sel_col)
                    else:
                        print('there must be avaliable moves')
                        continue

        if all(x.is_drop is True for x in board.plw_figures):
            print(f'{side_dct[step_c % 2]} Победил')
            return None
        elif all(x.is_drop is True for x in board.plb_figures):
            print(f'{side_dct[step_c % 2]} Победил')

            return None
        step_c += 1
        avl_moves = []


start()

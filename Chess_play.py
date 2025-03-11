from Field import *


MAT = 'mat'
PAT = 'pat'
avl_moves = []
shah_flag = False
step_c = 0
notation = MoveNotation()


def start():
    global board, step_c, avl_moves, shah_flag
    col_conw = {r: ind for r, ind in zip(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], range(8))}
    row_conw = {c: ind for c, ind in zip([str(i) + '' for i in range(1, 9)], range(8))}
    side_dct = {0: 'w', 1: 'b'}
    board = Board()
    while True:
        board.print_field()
        print('Команды: quit - выход из игры, back n - откат ходов на n назад')
        events = input(f'Введите значение клетки хода для игрока {side_dct[step_c % 2]} или команду:')
        if 'quit' in events:
            print('end')
            return None
        elif 'back' in events:
            try:
                com, steps = events.split()
                steps = int(steps)
            except(ValueError):
                continue

            notation.rewind(board, steps)
            step_c -= steps % 2
            continue

        else:
            try:
                col, row = events.split(' ')
            except(ValueError):
                continue
            if row not in row_conw.keys() or col not in col_conw.keys():
                print('Надо ввести поля шахмат')
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
                        notation.write(figure, sel_row, sel_col, board.get_figure(sel_row, sel_col))
                        board.make_move(figure, sel_row, sel_col)
                    else:
                        print('Вы сходили не по правилам')
                        continue
                else:
                    print('Должны быть доступные ходы')
                    continue

        game_over = check_game_over(side_dct[step_c % 2])
        if game_over == MAT:
            print(f'{side_dct[step_c % 2]} Победил')
            return None
        if game_over == PAT:
            print('Ничья')
            return None
        if shah_flag is True:
            print('Закройте короля')
            notation.rewind(board, 1)
            continue
        step_c += 1
        avl_moves = []


def check_game_over(side):
    """function counts possible moves and returns game over type
    Args:
        side(str): 'w' or 'b' str value to determine for which side to check"""
    opposite = {'w': 'b', 'b': 'w'}
    king = board.kings_dict[side]
    row = king.row
    col = king.col
    sh_flag = board.is_strike_cell(row, col, opposite[side])
    moves = king.get_moves()
    avl_flag = False
    for n_row, n_col in moves:
        if board.is_strike_cell(n_row, n_col, opposite[side]):
            avl_flag = True
            break
        else:
            avl_flag = False
    if avl_flag and sh_flag:
        return MAT
    if avl_flag and not sh_flag:
        return PAT
    return None


start()

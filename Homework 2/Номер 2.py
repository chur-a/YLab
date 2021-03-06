from random import choice


def create_board():
    row = []
    for n in range(1, 101):
        CONTINUE_SQUARES.add(n)
        row.append(str(n).zfill(2))
        if len(row) == 10:
            MATRIX.append(row)
            row = []


def print_board():
    for r in MATRIX:
        print(' | '.join(r))


def player_input():
    print_board()
    input_square = input("Введите номер клетки, куда вы хотите поставить 'X': ")
    while True:
        try:
            input_square = int(input_square)
            if input_square % 10:
                i_player, j_player = input_square//10, input_square - input_square//10*10 - 1
            else:
                i_player, j_player = input_square//10 - 1, input_square - input_square//10*10 - 1
            if input_square < 1 or input_square > 100 or MATRIX[i_player][j_player] in 'X O ':
                raise ValueError
            MATRIX[i_player][j_player] = 'X '
            CONTINUE_SQUARES.discard(input_square)
            LOOSING_SQUARES.discard(input_square)
            return i_player, j_player
        except ValueError:
            print_board()
            input_square = input("В данную клетку нельзя поставить 'X'.\n"
                                 "Введите номер клетки, куда вы хотите поставить 'X': ")


def computer_input():
    while True:
        square = (choice(list(CONTINUE_SQUARES)) if CONTINUE_SQUARES else choice(list(LOOSING_SQUARES)))   
        if square % 10:
            i_comp, j_comp = square//10, square - square//10*10 - 1
        else:
            i_comp, j_comp = square//10 - 1, square - square//10*10 - 1
        MATRIX[i_comp][j_comp] = 'O '
        check_l = check_lines(i_comp, j_comp)
        if not CONTINUE_SQUARES or all('O ' * 5 not in line for line in check_l):
            CONTINUE_SQUARES.discard(square)
            return i_comp, j_comp
        elif any('O ' * 5 in line for line in check_l):
            LOOSING_SQUARES.add(square)
            CONTINUE_SQUARES.remove(square)
            MATRIX[i_comp][j_comp] = str(square)

def diagonals(i, j):
    first_d = []
    second_d = []
    i_f, j_f = i - min(i, j), j - min(i, j)
    i_s, j_s = i - min(i, 9 - j), j + min(i, 9 - j)
    while i_f < 10 and j_f < 10:
        first_d.append(MATRIX[i_f][j_f])
        i_f += 1
        j_f += 1
    while i_s < 10 and j_s >= 0:
        second_d.append(MATRIX[i_s][j_s])
        i_s += 1
        j_s -= 1
    return first_d, second_d


def check_lines(i, j):
    first_d, second_d = diagonals(i, j)
    return [''.join(MATRIX[i]), ''.join(MATRIX[k][j] for k in range(9)),
            ''.join(first_d), ''.join(second_d)]

def check_end_game(i, j):
    first_d, second_d = diagonals(i, j)
    for check_str in [''.join(MATRIX[i]), ''.join(MATRIX[k][j] for k in range(9)),
                      ''.join(first_d), ''.join(second_d)]:
        if 'X ' * 5 in check_str:
            print_board()
            print('К сожалению вы проиграли')
            return True
        elif 'O ' * 5 in check_str:
            print_board()
            print('Поздравляем, вы победили!')
            return True
        

def check_tie():
    for raw in MATRIX:
        for i in range(len(raw)):
            if raw[i] not in 'X O ':
                return False
    print_board()
    print('Ничья')
    return True
        

MATRIX = []
CONTINUE_SQUARES = set()
LOOSING_SQUARES = set()
RUN_GAME = True
        
create_board()
while RUN_GAME:
    i_player, j_player = player_input()     
    i_comp, j_comp = computer_input()
    for i_check, j_check in [(i_player, j_player), (i_comp, j_comp)]:
        if check_end_game(i_check, j_check):
            RUN_GAME = False
    if check_tie():
        RUN_GAME = False
        
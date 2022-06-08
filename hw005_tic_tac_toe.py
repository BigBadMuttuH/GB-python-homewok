# игральная доска
boad = [' ' for _ in range(9)]
winnig_combinations = [(0, 1, 2),  # X | X | X
                       (3, 4, 5),  # X | X | X
                       (6, 7, 8),  # X | X | X
                       (0, 3, 6),  # 0 | 1 | 2
                       (1, 4, 7),  # 3 | 4 | 5
                       (2, 5, 8),  # 6 | 7 | 8
                       (0, 4, 8),
                       (2, 4, 6)]


def print_state(state):
    """вывод игральной достки на конслоль"""
    for i, c in enumerate(state):
        if (i + 1) % 3 == 0:
            print(f"{c}")
        else:
            print(f"{c} | ", end='')  # end='' без перехода на новую строку


def get_winner(state, combinations):
    """Определяем победителя"""
    for (x, y, z) in combinations:
        if state[x] == state[y] \
                and state[y] == state[z] \
                and (state[x] == 'X' or state[x] == 'O'):
            return state[x]
    return ""


def play_game(boad):
    """Сыграем в игру"""
    current_sign = 'X'
    while get_winner(boad, winnig_combinations) == '':
        index = int(input(f"Где рисуем-'{current_sign}' (0-8)?"))
        boad[index] = current_sign

        print_state(boad)

        winner_sign = get_winner(boad, winnig_combinations)
        if winner_sign != '':
            print(f"Победитель: {winner_sign}")

        current_sign = 'X' if current_sign == 'O' else 'O'


play_game(boad)

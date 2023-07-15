"""Модуль формирования координатной сетки шахматной доски 8 на 8 с вычислением взаимодействия пар ферзей"""


def get_queen_attacks(queen_pos):
    row, col = queen_pos
    attacks = []

    # Все координаты на той же строке
    attacks.extend([(row, c) for c in range(8) if c != col])
    # Все координаты на том же столбце
    attacks.extend([(r, col) for r in range(8) if r != row])
    # Все координаты на главной диагонали
    diff = min(row, col)
    attacks.extend([(row - diff + i, col - diff + i) for i in range(8) if 0 <= row - diff + i < 8 and 0 <= col - diff + i < 8 and (row - diff + i, col - diff + i) != (row, col)])
    # Все координаты на побочной диагонали
    diff = min(row, 7 - col)
    attacks.extend([(row - diff + i, col + diff - i) for i in range(8) if 0 <= row - diff + i < 8 and 0 <= col + diff - i < 8 and (row - diff + i, col + diff - i) != (row, col)])
    return attacks

def is_queen_attacking(queen1, queen2):
    queen1_attacks = set(queen1['attacks'])
    queen2_position = queen2['position']

    if queen2_position in queen1_attacks:
        return True
    else:
        return False
# проверка и выявление бьющих друг друга пар ферзей
def check_queen_pairs(queens):
    result = []

    for queen1_key, queen1_value in queens.items():
        for queen2_key, queen2_value in queens.items():
            if queen1_key < queen2_key:  # Изменение условия для исключения повторных пар
                if is_queen_attacking(queen1_value, queen2_value):
                    result.append(f"Ферзи бьют друг друга '{queen1_key}{queen1_value['position']}' VS '{queen2_key}{queen2_value['position']}'")
                else:
                    result.append(f"Ферзи не бьют друг друга '{queen1_key}{queen1_value['position']}' VS '{queen2_key}{queen2_value['position']}'")

    return result
def queen_valid_position(queens, row, col):
    for queen_row, queen_col in queens:
        if queen_row == row or queen_col == col or abs(queen_row - row) == abs(queen_col - col):
            return False
    return True

def place_queens(row, queens, results):
    if row == 8:
        results.append(list(queens))
    else:
        for col in range(8):
            if queen_valid_position(queens, row, col):
                queens.append((row, col))
                place_queens(row + 1, queens, results)
                queens.pop()


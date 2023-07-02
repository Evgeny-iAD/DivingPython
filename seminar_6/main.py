"""1. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8
ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
2. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче
выше. Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
*Выведите все успешные варианты расстановок"""

import random

from seminar_6.chess88.chess88operation import get_queen_attacks, check_queen_pairs, place_queens


def random_koord():
    row = random.randint(0, 7)
    col = random.randint(0, 7)
    return row, col


if __name__ == '__main__':
    queens = {}

    for i in range(8):
        queen = {}
        queen['position'] = random_koord()
        queen['attacks'] = get_queen_attacks(queen['position'])
        queens[f"queen_{i + 1}"] = queen

    # ЗАДАЧА 1 проверка и выявление бьющих друг друга пар ферзей
    result_chek = check_queen_pairs(queens)
    for result in result_chek:
        print(result)

    # ЗАДАЧА 2 с помощью рекурсивного метода
    results_position = []
    place_queens(0, [], results_position)

    for i, result in enumerate(results_position):
        print(i, result)



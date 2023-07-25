"""Напишите следующие функции:
* Нахождение корней квадратного уравнения
* Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
* Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
* Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл."""

import csv
import random
import json

# Декоратор для запуска функции find_roots с каждой тройкой чисел из CSV-файла
def find_roots_with_each_triple(func):
    def wrapper(filename):
        roots = []
        with open(filename, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                a, b, c = map(int, row)
                roots.append(func(a, b, c))
            return roots
    return wrapper

# Декоратор для сохранения результатов в JSON-файл
def save_to_json_decorator(func):
    def wrapper_to_json(filename, *args, **kwargs):
        result = func(filename, *args, **kwargs)
        data_dict = {}
        with open(filename, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for i, row in enumerate(csv_reader):
                data_dict[str(row)] = result[i]
        with open("results.json", 'w', encoding="utf-8") as json_file:
            json.dump(data_dict, json_file)
        return result
    return wrapper_to_json

# Функция для генерации CSV-файла
def generate_csv(filename, rows):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for _ in range(rows): # !!!!!!! "_" указывает на то, что нам не важно значение элементов, генерируемых в списке
            row = [random.randint(1, 1000) for _ in range(3)]
            csv_writer.writerow(row)

@save_to_json_decorator
@find_roots_with_each_triple
def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        root1 = (-b + (discriminant)**0.5) / (2*a)
        root2 = (-b - (discriminant)**0.5) / (2*a)
        return root1, root2


if __name__ == '__main__':
    # Генерируем CSV-файл
    generate_csv("random_numbers.csv", 100)

    # Запускаем функцию find_roots, передав обертке имя файла + сохраняем в json
    find_roots("random_numbers.csv")






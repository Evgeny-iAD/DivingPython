"""Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. Для тестированию
возьмите pickle версию файла из предыдущей задачи. Функция должна извлекать ключи словаря для заголовков столбца
из переданного файла."""

import pickle
import csv

def new_pickle():
    data = [
        {'name': 'Alice', 'age': 25, 'city': 'New York'},
        {'name': 'Bob', 'age': 30, 'city': 'London'},
        {'name': 'Charlie', 'age': 35, 'city': 'Paris'}
    ]
    # Сохраняем список словарей в pickle файл
    pickle_file = 'data.pickle'
    with open(pickle_file, 'wb') as f:
        pickle.dump(data, f)

    return pickle_file

def pickle_to_csv(pickle_file, csv_file):
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)

    if len(data) > 0:
        headers = list(data[0].keys())
    else:
        return

    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    pickle_file = new_pickle()
    csv_file = 'data.csv'
    pickle_to_csv(pickle_file, csv_file)


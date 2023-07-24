""" Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию.
 Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, а для директорий
 размер файлов в ней с учётом всех вложенных файлов и директорий. """

import os
import json
import csv
import pickle

def process_directory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        current_dir = os.path.abspath(root)
        dir_size = sum(
            os.path.getsize(os.path.join(dirpath, filename))
            for dirpath, _, filenames in os.walk(current_dir)
            for filename in filenames
        )

        result = {
            'type': 'directory',
            'path': current_dir,
            'size': dir_size,
            'parent_directory': os.path.dirname(current_dir)
        }
        results.append(result)

        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            result = {
                'type': 'file',
                'path': file_path,
                'size': file_size,
                'parent_directory': current_dir
            }
            results.append(result)

    json_file = 'result.json'
    with open(json_file, 'w') as f:
        json.dump(results, f, indent=4)

    csv_file = 'result.csv'
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['type', 'path', 'size', 'parent_directory'])
        writer.writeheader()
        writer.writerows(results)

    pickle_file = 'result.pickle'
    with open(pickle_file, 'wb') as f:
        pickle.dump(results, f)

    return json_file, csv_file, pickle_file



if __name__ == '__main__':
    directory = 'task_3'
    print("Результаты обхода сохранены в файлы:", process_directory(directory))

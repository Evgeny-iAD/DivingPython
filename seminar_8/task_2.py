"""Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Распечатайте его как pickle строку."""

import pickle
import csv

def read_csv_to_pickle(csv_file):
    data = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    pickle_data = pickle.dumps(data)
    return pickle_data

if __name__ == '__main__':
    csv_file = 'data.csv'
    pickle_data = read_csv_to_pickle(csv_file)
    print(pickle_data)
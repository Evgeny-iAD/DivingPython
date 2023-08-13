import os
import logging
from collections import namedtuple
import sys

# Конфигурация логирования
logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Создание объекта namedtuple для хранения информации о файле/каталоге
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_file_info(path):
    items = os.listdir(path)
    for item in items:
        full_path = os.path.join(path, item)
        is_directory = os.path.isdir(full_path)
        if is_directory:
            extension = None
        else:
            _, extension = os.path.splitext(item)
        parent_directory = os.path.basename(path)
        file_info = FileInfo(name=item, extension=extension, is_directory=is_directory, parent_directory=parent_directory)
        logging.info(file_info)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Запуск: python directory_info.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print("Недопустимый путь к каталогу")
        sys.exit(1)

    get_file_info(directory_path)

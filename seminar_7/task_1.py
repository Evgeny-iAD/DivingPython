"""1 — Напишите функцию группового переименования файлов. Она должна:
* принимать в качестве аргумента желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
* принимать в качестве аргумента расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
* принимать в качестве аргумента расширение конечного файла.
Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>"""

import os

def group_rename_files(new_name, source_extension, new_extension):
    directory = os.path.join(os.getcwd(), ".task_1_file")

    if not os.path.isdir(directory):
        print("Указанная директория не существует.")
        return

    for filename in os.listdir(directory):
        if filename.endswith(source_extension):
            file_name, file_ext = os.path.splitext(filename)
            new_file_name = f"{file_name}_{new_name}_{len(os.listdir(directory))}.{new_extension}"

            if not os.path.exists(os.path.join(directory, new_file_name)):
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_file_name))
                print(f"Файл {filename} переименован в {new_file_name}")
            else:
                print(f"Файл {new_file_name} уже существует. Переименование не выполнено.")

if __name__ == '__main__':
    group_rename_files("new_name", ".txt", "csv")


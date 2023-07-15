"""Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла"""

def parse_file_path(file_path):
    path, filename = file_path.rsplit('/', 1)
    name, extension = filename.split('.', 1)
    return path, name, '.' + extension

if __name__ == '__main__':
    file_path = "H:/II/CheXNet-master/ChestX-ray14/images/images_work/uploaded_image.png"
    path, name, extension = parse_file_path(file_path)
    print(f"Путь к изображению: {path} \nИмя файла: {name} \nРасширение: {extension}")


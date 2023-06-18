#  Программа загадывает число от 0 до 1000.
from random import randint

def operationNum(i, number, numberResult):
    if i == 9:
        return f"Джон Крамер: 'Ошибки делают нас людьми. Но цена за ошибку - это учение. Вы проиграли!'\n"
    elif number < numberResult:
        return f"Джон Крамер: 'Попытка №{i+1}. Ваше число меньше загаданного!'\n"
    elif number > numberResult:
        return f"Джон Крамер: 'Попытка №{i+1}. Ваше число больше загаданного!'\n"


def checkNumber(number, lower, upper):
    try:
        if float(number) < lower:
            return f"Джон Крамер: 'Cмотрите подсказку!'"

        elif float(number) > upper >= 6:
            return f"Джон Крамер: 'Узрите подсказку!'"
    except ValueError:
        return f"Джон Крамер: 'Я хочу, чтобы играли по моим правилам!'"

if __name__ == '__main__':
    while True:
        LOWER_LIMIT = 0
        UPPER_LIMIT = 1000
        numberResult = randint(LOWER_LIMIT, UPPER_LIMIT)
        print(numberResult)
        for i in range(10):
            number = input(f"Джон Крамер: 'Играйте или погибните! Угадайте число! (подсказка: оно в пределах от {LOWER_LIMIT} до {UPPER_LIMIT})' ==> ")
            number = number.replace(" ", "")
            checkResult = checkNumber(number, LOWER_LIMIT, UPPER_LIMIT)
            if checkResult is not None:
                print(f"{checkResult}")
                break
            if operationNum(i, float(number), numberResult) is not None:
                print(operationNum(i, float(number), numberResult))
            else:
                print(f"Джон Крамер: 'Попытка №{i+1}. Все, что я делаю, направлено на то, чтобы вам показать цену жизни. Вы угадали!'\n")
                break




        # Пример условия для выхода из цикла
        answer = input("Еще разочек? (да/нет): ")
        if answer.lower() == "нет":
            break


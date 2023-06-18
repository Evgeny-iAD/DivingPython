# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
import math

def isPrime(number):
    if number < 2:
        return f"Число противоречит условию."
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return f"Введенное число составное"
    return f"Введенное число простое"

def checkNumber(number):
    try:
        if int(number) < 0:
            return f"Вы ввели отрицательное число, что противоречит условию."
        else:
            if len(str(int(number))) >= 6:
                return f"Вы ввели число превышающее 100 000."
    except ValueError:
        return f"Число ли Вы ввели?"

if __name__ == '__main__':
    while True:
        number = input(f"Введите любое число от 2 до 100 000: ")
        number = number.replace(" ", "")
        if checkNumber(number) == None:
            print(isPrime(int(number)))
        else:
            print(f"{checkNumber(number)}")

        # Пример условия для выхода из цикла
        answer = input("Еще разочек? (да/нет): ")
        if answer.lower() == "нет":
            break


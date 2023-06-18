def checkNumber(number):
    try:
        value = int(number)
    except ValueError:
        return f"Число ли Вы ввели?"

def hexadecimal(number):
    result = ''
    if number == 0:
        result = '0'
    else:
        while number > 0:
            remainder = number % 16
            if remainder < 10:
                result = str(remainder) + result
            else:
                result = chr(remainder + 55) + result
            number //= 16
    return result



if __name__ == '__main__':
    while True:
        number = input("Введите целое число без пробелов: ")
        if checkNumber(number) == None:
            print(f"Шестнадцатеричное представление:{hexadecimal(int(number))}")
            print(f"Проверка с помощью hex: {hex(int(number))[2:].upper()}")
        else:
            print(f"{checkNumber(number)}")

        # Пример условия для выхода из цикла
        answer = input("Еще разочек? (да/нет): ")
        if answer.lower() == "нет":
            break






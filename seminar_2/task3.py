"""Напишите программу, которая принимает две строки вида “a/b”
   - дробь с числителем и знаменателем. Программа должна возвращать сумму и
   произведение* дробей. Для проверки своего кода используйте модуль fractions."""
from fractions import Fraction

def checkNumber(number):
    try:
        value = Fraction(number)
        return number
    except ValueError:
        return None
    except ZeroDivisionError:
        return None
def fractionOperation(fraction1, fraction2):
    # Разделение числителя и знаменателя
    num1, den1 = map(int, fraction1.split('/'))
    num2, den2 = map(int, fraction2.split('/'))

    sum_num = num1 * den2 + num2 * den1
    sum_den = den1 * den2

    # Вычисление произведения дробей
    prod_num = num1 * num2
    prod_den = den1 * den2

    sumFraction = f"{sum_num}/{sum_den}"
    prodFraction = f"{prod_num}/{prod_den}"

    return sumFraction, prodFraction

if __name__ == '__main__':
    while True:
        number1 = checkNumber(input("Введите первое число вида a/b: "))
        number2 = checkNumber(input("Введите второе число вида a/b: "))

        if number2 and number1:
            sumFraction, prodFraction = fractionOperation(number1, number2)
            print(f"Результаты такие: сумма - {sumFraction}; произведение - {prodFraction}")

            sumFrac = Fraction(number1) + Fraction(number2)
            prodFrac = Fraction(number1) * Fraction(number2)
            print(f"Через функцию fraction результаты такие: сумма - {sumFrac}; произведение - {prodFrac}")
        else:
            print("Ошибка ввода дробей!")

        answer = input("Еще разочек? (да/нет): ")
        if answer.lower() == "нет":
            break


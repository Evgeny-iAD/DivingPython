"""Создайте функцию генератор чисел Фибоначчи"""


fibonacci_generator = (lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args))))(lambda f: lambda n: 0 if n == 0 else (1 if n == 1 else f(n - 1) + f(n - 2)))

for i in range(15):
    print(fibonacci_generator(i))
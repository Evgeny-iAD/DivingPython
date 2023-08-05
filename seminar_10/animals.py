
class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

class Fish(Animals):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def swim(self):
        return f"{self.name} плавает грациозно."

    def info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Вид: {self.species}"

class Bird(Animals):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def fly(self):
        return f"{self.name} летит высоко в небе."

    def info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Размах крыльев: {self.wingspan}"

class Mammal(Animals):
    def __init__(self, name, age, habitat):
        super().__init__(name, age)
        self.habitat = habitat

    def speak(self, speak):
        return f"{self.name} говорит {speak}"

    def info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Среда обитания: {self.habitat}"


# # Пример использования классов:
# if __name__ == "__main__":
#     fish1 = Fish("Немо", 2, "Рыба-клоун")
#     print(f"Информация об объекте исследования: {fish1.info()}. \n                         Специфика: {fish1.swim()}" )
#
#     bird1 = Bird("Орёл", 5, "2 метра")
#     print(f"Информация об объекте исследования: {bird1.info()}. \n                         Специфика: {bird1.fly()}" )
#
#     mammal1 = Mammal("Тигр", 7, "Джунгли")
#     print(f"Информация об объекте исследования: {mammal1.info()}. \n                         Специфика: {mammal1.speak()}" )



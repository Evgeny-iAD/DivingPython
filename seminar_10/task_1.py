from seminar_10.animals import Fish, Bird, Mammal

class AnimalFactory:

    def create_animal(self, animal_type, name, age, **kwargs):
        if animal_type == "Рыба":
            return Fish(name, age, **kwargs)
        elif animal_type == "Птица":
            return Bird(name, age, **kwargs)
        elif animal_type == "Млекопитающее":
            return Mammal(name, age, **kwargs)
        else:
            raise ValueError("Введен неправильный тип животного.")


# Пример использования классов:
if __name__ == "__main__":
    animal_factory = AnimalFactory()
    animal1 = animal_factory.create_animal("Рыба", "Рыба-клоун", 2, species="Полосатый")
    print(f"Информация об объекте исследования: {animal1.info()}. \n                         Специфика: {animal1.swim()}" )

    animal2 = animal_factory.create_animal("Птица", "Орёл", 5, wingspan="2 метра")
    print(f"Информация об объекте исследования: {animal2.info()}. \n                         Специфика: {animal2.fly()}" )

    animal3 = animal_factory.create_animal("Млекопитающее", "Котэ", 7, habitat="Комнатные джунгли")
    print(f"Информация об объекте исследования: {animal3.info()}. \n                         Специфика: {animal3.speak('мур мяу')}" )



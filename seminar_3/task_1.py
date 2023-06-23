"""Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
1) Какие вещи взяли все три друга

2) Какие вещи уникальны, есть только у одного друга и имя этого друга

3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей."""


def format_things_print(things):
    result = ''
    for i, element in enumerate(things):
        result += f" {element}"
        result += ",\n" if i % 5 == 0 else ", "
    return result[:-2]

def question_1(input_data):
    things = []
    for man in input_data:
        for element in input_data[man]:
            if not element in things:
                things.append(element)
    return things

def question_2(input_data, things):
    man_unique = []
    list_mans = input_data.keys()
    for element in things:
        buffer_man = {}
        for man in list_mans:
            if element in input_data[man]: buffer_man[man] = [element]
        # print(buffer_man)
        man_unique.append(buffer_man) if len(buffer_man) == 1 else ''
    return man_unique

def question_3(input_data, things):
    things_un_unique =[]
    man_unique = []
    list_mans = input_data.keys()
    for element in things:
        buffer_man = {}
        for man in list_mans:
            if element in input_data[man]:
                buffer_man[man] = [element]
        # print(buffer_man)
        man_unique.append(buffer_man) if len(buffer_man) == (len(input_data)-1) else ''
    return man_unique

if __name__ == '__main__':
    input_data = {'Василий':('рюкзак','спички','салфетки','котелок','гитара','спальник','горелка','паек','дождевик'),
                  'Петр': ( 'рюкзак', 'спички', 'туалетная бумага', 'котелок', 'укулеле', 'спальник', 'паек', 'дождевик'),
                  'Максимка': ( 'рюкзак', 'спички', 'салфетки', 'котелок', 'горелка', 'паек', 'подруга'),
                  'Валера': ( 'рюкзак', 'зажигалка', 'туалетная бумага', 'котелок',  'спальник', 'паек', 'палатка')
                  }

    print('Исходные данные:')
    for i in input_data:
        print(i, input_data[i])
    print('\n')

    # question 1
    print("Ответ №1")
    things = question_1(input_data)
    print(f"Пацаны взяли следующие вещи в поход: {format_things_print(things)}.\n")

    # question 2
    print("Ответ №2")
    man_unique = question_2(input_data, things)
    for el in man_unique:
        frend = {}
        for key in el:
            print(f"Уникальные вещи товарища {key}: {format_things_print(el[key])}.")

    # question 3
    print('\n')
    print("Ответ №3")
    man_un_unique = question_3(input_data, things)
    all_man = input_data.keys()

    for el in man_un_unique:
        un_unique_man = el.keys()
        for man in all_man:
            if man in un_unique_man: thing = el[man]
            if not man in un_unique_man: person = man
        print(f"У этого товарища {person} нет того, что есть у других, а именно: {format_things_print(thing)}.")






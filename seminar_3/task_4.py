"""4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните
все возможные варианты комплектации рюкзака."""
import random

def calc_things(max, input_data):
    buffer_max = max
    result = {}
    keys = list(input_data.keys())
    random.shuffle(keys)
    for key in keys:
        if not key in result:
            if (buffer_max - input_data[key]) >= 0:
                result[key] = input_data[key]
                buffer_max = buffer_max - input_data[key]
    return result

if __name__ == '__main__':
    input_data = {'спички':0.08,
                  'салфетки':0.1,
                  'котелок':0.4,
                  'гитара':3.5,
                  'спальник':0.9,
                  'горелка':0.6,
                  'паек':3.2,
                  'дождевик':0.07,
                  'квадрокоптер с аккумуляторами и базой': 1.5,
                  'электронная книга': 0.3,
                  'пауэрбанк': 0.3,
                  'экшен-камера': 0.2,
                  'органайзер с лекарствами': 0.5,
                  'подруга': 55,
                  'палатка': 3.5,
                  'топор': 1.6,
                  'мачете': 0.8,
                  'велосипед': 20
                  }
    max = 61.0
    result = []
    option = 100
    for i in range(100):
        things = calc_things(max, input_data)
        if not things in result:
            result.append(things)
    for i in range(len(result)):
        print(f"\nВариант №{i}: вес {sum(result[i].values(), 2)} кг ")
        for element in result[i]:
            print(f"{element}: {result[i][element]}")




